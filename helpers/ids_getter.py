

def getIDs():
    with open("chat_ids", 'r') as file:
        return file.read().split()
