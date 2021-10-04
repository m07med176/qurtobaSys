from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from fawryCodesApp.models import FawryCodes
from fawryCodesApp.api.serializers import FawryCodesSer

from rest_framework import viewsets

@api_view(['GET',])
def getOnItem(request):
    try:
        allCodes  = FawryCodes.objects.get(id=1)
    except FawryCodes.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        ser = FawryCodesSer(allCodes)
        return Response(ser.data)

@api_view(['PUT',])
def updateItem(request):
    try:
        allCodes  = FawryCodes.objects.get(id=1)
    except FawryCodes.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == "PUT":
        ser = FawryCodesSer(allCodes,data=request.data)
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
        ser = FawryCodesSer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data,status = status.HTTP_201_CREATED)
        return Response(ser.data,status = status.HTTP_400_BAD_REQUEST)


class FawryCodesL(viewsets.ModelViewSet):
    queryset = FawryCodes.objects.all()
    serializer_class = FawryCodesSer
