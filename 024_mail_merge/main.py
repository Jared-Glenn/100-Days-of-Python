#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

name_list = []

# Move all names in the file to a list.
with open("./Input/Names/invited_names.txt") as names:
    for name in names:
        stripped_line = name.strip()
        name_list.append(stripped_line)

# Move the text of the letter to a string for ease of use.
with open("./Input/Letters/starting_letter.txt") as letter:
    text = letter.readlines()
    full_text = ""
    for line in text:
        full_text += line

# For each name in the list, substitute the name into the letter and create a file for that name.
for name in name_list:
    letter_for_name =full_text.replace("[name]", name)
    file_name = "./Output/ReadyToSend/letter_to_" + name + ".txt"
    with open(file_name, "w") as new_letter:
        new_letter.write(letter_for_name)

