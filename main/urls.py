from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import model_api
from .views import RegisterView

urlpatterns = [
    # path('users/', model_api.UsersEndpoint.as_view(), name='main/users'),
    path('register', RegisterView.as_view(), ),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
