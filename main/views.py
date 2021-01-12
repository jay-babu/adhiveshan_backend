import os
import csv
from collections import defaultdict
from os import getenv

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import status
from rest_framework.generics import GenericAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from main.serializers import UserSerializer, ChangePasswordSerializer
from . import constants
from . import models

DEFAULT_CACHE_TIMEOUT = 60 * 60 * 12  # 12 Hours


class RegisterView(GenericAPIView):
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = UserSerializer(data=request.data, context=request)

        if serializer.is_valid():
            serializer.save()
            instantiate_module_instances_for_user(models.User.objects.get(email=serializer.data.get('email')))
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def instantiate_module_instances_for_user(user):
    # Get relevant modules for the user, depending on whether they are BM or KM.
    relevant_modules = None
    if user.is_kishore_mandal():
        relevant_modules = models.Module.objects.filter(is_kishore_mandal=True)
    elif user.is_bal_mandal():
        relevant_modules = models.Module.objects.filter(is_bal_mandal=True)

    for module in relevant_modules:
        module_instance = models.ModuleInstance.objects.create(user=user, module=module)
        for item in module.mukhpath_items.all():
            models.MukhpathItemInstance.objects.create(
                mukhpath_item=item,
                module_instance=module_instance)


class OnboardedView(APIView):
    permission_classes = (IsAuthenticated,)

    def put(self, request):
        request.user.is_onboarded = request.data.get('is_onboarded')
        request.user.save()
        return Response(
            data={'is_onboarded': request.user.is_onboarded},
            status=status.HTTP_200_OK)


class HasWatchedTutorialView(APIView):
    permission_classes = (IsAuthenticated,)

    def put(self, request):
        request.user.has_watched_tutorial = request.data.get('has_watched_tutorial')
        request.user.save()
        return Response(
            data={'has_watched_tutorial': request.user.has_watched_tutorial},
            status=status.HTTP_200_OK)


