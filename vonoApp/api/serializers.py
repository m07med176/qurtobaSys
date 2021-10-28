from django.db.models import fields
from rest_framework import serializers
from vonoApp.models import VodafoneNumber,VodafoneNumberShow,Area,District,Branch


class SVodafoneNumber(serializers.ModelSerializer):
    class Meta:
        model = VodafoneNumber
        fields = '__all__'

class SDistrict(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = '__all__'

class SBranch(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = '__all__'

class SArea(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = '__all__'

# ------------- this serializers for show only ----------------#
class VodafoneNumberSer(serializers.ModelSerializer):
    class Meta:
        model = VodafoneNumberShow
        fields ='__all__'
