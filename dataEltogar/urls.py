from django.urls import path
from dataEltogar import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
            # تحليل داتا التجار
            path('analys' , views.home),
            path('analys/<str:mandoop>' , views.analysMandop),
            path('getData',views.getDataList ,name = "getData"), 

            # جدول داتا التجار
            path('table',views.dataTable),      
            path('table/<str:mandoop>',views.dataTableMandoop),   

            # بورتال
            # جدول داتا التجار      
            path('table_data',views.dataTableEmbed,name = "table"),  
            # تحليل داتا التجار
            path('analys_data',views.analysMandopEmbed,name = "analys"), 
            
            ]
urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_URL)

