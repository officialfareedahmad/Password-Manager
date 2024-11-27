# Password Manager

This project is a beginner-friendly Password Manager implemented in Python. It allows you to securely store and manage your passwords using encryption.

## Features
- **Add Password**: Save your passwords for different websites or services.
- **View Passwords**: View all stored passwords in a decrypted format.

## How to Use

1. **Installation**:
   - Install Python 3.9 or later.
   - Install the `cryptography` library:
     ```
     pip install cryptography
     ```

2. **Run the Program**:
   - Save the code as `Password-Manager.py`.
   - Run the program:
     ```
     python Password-Manager.py
     ```

3. **Master Password**:
   - The program starts with a simple login using a pre-set master password.
   - Default master password: `my_master_password`.
   - You can change this in the code.

4. **Adding a Password**:
   - Select the option `1` in the menu.
   - Enter the website name, username, and password.
   - The password is encrypted and saved.

5. **Viewing Passwords**:
   - Select the option `2` in the menu.
   - View all stored passwords, decrypted.

6. **Exit**:
   - Select option `3` to exit the program safely.

## Files Created
- **`secret.key`**:
  - Stores the encryption key for encrypting and decrypting passwords.
  - Automatically generated if not present.

- **`passwords.txt`**:
  - Stores encrypted password entries in the format:
    ```
    website,username,encrypted_password
    ```
