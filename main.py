from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(plain_text, shift_amount, direction):
    if direction == "encode":
        cipher_text = ""
        for char in plain_text:
            if char in alphabet:
                position = alphabet.index(char)
                new_position = position + shift_amount
                cipher_text += alphabet[new_position]
            else:
                cipher_text += char
        print(f"The encoded text is {cipher_text}")

    elif direction == "decode":
        decoded_text = ""
        for char in plain_text:
            if char in alphabet:
                position = alphabet.index(char)
                new_position = position - shift_amount
                decoded_text += alphabet[new_position]
            else:
                decoded_text += char
        print(f"The decoded text is {decoded_text}")


print(logo)


should_end = False
while not should_end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = (int(input("Type the shift number:\n"))) % 26

    caesar(plain_text=text, shift_amount=shift, direction=direction)


    choice = input("If you want to continue type 'yes'; otherwise type 'no'\n")

    if choice == "no":
        print("Goodbye")
        should_end = True
    elif choice == "yes":
        continue
    else:
        print("Please type correctly...")

