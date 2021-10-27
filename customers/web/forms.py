from customers import models
from django import forms

from django.forms import Textarea
from django.core.validators import RegexValidator
from django.contrib import admin
from django.utils import timezone
from datetime import date
from phone_field import PhoneField

class FCustomer_info(forms.ModelForm):
    class Meta:
        model = models.CustomerInfo
        fields = '__all__'

# class FCustomer_Image(forms.ModelForm):
#     class Meta:
#         model = models.Customer_Image
#         fields = '__all__'

# class FCustomer(forms.ModelForm):
#     """
#     name,idNo,shopName,shopKind,phoneNo,address,images,date,time
#     """
#     name = forms.CharField(max_length=100,label="الإســم",required=False)
#     idNo = forms.CharField(max_length=11,label="الرقم القومى",required=True)
#     shopName = forms.CharField(max_length=45,label="إسم المحل",required=True)
#     shops=[
#         ("بقالة", "بقالة"),
#         ("منظفات", "منظفات"),
#         ("سنترال", "سنترال"),
#         ("صيانة محمول", "صيانة محمول"),
#         ("إكسسوارات محمول", "إكسسوارات محمول"),
#         ("أدوات صحية", "أدوات صحية"),
#         ("مكتبة", "مكتبة"),
#         ("شخصى", "شخصى"),
#            ]
#     shopKind = forms.MultipleChoiceField( widget=forms.CheckboxSelectMultiple,choices=shops,required=True,label = "نوع المحل")

#     #phoneNo = PhoneField(blank=True, help_text='قم بكتابة رقم التليفون ',label = "رقم التليفون")
    
#     address = forms.CharField(max_length=150,label="العنوان",widget=forms.Textarea(attrs={'rows': 4, 'cols': 20,'style':"height: 77px;"}), required=True)
    
#     #chronicDisease = models.ManyToManyField(ChronicDisease,verbose_name="Chronic Disease",null=True)
#     #diagnosis = models.ManyToManyField(Diagnosis,verbose_name="Diagnosis",null=True)
#     #image1 = forms.ImageField(upload_to="arshiv/Customerimages",label="وجه البطاقة",required=True)
#     #image2 = forms.ImageField(upload_to="arshiv/Customerimages",label="ظهر البطاقة",required=True)
#     #image3 = forms.ImageField(upload_to="arshiv/Customerimages",label="صورة مستند",required=True)

#     # to set head title of form "المستندات"
#     #date = forms.DateField(required=True,label = "Date",default=timezone.now)
#     #time = forms.TimeField(required=True,label = "Time",default=timezone.now) #default=date.today
#     class Meta:
#         model = models.Customer_info
#         fields = ['name','idNo','shopName','shopKind','address']


