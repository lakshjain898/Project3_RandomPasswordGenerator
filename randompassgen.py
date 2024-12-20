import random
import string
import os
import json
from datetime import datetime

# Password generation function
def generate_password(length=12, include_upper=True, include_lower=True, include_digits=True, include_symbols=True, exclude_similar=True):
    """
    Generates a highly customizable random password.

    Parameters:
        length (int): Length of the password.
        include_upper (bool): Include uppercase letters.
        include_lower (bool): Include lowercase letters.
        include_digits (bool): Include digits.
        include_symbols (bool): Include special characters.
        exclude_similar (bool): Exclude similar-looking characters (e.g., O and 0).

    Returns:
        str: Randomly generated password.
    """
    if length < 6:
        raise ValueError("Password length must be at least 6 characters for security.")

    # Define character pools
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    digits = string.digits
    symbols = string.punctuation
    similar_chars = "Il1O0"

    # Build character pool based on options
    char_pool = ""
    if include_upper:
        char_pool += upper
    if include_lower:
        char_pool += lower
    if include_digits:
        char_pool += digits
    if include_symbols:
        char_pool += symbols

    # Exclude similar characters if option enabled
    if exclude_similar:
        char_pool = ''.join(c for c in char_pool if c not in similar_chars)

    if not char_pool:
        raise ValueError("No character set selected. Please enable at least one character type.")

    # Securely generate the password
    secure_random = random.SystemRandom()  # Cryptographically secure random generator
    password = ''.join(secure_random.choice(char_pool) for _ in range(length))

    return password

# Save password history to a file
def save_password_history(password, settings):
    """
    Saves password and its generation settings to a history file.

    Parameters:
        password (str): Generated password.
        settings (dict): Settings used to generate the password.
    """
    history_file = "password_history.json"

    # Create a dictionary for this entry
    entry = {
        "password": password,
        "settings": settings,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    # Load existing history or create a new one
    try:
        with open(history_file, "r") as f:
            history = json.load(f)
    except FileNotFoundError:
        history = []

    # Append the new entry
    history.append(entry)

    # Save updated history back to the file
    with open(history_file, "w") as f:
        json.dump(history, f, indent=4)

# Generate password with user preferences
def main():
    print("Welcome to the Advanced Password Generator!")
    print("Customize your password generation preferences.")

    # Get user preferences
    try:
        length = int(input("Enter password length (minimum 6): "))
        include_upper = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
        include_lower = input("Include lowercase letters? (y/n): ").strip().lower() == 'y'
        include_digits = input("Include digits? (y/n): ").strip().lower() == 'y'
        include_symbols = input("Include symbols? (y/n): ").strip().lower() == 'y'
        exclude_similar = input("Exclude similar-looking characters (e.g., O and 0)? (y/n): ").strip().lower() == 'y'

        # Validate at least one type of character is included
        if not any([include_upper, include_lower, include_digits, include_symbols]):
            raise ValueError("At least one character type must be included.")

        # Generate the password
        password = generate_password(
            length=length,
            include_upper=include_upper,
            include_lower=include_lower,
            include_digits=include_digits,
            include_symbols=include_symbols,
            exclude_similar=exclude_similar
        )

        # Display the password
        print(f"\nGenerated Password: {password}")

        # Save the password and settings to history
        settings = {
            "length": length,
            "include_upper": include_upper,
            "include_lower": include_lower,
            "include_digits": include_digits,
            "include_symbols": include_symbols,
            "exclude_similar": exclude_similar
        }
        save_password_history(password, settings)
        print("Password saved to history!")

    except ValueError as e:
        print(f"Error: {e}")

    # Display the history option
    if input("\nDo you want to view your password history? (y/n): ").strip().lower() == 'y':
        display_password_history()

# Display password history
def display_password_history():
    """
    Displays the saved password history.
    """
    history_file = "password_history.json"
    try:
        with open(history_file, "r") as f:
            history = json.load(f)
        print("\nPassword History:")
        for entry in history:
            print(f"Time: {entry['timestamp']}, Password: {entry['password']}, Settings: {entry['settings']}")
    except FileNotFoundError:
        print("\nNo password history found.")

if __name__ == "__main__":
    main()
