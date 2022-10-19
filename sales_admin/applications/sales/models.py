
from locale import currency
from telnetlib import STATUS
from django.db import models
from decimal import Decimal
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

    status = models.CharField(
        max_length=10, choices=STATUS, default='enviado', db_column='estados')
    number_id = models.AutoField(primary_key=True, db_column='number_id')
    client = models.ForeignKey(Client, on_delete=models.CASCADE,
                               default=None, db_column="client_id", verbose_name="Cliente")
    address_order = models.CharField(
        max_length=50, db_column='address_order', verbose_name="Direccion de entrega")
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha de Creación")

    # Fecha de entrega
    date_delivered = models.DateTimeField(
        auto_now=True, verbose_name="Fecha de Entrega")

    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Fecha de Moficación")
    products = models.ManyToManyField(
        Product, db_column='products', verbose_name='Productos')

    total_amount = models.DecimalField(
        max_digits=20, decimal_places=2, blank = True, default=Decimal('0.0000'), db_column='total')
    subtotal_amount = models.DecimalField(
        max_digits=20, decimal_places=2, blank = True, default=Decimal('0.0000'), db_column='subtotal')
    igv = models.DecimalField(
        max_digits=20, decimal_places=2, blank = True, default=Decimal('0.0000'), db_column='igv')
    total_discount_amount = models.DecimalField(
        max_digits=7, decimal_places=2, blank = True, default=Decimal('0.0000'), verbose_name="Total Descuento")

    # def calculate_amounts(self):
    def save(self, *args, **kwargs):
        # Calculamos el importe subtotal
        self.subtotal_amount = functools.reduce(
            lambda x, y: x.sale_price + y.sale_price, self.products)

        # Calculamos el importe igv
        self.igv = round(
            (int(18)/100)*float(self.subtotal_amount), 2)

        # Calculamos el importe total
        self.total_amount = self.subtotal_amount + self.igv

        # Calculamos el importe total en descuento
        self.total_discount_amount = functools.reduce(
            lambda x, y: x.discount_amount + y.discount_amount, self.products)

    def __str__(self):
        return self.client.name_client

    class Meta:
        db_table = "order"
        verbose_name = "Orden de Pedido"

    # def funtion_format():
    #     year = datetime.datetime.today().year

    #     return str(year) + str(1).zfill(5)
