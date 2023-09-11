from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.tokens import AccessToken

from .models import User
from .serializers import UserSignUpSerialzier


class UserSignUpView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSignUpSerialzier
    http_method_names = ['post', 'get']

    def get_object(self):

        queryset = self.filter_queryset(self.get_queryset())
        # make sure to catch 404's below
        user_token = str(self.request.headers.get('Authorization')).split(' ')[1]
        access_token = AccessToken(user_token)
        userID = access_token['user_id']
        obj = queryset.get(pk=userID)
        self.check_object_permissions(self.request, obj)
        return obj