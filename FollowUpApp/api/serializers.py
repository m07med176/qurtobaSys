from rest_framework import serializers
from FollowUpApp.models import FollowUp
from account.models import Account
from rest_framework.authtoken.models import Token


class SFollowUp(serializers.ModelSerializer):
    class Meta:
        model = FollowUp
        fields = '__all__'


class SEmployersAll(serializers.ModelSerializer):
    token = serializers.SerializerMethodField('get_username_token')
    duration = serializers.SerializerMethodField('get_duration')
    class Meta:
        model = Account
        fields =['id','email','username','phone','date_joined','last_login','is_superuser','is_admin','is_staff','is_active','is_open','type','duration','token']
    def get_duration(self,employer):
        duration = FollowUp.objects.filter(user=employer).last()
        return SFollowUp(duration).data
    def get_username_token(self, account):
        try:
            token = Token.objects.get(user=account).key
        except Token.DoesNotExist:
            token = Token.objects.create(user=account)
        return token



class SFollowUpAll(serializers.ModelSerializer):
    user = SEmployersAll()
    class Meta:
        model = FollowUp
        fields = '__all__'
