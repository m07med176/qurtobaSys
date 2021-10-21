from rest_framework import serializers
from account.models import Account
from rest_framework.authtoken.models import Token


class SAccountShow(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['pk', 'email', 'username','phone','account_no' ]

class SAccountAll(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'
class SAccountResponse(serializers.ModelSerializer):
    token = serializers.SerializerMethodField('get_username_token')
    class Meta:
        model = Account
        fields = ['pk', 'email', 'username','phone','account_no' ,'is_admin','is_active','token']
    def get_username_token(self, account):
        try:
            token = Token.objects.get(user=account).key
        except Token.DoesNotExist:
            token = Token.objects.create(user=account)
        return token

class SAccountantState(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['is_admin','is_active','is_staff','is_superuser']

class SAccountantShort(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('username')

# to save and get data
class SAccountManager(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ["password","email","username","phone","account_no","is_superuser","is_admin","is_staff","is_active","type"]
        extra_kwargs = { 'password':{'write_only':True} }
    
    def save(self):
        account= Account(
            email           = self.validated_data['email'],
            username        = self.validated_data['username'],
            account_no      = self.validated_data['account_no'],
            phone           = self.validated_data['phone'],
            is_superuser    = self.validated_data['is_superuser'],
            is_admin        = self.validated_data['is_admin'],
            is_staff        = self.validated_data['is_staff'],
            is_active       = self.validated_data['is_active'],
            type            = self.validated_data['type'],
        )
        password = self.validated_data['password']
        account.set_password(password)
        account.save()
        return account

# to save from user
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