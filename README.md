# Blog CRUD Django

## 📘 Descripción

Este proyecto es una aplicación web sencilla de blog construida con **Django 6.0.4**. Permite realizar operaciones CRUD sobre artículos, además de manejar autenticación básica de usuarios con inicio de sesión y registro.

El proyecto está organizado en 3 apps principales:

- `newspaper`: gestión de los artículos.
- `signup`: registro de nuevos usuarios.
- `base_project`: configuración global de Django.

También utiliza un esquema de templates centralizado en `templates/` y un archivo de estilos estáticos en `static/css/style.css`.

---

## 🚀 Características principales

- Listado de artículos
- Detalle de artículo
- Creación de artículo
- Actualización de artículo
- Eliminación de artículo
- Registro de usuario
- Inicio/Cierre de sesión
- Autenticación basada en el sistema de usuarios de Django

---

## 🧱 Estructura del proyecto

```
blog-crud-abr-2026/
├── base_project/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── newspaper/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── migrations/
├── signup/
│   ├── views.py
│   └── urls.py
├── static/
│   └── css/style.css
├── templates/
│   ├── _base.html
│   ├── articles.html
│   ├── article-detail.html
│   ├── article-create.html
│   ├── article-update.html
│   ├── article-delete.html
│   └── registration/
│       ├── login.html
│       └── signup.html
├── db.sqlite3
├── manage.py
└── requirements.txt
```

---

## ⚙️ Configuración principal

### `base_project/settings.py`

- `DEBUG = True`
- Base de datos: **SQLite** (`db.sqlite3`)
- Apps instaladas:
  - `django.contrib.admin`
  - `django.contrib.auth`
  - `django.contrib.contenttypes`
  - `django.contrib.sessions`
  - `django.contrib.messages`
  - `django.contrib.staticfiles`
  - `newspaper`
- Rutas de templates: `BASE_DIR / 'templates'`
- Rutas de archivos estáticos: `BASE_DIR / 'static'`
- Redirecciones de sesión:
  - `LOGIN_REDIRECT_URL = 'article-list'`
  - `LOGOUT_REDIRECT_URL = 'article-list'`

---

## 📦 Dependencias

El proyecto usa estas dependencias principales definidas en `requirements.txt`:

- `asgiref==3.11.1`
- `Django==6.0.4`
- `sqlparse==0.5.5`

> Si no existe `requirements.txt` en UTF-8, asegúrate de abrirlo con el editor adecuado o recrearlo correctamente.

---

## 🏗️ Modelo principal

### `newspaper/models.py`

Modelo `Article` con campos:

- `title` (CharField, 200)
- `content` (TextField)
- `author` (ForeignKey a `auth.User`)
- `created_at` (DateTimeField auto ahora)
- `published_date` (DateTimeField auto ahora)

También presenta:

- `__str__()` para mostrar el título
- `get_absolute_url()` para redirigir al detalle de artículo después de crear/editar

---

## 🌐 URLs principales

### `base_project/urls.py`

- `admin/` → panel de administración de Django
- `''` → incluye rutas de `newspaper`
- `accounts/` → rutas de autenticación de Django
- `accounts/` → rutas de la app `signup`

### `newspaper/urls.py`

- `/` → `article-list`
- `/articulos/<pk>/` → `article-detail`
- `/articulos/nuevo/` → `article-create`
- `/articulos/<pk>/editar/` → `article-update`
- `/articulos/<pk>/eliminar/` → `article-delete`

### `signup/urls.py`

- `accounts/signup/` → `signup`

---

## 🧠 Vistas principales

### `newspaper/views.py`

- `ArticleListView`: lista artículos con template `articles.html`
- `ArticleDetailView`: muestra detalle con `article-detail.html`
- `ArticleCreateView`: crea artículos con `article-create.html`
- `ArticleUpdateView`: edita artículos con `article-update.html`
- `ArticleDeleteView`: elimina artículos con `article-delete.html`

### `signup/views.py`

- `SignUpView`: registra nuevos usuarios con `registration/signup.html`

---

## 🎨 Templates y diseño

Los templates están centralizados en `templates/`.

### Layout principal
- `_base.html`: estructura base compartida

### Gestión de artículos
- `articles.html`
- `article-detail.html`
- `article-create.html`
- `article-update.html`
- `article-delete.html`

### Autenticación
- `registration/login.html`
- `registration/signup.html`

---

## 🧪 Uso local

1. Crear y activar un entorno virtual:

```bash
python -m venv .venv
.venv\Scripts\activate
```

2. Instalar dependencias:

```bash
pip install -r requirements.txt
```

3. Ejecutar migraciones:

```bash
python manage.py migrate
```

4. Crear un usuario administrador (opcional):

```bash
python manage.py createsuperuser
```

5. Ejecutar el servidor:

```bash
python manage.py runserver
```

6. Abrir en el navegador:

```text
http://127.0.0.1:8000/
```

---

## 🔐 Rutas de autenticación

- `accounts/login/`: iniciar sesión
- `accounts/logout/`: cerrar sesión
- `accounts/signup/`: registro de usuario

---

## 💡 Notas

- El proyecto utiliza **SQLite** para desarrollo.
- `newspaper` es la app responsable de los artículos.
- `signup` maneja únicamente el registro de usuarios.
- La plantilla base debe cargarse en cada página para mantener el diseño coherente.

---

## 📌 Recomendaciones

- Cambia `DEBUG = False` antes de desplegar en producción.
- Protege la clave `SECRET_KEY` en un archivo de entorno o en variables de entorno.
- Revisa `signup/urls.py` si deseas completar o mejorar su configuración.

---

## 🧩 Comandos rápidos

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

---

## ✅ Estado actual

- CRUD de artículos funcionando
- Registro de usuario disponible
- Login y logout disponibles
- Base de datos SQLite incluida
- Templates organizados para cada vista principal
