# region MODULE
# ------------ API -----------#
# UTILS
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import  permissions
# VIEWSETS
from rest_framework import viewsets
# APIVIEW
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter,OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
# ------------ MODELS -----------#
# MODELS
from transactions.models import Rest,Record,Talabat
from customers.models import CustomerInfo, MandopInfo 
# UTILS
from django.db.models import Q,F,Prefetch
# ------------ SERIALIZERS -----------#
from transactions.api.serializers import SRecord,SRest ,SRecordSets,STalabat
from account.api.pagination import LargeResultsSetPagination

# --------------- PYTHON UTILS ------------------#
import datetime
from django.db.models import Sum
# endregion MODULE


class TalabatMVS(viewsets.ModelViewSet):
    pagination_class = LargeResultsSetPagination
    queryset = Talabat.objects.all()
    serializer_class = STalabat
    filter_backends = [SearchFilter,OrderingFilter,DjangoFilterBackend]
    filterset_fields = ['type','periority','stateTrans','date']
    search_fields = ["user__username"]
    ordering_fields = ['date', 'dateTime']
    def update(self, request, *args, **kwargs):
        super(TalabatMVS, self).update(request, *args, **kwargs)
        return Response({"message": "تم تعديل الطلب بنجاح","status":  True})
    def create(self, request, *args, **kwargs):
        super(TalabatMVS, self).create(request, *args, **kwargs)
        return Response({"message": "تم إضافه الطلب بنجاح","status":  True})
    def destroy(self, request, *args, **kwargs):
        super(TalabatMVS, self).destroy(request, *args, **kwargs)
        return Response({"message": "تم حذف الطلب بنجاح","status":  True})
