from django.shortcuts import render
from django.http import HttpResponse , FileResponse , JsonResponse,HttpResponseRedirect
import json
from django.shortcuts import get_object_or_404
from .forms import FCustomer_info  , FCustomer #FCustomer_Image
from .models import Customer_info,Customer,Customer_account #Customer_Image


from rest_framework import viewsets
from .serializers import SCustomer_info,SCustomer_account #SCustomer_Image

# firebase 
import json
from firebaseServerDB import FirebaseServerice
db = FirebaseServerice()
class Customer_infoL(viewsets.ModelViewSet):
    queryset = Customer_info.objects.all().prefetch_related('images')
    serializer_class = SCustomer_info


def createCustomer(request):
    dataRespose = {'message':"عفوا حدث خطأ أثناء التعديل",'status':"false","link":"#"}
    
    if request.is_ajax and request.method == "POST":
        myform = FCustomer_info(request.POST or None)
        if myform.is_valid():
            myform.save()
            dataRespose['message'] = "تم التسجيل بنجاح"
            dataRespose['status'] = "true"
            dataRespose['link'] = "#"
            return HttpResponse(
            json.dumps(dataRespose),
            content_type="application/json")
    return render(request,'customers/_customer.html',{'form':FCustomer_info})

def updateCustomer(request,id):
    dataRespose = {'message':"عفوا حدث خطأ أثناء التعديل",'status':"false","link":"#"}
    order = Customer_info.objects.get(id=id)
    if request.is_ajax and request.method == "POST":
        myform = FCustomer_info(request.POST,instance=order)
        if myform.is_valid():
            myform.save()
            dataRespose['message'] = "تم التعديل بنجاح"
            dataRespose['status'] = "true"
            dataRespose['link'] = "../../"
            return HttpResponse(
            json.dumps(dataRespose),
            content_type="application/json")
    return render(request,'customers/_customer.html',{'form':FCustomer_info(instance=order)})

def showList(request):
    return render(request,'customers/_customerList.html')

def customerTable(request):
    return render(request,'customers/customerTable.html',{"all":Customer_info.objects.all()})

def deleteCustomer(request,id):
    dataRespose = {'message':"عفوا حدث خطأ أثناء الحذف",'status':"false","link":"#"}
    if request.is_ajax and request.method == "POST":
        dataRespose['message'] = "تم الحذف بنجاح"
        dataRespose['status'] = "true"
        dataRespose['link'] = "#"
        member = Customer_info.objects.get(id=id)
        member.delete()
        return HttpResponse(
            json.dumps(dataRespose),
            content_type="application/json")
    return HttpResponseRedirect('/')

# firebase
def manadeepCustomers(request):
    return render(request,'customers/datatable_.html',db.getAllMandopCustomer())

def migrateCustomers(request,email):
    db.collectCustomers(email)
    return HttpResponse("<h1>تمت العملية بنجاح<h1>")

    

