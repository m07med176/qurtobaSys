
from django.contrib import admin
from django.urls import path,include
import debug_toolbar
from django.conf import settings
from accountApp.web.views import (
    registration_view,
    logout_view,
    login_view,
    account_view )
urlpatterns = [
    path('', include('homeApp.urls')), # root
    path('account/', include('accountApp.urls')),
    path('customers/',include('customers.urls')),
    path('dataEltogar/',include('dataEltogarApp.urls')),
    path('transactions/',include('transactions.urls')),
    path('fawryCodes/',include('fawryCodesApp.urls')),

    path('storeApp/',include('storeApp.urls')),
    path('productsSelesApp/',include('productsSelesApp.urls')),
    path('fawrySelesApp/',include('fawrySelesApp.urls')),
    path('sellersApp/',include('sellersApp.urls')),

    # REST FRAMEWORK APIs
    path('api/fawryCodes/',include('fawryCodesApp.api.urls','fawry_api')),
    path('api/vono/',include('vonoApp.api.urls','vono_api')),
    

        # accounts
    path('admin/', admin.site.urls),
    path('register/',registration_view,name= "register"),
    path('logout/',logout_view,name= "logout"),
    path('login/',login_view,name= "login"),
    path('account/',account_view,name= "account"),
]


if settings.DEBUG:
    urlpatterns +=path('__debug__/', include(debug_toolbar.urls)),