class ChangePasswordView(UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer
    object = None

    def put(self, request, *args, **kwargs):
        serializer = ChangePasswordSerializer(data=request.data, context=self.request)

        if serializer.is_valid():
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'mukhpath_content_data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PledgeOptionsView(APIView):
    """Gets all the pledge options so that frontend can display them."""
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        response = constants.get_pledge_options(request.user.mandal.lower().replace(' ', '_'))
        return Response(data=response, status=status.HTTP_200_OK)


class MyPledgeView(APIView):
    """Endpoints for Pledge objects."""
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        # Checks if pledge object exists.
        if hasattr(request.user, 'pledge'):
            response = defaultdict(list)
            modules = response['modules']
            for pledged_module in request.user.pledge.pledged_modules.all():
                modules.append({
                    'title': pledged_module.module.title,
                    'tier': pledged_module.tier,
                    'required': constants.get_required_mukhpath_items(
                        pledged_module.module.title,
                        request.user.mandal.lower().replace(' ', '_'),
                        pledged_module.tier)
                })
            return Response(data=response, status=status.HTTP_200_OK)
        else:
            return Response(data={},
                            status=status.HTTP_200_OK)

    def put(self, request):
        """Sets or updates a pledge."""
        # Checks if pledge object exists. If so, update.
        if hasattr(request.user, 'pledge'):
            request.user.pledge.pledged_modules.all().delete()
            pledge = request.user.pledge
        # If not, create new pledge object.
        else:
            pledge = models.Pledge.objects.create(user=request.user)

        for module in request.data['modules']:
            models.PledgedModule.objects.create(
                pledge=pledge,
                module=models.Module.objects.get(title=module['title']),
                tier=module['tier'])

            # If pledged module is satsang diksha, bookmark all items.
            if module['title'] == constants.SATSANG_DIKSHA:
                module_instance = request.user.module_instances.get(module__title=constants.SATSANG_DIKSHA)
                for mukhpath_item_instance in module_instance.mukhpath_item_instances.all():
                    mukhpath_item_instance.is_bookmarked = True
                    mukhpath_item_instance.save()

        return Response(data=request.data,
                        status=status.HTTP_201_CREATED)


class DashboardView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        # Checks if pledge object exists.
        if request.user.is_bal_mandal():
            return get_bal_mandal_dashboard_view(request.user)
        elif request.user.is_kishore_mandal():
            return get_kishore_mandal_dashboard_view(request.user)


def get_bal_mandal_dashboard_view(user):
    response = defaultdict(list)
    modules = response['modules']
    for pledged_module in user.pledge.pledged_modules.all():
        module_instance = models.ModuleInstance.objects.get(
            user=user,
            module=pledged_module.module)
        modules.append({
            'title': pledged_module.module.title,
            'tier': pledged_module.tier,
            'required': constants.get_required_mukhpath_items(
                pledged_module.module.title,
                user.mandal.lower().replace(' ', '_'),
                pledged_module.tier),
            'memorized': get_num_of_items_memorized(module_instance)
        })
    return Response(data=response, status=status.HTTP_200_OK)


def get_kishore_mandal_dashboard_view(user):
    response = defaultdict(list)
    modules = response['modules']
    for pledged_module in user.pledge.pledged_modules.all():
        if pledged_module.module.title == constants.SATSANG_DIKSHA:
            module_instance = models.ModuleInstance.objects.get(
                user=user,
                module=pledged_module.module)
            modules.append({
                'title': pledged_module.module.title,
                'tier': pledged_module.tier,
                'required': constants.get_required_mukhpath_items(
                    pledged_module.module.title,
                    user.mandal.lower().replace(' ', '_'),
                    pledged_module.tier),
                'memorized': get_num_of_items_memorized(module_instance)
            })

    # For module in all user module instances except for SATSANG DIKSHA and KM_MODULES
    # If is one bookmarked, show that
    # Set required as constant value.
    for module_instance in user.module_instances.all():
        if module_instance.module.title in (constants.SATSANG_DIKSHA, constants.KM_MODULES):
            continue
        if module_instance.mukhpath_item_instances.filter(is_bookmarked=True).count() > 0:
            modules.append({
                'title': module_instance.module.title,
                'required': constants.REQUIRED_PER_KM_MODULE,
                'memorized': get_num_of_items_memorized(module_instance)
            })
    # Get all modules that the user has added bookmarks too.
    return Response(data=response, status=status.HTTP_200_OK)


def get_num_of_items_memorized(module_instance):
    return module_instance.mukhpath_item_instances.filter(is_memorized=True).count()


class AccessAllowedView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request: Request):
        if request.data.get('ADHIVESHAN_ACCESS_CODE', '') == getenv('ADHIVESHAN_ACCESS_CODE'):
            return Response({'access_allowed': True}, status=status.HTTP_200_OK)
        return Response({'access_allowed': False}, status=status.HTTP_401_UNAUTHORIZED)


class AllMukhpathItemsView(APIView):
    permission_classes = (IsAuthenticated,)

    @method_decorator(cache_page(DEFAULT_CACHE_TIMEOUT))
    def get(self, request):
        return Response(data=get_modules(user=request.user), status=status.HTTP_200_OK)


class BookmarkedMukhpathItemsView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        return Response(
            data=get_modules(user=request.user, bookmarked_only=True),
            status=status.HTTP_200_OK)


def get_modules(user, bookmarked_only=False):
    response = {}
    has_pledged_for_satsang_diksha = user.pledge.pledged_modules.filter(
        module__title=constants.SATSANG_DIKSHA).count() > 0
    sd_tier = None
    if has_pledged_for_satsang_diksha:
        sd_tier = user.pledge.pledged_modules.get(module__title=constants.SATSANG_DIKSHA).tier

    for module_instance in user.module_instances.all():
        mukhpath_item_instances = []
        module_instance_is_sd = module_instance.module.title == constants.SATSANG_DIKSHA
        for mukhpath_item_instance in module_instance.mukhpath_item_instances.all():
            if bookmarked_only and not mukhpath_item_instance.is_bookmarked and not module_instance_is_sd:
                continue

            if module_instance_is_sd and has_pledged_for_satsang_diksha:
                is_item_in_sd_tier = mukhpath_item_instance.mukhpath_item.title in constants.SD_SHLOKS_FOR_TIER[sd_tier]
                if not is_item_in_sd_tier:
                    continue

            mukhpath_item_instance_dict = {
                'id': mukhpath_item_instance.id,
                'title': mukhpath_item_instance.mukhpath_item.title,
                'english_content': mukhpath_item_instance.mukhpath_item.english_content,
                'gujurati_content': mukhpath_item_instance.mukhpath_item.gujurati_content,
                'transliteration_content': mukhpath_item_instance.mukhpath_item.transliteration_content,
                'audio_url': mukhpath_item_instance.mukhpath_item.audio_url,
                'is_memorized': mukhpath_item_instance.is_memorized,
                'is_bookmarked': mukhpath_item_instance.is_bookmarked,
                'value': mukhpath_item_instance.mukhpath_item.value,
            }
            mukhpath_item_instances.append(mukhpath_item_instance_dict)

        if len(mukhpath_item_instances) > 0:
            response[module_instance.module.title] = mukhpath_item_instances
    return response


