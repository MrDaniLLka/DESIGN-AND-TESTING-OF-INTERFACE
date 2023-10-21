from connection import Connection


class UserRepository:
    def update(self, *args):
        con = Connection()
        con.exec_edit(query="UPDATE employes SET name=%s, surname=%s, position=%s, company_id=%s "
                            "WHERE id = %s",
                      args=(args))
        con.close()

    def delete(self, del_id: int):
        con = Connection()
        con.exec_edit("DELETE FROM employes WHERE id = %s", (del_id,))
        con.close()

    def exist(self, id):
        con = Connection()
        res = con.exec_select("SELECT * FROM employes WHERE id = %s", (id,))
        con.close()
        return bool(len(res))

    def get_all(self):
        con = Connection()
        res = con.exec_select("SELECT id, name, surname FROM employes")
        con.close()
        return res

    def add(self, *args):
        con = Connection()
        con.exec_edit("INSERT INTO employes(name, surname, position, company_id) VALUES (%s, %s, %s, %s)", args)
        con.close()


class CompanyRepository:
    def get_id(self, comp_name: str):
        con = Connection()
        res = con.exec_select(f"SELECT id FROM companies WHERE name = %s", (comp_name,))
        con.close()
        if not len(res):
            return 0
        return res[0]['id']

    def get_all(self):
        con = Connection()
        res = con.exec_select("SELECT name FROM companies")
        con.close()
        return res
