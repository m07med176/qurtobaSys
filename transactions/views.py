from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from firebaseServerDB import FirebaseServerice
db = FirebaseServerice()

def home(request):
    #return JsonResponse(, safe=False)
    return render(request,'transactions\dataTable.html',{'all_data':db.getAllSellers()})
