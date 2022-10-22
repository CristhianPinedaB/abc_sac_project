from django.urls import path
from . import views

app_name = "crm"

urlpatterns = [
    #path("", views.index, name = "home_client"),
    path("registro-cliente/nuevo", views.new, name="register_client_new"),
    path("registro-cliente/guardar", views.save, name="register_client_save"),
    path("registro-cliente",views.register_client_list, name = "register_client_list"),
    # URL para categorías de producto
    # path("categorias-producto",views.product_category_list, name = "product_category_list"),
    # path("categorias-producto/<int:product_category_id>",views.detail, name = "product_category_detail"),

    # path("categorias-producto/buscar", views.search,name="product_category_search"),
    # path("categorias-producto/guardar", views.save, name="product_category_save")
]
