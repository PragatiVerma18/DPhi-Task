from django.contrib import admin
from .models import Product, Category, CartItem


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = ("name", "price", "quantity",
                    "is_available", "created", "discount")

    search_fields = (
        "name",
        "category",
    )
    date_hierarchy = "created"
    list_editable = ["price", "is_available", "quantity", "discount"]
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "slug",
    )
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(CartItem)
