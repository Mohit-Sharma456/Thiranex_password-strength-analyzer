import secrets
import string


def generate_strong_password(length=18):
    """
    Generate a cryptographically stronger random password.
    """

    if length < 12:
        length = 12

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special = "!@#$%^&*()-_=+"

    # Guarantee at least one character from each category
    password_chars = [
        secrets.choice(lowercase),
        secrets.choice(uppercase),
        secrets.choice(digits),
        secrets.choice(special),
    ]

    all_characters = lowercase + uppercase + digits + special

    for _ in range(length - 4):
        password_chars.append(secrets.choice(all_characters))

    # Secure shuffle
    secrets.SystemRandom().shuffle(password_chars)

    return "".join(password_chars)