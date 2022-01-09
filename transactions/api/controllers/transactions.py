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
from django.db.models import Q,F,Prefetch,Sum
# ------------ SERIALIZERS -----------#
from transactions.api.serializers import SRecord,SRest ,SRecordSets,STalabat
from account.api.pagination import LargeResultsSetPagination

# --------------- PYTHON UTILS ------------------#
import datetime
# --------------- DATABASE MANAGER ------------------#
import datetime
from databaseManager import DatabaseManager
db = DatabaseManager()



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

                return Response({"message": "تم التسجيل بنجاح","status":  True})
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        return Response({"message": "فشل فى التسجيل","status":  False})
#   region ACCOUNT TRANSACTION FILTER
#       region TRANSACTION USER

@api_view(['POST',])
def archiveTransactionsData(request):
    dateF = request.data.get('dateF')
    dateT = request.data.get('dateT')
    for i in CustomerInfo.objects.all().values('id'):
        customerId = i['id']
        value1 = Record.objects.filter(date__range=(dateF,dateT),isDone=True,isDown=False,customerData_id=customerId).aggregate(Sum('value'))['value__sum']
        value1 = value1 if value1 != None else 0

        value2 = Record.objects.filter(date__range=(dateF,dateT),isDone=True,isDown=True,customerData_id=customerId).aggregate(Sum('value'))['value__sum']
        value2 = value2 if value2 != None else 0

        value = value1 - value2

        data = Record(       
            value = value,  
            date = dateF,     
            time = '00:00:00',
            customerData_id=customerId,
            isDone = True,
            type='أخرى',
            isDown=False,
            accountant_id=62,
            notes='archive value',
            rest = 0,
            datetime='2021-09-01 00:00:00')    
        data.save()

        Record.objects.filter(date__range=(dateF,dateT),isDone=True,customerData_id=customerId).delete()

    return Response({"result":'تم الأرشفة','status':True})


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
@permission_classes([IsAuthenticated,])
def getTransactionsUserToday(request):
    id = request.user.id
    try: customer = CustomerInfo.objects.get(user_id=id)
    except CustomerInfo.DoesNotExist: return Response({"data":"","rest":0,"name":""})

    record = Record.objects.filter(customerData__user_id=id,date=datetime.datetime.now()).order_by(F('time').desc(nulls_last=True))[:30]
    try:
        rest = Rest.objects.get(customer_id=customer.id).value
    except Exception as e:
        rest = 0
    serializer = SRecord(record,many=True)
    return Response({"data":serializer.data,"rest":rest,"name":customer.name})

@api_view(['GET',])
@permission_classes([IsAuthenticated,])
def getTransactionsUserLimit(request):
    id = request.user.id
    try: customer = CustomerInfo.objects.get(user_id=id)
    except CustomerInfo.DoesNotExist: return Response({"data":"","rest":0,"name":""})

    record = Record.objects.filter(customerData__user_id=id).order_by(F('datetime').desc(nulls_last=True))[:30]
    try:
        rest = Rest.objects.get(customer_id=customer.id).value
    except Exception as e:
        rest = 0
    serializer = SRecord(record,many=True)
    return Response({"data":serializer.data,"rest":rest,"name":customer.name})

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
