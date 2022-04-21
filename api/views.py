from django.http import FileResponse, JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import ListingSerializer, UserSerializer, ExtraUserInformationSerializer, OfferSerializer
from .models import Listing, ExtraUserInformation, Offer
from rest_framework import generics, permissions

from django.contrib.auth.models import User

from rest_framework.permissions import IsAuthenticated
from rest_framework import status

import os

# default listing view
class ListingList(generics.ListCreateAPIView):

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


    # to filter append ?owner_id=X to end of url
    def get_queryset(self):
        queryset = Listing.objects.all()

        owner_id = self.request.query_params.get('owner_id')

        # can query for list of ids of Listings
        pk_list = self.request.query_params.get('pk_list')

        if owner_id is not None:
            queryset = queryset.filter(owner_id=owner_id)

        if pk_list is not None:
            pk_list = pk_list.split(',')
            queryset = queryset.filter(pk__in=pk_list)

        return queryset

    serializer_class = ListingSerializer

# default listing detail view
class ListingDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

# default user view
class UserList(generics.ListCreateAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = User.objects.all()
    serializer_class = UserSerializer

# default user detail view
class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = User.objects.all()
    serializer_class = UserSerializer

# authentication view
class AuthenticatedView(APIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, request):
        # Respond with user's id and is_banned flag
        id = request.user.id
        extra_info = ExtraUserInformation.objects.get(pk=id)

        # if successful login respond with user's flags
        msg = {'id': id, 'is_banned': extra_info.is_banned, 'is_admin': extra_info.is_admin}

        return Response(msg, status=status.HTTP_200_OK)

# default extra user info view
class ExtraUserInformationList(generics.ListCreateAPIView):

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    queryset = ExtraUserInformation.objects.all()
    serializer_class = ExtraUserInformationSerializer

# default extra user info detail view
class ExtraUserInformationDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = ExtraUserInformation.objects.all()
    serializer_class = ExtraUserInformationSerializer

# default offer view
class OfferList(generics.ListCreateAPIView):

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # to filter append ?offered_for=X to end of url
    def get_queryset(self):
        queryset = Offer.objects.all()

        offered_for = self.request.query_params.get('offered_for')

        offered_for_owner = self.request.query_params.get('offer_for_owner_id')

        if offered_for is not None:
            queryset = queryset.filter(offer_for_id=offered_for)

        if offered_for_owner is not None:
            queryset = queryset.filter(offer_for__owner_id=offered_for_owner)

        return queryset

    serializer_class = OfferSerializer

# default offer detail view
class OfferDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer

# homepage of api
def homepage(request):
    return render(request, 'homepage.html')

# Lets user download APK
def downloadAPK(request):

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filename = 'RublixApp.apk'
    filepath = BASE_DIR + '/api/Files/' + filename

    # Provide file
    response = FileResponse(open(filepath, 'rb'))
    return response
