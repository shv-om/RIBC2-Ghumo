from rest_framework import serializers

from . import models

class MarketplaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Marketplace
        fields = '__all__'

