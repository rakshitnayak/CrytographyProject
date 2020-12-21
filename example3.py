def encrypt(text, s):
    result = ""
    # traverse text
    for i in range(len(text)):
        char = text[i]

        # Encrypt uppercase characters
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)

        # Encrypt lowercase characters
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)

    return result

# Decryption


def decrypt(text, s):
    result = ""
    # traverse text
    for i in range(len(text)):
        char = text[i]

        # Encrypt uppercase characters
        if (char.isupper()):
            result += chr((ord(char) - s-65) % 26 + 65)

        # Encrypt lowercase characters
        else:
            result += chr((ord(char) - s - 97) % 26 + 97)

    return result


# check the above function
text = input("Enter the message \n")
s =int(input("Enter the value \n"))
text2 = encrypt(text, s)
print("Text  : " + text)
print("Key : " + str(s))
print("Encrypted  Text : " + encrypt(text, s))
print("Decrypted  Text : " + decrypt(text2, s))
