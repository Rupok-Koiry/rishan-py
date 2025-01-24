# # Write your code below this line 👇


# # Write your code above this line 👆
# # Define a function called paint_calc() so that the code below works.
# import math


# def paint_calc(height, width, cover):
#     area = height*width
#     print(math.ceil(area/cover))


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
            'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().


def caesar(plain_text, shift_amount, direction):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + \
            shift_amount if direction == 'encode' else position - shift_amount
        cipher_text += alphabet[new_position]
    print(f"The encoded text is {cipher_text}")


caesar(plain_text=text, shift_amount=shift, direction=direction)
