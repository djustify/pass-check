import re

def evaluate_password_strength(password):
    score = 0
    length = len(password)

    # Length points
    if length >= 8:
        score += 1
    if length >= 12:
        score += 1

    # Uppercase letters
    if re.search(r'[A-Z]', password):
        score += 1

    # Lowercase letters
    if re.search(r'[a-z]', password):
        score += 1

    # Numbers
    if re.search(r'\d', password):
        score += 1

    # Special characters
    if re.search(r'[^A-Za-z0-9]', password):
        score += 1

    # Strength evaluation
    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Moderate"
    else:
        strength = "Strong"

    return score, strength

if __name__ == "__main__":
    pwd = input("Enter a password to evaluate: ")
    score, strength = evaluate_password_strength(pwd)
    print(f"Password score: {score}/6")
    print(f"Password strength: {strength}")
