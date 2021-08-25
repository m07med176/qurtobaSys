
# firebase 
import json
from firebaseServerDB import FirebaseServerice
db = FirebaseServerice()
from django.shortcuts import render
from django.http import HttpResponse , FileResponse , JsonResponse,HttpResponseRedirect

# firebase
def manadeepCustomers(request):
    return render(request,'customers/datatable_.html',db.getAllMandopCustomer())

def migrateCustomers(request,email):
    db.collectCustomers(email)
    return HttpResponse("<h1>تمت العملية بنجاح<h1>")

    

