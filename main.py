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

# main function implementation
def main():
    stored_password = ''
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        option = input("\nPlease enter an option: ")

        # menu options
        if option == '1':
            password = input("Please enter the password to encode: ")
            stored_password = encode(password)
            print("Your password has been encoded and stored!\n")
        elif option == '2':
            if stored_password:
                original_password = decode(stored_password)
                print(f"The encoded password is {stored_password}, and the original password is {original_password}.\n")
            else:
                print("No password has been encoded yet.\n")
        elif option == '3':
            break
        else:
            print("Invalid option, please try again.")

# run the main function
main()
