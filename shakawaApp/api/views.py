# ------------ API AND  APIVIEW AND VIEWSETS-----------#

from rest_framework.generics import UpdateAPIView
from django.contrib.auth import authenticate
# API UTILS
from rest_framework import status
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser 
from main.permissions import IsAdmin
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.filters import SearchFilter,OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

# VIEWSETS
from rest_framework import viewsets
# APIVIEW
from rest_framework.views import APIView
# ------------ SERIALIZERS -----------#
from shakawaApp.api.serializers import (
	ShakawaSer)
# ------------ MODELS -----------#
from shakawaApp.models import Shakawa



"link: http://127.0.0.1:8000/shakawa/api/router/"
class ShakawaMVS(viewsets.ModelViewSet):
	permission_classes =[AllowAny,]
	queryset = 			Shakawa.objects.all()
	serializer_class =  ShakawaSer
	filter_backends  =  [SearchFilter,OrderingFilter,DjangoFilterBackend]
	filterset_fields =  ["user","kind","date"]
	search_fields    =  ["^user_name"]
	ordering_fields  =  ['datetime']
	
	def update(self, request, *args, **kwargs):
		super(ShakawaMVS, self).update(request, *args, **kwargs)
		return Response({"message": "تم التعديل بنجاح","status":  True})
	def create(self, request, *args, **kwargs):
		super(ShakawaMVS, self).create(request, *args, **kwargs)
		return Response({"message": "تم الإضافه بنجاح","status":  True})
	def destroy(self, request, *args, **kwargs):
		super(ShakawaMVS, self).destroy(request, *args, **kwargs)
		return Response({"message": "تم الحذف بنجاح","status":  True})


"link: http://127.0.0.1:8000/shakawa/api/getShakawa/"
@api_view(['GET',])
@permission_classes([IsAdmin,])
def getShakawa(request):
	if request.method == 'GET':
		data = Shakawa.objects.all()
		serializers = ShakawaSer(data,many=True)
		return Response({"results":serializers.data})
	else:
		return Response(status=status.HTTP_404_NOT_FOUND)
