import mysql.connector
from mysql.connector import Error

class repository_base:
    def connect():
        try:
            connection = mysql.connector.connect(
                host='localhost',
                database='locadora',
                user='root',
                password='root' 
            )

            if connection.is_connected():
                print("Conexão bem-sucedida ao MySQL")

                cursor = connection.cursor()
                
                cursor.execute("SELECT DATABASE();")
                db_info = cursor.fetchone()
                print(f"Conectado ao banco de dados: {db_info}")
                cursor.close();

            return connection;
        except Error as e:
            print(f"Erro ao conectar ao MySQL: {e}");