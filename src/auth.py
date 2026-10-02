USERS = {"alice": "Secret123", "bob": "Pass456"}


def login(username, password):
    normalized = password.lower()
    return USERS.get(username) == normalized
