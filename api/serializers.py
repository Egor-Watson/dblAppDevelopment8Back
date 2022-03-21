from rest_framework import serializers

from .models import Listing, ExtraUserInformation

from django.contrib.auth.models import User


# Serializers from official page:
class ListingSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Listing
        fields = ['id', 'name', 'description', 'category', 'similar_items', 'location', 'owner', 'image1', 'image2',
                  'image3', 'image4', 'offers']


class ExtraUserInformationSerializer(serializers.ModelSerializer):

    class Meta:
        model = ExtraUserInformation
        fields = ['user', 'is_admin', 'is_reported']


class UserSerializer(serializers.ModelSerializer):
    listings = serializers.PrimaryKeyRelatedField(many=True, queryset=Listing.objects.all())
    # The below doesnt work for displaying the extra user info
    # extrauserinformations = serializers.PrimaryKeyRelatedField(
    #     many=False,
    #     read_only=False,
    #     queryset=ExtraUserInformation.objects.all()
    # )

    # extrauserinformations = ExtraUserInformationSerializer(many=True)

    password = serializers.CharField(write_only=True)

    # overriding create method so that password is properly posted
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email']
        )

        return user

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'first_name', 'last_name', 'email', 'listings']

