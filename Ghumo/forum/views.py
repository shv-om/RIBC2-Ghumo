from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics, status
from rest_framework.views import APIView

from .serializers import FAQSerializer
from .models import FAQs


class faqview(generics.GenericAPIView):
    serializer_class = FAQSerializer
    queryset = FAQs.objects.all()

    def get(self, request):
        serializer = FAQSerializer(self.get_queryset(), many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FAQSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUES)