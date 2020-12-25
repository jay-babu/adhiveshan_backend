from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import RegisterView, ChangePassword, PledgeView

urlpatterns = [
    path('register/', RegisterView.as_view(), ),
    path('change_password/', ChangePassword.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('pledges/', PledgeView.as_view(), name='pledge_view'),
]
