from rest_framework import serializers
from shakawaApp.models import Shakawa
from account.api.serializers import SAccountantShort
class ShakawaSer(serializers.ModelSerializer):
    #dateTime = serializers.DateTimeField(format=base.DATETIME_FORMAT, input_formats=None)
    user = SAccountantShort()
    class Meta:
        model = Shakawa
        fields =  '__all__'

    
class ShakawaSerAll(serializers.ModelSerializer):
    #dateTime = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = Shakawa
        fields =  '__all__'

"""
    user = serializers.SerializerMethodField('get_username')

def get_username(self, shakawa):
        try:
            return shakawa.user.username
        except AttributeError:
            return ""
"""