from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from fawryCodesApp.models import FawryCodes
from fawryCodesApp.api.serializers import SFawryCodes
from rest_framework import viewsets
# APIVIEW
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter,OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from account.api.pagination import LargeResultsSetPagination

class FawryCodesMVS(viewsets.ModelViewSet):
    pagination_class = LargeResultsSetPagination
    queryset = FawryCodes.objects.all()
    serializer_class = SFawryCodes
    filter_backends = [SearchFilter,OrderingFilter,DjangoFilterBackend]
    filterset_fields = ['serviceKind']
    search_fields = ["serviceName","serviceName"]
    ordering_fields = ['date', 'dateTime']
    def update(self, request, *args, **kwargs):
        super(FawryCodesMVS, self).update(request, *args, **kwargs)
        return Response({"message": "تم تعديل الكود بنجاح","status":  True})
    def create(self, request, *args, **kwargs):
        super(FawryCodesMVS, self).create(request, *args, **kwargs)
        return Response({"message": "تم إضافه الكود بنجاح","status":  True})
    def destroy(self, request, *args, **kwargs):
        super(FawryCodesMVS, self).destroy(request, *args, **kwargs)
        return Response({"message": "تم حذف الكود بنجاح","status":  True})

@api_view(['GET',])
def getOnItem(request):
    try:
        allCodes  = FawryCodes.objects.get(id=1)
    except FawryCodes.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        ser = SFawryCodes(allCodes)
        return Response(ser.data)

@api_view(['PUT',])
def updateItem(request):
    try:
        allCodes  = FawryCodes.objects.get(id=1)
    except FawryCodes.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == "PUT":
        ser = SFawryCodes(allCodes,data=request.data)
        data = {}
        if ser.is_valid():
            ser.save()
            data['success'] =  "data update successful"
            return Response(data=data)
        return Response(ser.errors,status= status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE',])
def deleteItem(request):
    try:
        allCodes  = FawryCodes.objects.get(id=1)
    except FawryCodes.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == "DELETE":
        operation = allCodes.delete()
        data = {}
        if operation:
            data['success'] =  "data delete successful"
        else:
            data['failler'] =  "data delete not successful"
        return Response(data=data)

@api_view(['POST',])
def createItem(request):
    item  = FawryCodes()
    if request.method == "POST":
        ser = SFawryCodes(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data,status = status.HTTP_201_CREATED)
        return Response(ser.data,status = status.HTTP_400_BAD_REQUEST)
