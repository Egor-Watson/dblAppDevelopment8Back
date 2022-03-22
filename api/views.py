from django.http import FileResponse
from django.shortcuts import render, HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import ListingSerializer, UserSerializer, ExtraUserInformationSerializer
from .models import Listing, ExtraUserInformation
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

    queryset = Listing.objects.all()
    serializer_class = ListingSerializer


class ListingDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
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