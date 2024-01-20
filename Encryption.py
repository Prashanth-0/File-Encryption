from cryptography.fernet import Fernet, MultiFernet
from pyfiglet import Figlet  
from termcolor import colored
import os


def generate_key():
    return Fernet.generate_key()

def save_key(key, filename="secret.key"):
    with open(filename, "wb") as key_file:
        key_file.write(key)

def load_key(filename="secret.key"):
    return open(filename, "rb").read()

def encrypt_file(file_path, key):
    with open(file_path, "rb") as file:
        data = file.read()

    cipher_suite = Fernet(key)
    encrypted_data = cipher_suite.encrypt(data)

    with open(file_path, "wb") as encrypted_file:
        encrypted_file.write(encrypted_data)

def decrypt_file(file_path, key, passphrase=None):
    if passphrase:
        key = MultiFernet([Fernet(load_key()), Fernet(passphrase)])

    with open(file_path, "rb") as encrypted_file:
        encrypted_data = encrypted_file.read()

    decrypted_data = key.decrypt(encrypted_data)

    with open(file_path, "wb") as original_file:
        original_file.write(decrypted_data)

if __name__ == "__main__":
    figlet = Figlet(font="slant")
    print(colored(figlet.renderText("Encryption"), "green"))

    developer_name = "Prashanth"
    print(colored(f"Developer: {developer_name}".center(80), "red"))

    while True:
        print(colored("Options:", "red"))
        print(colored("1. Encryption", "green"))
        print(colored("2. Decryption", "green"))
        print(colored("3. Exit", "green"))

        choice = input(colored("Enter your choice (1, 2, or 3): ", "red"))

        if choice == "1":
            encryption_key = generate_key()
            save_key(encryption_key)

            target_file = input("Enter the path to your file: ")
            encrypt_file(target_file, encryption_key)
            print(colored("File encrypted successfully.", "green"))

            break

        elif choice == "2":
            target_file = input("Enter the path to your encrypted file: ")
            passphrase_input = input("Enter the passphrase for decryption: ")
            decrypt_file(target_file, None, passphrase_input)
            print(colored("File decrypted successfully.", "green"))

            break

        elif choice == "3":
            print(colored("Exiting the program.", "yellow"))
            break

        else:
            print(colored("Invalid choice. Please choose either 1, 2, or 3.", "yellow"))
