from django.db import models
from customers.models import  CustomerInfo
from django.utils import timezone

class RassedProtal(models.Model):
    value= models.FloatField(blank=True,null=True,verbose_name="القيمة")
    note = models.TextField(max_length=150,verbose_name="ملاحظات",null=True,blank=True)

    date = models.DateField(null=True,verbose_name = "Date",default=timezone.now)
    time = models.TimeField(null=True,verbose_name = "Time",default=timezone.now)
    dateTime = models.DateTimeField(null=False,verbose_name = "Date Time",default=timezone.now)

    def __str__(self):
        return str(self.value)

    class Meta:
        verbose_name = "رصيد البورتال"
        verbose_name_plural = "أرصدة البورتال"
        ordering = ['-dateTime']

class TransactionsPortal(models.Model):
    customer = models.ForeignKey(CustomerInfo,related_name="TransactionsPortal.customer+",on_delete = models.PROTECT,verbose_name="العميل",null=False,blank=False)
    
    value= models.FloatField(blank=False,null=False,verbose_name="المبلغ")
    isDone= models.BooleanField(blank=True,null=True,verbose_name="انتهاء السداد")
    isDown= models.BooleanField(blank=True,null=True,verbose_name="سداد أم دفع")

    date = models.DateField(null=False,verbose_name = "Date",default=timezone.now)
    recordDate = models.DateField(null=False,verbose_name = "Record Date",default=timezone.now)

    time = models.TimeField(null=False,verbose_name = "Time",default=timezone.now)
    dateTime = models.DateTimeField(null=False,verbose_name = "Date Time",default=timezone.now)
    dateTimeProtal = models.DateTimeField(null=False,verbose_name = "Date Time Protal",default=timezone.now)

    def __str__(self):
        return str(self.value)

    class Meta:
        verbose_name = "تحويل البورتال"
        verbose_name_plural = "سجل التحويلات البورتال"
        ordering = ['-dateTime']
