# API de Tareas - Proyecto de Examen

API REST simple en Python/Flask para gestión de tareas.

## Descripción

Esta es una API de ejemplo para un examen de GitHub Actions. Proporciona endpoints básicos para operaciones CRUD sobre tareas.

## Endpoints

- `GET /` - Mensaje de bienvenida
- `GET /health` - Health check
- `GET /tasks` - Obtener todas las tareas
- `GET /tasks/<id>` - Obtener una tarea específica
- `POST /tasks` - Crear una nueva tarea
- `PUT /tasks/<id>` - Actualizar una tarea
- `DELETE /tasks/<id>` - Eliminar una tarea

## Instalación Local

```bash
# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Configurar variables de entorno
cp .env.example .env
# Edita .env con tus valores

# Ejecutar la aplicación
python app.py
```

La API estará disponible en `http://localhost:5000`

## Ejecutar Tests

```bash
pytest
```

## Estructura del Proyecto

```
.
├── app.py              # Aplicación Flask
├── test_app.py         # Tests unitarios
├── requirements.txt    # Dependencias
├── pytest.ini         # Configuración de pytest
├── EXAMEN.md          # Instrucciones del examen
└── README.md          # Este archivo
```

## Para Estudiantes

Lee las instrucciones completas en [EXAMEN.md](EXAMEN.md)
