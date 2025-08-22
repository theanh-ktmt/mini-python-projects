import random

# Define character
lower_char = 'abcdefghijklmnopqrstuvwxyz'
upper_char = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
num = '0123456789'
spec_char = '@#$%&*'

combined_char = lower_char + upper_char + num + spec_char

def password_generator(length):
    # if length < 4:
    #     return "Error: Length must be at least 4."

    # Create a list with 1 character from each type
    password = [
        random.choice(lower_char),
        random.choice(upper_char),
        random.choice(num),
        random.choice(spec_char)
    ]

    # Create a list of random character from combined character list with remaining length

    remaining = length - 4
    password.extend(random.choices(combined_char, weights=None, cum_weights=None, k=remaining))

    # Shuffle list items
    random.shuffle(password)

    # Combine list items
    password = ''.join(password)
    return password

if __name__ == '__main__':
    while True:
        try:
            length = int(input("Enter your desired length (at least 4): "))
            if length >= 4:
                break
            else:
                print("Please enter a length of at least 4.")    
        except ValueError:
            print("Please enter a valid number")    

    print(f"Your generated password: {password_generator(length)}\n")
