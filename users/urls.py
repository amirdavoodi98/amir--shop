from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import UserSignUpView

urlpatterns = [
    path('sign-up',UserSignUpView.as_view({
        'post': 'create'
    })),
    path('user-info/',UserSignUpView.as_view({
        'get': 'retrieve'
    })),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]