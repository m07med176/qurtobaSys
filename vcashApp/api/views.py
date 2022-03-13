# ------------ API AND  APIVIEW AND VIEWSETS-----------#
import datetime
from pyexpat import model
from django.contrib.auth import authenticate
# API UTILS
from rest_framework import status
from rest_framework.response import Response
from django.urls import reverse


from django_filters import rest_framework as filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter,OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.generics import ListAPIView  # ListAPIView
from rest_framework import viewsets  			 # VIEWSETS
from rest_framework.views import APIView  		 # APIVIEW
# ------------ SERIALIZERS AND MODEL -----------#
from vcashApp.models import SimLog,Sim,Device,TransactionsCash
from vcashApp.api.serializers import (
    SSim,SSimLog,SDevice,STransactionsCash,SSimCollection,SDeviceCollection,
    STransactionsCashCollection,SSimCollectionRetrieve)

@api_view(['POST',])
def insertAndRemoveSim(request):
    """
    # insert and remove sim
    -----------------------
    1 - get number and get device number
    2- check if this number recorded before
    3- check if this number is the same of last number of log sim
        1- get last recorded log sim
        2- make if condition
    4- update remove record date ,time and datetime of last number
    5 - record insert record date,time and datetime of new number
    """
    number = request.query_params.get('number','')
    try:
        cSim = Sim.objects.get(phone = number)
        oSim = SimLog.objects.all().last()
        date  = datetime.datetime.now().date()
        time  = datetime.datetime.now().time()
        datetime  = datetime.datetime.now()

        if oSim == None:  # if there is no log
            cSim.isused = True
            cSim.save()
            # insert new sim
            nSim = SimLog()
            nSim.sim = cSim
            nSim.value = cSim.value
            nSim.timeinsert = time
            nSim.datetimeinsert = datetime
            nSim.dateinsert = date
            nSim.save()
            return Response({"result":'تم تغيير الشريحه بنجاح','status':True})
            
        if oSim.sim.phone != cSim.phone:
            # update remove
            oSim.timeremove = time
            oSim.datetimeremove = datetime
            oSim.dateremove = date
            oSim.save()

            oSi = oSim.sim
            oSi.isused = False
            oSi.save()

            cSim.isused = True
            cSim.save()
            # insert new sim
            nSim = SimLog()
            nSim.sim = cSim
            nSim.value = cSim.value
            nSim.timeinsert = time
            nSim.datetimeinsert = datetime
            nSim.dateinsert = date
            nSim.save()
            return Response({"result":'تم تغيير الشريحه بنجاح','status':True})
        return Response({"result":'الشريحه الحالية لم تتغير','status':False})
    except Sim.DoesNotExist:
        return Response({"result":'لم يتم تسجيل هذه الشريحه','status':False})

@api_view(['PUT',])
def updateCoast(request):
    number = request.data.get('number','')
    coast = request.data.get('coast','0')
    try:
        sim = Sim.objects.get(phone = number)
        sim.value = coast
        sim.save()
    except Sim.DoesNotExist:
        return Response({"result":'لم يتم تسجيل هذه الشريحه','status':False})
    return Response({"result":'تم تحديث الرصيد','status':True})

class SimMVS(viewsets.ModelViewSet):
    queryset = Sim.objects.all()
    serializer_class = SSim
    filter_backends     = [OrderingFilter,DjangoFilterBackend]
    filterset_fields    = '__all__'
    ordering_fields     = '__all__'
    lookup_field        = 'phone'

    def update(self, request, *args, **kwargs):
        super(SimMVS, self).update(request, *args, **kwargs)
        return Response({"message": "تم تعديل الشريحة بنجاح","status":  True})
        
    def list(self, request, *args, **kwargs):
        self.serializer_class = SSimCollection
        return super(SimMVS, self).list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.isused = True
        instance.save()
        self.serializer_class = SSimCollectionRetrieve
        return super(SimMVS, self).retrieve(request, *args, **kwargs)


    def create(self, request, *args, **kwargs):
        request.data['user'] = request.user.id
        super(SimMVS, self).create(request, *args, **kwargs)
        return Response({"message": "تم إضافه الشريحة بنجاح","status":  True})
    def destroy(self, request, *args, **kwargs):
        super(SimMVS, self).destroy(request, *args, **kwargs)
        return Response({"message": "تم حذف الشريحة بنجاح","status":  True})

