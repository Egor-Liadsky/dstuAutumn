import json
import typing


class DataOperator:
    @staticmethod
    def create_json_db(data):
        json_data = {'email': data[0],
                     'public_name': data[2],
                     "phone_number": data[3],
                     "user_id": data[4],
                     "is_moderator": data[5]}
        return json.dumps(json_data, ensure_ascii=False)

    @staticmethod
    def create_json_with_id(id):
        return json.dumps({'user_id': id}, ensure_ascii=False)

    @staticmethod
    def create_json_all_users(users):
        data = []
        for user in users:
            json_data = {'email': user[3],
                         'public_name': user[1],
                         "phone_number": user[0],
                         "user_id": user[4],
                         "is_moderator": user[5]}
            data.append(json_data)
        return json.dumps(data, ensure_ascii=False)

    @staticmethod
    def create_json_task_info(id):
        return json.dumps({'task_id':  list(map(lambda x: x[-1], id))}, ensure_ascii=False)

    @staticmethod
    def create_json_task_all_info(task_data: typing.List[tuple]):
        tasks = []
        for task in task_data:
            temp_task = {}
            temp_task.update(from_id=task_data[0])
            temp_task.update(to_id=task_data[1])
            temp_task.update(text=task_data[2])
            temp_task.update(is_secret=task_data[3])
            temp_task.update(progress_start=task_data[4])
            temp_task.update(progress_end=task_data[5])
            temp_task.update(title=task_data[6])
            temp_task.update(time_start=task_data[7])
            temp_task.update(time_end=task_data[8])
            temp_task.update(task_id=task_data[9])
            tasks.append(temp_task)
        return json.dumps(tasks, ensure_ascii=False)

    @staticmethod
    def create_json_del_task(is_like):
        return json.dumps({'responce': is_like}, ensure_ascii=False)