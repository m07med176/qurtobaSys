# ------------ API AND  APIVIEW AND VIEWSETS-----------#
# API UTILS
from rest_framework.response import Response
from rest_framework import  permissions
from django.http import JsonResponse
# VIEWSETS
from rest_framework import viewsets
# APIVIEW
from rest_framework.views import APIView
from rest_framework.decorators import api_view
# ------------ SERIALIZERS -----------#
from .serializers import SCustomer_info,SMandop_Info,SCustomer,SMandopShort
# ------------ MODELS -----------#
# MODELS
from customers.models import CustomerInfo ,MandopInfo
# UTILS
from django.db.models import Q

class Customer_infoL(viewsets.ModelViewSet):
    queryset = CustomerInfo.objects.all()#.select_related('seller') #.prefetch_related('seller')
    serializer_class = SCustomer_info

class Mandop_InfoL(viewsets.ModelViewSet):
    queryset = MandopInfo.objects.all()
    serializer_class = SMandop_Info

class GetCustomersData(APIView):
    permission_classes = (permissions.AllowAny,)
    def customSerializers(self):
        queryset  =  CustomerInfo.objects.all().select_related('seller')
        data = []
        for i in queryset:
            row =  {
                "name":i.name,
                "shopName":i.shopName,
                "shopKind":i.shopKind,
                "phoneNo":i.phoneNo,
                "address":i.address,
                "seller":{
                    "id":i.seller.id,
                    "name":i.seller.name,
                    "email":i.seller.email
                },
                "accounts": i.accounts,
                "time":i.time,
                "date":i.date}
            data.append(row)
        return data

    def get(self,request):
        return Response({"data":self.customSerializers()})

#{"data":list(Customer_info.objects.all().select_related('seller'))}
# serializer = SCustomer_info(queryset,many=True)
# return Response(serializer.data)
#return JsonResponse(self.customSerializers())
# rowData = i.accounts.all()
# [{"accountsKind":d.accountsKind,"value":d.value} for d in rowData if len(rowData) != 0]


# get seller names and account no list
@api_view(['GET',])
def getSellersNamesAndAccountsNo(request):
    names = MandopInfo.objects.values('name','code')
    return Response({"data":list(names)})

# get customer names and account no list
@api_view(['GET',])
def getCustomersNamesAndAccountsNo(request):
    names = CustomerInfo.objects.values('name','deviceNo')
    return Response({"data":list(names)})

# get customer areas
@api_view(['GET',])
def getCustomersAreas(request):
    areas = CustomerInfo.objects.values('area').order_by('area').distinct('area')
    if len(areas) == 0:return Response({"data": ""})
    return Response({"data":list(areas)})

# get seller areas
@api_view(['GET',])
def getSellersAreas(request):
    areas = MandopInfo.objects.values('region').order_by('region').distinct('region')
    if len(areas) == 0:return Response({"data": ""})
    return Response({"data":list(areas)})

# get all auto complete data
@api_view(['GET',])
def getAllAutocompleteData(request):
    sellerAreas = MandopInfo.objects.values('region').order_by('region').distinct('region')
    customerAreas = CustomerInfo.objects.values('area').order_by('area').distinct('area')
    customerNames = CustomerInfo.objects.values('name','deviceNo')
    sellerNames = MandopInfo.objects.values('name','code')
    return Response({
        "sellerAreas":list(sellerAreas),
        "customerAreas":list(customerAreas),
        "sellerNames":list(sellerNames),
        "customerNames":list(customerNames)
    })

@api_view(['GET',])
def getCustomerByDeviceNoOrName(request,name):
        if name.isdigit():
            customer = CustomerInfo.objects.filter(Q(deviceNo=name)).select_related('seller') #deviceNo__startswith
        else:
            customer = CustomerInfo.objects.filter(Q(name=name)).select_related('seller')
        serializer = SCustomer(customer, many=True)
        return Response({"results": serializer.data})

@api_view(['GET',])
def getSellerByAccountNoOrName(request,name):
        if name.isdigit():
            seller = MandopInfo.objects.filter(Q(code=name)) 
        else:
            seller = MandopInfo.objects.filter(Q(name=name))
        serializer = SMandop_Info(seller,many=True)
        return Response({"results": serializer.data})

@api_view(['DELETE',])
def deleteSeller(request,id):
    customer = CustomerInfo.objects.filter(seller_id = id).count()
    if customer == 0:
        MandopInfo.objects.get(id=id).delete()
        return Response({"results": "تم حذف المندوب بنجاح","status":True})
    else:
        return Response({"results": f"يملك المندوب {customer} عميل لا يمكن حذفه","status":False})
