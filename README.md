# FavContent - Plataforma de gestión de contenido favorito

FavContent es una aplicación web desarrollada con Django que permite a los usuarios registrar y organizar su contenido favorito como libros, artículos y videos.

## Características principales

- **Sistema de autenticación**: Registro, inicio de sesión y gestión de perfiles de usuario
- **Gestión de contenido**: Crear, editar, ver y eliminar elementos (CRUD)
- **Organización**: Categorías y etiquetas para clasificar el contenido
- **Búsqueda avanzada**: Búsqueda global y filtros específicos por tipo de contenido
- **Interfaz responsiva**: Diseño adaptable a dispositivos móviles y de escritorio

## Requisitos previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- MySQL (opcional, puede usar SQLite)
- Conocimientos básicos de Django y entornos virtuales

## Instalación

1. Clonar el repositorio:
```bash
git clone https://github.com/tu-usuario/favcontent.git
cd favcontent
```

2. Crear un entorno virtual:
```bash
python -m venv venv
```

3. Activar el entorno virtual:
   - En Windows:
   ```bash
   venv\Scripts\activate
   ```
   - En macOS/Linux:
   ```bash
   source venv/bin/activate
   ```

4. Instalar dependencias:
```bash
pip install -r requirements.txt
```

5. Configurar la base de datos:
   - Para SQLite (por defecto), no se requiere configuración adicional
   - Para MySQL, ajustar los parámetros en `config/settings.py`

6. Ejecutar migraciones:
```bash
python manage.py migrate
```

7. Crear un superusuario:
```bash
python manage.py createsuperuser
```

8. Iniciar el servidor de desarrollo:
```bash
python manage.py runserver
```

9. Acceder a la aplicación: [http://localhost:8000](http://localhost:8000)

## Estructura del proyecto

```
favcontent/
│
├── apps/                  # Aplicaciones Django
│   ├── articles/          # Gestión de artículos
│   ├── authentication/    # Sistema de autenticación
│   ├── books/             # Gestión de libros
│   └── videos/            # Gestión de videos
│
├── config/                # Configuración del proyecto
│   ├── settings.py        # Configuración principal
│   ├── urls.py            # URLs principales
│   └── wsgi.py            # Configuración WSGI
│
├── core/                  # Funcionalidades compartidas
│   ├── mixins.py          # Mixins reutilizables
│   ├── urls.py            # URLs del núcleo
│   └── views.py           # Vistas compartidas
│
├── media/                 # Archivos subidos por los usuarios
│
├── static/                # Archivos estáticos
│   ├── css/               # Hojas de estilo
│   ├── js/                # Scripts de JavaScript
│   └── img/               # Imágenes
│
├── templates/             # Plantillas HTML
│   ├── base/              # Plantillas base
│   ├── authentication/    # Plantillas de autenticación
│   ├── books/             # Plantillas de libros
│   ├── articles/          # Plantillas de artículos
│   └── videos/            # Plantillas de videos
│
├── .gitignore             # Archivos ignorados por Git
├── manage.py              # Script de gestión de Django
├── README.md              # Documentación del proyecto
└── requirements.txt       # Dependencias del proyecto
```

## Uso

### Panel de administración

Accede al panel de administración en [http://localhost:8000/admin/](http://localhost:8000/admin/) con las credenciales del superusuario creado anteriormente.

### Gestión de contenido

1. **Libros**: Registra tus libros favoritos con título, autor, ISBN, género, año de publicación, etc.
2. **Artículos**: Guarda artículos interesantes con título, autor, fuente, fecha de publicación, etc.
3. **Videos**: Almacena videos con título, creador, plataforma, duración, categoría, etc.

## Contribución

Las contribuciones son bienvenidas. Para cambios importantes:

1. Haz un fork del repositorio
2. Crea una rama para tu característica (`git checkout -b feature/nueva-caracteristica`)
3. Realiza tus cambios y haz commit (`git commit -m 'Añadir nueva característica'`)
4. Envía tus cambios (`git push origin feature/nueva-caracteristica`)
5. Abre un Pull Request

## Licencia

Este proyecto está licenciado bajo [MIT License](LICENSE).
