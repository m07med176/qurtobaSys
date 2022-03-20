
from django.contrib import admin
from django.urls import path,include

from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from account.web.views import (register_view,logout_view,login_view,account_view,account_search_view )

import debug_toolbar
from django.conf import settings
from django.conf.urls import url
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions


admin.site.site_header = 'موقع الإشباح'
admin.site.site_title = 'الأشباح للإتصالات'

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('homeApp.urls')),     
    path('cash/',include('vcashApp.urls')),
    path('follow/',include('FollowUpApp.urls')),
    
    path('customers/',include('customers.urls')),
    path('transactions/',include('transactions.urls')),

    path('sellers/',include('sellersApp.urls')),
    path('store/',include('storeApp.urls')),
    path('productsSeles/',include('productsSelesApp.urls')),
    path('fawrySeles/',include('fawrySelesApp.urls')),

    path('fawryCodes/',include('fawryCodesApp.urls')),
    path('dataEltogar/',include('dataEltogarApp.urls')),
    path('code/',include('fawryCodesApp.api.urls','fawry_api')),
    path('shakawa/', include('shakawaApp.urls')),

    # region ACCOUNTS
    path('account/', include('account.urls')),
    path('register/',register_view,name= "register"),
    path('logout/',logout_view,name= "logout"),
    path('login/',login_view,name= "login"),

    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='password_reset/password_change_done.html'), name='password_change_done'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='password_reset/password_change.html'), name='password_change'),
    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset/password_reset_done.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset/password_reset_complete.html'),name='password_reset_complete'),
    path('search/', account_search_view, name="search"),
    # endregion ACCOUNTS
]


if settings.DEBUG: 
    schema_view = get_schema_view(
   openapi.Info(
      title=admin.site.site_title,
      default_version='v1',
      description="Test description",
      terms_of_service=settings.ALLOWED_HOSTS[0],
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
    )
    urlpatterns +=[
        path('__debug__/', include(debug_toolbar.urls)),
        # Swagger
        url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
        url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
        url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    ]
