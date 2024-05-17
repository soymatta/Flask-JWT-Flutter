# Proyecto de Backend Flask con SQLAlchemy y JWT

Este proyecto implementa un backend Flask con SQLAlchemy para la gestión de una base de datos MySQL y autenticación JWT.

## Configuración del Entorno

1. **Instalación de Python**: Asegúrate de tener Python instalado en tu sistema. Puedes descargarlo desde [python.org](https://www.python.org/).

2. **Configuración del Entorno Virtual**: Se recomienda crear un entorno virtual para este proyecto. Puedes hacerlo ejecutando los siguientes comandos:

   ```bash
   python -m venv venv
   source venv/bin/activate  # Para sistemas Unix
   # venv\Scripts\activate  # Para sistemas Windows
   ```

3. **Instalación de Dependencias**: Instala las dependencias necesarias ejecutando:

   ```bash
   pip install -r requirements.txt
   ```

## Configuración de la Base de Datos

1. **Configuración de MySQL**: Asegúrate de tener un servidor MySQL instalado y configurado en tu sistema o usa un servicio en la nube como [ClearDB](https://www.cleardb.com/).

2. **Configuración de la Base de Datos**: Define la URL de conexión a la base de datos en el archivo `config.py`:

   ```python
   SQLALCHEMY_DATABASE_URI = 'mysql://usuario:contraseña@localhost/nombre_base_de_datos'
   ```

## Ejecución de Migraciones de Base de Datos

1. **Inicialización de Migraciones**: Inicia las migraciones de base de datos ejecutando:

   ```bash
   flask db init
   ```

2. **Generación de Migraciones**: Genera las migraciones iniciales con el siguiente comando:

   ```bash
   flask db migrate -m "Migración inicial"
   ```

3. **Aplicación de Migraciones**: Aplica las migraciones a la base de datos ejecutando:

   ```bash
   flask db upgrade
   ```

## Ejecución del Servidor

Para ejecutar el servidor, simplemente corre el archivo `app.py`:

```bash
python app.py
```

## Endpoints Disponibles

- `/auth/login`: Ruta para el inicio de sesión y obtención del token JWT.
- `/auth/protected`: Ruta protegida que requiere un token JWT válido para acceder.

## Licencia

Este proyecto está bajo la licencia [MIT](LICENSE).
