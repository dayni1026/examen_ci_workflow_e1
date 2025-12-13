import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"API de Tareas" in response.data

def test_health(client):
    response = client.get('/health')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'healthy'

def test_get_tasks(client):
    response = client.get('/tasks')
    assert response.status_code == 200
    data = response.get_json()
    assert 'tasks' in data
    assert len(data['tasks']) >= 0

def test_get_task_success(client):
    response = client.get('/tasks/1')
    assert response.status_code == 200
    data = response.get_json()
    assert data['id'] == 1

def test_get_task_not_found(client):
    response = client.get('/tasks/9999')
    assert response.status_code == 404
    data = response.get_json()
    assert 'error' in data

def test_create_task(client):
    new_task = {"title": "Nueva tarea", "completed": False}
    response = client.post('/tasks', json=new_task)
    assert response.status_code == 201
    data = response.get_json()
    assert data['title'] == "Nueva tarea"
    assert 'id' in data

def test_create_task_without_title(client):
    response = client.post('/tasks', json={})
    assert response.status_code == 400
    data = response.get_json()
    assert 'error' in data

def test_update_task(client):
    update_data = {"title": "Tarea actualizada", "completed": True}
    response = client.put('/tasks/1', json=update_data)
    assert response.status_code == 200
    data = response.get_json()
    assert data['title'] == "Tarea actualizada"
    assert data['completed'] == True

def test_update_task_not_found(client):
    response = client.put('/tasks/9999', json={"title": "Test"})
    assert response.status_code == 404

def test_delete_task(client):
    response = client.delete('/tasks/2')
    assert response.status_code == 200
    data = response.get_json()
    assert 'message' in data

def test_delete_task_not_found(client):
    response = client.delete('/tasks/9999')
    assert response.status_code == 404
