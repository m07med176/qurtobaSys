from django.db import models
from customers.models import  MandopInfo
from django.utils import timezone

class SellerRecord(models.Model):
    seller = models.ForeignKey(MandopInfo,related_name="customerData",on_delete = models.PROTECT,verbose_name="العميل",null=False,blank=False)
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
    isDown= models.BooleanField(blank=True,null=True,verbose_name="سداد أم دفع")

    date = models.DateField(null=False,verbose_name = "Date",default=timezone.now)
    time = models.TimeField(null=False,verbose_name = "Time",default=timezone.now)
    dateTime = models.DateTimeField(null=False,verbose_name = "Date Time",default=timezone.now)

    def __str__(self):
        return str(self.type)

    class Meta:
        verbose_name = "مبيعات"
        verbose_name_plural = "سجل المبيعات"
        ordering = ['-dateTime']
