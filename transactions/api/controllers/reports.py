# region MODULE
# ------------ API -----------#
# UTILS
from rest_framework.response import Response
from rest_framework import  permissions
# VIEWSETS
from rest_framework import viewsets
# APIVIEW
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.filters import SearchFilter,OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status

from main.utils.permissions import IS_ACTIVATE,IS_ADMIN,IS_STAFF,IS_SUPERUSER,IS_HEADER
# ------------ MODELS -----------#
# MODELS
from transactions.models import LogDate,Record,Rest
# UTILS
from django.db.models import Q,F,Prefetch,Sum
import pytz
# ------------ SERIALIZERS -----------#
from transactions.api.serializers import SLogDate

# --------------- PYTHON UTILS ------------------#
import datetime

class DateLogL(viewsets.ModelViewSet):
    queryset = LogDate.objects.all()
    serializer_class = SLogDate
    def update(self, request, *args, **kwargs):
        super(DateLogL, self).update(request, *args, **kwargs)
        return Response({"message": "تم التعديل بنجاح","status":  True})
    def create(self, request, *args, **kwargs):
        super(DateLogL, self).create(request, *args, **kwargs)
        return Response({"message": "تم تسجيل جميع الأرصدة بنجاح","status":  True})
    def destroy(self, request, *args, **kwargs):
        super(DateLogL, self).destroy(request, *args, **kwargs)
        return Response({"message": "تم الحذف بنجاح","status":  True})

def get_rest(records):
    summitions = 0
    for record in records:
        start = "2021-09-06 19:00:59+00"
        end = record.datetime
        customer_id = record.customerData.id

        value1 = Record.objects.filter(customerData_id=customer_id,isDown=False,datetime__range = (start,end)).aggregate(Sum('value'))['value__sum'] if Record.objects.filter(customerData_id=customer_id,isDown=False,datetime__range = (start,end)).aggregate(Sum('value'))['value__sum'] != None else 0
        value2 = Record.objects.filter(customerData_id=customer_id,isDown=True,datetime__range = (start,end)).aggregate(Sum('value'))['value__sum'] if Record.objects.filter(customerData_id=customer_id,isDown=True,datetime__range = (start,end)).aggregate(Sum('value'))['value__sum'] != None else 0
        sum  = value1 - value2
        summitions+=sum
    return summitions

@api_view(['GET',])
@permission_classes([IS_HEADER,])
def getReports(request):
    tz = pytz.timezone('Africa/Cairo')
    listData = ['فورى','كاش','تحصيل','أمان','طاير','شراء','الدفع','بى','أخرى']

    id = request.query_params.get('id')
    df = request.query_params.get('df')
    dt = request.query_params.get('dt')
    
    dtf = request.query_params.get('dtf')
    dtt = request.query_params.get('dtt')

    dtfn = request.query_params.get('dtfn')
    dttn = request.query_params.get('dttn')

    if id != None and id.isdigit():
        d       = LogDate.objects.get(pk=int(id)).datetime.astimezone(tz)
        pd      = LogDate.objects.get(pk=int(id)-1).datetime.astimezone(tz)
        date1   = d.strftime("%m/%d/%Y %I:%M:%p")
        date2   = pd.strftime("%m/%d/%Y %I:%M:%p")
        results = Record.objects.filter(datetime__range = (str(d),str(pd))) #.order_by('-datetime')
        #data = results.order_by('customerData_id').distinct("customerData_id")
        #rest    = get_rest(data)
    
    elif df != None and dt != None:
        date1   = df
        date2   = dt
        results = Record.objects.filter(date__range = (df,dt))
        #data = results.order_by('customerData_id').distinct("customerData_id")
        #rest  = get_rest(data)

    elif dtf != None and dtt != None:
        dtf = dtf.replace(" ","+")
        dtt = dtt.replace(" ","+")
        #date_from_obj = datetime.datetime.strptime(dtf, '%Y-%m-%d %H:%M:%S.%f+%H:%H').astimezone(tz)
        #date_to_obj = datetime.datetime.strptime(dtt, '%Y-%m-%d %H:%M:%S.%f+%H:%H').astimezone(tz)
        date_from_obj = datetime.datetime.fromisoformat(dtf)
        date_to_obj = datetime.datetime.fromisoformat(dtt)
        date1 = date_from_obj.strftime("%m/%d/%Y %I:%M:%p")
        date2 = date_to_obj.strftime("%m/%d/%Y %I:%M:%p")
        results = Record.objects.filter(datetime__range = (str(date_from_obj),str(date_to_obj)))
        #data = results.order_by('customerData_id').distinct("customerData_id")
        #rest  = get_rest(data)

    elif dtfn != None and dttn != None:
        date_from_obj = datetime.datetime.strptime(dtfn, '%Y-%m-%d %H:%M:%S')
        date_to_obj = datetime.datetime.strptime(dttn, '%Y-%m-%d %H:%M:%S')
        date1 = date_from_obj.strftime("%m/%d/%Y %I:%M:%p")
        date2 = date_to_obj.strftime("%m/%d/%Y %I:%M:%p")
        results = Record.objects.filter(datetime__range = (str(date_from_obj),str(date_to_obj)))
        #data = results.order_by('customerData_id').distinct("customerData_id")
        #rest  = get_rest(data)
   
    else:
        ld = LogDate.objects.order_by('id').last().datetime.astimezone(tz)
        cd = datetime.datetime.now().astimezone(tz)
        date1 = ld.strftime("%m/%d/%Y %I:%M:%p")
        date2 = cd.strftime("%m/%d/%Y %I:%M:%p")
        results = Record.objects.filter(datetime__range = (str(ld),str(cd)))
        #rest = Rest.objects.all().aggregate(Sum('value'))['value__sum']
    
    record = list(results.values('type').annotate(Sum('value')))
    zeros = []
    for i in listData:
        if i not in [i['type'] for i in record]:
            zeros.append({'type':i,'value__sum':0})
    zeros.append(
        {
        'type':'المتبقى',
        'value__sum': Rest.objects.all().aggregate(Sum('value'))['value__sum'] 
        }
    )   
    return Response({"df":date1,"dt":date2,"data":record + zeros})
