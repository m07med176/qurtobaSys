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
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import api_view, permission_classes
# ------------ SERIALIZERS -----------#
from account.api.serializers import AccountS,SAccountShow
from account.models import Account
from rest_framework.authtoken.models import Token
@api_view(['POST',])
def register_account(request):
    if request.method == 'POST':
        serializers = AccountS(data=request.data)
        data = {}
        if serializers.is_valid():
            print("*"*150)
            account = serializers.save()
            data['response'] = 'successfully registered new user.'
            data['email'] = account.email
            data['username'] = account.username
            data['phone'] = account.phone
            data['account_no'] = account.account_no
            data['pk'] = account.pk
            token = Token.objects.get(user=account).key
            data['token'] = token
        else:
            data = serializers.errors
        return Response(data)


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
			data['response'] = 'Account update success'
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
			try:
				token = Token.objects.get(user=account)
			except Token.DoesNotExist:
				token = Token.objects.create(user=account)
			context['response'] = 'تم الدخول بنجاج.'
			context['pk'] = account.pk
			context['phone'] = account.phone
			context['account_no'] = account.account_no
			context['username'] = account.username
			context['email'] = account.email.lower()
			context['token'] = token.key
		else:
			context['response'] = 'خطأ'
			context['error_message'] = 'يوجد مشكلة حدثت'

		return Response(context)
