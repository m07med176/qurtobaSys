# ------------ API AND  APIVIEW AND VIEWSETS-----------#
# API UTILS
from rest_framework.response import Response
from rest_framework import  permissions
from django.http import JsonResponse
# VIEWSETS
from rest_framework import viewsets
# APIVIEW
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination

from rest_framework.decorators import api_view
# ------------ SERIALIZERS -----------#

# ------------ MODELS -----------#
# MODELS
from customers.models import CustomerInfo ,MandopInfo 
from transactions.models import Rest
# UTILS
from django.db.models import Q


# region AutoComplete 
# get all auto complete data 
@api_view(['GET',])
def getAllAutocompleteData(request):
    sellerAreas = MandopInfo.objects.values('region').order_by('region').distinct('region')
    customerAreas = CustomerInfo.objects.values('area').order_by('area').distinct('area')
    customerNames = CustomerInfo.objects.values('name','deviceNo')
    sellerNames = MandopInfo.objects.values('name','code')
    sellers = MandopInfo.objects.values('name')
    return Response({
        "sellerAreas":list(sellerAreas),
        "customerAreas":list(customerAreas),
        "sellerNames":list(sellerNames),
        "customerNames":list(customerNames),
        "sellers":list(sellers),
    })
# endregion AutoComplete 


# region Trash
    # def customSerializers(self):
    #     queryset  =  CustomerInfo.objects.all().select_related('seller')
    #     data = []
    #     for i in queryset:
    #         row =  {
    #             "name":i.name,
    #             "shopName":i.shopName,
    #             "shopKind":i.shopKind,
    #             "phoneNo":i.phoneNo,
    #             "address":i.address,
    #             "seller":{
    #                 "id":i.seller.id,
    #                 "name":i.seller.name,
    #                 "email":i.seller.email
    #             },
    #             "accounts": i.accounts,
    #             "time":i.time,
    #             "date":i.date}
    #         data.append(row)
    #     return data

    # def get(self,request):
    #     return Response({"data":self.customSerializers()})

#{"data":list(Customer_info.objects.all().select_related('seller'))}
# serializer = SCustomer_info(queryset,many=True)
# return Response(serializer.data)
#return JsonResponse(self.customSerializers())
# rowData = i.accounts.all()
# [{"accountsKind":d.accountsKind,"value":d.value} for d in rowData if len(rowData) != 0]

# endregion Trash