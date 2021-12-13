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

# region MainRest
class RestL(viewsets.ModelViewSet):
    pagination_class = None
    queryset = Rest.objects.all().order_by('date','time')
    serializer_class = SRest
    filter_backends = [SearchFilter,OrderingFilter,DjangoFilterBackend]
    filterset_fields = ['date']
    search_fields = ["customer__seller__name"]
    ordering_fields = ['date', 'time']

# GET REST OF SEPCIFIC SELLER
class GetRest(APIView):
    permission_classes = (permissions.AllowAny,)
    def customSerializers(self,name):
        if name.isdigit():
            customer = CustomerInfo.objects.filter(Q(deviceNo=name)) 
        else:
            customer = CustomerInfo.objects.filter(Q(name=name))
        if len(customer) == 0:return "0"
        rest=Rest.objects.filter(customer__id=customer[0].id)
        if len(rest) != 0: return str(rest[0].value)
        else: return "0"

    def get(self,request,name):
        return Response({"data":self.customSerializers(name)})

def getRestByCustomSerializer(objectData):
    allData = []
    areaName = ''
    for data in objectData:
        if areaName != data.customer.area:
            if data.value != 0:
                row = {}
                row['deviceNo'] = 0
                row['customerName'] = data.customer.area
                row['phoneNo'] = '1111111111111112111111111'
                row['seller'] = ''
                row['rest'] = 0
                areaName = data.customer.area
                allData.append(row)
                row = {}
                row['deviceNo'] =data.customer.deviceNo
                row['customerName'] = data.customer.name
                row['phoneNo'] = data.customer.phoneNo
                row['rest'] = data.value
                row['seller'] = data.customer.seller.name
                allData.append(row)
        else: 
            if data.value != 0:
                row = {}
                row['deviceNo'] =data.customer.deviceNo
                row['customerName'] = data.customer.name
                row['phoneNo'] = data.customer.phoneNo
                row['rest'] = data.value
                row['seller'] = data.customer.seller.name
                allData.append(row)
            
    return allData

@api_view(['GET',])
def getSellerRestId(request,id):
    rest=Rest.objects.filter(customer__seller=id).select_related('customer').order_by('customer__area','date')
    if len(rest) == 0:return Response({"data": []})
    return Response({"data": getRestByCustomSerializer(rest)})

# region Collector , Assistance , Seller
@api_view(['GET',])
def getAssistanceRest(request,email):
    assistant = MandopInfo.objects.filter(Q(email=email))
    latestDate = Record.objects.filter(customerData__assistant=assistant[0].id)
    
    if len(assistant) == 0 or len(latestDate) == 0: return Response({"data": [],"date":""})
    latestDate = latestDate.latest('date')

    rest=Rest.objects.filter(customer__assistant=assistant[0].id).select_related('customer').order_by('customer__area','date')
    if len(rest) == 0:return Response({"data": [],"date":""})
    return Response({"data": getRestByCustomSerializer(rest),"date":f"أخر تحويل: {latestDate.date} {latestDate.time}"})
    
@api_view(['GET',])
def getSellerRest(request,email):
    seller = MandopInfo.objects.filter(Q(email=email))
    latestDate = Record.objects.filter(customerData__seller=seller[0].id)
    
    if len(seller) == 0 or len(latestDate) == 0: return Response({"data": [],"date":""})
    latestDate = latestDate.latest('date')

    rest=Rest.objects.filter(customer__seller=seller[0].id).select_related('customer').order_by('customer__area','date')
    if len(rest) == 0:return Response({"data": [],"date":""})
    return Response({"data": getRestByCustomSerializer(rest),"date":f"أخر تحويل: {latestDate.date} {latestDate.time}"})
    # region All Customers Main Rest
@api_view(['GET',])
def getAllRest(request):
    rest=Rest.objects.all().select_related('customer').order_by('customer__area','date')
    if len(rest) == 0:return Response({"data": []})
    return Response({"data": getRestByCustomSerializer(rest)})

@api_view(['GET',])
def getAllRestGte(request,value):
    rest=Rest.objects.filter(value__gte=value).select_related('customer').order_by('customer__area','date')
    if len(rest) == 0:return Response({"data": []})
    return Response({"data": getRestByCustomSerializer(rest)})
    # endregion
# endregion
# endregion MainRest
