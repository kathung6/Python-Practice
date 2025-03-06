user_input = input("")
lowercase_input = user_input.strip().lower()
character_list = {}

# loops throught the string
for c in lowercase_input:
    if c == " ": #skips spaces
        continue
    # if character is in dict, increase count
    if c in character_list:
        character_list[c] += 1
    # if character is not in dict, initialize count to 1 
    else:
        character_list[c] = 1
        
# defines alphabet to check for missing letters
alphabet = set('abcdefghijklmnopqrstuvwxyz')

# finds the missing letters from the string
missing_letters = alphabet - set(lowercase_input)

# print each character and how many times it appears
for key in sorted(character_list):
    print(key,"       ",character_list[key])

# prints the missing letters
print("Missing letters:")
for m in sorted(missing_letters):
    print(f"{m}", end=" ")