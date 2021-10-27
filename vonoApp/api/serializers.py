from rest_framework import serializers
from vonoApp.models import VodafoneNumber

class VodafoneNumberSer(serializers.ModelSerializer):
    class Meta:
        model = VodafoneNumber
        fields ='__all__'