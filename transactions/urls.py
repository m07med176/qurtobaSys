from django.urls import path
from transactions import views
from django.conf import settings
from django.conf.urls.static import static
# root : transactions
urlpatterns = [
        path('' , views.getDataList),
        path('transactions' , views.getDataListEmbed , name= "transactions"),
        path('trans/<str:seller>',views.getMandopTrans , name ='trans' ),
        path('transApi/<str:seller>/<str:manager>',views.ApiView.as_view() , name ='transApi' ),
        path('office_trans/<str:manager>/<int:deviceNo>/',views.GetTrans.as_view() , name = 'office_trans')
        #path('analys/<str:mandoop>' , views.analysMandop),
        #path('table',views.dataTable),      
        #path('table/<str:mandoop>',views.dataTableMandoop),        
        #path('getData',views.getDataList ,name = "getData"), 
    ]
urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_URL)
