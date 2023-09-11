from rest_framework.viewsets import ModelViewSet

from .models import Product
from .serialziers import ProductSerializer

class ProductView(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    http_method_names = ['get', ]