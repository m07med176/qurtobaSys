
from django.contrib import admin
from django.urls import path,include
import debug_toolbar
from django.conf import settings

from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from account.web.views import (
    register_view,
    logout_view,
    login_view,
    account_view,
    account_search_view )
urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('homeApp.urls')),      # ROOT
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
    
    # ACCOUNTS
    path('account/', include('account.web.urls')),
    path('register/',register_view,name= "register"),
    path('logout/',logout_view,name= "logout"),
    path('login/',login_view,name= "login"),
    path('account/',account_view,name= "account"),

    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='password_reset/password_change_done.html'), 
    name='password_change_done'),

    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='password_reset/password_change.html'), 
        name='password_change'),

    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset/password_reset_done.html'),name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset/password_reset_complete.html'),name='password_reset_complete'),
    
    path('search/', account_search_view, name="search"),
]


if settings.DEBUG:
    urlpatterns +=path('__debug__/', include(debug_toolbar.urls)),
