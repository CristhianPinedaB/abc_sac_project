
from django.db import models
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

    code = models.CharField(max_length=3,unique=True, verbose_name="Código")

    symbol = models.CharField(max_length=4, verbose_name="Simbolo")

    name = models.CharField(max_length=20, verbose_name="Nombre")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")

    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de Moficación")

    def __str__(self):
        return f"{self.symbol} {self.code}"

    class Meta:
        db_table = "currency"
        verbose_name = "Moneda"


class Order(models.Model):
    """
    Clase de Orden de Pedido
    """
 
    number_id = models.AutoField(primary_key=True, db_column='number_id')
    client = models.ForeignKey(Client, default=None, db_column="client_id", verbose_name="Cliente")
    address_order = models.CharField(max_length=50, db_column='address_order', verbose_name="Direccion de entrega")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de Moficación")
    products = models.ManyToManyField(Product, db_column='products', verbose_name='Productos')
    
    def calculate_amounts(self):
        total = functools.reduce(lambda x, y: x.sale_price + y.sale_price ,self.products)
    
    def __str__(self):
        return self.client.name_client
    
    class Meta:
        db_table = "order"
        verbose_name = "Orden de Pedido"


    # def funtion_format():
    #     year = datetime.datetime.today().year
        
    #     return str(year) + str(1).zfill(5)



