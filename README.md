# Equipos de Fútbol API - Flask + Docker

Este proyecto corresponde a la Actividad 4 - Unidad IV de la asignatura **Desarrollo Web**. Es una API RESTful desarrollada con **Flask** (Python), conectada a una base de datos **PostgreSQL** y ejecutada en un entorno **contenerizado con Docker Compose**.



##  Requisitos

- Tener instalado **Docker y Docker Compose**
- Puerto 5000 libre en tu máquina local



##  Cómo ejecutar el proyecto

1. Clonar este repositorio:

```bash
git clone https://github.com/MartinEGomez/equiposapp_flask.git
cd equiposapp_flask
```

2. Ejecutar Docker Compose:

```bash
docker-compose up --build
```

3. Abrir Postman o el navegador y acceder a:

```
http://localhost:5000/equipos
```



##  Endpoints disponibles (API REST)

| Método | Ruta               | Descripción                   |
|--------|--------------------|-------------------------------|
| GET    | /equipos           | Listar todos los equipos      |
| GET    | /equipos/:id       | Obtener equipo por ID         |
| POST   | /equipos           | Crear nuevo equipo            |
| PUT    | /equipos/:id       | Actualizar equipo por ID      |
| DELETE | /equipos/:id       | Eliminar equipo por ID        |

---

##  Pruebas con Postman

Importar esta colección en Postman:

 `EquiposFutbol_API.postman_collection.json`





##  Estructura del proyecto

```
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
├── config.py
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── run.py
```

---

##  Acceso base de datos (contenedor PostgreSQL)

- Usuario: `postgres`
- Contraseña: `martin123`
- Base de datos: `equiposdb`

---

##  Autor

Martín Gómez Contreras
Ingeniería de Software
