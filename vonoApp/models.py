from django.db import models
from account.models import Account
from django.utils import timezone
class District(models.Model):
    district_name = models.CharField(max_length=50,null=False,verbose_name="إسم القطاع")
    selected = models.BooleanField(default=False)
    class Meta:
        db_table = "District"
        verbose_name = "القطاع"
        verbose_name_plural = "القطاعات"
        ordering = ['-district_name']

class Area(models.Model):
    area_name = models.CharField(max_length=50,null=False,verbose_name="إسم المنطقة")
    selected = models.BooleanField(default=False)
    district = models.ForeignKey(District,on_delete = models.CASCADE,verbose_name="القطاع",null=False)
    class Meta:
        db_table = "Area"
        verbose_name = "المنطقة"
        verbose_name_plural = "المناطق"
        ordering = ['-area_name']

class Branch(models.Model):
    branch_name = models.CharField(max_length=50,null=False,verbose_name="إسم الفرع")
    selected = models.BooleanField(default=False)
    area = models.ForeignKey(Area,on_delete = models.CASCADE,verbose_name="المنطقة",null=False)
    class Meta:
        db_table = "Branch"
        verbose_name = "الفرع"
        verbose_name_plural = "الفرع"
        ordering = ['-branch_name']

class ROR(models.Model):
    date_record = models.DateField(null=False,auto_now = True,verbose_name = "تاريخ التسجيل")


class VodafoneNumber(models.Model):
    number = models.CharField(max_length=15,null=True,verbose_name = "رقم التليفون")
    best  = models.IntegerField(default=0,null=True,verbose_name = "الأفضل")

    # relations
    area = models.ForeignKey(Area,on_delete = models.CASCADE,verbose_name="المنطقة",null=False)
    branch = models.ForeignKey(Branch,on_delete = models.CASCADE,verbose_name="الفرع",null=False)
    reviewer  = models.ForeignKey(Account,related_name="VodafoneNumber.user+",on_delete = models.PROTECT,verbose_name="تابع لحساب",null=True,blank=True)

    # validation
    is_deleted      = models.BooleanField(default=False,null=True,verbose_name = "تم مسحه")
    is_available    = models.BooleanField(default=False,null=True,verbose_name = "متاح للعرض")

    # time stamp
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    version = models.DateField(verbose_name = "اخر إصدار",null=True,default=timezone.now)
    date_record = models.DateField(auto_now = True,null=True,verbose_name = "تاريخ إصداره")

    def __str__(self):
        return str(self.number)
    class Meta:
        db_table = "VodafoneNumber"
        verbose_name = "رقم فودافون"
        verbose_name_plural = "أرقام فودافون"
        ordering = ['-updated_at']



# ------------------ this model for show only ----------------------- #
class VodafoneNumberShow(models.Model):
    number = models.CharField(max_length=15,null=True,verbose_name = "رقم التليفون")
    area = models.CharField(max_length=50,null=True,verbose_name = "المنطقة")
    branch = models.CharField(max_length=50,null=True,verbose_name = "الفرع")
    best  = models.IntegerField(default=0,null=True,verbose_name = "الأفضل")
    reviewer = models.CharField(max_length=50,null=True,verbose_name = "المراجع")
    version = models.DateField(verbose_name = "اخر إصدار",null=True)
    date_record = models.DateField(auto_now = True,null=True,verbose_name = "تاريخ إصداره")
    deleted = models.BooleanField(default=False,null=True,verbose_name = "تم مسحه؟")
    def __str__(self):
        return str(self.number)
    class Meta:
        db_table = "VodafoneNumberShow"
        verbose_name = "عرض رقم فودافون "
        verbose_name_plural = " عرض أرقام فودافون"
        ordering = ['-area']
