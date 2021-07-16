from django.contrib import admin
from .models import User

admin.site.site_url = "/"


@admin.register(User)
class AccountsAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "role", "verified")
    list_editable = ("verified",)
    search_fields = ("username", "email")
    list_filter = (
        "role",
        "verified",
    )
