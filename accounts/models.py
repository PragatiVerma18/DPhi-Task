from django.contrib.auth.models import AbstractUser
from django.db import models

ROLE_CHOICES = (("nursery", "Nursery"), ("buyer", "Buyer"))


class User(AbstractUser):
    username = models.CharField(
        max_length=256,
        unique=True,
        blank=False,
        default="",
        error_messages={
            "required": "Username must be provided.",
            "unique": "A user with that username already exists.",
        },
    )
    role = models.CharField(max_length=15,
                            choices=ROLE_CHOICES, error_messages={
                                "required": "Role must be provided"}
                            )
    verified = models.BooleanField(default=False)
    email = models.EmailField(
        unique=True,
        blank=False,
        error_messages={
            "unique": "A user with that email already exists.",
        },
    )
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.email
