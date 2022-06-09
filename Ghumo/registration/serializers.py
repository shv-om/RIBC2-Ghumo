from rest_framework import serializers
from rest_framework.authtoken.models import Token

from django.contrib.auth import authenticate

from .models import User, Seller


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'phone')


# Seller
class Seller_extrainfo(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = ['shopname', 'nearby_area']

class SellerRegisterSerializer(serializers.ModelSerializer):
    seller_extra = Seller_extrainfo()
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'phone', 'seller_extra')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        seller_info = validated_data.pop('seller_extra')
        user = User.objects.create_user(
                                validated_data['username'],
                                email=validated_data['email'],
                                password=validated_data['password'],
                                phone=validated_data['phone'],
                                is_seller=True
                            )

        seller_instance = Seller.objects.create(seller=user, **seller_info)

        return (user, seller_instance)

# Login
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError('Incorrect Credentials Passed.')