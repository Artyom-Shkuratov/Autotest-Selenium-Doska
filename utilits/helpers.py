import random

def generate_random_email():
    random_number = random.randint(1000, 9999)
    return f"test{random_number}@example.com"
