from rest_framework import viewsets

from django.db.models import Q
from django.db.models import Prefetch
# ------------ APIVIEW -----------#
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import  permissions
# ------------ MODELS -----------#
from transactions.models import Rest,Record
from customers.models import CustomerInfo
# ------------ SERIALIZERS -----------#
#from customers.api.serializers import SCustomer_info
from .serializers import SRecord,SRest 

class RestL(viewsets.ModelViewSet):
    queryset = Rest.objects.all()
    serializer_class = SRest

class RecordL(viewsets.ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = SRecord

#


class GetRest(APIView):
    permission_classes = (permissions.AllowAny,)
    def customSerializers(self,name):
        if name.isdigit():
            customer = CustomerInfo.objects.filter(Q(deviceNo=name)) # | 
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