class MukhpathItemInstanceView(APIView):
    """Endpoints for MukhpathItemInstances objects."""
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        mukhpath_item_instance = models.MukhpathItemInstance.objects.get(id=request.data['id'])
        mukhpath_item_instance.is_memorized = request.data.get('is_memorized', mukhpath_item_instance.is_memorized)
        mukhpath_item_instance.is_bookmarked = request.data.get('is_bookmarked', mukhpath_item_instance.is_bookmarked)

        mukhpath_item_instance.save()
        return Response(status=status.HTTP_200_OK)


class CentersView(APIView):
    permission_classes = (AllowAny,)

    @method_decorator(cache_page(DEFAULT_CACHE_TIMEOUT))
    def get(self, request):
        return Response(data={
            'centers': sorted(map(lambda item: item.replace('_', ' ').title(), constants.CENTERS_REGIONS.keys()))},
            status=status.HTTP_200_OK)


class UserDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request: Request):
        user = request.user
        return Response(data={
            'username': user.get_username(),
            'email': user.email,
            'first_name': user.first_name or '',
            'middle_name': user.middle_name or '',
            'last_name': user.last_name or '',
            'region': user.region or '',
            'center': user.center or '',
            'gender': user.gender or '',
            'mandal': user.mandal or '',
            'is_onboarded': user.is_onboarded,
            'has_watched_tutorial': user.has_watched_tutorial,
        }, status=status.HTTP_200_OK)


class GetFAQView(APIView):
    permission_classes = (IsAuthenticated,)

    @method_decorator(cache_page(60 * 60 * 12))
    def get(self, request: Request):
        return Response(data=constants.FAQ, status=status.HTTP_200_OK)


class ResetMemorizedView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request: Request):
        for module_instance in request.user.module_instances.all():
            for mukhpath_item_instance in module_instance.mukhpath_item_instances.all():
                mukhpath_item_instance.is_memorized = False
                mukhpath_item_instance.save()
        return Response(data={}, status=status.HTTP_200_OK)


class ResetBookmarkedView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request: Request):
        for module_instance in request.user.module_instances.all():
            if module_instance.module.title == constants.SATSANG_DIKSHA:
                continue
            for mukhpath_item_instance in module_instance.mukhpath_item_instances.all():
                mukhpath_item_instance.is_bookmarked = False
                mukhpath_item_instance.save()
        return Response(data={}, status=status.HTTP_200_OK)


class UploadContentView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request: Request):
        # Call python func here.
        upload_mukhpath_content()
        return Response(data={}, status=status.HTTP_200_OK)


MUKHPATH_CONTENT_DIR = 'main/mukhpath_content_data'


def upload_mukhpath_content():
    for module_name in os.listdir(MUKHPATH_CONTENT_DIR):
        file_name = os.path.join(MUKHPATH_CONTENT_DIR, module_name)
        with open(file_name) as opened_file:
            mukhpath_items = csv.reader(opened_file, delimiter='\t')
            # Skip header
            next(mukhpath_items)

            module_name_trunc = module_name[:-4]
            for row in mukhpath_items:
                current_module = models.Module.objects.get(title=module_name_trunc)
                new_item = models.MukhpathItem.objects.create(
                    title=row[0],
                    english_content=row[1],
                    gujurati_content=row[2],
                    transliteration_content=row[3],
                    audio_url=row[4],
                    module=current_module,
                )

                new_item.value = 1 if current_module.title != constants.SATSANG_DIKSHA else row[5]
                new_item.source = '' if current_module.is_bal_mandal else row[5]
