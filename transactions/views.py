from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from firebaseServerDB import FirebaseServerice
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
db = FirebaseServerice()

def getDataList(request):
    #return JsonResponse(, safe=False)
    return render(request,'transactions/accountTable.html',{'all_data':db.getAllSellers()})

def getDataListEmbed(request):
    return render(request,'transactions/datatable_.html',{'all_data':db.getAllSellers()})

def getMandopTrans(request,seller):
    return JsonResponse(db.getAccountOffice(seller),safe=False)

class ApiView(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self,request,seller):
        return Response(db.getAccountOffice(seller))




