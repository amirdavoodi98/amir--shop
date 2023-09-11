from django.db import models
from custom.enum import Enum

from users.models import User
from products.models import Product


class OrderStatus(Enum):
    OPEN = 'پراخت نشده'
    CANCELED = 'لغو ده'
    DONE = 'تکمیل شده'

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='carts', verbose_name='کاربر')
    status = models.CharField(max_length=128, choices=OrderStatus.choices(), default=OrderStatus.DONE.value, verbose_name='وضعیت')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='تاریخ آخرین تغییر')

    def __str__(self) -> str:
        return f"{self.user.first_name}_{self.status}"

    def is_order_owner(self, user):
        if self.user == user:
            return True
        return False
    
    @property
    def cart_total_price(self):
        orders = self.orders.all()
        sum = 0
        for order in orders:
            sum += order.total_price
        return sum
    cart_total_price.fget.short_description = 'قیمت کل سبد خرید'
    
    class Meta:
        verbose_name = 'سبد خرید'
    
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='orders', verbose_name='محصول')
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='orders', verbose_name='سبد خرید')
    weight = models.FloatField(default=1, verbose_name='وزن')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')

    @property
    def total_price(self):
        return self.weight * self.product.price
    total_price.fget.short_description = 'قیمت کل  سفارش'
    
    class Meta:
        verbose_name = 'سفارش'
