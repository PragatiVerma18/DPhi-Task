from rest_framework import serializers
from ..models import Product, Category, CartItem
from django.conf import settings
from django.shortcuts import get_object_or_404

User = settings.AUTH_USER_MODEL


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"


class ProductSerializer(serializers.HyperlinkedModelSerializer):

    category = CategorySerializer(many=True)

    class Meta:
        model = Product
        fields = (
            "id",
            "url",
            "name",
            "slug",
            "category",
            "price",
            "discount",
            "available",
            "quantity",
            "created",
            "image",
            "description",
        )

    def create(self, validated_data):
        category = validated_data.pop("category")
        user = self.context["request"].user
        product = Product.objects.create(user=user, **validated_data)
        for i in category:
            Category.objects.create(**i)
        return product

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.slug = validated_data.get("slug", instance.slug)
        instance.price = validated_data.get("price", instance.price)
        instance.discount = validated_data.get("discount", instance.discount)
        instance.quantity = validated_data.get("quantity", instance.quantity)
        instance.image = validated_data.get("image", instance.image)
        instance.description = validated_data.get(
            "description", instance.description)
        instance.save()
        return instance


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "is_staff",
            "is_active",
            "is_superuser",
        )


class CartItemSerializer(serializers.ModelSerializer):

    product = ProductSerializer()

    class Meta:
        model = CartItem
        fields = ("id", "quantity", "product")


class CartItemAddSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField()

    class Meta:
        model = CartItem
        fields = ("quantity", "product_id")
        extra_kwargs = {
            "quantity": {"required": True},
            "product_id": {"required": True},
        }

    def create(self, validated_data):
        user = self.context["request"].user
        product = get_object_or_404(Product, id=validated_data["product_id"])
        if product.quantity == 0 or product.is_available is False:
            raise serializers.ValidationsError(
                {"not available": "the product is not available."}
            )

        cart_item = CartItem.objects.create(
            product=product, user=user, quantity=validated_data["quantity"]
        )
        cart_item.save()
        product.quantity = product.quantity - cart_item.quantity
        product.save()
        return cart_item
