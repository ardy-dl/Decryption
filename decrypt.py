# ask for string input to decrypt, save it
encrypt_text = input("Enter a string to decrypt: ")
decrypt_text = ""
# loop through entire characters
for char in encrypt_text:
#   if * change to a
    if char == "*":
        decrypt_text += "a"
#   if & change to e
#   if # change to i
#   if + change to o
#   if ! change to u
# if not vowel
    else:
        decrypt_text += char
# print the output
print(decrypt_text)
# Create design