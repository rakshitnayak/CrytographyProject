message = input("Enter the string to be encrypted\n")
translated = ''


i = len(message) - 1
while i >= 0:
    translated = translated + message[i]
    i = i-1
print("The encrypted code is ")
print(translated)


message = translated
translated = ''

i = len(message) - 1
while i >= 0:
    translated = translated + message[i]
    i = i-1

print("The decrypted code is ")
print(translated)
