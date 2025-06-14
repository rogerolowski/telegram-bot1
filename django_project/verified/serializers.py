from rest_framework import serializers
from .models import VerifiedAddress

class VerifiedAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = VerifiedAddress
        fields = ["id", "wallet_address", "verified_at"]
