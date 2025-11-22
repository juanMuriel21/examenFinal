
=======
# Biblioteca Escolar API

API REST para gestionar libros usando Django + DRF.

## Instalación
1. Clona el repo y activa el entorno virtual.
2. Instala dependencias: `pip install -r requirements.txt` (crea este archivo con `pip freeze > requirements.txt`).
3. Ejecuta migraciones: `python manage.py migrate`.
4. Ejecuta pruebas: `pytest` o `python manage.py test`.
5. Inicia servidor: `python manage.py runserver`.

## Endpoints
- GET/POST /api/libro/ (list/create)
- GET/PUT/PATCH/DELETE /api/libro/{id}/ (retrieve/update/delete)
- Filtrado: ?author=Nombre
- Paginación: 10 por página.

