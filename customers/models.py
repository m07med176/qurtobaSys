from django.db import models
from django.utils import timezone
# from datetime import date
# from phone_field import PhoneField



class MandopInfo(models.Model):
    """id,name,email"""
    code= models.IntegerField(blank=True,verbose_name="الرقم الكودى",null=True)
    email= models.CharField(blank=True,max_length=100,verbose_name="الإيميل",null=True)
    name= models.CharField(blank=False,max_length=100,verbose_name="إسم المندوب",null=False)
    phone= models.CharField(blank=True,max_length=11,verbose_name="رقم التليفون",null=True)
    region = models.CharField(blank=True,max_length=50,verbose_name="المنطقة",null=True)

    date = models.DateField(null=True,verbose_name = "Date",default=timezone.now)
    time = models.TimeField(null=True,verbose_name = "Time",default=timezone.now) #default=date.today
    
    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "بيانات المندوب"
        verbose_name_plural = "بيانات المناديب"
        managed = True


class CustomerInfo(models.Model):
    """
    name,shopName,shopKind,phoneNo,address,seller,accounts,time,date
    """
    name = models.CharField(blank=False,max_length=100,verbose_name="الإســم",null=False)
    surName = models.CharField(blank=True,max_length=50,verbose_name=" إسم الشهره",null=True)
    shopName = models.CharField(max_length=45,verbose_name="إسم المحل",null=Trueوblank=True)
    deviceNo = models.IntegerField(blank=True,verbose_name="الرقم الكودى",null=True,unique=True)
    shops=[
        ("بقالة", "بقالة"),
        ("منظفات", "منظفات"),
        ("سنترال", "سنترال"),
        ("صيانة محمول", "صيانة محمول"),
        ("إكسسوارات محمول", "إكسسوارات محمول"),
        ("أدوات صحية", "أدوات صحية"),
        ("مكتبة", "مكتبة"),
        ("شخصى", "شخصى"), ]

    shopKind = models.CharField(max_length=50,choices=shops,null=True,verbose_name = "نوع المحل",default=1)
    phoneNo = models.CharField(max_length=11,blank=True, help_text='قم بكتابة رقم التليفون ',verbose_name = "رقم التليفون")
    address = models.TextField(max_length=150,verbose_name="العنوان",null=True,blank=True)
    area = models.CharField(max_length=50,verbose_name="المنطقة",null=True)
    seller = models.ForeignKey('MandopInfo',related_name="seller",on_delete = models.PROTECT,verbose_name="المندوب المسئول",null=False,blank=False)
    # jasonData = { "accountsKind": "فورى", "value": deviceNo}
    # accounts = models.JSONField(default=dict ,null=True,blank=True,verbose_name="حسابات العميل")
    accounts = models.TextField(default="" ,null=True,blank=True,verbose_name="حسابات العميل")

    date = models.DateField(null=True,verbose_name = "Date",default=timezone.now)
    time = models.TimeField(null=True,verbose_name = "Time",default=timezone.now) #default=date.today


    def __str__(self):
        return str(self.name)
    class Meta:
        verbose_name = "عميل"
        verbose_name_plural = "العملاء"
        managed = True
        
class Customer(CustomerInfo):
    class Meta:
        proxy = True
        verbose_name = "إضافة عميل"
        verbose_name_plural = "قائمة العملاء"


# class CustomerAccount(models.Model):
#     accounts=[
#         ("كاش", "كاش"),
#         ("فورى", "فورى"),
#         ("بى", "بى"),
#         ("امان", "امان"),
#         ("اخرى", "اخرى"), ]
#     accountsKind = models.CharField(max_length=50,choices=accounts,null=True,verbose_name = "نوع الحساب",default=2)
#     value = models.CharField(blank=True,max_length=50,verbose_name="رقم الحساب",null=True)


#     def __str__(self):
#         return str(self.value)
#     class Meta:
#         verbose_name = "حسابات المندوب"
#         verbose_name_plural = "حسابات المناديب"
#         managed = True


# class Customer_Image(models.Model):
#     image1 = models.ImageField(upload_to="arshiv/Customerimages",verbose_name="وجه البطاقة",null=True)
#     image2 = models.ImageField(upload_to="arshiv/Customerimages",verbose_name="ظهر البطاقة",null=True)
#     image3 = models.ImageField(upload_to="arshiv/Customerimages",verbose_name="صورة مستند",null=True)
#     class Meta:
#         verbose_name = "صور عميل"
#         verbose_name_plural = "أرشيف صور العملاء"
#         managed = True
#         db_table = 'customers_customer_image'


# -------------------------- Customer Info -------------------------- #
#chronicDisease = models.ManyToManyField(ChronicDisease,verbose_name="Chronic Disease",null=True)
#diagnosis = models.ManyToManyField(Diagnosis,verbose_name="Diagnosis",null=True)
# images = models.OneToOneField(Customer_Image,on_delete = models.CASCADE,verbose_name="المستندات",null=True)
# idNo = models.CharField(max_length=11,verbose_name="الرقم القومى",null=True,blank=True)
# created_at = models.DateTimeField(auto_now_add=True)
# updated_at = models.DateTimeField(auto_now=True)
# ------------------------------------------------------------------------------#

# ### Accounts #### 
# machines=[
#     ("vx520c", "vx520c"),
#     ("vx520 contact", "vx520 contact"),
#     ("nexgo", "nexgo"),
#     ("mobile app", "mobile app"),
#     ("newland", " newland")]
# machineKind = models.CharField(max_length=50,choices=machines,null=True,verbose_name = " نوع المكن",default=1)

# sims=[
# ("vodafone", "vodafone"),
# ("etsalat", "etsalat"),
# ("orange", " orange"),
#     ]
#account = models.OneToOneField('Customer_account',on_delete = models.CASCADE,verbose_name="حساب العميل",null=True)
# sim = models.CharField(max_length=50,choices=sims,null=True,verbose_name = "نوع الشريحه",default=1)


""" 
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation

class Comment(models.Model):
    comm = models.CharField(max_length=50)
    content_type =   models.ForeignKey(ContentType, on_delete = models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object=GenericForeignKey('content_type', 'object_id')
class Article(models.Model):
    content = models.CharField(max_length=100)
    comments = GenericRelation(Comment)
class Post(models.Model):
    content = models.CharField(max_length=100)
    comments = GenericRelation(Comment)
 """
