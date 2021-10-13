from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class MyAccountManager(BaseUserManager):
	def create_user(self, phoneNo,email, username, password=None):
		if not email:
			raise ValueError('Users must have an email address')
		if not username:
			raise ValueError('Users must have a username')
		if not phoneNo:
			raise ValueError('Users must have a phone number')
		
		user = self.model(
			email=self.normalize_email(email),
			username=username,
			phoneNo=phoneNo,
		)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, phoneNo,email, username, password):
		user = self.create_user(
			email=self.normalize_email(email),
			password=password,
			username=username,
			phoneNo=phoneNo,
		)
		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)
		return user


class Account(AbstractBaseUser):
	email = models.EmailField(verbose_name="الإيميل", max_length=60, unique=True,help_text='مطلوب إضافة الايميل')
	username = models.CharField(verbose_name="إسم المستخدم",max_length=30, unique=True,help_text='مطلوب إضافة الإســم')
	phone = models.CharField(max_length=11,unique=True,blank=False,verbose_name = "رقم التليفون",help_text='مطلوب إضافة رقم التليفون')
	account_no = models.IntegerField(blank=True,verbose_name="الرقم الكودى",null=True,unique=True,help_text='مطلوب إضافة رقم الحساب')
	
	date_joined				= models.DateTimeField(verbose_name='تاريخ التسجيل', auto_now_add=True)
	last_login				= models.DateTimeField(verbose_name='أخر دخول', auto_now=True)
	
	is_superuser			= models.BooleanField(default=False,verbose_name = 'مسئول عام')
	is_admin				= models.BooleanField(default=False,verbose_name = 'مدير')
	is_staff				= models.BooleanField(default=False,verbose_name = 'محاسب')
	is_active				= models.BooleanField(default=True,verbose_name = 'نشط')

	is_customer				= models.BooleanField(default=False,verbose_name = 'عميل')
	is_accepted				= models.BooleanField(default=False,verbose_name = 'مقبول')

	hide_email				= models.BooleanField(default=True,verbose_name = 'إخفاء الايميل')

	USERNAME_FIELD = 'phone'
	REQUIRED_FIELDS = ['email']

	objects = MyAccountManager()

	def __str__(self):
		return self.username

	# For checking permissions. to keep it simple all admin have ALL permissons
	def has_perm(self, perm, obj=None):
		return self.is_admin

	# Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
	def has_module_perms(self, app_label):
		return True