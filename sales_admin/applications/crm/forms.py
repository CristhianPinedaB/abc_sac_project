from random import choices
from django import forms
from .models import Client

class ClientForm(forms.ModelForm):
    """
    Formulario para el Modelo Client.

    Creamos formulario con tres inputs.
    """

    # document_type = forms.CharField(
    #     #label = "Código Cat",
    #     #unique = Client._meta.get_field('document_type').unique,
    #     label=Client._meta.get_field('document_type').verbose_name,
    #     max_length= Client._meta.get_field('document_type').max_length,
    #     help_text=('Elija el tipo de documento'),
    #     widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'document_type', 'placeholder': 'Tipo de documento'}))

    # document_number = forms.CharField(
    #     label=Client._meta.get_field('document_number').verbose_name,
    #     max_length=Client._meta.get_field('document_number').max_length,
    #     widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'document_number'}))
    
    # name_client = forms.CharField(
    #     label=Client._meta.get_field('name_client').verbose_name,
    #     max_length=Client._meta.get_field('name_client').max_length,
    #     widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'name_client'}))
    
    # type_client = forms.CharField(
    #     label=Client._meta.get_field('type_client').verbose_name,
    #     #choices = Client._meta.get_field('type_client').choices,
    #     max_length=Client._meta.get_field('type_client').max_length,
    #     widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'type_client'}))
    
    # address = forms.CharField(
    #     label=Client._meta.get_field('address').verbose_name,
    #     max_length=Client._meta.get_field('address').max_length,
    #     widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'address'}))

    # phone_number = forms.CharField(
    #     #blank = Client._meta.get_field('phone_number').blank,
    #     label=Client._meta.get_field('phone_number').verbose_name,
    #     max_length=Client._meta.get_field('phone_number').max_length,
    #     widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'phone_number'}))

    class Meta:
        model = Client
        fields = "__all__"