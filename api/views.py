from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import ListingSerializer, UserSerializer, ExtraUserInformationSerializer
from .models import Listing, ExtraUserInformation
from rest_framework import generics, permissions

from django.contrib.auth.models import User
from .permissions import IsOwnerOrReadOnly

from rest_framework.permissions import IsAuthenticated
from rest_framework import status



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

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = User.objects.all()
    serializer_class = UserSerializer

class AuthenticatedView(APIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, request):
        msg = {'message': f'Hi {request.user.username}! Congratulations on being authenticated!'}
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