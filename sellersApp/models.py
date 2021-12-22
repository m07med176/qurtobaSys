from django.db import models
from customers.models import  MandopInfo
from django.utils import timezone
from account.models import Account


class SellerRecord(models.Model):
    seller          = models.ForeignKey(MandopInfo,related_name="Store.seller+",on_delete = models.PROTECT,verbose_name="المندوب",null=True,blank=True)
    accountant      = models.ForeignKey(Account,related_name="Store.accountant+",on_delete = models.PROTECT,verbose_name="المحاسب",null=True,blank=True)
    accounts=[
        (1, "أرصدة"),
        (2, "تنزيل"),
        (3, "تحصيل"),
        (4, "شراء"),
        (5, "الدفع"),
        ]
    type            = models.IntegerField(choices=accounts,blank=True,null=True,verbose_name = "نوع الحساب")
    rest            = models.FloatField(default=0,blank=True,null=True,verbose_name="المتبقى")
    value           = models.FloatField(blank=False,null=False,verbose_name="المبلغ")
    isDone          = models.BooleanField(default=False,blank=True,null=True,verbose_name="انتهاء السداد")
    isDown          = models.BooleanField(default=False,blank=True,null=True,verbose_name="تحويل أم تنزبل")

    date            = models.DateField(null=False,verbose_name = "Date",default=timezone.now)
    time            = models.TimeField(null=False,verbose_name = "Time",default=timezone.now)
    datetime        = models.DateTimeField(null=True,verbose_name = "DateTime",default=timezone.datetime.now)
    
    notes           = models.TextField(max_length=150,verbose_name="الملاحظات",null=True,blank=True)

    def __str__(self):
        return self.type+" ("+str(self.value)+") "+str(self.date)+"|"+str(self.time)

    class Meta:
        verbose_name = "مبيعات"
        verbose_name_plural = "سجل المبيعات"
        managed = True
