from database.DB_connect import DBConnect
from model.data_transfer_object import DTO_name

class DAO():
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
            result.append(DTO_name(**row)) # tip: salvare il risultato di ogni query in una lista di DTO

        cursor.close()
        conn.close()
        return result