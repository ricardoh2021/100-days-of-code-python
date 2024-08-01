alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

from art import logo

def caesar(direction, text, shift):
    result = ""

    if direction == "decode":
        shift *= -1

    for index in range (0, len(text)):
        letter = text[index]
        if letter in alphabet:
            newIndex = (alphabet.index(letter) + shift) % 26
            result = result + alphabet[newIndex]
        else:
            result = result + letter
    print(f"Here is the {direction}d result: {result}")

print(logo)

while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(direction, text, shift)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")

    if restart != "yes":
        break
