from django.urls import path
from dataEltogar import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
            path('analys' , views.home),
            path('analys/<str:mandoop>' , views.analysMandop),
            path('table',views.dataTable),      
            path('table/<str:mandoop>',views.dataTableMandoop),        
            path('getData',views.getDataList ,name = "getData"), 
            
            ]
