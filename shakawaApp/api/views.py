# ------------ API AND  APIVIEW AND VIEWSETS-----------#

from rest_framework.generics import ListAPIView
from django.contrib.auth import authenticate
# API UTILS
from rest_framework import status
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser 
from main.permissions import IsAdmin
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.filters import SearchFilter,OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination

# VIEWSETS
from rest_framework import viewsets
# APIVIEW
from rest_framework.views import APIView
# ------------ SERIALIZERS -----------#
from shakawaApp.api.serializers import (ShakawaSer,ShakawaSerAll)
# ------------ MODELS -----------#
from shakawaApp.models import Shakawa



"link: http://127.0.0.1:8000/shakawa/api/router/"
class ShakawaMVS(viewsets.ModelViewSet):
	permission_classes =[IsAuthenticated,]
	pagination_class = PageNumberPagination
	queryset = 			Shakawa.objects.all()
	serializer_class =  ShakawaSerAll
	filter_backends  =  [SearchFilter,OrderingFilter,DjangoFilterBackend]
	filterset_fields =  ["user","kind","date","is_deleted"]
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


@api_view(['GET',])
@permission_classes([IsAuthenticated,])
def getShakawa(request):
	if request.method == 'GET':
		data = Shakawa.objects.all()
		serializers = ShakawaSer(data,many=True)
		return Response({"results":serializers.data})
	else:
		return Response(status=status.HTTP_404_NOT_FOUND)


# region PRODUCT
# url: http://127.0.0.1:8000/shakawa/api/getShakawa/
# methods: GET
class GetShakawa(ListAPIView):
	pagination_class = PageNumberPagination
	PageNumberPagination.page_size = 200
	queryset = Shakawa.objects.all()
	serializer_class = ShakawaSer
	permission_classes = [IsAuthenticated,]
	model = Shakawa
	filter_backends  =  [SearchFilter,OrderingFilter,DjangoFilterBackend]
	filterset_fields =  ["user","kind","date","is_deleted"]
	search_fields    =  ["=user__username"]
	ordering_fields  =  ['datetime']


