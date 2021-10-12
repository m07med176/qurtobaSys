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
from transactions.api.serializers import SRecord,SRest ,SMainRest,SRecordSets
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
    rest=Rest.objects.filter(customer__seller=id).select_related('customer').order_by('customer__area')
    if len(rest) == 0:return Response({"data": []})
    return Response({"data": getRestByCustomSerializer(rest)})

@api_view(['GET',])
def getSellerRest(request,email):
    seller = MandopInfo.objects.filter(Q(email=email))
    latestDate = Record.objects.filter(customerData__seller=seller[0].id)
    
    if len(seller) == 0 or len(latestDate) == 0: return Response({"data": [],"date":""})
    latestDate = latestDate.latest('date')

    rest=Rest.objects.filter(customer__seller=seller[0].id).select_related('customer').order_by('customer__area')
    if len(rest) == 0:return Response({"data": [],"date":""})
    return Response({"data": getRestByCustomSerializer(rest),"date":f"أخر تحويل: {latestDate.date} {latestDate.time}"})



@api_view(['GET',])
def getAllRest(request):
    rest=Rest.objects.all().select_related('customer').order_by('customer__area','date')
    if len(rest) == 0:return Response({"data": []})
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
        if len(rest) != 0: return str(rest[0].rest)
        else: return "0"

    def get(self,request,name):
        return Response({"data":self.customSerializers(name)})

