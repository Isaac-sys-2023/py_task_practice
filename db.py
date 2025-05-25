from psycopg2 import connect

host = "localhost"
port = 5432
dbname = "pg_webtasks"
user = "postgres"
password = "postgres"

def cadenaConexion():
    conexion = connect(host=host, port=port, dbname=dbname, user=user, password=password)
    return conexion