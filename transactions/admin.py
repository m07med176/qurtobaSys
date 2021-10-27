from django.contrib import admin
from . import models 
admin.site.register(models.Rest)
admin.site.register(models.Record)
admin.site.register(models.Talabat)