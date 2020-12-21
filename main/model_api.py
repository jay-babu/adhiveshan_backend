from rest_framework.request import Request
from rest_framework import response
from rest_framework import status
from rest_framework import views
from rest_framework.permissions import AllowAny

from . import models
from . import serializers


class UsersEndpoint(views.APIView):
    """Endpoints for User objects."""
    permission_classes = (AllowAny, )

    def post(self, request: Request) -> response.Response:
        """Registers a new user."""
        try:
            user: models.User = models.User.objects.create_user_from_json(
                data=request.data)
        except:
            return response.Response(status=status.HTTP_400_BAD_REQUEST)

        serialized_user = serializers.UserSerializer(instance=user)
        return response.Response(data=serialized_user.data,
                                 status=status.HTTP_201_CREATED)
