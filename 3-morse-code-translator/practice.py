def morse_code_translator(message):
    # empty list
    result = []
    # morse code table
    morse_code_dict = {
    # alphabet
    'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',   'E': '.', 
    'F': '..-.',  'G': '--.',   'H': '....',  'I': '..',    'J': '.---', 
    'K': '-.-',   'L': '.-..',  'M': '--',    'N': '-.',    'O': '---', 
    'P': '.--.',  'Q': '--.-',  'R': '.-.',   'S': '...',   'T': '-', 
    'U': '..-',   'V': '...-',  'W': '.--',   'X': '-..-',  'Y': '-.--', 
    'Z': '--..',

    # numbers
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', 
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    
    # special characters
    '.': '.-.-.-',  ',': '--..--',  '?': '..--..',  "'": '.----.',  '!': '-.-.--',
    '/': '-..-.',   '(': '-.--.',   ')': '-.--.-',  '&': '.-...',   ':': '---...',
    ';': '-.-.-.',  '=': '-...-',   '+': '.-.-.',   '-': '-....-',  '_': '..--.-',
    '"': '.-..-.',  '$': '...-..-', '@': '.--.-.', ' ': '/'
}
    message = message.upper()
    for index, char in enumerate(message):
        if char in morse_code_dict.keys():
            morse_code = morse_code_dict.get(char)
        else:
            print(f"Skipping unsupported {char} at position {index + 1}")
            continue
        result.append(morse_code)
        
    return ' '.join(result)
    
if __name__ == '__main__':
    user_message = input("Enter your message: ")
    print(f"Your morse code translator: {morse_code_translator(user_message)}")
