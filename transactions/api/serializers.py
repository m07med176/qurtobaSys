from transactions.models import Rest,Record,Talabat,LogDate
from rest_framework import serializers
from account.api.serializers import SAccountantShort
from customers.api.serializers import SCustomerShort
from django.db.models import Sum

class SLogDate(serializers.ModelSerializer):
    class Meta:
        model = LogDate
        fields = '__all__'

class STalabat(serializers.ModelSerializer):
    user = serializers.SerializerMethodField('get_username_from_author')

    class Meta:
        model = Talabat
        fields = '__all__'
    def get_username_from_author(self, talabat):
            try:
                username = talabat.user.username
            except Exception: # Record.DoesNotExist
                return ""
            return username

class STalabatGet(serializers.ModelSerializer):
    user = SAccountantShort()
    class Meta:
        model = Talabat
        fields = ['user','type','periority','stateTrans','date', 'dateTime']

class SRest(serializers.ModelSerializer):
    customer = SCustomerShort()
    class Meta:
        model = Rest
        fields = '__all__'

class SRecord(serializers.ModelSerializer):
    customerData = SCustomerShort()
    accountant = serializers.SerializerMethodField('get_username_from_author')
    rest = serializers.SerializerMethodField('get_rest')
    class Meta:
        model = Record
        fields = '__all__'
    def get_rest(self,record):
        start = "2021-09-06 19:00:59+00"
        end = record.datetime
        customer_id = record.customerData.id

        value1 = Record.objects.filter(customerData_id=customer_id,isDown=False,datetime__range = (start,end)).aggregate(Sum('value'))['value__sum'] if Record.objects.filter(customerData_id=customer_id,isDown=False,datetime__range = (start,end)).aggregate(Sum('value'))['value__sum'] != None else 0
        value2 = Record.objects.filter(customerData_id=customer_id,isDown=True,datetime__range = (start,end)).aggregate(Sum('value'))['value__sum'] if Record.objects.filter(customerData_id=customer_id,isDown=True,datetime__range = (start,end)).aggregate(Sum('value'))['value__sum'] != None else 0
        sum  = value1 - value2
        return sum
    def get_username_from_author(self, record):
        try:
            username = record.accountant.username
        except Exception: # Record.DoesNotExist
            return ""
        return username
  
class SRecordSets(serializers.ModelSerializer):
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


# region JUNK

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


"""
class SRecord(serializers.ModelSerializer):
    customerData = SCustomerShort()
    username = serializers.SerializerMethodField('get_username_from_author')
    class Meta:
        model = Record
        fields = ["id","customerData","username","type","value","isDone","isDown","date","time","notes"]

    def get_username_from_author(self, record):
        try:
            username = record.accountant.username
        except Record.DoesNotExist:
            return None
        return username

"""
# endregion JUNK