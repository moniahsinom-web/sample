import random
import string

def generate_password(length):
    # Define possible characters for the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a random password
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

# Ask user for desired password length
length = int(input("Enter the desired password length: "))

# Generate and display password
print("Generated Password:", generate_password(length))
