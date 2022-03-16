from django.urls import path
from . import views
from .views import homepage
from rest_framework.urlpatterns import format_suffix_patterns

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', homepage),
    path('listings/', views.ListingList.as_view()),
    path('listings/<int:pk>', views.ListingDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('extrauserinformation/', views.ExtraUserInformationList.as_view()),
    path('extrauserinformation/<int:pk>/', views.ExtraUserInformationDetail.as_view()),
    path('api/auth/', views.AuthenticatedView.as_view()),
    # path('auth/', include('rest_framework_social_oauth2.urls'))
]

urlpatterns = format_suffix_patterns(urlpatterns)