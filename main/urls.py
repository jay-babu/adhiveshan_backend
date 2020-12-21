from django.urls import path

from . import model_api

urlpatterns = [
    path('users/', model_api.UsersEndpoint.as_view(), name='main/users'),
]