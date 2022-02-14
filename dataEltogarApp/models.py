from statistics import mode
from django.db import models
from django.utils import timezone
from account.models import Account

class Test(models.Model):
    name1   = models.CharField(blank=False,null=False,max_length=50)


# class Area(models.Model):
#     user   = models.ForeignKey(Account,related_name="Area.user+",on_delete = models.PROTECT,verbose_name="المستخدم",null=True,blank=True)
#     name   = models.CharField(blank=False,null=False,verbose_name='المنطقة',max_length=50)

# class Info(models.Model):
#     #بيانات التاجر
#     nameOfMandoop   = models.CharField(blank=True,null=True,verbose_name='إسم المندوب',max_length=50,)
#     activityKind    = models.CharField(blank=True,null=True,verbose_name='إسم المندوب',max_length=50)
#     address         = models.CharField(blank=True,null=True,verbose_name='إسم المندوب',max_length=50) 
#     area            = models.CharField(blank=True,null=True,verbose_name='إسم المندوب',max_length=50)

#     evaluate        = models.CharField(blank=True,null=True,verbose_name='إسم المندوب',max_length=50)
#     notes           = models.CharField(blank=True,null=True,verbose_name='إسم المندوب',max_length=50)      
#     phoneNumber     = models.CharField(blank=True,null=True,verbose_name='إسم المندوب',max_length=50) 
#     shopName        = models.CharField(blank=True,null=True,verbose_name='إسم المندوب',max_length=50)
#     ownerName       = models.CharField(blank=True,null=True,verbose_name='إسم المندوب',max_length=50)   

# class Tayer(models.Model):
#     #الطاير
#     intention= models.CharField(blank=True,null=True,verbose_name='إسم المندوب',max_length=50)      
#     tayer= models.CharField(blank=True,null=True,verbose_name='إسم المندوب',max_length=50)      
#     tayerFromWho= models.CharField(blank=True,null=True,verbose_name='إسم المندوب',max_length=50)
#     amountPayTayer= models.CharField(blank=True,null=True,verbose_name='إسم المندوب',max_length=50)  

# class Cash(models.Model):
#     #الكاش
#     cash= models.CharField(blank=True,null=True,verbose_name='إسم المندوب',max_length=50)
#     intent_cash= models.CharField(blank=True,null=True,verbose_name='إسم المندوب',max_length=50) 
#     amountPayCash= models.CharField(blank=True,null=True,verbose_name='إسم المندوب',max_length=50)   

# class Phone(models.Model):
#     #المحمول
#     kindOfMobile= models.CharField(blank=True,null=True,verbose_name='إسم المندوب',max_length=50)
#     mobileNotes= models.CharField(blank=True,null=True,verbose_name='إسم المندوب',max_length=50) 
#     mobileFromWhow= models.CharField(blank=True,null=True,verbose_name='إسم المندوب',max_length=50) 

# class EPay(models.Model):
#     #الدفع الإلكترونى
#     machinesOfepay= models.CharField(blank=True,null=True,verbose_name='إسم المندوب',max_length=50)     
#     machinesOfepayIsNeedMachine= models.CharField(blank=True,null=True,verbose_name='إسم المندوب',max_length=50) 
#     amountOfTreat= models.CharField(blank=True,null=True,verbose_name='إسم المندوب',max_length=50) 

# class Bakar(models.Model):
#     #الكارت
#     sim= models.CharField(blank=True,null=True,verbose_name='إسم المندوب',max_length=50) 
#     cardNotes= models.CharField(blank=True,null=True,verbose_name='إسم المندوب',max_length=50)      

#     #البكر
#     bakar= models.CharField(blank=True,null=True,verbose_name='إسم المندوب',max_length=50)      
#     #يريد التعامل ام لا
#     bakar_intention= models.CharField(blank=True,null=True,verbose_name='إسم المندوب',max_length=50) 
#     #السبب فى عدم التعامل
#     bakar_withdraw= models.CharField(blank=True,null=True,verbose_name='إسم المندوب',max_length=50)     
#     #amountPayBakar
#     bakarFromWho= models.CharField(blank=True,null=True,verbose_name='إسم المندوب',max_length=50)
#     #بيشترى كام فى الشهر
#     bakarNotes   = models.CharField(blank=True,null=True,verbose_name='إسم المندوب',max_length=50)

# class Location(models.Model):
#     #location
#     sellerLangitude= models.CharField(blank=True,null=True,verbose_name='إسم المندوب',max_length=50) 
#     sellerLatittude= models.CharField(blank=True,null=True,verbose_name='إسم المندوب',max_length=50)  

class DataTogar(models.Model):
    # user   = models.ForeignKey(Account,related_name="DataTogar.user+",on_delete = models.PROTECT,verbose_name="المستخدم",null=True,blank=True)
    #timestamp
    test = models.OneToOneField(Test,on_delete=models.CASCADE)
    name2   = models.CharField(blank=False,null=False,max_length=50)
    date    = models.DateField(null=True,verbose_name = "Date",default=timezone.now)
    time    = models.TimeField(null=True,verbose_name = "Time",default=timezone.now)
    


