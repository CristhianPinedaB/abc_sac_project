from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_http_methods
from applications.warehouse.models import ProductCategory
from django.views.decorators.csrf import csrf_protect

from applications.sales.forms import OrderForm, OrderItemForm
from django.http import HttpResponse

# Create your views here.

def index(request):
    """
    Vista Basada en Función.
    Función que devuelve página home del módulo de almacén.
    """
    return render(request, 'sales/index.html')


def new(request):
    """
    Función que devuelve el formulario para agregar un nuevo pedido 
    """
    form = OrderForm()
    formitem = OrderItemForm()
    return render(request, "sales/orders/new.html", {
        'form': form,
        'formitem' :formitem
    })

def order_list(request):
    """
    Función que devolverá la lista de categorías.
    Vista basada en función.
    """
    pass

@require_http_methods(["POST"])
@csrf_protect
def save(request):
    """
    Función para registrar los datos del pedido en la base de datos.
    """
    pass
