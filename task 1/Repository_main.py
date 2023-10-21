from utils import get_info, warning
from repositories import UserRepository, CompanyRepository
import sqlalchemy 

if __name__ == '__main__':
    userRep = UserRepository()
    compRep = CompanyRepository()
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
            for company in compRep.get_all():
                print(company['name'])
        if status == 2:
            for employee in userRep.get_all():
                print(employee['id'], employee['name'], employee['surname'])
        if status == 3:
            name = input('Имя:')
            surname = input('Фамилия:')
            position = input('Должность:')
            company = input('Компания:')
            company_id = compRep.get_id(company)
            if not company_id:
                warning()
                continue
            else:
                userRep.add(name, surname, position, company_id)

        if status == 4:
            del_id = input('Введите id пользователя для его удаления:')
            if del_id.isdigit():
                if userRep.exist(int(del_id)):
                    userRep.delete(int(del_id))
                else:
                    warning()
            else:
                warning()

        if status == 5:
            upd_id = input('Введите id пользователя для его изменения:')
            if upd_id.isdigit() and userRep.exist(upd_id):
                name = input('Имя:')
                surname = input('Фамилия:')
                position = input('Должность:')
                company = input('Компания:')
                company_id = compRep.get_id(company)
                if not company_id:
                    warning()
                    continue
                else:
                    userRep.update(name, surname, position, company_id, upd_id)
