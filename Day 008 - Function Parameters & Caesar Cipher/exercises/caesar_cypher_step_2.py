alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text, shift):
    encrypted_word = ""

    for index in range (0, len(text)):
        letter = text[index]
        newIndex = (alphabet.index(letter) + shift) % 26

        encrypted_word = encrypted_word + alphabet[newIndex]
    print(f"Encrypted word is {encrypted_word}")

#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
def decrypt(text, shift):


  #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
  #e.g. 
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"
    decrypted_word = ""

    for index in range (0, len(text)):
        letter = text[index]
        newIndex = (alphabet.index(letter) - shift) % 26

        decrypted_word = decrypted_word + alphabet[newIndex]
    print(f"Decrypted word is {decrypted_word}")


#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.

if direction == "encode":
    encrypt(text,shift)
elif direction == "decode":
    decrypt(text,shift)