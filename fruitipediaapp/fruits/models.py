from django.core.validators import MinLengthValidator
from django.db import models

from fruitipediaapp.fruits import validators
from fruitipediaapp.profiles.models import Profile


# Create your models here.
class Fruit(models.Model):
    MAX_NAME_LENGTH = 30
    MIN_NAME_LENGTH = 2

    name = models.CharField(
        unique=True,
        max_length=MAX_NAME_LENGTH,
        validators=[
            MinLengthValidator(limit_value=MIN_NAME_LENGTH),
            validators.all_letters_validator,
        ],
        error_messages={
            'unique': 'This fruit name is already in use! Try a new one.'
        },
    )

    image_url = models.URLField()

    description = models.TextField()

    nutrition = models.TextField()

    owner = models.ForeignKey(
        to=Profile,
        on_delete=models.CASCADE
    )
