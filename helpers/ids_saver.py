

def saveChatId(id):
    with open('chat_ids.txt', 'a') as file:
        file.write(f'{id}\n')