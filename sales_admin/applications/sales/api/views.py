
from rest_framework.views import APIView
from applications.sales.models import Order
from applications.sales.api.serializers import OrderSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status

class OrderApiView(APIView):
    """
    Clase ApiView de Order
    """
    permission_classes = [AllowAny]

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def post(self, request, format=None):
        print('request0---------------->',request.data)
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
