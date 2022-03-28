from rest_framework import serializers

from .models import Listing, ExtraUserInformation, Offer

from django.contrib.auth.models import User





class ExtraUserInformationSerializer(serializers.ModelSerializer):

    class Meta:
        model = ExtraUserInformation
        fields = ['user', 'is_admin', 'is_reported', 'is_banned']


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

    # update method for proper password posting
    def update(self, instance, validated_data):

        instance.username = validated_data['username']
        instance.set_password(validated_data['password'])
        instance.save()

        return instance

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'first_name', 'last_name', 'email', 'listings']

# Modified user serializer to be without listings so can be displayed in Listings
class UserForListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'listings']

# Serializers from official page:
class ListingSerializer(serializers.ModelSerializer):
    owner = UserForListingSerializer()
    owner_id = serializers.ReadOnlyField(source='owner.id')

    class Meta:
        model = Listing
        fields = ['id', 'name', 'description', 'category', 'similar_items', 'latitude', 'longitude', 'owner',
                  'owner_id', 'image1', 'image2', 'image3', 'image4', 'offers', 'archived', 'featured']


class UserForOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']

# modified listing serailizer for offers
class ListingForOffersSerializer(serializers.ModelSerializer):
    owner = UserForOfferSerializer()

    class Meta:
        model = Listing
        fields = ['id', 'name', 'owner', 'image1']

class OfferSerializer(serializers.ModelSerializer):
    # cant get this to work as a read only field
    # owner = UserForOfferSerializer()
    # offering = ListingForOffersSerializer()
    # offer_for = ListingForOffersSerializer()

    # def create(self, validated_data):
    #     print(validated_data)
    #
    #     offering = Offer.objects.create(
    #         owner=validated_data['owner'],
    #         offering=validated_data['offering'],
    #         offer_for=validated_data['offer_for'],
    #         status=validated_data['status']
    #     )
    #
    #     return offering

    # offering_id = serializers.IntegerField(source='offering_id')
    # offer_for_id = serializers.IntegerField(source='offer_for_id')
    # owner_id = serializers.IntegerField(source='owner')

    class Meta:
        model = Offer
        # read_only_fields = ['owner', 'offering', 'offer_for']
        # fields = ['id', 'owner_id', 'status', 'offering_id', 'offer_for_id', 'owner_id']
        fields = ['id', 'owner', 'offering', 'offer_for', 'status']

