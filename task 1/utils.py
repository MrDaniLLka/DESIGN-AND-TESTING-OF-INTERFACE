def get_info():
    print("""
    1 - Показать список всех компаний
    2 - Показать список всех сотрудников
    3 - Добавить нового сотрудника
    4 - Удалить сотрудника из базы
    5 - Изменить поля существующей записи сотрудника\n
    """)
    return

def get_id_company(con, comp_name: str):
    company_id = con.exec_select(f"SELECT id FROM companies WHERE name = %s", (comp_name,))

    if len(company_id) == 0:
        print('Такой компании нет!')
        return False
    else:
        return company_id[0]['id']

