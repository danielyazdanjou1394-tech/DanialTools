
import random

# DanialTools 1.0


# 1. Password Generator
def password_generator(length):
    chars = "abcdefghijklmnopqrstuvwxyz0123456789"
    password = ""

    for i in range(length):
        password += random.choice(chars)

    return password


# 2. Password Strength Checker
def password_strength(password):
    if len(password) < 6:
        return "Weak"

    elif len(password) < 10:
        return "Medium"

    else:
        return "Strong"


# 3. Verification Code Generator
def verification_code(length):
    code = ""

    for i in range(length):
        code += str(random.randint(0, 9))

    return code


# 4. Text Counter
def text_counter(text):
    words = len(text.split())
    letters = 0

    for char in text:
        if char != " ":
            letters += 1

    return {
        "words": words,
        "letters": letters
    }


# 5. Random Choice
def random_choice(items):
    return random.choice(items)
