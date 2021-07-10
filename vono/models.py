from django.db import models

class District(models.Model):
    district_name = models.CharField(max_length=50,null=False,verbose_name="إسم القطاع")
    selected = models.BooleanField(default=False)

class Area(models.Model):
    area_name = models.CharField(max_length=50,null=False,verbose_name="إسم المنطقة")
    selected = models.BooleanField(default=False)
    district = models.ForeignKey(District,on_delete = models.CASCADE,verbose_name="القطاع",null=False)
    
class Branch(models.Model):
    branch_name = models.CharField(max_length=50,null=False,verbose_name="إسم الفرع")
    selected = models.BooleanField(default=False)
    area = models.ForeignKey(Area,on_delete = models.CASCADE,verbose_name="المنطقة",null=False)

class ROR(models.Model):
    date_record = models.DateField(null=False,auto_now = True,verbose_name = "تاريخ التسجيل")

class VodafoneNumber(models.Model):
    number = models.CharField(max_length=15,null=True,verbose_name = "رقم التليفون")
    area = models.CharField(max_length=50,null=True,verbose_name = "المنطقة")
    branch = models.CharField(max_length=50,null=True,verbose_name = "الفرع")
    best  = models.IntegerField(default=0,null=True,verbose_name = "الأفضل")
    reviewer = models.CharField(max_length=50,null=True,verbose_name = "المراجع")
    version = models.DateField(verbose_name = "اخر إصدار",null=True)
    date_record = models.DateField(auto_now = True,null=True,verbose_name = "تاريخ إصداره")
    deleted = models.BooleanField(default=False,null=True,verbose_name = "تم مسحه؟")
