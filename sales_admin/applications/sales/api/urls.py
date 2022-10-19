from rest_framework import routers
from django.urls import path
from django.conf.urls import include
from applications.sales.api.views import OrderApiView

router = routers.DefaultRouter()
#router.register('orders', OrderViewSet)
# router.register('products', ProductViewSet)

urlpatterns = [
    path("record-order/", OrderApiView.as_view(), name='record-order'),
   

]
urlpatterns += router.urls
