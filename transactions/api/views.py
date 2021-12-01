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
# --------------- DATABASE MANAGER ------------------#
import datetime
from databaseManager import DatabaseManager
db = DatabaseManager()
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

@api_view(['GET',])
def getSellerRest(request,email):
    seller = MandopInfo.objects.filter(Q(email=email))
    latestDate = Record.objects.filter(customerData__seller=seller[0].id)
    
    if len(seller) == 0 or len(latestDate) == 0: return Response({"data": [],"date":""})
    latestDate = latestDate.latest('date')

    rest=Rest.objects.filter(customer__seller=seller[0].id).select_related('customer').order_by('customer__area','date')
    if len(rest) == 0:return Response({"data": [],"date":""})
    return Response({"data": getRestByCustomSerializer(rest),"date":f"أخر تحويل: {latestDate.date} {latestDate.time}"})

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

# endregion MainRest

# region Transactions
class RecordL(viewsets.ModelViewSet):
    queryset = Record.objects.all().order_by('date','time')
    serializer_class = SRecordSets
    def create(self, request, *args, **kwargs):
        #super(RecordL, self).create(request, *args, **kwargs)
        return self.createRecord(request)

    def createRecord(self,request):
        ser = SRecordSets(data=request.data)

        if ser.is_valid():
            try:
                Record.objects.get(date=ser.validated_data.get('date'),time=ser.validated_data.get('time'))
            except Record.DoesNotExist:
                ser.save()
                customer_id = ser.validated_data.get('customerData').id

                value1 = Record.objects.filter(customerData_id=customer_id,isDown=False,isDone=False).aggregate(Sum('value'))['value__sum'] if Record.objects.filter(customerData_id=customer_id,isDown=False,isDone=False).aggregate(Sum('value'))['value__sum'] != None else 0
                value2 = Record.objects.filter(customerData_id=customer_id,isDown=True,isDone=False).aggregate(Sum('value'))['value__sum'] if Record.objects.filter(customerData_id=customer_id,isDown=True,isDone=False).aggregate(Sum('value'))['value__sum'] != None else 0
                sum  = value1 - value2
                
                date = str(datetime.datetime.now().date())
                time = str(datetime.datetime.now().time()).split(".")[0]

                Rest.objects.update_or_create(
                customer_id=customer_id, 
                defaults={ 'value' :sum, 'date'  :date, 'time'  :time } )

                return Response({"message": "تم إضافة التحويل بنجاح","status":  True})
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        return Response({"message": "فشل فى التحويل","status":  False})
#   region ACCOUNT TRANSACTION FILTER
#       region TRANSACTION USER
@api_view(['GET',])
def getTransactionsDateUser(request,type='الكل',dateSelect=''):
    id = request.user.id
    if type == 'الكل':
        record = Record.objects.filter(customerData__user_id=id,date=datetime.datetime.fromisoformat(dateSelect)).order_by(F('time').desc(nulls_last=True))
    elif type != 'الكل':
        record = Record.objects.filter(customerData__user_id=id,type=type,date=datetime.datetime.fromisoformat(dateSelect)).order_by(F('time').desc(nulls_last=True))
    serializer = SRecord(record,many=True)
    return Response({"data":serializer.data})

@api_view(['GET',])
def getTransactionsUserToday(request):
    id = request.user.id
    record = Record.objects.filter(customerData__user_id=id,date=datetime.datetime.now()).order_by(F('time').desc(nulls_last=True))[:30]
    rest = Rest.objects.get(customer__user_id=id).value
    name = CustomerInfo.objects.get(user_id=id).name
    serializer = SRecord(record,many=True)
    return Response({"data":serializer.data,"rest":rest,"name":name})
@api_view(['GET',])
def getTransactionsDateFromToUser(request,type= 'الكل',dateFrom='',dateTo=''):
    start = datetime.datetime.fromisoformat(dateFrom) 
    end = datetime.datetime.fromisoformat(dateTo) 
    id = request.user.id
    if type == 'الكل':
        record = Record.objects.filter(customerData__user_id=id,date__range = (start,end)).order_by(F('time').desc(nulls_last=True))
    elif type != 'الكل':
        record = Record.objects.filter(customerData__user_id=id,type=type,date__range = (start,end)).order_by(F('time').desc(nulls_last=True))
    serializer = SRecord(record,many=True)
    return Response({"data":serializer.data})
#       endregion TRANSACTION USER
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

def getRestValueForCustomer(customer_id):
    value1 = Record.objects.filter(customerData_id=customer_id,isDown=False,isDone=False).aggregate(Sum('value'))['value__sum'] if Record.objects.filter(customerData_id=customer_id,isDown=False,isDone=False).aggregate(Sum('value'))['value__sum'] != None else 0
    value2 = Record.objects.filter(customerData_id=customer_id,isDown=True,isDone=False).aggregate(Sum('value'))['value__sum'] if Record.objects.filter(customerData_id=customer_id,isDown=True,isDone=False).aggregate(Sum('value'))['value__sum'] != None else 0
    sum  = value1 - value2

    date = str(datetime.datetime.now().date())
    time = str(datetime.datetime.now().time()).split(".")[0]

    # Rest.objects.update_or_create(
    # customer_id=customer_id, 
    # defaults={ 'value' :sum, 'date'  :date, 'time'  :time } )

    if sum == 0:
        Record.objects.filter(customerData_id=customer_id).update(isDone=True)
    return sum
@api_view(['GET',])
def getTransactionsCustomerById(request,id):

    record=Record.objects.filter(customerData_id=id).select_related('customerData').order_by(F('date').desc(nulls_last=True),F('time').desc(nulls_last=True))[:30]
    serializer = SRecord(record,many=True)
    # db.getCustomerRest(id)
    return Response({"data":serializer.data,"sum": getRestValueForCustomer(id)   })

@api_view(['GET',])
# @permission_classes((IsAuthenticated, ))
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

# region ACCOUNTS
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
# endregion ACCOUNTS