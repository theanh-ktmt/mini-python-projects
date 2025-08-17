import random

# Define character sets
lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789'
special = '@#$%&*'

# Combine all characters
all_chars = lower + upper + digits + special


def generate_password(length):
    """
    Generates a random password of given length using
    lowercase, uppercase, digits, and special characters.
    
    Args:
        length (int): The desired password length.
    
    Returns:
        str: Generated password.
    """
    if length < 1:
        return "Error: Password length should be at least 1."
    
    # Use random.choices() instead of sample() to allow repetition and avoid sampling issues
    password = ''.join(random.choices(all_chars, k=length))
    return password


# Main Program
if __name__ == '__main__':
    while True:
        length = int(input("Enter the desired password length: "))
        password = generate_password(length)
        print(f"Generated Password: {password}\n")