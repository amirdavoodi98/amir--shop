from django.urls import path

from .views import CartView
# from .views import CartView, AddProductToOrderView, RemoveProductFromOrderView, StatusOrderView

urlpatterns = [
    path('cart/',CartView.as_view({
        'post': 'create',
        'get': 'list'
    })),
    # path('order/<int:pk>',OrderView.as_view({
    #     'get': 'retrieve',
    # })),
    # path('add-to-order/<int:pk>', AddProductToOrderView.as_view({
    #     'patch': 'partial_update',
    # })),
    # path('remove-from-order/<int:pk>', RemoveProductFromOrderView.as_view({
    #     'patch': 'partial_update',
    # })),
    # path('status-order/<int:pk>', StatusOrderView.as_view({
    #     'patch': 'partial_update',
    # })),
]