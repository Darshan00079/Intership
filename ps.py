import re
import hashlib
import random

# Deterministic password encrypter using hash + salt + formatting
def encrypt_password(password):
    # Create a deterministic hash
    hash_object = hashlib.sha256(password.encode())
    hex_dig = hash_object.hexdigest()

    # Use part of the hash to create a complex password
    symbols = "!@#$%^&*()_+-=[]{}|:;,.<>?"
    encrypted = []

    for i in range(12):  # Take first 12 characters
        char = hex_dig[i]
        if i % 4 == 0:
            encrypted.append(symbols[int(char, 16) % len(symbols)])
        elif i % 4 == 1:
            encrypted.append(char.upper())
        elif i % 4 == 2:
            encrypted.append(str(int(char, 16) % 10))
        else:
            encrypted.append(char.lower())

    return ''.join(encrypted)


def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 2
    elif len(password) >= 6:
        score += 1
    else:
        feedback.append("Password should be at least 6 characters long.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Password should contain at least one lowercase letter.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Password should contain at least one digit.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 2
    else:
        feedback.append("Password should contain at least one special character.")

    common_patterns = ["123", "password", "qwerty", "admin", "abc"]
    if any(p in password.lower() for p in common_patterns):
        score = 0
        feedback.append("Password contains easily guessable patterns.")

    if score >= 6:
        strength = "Excellent"
    elif score >= 4:
        strength = "Strong"
    elif score >= 3:
        strength = "Moderate"
    else:
        strength = "Poor"

    return {
        "strength": strength,
        "score": score,
        "feedback": feedback
    }


if __name__ == "__main__":
    password = input("Enter your password: ")

    # Analyze strength
    result = check_password_strength(password)

    # Show strength and suggestions
    print(f"\n🔐 Password Strength: {result['strength']} (Score: {result['score']}/7)")
    for fb in result['feedback']:
        print(" -", fb)

    # Generate and display encrypted version
    encrypted_version = encrypt_password(password)
    print("\n🔒 Suggested Encrypted Version of Your Password:")
    print(f"👉 {encrypted_version}")
