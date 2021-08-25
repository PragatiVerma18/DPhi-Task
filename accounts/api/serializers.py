from rest_framework import serializers

from ..models import *
from rest_framework_simplejwt.tokens import RefreshToken


class UserSerializer(serializers.ModelSerializer):

    """
    Serializes user data - username, email, token
    """

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
        )

    def get_token(self, value):
        refresh = RefreshToken.for_user(value)
        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }


class UserAPISerializer(serializers.ModelSerializer):

    """
    Serializes User data - username, verified, email
    """

    class Meta:
        model = User
        fields = ["username", "verified", "email"]


class NurseryRegisterSerializer(serializers.ModelSerializer):

    """
    Serializes Nursery Registration data
    """

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
            "verified",
            "token",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def get_message(self, obj):
        return "Thank you for registering. You can now log in and start selling plants!"

    def get_role(self, obj):
        return "Nursery"

    def get_verified(self, obj):
        return False

    def get_token(self, value):
        refresh = RefreshToken.for_user(value)
        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }

    def validate(self, data):
        pw = data.get("password")
        pw2 = data.pop("password2")
        if pw != pw2:
            raise serializers.ValidationError("Passwords must match")
        return data

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

    """
    Serializes Buyer Registration data
    """

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
            "verified",
            "token",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def get_message(self, obj):
        return "Thank you for registering. You can now log in to your account and shop for your favourite plants!"

    def get_role(self, obj):
        return "Buyer"

    def get_verified(self, obj):
        return False

    def get_token(self, value):
        refresh = RefreshToken.for_user(value)
        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }

    def validate_email(self, value):
        qs = User.objects.filter(email__iexact=value)
        if qs.exists():
            raise serializers.ValidationError(
                "User with this email already exists")
        return value

    def validate_username(self, value):
        qs = User.objects.filter(username__iexact=value)
        if qs.exists():
            raise serializers.ValidationError(
                "User with this username already exists")
        return value

    def validate(self, data):
        pw = data.get("password")
        pw2 = data.pop("password2")
        if pw != pw2:
            raise serializers.ValidationError("Passwords must match")
        return data

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
