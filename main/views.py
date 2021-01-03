from collections import defaultdict
from os import getenv

from rest_framework import status
from rest_framework.generics import GenericAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from main.serializers import UserSerializer, ChangePasswordSerializer
from . import constants
from . import models


class RegisterView(GenericAPIView):
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            instantiate_module_instances_for_user(models.User.objects.get(email=serializer.data.get('email')))
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def instantiate_module_instances_for_user(user):
    # Bal mandal
    for module in models.Module.objects.filter(is_bal_mandal=True):
        module_instance = models.ModuleInstance.objects.create(user=user, module=module)
        for item in module.mukhpath_items.all():
            models.MukhpathItemInstance.objects.create(
                mukhpath_item=item,
                module_instance=module_instance)


class OnboardedView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        response = {'is_onboarded': request.user.is_onboarded}
        return Response(
            data=response,
            status=status.HTTP_200_OK)

    def put(self, request):
        request.user.is_onboarded = request.data.get('is_onboarded')
        request.user.save()
        return Response(
            data={'is_onboarded': request.user.is_onboarded},
            status=status.HTTP_200_OK)


class ChangePasswordView(UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer
    object = None

    def get_object(self, queryset=None):
        return self.request.user

    def put(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = ChangePasswordSerializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
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

        return Response(data=request.data,
                        status=status.HTTP_201_CREATED)


class DashboardView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        # Checks if pledge object exists.
        if hasattr(request.user, 'pledge'):
            response = defaultdict(list)
            modules = response['modules']
            for pledged_module in request.user.pledge.pledged_modules.all():
                module_instance = models.ModuleInstance.objects.get(
                    user=request.user,
                    module=pledged_module.module)
                modules.append({
                    'title': pledged_module.module.title,
                    'tier': pledged_module.tier,
                    'required': constants.get_required_mukhpath_items(
                        pledged_module.module.title,
                        request.user.mandal,
                        pledged_module.tier),
                    'memorized': get_num_of_items_memorized(module_instance)
                })
            return Response(data=response, status=status.HTTP_200_OK)
        else:
            return Response(data={},
                            status=status.HTTP_200_OK)


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
    for module_instance in user.module_instances.all():
        mukhpath_item_instances = []
        for mukhpath_item_instance in module_instance.mukhpath_item_instances.all():
            if bookmarked_only and not mukhpath_item_instance.is_bookmarked:
                continue
            mukhpath_item_instance_dict = {
                'id': mukhpath_item_instance.id,
                'title': mukhpath_item_instance.mukhpath_item.title,
                'english_content': mukhpath_item_instance.mukhpath_item.english_content,
                'gujurati_content': mukhpath_item_instance.mukhpath_item.gujurati_content,
                'transliteration_content': mukhpath_item_instance.mukhpath_item.transliteration_content,
                'is_memorized': mukhpath_item_instance.is_memorized,
                'is_bookmarked': mukhpath_item_instance.is_bookmarked
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
        }, status=status.HTTP_200_OK)
