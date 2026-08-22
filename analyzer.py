import math
import re
import string


COMMON_PASSWORDS = {
    "123456",
    "123456789",
    "12345678",
    "1234567890",
    "password",
    "password1",
    "password123",
    "admin",
    "admin123",
    "qwerty",
    "qwerty123",
    "abc123",
    "letmein",
    "welcome",
    "welcome123",
    "iloveyou",
    "monkey",
    "dragon",
    "football",
    "login",
    "pass",
    "secret",
    "user",
    "test",
    "india123",
    "india@123",
}


def calculate_entropy(password):
    """
    Estimate password entropy based on character pool.
    This is an educational estimate, not a full password-cracking model.
    """

    if not password:
        return 0.0

    pool_size = 0

    if re.search(r"[a-z]", password):
        pool_size += 26

    if re.search(r"[A-Z]", password):
        pool_size += 26

    if re.search(r"[0-9]", password):
        pool_size += 10

    if re.search(r"[^a-zA-Z0-9]", password):
        pool_size += 32

    if pool_size == 0:
        return 0.0

    entropy = len(password) * math.log2(pool_size)

    return round(entropy, 2)


def has_repeated_characters(password):
    """
    Detect characters repeated 3 or more times consecutively.
    Example: aaa, 111, !!!
    """

    return bool(re.search(r"(.)\1\1", password))


def has_sequential_pattern(password):
    """
    Detect simple ascending/descending sequences.
    Examples:
    abc
    123
    321
    xyz
    """

    if len(password) < 3:
        return False

    password_lower = password.lower()

    sequences = [
        "abcdefghijklmnopqrstuvwxyz",
        "0123456789",
        "qwertyuiop",
        "asdfghjkl",
        "zxcvbnm",
    ]

    for sequence in sequences:
        for i in range(len(sequence) - 2):
            part = sequence[i:i + 3]

            if part in password_lower:
                return True

            if part[::-1] in password_lower:
                return True

    return False


