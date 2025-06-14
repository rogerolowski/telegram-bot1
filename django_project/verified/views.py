from django.shortcuts import render

from rest_framework import viewsets
from .models import VerifiedAddress
from .serializers import VerifiedAddressSerializer

class VerifiedAddressViewSet(viewsets.ModelViewSet):
    queryset = VerifiedAddress.objects.all()
    serializer_class = VerifiedAddressSerializer
