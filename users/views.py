from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.tokens import AccessToken

from .models import User
from .serializers import UserSignUpSerialzier


class UserSignUpView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSignUpSerialzier
    http_method_names = ['post', 'get']

    def get_object(self):
        """
        SELECT "users_user"."id", "users_user"."last_login", "users_user"."is_superuser", "users_user"."is_staff", "users_user"."is_active", "users_user"."date_joined", "users_user"."email", "users_user"."username", "users_user"."first_name", "users_user"."last_name" FROM "users_user" WHERE "users_user"."id" = 1
        """
        queryset = self.filter_queryset(self.get_queryset())
        # make sure to catch 404's below
        user_token = str(self.request.headers.get('Authorization')).split(' ')[1]
        access_token = AccessToken(user_token)
        userID = access_token['user_id']
        obj = queryset.get(pk=userID)
        self.check_object_permissions(self.request, obj)
        return obj
    
    def create(self, request, *args, **kwargs):
        """
        INSERT INTO auth_user (email, username, first_name, last_name) VALUES ('user@example.com', 'username', 'First', 'Last');
        """
        return super().create(request, *args, **kwargs)