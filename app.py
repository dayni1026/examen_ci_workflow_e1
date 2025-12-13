from flask import Flask, jsonify, request
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key')
app.config['ENV_MODE'] = os.getenv('ENV_MODE', 'development')

# Base de datos en memoria
tasks = [
    {"id": 1, "title": "Completar examen", "completed": False},
    {"id": 2, "title": "Estudiar GitHub Actions", "completed": True}
]

@app.route('/')
def home():
    return jsonify({
        "message": "API de Tareas - Examen GitHub Actions",
        "environment": app.config['ENV_MODE']
    })

@app.route('/health')
def health():
    return jsonify({"status": "healthy"}), 200

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({"tasks": tasks}), 200

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((t for t in tasks if t["id"] == task_id), None)
    if task:
        return jsonify(task), 200
    return jsonify({"error": "Tarea no encontrada"}), 404

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    if not data or 'title' not in data:
        return jsonify({"error": "Título requerido"}), 400

    new_task = {
        "id": len(tasks) + 1,
        "title": data['title'],
        "completed": data.get('completed', False)
    }
    tasks.append(new_task)
    return jsonify(new_task), 201

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = next((t for t in tasks if t["id"] == task_id), None)
    if not task:
        return jsonify({"error": "Tarea no encontrada"}), 404

    data = request.get_json()
    task['title'] = data.get('title', task['title'])
    task['completed'] = data.get('completed', task['completed'])
    return jsonify(task), 200

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    task = next((t for t in tasks if t["id"] == task_id), None)
    if not task:
        return jsonify({"error": "Tarea no encontrada"}), 404

    tasks = [t for t in tasks if t["id"] != task_id]
    return jsonify({"message": "Tarea eliminada"}), 200

if __name__ == '__main__':
    app.run(debug=True)
