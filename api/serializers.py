from rest_framework import serializers

from .models import Listing

from django.contrib.auth.models import User


# Serializers from official page:
class ListingSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Listing
        fields = ['id', 'name', 'description', 'owner', 'image']


class UserSerializer(serializers.ModelSerializer):
    listings = serializers.PrimaryKeyRelatedField(many=True, queryset=Listing.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'listings']