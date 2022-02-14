from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
#-----------------------------
from transactions.api import views as api
from transactions.api.controllers import transactions,reports,mainRest
#-----------------------------
from rest_framework import routers
router = routers.DefaultRouter()
router.register('talabat',api.TalabatMVS)
router.register('record',transactions.RecordL)
router.register('report',reports.DateLogL)
router.register('rest',mainRest.RestL)
router.register('rest-comulate',mainRest.RestComulate)
router.register('rest-last',mainRest.RestLast)

# Urls -----------------------
from transactions.api.urls import urls_firebase,urls_trans,urls_accounts,urls_rest,urls_reports

# root : transactions
urlpatterns = [
        #---| api |---#
        path('api/', include(router.urls)),
    ]
urlpatterns +=urls_reports.urlpatterns
urlpatterns +=urls_rest.urlpatterns
urlpatterns +=urls_trans.urlpatterns
urlpatterns +=urls_accounts.urlpatterns
urlpatterns +=urls_firebase.urlpatterns
urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_URL)
