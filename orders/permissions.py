from rest_framework.permissions import BasePermission
from rest_framework_simplejwt.tokens import AccessToken

from users.models import User

class IsOrderOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        user_token = str(request.headers.get('Authorization')).split(' ')[1]
        access_token = AccessToken(user_token)
        userID = access_token['user_id']
        user = User.objects.get(id=userID)
        return obj.is_order_owner(user)