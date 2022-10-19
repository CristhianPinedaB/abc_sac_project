from rest_framework.serializers import ModelSerializer
from applications.sales.models import Order

class OrderSerializer(ModelSerializer):
    """
    Clase para convertir un objeto ProductCategory a un formato JSON.
    """
    class Meta:
        model = Order
        fields = '__all__'