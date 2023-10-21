from entities import Company, Employee
from base import Session
from utils import get_info, warning



if __name__ == '__main__':
    session = Session()
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
            for company in session.query(Company).all():
                print(company.name)
        if status == 2:
            for employee in session.query(Employee).all():
                print(employee.id, employee.name, employee.surname)
        if status == 3:
            name = input('Имя:')
            surname = input('Фамилия:')
            position = input('Должность:')
            company = input('Компания:')
            company_id = session.query(Company).filter(Company.name == company).all()[0].id
            print(company_id)
            if not company_id:
                warning()
                continue
            else:
                session.add(Employee(name, surname, position, company_id))
                session.commit()

        if status == 4:
            del_id = input('Введите id пользователя для его удаления:')
            if del_id.isdigit():
                if session.query(Employee).filter(Employee.id == del_id).count():
                    session.query(Employee).filter(Employee.id == del_id).delete()
                else:
                    warning()
            else:
                warning()

        if status == 5:
            upd_id = input('Введите id пользователя для его изменения:')
            if upd_id.isdigit() and session.query(Employee).filter(Employee.id == upd_id).count():#userRep.exist(upd_id):
                name = input('Имя:')
                surname = input('Фамилия:')
                position = input('Должность:')
                company = input('Компания:')
                company_id = session.query(Company).filter(Company.name == company).all()[0].id#compRep.get_id(company)
                if not company_id:
                    warning()
                    continue
                else:
                    record_to_update = session.query(Employee).filter_by(id=upd_id).first()
                    record_to_update.name = name
                    record_to_update.surname = surname
                    record_to_update.position = position
                    record_to_update.company = company
                    record_to_update.company_id = company_id
                    session.commit()
