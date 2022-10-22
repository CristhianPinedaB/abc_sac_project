from rest_framework import routers
from django.urls import path
from django.conf.urls import include
from applications.sales.api.views import OrderApiView,OrderApiDetailView,OrderApiGainView
from applications.sales.api.views import OrderItemApiView

router = routers.DefaultRouter()
#router.register('orders', OrderViewSet)
# router.register('products', ProductViewSet)

urlpatterns = [
    path("record-order/", OrderApiView.as_view(), name='record-order'),
    path("record-order/<int:id>/", OrderApiDetailView.as_view(), name='record-order-detail'),
    path("record-order/gain/<int:id>/", OrderApiGainView.as_view(), name='record-order-gain-detail'),
    path("record-order-item/", OrderItemApiView.as_view(), name='record-order-item'),
]
urlpatterns += router.urls
