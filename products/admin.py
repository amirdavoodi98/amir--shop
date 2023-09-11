from django.contrib import admin

from .models import Product


@admin.register(Product)
class UserAdminProduct(admin.ModelAdmin):
    list_display = ('id', 'name', 'price')
    # list_filter = (
    #     ('project_name'),
    # )