import random

# Define character

lower_char = 'abcdefghijklmnopqrstuvwxyz'
upper_char = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
num = '0123456789'
spec_char = '@#$%&*'

combined_char = lower_char + upper_char + num + spec_char

def password_generator(length):
    if length < 1:
        print("Invalid. Length must be greater than 1")

    
    # Generate randomly k-length password from combined character list. Repetition is allowed

    password = ''.join(random.choices(combined_char, weights=None, cum_weights=None, k=length))
    return password

while __name__ == '__main__':

    length = int(input("Enter your desired length: "))
    print(f"Your generated password: {password_generator(length)}\n")
