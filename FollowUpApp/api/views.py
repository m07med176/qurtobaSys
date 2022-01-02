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
from FollowUpApp.models import FollowUp,Employers
from FollowUpApp.api.serializers import SFollowUpAll,SEmployersAll

class EmployersMVS(viewsets.ModelViewSet):
	permission_classes =  [AllowAny, ]
	pagination_class   =  LargeResultsSetPagination
	queryset 		   =  Employers.objects.all()
	serializer_class   =  SEmployersAll
	filter_backends    =  [SearchFilter,OrderingFilter,DjangoFilterBackend]
	filterset_fields   =  ["uid","email","name","phone","date_joined","last_login","is_superuser","is_admin","is_staff","is_active","type"]
	search_fields      =  ["uid","email","name"]
	ordering_fields    =  ['email', 'name','uid','phone','date_joined','last_login','is_active','type']

	def update(self, request, *args, **kwargs):
		super(EmployersMVS, self).update(request, *args, **kwargs)
		return Response({"message": "تم التعديل بنجاح","status":  True})
	def create(self, request, *args, **kwargs):
		try:
			Employers.objects.get(uid=request.data.get('uid', ''))
			return Response({"message": "تم الدخول بنجاح","status":  True})
		except Employers.DoesNotExist:
			super(EmployersMVS, self).create(request, *args, **kwargs)
			return Response({"message": "تم التسجيل بنجاح","status":  True})
	def destroy(self, request, *args, **kwargs):
		super(EmployersMVS, self).destroy(request, *args, **kwargs)
		return Response({"message": "تم الحذف بنجاح","status":  True})

class FollowUpMVS(viewsets.ModelViewSet):
	permission_classes  = [AllowAny, ]
	pagination_class  	= LargeResultsSetPagination
	queryset = FollowUp.objects.all()
	serializer_class 	= SFollowUpAll
	filter_backends 	= [SearchFilter,OrderingFilter,DjangoFilterBackend]
	filterset_fields 	= ["user__name","user__email","user__uid","day","startTime","endTime","duration","dateTime","transport"]
	search_fields 		= ["user__name","notes"]
	ordering_fields 	= ['dateTime','duration','user__email', 'user__name','user__uid',"transport"]

	def update(self, request, *args, **kwargs):
		super(FollowUpMVS, self).update(request, *args, **kwargs)
		return Response({"message": "تم التعديل بنجاح","status":  True})
	def create(self, request, *args, **kwargs):
		super(FollowUpMVS, self).create(request, *args, **kwargs)
		return Response({"message": "تم الإضافة بنجاح","status":  True})
	def destroy(self, request, *args, **kwargs):
		super(FollowUpMVS, self).destroy(request, *args, **kwargs)
		return Response({"message": "تم الحذف بنجاح","status":  True})

@api_view(['POST',])
@permission_classes((AllowAny, ))
def startDay(request):
	if request.method == 'POST':
		# static varialble
		day       = request.data.get('day', '')
		uid       = request.data.get('uid', '')
		# change varialble
		startTime = request.data.get('startTime', '')
		# validation
		if uid == '': return Response({"message": "حدثت مشكلة uid فارغ","status":  False})
		if day == '': return Response({"message": "حدثت مشكلة التاريخ فارغ","status":  False})
		if startTime == '': return Response({"message": "حدثت مشكلة بداية الوقت فارغ","status":  False})
		# create or update row
		values = {"startTime":startTime,"is_active":True }
		try:
			employer = Employers.objects.get(uid=uid)
			employer.is_active  = True
			employer.save()
			FollowUp.objects.update_or_create(
				user=employer,
				day = day,
				defaults=values )
			return Response({"message": "توكل عل الله","status":  True})
		except Exception as e:
			return Response({"message": f"حدثت مشكلة {e}","status":  False})

