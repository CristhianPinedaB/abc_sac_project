from django.contrib import admin

# Register your models here.
from applications.crm.models import Client

# Agregamos al modelo Currency al django admin
admin.site.register(Client)