from customers.models import CustomerInfo, MandopInfo #Customer_Image
from rest_framework import serializers

# region Normal Serializers
class SMandopInfo_Normal(serializers.ModelSerializer):
    class Meta:
        model = MandopInfo
        fields = '__all__'
class SCustomerInfo(serializers.ModelSerializer):
    class Meta:
        model = CustomerInfo
        fields = '__all__'
# endregion Normal Serializers

# region Short Serializers
class SMandopShort(serializers.ModelSerializer):
    class Meta:
        model = MandopInfo
        fields = ('name','id',)
        
class SCustomerShort(serializers.ModelSerializer):
    class Meta:
        model = CustomerInfo
        fields = ('id','name','deviceNo')
# endregion Short Serializers

# region Read Serializers
class SCustomer_info(serializers.ModelSerializer):
    seller = SMandopShort()
    assistant = SMandopShort()
    class Meta:
        model = CustomerInfo
        fields = '__all__'


class SCustomer(serializers.ModelSerializer):
    #seller = serializers.PrimaryKeyRelatedField( read_only=True)
    seller = SMandopShort()
    assistant = SMandopShort()
    class Meta:
        model = CustomerInfo
        fields = ('id','name','surName','area','deviceNo','seller','assistant','user','shopName','shopKind','phoneNo','address','accounts','time','date','notes','grade')
# endregion Read Serializers
