from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from applications.crm.models import Client
from applications.crm.api.serializers import ClientSerializer,ClientOrderSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    #max_page_size = 1000

class ClientViewSet(ModelViewSet):
    """
    Clase ViewSet de Product Category
    """

    queryset = Client.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['document_number', 'document_type']
    pagination_class = StandardResultsSetPagination
    serializer_class = ClientSerializer

    # Configuración para que el VIEW sea utilizado por usuarios autenticados.
    #permission_classes = [IsAuthenticated]
    
class ClientOrderApiView(APIView):
    """
    Clase ApiView de Order Details view
    """
    permission_classes = [AllowAny]
    serializer_class = ClientOrderSerializer

    def get(self, request, format=None, *args, **kwargs):
        id = self.kwargs['id']
        if id != None:
            try:
                queryset = Client.objects.get(id=id)
            except Client.DoesNotExist:
                return Response('Not exit Client ' + str(id), status=status.HTTP_404_NOT_FOUND)

            serializer = ClientOrderSerializer(queryset)
            return Response(serializer.data)
