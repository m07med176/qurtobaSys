from django.urls import path,include
from transactions.api.controllers import reports



#-----------------------------

urlpatterns = [
        path('api/reports/',reports.getReports)  
    ]
