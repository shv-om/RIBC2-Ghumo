from django.shortcuts import render
from django.contrib import auth
from rest_framework import permissions, viewsets, serializers, generics
from rest_framework.response import Response
from knox.models import AuthToken

from .models import User
from .serializers import (
                    UserSerializer, LoginSerializer,
                    SellerRegisterSerializer, ArtistRegisterSerializer, TravellerRegisterSerializer,
                    Seller_extrainfo, Artist_extrainfo, Traveller_extrainfo
                )

class MainUser(generics.RetrieveAPIView):
    permission_classes = [
                    permissions.IsAuthenticated
                ]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class SellerSignUpAPI(generics.GenericAPIView):
    serializer_class = SellerRegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, seller = serializer.save()
        token = AuthToken.objects.create(user)
        return Response({
                    "users": UserSerializer(user, context=self.get_serializer_context()).data,
                    "seller": Seller_extrainfo(seller, context=self.get_serializer_context()).data,
                    "token": token[1]
                })

class ArtistSignUpAPI(generics.GenericAPIView):
    serializer_class = ArtistRegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, artist = serializer.save()
        token = AuthToken.objects.create(user)
        return Response({
                    "users": UserSerializer(user, context=self.get_serializer_context()).data,
                    "artist": Artist_extrainfo(artist, context=self.get_serializer_context()).data,
                    "token": token[1]
                })

class TravellerSignUpAPI(generics.GenericAPIView):
    serializer_class = TravellerRegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, traveller = serializer.save()
        token = AuthToken.objects.create(user)
        return Response({
                    "users": UserSerializer(user, context=self.get_serializer_context()).data,
                    "traveller": Traveller_extrainfo(traveller, context=self.get_serializer_context()).data,
                    "token": token[1]
                })


class SignInAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({
                    "user": UserSerializer(user, context=self.get_serializer_context()).data,
                    "token": AuthToken.objects.create(user)[1]
                })
