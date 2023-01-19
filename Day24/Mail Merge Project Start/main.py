#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

NAMES = []

with open(r"Day24\Mail Merge Project Start\Input\Names\invited_names.txt") as names_file :
    for name in names_file:
        NAMES.append(name.strip())

# NAMES = ["Aang", "Toph", "CHICKEN", "Froggy"]
# print(NAMES)

with open(r"Day24\Mail Merge Project Start\Input\Letters\starting_letter.txt") as letter_file :
    letter_contents = letter_file.read()
    for name in NAMES :
        new_letter = letter_contents.replace("[name]", name)
        # print(new_letter)
        with open(fr"Day24\Mail Merge Project Start\Output\ReadyToSend\letter_for_{name}.txt", mode = "w") as completed_letter :
            completed_letter.write(new_letter)