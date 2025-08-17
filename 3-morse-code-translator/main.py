import time
import platform

# Morse code dictionary
morse_code_dict = {
    'A': '.-',      'B': '-...',    'C': '-.-.',    'D': '-..',     'E': '.',
    'F': '..-.',    'G': '--.',     'H': '....',    'I': '..',      'J': '.---',
    'K': '-.-',     'L': '.-..',    'M': '--',      'N': '-.',      'O': '---',
    'P': '.--.',    'Q': '--.-',    'R': '.-.',     'S': '...',     'T': '-',
    'U': '..-',     'V': '...-',    'W': '.--',     'X': '-..-',    'Y': '-.--',
    'Z': '--..',
    '0': '-----',   '1': '.----',   '2': '..---',   '3': '...--',   '4': '....-',
    '5': '.....',   '6': '-....',   '7': '--...',   '8': '---..',   '9': '----.',
    '.': '.-.-.-',  ',': '--..--',  '?': '..--..',  "'": '.----.',  '!': '-.-.--',
    '/': '-..-.',   '(': '-.--.',   ')': '-.--.-',  '&': '.-...',   ':': '---...',
    ';': '-.-.-.',  '=': '-...-',   '+': '.-.-.',   '-': '-....-',  '_': '..--.-',
    '"': '.-..-.',  '$': '...-..-', '@': '.--.-.',  ' ': '/'
}

def play_sound(duration):
    """Plays a beep sound for the given duration in milliseconds."""
    if platform.system() == 'Windows':
        import winsound
        winsound.Beep(1000, duration)  # 1000 Hz tone
    else:
        # For Linux and macOS: use terminal bell
        print('\a', end='', flush=True)
        time.sleep(duration / 1000)  # Approximate sound duration with a pause

def text_to_morse(text):
    """Converts text to Morse code with spaces between symbols."""
    morse_code = ''
    for char in text.upper():
        if char in morse_code_dict:
            morse_code += morse_code_dict[char] + ' '
        else:
            # Optionally warn about unsupported characters
            print(f"⚠️  Skipping unsupported character: '{char}'")
    return morse_code.strip()

def morse_to_sound(morse_code):
    """Plays Morse code using beeps and pauses."""
    print("🔊 Playing Morse code: ", end='', flush=True)
    
    i = 0
    while i < len(morse_code):
        symbol = morse_code[i]
        
        if symbol == '.':
            print('.', end='', flush=True)
            play_sound(100)           # Dot: 100ms
            time.sleep(0.1)           # Gap between signals
        elif symbol == '-':
            print('-', end='', flush=True)
            play_sound(300)           # Dash: 300ms
            time.sleep(0.1)           # Gap between signals
        elif symbol == ' ':
            # Space between characters
            print(' ', end='', flush=True)
            time.sleep(0.3)
        elif symbol == '/':
            # Space between words
            print(' / ', end='', flush=True)
            time.sleep(0.7)
        
        i += 1
    print()  # New line after playback

# ----------------------------
# Main Program
# ----------------------------
if __name__ == '__main__':
    print("🔤 Morse Code Translator with Sound")
    print("Enter text to hear it in Morse code!")
    print("📌 Example: 'SOS' → '... --- ...'")
    print("⌨️  Press Ctrl+C to exit.\n")

    try:
        while True:
            user_input = input("\nEnter text: ").strip()
            
            if not user_input:
                print("❗ Please enter some text.")
                continue

            # Convert to Morse
            morse = text_to_morse(user_input)
            print("Morse Code:", morse)
            
            # Play sound
            morse_to_sound(morse)
            
    except KeyboardInterrupt:
        print("\n\n👋 Thanks for using the Morse Code Translator. Goodbye!")
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")