def analyze_password(password):
    """
    Analyze password and return a result dictionary.
    """

    result = {
        "score": 0,
        "strength": "Very Weak",
        "length": len(password),
        "entropy": 0.0,
        "checks": [],
        "suggestions": [],
        "is_common": False,
        "is_repeated": False,
        "is_sequential": False,
    }

    if not password:
        result["suggestions"].append("Enter a password to analyze.")
        return result

    score = 0

    # ------------------------------------------------
    # Length
    # ------------------------------------------------

    length = len(password)

    if length >= 16:
        score += 30
        result["checks"].append(("Password length", True, "Excellent length"))
    elif length >= 12:
        score += 25
        result["checks"].append(("Password length", True, "Good length"))
    elif length >= 8:
        score += 15
        result["checks"].append(("Password length", True, "Acceptable length"))
    else:
        score += 5
        result["checks"].append(("Password length", False, "Use at least 12 characters"))

    # ------------------------------------------------
    # Lowercase
    # ------------------------------------------------

    if re.search(r"[a-z]", password):
        score += 10
        result["checks"].append(("Lowercase letters", True, "Present"))
    else:
        result["checks"].append(("Lowercase letters", False, "Add lowercase letters"))
        result["suggestions"].append(
            "Add lowercase letters such as a, b, c..."
        )

    # ------------------------------------------------
    # Uppercase
    # ------------------------------------------------

    if re.search(r"[A-Z]", password):
        score += 10
        result["checks"].append(("Uppercase letters", True, "Present"))
    else:
        result["checks"].append(("Uppercase letters", False, "Add uppercase letters"))
        result["suggestions"].append(
            "Add uppercase letters such as A, B, C..."
        )

    # ------------------------------------------------
    # Numbers
    # ------------------------------------------------

    if re.search(r"[0-9]", password):
        score += 10
        result["checks"].append(("Numbers", True, "Present"))
    else:
        result["checks"].append(("Numbers", False, "Add numbers"))
        result["suggestions"].append(
            "Add numbers such as 7, 24, 89..."
        )

    # ------------------------------------------------
    # Special characters
    # ------------------------------------------------

    if re.search(r"[^a-zA-Z0-9]", password):
        score += 15
        result["checks"].append(("Special characters", True, "Present"))
    else:
        result["checks"].append(
            ("Special characters", False, "Add special characters")
        )
        result["suggestions"].append(
            "Add special characters such as @, #, $, %, !"
        )

    # ------------------------------------------------
    # Common password
    # ------------------------------------------------

    if password.lower() in COMMON_PASSWORDS:
        result["is_common"] = True
        score -= 40

        result["checks"].append(
            ("Common password", False, "Password appears in common-password list")
        )

        result["suggestions"].append(
            "Avoid commonly used passwords."
        )
    else:
        result["checks"].append(
            ("Common password", True, "Not detected in basic common list")
        )

    # ------------------------------------------------
    # Repeated characters
    # ------------------------------------------------

    if has_repeated_characters(password):
        result["is_repeated"] = True
        score -= 10

        result["checks"].append(
            ("Repeated characters", False, "Repeated characters detected")
        )

        result["suggestions"].append(
            "Avoid repeated patterns such as aaa, 111 or !!!."
        )
    else:
        result["checks"].append(
            ("Repeated characters", True, "No obvious repetition")
        )

    # ------------------------------------------------
    # Sequential patterns
    # ------------------------------------------------

    if has_sequential_pattern(password):
        result["is_sequential"] = True
        score -= 10

        result["checks"].append(
            ("Sequential pattern", False, "Simple sequence detected")
        )

        result["suggestions"].append(
            "Avoid sequences such as 123, abc or qwerty."
        )
    else:
        result["checks"].append(
            ("Sequential pattern", True, "No simple sequence detected")
        )

    # ------------------------------------------------
    # Character diversity
    # ------------------------------------------------

    unique_characters = len(set(password))

    if length > 0:
        uniqueness_ratio = unique_characters / length
    else:
        uniqueness_ratio = 0

    if uniqueness_ratio >= 0.75:
        score += 5
        result["checks"].append(
            ("Character uniqueness", True, "Good character diversity")
        )
    elif uniqueness_ratio >= 0.5:
        result["checks"].append(
            ("Character uniqueness", True, "Moderate character diversity")
        )
    else:
        score -= 5
        result["checks"].append(
            ("Character uniqueness", False, "Many repeated characters")
        )

        result["suggestions"].append(
            "Use more unique characters."
        )

    # ------------------------------------------------
    # Entropy
    # ------------------------------------------------

    entropy = calculate_entropy(password)
    result["entropy"] = entropy

    if entropy >= 80:
        score += 10
    elif entropy >= 60:
        score += 7
    elif entropy >= 40:
        score += 4

    # ------------------------------------------------
    # Clamp score
    # ------------------------------------------------

    score = max(0, min(100, score))

    result["score"] = score

    # ------------------------------------------------
    # Strength
    # ------------------------------------------------

    if score < 25:
        strength = "Very Weak"
    elif score < 45:
        strength = "Weak"
    elif score < 65:
        strength = "Medium"
    elif score < 85:
        strength = "Strong"
    else:
        strength = "Very Strong"

    result["strength"] = strength

    # ------------------------------------------------
    # General suggestions
    # ------------------------------------------------

    if length < 12:
        result["suggestions"].append(
            "Use a password of at least 12 characters."
        )

    if entropy < 60:
        result["suggestions"].append(
            "Increase password length and character variety."
        )

    if not result["suggestions"] and score >= 85:
        result["suggestions"].append(
            "Excellent password. Avoid reusing it on other websites."
        )

    # Remove duplicate suggestions
    result["suggestions"] = list(dict.fromkeys(result["suggestions"]))

    return result