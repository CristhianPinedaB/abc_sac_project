from itertools import product
from random import choices
from django import forms
from .models import Order, OrderItem

class OrderForm(forms.ModelForm):
    """
    Formulario para el Modelo Client.

    Creamos formulario con tres inputs.
    """
    # STATUS = (
    #     ('enviado', 'enviado'),
    #     ('entregado', 'entregado'),
    #     ('pagado', 'pagado'),
    # )

    
    class Meta:
        model = Order
        fields = "__all__"

class OrderItemForm(forms.ModelForm):
        """
        Formulario para Item of Order.
        """
        class Meta:
            model = OrderItem
            fields = ['product','quantity']