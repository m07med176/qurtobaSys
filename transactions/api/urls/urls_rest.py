from django.urls import path,include
#-----------------------------
from transactions.api.controllers import mainRest as api

urlpatterns = [
        # region Main Rest
        path('api/getRest/<str:name>/',api.GetRest.as_view()),
        path('api/getRestDateCalc/',api.getRestDateCalc),
        # seller should pay
        path('restSeller/<str:email>/',api.getSellerRest),
        path('restAssistance/<str:email>/',api.getAssistanceRest),
        path('api/getAllRest/',api.getAllRest ),
        path('api/getAllRestId/<str:id>/',api.getSellerRestId),
        path('api/rest_gte/<int:value>/',api.getAllRestGte),
        # endregion Main Rest
    ]