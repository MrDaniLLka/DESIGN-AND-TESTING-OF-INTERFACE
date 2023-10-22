from entities import Company, Employee
import requests
from utils import get_info, warning
import json

base_url = "http://127.0.0.1:8000"


if __name__ == '__main__':
    while True:
        get_info()
        status = input('Введите опцию: ')
        if not status.isdigit() and int(status) not in range(1, 6):
            print(int(status) in range(1, 6))
            warning()
            continue
        else:
            status = int(status)
        if status == 1:
            print(requests.get(base_url + "/comps").content)
        if status == 2:
            print(requests.get(base_url + "/users").content)
        if status == 3:
            data = {"name": input('Имя:'),
                    "surname": input('Фамилия:'),
                    "position": input('Должность:'),
                    "company": input('Компания:')}
            requests.post(base_url + "/users", json.dumps(data), headers={"Content-Type": "application/json"})

        if status == 4:
            del_id = input('Введите id пользователя для его удаления:')
            if del_id.isdigit():
                requests.delete(base_url + f"/users/{del_id}")

        if status == 5:
            upd_id = input('Введите id пользователя для его изменения:')
            if upd_id.isdigit():
                data = {"name": input('Имя:'),
                        "surname": input('Фамилия:'),
                        "position": input('Должность:'),
                        "company": input('Компания:')}
                requests.put(base_url + f"/users/{upd_id}", json.dumps(data), headers={"Content-Type": "application/json"})