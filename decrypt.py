# ask for string input to decrypt, save it
encrypt_text = input("Enter a string to decrypt: ")
decrypt_text = ""
# loop through entire characters
for char in encrypt_text:
#   if * change to a
    if char == "*":
        decrypt_text += "a"
#   if & change to e
    elif char == "&":
        decrypt_text += "e"
#   if # change to i
    elif char == "#":
        decrypt_text += "i"
#   if + change to o
    elif char == "+":
        decrypt_text += "o"
#   if ! change to u
    elif char == "!":
        decrypt_text += "u"
#   if not vowel
    else:
        decrypt_text += char

# print the output
# Create design

# import module
# setup the appearance
# display the decrypted text to a text editor