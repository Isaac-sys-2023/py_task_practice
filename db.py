from psycopg2 import connect
from contextlib import contextmanager
from config import DB_CONFIG

def get_connection():
    conexion = connect(**DB_CONFIG)
    return conexion

@contextmanager
def get_cursor():
    conn = get_connection()
    cur = conn.cursor()
    try:
        # La palabra clave "yield" se utiliza para devolver una lista de valores de una función . A diferencia de la palabra clave "return", que detiene la ejecución de la función, la palabra clave "yield" continúa hasta el final de la función.
        yield cur
        conn.commit()
    except Exception as e:
        conn.rollback()
        # raise es una instrucción que se utiliza para lanzar una excepción de forma manual
        raise e
    finally:
        cur.close()
        conn.close()
