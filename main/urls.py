"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('', include('home.urls')), # root
    path('admin/', admin.site.urls),
    path('customers/',include('customers.urls')),
    path('dataEltogar/',include('dataEltogar.urls')),
    path('transactions/',include('transactions.urls')),
    path('fawryCodes/',include('fawryCodes.urls')),

    # REST FRAMEWORK APIs
    path('api/fawryCodes/',include('fawryCodes.api.urls','fawry_api')),
    path('api/vono/',include('vono.api.urls','vono_api')),

]
