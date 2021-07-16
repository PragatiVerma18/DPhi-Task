from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import UserSerializer


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

    """
    Serializes Custom Token Pair for User
    """

    @classmethod
    def get_token(cls, user):
        token = super(CustomTokenObtainPairSerializer, cls).get_token(user)
        token["user"] = UserSerializer(user, many=False).data

        return token


class CustomTokenObtainPairView(TokenObtainPairView):

    """
    View to generate Custom Token Pair for User
    """

    serializer_class = CustomTokenObtainPairSerializer
