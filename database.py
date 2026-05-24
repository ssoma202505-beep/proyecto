from dotenv import load_dotenv
import os
import mysql.connector

# cargar .env
load_dotenv()

def conectar_mysql():

    conexion = mysql.connector.connect(
        host=os.getenv("MYSQL_HOST"),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        database=os.getenv("MYSQL_DATABASE"),
        port=3306
    )

    return conexion
