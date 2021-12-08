from django.db import models
from account.models import Account
from django.utils import timezone
import datetime
class Shakawa(models.Model):
    "user,kind,content,date,time,datetime,is_deleted"
    user    = models.ForeignKey(Account,related_name="Shakawa.account+",on_delete = models.CASCADE,verbose_name="العميل",null=True,blank=True)
    type=[
        (0, "عام"),
        (1, "مكن"),
        (2, "تحويل"),
        (3, "كاش"),
        (4, "فورى"),
        (5, "أمان"),
    ]
    kind = models.IntegerField(verbose_name="نوع المشكلة",choices=type,default=1,null=True,blank=True)

    content = models.TextField(verbose_name="المشكلة",null=False,blank=False)
    is_deleted = models.BooleanField(verbose_name="تم مسحه",null=False,blank=False,default=False)

    date       = models.DateField(blank=True,null=True,verbose_name = "Date",default=timezone.now)
    time       = models.TimeField(blank=True,null=True,verbose_name = "Time",default=timezone.now)
    dateTime   = models.DateTimeField(blank=True,null=True,verbose_name = "Date Time",default=timezone.datetime.today)

    def __str__(self):
        return str(self.content)

    class Meta:
        verbose_name = "شكوى"
        verbose_name_plural = "سجل الشكاوى"
        ordering = ['-dateTime']