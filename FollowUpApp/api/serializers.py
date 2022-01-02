from rest_framework import serializers
from FollowUpApp.models import FollowUp,Employers

class SFollowUp(serializers.ModelSerializer):
    class Meta:
        model = FollowUp
        fields = '__all__'

class SEmployersAll(serializers.ModelSerializer):
    duration = serializers.SerializerMethodField('get_duration')
    class Meta:
        model = Employers
        fields =['uid','email','name','image','phone','date_joined','last_login','is_superuser','is_admin','is_staff','is_active','type','duration']
    def get_duration(self,employer):
        duration = FollowUp.objects.filter(user=employer).first()
        return SFollowUp(duration).data
class SFollowUpAll(serializers.ModelSerializer):
    user = SEmployersAll()
    class Meta:
        model = FollowUp
        fields = '__all__'

class SFollowUp(serializers.ModelSerializer):
    class Meta:
        model = FollowUp
        fields = '__all__'


