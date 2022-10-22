import typing

import psycopg2
from server.settings import database as setting

class Db:
    def __init__(self):
        self.connection = psycopg2.connect(user=setting.USER,
                                      password=setting.PASSWORD,
                                      host=setting.HOST,
                                      port=setting.PORT)
        self.cur = self.connection.cursor()
    def _select_with_email(self, email: str) -> typing.Tuple[str] or None:
        self.cur.execute("SELECT user_id FROM users WHERE email=%s", (email,))
        return self.cur.fetchone()

    def _select_with_number(self, number: str) -> typing.Tuple[str] or None:
        self.cur.execute("SELECT user_id FROM users WHERE phone_number=%s", (number,))
        return self.cur.fetchone()

    def _select_user_info(self, id: int) -> typing.Tuple[str] or None:
        self.cur.execute("SELECT * FROM users WHERE user_id=%s", (id,))
        return self.cur.fetchone()

    def new_user(self, email: str, secret_key: str, public_name: str, phone_number: str):
        self.cur.execute("INSERT INTO public.users(email, secret_key, public_name, phone_number) "
                         "VALUES (%s, %s, %s, %s)", (email, secret_key, public_name, phone_number,))
        self.connection.commit()

