import random
import string
import time

def generate_random_password(length):
    # Define the characters to choose from for the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password by selecting 'length' characters from the defined set
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password


import string

def passwordCrack(password):
    start = time.time()
    characters = string.ascii_letters + string.digits + string.punctuation
    attempts = 0

    for length in range(1, len(password) + 1):
        for guess in generate_combinations(length, characters):
            attempts += 1
            if guess == password:
                end = time.time()
                return (attempts, guess, end-start)
    return (attempts, None)

def generate_combinations(length, characters):
    if length == 0:
        yield ''
    else:
        for char in characters:
            for combo in generate_combinations(length - 1, characters):
                yield char + combo

# Example usage:

password = "aaaaa"
generate_random_password(5)
print("password is:", password)
print(passwordCrack(password))


