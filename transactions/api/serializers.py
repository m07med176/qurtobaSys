from transactions.models import Rest,Record
from rest_framework import serializers

class SRest(serializers.ModelSerializer):
    class Meta:
        model = Rest
        fields = '__all__'

class SRecord(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = '__all__'
