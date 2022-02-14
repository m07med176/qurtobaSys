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

class SRestDateCalcComulate(serializers.ModelSerializer):
    customer = SCustomerShort()
    date = serializers.SerializerMethodField('get_last_date')
    class Meta:
        model = Rest
        fields = ["id","customer","value","date","time"]
    
    def get_last_date(self, rest):
            try:
                record = Record.objects.filter(customerData_id=359,isDone=True).order_by('-datetime').first()
                return str(record.date)
            except Exception: # Record.DoesNotExist
                return ""

class SRestDateCalc(serializers.ModelSerializer):
    customer = SCustomerShort()
    date = serializers.SerializerMethodField('get_last_date')
    class Meta:
        model = Rest
        fields = ["id","customer","value","date","time"]
    
    def get_last_date(self, rest):
            try:
                record = Record.objects.filter(customerData=rest.customer,isDown=True).order_by('-datetime').first()
                if record.isDone: 
                    return str(Record.objects.filter(customerData=rest.customer,isDown=False,isDone=False).order_by('-datetime').last().date)
                return str(record.date)
            except Exception: # Record.DoesNotExist
                return rest.date

class SRestDateLast(serializers.ModelSerializer):
    customer = SCustomerShort()
    date = serializers.SerializerMethodField('get_last_date')
    class Meta:
        model = Rest
        fields = ["id","customer","value","date","time"]
    
    def get_last_date(self, rest):
            return rest.date

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

        if record.isDone==False:
            value1 = Record.objects.filter(customerData_id=customer_id,isDone=False,isDown=False,datetime__range = (start,end)).aggregate(Sum('value'))['value__sum'] if Record.objects.filter(customerData_id=customer_id,isDone=False,isDown=False,datetime__range = (start,end)).aggregate(Sum('value'))['value__sum'] != None else 0
            value2 = Record.objects.filter(customerData_id=customer_id,isDone=False,isDown=True,datetime__range = (start,end)).aggregate(Sum('value'))['value__sum'] if Record.objects.filter(customerData_id=customer_id,isDone=False,isDown=True,datetime__range = (start,end)).aggregate(Sum('value'))['value__sum'] != None else 0
            return value1 - value2
        else:
            last1 = Record.objects.filter(isDone=True,isDown=False,customerData=customer_id).order_by('-datetime').aggregate(Sum('value'))['value__sum']
            last2 = Record.objects.filter(isDone=True,isDown=True,customerData=customer_id).order_by('-datetime').aggregate(Sum('value'))['value__sum']
            
            last1 = last1 if last1!=None else 0
            last2 = last2 if last2!=None else 0

            valueDone = last1 - last2
            
            value1 = Record.objects.filter(customerData_id=customer_id,isDown=False,datetime__range = (start,end)).aggregate(Sum('value'))['value__sum'] if Record.objects.filter(customerData_id=customer_id,isDown=False,datetime__range = (start,end)).aggregate(Sum('value'))['value__sum'] != None else 0
            value2 = Record.objects.filter(customerData_id=customer_id,isDown=True,datetime__range = (start,end)).aggregate(Sum('value'))['value__sum'] if Record.objects.filter(customerData_id=customer_id,isDown=True,datetime__range = (start,end)).aggregate(Sum('value'))['value__sum'] != None else 0
            
            finalValue = (value1 - value2)-valueDone
            if finalValue >= 0: return finalValue
            else: return value1 - value2

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