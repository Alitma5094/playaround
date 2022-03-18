from crypt import generate_key, load_key, encrypt_data, decrypt_data
from database import save_data, load_data
import json
import ast
import configparser


def get_data(save_data):
    print("What is the name of the website?")
    website = input("> ")
    print("What is your email or username?")
    username = input("> ")
    print("What is your password?")
    password = input("> ")
    save_data[website] = {"Username": username, "Password": password}
    return save_data


def get_key():  # clean up this function remove first part of if statement
    print("Have you already created a key file? (Y/n)")
    response = input("> ").lower()
    while True:
        if response.startswith("y") or response == "":
            return load_key()
        elif response.startswith("n"):
            generate_key()
            return load_key()

def settings():
    print()


def start_cli():
    data = {}
    key = get_key()
    while True:  # Keep asking until the user enters e or d.
        print('Do you want to add a (n)ew password, (v)iew old passwords, or (q)uit?')
        response = input('> ').lower()
        if response.startswith('n'):
            data = get_data(data)
        elif response.startswith("v"):
            loaded_data = bytes(load_data(), "ascii")
            decrypted_data = decrypt_data(loaded_data, key)
            new = decrypted_data.decode("ascii")
            new = ast.literal_eval(new)
            for i in new:
                print(i + ": Username: " + new[i]["Username"] + ", Password: " + new[i]["Password"])
        elif response.startswith("q"):
            encrypted_data = encrypt_data(json.dumps(data), key)
            save_data(encrypted_data)
            break
