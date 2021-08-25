from customers.models import CustomerInfo ,MandopInfo#,Customer_account    #Customer_Image
from rest_framework import viewsets
from .serializers import SCustomer_info,SMandop_Info      #SCustomer_Image SCustomer_account
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import  permissions

class Customer_infoL(viewsets.ModelViewSet):
    queryset = CustomerInfo.objects.all()#.select_related('seller') #.prefetch_related('seller')
    serializer_class = SCustomer_info

class Mandop_InfoL(viewsets.ModelViewSet):
    queryset = MandopInfo.objects.all()
    serializer_class = SMandop_Info

# class Customer_accountL(viewsets.ModelViewSet):
#     queryset = Customer_account.objects.all()
#     serializer_class = SCustomer_account

class GetCustomersData(APIView):
    permission_classes = (permissions.AllowAny,)
    def customSerializers(self):
        queryset  =  CustomerInfo.objects.all()#.select_related('accounts')
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

