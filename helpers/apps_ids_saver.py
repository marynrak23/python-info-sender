from helpers.apps_ids_getter import getIdsApps


def saveChatIdApps(id):
    if id not in getIdsApps():
        with open('chat_ids_apps', 'a') as file:
            file.write(f'{id}\n')