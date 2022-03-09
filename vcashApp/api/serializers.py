from rest_framework import serializers
from django.db.models import Sum
import datetime
from vcashApp.models import Sim,SimLog,Device,TransactionsCash
    
class SSimLog(serializers.ModelSerializer):
    class Meta:
        model = SimLog
        fields = '__all__'

# region Sim
class SSim(serializers.ModelSerializer):
    class Meta:
        model = Sim
        fields = '__all__'

class SSimCollection(serializers.ModelSerializer):
    user = serializers.SerializerMethodField('get_username')
    device = serializers.SerializerMethodField('get_device')
    month = serializers.SerializerMethodField('get_month')
    day = serializers.SerializerMethodField('get_day')
    class Meta:
        model = Sim
        fields = ['id','phone','number','note','value','isused','device','user','month','day']
    
    def get_month(self, sim):
        value = TransactionsCash.objects.filter(sim=sim,isSend=True,datetime__year=datetime.datetime.now().year,datetime__month=datetime.datetime.now().month).aggregate(Sum('value'))['value__sum']
        return value if value != None else 0
    
    def get_day(self, sim):
        """ get transactions of this sim in current day """
        value = TransactionsCash.objects.filter(sim=sim,isSend=True,date=datetime.datetime.now().date()).aggregate(Sum('value'))['value__sum']
        return value if value != None else 0
    
    def get_username(self, sim):
            try:
                username = sim.user.username
            except Exception:
                return ""
            return username
    
    def get_device(self, sim):
            try:
                username = sim.device.name
            except Exception:
                return ""
            return username
    
class SSimCollectionRetrieve(serializers.ModelSerializer):
    month = serializers.SerializerMethodField('get_month')
    day = serializers.SerializerMethodField('get_day')
    class Meta:
        model = Sim
        fields = ['phone','number','note','value','isused','device','user','month','day']
    
    def get_month(self, sim):
        value = TransactionsCash.objects.filter(sim=sim,isSend=True,datetime__year=datetime.datetime.now().year,datetime__month=datetime.datetime.now().month).aggregate(Sum('value'))['value__sum']
        return value if value != None else 0
    
    def get_day(self, sim):
        """ get transactions of this sim in current day """
        value = TransactionsCash.objects.filter(sim=sim,isSend=True,date=datetime.datetime.now().date()).aggregate(Sum('value'))['value__sum']
        return value if value != None else 0
    
    def get_username(self, sim):
            try:
                username = sim.user.username
            except Exception:
                return ""
            return username
    
    def get_device(self, sim):
            try:
                username = sim.device.name
            except Exception:
                return ""
            return username
# endregion Sim

# region Device
class SDevice(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'
        lookup_field = "imei"

class SDeviceCollection(serializers.ModelSerializer):
    user = serializers.SerializerMethodField('get_username')
    class Meta:
        model = Device
        fields = '__all__'

    def get_username(self, device):
        try: return device.user.username
        except Exception: return ""
    
# endregion Device
   
# region Transactions
class STransactionsCash(serializers.ModelSerializer):
    class Meta:
        model = TransactionsCash
        fields = '__all__'

class STransactionsCashCollection(serializers.ModelSerializer):
    user  = serializers.SerializerMethodField('get_username')
    device  = serializers.SerializerMethodField('get_device')
    sim     = serializers.SerializerMethodField('get_sim')
    class Meta:
        model = TransactionsCash
        fields = '__all__'
    
    
    def get_username(self, tranc):
        try: return tranc.user.username
        except Exception: return ""

    def get_device(self, tranc):
        try: return tranc.device.name
        except Exception: return ""

    def get_sim(self, tranc):
        try: return tranc.sim.phone
        except Exception: return ""
# endregion Transactions