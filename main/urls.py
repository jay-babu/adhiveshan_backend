from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), ),
    path('change_password/', views.ChangePasswordView.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('access_allowed/', views.AccessAllowedView.as_view()),

    path('pledges/', views.PledgeView.as_view(), name='pledge_view'),
    path('modules/', views.ModuleView.as_view(), name='module_view'),
]
