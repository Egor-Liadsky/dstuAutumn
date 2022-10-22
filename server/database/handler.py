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

    def _insert_user(self, email: str, secret_key: str, public_name: str, phone_number: str):
        self.cur.execute("INSERT INTO public.users(email, secret_key, public_name, phone_number) "
                         "VALUES (%s, %s, %s, %s)", (email, secret_key, public_name, phone_number,))
        return self.connection.commit()

    def _insert_task(self, from_id, to_id, text, title, is_secret, progress_start, progress_end, time_start, time_end):
        sql = """INSERT INTO public.task(
        from_id, to_id, text, is_secret, progress_start, progress_end, title, time_start, time_end)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING task_id"""
        self.cur.execute(sql, (from_id, to_id, text, is_secret, progress_start, progress_end, title, time_start, time_end))
        self.connection.commit()
        return self.cur.fetchone()

    def _update_task(self, task_id, from_id, to_id, text, title, is_secret, progress_start, progress_end, time_start, time_end):
        sql = """UPDATE public.task
        SET from_id=%s, to_id=%s, text=%s, is_secret=%s, progress_start=%s, progress_end=%s, title=%s time_start=%s, time_end=%s
        WHERE task_id=%s"""
        self.cur.execute(sql, (from_id, to_id, text, is_secret, progress_start, progress_end, title, task_id, time_start, time_end))
        self.connection.commit()
        return task_id


