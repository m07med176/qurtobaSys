from rest_framework import serializers

from sellersApp.models import SellerRecord
class S_SellerRecord(serializers.ModelSerializer):
    class Meta:
        model = SellerRecord
        fields = '__all__'