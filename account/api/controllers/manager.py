# ------------ API AND  APIVIEW AND VIEWSETS-----------#

from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination

from django.contrib.auth import authenticate
# API UTILS
from rest_framework import status
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.filters import SearchFilter,OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from account.api.pagination import LargeResultsSetPagination

# VIEWSETS
from rest_framework import viewsets
# APIVIEW
from rest_framework.views import APIView
# ------------ SERIALIZERS -----------#
from account.api.serializers import (
	SAccountResponse,
	SAccountAll,
	SAccountManager,
	SAccountManagerForCustomer)
from rest_framework.authtoken.models import Token
# ------------ MODELS -----------#
from account.models import Account

# region General Functions
# url: http://127.0.0.1:8000/account/api/updateActivation/<int:id>/
@api_view(['PUT',])
def updateUserActivationAccountManager(request,id):
	if request.method == 'PUT':
		context = {}
		try:
			account = Account.objects.get(pk=id)
		except Account.DoesNotExist:
			return Response(status=status.HTTP_404_NOT_FOUND)
		
		is_active = request.data.get('is_active')
		account.is_active = is_active
		account.save()
		context['message'] = "تم التعديل بنجاح."
		context['status'] = True
		return Response(context)

# url: http://127.0.0.1:8000/account/api/state/<int:id>/
@api_view(['GET', ])
def getUserState(request,id):
	try:
		account = Account.objects.get(pk=id)
		return Response(SAccountResponse(account).data)
	except Account.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

# url: http://127.0.0.1:8000/account/api/getManager/
class GetAccountManage(ListAPIView):
	pagination_class = PageNumberPagination
	PageNumberPagination.page_size = 200
	queryset = Account.objects.get_queryset().order_by('id')
	serializer_class = SAccountAll
	permission_classes = [IsAuthenticated,]
	filter_backends  =  [SearchFilter,OrderingFilter,DjangoFilterBackend]
	filterset_fields =  ["is_superuser","is_admin","is_staff","is_active","type"]
	search_fields    =  ["email","username","phone","account_no"]
	ordering_fields  =  ['date_joined','last_login','id']

# endregion General Functions

# region CUSTOMERS
# url: http://127.0.0.1:8000/account/api/registerManagerCustomer/
@api_view(['POST',])
def registerAccountManagerCustomer(request):
	if request.method == 'POST':
		context = {}

		phone = request.data.get('phone', '0')
		if validate_phone(phone) != None:
			context['response'] = 'رقم المحمول هذا مستخدم من قبل.'
			context['status'] = False
			return Response(context)

			
		serializers = SAccountManagerForCustomer(data=request.data)
		if serializers.is_valid():
			return serializers.save()
		else:
			return Response({"message": "عفواً حدث خطأ أثناء التسجيل","status":  False})

# url: http://127.0.0.1:8000/account/api/updateManager/<int:id>/
@api_view(['PUT',])
def updateAccountManagerCustomer(request,id):
	if request.method == 'PUT':
		context = {}
		try:
			account = Account.objects.get(pk=id)
		except Account.DoesNotExist:
			return Response(status=status.HTTP_404_NOT_FOUND)
		serializers = SAccountManager(instance=account,data=request.data)  
		if serializers.is_valid():
			serializers.update(account)
			context = SAccountResponse(account).data
			context['message'] = "تم التعديل بنجاح."
			context['status'] = True
			return Response(context)
		else:
			return Response(serializers.errors)

# url: http://127.0.0.1:8000/account/api/deleteManager/<int:id>/
@api_view(['DELETE',])
def deleteAccountManagerCustomer(request,id):
	if request.method == 'DELETE':
		context = {}
		try:
			token = Token.objects.get(user_id=id)
			account = Account.objects.get(pk=id)
		except Account.DoesNotExist:
			return Response(status=status.HTTP_404_NOT_FOUND)
		token.delete()
		account.delete()
		context['message'] = "تم الحذف بنجاح ."
		context['status'] = True
		return Response(context)


# endregion CUSTOMERS

# region USERS
# url: http://127.0.0.1:8000/account/api/registerAccountManager/
@api_view(['POST',])
def registerAccountManager(request):
	if request.method == 'POST':
		context = {}
		email = request.data.get('email', '0').lower()
		if validate_email(email) != None:
			context['message'] = 'هذا الإيميل مستخدم من قبل.'
			context['status'] = False
			return Response(context)

		username = request.data.get('username', '0')
		if validate_username(username) != None:
			context['message'] = 'هذا الإسم مستخدم من قبل.'
			context['status'] = False
			return Response(context)

		account_no = request.data.get('account_no', '0')
		if validate_account_no(account_no) != None:
			context['message'] = 'هذا الرقم مستخدم من قبل.'
			context['status'] = False
			return Response(context)

		phone = request.data.get('phone', '0')
		if validate_phone(phone) != None:
			context['response'] = 'رقم المحمول هذا مستخدم من قبل.'
			context['status'] = False
			return Response(context)

		serializers = SAccountManager(data=request.data)
		if serializers.is_valid():
			account = serializers.save()
			context = SAccountResponse(account).data
			context['message'] = "تم التسجيل بنجاح."
			context['status'] = True
			return Response(context)
		else:
			return Response(serializers.errors)


# url: http://127.0.0.1:8000/account/api/updateManager/<int:id>/
@api_view(['PUT',])
def updateAccountManager(request,id):
	if request.method == 'PUT':
		context = {}
		try:
			account = Account.objects.get(pk=id)
		except Account.DoesNotExist:
			return Response(status=status.HTTP_404_NOT_FOUND)
		serializers = SAccountManager(instance=account,data=request.data)  
		if serializers.is_valid():
			serializers.update(account)
			context = SAccountResponse(account).data
			context['message'] = "تم التعديل بنجاح."
			context['status'] = True
			return Response(context)
		else:
			return Response(serializers.errors)


# url: http://127.0.0.1:8000/account/api/deleteManager/<int:id>/
@api_view(['DELETE',])
def deleteAccountManager(request,id):
	if request.method == 'DELETE':
		context = {}
		try:
			token = Token.objects.get(user_id=id)
			account = Account.objects.get(pk=id)
		except Account.DoesNotExist:
			return Response(status=status.HTTP_404_NOT_FOUND)
		token.delete()
		account.delete()
		context['message'] = "تم الحذف بنجاح ."
		context['status'] = True
		return Response(context)

# endregion USERS

# region VALIDATION
def validate_email(email):
	account = None
	try:
		account = Account.objects.get(email=email)
	except Account.DoesNotExist:
		return None
	if account != None:
		return email

def validate_username(username):
	account = None
	try:
		account = Account.objects.get(username=username)
	except Account.DoesNotExist:
		return None
	if account != None:
		return username

def validate_phone(phone):
	account = None
	try:
		account = Account.objects.get(phone=phone)
	except Account.DoesNotExist:
		return None
	if account != None:
		return phone

def validate_account_no(account_no):
	account = None
	try:
		account = Account.objects.get(account_no=account_no)
	except Account.DoesNotExist:
		return None
	if account != None:
		return account_no
# endregion VALIDATION