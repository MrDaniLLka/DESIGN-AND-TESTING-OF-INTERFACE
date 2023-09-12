import psycopg2
import psycopg2.extras


class Connection:
    def __init__(self, dbname='test', user='postgres', password='admin', port=5432):
        self.connection = None
        self.dbname = dbname
        self.user = user
        self.password = password
        self.port = port

    def exec_select(self, query: str, args=None):
        self.connection = psycopg2.connect(database=self.dbname,
                                           user=self.user,
                                           password=self.password,
                                           port=self.port)
        cursor = self.connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        if args:
            cursor.execute(query, args)
        else:
            cursor.execute(query)

        return cursor.fetchall()

    def exec_edit(self, query: str,  args: tuple):
        self.connection = psycopg2.connect(database=self.dbname,
                                           user=self.user,
                                           password=self.password,
                                           port=self.port)
        cursor = self.connection.cursor()
        cursor.execute(query, args)
        self.connection.commit()
        self.close()


    def close(self):
        self.connection.close()
