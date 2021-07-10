from rest_framework import serializers
from fawryCodes.models import FawryCodes

class FawryCodesSer(serializers.ModelSerializer):
    class Meta:
        model = FawryCodes
        fields = ["serviceCode","serviceKind","datetime"]