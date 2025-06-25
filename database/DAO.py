from database.DB_connect import DBConnect
from model.data_transfer_object import DTO_name

class DAO():
    def __init__(self):
        pass

    @staticmethod
    def DAOfunction_name1():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """
                query
                """
        cursor.execute(query)

        for row in cursor:
            result.append(DTO_name(**row))

        cursor.close()
        conn.close()
        return result