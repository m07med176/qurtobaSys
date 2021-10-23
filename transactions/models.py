from django.db import models
from customers.models import  CustomerInfo
from django.utils import timezone
from account.models import Account
class Rest(models.Model):
    customer    = models.OneToOneField(CustomerInfo,related_name="Rest.customer+",on_delete = models.CASCADE,verbose_name="العميل",null=False,blank=False)
    value       = models.FloatField(blank=True,null=True,verbose_name="المتبقى")
    date        = models.DateField(null=True,verbose_name = "Date",default=timezone.now)
    time        = models.TimeField(null=True,verbose_name = "Time",default=timezone.now)
    def __str__(self):
        return str(self.value)

    class Meta:
        verbose_name = "المتبقى"
        verbose_name_plural = "المتبقيات"
        managed = True

class Record(models.Model):
    customerData    = models.ForeignKey(CustomerInfo,related_name="customerData",on_delete = models.CASCADE,verbose_name="العميل",null=False,blank=False)
    accountant      = models.ForeignKey(Account,related_name="accountant",on_delete = models.PROTECT,verbose_name="المحاسب",null=True,blank=True)
    accounts=[
        ("فورى", "فورى"),
        ("كاش", "كاش"),
        ("طاير", "طاير"),
        ("بى", "بى"),
        ("أمان", "أمان"),
        ("أخرى", "أخرى"), 
        ("تنزيل", "تنزيل"),
        ("تحصيل", "تحصيل"),
        ]
    type            = models.CharField(max_length=50,choices=accounts,null=False,verbose_name = "نوع الحساب",default=1)
    
    value           = models.FloatField(blank=False,null=False,verbose_name="المبلغ")
    isDone          = models.BooleanField(blank=True,null=True,verbose_name="انتهاء السداد")
    isDown          = models.BooleanField(blank=True,null=True,verbose_name="تحويل أم تنزبل")

    date            = models.DateField(null=False,verbose_name = "Date",default=timezone.now)
    time            = models.TimeField(null=False,verbose_name = "Time",default=timezone.now)
    
    notes           = models.TextField(max_length=150,verbose_name="الملاحظات",null=True,blank=True)

    def __str__(self):
        return self.type+" ("+str(self.value)+") "+str(self.date)+"|"+str(self.time)

    class Meta:
        verbose_name = "تحويل"
        verbose_name_plural = "سجل التحويلات"
        managed = True

class Talabat(models.Model):
    "sender,type,periority,stateTrans,date"
    user    = models.ForeignKey(Account,related_name="Talabat.account+",on_delete = models.CASCADE,verbose_name="العميل",null=True,blank=True)
    senderTypes=[
        (1,"عميل"),
        (2, "مندوب"),
        (3, "محصل"),
        (4, "مشرف"),
        ]
    sender      = models.IntegerField(choices=senderTypes,default=1,null=False,verbose_name = "المرسل")
    
    accounts=[
        ("فورى", "فورى"),
        ("كاش", "كاش"),
        ("طاير", "طاير"),
        ("بى", "بى"),
        ("أمان", "أمان"),
        ("أخرى", "أخرى"), 
        ("تنزيل", "تنزيل"),]
    type       = models.CharField(max_length=50,choices=accounts,null=False,verbose_name = "نوع الحساب",default=1)
    value      = models.FloatField(blank=False,null=False,verbose_name="المبلغ")
    perioritesType=[
        (1, "عادى"),
        (2, "مستعجل"),
        (3, "مستعجل جداً"),
        (4, "مستعجل للغاية"),
    ]
    periority  = models.IntegerField(verbose_name="الاولوية",choices=perioritesType,default=1,null=True,blank=True)
    transType=[
        (1, "تم الطلب"),
        (2, "جارى تنفيذ الطلب"),
        (3, "طلب ناجح"),
        (4, "طلب فاشل"),
        (5, "طلب موفوف"),
        (6, "طلب معطل"),
        (7, "طلب مسحوب"),
    ]
    stateTrans = models.IntegerField(verbose_name="حالة الطلب",choices=transType,default=1,null=True,blank=True)

    date       = models.DateField(null=False,verbose_name = "Date",default=timezone.now)
    time       = models.TimeField(null=False,verbose_name = "Time",default=timezone.now)
    dateTime   = models.DateTimeField(null=False,verbose_name = "Date Time",default=timezone.now)

    def __str__(self):
        return str(self.type)

    class Meta:
        verbose_name = "طلب"
        verbose_name_plural = "سجل الطلبات"
        ordering = ['-dateTime']



