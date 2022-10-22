
from unittest import result
from rest_framework.views import APIView
from applications.sales.models import Order, OrderItem
from applications.sales.api.serializers import (
    OrderSerializer, OrderGetSerializer, OrderDetailSerializer, OrderGainSerializer)
from applications.sales.api.serializers import OrderItemSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from decimal import Decimal
from django.db.models import Sum
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.settings import api_settings
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination


class OrderApiView(APIView, PageNumberPagination):
    """
    Clase ApiView de Order
    """
    permission_classes = [AllowAny]

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['number_order', 'created_at', 'delivered_at']

    def get(self, request, format=None):

        number_order = request.GET.get('number_order')
        totalAmountHigherThan = request.GET.get('totalAmountHigherThan')
        if number_order != None:
            try:
                queryset = Order.objects.get(number_order=number_order)
            except Order.DoesNotExist:
                return Response('Not exit Order ' + str(number_order), status=status.HTTP_404_NOT_FOUND)
            serializer = OrderGetSerializer(queryset)
            return Response(serializer.data)

        elif totalAmountHigherThan != None:
            queryset = Order.objects.filter(
                total_amount__gte=totalAmountHigherThan)
                
            res = self.paginate_queryset(queryset, request, view=self)
            serializer = OrderGetSerializer(res, many=True)
            return Response(serializer.data)

        else:
            orders = Order.objects.all()
            result = self.paginate_queryset(orders, request, view=self)
            serializer = OrderGetSerializer(result, many=True)
            return self.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderApiDetailView(APIView):
    """
    Clase ApiView de Order Details view
    """
    permission_classes = [AllowAny]
    serializer_class = OrderDetailSerializer

    def get(self, request, format=None, *args, **kwargs):
        id = self.kwargs['id']
        if id != None:
            try:
                queryset = Order.objects.get(number_id=id)
            except Order.DoesNotExist:
                return Response('Not exit Order ' + str(id), status=status.HTTP_404_NOT_FOUND)

            serializer = OrderDetailSerializer(queryset)
            return Response(serializer.data)


class OrderApiGainView(APIView):
    """
    Clase ApiView de Order Details view
    """
    permission_classes = [AllowAny]
    serializer_class = OrderGainSerializer

    def get(self, request, format=None, *args, **kwargs):
        id = self.kwargs['id']
        if id != None:
            try:
                queryset = Order.objects.get(number_id=id)
            except Order.DoesNotExist:
                return Response('Not exit Order ' + str(id), status=status.HTTP_404_NOT_FOUND)

            serializer = OrderGainSerializer(queryset)
            return Response(serializer.data)


class OrderItemApiView(APIView):
    """
    Clase ApiView de Order Item API
    """
    permission_classes = [AllowAny]

    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

    def get(self, request, format=None):
        items = OrderItem.objects.all()
        serializer = OrderItemSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = OrderItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
