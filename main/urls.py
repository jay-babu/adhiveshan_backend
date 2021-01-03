from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), ),
    path('change_password/', views.ChangePasswordView.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('access_allowed/', views.AccessAllowedView.as_view()),
    path('get_all_centers/', views.CentersView.as_view()),
    path('get_user_detail/', views.UserDetailView.as_view()),


    path('pledge_options/', views.PledgeOptionsView.as_view(), name='pledge_options_view'),
    path('my_pledges/', views.MyPledgeView.as_view(), name='my_pledges_view'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard_view'),
    path('all_mukhpath_items/', views.AllMukhpathItemsView.as_view(), name='all_mukhpath_items'),
    path('bookmarked_mukhpath_items/', views.BookmarkedMukhpathItemsView.as_view(),
         name='bookmarked_mukhpath_items'),
    path('mukhpath_item_instances/', views.MukhpathItemInstanceView.as_view(),
         name='mukhpath_item_instance_view')
]
