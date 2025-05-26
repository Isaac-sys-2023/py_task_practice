from flask import Flask, jsonify, request
import routes
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.get("/api/tareas")
def get_tareas():
    data = routes.listadoTareas()

    respuesta = []
    for fila in data:
        respuesta.append({
            "id": fila[0],
            "titulo": fila[1],
            "contexto": fila[2],
            "autor": fila[3]
        })

    # return jsonify(data)
    return respuesta

@app.get("/api/tareas/<id>")
def get_tarea(id):
    data = routes.listarTarea(id)
    return jsonify(data)

@app.post("/api/tareas")
def post_tarea():
    tarea = request.json
    titulo = tarea.get("titulo")
    contexto = tarea.get("contexto")
    autor = tarea.get("autor")
    result = routes.guardarTarea(titulo, contexto, autor)
    return jsonify({"message": result})

@app.put("/api/tareas/<id>")
def put_tarea(id):
    tarea = request.json
    titulo = tarea.get("titulo")
    contexto = tarea.get("contexto")
    autor = tarea.get("autor")
    result = routes.actualizarTarea(id, titulo, contexto, autor)
    return jsonify({"message": result})

@app.delete("/api/tareas/<id>")
def delete_tarea(id):
    result = routes.eliminarTarea(id)
    return jsonify({"message": result})

@app.get("/")
def index():
    return "HI"

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5220, debug=True)
