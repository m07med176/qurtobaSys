from django.db import models
from django.utils import timezone
from datetime import date
#from phone_field import PhoneField



class Customer_account(models.Model):
    """

    """
    name = models.CharField(blank=False,max_length=100,verbose_name="الإســم",null=False)
    idNo = models.CharField(max_length=11,verbose_name="العنوان",null=True)
    
    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "حساب العميل"
        verbose_name_plural = "حساب العملاء"
        managed = True
        db_table = 'customers_customer_account'

# class Customer_Image(models.Model):
#     image1 = models.ImageField(upload_to="arshiv/Customerimages",verbose_name="وجه البطاقة",null=True)
#     image2 = models.ImageField(upload_to="arshiv/Customerimages",verbose_name="ظهر البطاقة",null=True)
#     image3 = models.ImageField(upload_to="arshiv/Customerimages",verbose_name="صورة مستند",null=True)
#     class Meta:
#         verbose_name = "صور عميل"
#         verbose_name_plural = "أرشيف صور العملاء"
#         managed = True
#         db_table = 'customers_customer_image'

class Customer_info(models.Model):
    """
    name
    idNo
    shopName
    shopKind
    phoneNo
    address
    images
    date
    time
    """
    name = models.CharField(blank=False,max_length=100,verbose_name="الإســم",null=False)
    idNo = models.CharField(max_length=11,verbose_name="الرقم القومى",null=True)
    shopName = models.CharField(max_length=45,verbose_name="إسم المحل",null=True)
    shops=[
        ("بقالة", "بقالة"),
        ("منظفات", "منظفات"),
        ("سنترال", "سنترال"),
        ("صيانة محمول", "صيانة محمول"),
        ("إكسسوارات محمول", "إكسسوارات محمول"),
        ("أدوات صحية", "أدوات صحية"),
        ("مكتبة", "مكتبة"),
        ("شخصى", "شخصى"),
           ]
    shopKind = models.CharField(max_length=50,choices=shops,null=True,verbose_name = "نوع المحل",default=1)
    phoneNo = models.CharField(max_length=11,blank=True, help_text='قم بكتابة رقم التليفون ',verbose_name = "رقم التليفون")
    address = models.TextField(max_length=150,verbose_name="العنوان",null=True)
    
    #chronicDisease = models.ManyToManyField(ChronicDisease,verbose_name="Chronic Disease",null=True)
    #diagnosis = models.ManyToManyField(Diagnosis,verbose_name="Diagnosis",null=True)
    # images = models.OneToOneField(Customer_Image,on_delete = models.CASCADE,verbose_name="المستندات",null=True)
    #account = models.OneToOneField('Customer_account',on_delete = models.CASCADE,verbose_name="حساب العميل",null=True)
    date = models.DateField(null=True,verbose_name = "Date",default=timezone.now)
    time = models.TimeField(null=True,verbose_name = "Time",default=timezone.now) #default=date.today
    

    ### Accounts #### 
    machines=[
        ("vx520c", "vx520c"),
        ("vx520 contact", "vx520 contact"),
        ("nexgo", "nexgo"),
        ("mobile app", "mobile app"),
        ("newland", " newland")]
    machineKind = models.CharField(max_length=50,choices=machines,null=True,verbose_name = " نوع المكن",default=1)
    
    sims=[
    ("vodafone", "vodafone"),
    ("etsalat", "etsalat"),
    ("orange", " orange"),
        ]
    sim = models.CharField(max_length=50,choices=sims,null=True,verbose_name = "نوع الشريحه",default=1)

    def __str__(self):
        return str(self.name)
    class Meta:
        verbose_name = "عميل"
        verbose_name_plural = "العملاء"
        managed = True
        db_table = 'customers_customer_info'
        
class Customer(Customer_info):
    class Meta:
        proxy = True
        verbose_name = "إضافة عميل"
        verbose_name_plural = "قائمة العملاء"










""" from django.contrib.contenttypes.fields import GenericForeignKey
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
