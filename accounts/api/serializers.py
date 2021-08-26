from rest_framework import serializers

from ..models import *
from rest_framework_simplejwt.tokens import RefreshToken


class UserSerializer(serializers.ModelSerializer):

    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        exclude = (
            "first_name",
            "last_name",
            "password",
            "user_permissions",
            "groups",
            "is_staff",
            "is_active",
            "is_superuser",
            "last_login",
            "date_joined",
        )

    def get_token(self, value):
        refresh = RefreshToken.for_user(value)
        return {
            "access": str(refresh.access_token),
        }


class NurseryRegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        style={"input_type": "password"}, write_only=True)
    password2 = serializers.CharField(
        style={"input_type": "password"}, write_only=True)
    message = serializers.SerializerMethodField(read_only=True)
    role = serializers.SerializerMethodField(read_only=True)
    token = serializers.SerializerMethodField(read_only=True)
    verified = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password",
            "password2",
            "message",
            "role",
            "token",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def get_message(self, obj):
        return "Thank you for registering. You can now log in and start selling plants!"

    def get_verified(self, obj):
        return False

    def get_role(self, obj):
        return "Nursery"

    def get_token(self, value):
        refresh = RefreshToken.for_user(value)
        return {
            "access": str(refresh.access_token),
        }

    def create(self, validated_data):
        user_obj = User.objects.create(
            username=validated_data.get("username"),
            email=validated_data.get("email"),
            role="Nursery",
            verified=False,
        )
        user_obj.set_password(validated_data.get("password"))
        user_obj.is_active = True
        user_obj.save()
        return user_obj


class BuyerRegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        style={"input_type": "password"}, write_only=True)
    password2 = serializers.CharField(
        style={"input_type": "password"}, write_only=True)
    message = serializers.SerializerMethodField(read_only=True)
    role = serializers.SerializerMethodField(read_only=True)
    token = serializers.SerializerMethodField(read_only=True)
    verified = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password",
            "password2",
            "message",
            "role",
            "token",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def get_message(self, obj):
        return "Thank you for registering. You can now log in to your account and shop for your favourite plants!"

    def get_verified(self, obj):
        return False

    def get_role(self, obj):
        return "Buyer"

    def get_token(self, value):
        refresh = RefreshToken.for_user(value)
        return {
            "access": str(refresh.access_token),
        }

    def create(self, validated_data):
        user_obj = User.objects.create(
            username=validated_data.get("username"),
            email=validated_data.get("email"),
            role="Buyer",
            verified=False,
        )
        user_obj.set_password(validated_data.get("password"))
        user_obj.is_active = True
        user_obj.save()
        return user_obj
