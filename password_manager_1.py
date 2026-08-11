from cryptography.fernet import Fernet
import os


KEY_FILE = "key.key"
PASSWORD_FILE = "password.txt"


# Create the encryption key if it doesn't exist
def create_key():
    key = Fernet.generate_key()

    with open(KEY_FILE, "wb") as file:
        file.write(key)

    print("New encryption key created!")


# Load the existing encryption key
def load_key():
    with open(KEY_FILE, "rb") as file:
        return file.read()



# Create a key automatically if we don't have one
if not os.path.exists(KEY_FILE):
    create_key()


# Load the key
key = load_key()

# Create our encryption/decryption tool
fer = Fernet(key)


# View saved passwords
def view():
    if not os.path.exists(PASSWORD_FILE):
        print("No passwords saved yet.")
        return

    with open(PASSWORD_FILE, "r") as file:
        for line in file.readlines():

            data = line.rstrip()

            if not data:
                continue

            user, encrypted_password = data.split("|")

            password = fer.decrypt(
                encrypted_password.encode()
            ).decode()

            print(f"Account: {user}")
            print(f"Password: {password}")
            print()


# Add a new password
def add():
    name = input("Account Name: ")
    password = input("Password: ")

    encrypted_password = fer.encrypt(
        password.encode()
    ).decode()

    with open(PASSWORD_FILE, "a") as file:
        file.write(
            name + "|" + encrypted_password + "\n"
        )

    print("Password saved!")


# Main program
while True:

    mode = input(
        "\nWould you like to add a new password "
        "or view existing ones? (view, add) "
        "Press q to quit: "
    ).lower()

    if mode == "q":
        break

    elif mode == "view":
        view()

    elif mode == "add":
        add()

    else:
        print("Invalid mode.")