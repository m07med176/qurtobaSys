from django.urls import path
from dataEltogar import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
            path('analys' , views.home),
            path('table',views.dataTable),              
            path('getData',views.getDataList ,name = "getData"), 
            ]
