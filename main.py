# Iris Prifti Lab 9: create a password encoder/decoder program with a partner

# takes a string of numbers, and returns a string of the numbers after adding 3
def encode(password):
    # my implementation
    encoded_password = ''.join(str((int(char) + 3) % 10) for char in password)
    return encoded_password

    # Example usage
    encoded_password = encode("12345555")
    print(f"Encoded: {encoded_password}")  # Output: Encoded: 45678888


def decode(password):
    decoded_password = ''.join(str((int(char) - 3) % 10) for char in password)
    return decoded_password

# main function: encode, decode, and exit options
if __name__ == '__main__':
    while True:
        break