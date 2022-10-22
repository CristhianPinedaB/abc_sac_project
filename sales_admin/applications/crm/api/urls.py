from rest_framework import routers
from django.urls import path
from django.conf.urls import include
from applications.crm.api.views import ClientViewSet, ClientOrderApiView
router = routers.DefaultRouter()
router.register('client', ClientViewSet)
# router.register('products', ProductViewSet)

urlpatterns = [
    path("client-order/<int:id>/", ClientOrderApiView.as_view(), name='client-order'),
]
urlpatterns += router.urls
