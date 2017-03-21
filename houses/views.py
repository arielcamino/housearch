from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import HouseSerializer
from .models import (House, HouseImage)


class HouseView(APIView):
    allowed_methods = ('GET', 'OPTIONS', 'HEAD')
    serializer = HouseSerializer

    def get(self, request, format=None):
        serializer = self.serializer(House.objects.all(), many=True)
        return Response(serializer.data)
