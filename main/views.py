import os
import csv
from collections import defaultdict
from datetime import timedelta
from os import getenv
from random import randint

from django.utils import timezone
from rest_framework import status, mixins, viewsets
from rest_framework.decorators import permission_classes as pc
from rest_framework.generics import GenericAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from main.serializers import UserSerializer, ChangePasswordSerializer, CreateExternalTokenSerializer
from . import constants
from . import models
from .models import title_and_capitial, ExternalUserModel, User


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

    def get_object(self, queryset=None):
        return self.request.user

    def put(self, request, *args, **kwargs):
        serializer = ChangePasswordSerializer(data=request.data, context=self.request)

        if serializer.is_valid():
            # set_password also hashes the password that the user will get
            self.get_object().set_password(serializer.validated_data.get("new_password"))
            self.get_object().save()
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
            # Remove all satsang diksha bookmarks here.
            satsang_diksha_instance = request.user.module_instances.get(module__title=constants.SATSANG_DIKSHA)
            for mukhpath_item_instance in satsang_diksha_instance.mukhpath_item_instances.all():
                mukhpath_item_instance.is_bookmarked = False
                mukhpath_item_instance.save()

            pledge = request.user.pledge
        # If not, create new pledge object.
        else:
            pledge = models.Pledge.objects.create(user=request.user)

        for module in request.data['modules']:
            models.PledgedModule.objects.create(
                pledge=pledge,
                module=models.Module.objects.get(title=module['title']),
                tier=module['tier'])

            # If pledged module is satsang diksha, bookmark items in tier.
            if module['title'] == constants.SATSANG_DIKSHA:
                module_instance = request.user.module_instances.get(module__title=constants.SATSANG_DIKSHA)
                for mukhpath_item_instance in module_instance.mukhpath_item_instances.all():
                    if mukhpath_item_instance.mukhpath_item.title in constants.SD_SHLOKAS_FOR_TIER[module['tier']]:
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
                'required': constants.REQUIRED_PER_KM_MODULE[module_instance.module.title],
                'memorized': get_num_of_items_memorized(module_instance)
            })
    # Get all modules that the user has added bookmarks too.
    return Response(data=response, status=status.HTTP_200_OK)


def get_num_of_items_memorized(module_instance):
    value_of_items_memorized = 0
    for item_instance in module_instance.mukhpath_item_instances.filter(is_memorized=True):
        value_of_items_memorized += item_instance.mukhpath_item.value
    return value_of_items_memorized


class AccessAllowedView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request: Request):
        if request.data.get('ADHIVESHAN_ACCESS_CODE', '') == getenv('ADHIVESHAN_ACCESS_CODE'):
            return Response({'access_allowed': True}, status=status.HTTP_200_OK)
        return Response({'access_allowed': False}, status=status.HTTP_401_UNAUTHORIZED)


class ModuleImagesView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        data = {}
        for module_instance in request.user.module_instances.all():
            if module_instance.module.title == constants.KM_MODULES:
                continue
            data[module_instance.module.title] = module_instance.module.image_url

        return Response(data=data, status=status.HTTP_200_OK)


class AllMukhpathItemsView(APIView):
    permission_classes = (IsAuthenticated,)

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
    has_pledged_for_satsang_diksha = False
    try:
        _ = user.pledge
        has_pledged_for_satsang_diksha = user.pledge.pledged_modules.filter(
            module__title=constants.SATSANG_DIKSHA).count() > 0
    except Exception:
        pass

    sd_tier = None
    if has_pledged_for_satsang_diksha:
        sd_tier = user.pledge.pledged_modules.get(module__title=constants.SATSANG_DIKSHA).tier

    for module_instance in user.module_instances.all().order_by('module__index'):
        mukhpath_item_instances = []
        module_instance_is_sd = module_instance.module.title == constants.SATSANG_DIKSHA

        for mukhpath_item_instance in module_instance.mukhpath_item_instances.all().order_by('mukhpath_item__index'):
            if bookmarked_only and not mukhpath_item_instance.is_bookmarked:
                continue

            if module_instance_is_sd and has_pledged_for_satsang_diksha:
                is_item_in_sd_tier = mukhpath_item_instance.mukhpath_item.title in constants.SD_SHLOKAS_FOR_TIER[
                    sd_tier]
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

    def get(self, request):
        return Response(data={
            'centers': sorted(map(lambda center: center.replace('_', ' ').title()
            if len(center.split('_')) == 1
            else title_and_capitial(center.replace('_', ' ')), constants.CENTERS_REGIONS.keys()))},
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

    def get(self, request):
        if request.user.is_bal_mandal():
            return Response(data=constants.BAL_FAQ, status=status.HTTP_200_OK)
        elif request.user.is_kishore_mandal():
            return Response(data=constants.KISHORE_FAQ, status=status.HTTP_200_OK)
        else:
            return Response(data={}, status=status.HTTP_200_OK)


class GetSkillsChallengeView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        if request.user.is_bal_mandal():
            return Response(data=constants.BAL_SKILLS_CHALLENGE, status=status.HTTP_200_OK)
        elif request.user.is_kishore_mandal():
            return Response(data=constants.KISHORE_SKILLS_CHALLENGE, status=status.HTTP_200_OK)
        else:
            return Response(data={}, status=status.HTTP_200_OK)


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


class DeleteUserView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request: Request):
        request.user.delete()
        return Response(data={}, status=status.HTTP_200_OK)


class AnnouncementsPageView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        if request.user.is_bal_mandal():
            return Response(data=constants.BM_ANNOUNCEMENT_PAGE_CONTENT, status=status.HTTP_200_OK)
        elif request.user.is_kishore_mandal():
            return Response(data=constants.KM_ANNOUNCEMENT_PAGE_CONTENT, status=status.HTTP_200_OK)
        else:
            return Response(data={}, status=status.HTTP_200_OK)


class UploadContentView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request: Request):
        # Call python func here.
        upload_mukhpath_content()
        return Response(data={}, status=status.HTTP_200_OK)


class AddModulesToDB(APIView):
    permission_classes = (AllowAny,)

    def post(self, request: Request):
        # Add special KM MODULES
        models.Module.objects.create(
            title='km_modules',
            image_url='',
            is_bal_mandal=False,
            is_kishore_mandal=False,
            index=1
        )

        # Only satsang diksha
        for module_title in constants.BAL_AND_KISHORE_MODULES:
            models.Module.objects.update_or_create(
                title=module_title,
                is_bal_mandal=True,
                is_kishore_mandal=True,
                index=1,
                defaults={
                    'image_url': constants.MODULE_ICON_LINKS[module_title],
                }
            )

        index = 2
        for module_title in constants.BAL_ONLY_MODULES:
            models.Module.objects.update_or_create(
                title=module_title,
                is_bal_mandal=True,
                is_kishore_mandal=False,
                index=index,
                defaults={
                    'image_url': constants.MODULE_ICON_LINKS[module_title],
                }
            )
            index += 1

        index = 2
        for module_title in constants.KISHORE_ONLY_MODULES:
            models.Module.objects.update_or_create(
                title=module_title,
                is_bal_mandal=False,
                is_kishore_mandal=True,
                index=index,
                defaults={
                    'image_url': constants.MODULE_ICON_LINKS[module_title],
                }
            )
            index += 1
        return Response(data={}, status=status.HTTP_200_OK)


MUKHPATH_CONTENT_DIR = 'main/mukhpath_content_data'


def upload_mukhpath_content():
    for module_name in os.listdir(MUKHPATH_CONTENT_DIR):
        file_name = os.path.join(MUKHPATH_CONTENT_DIR, module_name)
        with open(file_name) as opened_file:
            mukhpath_items = csv.reader(opened_file, delimiter=',')
            # Skip header
            next(mukhpath_items)

            module_name_trunc = module_name[:-4]
            index = 1
            for row in mukhpath_items:
                current_module = models.Module.objects.get(title=module_name_trunc)
                new_item = models.MukhpathItem.objects.create(
                    title=row[0],
                    english_content='\n'.join(row[1].splitlines()),
                    gujurati_content='\n'.join(row[2].splitlines()),
                    transliteration_content='\n'.join(row[3].splitlines()),
                    audio_url=row[4],
                    module=current_module,
                    index=index,
                )
                index += 1

                new_item.value = 1 if current_module.title != constants.SATSANG_DIKSHA else row[5]
                new_item.save()


class CreateExternalTokenView(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = CreateExternalTokenSerializer
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        request.data['user'] = self.request.user.pk
        request.data['code'] = randint(99999, 999999)
        request.data['code_expiration'] = timezone.now() + timedelta(days=1)
        return super().create(request, *args, **kwargs)


class GetExternalUserView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request: Request):
        data = request.data
        try:
            if (ex_user := ExternalUserModel.objects.get(user=User.objects.get(email=data.get('email')), code=data.get(
                    'code'))) and timezone.now() <= ex_user.code_expiration:
                user = User.objects.get(email=data.get('email'))
                return Response(data=get_modules(user=user, bookmarked_only=True), status=status.HTTP_200_OK)
        except ExternalUserModel.DoesNotExist:
            pass
        return Response(data={'error': 'Invalid Email or Code'}, status=status.HTTP_400_BAD_REQUEST)
