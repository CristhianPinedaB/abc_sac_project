from rest_framework import serializers
from applications.sales.models import Order, OrderItem
from applications.crm.models import Client
from decimal import Decimal


class OrderItemSerializer(serializers.ModelSerializer):
    """
    Clase para convertir un objeto Oder a un formato JSON.
    """
    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'quantity', 'price',
                  'sales_price', 'discount_price', 'total_price']


class OrderItemAllSerializer(serializers.ModelSerializer):
    """
    Clase para convertir un objeto Oder a un formato JSON.
    """
    class Meta:
        model = OrderItem
        fields = '__all__'

# class OrderSerializer(serializers.ModelSerializer):
#     """
#     Clase para convertir un objeto Oder a un formato JSON.
#     """
#     class Meta:
#         model = Order
#         fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    """
    Clase para convertir un objeto Oder a un formato JSON.
    """
    items = OrderItemAllSerializer(many=True)

    class Meta:
        model = Order
        fields = ['number_id', 'number_order', 'created_at', 'client', 'delivered_at',
                  'subtotal_amount', 'igv', 'total_amount', 'total_discount_amount', 'items']

    def create(self, validated_data):

        items_id = []
        subtotal_amount = Decimal('0')
        total_discount_amount = Decimal('0')

        #Create Item
        items_data = validated_data.pop('items')
        for item_data in items_data:
            item = OrderItem.objects.create(**item_data) 
            items_id.append(item)
            subtotal_amount += item.total_price
            total_discount_amount += item.discount_price
            
        # Create Order
        order = Order.objects.create(subtotal_amount=subtotal_amount,
                                     total_discount_amount=total_discount_amount,
                                      **validated_data)
        order.items.set(items_id)

        return order


class OrderGetSerializer(serializers.ModelSerializer):
    """
    Clase para convertir un objeto Oder a un formato JSON.
    """
    # https://www.django-rest-framework.org/api-guide/relations/#writable-nested-serializers
    # https://stackoverflow.com/questions/33182092/django-rest-framework-serializing-many-to-many-field
    # items = OrderItemSerializer(many=True)
    client_name = serializers.CharField(source='client.name_client')

    class Meta:
        model = Order
        fields = ['number_id', 'number_order', 'created_at', 'client_name', 'delivered_at',
                  'subtotal_amount', 'igv', 'total_amount', 'total_discount_amount']


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class OrderDetailSerializer(serializers.ModelSerializer):
    """
    Clase para convertir un objeto Oder a un formato JSON.
    """
    Client = ClientSerializer(source='client')
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['number_id', 'number_order', 'created_at', 'Client', 'delivered_at',
                  'subtotal_amount', 'igv', 'total_amount', 'total_discount_amount', 'items']


class OrderGainSerializer(serializers.ModelSerializer):
    """
    Clase para convertir un objeto Oder a un formato JSON.
    """

    class Meta:
        model = Order
        fields = ['number_order', 'subtotal_amount',
                  'igv', 'total_amount', 'total_discount_amount']
