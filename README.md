# Advanced Password Generator

This is a feature-packed **Advanced Password Generator** built in Python. It allows users to generate highly customizable, secure passwords and manage them with a history feature. The program includes enhanced options for flexibility and security, ensuring robust password generation for all needs.

---

## Features

### 1. **Highly Customizable Passwords**:
- User-defined password length (minimum 6 characters).
- Option to include/exclude:
  - Uppercase letters.
  - Lowercase letters.
  - Digits.
  - Special symbols.
- Option to exclude similar-looking characters (e.g., `O` and `0`, `I` and `l`).

### 2. **Secure Password Generation**:
- Uses `random.SystemRandom()` for cryptographically secure random numbers.
- Ensures randomness and unpredictability in password generation.

### 3. **Password History Management**:
- Saves all generated passwords with their settings to `password_history.json`.
- Includes timestamps for tracking when passwords were generated.
- Allows users to view saved password history.

### 4. **Error Handling**:
- Ensures minimum password length requirement.
- Validates that at least one character type is included.
- Provides clear error messages for invalid inputs.

### 5. **User-Friendly Interaction**:
- Interactive prompts for custom password generation.
- Clean and informative output.
- Simple to use, even for non-technical users.

---

## How It Works

1. The script starts with a welcome message and guides the user through setting their preferences for password generation.
2. Users can customize password length and the inclusion of character types.
3. The program generates a secure password based on the selected options.
4. The generated password is displayed and saved to a history file (`password_history.json`).
5. Users can optionally view their password history with timestamps and settings.

---

## Prerequisites

- Python 3.x installed on your system.
- The `os`, `random`, `json`, and `datetime` modules (built-in with Python).

---

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/advanced-password-generator.git
   ```

2. Navigate to the project directory:
   ```bash
   cd advanced-password-generator
   ```

3. Run the script:
   ```bash
   python password_generator.py
   ```

---

## Usage

1. Run the script and follow the prompts:
   - Set password length.
   - Choose character types (uppercase, lowercase, digits, symbols).
   - Decide whether to exclude similar-looking characters.
2. View the generated password.
3. Save it securely (optional).
4. Access the password history to retrieve previous passwords.

### Example Interaction

```
Welcome to the Advanced Password Generator!
Customize your password generation preferences.
Enter password length (minimum 6): 12
Include uppercase letters? (y/n): y
Include lowercase letters? (y/n): y
Include digits? (y/n): y
Include symbols? (y/n): n
Exclude similar-looking characters (e.g., O and 0)? (y/n): y

Generated Password: AhKqT7mwp2Lc
Password saved to history!

Do you want to view your password history? (y/n): y

Password History:
Time: 2024-12-20 12:34:56, Password: AhKqT7mwp2Lc, Settings: {"length": 12, "include_upper": true, "include_lower": true, "include_digits": true, "include_symbols": false, "exclude_similar": true}
```

---

## File Structure

- **`password_generator.py`**: Main script file containing the logic.
- **`password_history.json`**: JSON file where password history is stored.

---

## Future Enhancements

- Add an option to export passwords to an encrypted file.
- Include a strength meter to evaluate password complexity.
- Build a GUI interface for easier use.
- Integrate with a password manager API for secure storage.

---



## Contribution

Contributions are welcome! Feel free to open issues or submit pull requests for improvements or bug fixes.

---

## Author

Created by **Laksh Jain**.
