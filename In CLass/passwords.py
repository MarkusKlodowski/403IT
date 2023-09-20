import random
import string

def generate_random_password(length):
    # Define the characters to choose from for the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password by selecting 'length' characters from the defined set
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

password = generate_random_password(7)
print("Generated Password:", password)

f = open("passwords.txt", "w")
f.write(password)
f.close()

