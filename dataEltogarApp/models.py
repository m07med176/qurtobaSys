from django.db import models

class DataTogar(models.Model):
        #بيانات التاجر
    nameOfMandoop   = models.CharField(blank=True,null=True,verbose_name='إسم المندوب',max_length=50,)
    activityKind    = models.CharField(blank=True,null=True,verbose_name='إسم المندوب',max_length=50)
    address         = models.CharField(blank=True,null=True,verbose_name='إسم المندوب',max_length=50) 
    area            = models.CharField(blank=True,null=True,verbose_name='إسم المندوب',max_length=50)

    evaluate        = models.CharField(blank=True,null=True,verbose_name='إسم المندوب',max_length=50)
    notes           = models.CharField(blank=True,null=True,verbose_name='إسم المندوب',max_length=50)      
    phoneNumber     = models.CharField(blank=True,null=True,verbose_name='إسم المندوب',max_length=50) 
    shopName        = models.CharField(blank=True,null=True,verbose_name='إسم المندوب',max_length=50)
    ownerName       = models.CharField(blank=True,null=True,verbose_name='إسم المندوب',max_length=50)   

    #timestamp
    time= models.CharField(blank=True,null=True,verbose_name='إسم المندوب',max_length=50)
    date= models.CharField(blank=True,null=True,verbose_name='إسم المندوب',max_length=50)

    #location
    sellerLangitude= models.CharField(blank=True,null=True,verbose_name='إسم المندوب',max_length=50) 
    sellerLatittude= models.CharField(blank=True,null=True,verbose_name='إسم المندوب',max_length=50)  

    #الطاير
    intention= models.CharField(blank=True,null=True,verbose_name='إسم المندوب',max_length=50)      
    tayer= models.CharField(blank=True,null=True,verbose_name='إسم المندوب',max_length=50)      
    tayerFromWho= models.CharField(blank=True,null=True,verbose_name='إسم المندوب',max_length=50)
    amountPayTayer= models.CharField(blank=True,null=True,verbose_name='إسم المندوب',max_length=50)  

    #الكاش
    cash= models.CharField(blank=True,null=True,verbose_name='إسم المندوب',max_length=50)
    intent_cash= models.CharField(blank=True,null=True,verbose_name='إسم المندوب',max_length=50) 
    amountPayCash= models.CharField(blank=True,null=True,verbose_name='إسم المندوب',max_length=50)   

    #المحمول
    kindOfMobile= models.CharField(blank=True,null=True,verbose_name='إسم المندوب',max_length=50)
    mobileNotes= models.CharField(blank=True,null=True,verbose_name='إسم المندوب',max_length=50) 
    mobileFromWhow= models.CharField(blank=True,null=True,verbose_name='إسم المندوب',max_length=50) 

    #الدفع الإلكترونى
    machinesOfepay= models.CharField(blank=True,null=True,verbose_name='إسم المندوب',max_length=50)     
    machinesOfepayIsNeedMachine= models.CharField(blank=True,null=True,verbose_name='إسم المندوب',max_length=50) 
    amountOfTreat= models.CharField(blank=True,null=True,verbose_name='إسم المندوب',max_length=50) 

    #الكارت
    sim= models.CharField(blank=True,null=True,verbose_name='إسم المندوب',max_length=50) 
    cardNotes= models.CharField(blank=True,null=True,verbose_name='إسم المندوب',max_length=50)      

    #البكر
    bakar= models.CharField(blank=True,null=True,verbose_name='إسم المندوب',max_length=50)      
    #يريد التعامل ام لا
    bakar_intention= models.CharField(blank=True,null=True,verbose_name='إسم المندوب',max_length=50) 
    #السبب فى عدم التعامل
    bakar_withdraw= models.CharField(blank=True,null=True,verbose_name='إسم المندوب',max_length=50)     
    #amountPayBakar
    bakarFromWho= models.CharField(blank=True,null=True,verbose_name='إسم المندوب',max_length=50)
    #بيشترى كام فى الشهر
    bakarNotes   = models.CharField(blank=True,null=True,verbose_name='إسم المندوب',max_length=50)