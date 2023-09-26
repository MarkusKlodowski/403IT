import random
import string
import time

# This function generates a random password of a given length
def generate_random_password(length):
    # Define the characters to choose from for the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password by selecting 'length' characters from the defined set
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password


# This function attempts to crack a given password by generating all possible combinations of characters
# and comparing them to the given password
def passwordCrack(password):
    start = time.time()
    characters = string.ascii_letters + string.digits + string.punctuation
    attempts = 0

    # Generate all possible combinations of characters of length 1 to the length of the password
    for length in range(1, len(password) + 1):
        for guess in generate_combinations(length, characters):
            attempts += 1
            if guess == password:
                end = time.time()
                # Return the number of attempts, the cracked password, and the time taken to crack the password
                return (attempts, guess, end-start)
    # If the password is not cracked, return the number of attempts and None for the cracked password
    return (attempts, None)


# This function generates all possible combinations of characters of a given length from a given set of characters
def generate_combinations(length, characters):
    # If the length is 0, yield an empty string
    if length == 0:
        yield ''
    else:
        # For each character in the given set of characters, generate all possible combinations of length-1 characters
        # and append the current character to each of those combinations
        for char in characters:
            for combo in generate_combinations(length - 1, characters):
                yield char + combo

