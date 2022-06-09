from rest_framework import serializers

from . import models


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.District
        fields = '__all__'


class MarketplaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Marketplace
        fields = '__all__'


class EventDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.EventDetails
        fields = '__all__'
