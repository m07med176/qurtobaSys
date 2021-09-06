from django.db import models
from customers.models import  CustomerInfo
from django.utils import timezone

class Rest(models.Model):
    customer = models.OneToOneField(CustomerInfo,related_name="customer",on_delete = models.CASCADE,verbose_name="العميل",null=False,blank=False)
    value= models.FloatField(blank=True,null=True,verbose_name="المتبقى")
    date = models.DateField(null=True,verbose_name = "Date",default=timezone.now)
    time = models.TimeField(null=True,verbose_name = "Time",default=timezone.now)
    def __str__(self):
        return str(self.value)

    class Meta:
        verbose_name = "المتبقى"
        verbose_name_plural = "المتبقيات"
        managed = True

class Record(models.Model):
    customerData = models.ForeignKey(CustomerInfo,related_name="customerData",on_delete = models.CASCADE,verbose_name="العميل",null=False,blank=False)
    accounts=[
        ("فورى", "فورى"),
        ("كاش", "كاش"),
        ("طاير", "طاير"),
        ("بى", "بى"),
        ("أمان", "أمان"),
        ("أخرى", "أخرى"), 
        ("تنزيل", "تنزيل"),]
    type = models.CharField(max_length=50,choices=accounts,null=False,verbose_name = "نوع الحساب",default=1)
    
    value= models.FloatField(blank=False,null=False,verbose_name="المبلغ")
    isDone= models.BooleanField(blank=True,null=True,verbose_name="انتهاء السداد")
    isDown= models.BooleanField(blank=True,null=True,verbose_name="تحويل أم تنزبل")

    date = models.DateField(null=False,verbose_name = "Date",default=timezone.now)
    time = models.TimeField(null=False,verbose_name = "Time",default=timezone.now)
    
    def __str__(self):
        return str(self.type)

    class Meta:
        verbose_name = "تحويل"
        verbose_name_plural = "سجل التحويلات"
        managed = True
