def first_letter_validator(value: str):
    if not value[0].isalpha():
        raise ValueError("Your name must start with a letter!")