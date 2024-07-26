#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
randomLetters = []
randomSymbols = []
randomNumbers = []

symbolIndicator = ['1', '2', '3'] #1 for letters, 2 for numbers, and 3 for symbols.

password = ""


for letterIndex in range(0, nr_letters):
    randomLetters.append(random.randint(0, len(letters)))

for symbolIndex in range(0, nr_symbols):
    randomSymbols.append(random.randint(0, len(symbols)))

for numberIndex in range(0, nr_numbers):
    randomNumbers.append(random.randint(0, len(numbers)))

print(randomLetters)
print(randomSymbols)
print(randomNumbers)

while len(randomLetters) > 0 or len(randomNumbers) or len(randomSymbols):
    randomNumber = random.randint(1,3)
    if(randomNumber == 1 and len(randomLetters) > 0):
        indexLetter = randomLetters.pop()
        passwordLetter = letters[indexLetter]
        password += passwordLetter
    elif(randomNumber == 2 and len(randomSymbols) > 0):
        indexSymbol = randomSymbols.pop()
        passwordSymbol = symbols[indexSymbol]
        password += passwordSymbol
    elif(randomNumber == 3 and len(randomNumbers) > 0):
        indexNumber = randomNumbers.pop()
        passwordNumber = numbers[indexNumber]
        password += passwordNumber

print(f"Your password is {password}")
## Chat GPT refactored version below .

# random_letters = [random.choice(letters) for _ in range(nr_letters)]
# random_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
# random_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

# password_characters = random_letters + random_symbols + random_numbers
# random.shuffle(password_characters)

# password = ''.join(password_characters)

# print(f"Your generated password is: {password}")