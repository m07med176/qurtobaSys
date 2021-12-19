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
from  customers.api.serializers import SCustomer_info,SCustomerInfo,SMandopInfo_Normal,SCustomer,SMandopShort
# ------------ MODELS -----------#
# MODELS
from customers.models import CustomerInfo ,MandopInfo ,Areas
from transactions.models import Rest
# UTILS
from django.db.models import Q

class Mandop_InfoL(viewsets.ModelViewSet):
    queryset = MandopInfo.objects.all()
    serializer_class = SMandopInfo_Normal
    def update(self, request, *args, **kwargs):
        super(Mandop_InfoL, self).update(request, *args, **kwargs)
        return Response({"message": "تم تعديل المندوب بنجاح","status":  True})
    def create(self, request, *args, **kwargs):
        super(Mandop_InfoL, self).create(request, *args, **kwargs)
        return Response({"message": "تم إضافة المندوب بنجاح","status":  True})

# region Get By Number Or Name

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

# endregion All DATA

# region get List
# get seller names and account no list
@api_view(['GET',])
def getSellersNamesAndAccountsNo(request):
    names = MandopInfo.objects.values('name','code')
    return Response({"data":list(names)})


# endregion get List

# region Delete Rank  
@api_view(['DELETE',])
def deleteSeller(request,id):
    customer = CustomerInfo.objects.filter(seller_id = id).count()
    if customer == 0:
        MandopInfo.objects.get(id=id).delete()
        return Response({"results": "تم حذف المندوب بنجاح","status":True})
    else:
        return Response({"results": f"يملك المندوب {customer} عميل لا يمكن حذفه","status":False})

# endregion Delete Rank