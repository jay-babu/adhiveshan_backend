from rest_framework import status
from rest_framework.generics import GenericAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from . import constants
from main.models import User
from main.serializers import UserSerializer, ChangePasswordSerializer
from . import models


class RegisterView(GenericAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ChangePassword(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ChangePasswordSerializer
    object = None

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

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


class PledgeView(APIView):
    """Endpoints for User objects."""
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        # Checks if pledge object exists.
        if hasattr(request.user, 'pledge'):
            response = {'modules': []}
            for pledged_module in request.user.pledge.pledged_modules.all():
                response['modules'].append({
                    'title': pledged_module.module.title,
                    'tier': pledged_module.tier,
                    'required': constants.REQUIRED_MUKHPATH_ITEMS[
                        (pledged_module.module.title, request.user.mandal, pledged_module.tier)
                    ]
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

