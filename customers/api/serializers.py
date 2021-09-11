from customers.models import CustomerInfo, MandopInfo #Customer_Image
from rest_framework import serializers

class SMandop_Info(serializers.ModelSerializer):
    class Meta:
        model = MandopInfo
        fields = '__all__'

class SMandopShort(serializers.ModelSerializer):
    class Meta:
        model = MandopInfo
        fields = ('name','id',)

class SCustomer_info(serializers.ModelSerializer):
    seller = SMandopShort()
    class Meta:
        model = CustomerInfo
        fields = '__all__'


class SCustomer(serializers.ModelSerializer):
    #seller = serializers.PrimaryKeyRelatedField( read_only=True)
    seller = SMandopShort()
    class Meta:
        model = CustomerInfo
        fields = ('id','name','deviceNo','seller','shopName','shopKind','phoneNo','address','accounts','time','date')

class SCustomerShort(serializers.ModelSerializer):
    class Meta:
        model = CustomerInfo
        fields = ('id','name','deviceNo')
