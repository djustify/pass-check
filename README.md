# Password Strength Checker

A simple Python script that evaluates the strength of a password based on length, uppercase letters, lowercase letters, digits, and special characters. It provides a strength rating (Strong, Moderate, Weak) along with actionable feedback to help users improve their passwords.

## Features

- Checks if the password length is at least 8 characters, with extra weight for 10 or more characters.
- Verifies presence of uppercase and lowercase letters.
- Checks for digits and special characters.
- Scores the password and categorizes it as Strong, Moderate, or Weak.
- Provides suggestions to improve password strength.

## Usage

Run the script and enter a password when prompted:

```bash
python password_strength_checker.py
```

## Example:
```bash
Enter a password to evaluate: MyPass123
Password score: 4/6
Password strength: Moderate
```

## How It Works
The script uses regular expressions to detect character types and assigns points based on the presence of each category and password length. The total score determines the strength category.# pass-check
