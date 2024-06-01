from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions
from .models import Item
from .serializers import ItemSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['sku', 'name', 'category', 'tags', 'in_stock', 'available_stock']
