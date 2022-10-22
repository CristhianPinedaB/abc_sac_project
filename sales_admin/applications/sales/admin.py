from django.contrib import admin

from applications.sales.models import Currency, Order, OrderItem

# Agregamos al modelo Currency al django admin
admin.site.register(Currency)
admin.site.register(Order)
admin.site.register(OrderItem)