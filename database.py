def save_data(encrypted_data):
    with open("data.crypt", "w") as file:
        data = encrypted_data.decode()
        file.write(data)
        file.close()


def load_data():
    with open("data.crypt", "r") as file:
        # Reading from a file
        token_dec = file.read()
        file.close()
        return token_dec


def load_key():
    """
    Load the previously generated key
    """
    return open("secret.key", "rb").read()
