from rest_framework import serializers
from fawryCodesApp.models import FawryCodes

class SFawryCodes(serializers.ModelSerializer):
    class Meta:
        model = FawryCodes
        fields = '__all__'