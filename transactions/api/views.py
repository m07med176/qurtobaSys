from rest_framework import viewsets
from django.db.models import Q
from django.db.models import Prefetch
# ------------ APIVIEW -----------#
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import  permissions
# ------------ MODELS -----------#
from transactions.models import Rest,Record
from customers.models import CustomerInfo, MandopInfo 
# ------------ SERIALIZERS -----------#
#from customers.api.serializers import SCustomer_info
from transactions.api.serializers import SRecord,SRest ,SMainRest
from customers.api.serializers import SCustomer_info,SMandop_Info 

class RestL(viewsets.ModelViewSet):
    queryset = Rest.objects.all()
    serializer_class = SRest

class RecordL(viewsets.ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = SRecord

class GetRest(APIView):
    permission_classes = (permissions.AllowAny,)
    def customSerializers(self,name):
        if name.isdigit():
            customer = CustomerInfo.objects.filter(Q(deviceNo=name)) 
        else:
            customer = CustomerInfo.objects.filter(Q(name=name))
        if len(customer) == 0:
            return "0"
        rest=Rest.objects.filter(customer__id=customer[0].id)
        if len(rest) != 0:
            return str(rest[0].rest)
        else:
            return "0"

    def get(self,request,name):
        return Response({"data":self.customSerializers(name)})

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
