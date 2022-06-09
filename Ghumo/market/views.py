from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics, status
from rest_framework.views import APIView

from .serializers import MarketplaceSerializer, EventDetailsSerializer, DistrictSerializer
from .models import Marketplace, EventDetails, District


class districtview(generics.GenericAPIView):
    serializer_class = DistrictSerializer
    queryset = District.objects.all()

    def get(self, request):
        serializer = DistrictSerializer(self.get_queryset(), many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DistrictSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUES)


class marketplaceview(generics.GenericAPIView):
    serializer_class = MarketplaceSerializer
    queryset = Marketplace.objects.all()

    def get(self, request):
        serializer = MarketplaceSerializer(self.get_queryset(), many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MarketplaceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class eventdetailsview(generics.GenericAPIView):
    serializer_class = EventDetailsSerializer
    queryset = EventDetails.objects.all()

    def get(self, request):
        serializer = EventDetailsSerializer(self.get_queryset(), many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EventDetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)