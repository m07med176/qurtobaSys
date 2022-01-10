# ------------ API AND  APIVIEW AND VIEWSETS-----------#
# API UTILS
from rest_framework.response import Response
from rest_framework import  permissions
from django.http import JsonResponse
# VIEWSETS
from rest_framework import viewsets
# APIVIEW
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from main.utils.pagination import LargeResultsSetPagination
from rest_framework.decorators import api_view
# ------------ SERIALIZERS -----------#
from  customers.api.serializers import SCustomerInfo,SCustomer
# ------------ MODELS -----------#
# MODELS
from customers.models import CustomerInfo
from transactions.models import Rest
# UTILS
from django.db.models import Q


from rest_framework.filters import SearchFilter,OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination

class Customer_infoL(viewsets.ModelViewSet):
    queryset = CustomerInfo.objects.all()
    serializer_class = SCustomerInfo
    filter_backends  =  [SearchFilter,OrderingFilter,DjangoFilterBackend]
    filterset_fields =  ['pk','name','surName','shopName','deviceNo','shopKind','phoneNo','address','area','accounts','accounts_data','grade','assistant','assistant__name','seller','seller__name','user','date','time','notes','areas']
    search_fields    =  ["^name","=grade","^seller__name","^assistant__name","=deviceNo"]
    ordering_fields  =  ['pk','name','surName','shopName','deviceNo','shopKind','phoneNo','address','area','accounts','accounts_data','grade','assistant','seller','user','date','time','notes','areas']
    def update(self, request, *args, **kwargs):
        if request.user.is_admin:
            super(Customer_infoL, self).update(request, *args, **kwargs)
            return Response({"message": "تم تعديل العميل بنجاح","status":  True})
        else:
            return Response({"message": "غير مسموح لك بالتعديل","status":  False})

    def create(self, request, *args, **kwargs):
            if request.user.is_admin:
                super(Customer_infoL, self).create(request, *args, **kwargs)
                return Response({"message": "تم إضافة العميل بنجاح","status":  True})
            else:
                return Response({"message": "غير مسموح لك بالإضافة","status":  False})


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

# endregion Get By Number Or Name

# region All DATA

# Get All Customer
@api_view(['GET',])
def getAllCustomer(request):
    customers = CustomerInfo.objects.all()
    serializer = SCustomer(customers, many=True)
    return Response({"results":serializer.data})
# endregion All DATA

# region get List

class GetCustomersData(ListAPIView):
    queryset = CustomerInfo.objects.all().order_by('area','name')
    serializer_class = SCustomer
    pagination_class = LargeResultsSetPagination


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


# endregion AutoComplete And Areas

# region Delete Rank  
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
    # def get(self,request):
    #     return Response({"data":self.customSerializers()})

#{"data":list(Customer_info.objects.all().select_related('seller'))}
# serializer = SCustomer_info(queryset,many=True)
# return Response(serializer.data)
#return JsonResponse(self.customSerializers())
# rowData = i.accounts.all()
# [{"accountsKind":d.accountsKind,"value":d.value} for d in rowData if len(rowData) != 0]

# endregion Trash