from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_http_methods
from applications.warehouse.models import ProductCategory
from django.views.decorators.csrf import csrf_protect
from applications.crm.forms import ClientForm
from django.http import HttpResponse

# Create your views here.

def index(request):
    """
    Vista Basada en Función.
    Función que devuelve página home del módulo de almacén.
    """
    return render(request, 'client/index.html')

def new(request):
    """
    Función que devuelve el formulario para agregar un nuevo cliente
    """
    form = ClientForm()
    return render(request, "warehouse/product_category/new.html", {
        'form': form
    })

def register_client_list(request):
    """
    Función que devolverá la lista de categorías.
    Vista basada en función.
    """
    # link: https://docs.djangoproject.com/en/4.1/topics/db/queries/

    # Obtenemos los registros de la tabla product_category
    product_category_list = ProductCategory.objects.all().order_by('-id')

    # render(request, 'template.html',variables)
    return render(request, 'warehouse/product_category/list.html', {
        'product_category_list': product_category_list
    })

@require_http_methods(["POST"])
@csrf_protect
def save(request):
    """
    Función para registrar los datos del formulario en la base de datos.
    """
    #print(request.POST)
    form = ClientForm(request.POST)
    if form.is_valid():
        try:
            # Alternativa 1
            code = form.cleaned_data.get('code')
            name = form.cleaned_data.get('name')
            percent_discount = int(form.cleaned_data.get('percent_discount'))
            pc = ProductCategory(code=code, name=name,percent_discount=percent_discount)
            pc.save()

            # Alternativa 2
            #form.save()

            return render(request, 'crm/product_category/new.html', {'form': form})
            # return HttpResponse("Categoría creada con éxito")
        except Exception as e:
            return HttpResponse(e)
    else:
        print(form.errors)
        return render(request, 'warehouse/product_category/new.html', {'form': form})

