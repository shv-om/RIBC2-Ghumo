from rest_framework import serializers

from . import models


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FAQs
        fields = '__all__'