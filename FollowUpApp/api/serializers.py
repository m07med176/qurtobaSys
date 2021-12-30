from rest_framework import serializers
from FollowUpApp.models import FollowUp,Employers

class SEmployersAll(serializers.ModelSerializer):
    class Meta:
        model = Employers
        fields = '__all__'
        
class SFollowUpAll(serializers.ModelSerializer):
    user = SEmployersAll()
    class Meta:
        model = FollowUp
        fields = '__all__'

