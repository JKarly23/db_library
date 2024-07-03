import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

try:
    dbname = os.getenv('dbname')
    user = os.getenv('user')
    password = os.getenv('password')
    host = os.getenv('host')
    port = os.getenv('port')

    connection = psycopg2.connect(
        dbname=dbname,
        user=user,
        password=password,
        host=host,
        port=port
    )

    cursor = connection.cursor()

except psycopg2.Error as e:
    print("Error al conectar a PostgreSQL:", e)
    connection = None
    cursor = None
