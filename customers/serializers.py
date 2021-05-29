from .models import Customer_info,Customer_Image,Customer_account

from rest_framework import serializers

class SCustomer_info(serializers.ModelSerializer):
    class Meta:
        model = Customer_info
        fields = '__all__'

class SCustomer_Image(serializers.ModelSerializer):
    class Meta:
        model = Customer_Image
        fields = '__all__'

class SCustomer_account(serializers.ModelSerializer):
    class Meta:
        model = Customer_account
        fields = '__all__'

