# Lab 9: create a password encoder/decoder program with a partner

# takes a string of numbers, and returns a string of the numbers after adding 3
def encode(password):
    encoded_password = ' '.join(str((int(char) + 3) % 10) for char in password)
    return encoded_password
    # iris' implementation


# takes a string of numbers, and returns a string of the numbers after subtracting 3
def decode(password):
    # partner implementation
    pass


# main function: encode, decode, and exit options
