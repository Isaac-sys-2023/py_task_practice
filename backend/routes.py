from db import get_cursor

def listadoTareas():
    sql = "SELECT * FROM tarea"
    with get_cursor() as cur:
        cur.execute(sql)
        return cur.fetchall()

def listarTarea(id):
    sql = "SELECT * FROM tarea WHERE id=%s"
    with get_cursor() as cur:
        cur.execute(sql, (id,))
        return cur.fetchone()

def guardarTarea(titulo, contexto, autor):
    sql = "INSERT INTO tarea (titulo,contexto,autor) VALUES (%s,%s,%s)"
    with get_cursor() as cur:
        cur.execute(sql, (titulo, contexto, autor))
        return "Tarea creada exitosamente"

def actualizarTarea(id, titulo, contexto, autor):
    sql = "UPDATE tarea SET titulo=%s,contexto=%s,autor=%s WHERE id=%s"
    with get_cursor() as cur:
        cur.execute(sql, (titulo, contexto, autor, id))
        return "Tarea actualizada exitosamente"

def eliminarTarea(id):
    sql = "DELETE FROM tarea WHERE id=%s"
    with get_cursor() as cur:
        cur.execute(sql, (id,))
        return "Tarea eliminada exitosamente"