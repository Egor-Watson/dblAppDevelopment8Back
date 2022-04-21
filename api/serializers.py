from rest_framework import serializers

from .models import Listing, ExtraUserInformation, Offer

from django.contrib.auth.models import User

# extra user info serializer
class ExtraUserInformationSerializer(serializers.ModelSerializer):

    class Meta:
        model = ExtraUserInformation
        fields = ['user', 'is_admin', 'is_reported', 'is_banned']

# user serializer
class UserSerializer(serializers.ModelSerializer):

    # fetch user's listings
    listings = serializers.PrimaryKeyRelatedField(many=True, queryset=Listing.objects.all())

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

# modified user serializer to be without listings so can be displayed in Listings
class UserForListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'listings']

# listing serializer
class ListingSerializer(serializers.ModelSerializer):

    # get listing's owner
    owner_id = serializers.ReadOnlyField(source='owner.id')

    class Meta:
        model = Listing
        fields = ['id', 'name', 'description', 'category', 'similar_items', 'latitude', 'longitude',
                  'owner_id', 'image1', 'image2', 'image3', 'image4', 'offers', 'archived', 'featured']

# serializer for getting offer's user
class UserForOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']

# modified listing serializer for offers
class ListingForOffersSerializer(serializers.ModelSerializer):
    owner = UserForOfferSerializer()

    class Meta:
        model = Listing
        fields = ['id', 'name', 'owner', 'image1']

# offer serializer
class OfferSerializer(serializers.ModelSerializer):

    # get offer's owner's id
    offer_for_owner_id = serializers.ReadOnlyField(source='offer_for.owner.id')

    class Meta:
        model = Offer
        fields = ['id', 'owner', 'offering', 'offer_for', 'status', 'offer_for_owner_id']
