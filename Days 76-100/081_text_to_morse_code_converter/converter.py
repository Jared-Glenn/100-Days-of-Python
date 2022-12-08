

class Converter:
    def __init__(self):
        self.morse_library = { 'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
                          'F': '..-.', 'G': '--.', 'H': '....','I': '..', 'J': '.---',
                          'K': '-.-','L': '.-..', 'M': '--', 'N': '-.','O': '---', 'P': '.--.',
                          'Q': '--.-','R': '.-.', 'S': '...', 'T': '-','U': '..-', 'V': '...-',
                          'W': '.--','X': '-..-', 'Y': '-.--', 'Z': '--..','1': '.----', '2': '..---',
                          '3': '...--','4': '....-', '5': '.....', '6': '-....','7': '--...', '8': '---..',
                          '9': '----.','0': '-----', ', ': '--..--', '.': '.-.-.-','?': '..--..',
                          '/': '-..-.', '-': '-....-','(': '-.--.', ')': '-.--.-'}

    def text_to_morse(self, text):
        text = str(text)
        text = text.upper()

        final_text = ""
        for letter in text:
            if letter in self.morse_library:
                final_text = final_text + self.morse_library[letter]
            else:
                final_text = final_text + letter

        return final_text