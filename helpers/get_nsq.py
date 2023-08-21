import requests
import json


def getApps():
    url = 'https://profitovhome.com/api/apps/getAll'
    headers = {
        'Authorization': 'yzwvbrKSJyY0U65beFlvLerkLHat',
        'Content-type': 'application/json'
    }
    response = requests.get(url, headers=headers)
    for item in response.json():
        if item['newMark'] or item['newBan']:
            print(item)


getApps()