# region Transactions
class RecordL(viewsets.ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = SRecordSets
    def create(self, request, *args, **kwargs):
        super(RecordL, self).create(request, *args, **kwargs)
        return Response({"message": "تم إضافة التحويل بنجاح","status":  True})
#   region ACCOUNT TRANSACTION FILTER
#       region DATE FILTER
@api_view(['GET',])
def getTransactionsDateFromTo(request,dateFrom,dateTo,type= 'الكل',seller= 0):
    # request.dateFrom # dateTo deviceNo
    start = datetime.datetime.fromisoformat(dateFrom) 
    end = datetime.datetime.fromisoformat(dateTo)   
    if seller == 0 and type == 'الكل':
        record=Record.objects.filter(date__range = (start,end)).order_by(F('date').desc(nulls_last=True),F('time').desc(nulls_last=True))
    elif seller != 0 and type != 'الكل':
        record=Record.objects.filter(customerData__seller=seller,type=type,date__range = (start,end)).order_by(F('date').desc(nulls_last=True),F('time').desc(nulls_last=True))
    elif seller == 0 and type != 'الكل':
        record=Record.objects.filter(type=type,date__range = (start,end)).order_by(F('date').desc(nulls_last=True),F('time').desc(nulls_last=True))
    elif seller != 0 and type == 'الكل':
        record=Record.objects.filter(customerData__seller=seller,date__range = (start,end)).order_by(F('date').desc(nulls_last=True),F('time').desc(nulls_last=True))
    
    serializer = SRecord(record,many=True)
    return Response({"data":serializer.data})

@api_view(['GET',])
def getTransactionsDate(request,dateSelect,type= 'الكل',seller= 0):
    
    if seller == 0 and type == 'الكل':
        record = Record.objects.filter(date=datetime.datetime.fromisoformat(dateSelect)).order_by(F('time').desc(nulls_last=True))
    elif seller != 0 and type != 'الكل':
        record = Record.objects.filter(customerData__seller=seller,type=type,date=datetime.datetime.fromisoformat(dateSelect)).order_by(F('time').desc(nulls_last=True))
    elif seller == 0 and type != 'الكل':
        record = Record.objects.filter(type=type,date=datetime.datetime.fromisoformat(dateSelect)).order_by(F('time').desc(nulls_last=True))
    elif seller != 0 and type == 'الكل':
        record = Record.objects.filter(customerData__seller=seller,date=datetime.datetime.fromisoformat(dateSelect)).order_by(F('time').desc(nulls_last=True))
    serializer = SRecord(record,many=True)
    return Response({"data":serializer.data})
#       endregion
#       region DEVICE NUMBER FILTER
@api_view(['GET',])
def getTransactionsCustomerAndDateFromTo(request,deviceNo,dateFrom,dateTo,type= 'الكل'):
    start = datetime.datetime.fromisoformat(dateFrom) 
    end = datetime.datetime.fromisoformat(dateTo)   

    if type== 'الكل':
        if deviceNo.isdigit():
            record=Record.objects.filter(date__range = (start,end),customerData__deviceNo=deviceNo).order_by(F('date').desc(nulls_last=True),F('time').desc(nulls_last=True))
        else:
            record=Record.objects.filter(date__range = (start,end),customerData__name=deviceNo).order_by(F('date').desc(nulls_last=True),F('time').desc(nulls_last=True))
    else:
        if deviceNo.isdigit():
            record=Record.objects.filter(type=type,date__range = (start,end),customerData__deviceNo=deviceNo).order_by(F('date').desc(nulls_last=True),F('time').desc(nulls_last=True))
        else:
            record=Record.objects.filter(type=type,date__range = (start,end),customerData__name=deviceNo).order_by(F('date').desc(nulls_last=True),F('time').desc(nulls_last=True))
    
    serializer = SRecord(record,many=True)
    return Response({"data":serializer.data})

@api_view(['GET',])
def getTransactionsCustomerAndDate(request,deviceNo,dateSelect,type= 'الكل'):
    if type== 'الكل':
        if deviceNo.isdigit():
            record=Record.objects.filter(date=datetime.datetime.fromisoformat(dateSelect),customerData__deviceNo=deviceNo).order_by(F('time').desc(nulls_last=True))
        else:
            record=Record.objects.filter(date=datetime.datetime.fromisoformat(dateSelect),customerData__name=deviceNo).order_by(F('time').desc(nulls_last=True))
    else:
        if deviceNo.isdigit():
            record=Record.objects.filter(type=type,date=datetime.datetime.fromisoformat(dateSelect),customerData__deviceNo=deviceNo).order_by(F('time').desc(nulls_last=True))
        else:
            record=Record.objects.filter(type=type,date=datetime.datetime.fromisoformat(dateSelect),customerData__name=deviceNo).order_by(F('time').desc(nulls_last=True))
    
    serializer = SRecord(record,many=True)
    return Response({"data":serializer.data})

@api_view(['GET',])
def getTransactionsCustomer(request,deviceNo,type= 'الكل'):
    if type== 'الكل':
        if deviceNo.isdigit():
            record=Record.objects.filter(customerData__deviceNo=deviceNo).select_related('customerData').order_by(F('date').desc(nulls_last=True),F('time').desc(nulls_last=True))
        else:
            record=Record.objects.filter(customerData__name=deviceNo).select_related('customerData').order_by(F('date').desc(nulls_last=True),F('time').desc(nulls_last=True))
    else:
        if deviceNo.isdigit():
            record=Record.objects.filter(type=type,customerData__deviceNo=deviceNo).select_related('customerData').order_by(F('date').desc(nulls_last=True),F('time').desc(nulls_last=True))
        else:
            record=Record.objects.filter(type=type,customerData__name=deviceNo).select_related('customerData').order_by(F('date').desc(nulls_last=True),F('time').desc(nulls_last=True))
    
    serializer = SRecord(record,many=True)
    return Response({"data":serializer.data})
#       endregion
#   endregion
#   region TRANSACTION UTILS
@api_view(['GET',])
def getTransactionsCustomerById(request,id):

    record=Record.objects.filter(customerData_id=id).select_related('customerData').order_by(F('date').desc(nulls_last=True),F('time').desc(nulls_last=True))
    serializer = SRecord(record,many=True)
    return Response({"data":serializer.data,"sum":db.getCustomerRest(id)})

@api_view(['GET',])
def getTransactionsToday(request):
    record=Record.objects.filter(date=datetime.datetime.now()).order_by(F('time').desc(nulls_last=True))
    serializer = SRecord(record,many=True)
    return Response({"data":serializer.data})

@api_view(['GET',])
def getLastDateAndTime(request):
    rest=Record.objects.all().order_by('date','time').first()
    return Response({"data":f"التحويلات : {rest.date} {rest.time}"})
#   endregion
# endregion

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

