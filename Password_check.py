import re


def check_password_strength(password):
    if len(password)<8:
        return False
    if not re.search(r'[A-Z]',password):
        return False
    if not re.search(r'[a-z]',password):
        return False
    if not re.search(r'\d',password):
        return False
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]',password):
        return False
    return True

password=input("enter the password:")
Is_strong=check_password_strength(password)

if Is_strong:
    print("Password is strong")
else:
    print("Password is weak")