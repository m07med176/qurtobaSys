from customers.models import CustomerInfo, MandopInfo #Customer_Image

from rest_framework import serializers

class SCustomer_info(serializers.ModelSerializer):
    #seller = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    #seller = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = CustomerInfo
        fields = '__all__'

# class SCustomer_Image(serializers.ModelSerializer):
#     class Meta:
#         model = Customer_Image
#         fields = '__all__'

# class SCustomer_account(serializers.ModelSerializer):
#     class Meta:
#         model = Customer_account
#         fields = '__all__'

class SMandop_Info(serializers.ModelSerializer):
    class Meta:
        model = MandopInfo
        fields = '__all__'
