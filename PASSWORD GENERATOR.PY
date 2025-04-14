import random
import string
import pyperclip
from termcolor import colored

def generate_password(length, include_uppercase, include_digits, include_special_chars):
    # Define character sets based on the user's options
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

    # Create a pool of characters based on the user's preferences
    characters = lowercase
    if include_uppercase:
        characters += uppercase
    if include_digits:
        characters += digits
    if include_special_chars:
        characters += special_chars

    # Generate the password by randomly selecting characters
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def password_strength(password):
    # Evaluate the strength of the password based on its length and character variety
    if len(password) < 8:
        return "Weak"
    elif any(c.isdigit() for c in password) and any(c.isupper() for c in password) and any(c in string.punctuation for c in password):
        return "Strong"
    else:
        return "Moderate"

def main():
    print(colored("Welcome to the Professional Password Generator!", "cyan"))
    print(colored("---------------------------------------------", "cyan"))

    # Get user input for password length
    while True:
        try:
            length = int(input("Enter the desired length of the password (e.g., 12): "))
            if length < 6:
                print(colored("Password length should be at least 6 characters for security reasons.", "red"))
                continue
            break
        except ValueError:
            print(colored("Please enter a valid number for length.", "red"))

    # Ask for character inclusion preferences
    include_uppercase = input("Include uppercase letters? (yes/no): ").strip().lower() == "yes"
    include_digits = input("Include digits? (yes/no): ").strip().lower() == "yes"
    include_special_chars = input("Include special characters? (yes/no): ").strip().lower() == "yes"

    # Generate the password
    password = generate_password(length, include_uppercase, include_digits, include_special_chars)

    # Show password strength
    strength = password_strength(password)
    if strength == "Strong":
        strength_color = "green"
    elif strength == "Moderate":
        strength_color = "yellow"
    else:
        strength_color = "red"

    # Display the generated password
    print("\n" + colored("Your Generated Password:", "magenta").center(40, "-"))
    print(colored(password, strength_color).center(40))
    print("-" * 40)
    print(f"Password Strength: {colored(strength, strength_color)}")

    # Option to copy the password to clipboard
    copy = input("\nWould you like to copy this password to your clipboard? (yes/no): ").strip().lower()
    if copy == "yes":
        pyperclip.copy(password)
        print(colored("Password copied to clipboard!", "green"))
    
    print("\n" + colored("Stay safe and keep your password secure!", "blue"))

if __name__ == "__main__":
    main()
