
from django.db import models

# Create your models here.

class Client(models.Model):
    """
    Clase para los Clientes
    """
    DOCUMENTS_LIST = (
        ('DNI', 'Documento de identidad',),
        ('RUC', 'Registro Unico de Contribuyente'),
        ('PAS', 'Pasaporte'),
    )

    TYPE_CLIENTS = (
        ('Restaurantes', 'Restaurantes'),
        ('Hoteles', 'Hoteles'),
        ('Tiendas', 'Tiendas'),
        ('Otro', 'Otro'),
    )

    id = models.AutoField(primary_key=True, db_column='id')
    document_type = models.CharField(max_length=3, choices=DOCUMENTS_LIST, db_column='document_type',verbose_name = 'Tipo de Documento')
    document_number = models.CharField(max_length=15, unique=True, db_column='document_number',verbose_name = 'Numero de Documento')
    name_client = models.CharField(max_length=30, db_column='name_client', verbose_name = 'Razon social ')
    type_client = models.CharField(max_length=30, choices=TYPE_CLIENTS,db_column='type_client', verbose_name = 'Tipo de Cliente')
    address = models.CharField(max_length=50, db_column='address',verbose_name = 'Direccion')
    phone_number = models.CharField(max_length=15, blank=True, db_column='phone_number',verbose_name = 'Telefono')

    def __str__(self):
        return self.name_client

    class Meta:
        db_table = "clients"
        verbose_name = "Clientes"