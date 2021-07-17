from django.db import models
from django.conf import settings
from django.db.models.signals import post_delete
from django.dispatch.dispatcher import receiver
from datetime import datetime


User = settings.AUTH_USER_MODEL


def get_superuser():
    user = User.objects.filter(is_superuser=True).first()
    return user


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)

    class Meta:
        ordering = ("name",)
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class AvailableManager(models.Manager):
    def get_queryset(self):
        return (
            super(AvailableManager, self)
            .get_queryset()
            .filter(is_available=True, quantity__gte=1)
        )


class Product(models.Model):
    name = models.CharField(max_length=150, unique=True, null=False, blank=False)
    slug = models.SlugField(unique=True, null=False, blank=False)
    category = models.ManyToManyField(Category, related_name="products")
    price = models.PositiveIntegerField()
    discount = models.PositiveIntegerField(default=0)
    is_available = models.BooleanField(default=True)
    quantity = models.PositiveIntegerField()
    objects = models.Manager()
    available = AvailableManager()
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.SET(get_superuser))
    image = models.URLField()
    description = models.TextField()

    def __str__(self):
        return self.name


class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.product.name
