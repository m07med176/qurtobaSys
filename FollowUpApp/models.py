from django.db import models
from django.utils import timezone
import datetime
class FollowUp(models.Model):
    "name,email,uid,day,startTime,endTime,duration,dateTime,transport,notes"
    uid        = models.CharField(verbose_name="UID",null=False,blank=False,max_length=100)
    email      = models.CharField(verbose_name="الايميل",null=False,blank=False,max_length=100)
    name       = models.CharField(verbose_name="الإسم",null=False,blank=False,max_length=30)
    day        = models.DateField(blank=True,null=True,verbose_name = "اليوم")
    startTime  = models.TimeField(blank=True,null=True,verbose_name = "بداية اليوم")
    endTime    = models.TimeField(blank=True,null=True,verbose_name = "نهاية اليوم")
    duration   = models.TimeField(blank=True,null=True,verbose_name = "الفترة")
    dateTime   = models.DateTimeField(blank=True,null=True,verbose_name = "Date Time",default=timezone.datetime.today)
    transport  = models.FloatField(blank=True,null=True,verbose_name="تكلفة المواصلات",default=0)
    notes      = models.TextField(blank=True,null=True,verbose_name="الملاحظات",default="")
    is_active  = models.BooleanField(verbose_name="متاح",null=False,blank=False,default=False)

    
    def __str__(self): return str(self.duration)+"-"+str(self.name)

    class Meta:
        verbose_name = "متابعه"
        verbose_name_plural = "المتابعات"
        ordering = ['-dateTime']
