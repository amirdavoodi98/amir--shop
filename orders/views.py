from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny

from custom.get_user import get_user_by_token
from .models import Cart
from .serializers import CartCreateSerializer

class CartView(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Cart.objects.all()
    serializer_class = CartCreateSerializer
    http_method_names = ['post', 'get']

    def get_queryset(self):
        user_token = str(self.request.headers.get('Authorization')).split(' ')[1]
        user = get_user_by_token(user_token=user_token)
        return self.queryset.filter(user=user)

    def create(self, request, *args, **kwargs):
        """
        INSERT INTO cart (status, cart_total_price, created_at) VALUES ('reques.status', request.total_price1000);
        """
        return super().create(request, *args, **kwargs)
    
    # def get_serializer_class(self):
    #     if self.action == 'create':
    #         return CartCreateSerializer
        # elif self.action == 'retrieve' or self.action == 'list':
        #     return OrderRetrieveSerializer
    
    # def get_permissions(self):
    #     if self.action == 'create':
    #         return (IsAuthenticated(),)
    #     else:
    #         return (IsAuthenticated(), IsOrderOwner())

