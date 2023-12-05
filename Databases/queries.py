from Databases.dbUtility import DBUtility
import random


class Queries(DBUtility):

    def __init__(self, stand: str, dbname, user, password):
        super().__init__(dbname, user, password)
        self.stand = stand

    def create_connection_to_db_by_stand(self):
        """Создание подключения к бд в зависимости от выбранного стенда"""
        if self.stand == 'dev':
            db = DBUtility(dbname=DBNAME_DEV, user=USER_DEV, password=PASS_DEV)
        elif self.stand == 'stage':
            db = DBUtility(dbname=DBNAME_STAGE, user=USER_STAGE, password=PASS_STAGE)
        elif self.stand == 'prod':
            db = DBUtility(dbname=DBNAME_PROD, user=USER_PROD, password=PASS_PROD)
        else:
            db = DBUtility(dbname=DBNAME_DEV, user=USER_DEV, password=PASS_DEV)

        return db

    def get_customer_by_email(self, email):

        sql = f"SELECT * FROM local.wp_users WHERE user_email='{email}';"
        rs_sql = self.db_helper.execute_select(sql)

        return rs_sql

    def get_random_customer_from_db(self, qty=1):

        sql = "SELECT * FROM local.wp_users ORDER BY ID DESC LIMIT	5000;"
        rs_sql = self.db_helper.execute_select(sql)

        return random.sample(rs_sql, int(qty))


