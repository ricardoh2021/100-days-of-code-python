#TODO: Create a letter using starting_letter.txt
with open("./Input/Letters/starting_letter.txt") as file:
    starting_letter = file.read()

print(starting_letter)

names = []
with open("./Input/Names/invited_names.txt") as name_file:
        for line in name_file:
            name = line.rstrip()
            names.append(name)

print(names)

# Replace the target string
for name in names:
    personal_letter = starting_letter.replace('[name]', name)
    with open(f"./Output/ReadyToSend/letter_for_{name}.docx", 'w') as file:
        file.write(personal_letter)

# Write the file out again

#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp