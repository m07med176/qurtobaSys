from transactions.models import Rest,Record
from rest_framework import serializers

from customers.api.serializers import SCustomerShort


class SRest(serializers.ModelSerializer):
    class Meta:
        model = Rest
        fields = '__all__'

class SRecord(serializers.ModelSerializer):
    customerData = SCustomerShort()
    class Meta:
        model = Record
        fields = '__all__'




class TrackListingField(serializers.RelatedField):
    def to_representation(self, value):
        return 'Track %s: ' % (value.name)

class SMainRest(serializers.ModelSerializer):
    #customer = serializers.SCustomer_info(many=True, read_only=True)
    #customer = serializers.StringRelatedField(many=True)
    #customer = TrackListingField(many=True, read_only=True)
    #customer = serializers.SlugRelatedField(
    #     many=True,
    #     read_only=True,
    #     slug_field='name'
    #  )
    class Meta:
        model = Rest
        fields = ['value','customer','date','time']


        """
        
        class SMainRest(serializers.HyperlinkedModelSerializer):
        area = serializers.CharField(source='customerinfo.area')
    name = serializers.CharField(source='customerinfo.area')
    deviceNo = serializers.IntegerField(source='customerinfo.area')
    phoneNo = serializers.CharField(source='customerinfo.area')

    #customer = serializers.SCustomer_info(many=True, read_only=True)
    #customer = serializers.StringRelatedField(many=True)
    #customer = TrackListingField(many=True, read_only=True)
    #customer = serializers.SlugRelatedField(
    #     many=True,
    #     read_only=True,
    #     slug_field='name'
    #  )
    class Meta:
        model = Rest
        fields = ['value','customer','date','time','area','name','deviceNo',]
        #fields = '__all__'
        """