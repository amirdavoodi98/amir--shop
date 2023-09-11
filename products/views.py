from rest_framework.viewsets import ModelViewSet

from .models import Product
from .serialziers import ProductSerializer

class ProductView(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    http_method_names = ['get', ]

    def get_queryset(self):
        """
        SELECT "products_product"."id", "products_product"."name", "products_product"."price", "products_product"."image" FROM "products_product"
        """
        return super().get_queryset()

    def create(self, request, *args, **kwargs):
        """
        INSERT INTO product (name, price, image) VALUES ('Product Name', 1000, 'products/image.jpg');
        """
        return super().create(request, *args, **kwargs)