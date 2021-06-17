from django.urls import path
from transactions import views
urlpatterns = [
            path('' , views.getDataList),
            #path('analys/<str:mandoop>' , views.analysMandop),
            #path('table',views.dataTable),      
            #path('table/<str:mandoop>',views.dataTableMandoop),        
            #path('getData',views.getDataList ,name = "getData"), 
            
            ]
