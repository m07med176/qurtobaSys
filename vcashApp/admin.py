from django.contrib import admin
from vcashApp.models import Sim,SimLog,Device,TransactionsCash

admin.site.register(Sim)
admin.site.register(SimLog)
admin.site.register(Device)
admin.site.register(TransactionsCash)