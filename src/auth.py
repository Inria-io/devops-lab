USERS = {"alice": "Secret123", "bob": "Pass456"}


def login(username, password):
    return USERS.get(username) == password
