from .serializers import UserSerializer
from ..models import User
from .serializers import NurseryRegisterSerializer, BuyerRegisterSerializer
from rest_framework import viewsets
from rest_framework import generics, permissions
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_200_OK
from django.core.exceptions import ValidationError


def get_user_from_token(request):
    """
    Function that returns the user from access token.
    """

    token = request.META.get("HTTP_AUTHORIZATION", " ").split(" ")[1]
    try:
        valid_data = TokenBackend(
            algorithm="HS256").decode(token, verify=False)
        user = valid_data["user"]
        request.user = user
    except ValidationError as v:
        print("validation error", v)


class NurseryRegisterAPIView(generics.CreateAPIView):

    """
    A view that handles Nursery Registration.
    """

    queryset = User.objects.all()
    serializer_class = NurseryRegisterSerializer

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}


class BuyerRegisterAPIView(generics.CreateAPIView):

    """
    A view that handles Buyer Registration.
    """

    queryset = User.objects.all()
    serializer_class = BuyerRegisterSerializer

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}


class BuyerList(generics.ListAPIView):

    """
    A view that returns buyer list.
    """

    model = User
    serializer_class = UserSerializer

    def get_queryset(self):
        user = self.request.user
        return User.objects.filter(role="Buyer")


class NurseryList(generics.ListAPIView):

    """
    A view that returns nursery list.
    """

    model = User
    serializer_class = UserSerializer

    def get_queryset(self):
        user = self.request.user
        return User.objects.filter(role="Nursery")


class UserDetail(generics.RetrieveAPIView):

    """
    A view that returns user details from username.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def retrieve(self, request, username):
        queryset = User.objects.filter(username=username)
        user = get_object_or_404(queryset, username=username)
        serializer = UserSerializer(user)
        return Response(serializer.data)


@api_view(["POST"])
def login(request):
    """
    A view that handles login for buyers and nurseries.
    """

    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response(
            {"error": "Please provide both username and password"},
            status=HTTP_400_BAD_REQUEST,
        )
    user = authenticate(username=username, password=password)
    if not user:
        return Response({"error": "Invalid Credentials"}, status=HTTP_404_NOT_FOUND)
    serializer = UserSerializer(user)
    data = serializer.data
    return Response(data, status=HTTP_200_OK)
