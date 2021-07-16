"""
nursery URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = [
    path("", include(router.urls)),
    path("admin/", admin.site.urls),
    path("accounts/api/", include("accounts.api.urls")),
    path("shop/api/", include("shop.api.urls")),
]
