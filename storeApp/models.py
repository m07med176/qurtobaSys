from django.db import models
from account.models import Account
from customers.models import CustomerInfo
from django.utils import timezone

class Store(models.Model):
    """id,name,serial,account,type,sanf,stage,price"""
    name    = models.CharField(blank=True,max_length=50,verbose_name="إسم الحساب",null=True)
    serial    = models.CharField(blank=True,max_length=50,verbose_name="رقم السيريال",null=True,unique=True)
    account     = models.IntegerField(blank=True,null=True,verbose_name="رقم الحساب")

    types=[
        (1, "فورى"),
        (2, "كاش"),
        (3, "طاير"),
        (4, "بى"),
        (5, "أمان"),
        ]
    type            = models.IntegerField(choices=types,null=True,blank=True,verbose_name = "نوع الحساب")
    asnaf=[
        (1, "520 Contact كسر"),
        (2, "520 Contact زيرو بدون بطارية"),
        (3, "520 Contact كسر بدون بطارية"),
        (5, "520 Contact زيرو"),
        (6, "520 C كسر"), 
        (7, "nexgo نكس جو"),
        (8, "موبايل كاش"),
        (9, "موبايل فورى"),
        ]
    sanf            = models.IntegerField(choices=asnaf,null=True,blank=True,verbose_name = "نوع الصنف")
    stages=[
        (1, "new machine"),
        (2, "created"),
        (3, "portal"),
        (4, "validate"),
        (5, "working"),
        ]
    stage            = models.IntegerField(choices=stages,null=True,blank=True,verbose_name = "نوع المخزن",default=1)
    price           = models.FloatField(blank=True,null=True,verbose_name="السعر")


    date        = models.DateField(null=False,verbose_name = "التاريخ",default=timezone.now)
    time        = models.TimeField(null=False,verbose_name = "الوقت",default=timezone.now)
    notes       = models.TextField(max_length=150,verbose_name="الملاحظات",null=True,blank=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)    
    user        = models.ForeignKey(Account,related_name="Store.user+",on_delete=models.SET_NULL,verbose_name="المحاسب",null=True,blank=True)
    customer    = models.ForeignKey(CustomerInfo,related_name="Store.customer+",on_delete=models.SET_NULL,verbose_name="تابع لحساب",null=True,blank=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "إدارة الحسابات والمخازن"
        verbose_name_plural = "حساب"
        managed = True