class SimLogMVS(viewsets.ModelViewSet):
    queryset = SimLog.objects.all()
    serializer_class = SSimLog
    filter_backends     = [OrderingFilter,DjangoFilterBackend]
    filterset_fields    = '__all__'
    ordering_fields     = '__all__'
    def update(self, request, *args, **kwargs):
        super(SimLogMVS, self).update(request, *args, **kwargs)
        return Response({"message": "تم تعديل الشريحة بنجاح","status":  True})
    def create(self, request, *args, **kwargs):
        request.data['user'] = request.user.id
        super(SimLogMVS, self).create(request, *args, **kwargs)
        return Response({"message": "تم إضافه الشريحة بنجاح","status":  True})
    def destroy(self, request, *args, **kwargs):
        super(SimLogMVS, self).destroy(request, *args, **kwargs)
        return Response({"message": "تم حذف الشريحة بنجاح","status":  True})

class DeviceMVS(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = SDevice
    filter_backends     = [OrderingFilter,DjangoFilterBackend]
    filterset_fields    = '__all__'
    ordering_fields     = '__all__'
    #lookup_field        = 'imei'

    def list(self, request, *args, **kwargs):
        self.serializer_class = SDeviceCollection
        return super(DeviceMVS, self).list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        try:
            data = Device.objects.get(imei=kwargs[self.lookup_field])
            return Response(SDeviceCollection(data,many=False).data)
        except Device.DoesNotExist:
            data = Device()
            data.name = request.query_params.get('name','')
            data.deviceid = request.query_params.get('deviceid','')
            data.imei = request.query_params.get('imei','')
            data.baddress = request.query_params.get('baddress','')
            data.user = request.user
            data.save()
            return Response(SDeviceCollection(data,many=False).data)


    def update(self, request, *args, **kwargs):
        super(DeviceMVS, self).update(request, *args, **kwargs)
        return Response({"message": "تم تعديل الجهاز بنجاح","status":  True})
    def create(self, request, *args, **kwargs):
        request.data['user'] = request.user.id
        super(DeviceMVS, self).create(request, *args, **kwargs)
        return Response({"message": "تم إضافه الجهاز بنجاح","status":  True})
    def destroy(self, request, *args, **kwargs):
        super(DeviceMVS, self).destroy(request, *args, **kwargs)
        return Response({"message": "تم حذف الجهاز بنجاح","status":  True})

class DateFilter(filters.FilterSet):
    month = filters.NumberFilter(field_name='date__month', lookup_expr='exact')
    year = filters.NumberFilter(field_name='date__year', lookup_expr='exact')

    class Meta:
        model = TransactionsCash
        fields = ["device","sim","sim__isused","sim__phone","sim__number","user","user__username","customer","value","isSend","seller","date",'month','year']

class TransactionsCashMVS(viewsets.ModelViewSet):
    queryset = TransactionsCash.objects.all()
    serializer_class    = STransactionsCash
    filter_backends     = [SearchFilter,OrderingFilter,DjangoFilterBackend]
    filter_class        = DateFilter
    search_fields       = ["note","customer","operationno"]
    ordering_fields     = ['timestamp','datetime','time','value', 'rest']
    
    def list(self, request, *args, **kwargs):
        self.serializer_class = STransactionsCashCollection
        return super(TransactionsCashMVS, self).list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = STransactionsCashCollection
        return super(TransactionsCashMVS, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        super(TransactionsCashMVS, self).update(request, *args, **kwargs)
        return Response({"message": "تم تعديل التحويل بنجاح","status":  True})
    def create(self, request, *args, **kwargs):
        request.data['user'] = request.user.id
        super(TransactionsCashMVS, self).create(request, *args, **kwargs)
        return Response({"message": "تم إضافه التحويل بنجاح","status":  True})
    def destroy(self, request, *args, **kwargs):
        super(TransactionsCashMVS, self).destroy(request, *args, **kwargs)
        return Response({"message": "تم حذف التحويل بنجاح","status":  True})

"""
class SimLogMVS(viewsets.ModelViewSet):
    pagination_class = LargeResultsSetPagination
    queryset = SimLog.objects.all()
    serializer_class = SSimLog
    filter_backends = [SearchFilter,OrderingFilter,DjangoFilterBackend]
    filterset_fields = ["is_superuser","is_admin","is_staff","is_active","type"]
    search_fields = ["email","username","phone","account_no"]
    ordering_fields = ['type','username','date_joined', 'last_login']
    def update(self, request, *args, **kwargs):
        super(UsersMVS, self).update(request, *args, **kwargs)
        return Response({"message": "تم تعديل المستخدم بنجاح","status":  True})
    def create(self, request, *args, **kwargs):
        super(UsersMVS, self).create(request, *args, **kwargs)
        return Response({"message": "تم إضافه المستخدم بنجاح","status":  True})
    def destroy(self, request, *args, **kwargs):
        super(UsersMVS, self).destroy(request, *args, **kwargs)
        return Response({"message": "تم حذف المستخدم بنجاح","status":  True})

"""