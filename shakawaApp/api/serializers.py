from rest_framework import serializers
from shakawaApp.models import Shakawa

class ShakawaSer(serializers.ModelSerializer):
    #dateTime = serializers.DateTimeField(format=base.DATETIME_FORMAT, input_formats=None)
    user = serializers.SerializerMethodField('get_username')
    class Meta:
        model = Shakawa
        fields =  '__all__'

    def get_username(self, shakawa):
        return shakawa.user.username
class ShakawaSerAll(serializers.ModelSerializer):
    #dateTime = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = Shakawa
        fields =  '__all__'
