# Remembering Caesar cipher
def caesar_cipher(text, shift):
    result = ""

    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)

        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char

    return result


def polyalphabetic_encryption(plaintext):
    result = ""
    toggle = True

    for char in plaintext:
        if char.isalpha():
            k = 5 if toggle else 19
            result += caesar_cipher(char, k)
            toggle = not toggle
        else:
            result += char
    return result


plaintext = "Alice, I love you."
ciphertext = polyalphabetic_encryption(plaintext)
print("Encrypted:", ciphertext)
