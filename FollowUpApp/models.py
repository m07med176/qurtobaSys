from django.db import models
from django.utils import timezone
import datetime


class Employers(models.Model):
    """ uid,email,name,image,phone,date_joined,last_login,is_superuser,is_admin,is_staff,is_active,type"""

    uid        = models.CharField(verbose_name="UID",null=False,blank=False,max_length=100, unique=False,help_text='مطلوب إضافة الايميل')
    email      = models.CharField(verbose_name="الايميل",null=False,blank=False,max_length=100)
    name       = models.CharField(verbose_name="الإسم",null=False,blank=False,max_length=30)
    image      = models.CharField(verbose_name="الصورة الشخصية",null=True,blank=True,max_length=300)
    phone      = models.CharField(max_length=11,unique=True,blank=True,null=True,verbose_name = "رقم التليفون",help_text='مطلوب إضافة رقم التليفون')

    date_joined				= models.DateTimeField(verbose_name='تاريخ التسجيل', auto_now_add=True)
    last_login				= models.DateTimeField(verbose_name='أخر دخول', auto_now=True)

    is_superuser			= models.BooleanField(null=False,blank=False,default=False,verbose_name = 'مسئول عام')
    is_admin				= models.BooleanField(null=False,blank=False,default=False,verbose_name = 'مدير')
    is_staff				= models.BooleanField(null=False,blank=False,default=False,verbose_name = 'محاسب')
    is_active				= models.BooleanField(null=False,blank=False,default=False,verbose_name = 'نشط')

    choices = [ (0, 'محاسب'), (1, 'مندوب'), (2, 'عميل'), (3, 'محصل'), (4, 'محول'), (5, 'مدير'), ]
    type				    = models.IntegerField(choices=choices,default=0,verbose_name="نوع الحساب")


    def __str__(self): return self.name

    class Meta:
        verbose_name = "الموظف"
        verbose_name_plural = "الموظفين"
        ordering = ['-last_login']

class FollowUp(models.Model):
    "name,email,uid,day,startTime,endTime,duration,dateTime,transport,notes"
    user      = models.ForeignKey(Employers,related_name="FollowUp.user+",on_delete = models.PROTECT,verbose_name="الموظف",null=True,blank=True)
    is_active  = models.BooleanField(verbose_name="متاح",null=False,blank=False,default=False)
    
    day        = models.DateField(blank=True,null=True,verbose_name = "اليوم")
    startTime  = models.TimeField(blank=True,null=True,verbose_name = "بداية اليوم")
    endTime    = models.TimeField(blank=True,null=True,verbose_name = "نهاية اليوم")
    duration   = models.TimeField(blank=True,null=True,verbose_name = "الفترة")
    dateTime   = models.DateTimeField(blank=True,null=True,verbose_name = "Date Time",default=timezone.datetime.today)
    transport  = models.FloatField(blank=True,null=True,verbose_name="تكلفة المواصلات",default=0)
    notes      = models.TextField(blank=True,null=True,verbose_name="الملاحظات",default="")

    
    def __str__(self): return str(self.duration)+"-"+str(self.user.name)

    class Meta:
        verbose_name = "متابعه"
        verbose_name_plural = "المتابعات"
        ordering = ['-dateTime']
