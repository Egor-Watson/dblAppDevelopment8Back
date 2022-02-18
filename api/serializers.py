from rest_framework import serializers

from .models import Listing

class ListingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Listing
        fields = ('id', 'name',)