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
        if item['mark'] or item['status'] == 'banned':
            print(item)


getApps()