

def getIDs():
    with open("chat_ids.txt", 'r') as file:
        return file.read().split()
