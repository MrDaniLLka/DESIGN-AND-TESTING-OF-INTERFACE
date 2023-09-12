from connection import Connection
from utils import get_info, get_id_company

if __name__ == '__main__':
    con = Connection()
    while True:
        get_info()
        status = input('Введите опцию: ')
        if not status.isdigit() and int(status) not in range(1, 6):
            print(int(status) in range(1, 6))
            print('Введите корректное значение!')
            continue
        else:
            status = int(status)
        if status == 1:
            for company in con.exec_select("SELECT name FROM companies"):
                print(company['name'])
        if status == 2:
            for employee in con.exec_select("SELECT id, name, surname FROM employes"):
                print(employee['id'], employee['name'], employee['surname'])
        if status == 3:
            name = input('Имя:')
            surname = input('Фамилия:')
            position = input('Должность:')
            company = input('Компания:')
            company_id = get_id_company(con, company)
            if not company_id:
                continue
            else:
                con.exec_edit(query="INSERT INTO employes(name, surname, position, company_id) VALUES (%s, %s, %s, %s)",
                              args=(name, surname, position, company_id))

        if status == 4:
            del_id = input('Введите id пользователя для его удаления:')
            if del_id.isdigit():
                con.exec_edit("DELETE FROM employes WHERE id = %s", (del_id,))
            else:
                print('Введите корректное значение id!')

        if status == 5:
            upd_id = input('Введите id пользователя для его изменения:')
            if upd_id.isdigit() and con.exec_select("SELECT FROM employes WHERE id = %s", (upd_id,)):
                name = input('Имя:')
                surname = input('Фамилия:')
                position = input('Должность:')
                company = input('Компания:')
                company_id = get_id_company(con, company)
                if not company_id:
                    continue
                else:
                    con.exec_edit(query="UPDATE employes SET name=%s, surname=%s, position=%s, company_id=%s "
                                        "WHERE id = %s",
                                  args=(name, surname, position, company_id, upd_id))
