from rest_framework import serializers

from .models import Listing

from django.contrib.auth.models import User


# Serializers from official page:
class ListingSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Listing
        fields = ['id', 'name', 'description', 'owner', 'image']
        # fields = ['id', 'name', 'description', 'image']


class UserSerializer(serializers.ModelSerializer):
    listings = serializers.PrimaryKeyRelatedField(many=True, queryset=Listing.objects.all())

    password = serializers.CharField(write_only=True)

    # overriding create method so that password is properly posted
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
        )

        return user

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'listings', 'last_login']
        # fields = ['id', 'username', 'password', 'last_login']
