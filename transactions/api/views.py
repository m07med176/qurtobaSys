# ------------ API -----------#
# UTILS
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import  permissions
# VIEWSETS
from rest_framework import viewsets
# APIVIEW
from rest_framework.views import APIView
from rest_framework.decorators import api_view
# ------------ MODELS -----------#
# MODELS
from transactions.models import Rest,Record
from customers.models import CustomerInfo, MandopInfo 
# UTILS
from django.db.models import Q
from django.db.models import F
# from django.db.models import Prefetch
# ------------ SERIALIZERS -----------#
#from customers.api.serializers import SCustomer_info
from transactions.api.serializers import SRecord,SRest ,SMainRest
from customers.api.serializers import SCustomer_info,SMandop_Info 
# --------------- PYTHON UTILS ------------------#
import datetime
# --------------- DATABASE MANAGER ------------------#
from databaseManager import DatabaseManager
db = DatabaseManager()

# --------------- Office Rest ---------------------- #
class RestL(viewsets.ModelViewSet):
    queryset = Rest.objects.all()
    serializer_class = SRest

def getRestByCustomSerializer(objectData):
    allData = []
    areaName = ''
    for data in objectData:
        if areaName != data.customer.area:
            row = {}
            row['deviceNo'] = 0
            row['customerName'] = data.customer.area
            row['phoneNo'] = '1111111111111112111111111'
            row['rest'] = 0.0
            areaName = data.customer.area
            allData.append(row)
            row = {}
            row['deviceNo'] =data.customer.deviceNo
            row['customerName'] = data.customer.name
            row['phoneNo'] = data.customer.phoneNo
            row['rest'] = data.value
            allData.append(row)
        else: 
            row = {}
            row['deviceNo'] =data.customer.deviceNo
            row['customerName'] = data.customer.name
            row['phoneNo'] = data.customer.phoneNo
            row['rest'] = data.value
            allData.append(row)
            
    return allData

@api_view(['GET',])
def getSellerRest(request,email):
    seller = MandopInfo.objects.filter(Q(email=email))
    if len(seller) == 0: return Response({"results": ""})
    rest=Rest.objects.filter(customer__seller=seller[0].id).select_related('customer').order_by('customer__area')
    if len(rest) == 0:return Response({"results": ""})
    return Response({"data": getRestByCustomSerializer(rest)})

@api_view(['GET',])
def getAllRest(request):
    rest=Rest.objects.all().select_related('customer').order_by('customer__area')
    if len(rest) == 0:return Response({"results": ""})
    return Response({"data": getRestByCustomSerializer(rest)})

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
        if len(rest) != 0:
            return str(rest[0].rest)
        else:
            return "0"

    def get(self,request,name):
        return Response({"data":self.customSerializers(name)})

# --------------- Transactions ---------------------- #
class RecordL(viewsets.ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = SRecord

@api_view(['GET',])
def getTransactionsDateFromTo(request,dateFrom,dateTo):
    # request.dateFrom # dateTo deviceNo
    start = datetime.datetime.fromisoformat(dateFrom) 
    end = datetime.datetime.fromisoformat(dateTo)   

    record=Record.objects.filter(date__range = (start,end)).order_by(F('date').desc(nulls_last=True),F('time').desc(nulls_last=True))

    serializer = SRecord(record,many=True)
    return Response({"data":serializer.data})

@api_view(['GET',])
def getTransactionsCustomerAndDateFromTo(request,deviceNo,dateFrom,dateTo):
    start = datetime.datetime.fromisoformat(dateFrom) 
    end = datetime.datetime.fromisoformat(dateTo)   

    if deviceNo.isdigit():
        record=Record.objects.filter(date__range = (start,end),customerData__deviceNo=deviceNo).order_by(F('date').desc(nulls_last=True),F('time').desc(nulls_last=True))
    else:
        record=Record.objects.filter(date__range = (start,end),customerData__name=deviceNo).order_by(F('date').desc(nulls_last=True),F('time').desc(nulls_last=True))

    serializer = SRecord(record,many=True)
    return Response({"data":serializer.data})

@api_view(['GET',])
def getTransactionsDate(request,dateSelect):
    record = Record.objects.filter(date=datetime.datetime.fromisoformat(dateSelect)).order_by(F('time').desc(nulls_last=True))
    if len(record) == 0:return Response({"data": ""})
    serializer = SRecord(record,many=True)
    return Response({"data":serializer.data})

@api_view(['GET',])
def getTransactionsCustomerAndDate(request,deviceNo,dateSelect):
    if deviceNo.isdigit():
        record=Record.objects.filter(date=datetime.datetime.fromisoformat(dateSelect),customerData__deviceNo=deviceNo).order_by(F('time').desc(nulls_last=True))
    else:
        record=Record.objects.filter(date=datetime.datetime.fromisoformat(dateSelect),customerData__name=deviceNo).order_by(F('time').desc(nulls_last=True))
    if len(record) == 0:return Response({"data": ""})
    serializer = SRecord(record,many=True)
    return Response({"data":serializer.data})

@api_view(['GET',])
def getTransactionsCustomer(request,deviceNo):
    if deviceNo.isdigit():
        record=Record.objects.filter(customerData__deviceNo=deviceNo).select_related('customerData').order_by(F('date').desc(nulls_last=True),F('time').desc(nulls_last=True))
    else:
        record=Record.objects.filter(customerData__name=deviceNo).select_related('customerData').order_by(F('date').desc(nulls_last=True),F('time').desc(nulls_last=True))
    if len(record) == 0:return Response({"data": ""})
    serializer = SRecord(record,many=True)
    return Response({"data":serializer.data})

@api_view(['GET',])
def getTransactionsToday(request):
    record=Record.objects.filter(date=datetime.datetime.now()).order_by(F('time').desc(nulls_last=True))
    if len(record) == 0:return Response({"data": ""})
    serializer = SRecord(record,many=True)
    return Response({"data":serializer.data})

@api_view(['GET',])
def getLastDateAndTime(request):
    rest=Record.objects.all().order_by('date','time').first()
    return Response({"data":f"التحويلات : {rest.date} {rest.time}"})


# --------------- ACCOUNTS ---------------------- #
@api_view(['GET',])
def getAccountsDateFromTo(request,dateFrom,dateTo):
    return Response({"data":db.accounts(id=5,dateFrom=dateFrom,dateTo=dateTo)})

@api_view(['GET',])
def getAccountsCustomerAndDateFromTo(request,deviceNo,dateFrom,dateTo):
    return Response({"data":db.accounts(id=6,deviceNo=deviceNo,dateFrom=dateFrom,dateTo=dateTo)})

@api_view(['GET',])
def getAccountsDate(request,dateSelect):
    return Response({"data":db.accounts(id=3,dateFrom=dateSelect)})

@api_view(['GET',])
def getAccountsCustomerAndDate(request,deviceNo,dateSelect):
    return Response({"data":db.accounts(id=4,deviceNo=deviceNo,dateFrom=dateSelect)})

@api_view(['GET',])
def getAccountsCustomer(request,deviceNo):
    return Response({"data":db.accounts(id=2,deviceNo=deviceNo)})

@api_view(['GET',])
def getAccountsToday(request):
    return Response({"data":db.accounts(id=1)})

