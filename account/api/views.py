# ------------ API AND  APIVIEW AND VIEWSETS-----------#
from rest_framework import status
from rest_framework.generics import UpdateAPIView
from django.contrib.auth import authenticate
# API UTILS
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
# VIEWSETS
from rest_framework import viewsets
# APIVIEW
from rest_framework.views import APIView
from account.api.pagination import LargeResultsSetPagination
from rest_framework.decorators import api_view, permission_classes
# ------------ SERIALIZERS -----------#
from account.api.serializers import AccountS,SAccountShow,SAccountResponse,SAccountantState,SAccountAll,SAccountManager
from account.models import Account
from rest_framework.authtoken.models import Token


class UsersMVS(viewsets.ModelViewSet):
	queryset = Account.objects.get_queryset().order_by('id')
	pagination_class = LargeResultsSetPagination
	serializer_class = SAccountAll
	# def destroy(self, request, *args, **kwargs):
	# 	super(SAccountManager, self).destroy(request, *args, **kwargs)
	# 	return Response({"message": "تم حذف المستخدم بنجاح","status":  True})
	# def create(self, request, *args, **kwargs):
	# 	super(SAccountManager, self).create(request, *args, **kwargs)
	# 	return Response({"message": "تم إضافة المستخدم بنجاح","status":  True})
	# def update(self, request, *args, **kwargs):
	# 	super(SAccountManager, self).update(request, *args, **kwargs)
	# 	return Response({"message": "تم تعديل المستخدم بنجاح","status":  True})

@api_view(['POST',])
def register_account(request):
	if request.method == 'POST':
		context = {}
		email = request.data.get('email', '0').lower()
		if validate_email(email) != None:
			context['response'] = 'هذا الإيميل مستخدم من قبل.'
			context['status'] = False
			return Response(context)

		username = request.data.get('username', '0')
		if validate_username(username) != None:
			context['response'] = 'هذا الإسم مستخدم من قبل.'
			context['status'] = False
			return Response(context)

		account_no = request.data.get('account_no', '0')
		if validate_account_no(account_no) != None:
			context['response'] = 'هذا الرقم مستخدم من قبل.'
			context['status'] = False
			return Response(context)

		phone = request.data.get('phone', '0')
		if validate_phone(phone) != None:
			context['response'] = 'رقم المحمول هذا مستخدم من قبل.'
			context['status'] = False
			return Response(context)

		serializers = AccountS(data=request.data)
		if serializers.is_valid():
			account = serializers.save()
			context = SAccountResponse(account).data
			context['response'] = "تم التسجيل بنجاح."
			context['status'] = True
			return Response(context)
		else:
			return Response(serializers.errors)

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


@api_view(['GET',])
def getAccountManager(request):
	if request.method == 'GET':
		account = Account.objects.get_queryset().order_by('id')
		serializers = SAccountAll(account,many=True)
		return Response({"results":serializers.data})

@api_view(['DELETE',])
def deleteAccountManager(request,id):
	if request.method == 'DELETE':
		context = {}
		try:
			account = Account.objects.get(pk=id)
		except Account.DoesNotExist:
			return Response(status=status.HTTP_404_NOT_FOUND)
		account.delete()
		context['message'] = "تم الحذف بنجاح ."
		context['status'] = True
		return Response(context)


@api_view(['PUT',])
def updateAccountManager(request,id):
	if request.method == 'PUT':
		context = {}
		try:
			account = Account.objects.get(pk=id)
		except Account.DoesNotExist:
			return Response(status=status.HTTP_404_NOT_FOUND)
		serializers = SAccountManager(account,data=request.data)
		if serializers.is_valid():
			account = serializers.save()
			context = SAccountResponse(account).data
			context['message'] = "تم التعديل بنجاح."
			context['status'] = True
			return Response(context)
		else:
			return Response(serializers.errors)


@api_view(['GET', ])
def getUserState(request,id):
	try:
		account = Account.objects.get(pk=id)
		return Response(SAccountantState(account).data)
	except Account.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)
	
# Account properties
# Response: https://gist.github.com/mitchtabian/4adaaaabc767df73c5001a44b4828ca5
# Url: https://<your-domain>/api/account/
# Headers: Authorization: Token <token>
@api_view(['GET', ])
@permission_classes((IsAuthenticated, ))
def account_properties_view(request):

	try:
		account = request.user
	except Account.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = SAccountShow(account)
		return Response(serializer.data)


# Account update properties
# Response: https://gist.github.com/mitchtabian/72bb4c4811199b1d303eb2d71ec932b2
# Url: https://<your-domain>/api/account/properties/update
# Headers: Authorization: Token <token>
@api_view(['PUT',])
@permission_classes((IsAuthenticated, ))
def update_account_view(request):
	try:
		account = request.user
	except Account.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)
		
	if request.method == 'PUT':
		serializer = SAccountShow(account, data=request.data)
		data = {}
		if serializer.is_valid():
			serializer.save()
			data['response'] = 'تم تحديث الحساب.'
			return Response(data=data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# LOGIN
# Response: https://gist.github.com/mitchtabian/8e1bde81b3be342853ddfcc45ec0df8a
# URL: http://127.0.0.1:8000/api/account/login
class ObtainAuthTokenView(APIView):

	authentication_classes = []
	permission_classes = []

	def post(self, request):
		context = {}
		phone = request.POST.get('phone')
		password = request.POST.get('password')
		account = authenticate(phone=phone, password=password)
		if account:
			context = SAccountResponse(account).data
			context['response'] = "تم الدخول بنجاح."
			return Response(context)
		else:
			context['response'] = 'خطأ'
			context['error_message'] = 'يوجد مشكلة حدثت'
			return Response(context)

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
