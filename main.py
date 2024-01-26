import random
import string

def password_generator(passwordlength):
    # Define character sets for different complexity levels
    lower_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

    # Combine character sets based on desired complexity
    all_chars = lower_case + upper_case + digits + special_chars

    # Generate password using random.choices
    password = ''.join(random.choices(all_chars, k=passwordlength))

    return password

def main():
    # Get user input for password length
    try:
        passwordlength = int(input("Enter the desired length of the password: "))
    except ValueError:
        print("Please enter a valid number for password length.")
        return

    # Check if the length is non-negative
    if passwordlength <= 0:
        print("Password length should be greater than 0.")
        return

    # Generate and display the password
    password = password_generator(passwordlength)
    print("Generated Password:", password)

if __name__ == "__main__":
    main()
