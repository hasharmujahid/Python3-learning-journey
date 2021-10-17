alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
directions = input("enter 'encode' to encrypt and 'decode' to decrypt ").lower()
shift_val = int(input('enter the shift value'))
text = str(input("enter the text "))


def encryption(plain_text, shift_value):
    cypher_text = ''
    for letters in plain_text:
        pos = alphabets.index(letters)
        new_pos = pos + shift_value
        cypher_text += alphabets[new_pos]
    print(f"your encrypted text is {cypher_text}")
    return cypher_text


def decrytion(encrypted_text, shiftval):
    decrypt = ''
    for letter in encrypted_text:
        pos = alphabets.index(letter)
        new_pos = pos - shiftval
        decrypt += alphabets[new_pos]
    print(f"your decrypted text is {decrypt}")


if directions == 'encode':
    encryption(text, shift_val)
if directions == 'decode':
    decrytion(encrypted_text=text, shiftval=shift_val)
