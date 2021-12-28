from rest_framework import serializers
from FollowUpApp.models import FollowUp

class SFollowUpAll(serializers.ModelSerializer):
    class Meta:
        model = FollowUp
        fields = '__all__'