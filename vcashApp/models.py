from django.db import models
from account.models import Account
from customers.models import MandopInfo
from django.utils import timezone
class Device(models.Model):
    name = models.CharField(max_length=45, blank=True, null=True)
    deviceid = models.CharField(unique = True,max_length=50, blank=True, null=True) 
    imei = models.CharField(unique = True,max_length=50, blank=True, null=True) 
    baddress = models.CharField(unique = True,max_length=50, blank=True, null=True) 
    user = models.ForeignKey(Account,related_name="Device.Account+", on_delete = models.CASCADE,blank=True, null=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        managed = True
        ordering = ['-id']
        

class Sim(models.Model):
    phone = models.CharField(unique = True,max_length=45, blank=True, null=True)
    number = models.IntegerField(unique = True,blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    value = models.FloatField(blank=True, null=True)
    isused = models.BooleanField(blank=True, null=True,default=False)  
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    user = models.ForeignKey(Account,related_name="Sim.Account+", on_delete = models.CASCADE)

    def __str__(self):return str(self.phone)

    class Meta:
        managed = True
        ordering = ['-number']

class SimLog(models.Model):
    value       = models.FloatField(blank=True, null=True)
    dateinsert  = models.DateField(blank=True, null=True) 
    timeinsert  = models.TimeField(blank=True, null=True) 
    datetimeinsert = models.DateTimeField(blank=True, null=True)  
    dateremove  = models.DateField(blank=True, null=True) 
    timeremove  = models.TimeField(blank=True, null=True) 
    datetimeremove = models.DateTimeField(blank=True, null=True)  
    sim = models.ForeignKey(Sim, on_delete = models.CASCADE,blank=True, null=True)

    def __str__(self):return str(self.datetimeinsert)

    class Meta:
        managed = True


class TransactionsCash(models.Model):
    device = models.ForeignKey(Device, models.CASCADE)
    sim = models.ForeignKey(Sim, models.CASCADE)
    user = models.ForeignKey(Account,related_name="TransactionsCash.Account+", on_delete = models.CASCADE)
    customer = models.CharField(max_length=45)
    value = models.FloatField()
    rest = models.FloatField(blank=True, null=True)
    operationno = models.CharField(max_length=100, blank=True, null=True)  
    messagedate = models.CharField(max_length=100, blank=True, null=True)  
    note = models.TextField(blank=True, null=True)
    isSend = models.BooleanField(blank=True, null=True)

    date = models.DateField(blank=True, null=True,auto_now_add=True)
    time = models.TimeField(blank=True, null=True,auto_now_add=True)
    datetime = models.DateTimeField(blank=True, null=True,auto_now_add=True)
    timestamp = models.DateTimeField(blank=True, null=True,auto_now_add=True)
    
    seller    = models.ForeignKey(MandopInfo,related_name="TransactionsCash.MandopInfo+",on_delete = models.CASCADE,null=True,blank=True)

    def __str__(self):return str(self.value)

    class Meta:
        managed = True
        ordering = ['-datetime']