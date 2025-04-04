# Guía de Contribución para FavContent

¡Gracias por tu interés en contribuir a FavContent! Este documento proporciona lineamientos y mejores prácticas para contribuir al proyecto.

## Código de Conducta

Al participar en este proyecto, aceptas respetar nuestro Código de Conducta. Esperamos que todos los contribuyentes creen un ambiente positivo y acogedor.

## ¿Cómo puedo contribuir?

### Reportar Bugs

Los bugs se rastrean como issues en GitHub. Para reportar un bug:

1. Usa el buscador de issues para verificar que el bug no ha sido reportado anteriormente.
2. Si no encuentras un issue abierto sobre el problema, crea uno nuevo.
3. Incluye un título claro y una descripción detallada, con toda la información relevante.

### Sugerir Mejoras

Las sugerencias de mejoras también se rastrean como issues en GitHub:

1. Usa el buscador de issues para verificar que la mejora no ha sido sugerida anteriormente.
2. Proporciona un título claro y una descripción detallada.
3. Explica por qué esta mejora sería útil para la mayoría de los usuarios.

### Pull Requests

1. Haz fork del repositorio y crea tu rama desde `main`.
2. Si has añadido código que debe ser probado, añade pruebas.
3. Si has cambiado APIs, actualiza la documentación.
4. Asegúrate de que todas las pruebas pasen.
5. Asegúrate de que tu código cumpla con el estilo de codificación del proyecto.
6. Envía un pull request!

## Estilo de Codificación

### Python

- Sigue la guía de estilo PEP 8
- Usa nombres de variables descriptivos
- Documenta tus funciones y clases usando docstrings
- Escribe comentarios para explicar código complejo

### HTML/CSS/JavaScript

- Usa 2 espacios para la indentación
- Escribe nombres de clases en minúsculas, usando guiones para separar palabras
- Mantén el CSS modular y reutilizable

## Pruebas

- Añade pruebas unitarias para todas las nuevas funcionalidades
- Ejecuta las pruebas localmente antes de enviar un pull request

## Documentación

- Actualiza la documentación para reflejar cualquier cambio en la API o funcionalidad

## Proceso de Revisión

El mantenedor del proyecto revisará tu pull request y puede sugerir cambios, mejoras o alternativas.

## Configuración de Desarrollo

### Instalación del Entorno de Desarrollo

```bash
# Clonar el repositorio
git clone https://github.com/tu-usuario/favcontent.git
cd favcontent

# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
# En Windows:
venv\Scripts\activate
# En macOS/Linux:
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt

# Instalar dependencias de desarrollo
pip install -r requirements-dev.txt

# Configurar base de datos
python manage.py migrate

# Crear usuario administrador
python manage.py createsuperuser
```

## Herramientas de Desarrollo Recomendadas

- VSCode con las extensiones Python y Django
- Django Debug Toolbar
- Black para formateo de código
- flake8 para linting
- pytest para pruebas

## Agradecimientos

¡Gracias por dedicar tu tiempo a contribuir a este proyecto! Tu ayuda es muy apreciada. 