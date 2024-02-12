from django.core.exceptions import ValidationError


def all_letters_validator(value: str):
    for ch in value:
        if not ch.isalpha():
            raise ValidationError("Fruit name should contain only letters!")
