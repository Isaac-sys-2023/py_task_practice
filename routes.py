from db import cadenaConexion

def listadoTareas():
    sql = "SELECT * FROM tarea"
    conn = cadenaConexion()
    cur = conn.cursor()
    cur.execute(sql)
    result = cur.fetchall()
    cur.close()
    conn.close()
    return result

def listarTarea(id):
    sql = "SELECT * FROM tarea WHERE id=%s"
    conn = cadenaConexion()
    cur = conn.cursor()
    cur.execute(sql,(id,))
    result = cur.fetchone()
    cur.close()
    conn.close()
    return result

def guardarTarea(titulo, contexto, autor):
    sql = "INSERT INTO tarea (titulo,contexto,autor) VALUES (%s,%s,%s)"
    conn = cadenaConexion()
    cur = conn.cursor()
    cur.execute(sql,(titulo,contexto,autor))
    conn.commit()
    cur.close()
    conn.close()
    return "Tarea creada exitosamente"

def actualizarTarea(id, titulo, contexto, autor):
    sql = "UPDATE tarea SET titulo=%s,contexto=%s,autor=%s WHERE id=%s"
    conn = cadenaConexion()
    cur = conn.cursor()
    cur.execute(sql,(titulo,contexto,autor,id))
    conn.commit()
    cur.close()
    conn.close()
    return "Tarea actualizada exitosamente"

def eliminarTarea(id):
    sql = "DELETE FROM tarea WHERE id=%s"
    conn = cadenaConexion()
    cur = conn.cursor()
    cur.execute(sql,(id,))
    conn.commit()
    cur.close()
    conn.close()
    return "Tarea eliminada exitosamente"