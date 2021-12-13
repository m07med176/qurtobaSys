from django.urls import path
from transactions.api.controllers import  firebase
urlpatterns = [
        # region firebase
        path('' , firebase.getDataList),
        path('transactions' , firebase.getDataListEmbed , name= "transactions"),
        path('trans/<str:seller>',firebase.getMandopTrans , name ='trans' ),
        path('transApi/<str:seller>/<str:manager>',firebase.ApiView.as_view() , name ='transApi' ),
        path('office_trans/<str:manager>/<int:deviceNo>/',firebase.GetTrans.as_view() , name = 'office_trans'),
        #path('analys/<str:mandoop>' , views.analysMandop),
        #path('table',views.dataTable),      
        #path('table/<str:mandoop>',views.dataTableMandoop),        
        #path('getData',views.getDataList ,name = "getData"), 
        # endregion       
    ]