@api_view(['POST',])
@permission_classes((AllowAny, ))
def endDay(request):
	if request.method == 'POST':
		# static varialble
		uid       = request.data.get('uid', '')
		day       = request.data.get('day', '')
		# change varialble
		endTime = request.data.get('endTime', '')
		duration 	  = request.data.get('duration', '')
		# validation
		if uid == '': return Response({"message": "حدثت مشكلة uid فارغ","status":  False})
		if day == '': return Response({"message": "حدثت مشكلة التاريخ فارغ","status":  False})
		if endTime == '': return Response({"message": "حدثت مشكلة نهاية الوقت فارغ","status":  False})
		if duration == '': return Response({"message": "حدثت مشكلة الفتره فارغة","status":  False})
		# create or update row
		values = {"endTime":endTime,"duration":duration,"is_active":False }
		try:
			employer = Employers.objects.get(uid=uid)
			employer.is_active  = False
			employer.save()
			FollowUp.objects.update_or_create(
					user=employer,
					day = day,
					defaults=values )
			return Response({"message": "الحمد لله رب العالمين","status":  True})
		
		except Exception as e: return Response({"message": f"حدثت مشكلة {e}","status":  False})

@api_view(['POST',])
@permission_classes((AllowAny, ))
def addNotes(request):
	if request.method == 'POST':
		# static varialble
		uid       = request.data.get('uid', '')
		day       = request.data.get('day', '')
		# change varialble
		notes1     = request.data.get('notes', '')
		# validation
		if uid == '': 		return Response({"message": "حدثت مشكلة uid فارغ","status":  False})
		if day == '': 		return Response({"message": "حدثت مشكلة التاريخ فارغ","status":  False})
		if notes1 == '': 	return Response({"message": "حدثت مشكلة الملاحظة فارغة","status":  False})
		
		try:
			# if you have a row
			employer = Employers.objects.get(uid=uid)
			notes2 = FollowUp.objects.filter(user=employer,day=day).first().notes
			values = {"notes":notes1+"\n"+notes2 }
			try:
				FollowUp.objects.update_or_create(user=employer, day = day, defaults=values )
				return Response({"message": "تم حفظ الملاحظة","status":  True})
			except Exception as e:
				return Response({"message": f"حدثت مشكلة {e}","status":  False})
		except Exception as e:
			# if you don't have a row
			values = {"notes":notes1 }
			try:
				FollowUp.objects.update_or_create( 
					user=employer, day = day, defaults=values )
				return Response({"message": "تم حفظ الملاحظة","status":  True})
			except Exception as e:
				return Response({"message": f"حدثت مشكلة {e}","status":  False})

@api_view(['POST',])
@permission_classes((AllowAny, ))
def addTransport(request):
	if request.method == 'POST':
		# static varialble
		uid       = request.data.get('uid', '')
		day       = request.data.get('day', '')
		# change varialble
		transport = int(request.data.get('transport', 0))
		# validation
		if uid == '': 		return Response({"message": "حدثت مشكلة uid فارغ","status":  False})
		if day == '': 		return Response({"message": "حدثت مشكلة التاريخ فارغ","status":  False})
		if transport == 0: 	return Response({"message": "حدثت مشكلة القيمة فارغة","status":  False})
		
		try:
			# if you have a row
			employer = Employers.objects.get(uid=uid)
			transport_ = FollowUp.objects.filter(user__uid=uid,day=day).first().transport
			values = {"transport":transport+transport_ }
			try:
				FollowUp.objects.update_or_create( user=employer, day = day, defaults=values )
				return Response({"message": "تم حفظ القيمة","status":  True})
			except Exception as e:
				return Response({"message": f"حدثت مشكلة {e}","status":  False})
		except Exception as e:
			# if you don't have a row
			values = {"transport":transport}
			try:
				FollowUp.objects.update_or_create( 
				user=employer, day = day, defaults=values )
				return Response({"message": "تم حفظ القيمة","status":  True})
			except Exception as e: return Response({"message": f"حدثت مشكلة {e}","status":  False})