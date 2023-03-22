def encode(password):
    #Cristian Sanchez
    encoded_password = ''.join(str((int(digit) + 3) % 10) for digit in password)
    print("Your password has been encoded and stored!")
    return encoded_password


def decode(encoded_password):
    decoded_password = ''.join(str((int(digit) - 3) % 10) for digit in encoded_password)
    print("The encoded password is", encoded_password, ", and the original password is", decoded_password)
    return decoded_password


# Start of the loop
while True:
    # Menu with first input by user
    print("Menu \n-------------\n1. Encode\n2. Decode\n3. Quit")
    choice = int(input("Please enter an option:"))

    # This is the encoder option. It encodes the password.
    if choice == 1:
        password = input("Please enter your password to encode: ")
        encoded_password = encode(password)

    # This is the decoder option. It decodes the original encoded password.
    elif choice == 2:
        pass
    elif choice == 3:
        break
