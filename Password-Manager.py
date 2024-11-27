
from cryptography.fernet import Fernet

import os

# Function to generate a key for encryption
def generate_key():
    return Fernet.generate_key()

# Function to load or generate a key
def load_key():
    if os.path.exists("secret.key"):
        with open("secret.key", "rb") as key_file:
            return key_file.read()
    else:
        key = generate_key()
        with open("secret.key", "wb") as key_file:
            key_file.write(key)
        return key

# Function to encrypt a password
def encrypt_password(password, key):
    f = Fernet(key)
    encrypted_password = f.encrypt(password.encode())
    return encrypted_password

# Function to decrypt a password
def decrypt_password(encrypted_password, key):
    f = Fernet(key)
    decrypted_password = f.decrypt(encrypted_password).decode()
    return decrypted_password

# Function to add a password entry
def add_password(website, username, password, key):
    encrypted_password = encrypt_password(password, key)
    with open("passwords.txt", "a") as file:
        file.write(f"{website},{username},{encrypted_password.decode()}\n")
    print("Password added successfully.")

# Function to view saved passwords
def view_passwords(key):
    try:
        with open("passwords.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                website, username, encrypted_password = line.strip().split(",")
                decrypted_password = decrypt_password(encrypted_password.encode(), key)
                print(f"Website: {website}, Username: {username}, Password: {decrypted_password}")
    except FileNotFoundError:
        print("No passwords saved yet.")

# Main function for the password manager
def main():
    key = load_key()

    # Simulate a login process (master password)
    master_password = input("Enter your master password: ")
    if master_password != "my_master_password":
        print("Incorrect master password.")
        return

    while True:
        print("\n--- Password Manager ---")
        print("1. Add a new password")
        print("2. View saved passwords")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            website = input("Enter the website name: ")
            username = input("Enter the username: ")
            password = input("Enter the password: ")
            add_password(website, username, password, key)

        elif choice == "2":
            view_passwords(key)

        elif choice == "3":
            print("Exiting...")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
