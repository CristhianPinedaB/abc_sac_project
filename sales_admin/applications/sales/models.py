from itertools import product
from locale import currency
from telnetlib import STATUS
from django.db import models
from decimal import Decimal
from django.db.models import Sum
from django.dispatch import receiver
import functools

# Create your models here.
from applications.warehouse.models import Product
from applications.crm.models import Client



class Currency(models.Model):
    """
    Clase Moneda.
    Ejemplo 1: Moneda Sol
    Código: PEN
    Simbolo: S/.
    Nombre: Sol Peruano

    Ejemplo 2: Moneda Dólares Americanos.
    Código: USD
    Simbolo: $.
    Nombre: Dólares Americanos
    """

    id = models.AutoField(primary_key=True)

    code = models.CharField(max_length=3, unique=True, verbose_name="Código")

    symbol = models.CharField(max_length=4, verbose_name="Simbolo")

    name = models.CharField(max_length=20, verbose_name="Nombre")

    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha de Creación")

    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Fecha de Moficación")

    def __str__(self):
        return f"{self.symbol} {self.code}"

    class Meta:
        db_table = "currency"
        verbose_name = "Moneda"

class OrderItem(models.Model):

    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(default=0.00, decimal_places=2, max_digits=20)
    sales_price = models.DecimalField(default=0.00, decimal_places=2, max_digits=20)
    quantity = models.PositiveIntegerField(default=1)
    discount_price = models.DecimalField(default=0.00, decimal_places=2, max_digits=20)
    total_price = models.DecimalField(default=0.00, decimal_places=2, max_digits=20)
    ordered = models.BooleanField(default=False)
    def __str__(self):
        return f'{self.product.name}'
    
    class Meta:
        db_table = "order_item"
        verbose_name = "item de pedido"
    
    def save(self,  *args, **kwargs):
        self.price = self.product.base_sale_price
        self.sales_price = self.product.sale_price
        self.discount_price = self.product.discount_amount
        self.total_price = Decimal(self.quantity) * Decimal(self.sales_price)
        if self.quantity <= self.product.stock:
            self.product.stock -= self.quantity
            self.product.save()
        super().save(*args, **kwargs)


class Order(models.Model):
    """
    Clase de Orden de Pedido
    """
    #currency_id = models.CharField(max_length=20, verbose_name="Clase")
    STATUS = (
        ('enviado', 'enviado'),
        ('entregado', 'entregado'),
        ('pagado', 'pagado'),
    )

    number_id = models.AutoField(primary_key=True, db_column='number_id')
    status = models.CharField(
        max_length=10, choices=STATUS, default='enviado', db_column='estados')

    number_order = models.CharField(
        max_length=10, db_column='number_order',default='', verbose_name="Numero de Pedido")

    client = models.ForeignKey(Client, related_name='orders', on_delete=models.CASCADE,
                               default=None, db_column="client_id", verbose_name="Cliente")
    address_order = models.CharField(
        max_length=50, db_column='address_order', verbose_name="Direccion de entrega")
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha de Creación")

    # Fecha de entrega
    delivered_at = models.DateTimeField(
        auto_now=True, verbose_name="Fecha de Entrega")

    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Fecha de Moficación")
    items = models.ManyToManyField(
        OrderItem, db_column='items', verbose_name='Item de productos')

    total_amount = models.DecimalField(
        max_digits=20, decimal_places=2, blank = True, default=Decimal('0.0000'), db_column='total')
    subtotal_amount = models.DecimalField(
        max_digits=20, decimal_places=2, blank = True, default=Decimal('0.0000'), db_column='subtotal')
    igv = models.DecimalField(
        max_digits=20, decimal_places=2, blank = True, default=Decimal('0.0000'), db_column='igv')
    total_discount_amount = models.DecimalField(
        max_digits=7, decimal_places=2, blank = True, default=Decimal('0.0000'), verbose_name="Total Descuento")

    def save(self, *args, **kwargs):
        self.igv = round((int(18)/100)*float(self.subtotal_amount), 2)
        self.total_amount = Decimal(self.subtotal_amount) + Decimal(self.igv)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.client.name_client

    class Meta:
        db_table = "order"
        verbose_name = "Orden de Pedido"
    



  