from datetime import date
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.contrib.admin import SimpleListFilter, DateFieldListFilter
from django.db.models import Q
from rangefilter.filters import (
    DateRangeFilterBuilder,
    DateTimeRangeFilterBuilder,
    NumericRangeFilterBuilder,
    DateRangeQuickSelectListFilterBuilder,
)

from .models import Order, Cart


@admin.register(Cart)
class UserAdminCart(admin.ModelAdmin):
    list_display = ('id', 'user', 'status', 'updated_at', 'cart_total_price')
    list_filter = (("created_at", DateRangeFilterBuilder()), "status")


@admin.register(Order)
class UserAdminOrder(admin.ModelAdmin):
    list_display = ('id', 'product', 'cart', 'weight', 'total_price', 'created_at')
    list_filter = (("created_at", DateRangeFilterBuilder()), 'product')
