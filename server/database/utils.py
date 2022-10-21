import json
class DataOperator:
    @staticmethod
    def create_json_db(data):
        json_data = {'email': data[0],
                     'public_name': data[2],
                     "phone_number": data[3],
                     "user_id": data[4]}
        return json.dumps(json_data, ensure_ascii=False)

    @staticmethod
    def create_json_with_id(id):
        json_data = {'user_id': id}
        return json.dumps(json_data, ensure_ascii=False)