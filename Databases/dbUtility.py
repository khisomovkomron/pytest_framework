import psycopg2
import logging as logger


class DBUtility:

    def __init__(self, dbname, user, password):
        self.dbname = dbname
        self.user = user
        self.password = password
        # host - заглушка
        self.conn = psycopg2.connect(dbname=self.dbname, user=self.user,
                                     password=self.password, host='')
        self.cursor = self.conn.cursor()

    def create_connection(self):
        return self.cursor

    def execute_select(self, sql):
        conn = self.create_connection()

        try:
            logger.info(f"Executing: {sql}")
            conn.execute(sql)
            query = conn.fetchall()
            print(query)
            conn.close()
        except Exception as e:
            raise Exception(f'Failed running sql: {sql}, Error: {str(e)}')
        finally:
            conn.close()
        return query

    def update(self, sql):
        curr = self.create_connection()
        try:
            logger.info(f"Executing: {sql}")
            curr.execute(sql)
            # query = conn.fetchall()
            # print(query)
            self.conn.commit()
            curr.close()
        except Exception as e:
            raise Exception(f'Failed running sql: {sql}, Error: {str(e)}')
        finally:
            curr.close()
