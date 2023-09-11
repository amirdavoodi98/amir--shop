from rest_framework import serializers
from rest_framework_simplejwt.tokens import AccessToken

from custom.get_user import get_user_by_token
from .models import Order, User, Cart
from products.serialziers import ProductSerializer


class OrderSerialzier(serializers.ModelSerializer):
    total_price = serializers.FloatField(read_only=True)
    class Meta:
        model = Order
        fields = ('id', 'product', 'weight', 'total_price','created_at')


class CartCreateSerializer(serializers.ModelSerializer):
    orders = OrderSerialzier(many=True)
    class Meta:
        model = Cart
        fields = ('id', 'status', 'cart_total_price', 'created_at', 'orders')
        read_only_fields = ('id', 'status', 'cart_total_price', 'created_at')

    def create(self, validated_data):
        user_token = str(self.context['request'].headers.get('Authorization')).split(' ')[1]
        user = get_user_by_token(user_token)
        validated_data['user'] = user
        orders = validated_data.pop('orders')
        cart = Cart.objects.create(**validated_data)
        for order in orders:
            print("bbbbbbbbbb", order)
            Order.objects.create(cart=cart, **order)
            print("ccccccccccccc", order)
        return cart


