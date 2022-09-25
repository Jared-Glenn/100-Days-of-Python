import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift):
  cipher_text = ""
  for letter in text:
    if letter not in alphabet:
      cipher_text += letter
      continue
    ind = alphabet.index(letter)
    if direction == "encode":
      shifted_index = ind + shift
      while shifted_index > 25:
        shifted_index -= 26
    else:
      shifted_index = ind - shift
      while shifted_index < 0:
        shifted_index += 26
    cipher_text += alphabet[shifted_index]
  print(f"The {direction}d text is {cipher_text}")

print(art.logo)

running = True
while running:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  caesar(text, shift)
  keep_going = input("Type 'yes' if you want to go again. Otherwise type 'no'.").lower()
  if keep_going in ['n', 'no']:
    running = False

print("Goodbye!")