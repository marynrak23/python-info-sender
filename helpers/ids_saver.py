

def saveChatId(id):
    with open('chat_ids', 'a') as file:
        file.write(f'{id}\n')