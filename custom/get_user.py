from rest_framework_simplejwt.tokens import AccessToken
from users.models import User

def get_user_by_token(user_token):
    access_token = AccessToken(user_token)
    userID = access_token['user_id']
    user = User.objects.get(id=userID)
    return user