# Generating different types of passwords, strong medium and weak.
import string
import random

def generate_password_strong():
    return generate_password(12)

def generate_password_medium():
    return generate_password(8)

def generate_password_weak():
    return generate_password(6)

def generate_password(length):
    password = ""
    for i in range(length):
        password += random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
    return password
