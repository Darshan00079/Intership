import re


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

    common_passwords = ["password", "123456","12345678","Pass@1234",""]
    if password.lower() in common_passwords:
        score = 0
        feedback.append("Password is too common.")

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


password = input("Enter your password: ")
result = check_password_strength(password)
print("Password Strength:", result["strength"])
for i in result["feedback"]:
    print("-", i)

