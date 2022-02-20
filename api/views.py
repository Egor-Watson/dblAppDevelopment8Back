from django.shortcuts import render

from .serializers import ListingSerializer, UserSerializer
from .models import Listing
from rest_framework import generics

from django.contrib.auth.models import User
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly



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


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


def homepage(request):
    return render(request, 'homepage.html')