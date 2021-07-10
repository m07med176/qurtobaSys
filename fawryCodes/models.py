from django.db import models
from django.utils import timezone
from datetime import date


class FawryCodes(models.Model):
    serviceName = models.CharField(blank=False,max_length=100,verbose_name="إسم الخدمة",null=False)
    serviceCode = models.CharField(blank=False,max_length=100,verbose_name="كود الخدمة",null=False)
    serviceKind = models.CharField(blank=False,max_length=100,verbose_name="نوع الخدمة",null=False)
    datetime = models.DateTimeField(null=True,verbose_name = "DateTime",default=timezone.now)
    date = models.DateField(null=True,verbose_name = "التاريخ",default=timezone.now)
    time = models.TimeField(null=True,verbose_name = "الوقت",default=timezone.now) #default=date.today
    
    def __str__(self):
        return str(self.serviceName)

    class Meta:
        verbose_name = "كود فورى"
        verbose_name_plural = "أكواد فورى"
        managed = True

