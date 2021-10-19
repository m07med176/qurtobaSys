from rest_framework import serializers
from account.models import Account


class SAccountShow(serializers.ModelSerializer):
    
	class Meta:
		model = Account
		fields = ['pk', 'email', 'username','phone','account_no' ]

class SAccountantShort(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('username')
class AccountS(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'},write_only=True)
    class Meta:
        model = Account
        fields = ["email","username","phone","account_no","password","password2"]
        extra_kwargs = {
            'password':{'write_only':True}
        }

    def save(self):
        account= Account(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
            account_no=self.validated_data['account_no'],
            phone=self.validated_data['phone'],
        )

        password=self.validated_data['password']
        password2=self.validated_data['password2']
        if password!=password2:
            raise serializers.ValidationError({'password':'password must match'})
        
        account.set_password(password)
        account.save()
        return account