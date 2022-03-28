from django.http import FileResponse, JsonResponse
from django.shortcuts import render, HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import ListingSerializer, UserSerializer, ExtraUserInformationSerializer, OfferSerializer
from .models import Listing, ExtraUserInformation, Offer
from rest_framework import generics, permissions

from django.contrib.auth.models import User
from .permissions import IsOwnerOrReadOnly

from rest_framework.permissions import IsAuthenticated
from rest_framework import status

import os
import mimetypes



class ListingList(generics.ListCreateAPIView):

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


    # to filter append ?owner_id=X to end of url
    def get_queryset(self):
        queryset = Listing.objects.all()

        owner_id = self.request.query_params.get('owner_id')

        if owner_id is not None:
            queryset = queryset.filter(owner_id=owner_id)

        return queryset

    serializer_class = ListingSerializer


class ListingDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer


class UserList(generics.ListCreateAPIView):
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    permission_classes = [permissions.AllowAny]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    queryset = User.objects.all()
    serializer_class = UserSerializer

class AuthenticatedView(APIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, request):
        # Respond with user's id and is_banned flag
        id = request.user.id
        extra_info = ExtraUserInformation.objects.get(pk=id)

        # if successful login respond with user's flags
        msg = {'id': id, 'is_banned': extra_info.is_banned, 'is_admin': extra_info.is_admin}

        return Response(msg, status=status.HTTP_200_OK)


class ExtraUserInformationList(generics.ListCreateAPIView):

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    queryset = ExtraUserInformation.objects.all()
    serializer_class = ExtraUserInformationSerializer


class ExtraUserInformationDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = ExtraUserInformation.objects.all()
    serializer_class = ExtraUserInformationSerializer


class OfferList(generics.ListCreateAPIView):

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # to filter append ?offered_for=X to end of url
    def get_queryset(self):
        queryset = Offer.objects.all()

        offered_for = self.request.query_params.get('offered_for')

        if offered_for is not None:
            queryset = queryset.filter(offer_for=offered_for)

        return queryset



    serializer_class = OfferSerializer


class OfferDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer


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


def arrayTest(request, a):
    # theArray = request.GET.get('array', '')
    list = a.split(',')
    int_list = []

    # convert string ints to ints
    for l in list:
        int_list.append(int(l))

    Listings_list = []

    for i in int_list:
        Listings_list.append(Listing.objects.get(pk=i))


    print(ListingSerializer(Listings_list, many=True).data)

    data = ListingSerializer(Listings_list, many=True).data
    # serializer_class = ExtraUserInformationSerializer
    # return HttpResponse(ListingSerializer(Listings_list[0]).data)
    return JsonResponse(data)

class arrayTest2(APIView):
    queryset = Listing.objects.all()

    def get(self, request, format=None):

        usernames = [user.username for user in User.objects.all()]
        return Response(usernames)
