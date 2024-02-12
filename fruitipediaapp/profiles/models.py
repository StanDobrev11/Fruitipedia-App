from django.conf import settings
from django.core.validators import MinLengthValidator
from django.db import models

from fruitipediaapp.profiles import validators


# Create your models here.
class Profile(models.Model):
    MAX_FIRST_NAME_LENGTH = 25
    MIN_FIRST_NAME_LENGTH = 2
    MAX_LAST_NAME_LENGTH = 30
    MIN_LAST_NAME_LENGTH = 1
    MAX_EMAIL_LENGTH = 40
    MAX_PASSWORD_LENGTH = 20
    MIN_PASSWORD_LENGTH = 8

    first_name = models.CharField(
        max_length=MAX_FIRST_NAME_LENGTH,
        validators=[
            MinLengthValidator(limit_value=MIN_FIRST_NAME_LENGTH),
            validators.first_letter_validator,
        ],
    )

    last_name = models.CharField(
        max_length=MAX_LAST_NAME_LENGTH,
        validators=[
            MinLengthValidator(limit_value=MIN_LAST_NAME_LENGTH),
            validators.first_letter_validator,
        ]
    )

    email = models.EmailField(
        unique=True,
        max_length=MAX_EMAIL_LENGTH,
    )

    password = models.CharField(
        max_length=MAX_PASSWORD_LENGTH,
        help_text="*Password length requirements: 8 to 20 characters",
        validators=[
            MinLengthValidator(limit_value=MIN_PASSWORD_LENGTH)
        ]
    )

    image_url = models.ImageField(blank=True, null=True)

    age = models.PositiveSmallIntegerField(default=18, blank=True, null=True)

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
