import typing

from server.database import handler, utils, obj
class DbOperator:
    def select_user(self, email: str, number: str) -> bool:
        handlerDb = handler.Db()
        select_email = handlerDb._select_with_email(email)
        select_number = handlerDb._select_with_number(number)
        if isinstance(select_email, tuple) and isinstance(select_number, tuple):
            return utils.DataOperator.create_json_with_id(select_number[-1])
        return False

    def select_user_info(self, id: int) -> typing.Tuple[str] or None:
        user_info = handler.Db()._select_user_info(id)
        if isinstance(user_info, tuple):
            return utils.DataOperator.create_json_db(user_info)
        return None

    def new_user(self, email: str, secret_key: str, public_name: str, phone_number: str):
        handler.Db()._insert_user(email, secret_key, public_name, phone_number)
        return self.select_user(email, phone_number)

    def create_task(self, from_id: int, to_id: int, title: str, text: str, is_secret: bool):
        task_id = handler.Db()._insert_task(from_id, to_id, text, title, is_secret, 0, 100)
        return utils.DataOperator.create_json_task_id(task_id)

    def update_task(self, task_id: int, from_id: int, to_id: int, title: str, text: str, is_secret: bool, progress_start, progress_end):
        task_id = handler.Db()._update_task(task_id, from_id, to_id, text, title, is_secret, progress_start, progress_end)
        return utils.DataOperator.create_json_task_id(task_id)

