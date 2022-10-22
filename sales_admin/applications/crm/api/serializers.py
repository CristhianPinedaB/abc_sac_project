from rest_framework import serializers
from applications.crm.models import Client
from applications.sales.api.serializers import OrderSerializer


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class ClientOrderSerializer(serializers.ModelSerializer):
    orders = OrderSerializer(many=True)
    class Meta:
        model = Client
        fields = ['id', 'document_type', 'document_number',
                  'name_client', 'type_client', 'address', 'phone_number','orders']
