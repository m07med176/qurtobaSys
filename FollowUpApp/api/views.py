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
from FollowUpApp.api.pagination import CustomPagination
# VIEWSETS
from rest_framework import viewsets
# APIVIEW
from rest_framework.views import APIView
from FollowUpApp.models import FollowUp
from FollowUpApp.api.serializers import SFollowUpAll,SEmployersAll
from datetime import datetime
from account.api.views import UsersMVS
from account.models import Account

class UsersMVS(viewsets.ModelViewSet):
    pagination_class = LargeResultsSetPagination
    queryset = Account.objects.all().order_by('id')
    serializer_class = SEmployersAll
    filter_backends = [SearchFilter,OrderingFilter,DjangoFilterBackend]
    filterset_fields = ["is_superuser","is_admin","is_staff","is_active","is_open","type"]
    search_fields = ["email","username","phone","account_no"]
    ordering_fields = ['type','username','date_joined', 'last_login']
    def update(self, request, *args, **kwargs):
        super(UsersMVS, self).update(request, *args, **kwargs)
        return Response({"message": "تم تعديل المستخدم بنجاح","status":  True})
    def create(self, request, *args, **kwargs):
        super(UsersMVS, self).create(request, *args, **kwargs)
        return Response({"message": "تم إضافه المستخدم بنجاح","status":  True})
    def destroy(self, request, *args, **kwargs):
        super(UsersMVS, self).destroy(request, *args, **kwargs)
        return Response({"message": "تم حذف المستخدم بنجاح","status":  True})


class FollowUpMVS(viewsets.ModelViewSet):
	permission_classes  = [IsAuthenticated, ]
	pagination_class  	= CustomPagination
	queryset 			= FollowUp.objects.filter(dateTime__month=int(datetime.now().date().month),dateTime__year=int(datetime.now().date().year))
	serializer_class 	= SFollowUpAll
	filter_backends 	= [SearchFilter,OrderingFilter,DjangoFilterBackend]
	filterset_fields 	= ["dateTime","user__name","user__id","user__email","day","startTime","endTime","duration","dateTime","transport"]
	search_fields 		= ["user__name","notes"]
	ordering_fields 	= ['dateTime','duration','user__email',"user__id", 'user__name',"transport"]

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
@permission_classes((IsAuthenticated, ))
def startDay(request):
	if request.method == 'POST':
		# static varialble
		day       = request.data.get('day', '')
		# change varialble
		startTime = request.data.get('startTime', '')
		# validation
		if day == '': return Response({"message": "حدثت مشكلة التاريخ فارغ","status":  False})
		if startTime == '': return Response({"message": "حدثت مشكلة بداية الوقت فارغ","status":  False})
		# create or update row
		values = {"startTime":startTime,"is_active":True }
		try:
			employer = request.user
			employer.is_open  = True
			employer.save()
			FollowUp.objects.update_or_create(
				user=employer,
				day = day,
				defaults=values )
			return Response({"message": "توكل عل الله","status":  True})
		except Exception as e:
			return Response({"message": f"حدثت مشكلة {e}","status":  False})

@api_view(['POST',])
@permission_classes((IsAuthenticated, ))
def endDay(request):
	if request.method == 'POST':
		# static varialble
		day       = request.data.get('day', '')
		# change varialble
		endTime = request.data.get('endTime', '')
		duration 	  = request.data.get('duration', '')
		# validation
		if day == '': return Response({"message": "حدثت مشكلة التاريخ فارغ","status":  False})
		if endTime == '': return Response({"message": "حدثت مشكلة نهاية الوقت فارغ","status":  False})
		if duration == '': return Response({"message": "حدثت مشكلة الفتره فارغة","status":  False})
		# create or update row
		values = {"endTime":endTime,"duration":duration,"is_active":False }
		try:
			employer = request.user
			employer.is_open  = False
			employer.save()
			FollowUp.objects.update_or_create(
					user=employer,
					day = day,
					defaults=values )
			return Response({"message": "الحمد لله رب العالمين","status":  True})
		
		except Exception as e: return Response({"message": f"حدثت مشكلة {e}","status":  False})

@api_view(['POST',])
@permission_classes((IsAuthenticated, ))
def addNotes(request):
	if request.method == 'POST':
		# static varialble
		day       = request.data.get('day', '')
		# change varialble
		notes1     = request.data.get('notes', '')
		# validation
		if day    == '': 	return Response({"message": "حدثت مشكلة التاريخ فارغ","status":  False})
		if notes1 == '': 	return Response({"message": "حدثت مشكلة الملاحظة فارغة","status":  False})
		
		try:
			# if you have a row
			employer = request.user
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
@permission_classes((IsAuthenticated, ))
def addTransport(request):
	if request.method == 'POST':
		# static varialble
		day       = request.data.get('day', '')
		# change varialble
		transport = int(request.data.get('transport', 0))
		# validation
		if day == '': 		return Response({"message": "حدثت مشكلة التاريخ فارغ","status":  False})
		if transport == 0: 	return Response({"message": "حدثت مشكلة القيمة فارغة","status":  False})
		
		try:
			# if you have a row
			employer = request.user
			transport_ = FollowUp.objects.filter(user=employer,day=day).first().transport
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