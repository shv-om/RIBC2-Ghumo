from rest_framework import serializers
from rest_framework.authtoken.models import Token

from django.contrib.auth import authenticate

from .models import User, Seller, Artist, Traveller


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


# Artist
class Artist_extrainfo(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['event_type']

class ArtistRegisterSerializer(serializers.ModelSerializer):
    artist_extra = Artist_extrainfo()
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'phone', 'artist_extra')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        artist_info = validated_data.pop('artist_extra')

        user = User.objects.create_user(
                                validated_data['username'],
                                email=validated_data['email'],
                                password=validated_data['password'],
                                phone=validated_data['phone'],
                                is_artist=True
                            )

        artist_instance = Artist.objects.create(artist=user, **artist_info)

        return (user, artist_instance)


# Traveller
class Traveller_extrainfo(serializers.ModelSerializer):
    class Meta:
        model = Traveller
        fields = ['address']

class TravellerRegisterSerializer(serializers.ModelSerializer):
    traveller_extra = Traveller_extrainfo()
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'phone', 'traveller_extra')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        traveller_info = validated_data.pop('traveller_extra')
        user = User.objects.create_user(
                                validated_data['username'],
                                email=validated_data['email'],
                                password=validated_data['password'],
                                phone=validated_data['phone'],
                                is_traveller=True
                            )

        traveller_instance = Traveller.objects.create(traveller=user, **traveller_info)

        return (user, traveller_instance)


# Login
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError('Incorrect Credentials Passed.')
