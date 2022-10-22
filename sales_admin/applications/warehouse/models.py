"""
En el archivo models.py agregamos los modelos que utilizará nuestra aplicación.
Los modelos de esta aplicación pueden ser utilizados desde otras aplicaciones.
"""
# Importamos la clase models del módulo django.db
# Link: https://docs.djangoproject.com/en/4.1/topics/db/models/
from django.db import models

# Importamos las clases MinValueValidator, MaxValueValidator para agregar validaciones
# al atributo "percent_discount"
# Link: https://docs.djangoproject.com/en/4.1/ref/validators/#module-django.core.validators
from django.core.validators import MinValueValidator, MaxValueValidator

# Importamos la clase Currency de la aplicación Sales
# from applications.sales.models import Currency


class UnitMeasure(models.Model):
    """
    Clase Unidad de Medida.

    Ejem: 
        Unidad -> (UND)
        Botella -> (BOT)
        Bolsa -> (BOL)
        Caja -> (CAJ)
        Paquete -> (PAQ)
        Galón -> (GAL)
    """

    id = models.AutoField(primary_key=True, db_column='id')
    code = models.CharField(max_length=3, unique=True, db_column='code', verbose_name="Código")
    name = models.CharField(max_length=30, db_column='name', verbose_name="Nombre")
    created_at = models.DateTimeField(auto_now_add=True, db_column='created_at', verbose_name="Fecha de Creación")
    updated_at = models.DateTimeField(auto_now=True, db_column='updated_at', verbose_name="Fecha de Moficación")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "unit_measure"

        verbose_name = "Unidades de Medida"


class ProductCategory(models.Model):
    """
    Clase Categoría de Producto.
    Ejem: Abarrotes, Limpieza, Bebidas
    """

    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=3, unique=True, verbose_name="Código")
    name = models.CharField(max_length=50, verbose_name="Nombre")
    percent_discount = models.PositiveSmallIntegerField(default=0, validators=[
                                                        MinValueValidator(0), MaxValueValidator(50)], verbose_name="Descuento (%)")
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha de Creación")
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Fecha de Moficación")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        #self.percent_discount = 5
        super(ProductCategory, self).save(*args, **kwargs)

    class Meta:
        db_table = "product_category"
        verbose_name = "Categoría de Producto"


class Product(models.Model):

    id = models.AutoField(primary_key=True)

    code = models.CharField(max_length=6, unique=True, verbose_name="Código")

    name = models.CharField(max_length=60, blank=False,
                            default=None, verbose_name="Nombre")

    # foreign_key: categoría de producto
    product_category_id = models.ForeignKey(ProductCategory, on_delete=models.CASCADE,
                                            default=None, db_column="product_category_id", verbose_name="Categoría Producto")

    # foreign_key: unidad de medida
    unit_measure_id = models.ForeignKey(UnitMeasure, on_delete=models.CASCADE,
                                        default=None, db_column="unit_measure_id", verbose_name="Unidad de Medida")

    # foreign_key: Moneda
    # currency_id = models.ForeignKey(
    #     Currency, on_delete=models.CASCADE, default=None, db_column="currency_id", verbose_name="Moneda")

    # precio de compra.
    purchase_price = models.DecimalField(
        max_digits=7, decimal_places=2, default=0, verbose_name="Precio de Compra")

    # precio de venta base
    base_sale_price = models.DecimalField(
        max_digits=7, decimal_places=2, default=0, verbose_name="Precio de Venta Base")

    # require: from django.core.validators
    percent_discount = models.PositiveSmallIntegerField(default=0, validators=[
                                                        MinValueValidator(0), MaxValueValidator(60)], verbose_name="Descuento (%)")

    discount_amount = models.DecimalField(
        max_digits=7, decimal_places=2, default=0, verbose_name="Monto Descuento")

    # precio de venta
    sale_price = models.DecimalField(
        max_digits=7, decimal_places=2, default=0, verbose_name="Precio de Venta")

    # stock: PositiveIntegerField
    stock = models.PositiveIntegerField(default=0, verbose_name="Stock")

    # Activo: BooleanField
    active = models.BooleanField(default=True, verbose_name="Activo")

    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha Creación")

    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Fecha Modificación")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        """
        Sobre escribimos el método save de la clase Model.
        """
        percent_discount = self.percent_discount
        if percent_discount < self.product_category_id.percent_discount:
            percent_discount = self.product_category_id.percent_discount
        # Calculamos el monto de descuento
        self.discount_amount = round(
            (int(percent_discount)/100)*float(self.base_sale_price), 2)
        
        # Calculamos el precio de venta
        self.sale_price = float(self.base_sale_price) - \
            float(abs(self.discount_amount))
        
        # Guardamos información del modelo
        super(Product, self).save(*args, **kwargs)

    class Meta:
        db_table = "product"
        verbose_name = "Producto"
