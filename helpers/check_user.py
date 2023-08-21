


def checkUser(username):
    with open('approved_users', 'r') as file:
        if username not in file.read().split():
            return False
        else:
            return True

