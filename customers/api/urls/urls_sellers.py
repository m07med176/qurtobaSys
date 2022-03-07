from django.urls import path
# ----------- Views ----------#
from customers.api.controllers import sellers
#-----------------------------

urlpatterns = [
    # region seller
    path('api/sellers_names/',sellers.getSellersNamesAndAccountsNo),
    path('api/sellers_qname/<str:name>/',sellers.getSellerByAccountNoOrName),
    path('api/all_seller/',sellers.getAllSellers),
    path('api/all_seller-sort/',sellers.getAllSellersShort),
    path('api/delete_seller/<str:id>/',sellers.deleteSeller),
    # endregion seller

]
