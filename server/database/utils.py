import json
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
    def create_json_task_id(id):
        return json.dumps({'task_id': id}, ensure_ascii=False)

    @staticmethod
    def create_json_task_info(task_data):
        return json.dumps({'task_id': id}, ensure_ascii=False)