def all_letters_validator(value: str):
    for ch in value:
        if not ch.isalpha():
            raise ValueError("Fruit name should contain only letters!")
