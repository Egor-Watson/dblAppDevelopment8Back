from django.urls import path
from . import views
from .views import homepage, downloadAPK
from rest_framework.urlpatterns import format_suffix_patterns

# urls for api
urlpatterns = [
    path('', homepage),
    path('listings/', views.ListingList.as_view()),
    path('listings/<int:pk>/', views.ListingDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('extrauserinformation/', views.ExtraUserInformationList.as_view()),
    path('extrauserinformation/<int:pk>/', views.ExtraUserInformationDetail.as_view()),
    path('offers/', views.OfferList.as_view()),
    path('offers/<int:pk>/', views.OfferDetail.as_view()),
    path('api/auth/', views.AuthenticatedView.as_view()),
    path('downloadAPK/', downloadAPK),
]

urlpatterns = format_suffix_patterns(urlpatterns)