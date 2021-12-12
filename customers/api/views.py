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
from .serializers import SCustomer_info,SCustomerInfo,SMandopInfo_Normal,SCustomer,SMandopShort
# ------------ MODELS -----------#
# MODELS
from customers.models import CustomerInfo ,MandopInfo ,Areas
from transactions.models import Rest
# UTILS
from django.db.models import Q

class Customer_infoL(viewsets.ModelViewSet):
    queryset = CustomerInfo.objects.all()
    serializer_class = SCustomerInfo
    def update(self, request, *args, **kwargs):
        super(Customer_infoL, self).update(request, *args, **kwargs)
        return Response({"message": "تم تعديل العميل بنجاح","status":  True})
    def create(self, request, *args, **kwargs):
        super(Customer_infoL, self).create(request, *args, **kwargs)
        return Response({"message": "تم إضافة العميل بنجاح","status":  True})

class Mandop_InfoL(viewsets.ModelViewSet):
    queryset = MandopInfo.objects.all()
    serializer_class = SMandopInfo_Normal
    def update(self, request, *args, **kwargs):
        super(Mandop_InfoL, self).update(request, *args, **kwargs)
        return Response({"message": "تم تعديل المندوب بنجاح","status":  True})
    def create(self, request, *args, **kwargs):
        super(Mandop_InfoL, self).create(request, *args, **kwargs)
        return Response({"message": "تم إضافة المندوب بنجاح","status":  True})

class GetCustomersData(viewsets.ModelViewSet):
    queryset = CustomerInfo.objects.all().order_by('area','name')
    serializer_class = SCustomer

class GetCustomersDataBySeller(viewsets.ReadOnlyModelViewSet):
    serializer_class = SCustomer
    def get_queryset(self,**kwargs):
        seller = self.kwargs['seller']
        return CustomerInfo.objects.filter(seller=seller).order_by('area','name')


# get customer by email user
@api_view(['GET',])
def getCustomersByEmail(request,email):
    customers = CustomerInfo.objects.filter(seller__email=email)
    serializer = SCustomer(customers, many=True)
    return Response({"results":serializer.data})

# region Get By Number Or Name
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
        serializer = SMandopInfo_Normal(seller,many=True)
        return Response({"results": serializer.data})

# endregion Get By Number Or Name

# region All DATA
# Get All Seller
@api_view(['GET',])
def getAllSellers(request):
    sellers = MandopInfo.objects.all()
    serializer = SMandopInfo_Normal(sellers, many=True)
    return Response({"results":serializer.data})

# Get All Customer
@api_view(['GET',])
def getAllCustomer(request):
    customers = CustomerInfo.objects.all()
    serializer = SCustomer(customers, many=True)
    return Response({"results":serializer.data})
# endregion All DATA

# region get List
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
# endregion get List

# region AutoComplete And Areas
@api_view(['GET',])
def getCustomersAreas(request):
    seller = request.query_params.get('seller')
    if seller != None and seller.isdigit():
        customerAreas = CustomerInfo.objects.filter(seller=seller).values('area').order_by('area').distinct('area')
    else:
        customerAreas = CustomerInfo.objects.values('area').order_by('area').distinct('area')
    return Response({"data":list(customerAreas)  })

# http://127.0.0.1:8000/customers/api/editAreas/
@api_view(['PUT',])
def editCustomersAreas(request):
    try:
        old = request.query_params.get('old')
        new = request.query_params.get('new')
        no = CustomerInfo.objects.filter(area=old).update(area=new)
        return Response({"message": f" تم تعديل المنطقة بنجاح ل{no} عميل","status":  True})
    except Exception as e:
        return Response({"message": "فشل فى تعديل المنطقة","status":  False})

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
# endregion AutoComplete And Areas

# region Delete Rank  
@api_view(['DELETE',])
def deleteSeller(request,id):
    customer = CustomerInfo.objects.filter(seller_id = id).count()
    if customer == 0:
        MandopInfo.objects.get(id=id).delete()
        return Response({"results": "تم حذف المندوب بنجاح","status":True})
    else:
        return Response({"results": f"يملك المندوب {customer} عميل لا يمكن حذفه","status":False})

@api_view(['DELETE',])
def deleteCustomer(request,id):
    rest = Rest.objects.filter(customer_id=id).exists()
    if rest:
        value = Rest.objects.get(customer_id=id).value
        if value == 0:
            CustomerInfo.objects.get(id=id).delete()
            return Response({"results": "تم حذف العميل بنجاح","status":True})
        else:
            return Response({"results": f"مطلوب من العميل مبلغ وقدره {value} جنيه لا يمكن حذفه","status":False})
    else:
            CustomerInfo.objects.get(id=id).delete()
            return Response({"results": "تم حذف العميل بنجاح","status":True})
# endregion Delete Rank

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