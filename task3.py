import random
import string

def generate_password(length, complexity, user_string):
    # Define the character sets based on complexity
    if complexity == 'easy':
        characters = string.ascii_lowercase
    elif complexity == 'medium':
        characters = string.ascii_letters
    elif complexity == 'hard':
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        raise ValueError("Invalid complexity level. Choose 'easy', 'medium', or 'hard'.")

    # Ensure the length is positive
    if length <= 0:
        raise ValueError("Password length must be a positive integer.")

    # If a user string is provided, ensure it is included in the password
    if user_string:
        # Make sure the user string is valid within the character set
        user_string = ''.join(c for c in user_string if c in characters)
        if len(user_string) > length:
            raise ValueError("The password length is not sufficient to include the provided user string.")
        characters += user_string
        length -= len(user_string)
    else:
        user_string = ''

    # Generate the password with the required length
    password = ''.join(random.choice(characters) for _ in range(length))
    password += user_string

    # Shuffle the password to ensure the user string is mixed in
    password = ''.join(random.sample(password, len(password)))

    return password

def main():
    while True:
        print("\nPassword Complexity Levels:")
        print("1. Easy: Includes lowercase letters only (e.g., 'abcdefghij').")
        print("2. Medium: Includes both lowercase and uppercase letters (e.g., 'AbCdEfGhIj').")
        print("3. Hard: Includes lowercase letters, uppercase letters, digits, and special characters (e.g., 'A1b@C2d#').")
        print("You can specify a custom string to be included in the password. If no string is provided, the password will be generated with random characters based on the selected complexity level.")
        print("NOTE: User entered string is case-sensitive.\n")
        try:
            length = int(input("Enter the desired length of the password: "))
            complexity = input("Enter the complexity level (easy, medium, hard): ").strip().lower()
            user_string = input("Enter a string to include in the password (or press Enter to skip): ").strip()

            # If the input is empty, set user_string to None
            if user_string == '':
                user_string = None

            password = generate_password(length, complexity, user_string)
            print("Generated Password: ",password)

        except ValueError as error:
            print(error)

        # Ask user if they want to generate another password
        while True:
            repeat = input("\nDo you want to generate another password? (yes/no): ").strip().lower()
            if repeat == 'yes':
                break
            elif repeat == 'no':
                print("Thank you for using the password generator!")
                return
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    main()
