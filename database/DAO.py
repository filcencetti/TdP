from database.DB_connect import DBConnect

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
            result.append(row) # tip: salvare il risultato di ogni query in una lista di DBO

        cursor.close()
        conn.close()
        return result