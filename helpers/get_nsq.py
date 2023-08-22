import requests
import json
import os


def getApps():
    url = 'https://profitovhome.com/api/apps/getAll'
    headers = {
        'Authorization': 'yzwvbrKSJyY0U65beFlvLerkLHat',
        'Content-type': 'application/json'
    }
    response = requests.get(url, headers=headers)

    apps_data = []
    for item in response.json():
        name = item.get('name')
        mark = item.get('mark')
        status = item.get('status')

        apps_data.append({
            'name': name,
            'mark': mark,
            'status': status
        })

    changed_names = []
    with open('/Users/darkside/Desktop/python-info-sender/helpers/apps.json', 'r') as file:
        file_data = json.load(file)
        for item in file_data:
            name = item['name']
            file_mark = item.get('mark')
            file_status = item.get('status')

            for app in apps_data:
                if app['name'] == name and (app['mark'] != file_mark or app['status'] != file_status):
                    changed_names.append(name)
                    break

    with open('/Users/darkside/Desktop/python-info-sender/helpers/apps.json', 'w') as file:
        json.dump(apps_data, file, ensure_ascii=False, indent=4)

    return changed_names


changed_apps = getApps()
print("Changed apps:", changed_apps)