from dotenv import load_dotenv
import os
import mysql.connector

# Cargar variables del .env
load_dotenv()

def conectar_mysql():

    conexion = mysql.connector.connect(
        host=os.getenv("MYSQL_HOST"),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        database=os.getenv("MYSQL_DATABASE"),
        port=os.getenv("MYSQL_PORT")
    )

    return conexion