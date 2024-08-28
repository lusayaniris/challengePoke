# API de Servicio de Pokémon

Este proyecto es una API basada en Flask para gestionar y obtener datos de bichitos Pokemon. Incluye varios endpoints para obtener información de los Pokemon, realizar autenticación y gestionar tokens JWT.

Este proyecto es parte de un desafío técnico y tiene como objetivo proporcionar un ejemplo de cómo construir una API RESTful con Flask, incluyendo autenticación y autorización con tokens JWT. Dicho esto, pretende ser una PoC y no se recomienda para entornos de producción sin una revisión y configuración adicional.

La fuente de datos para los Pokémon es un archivo JSON que contiene información sobre los Pokemon, incluyendo su nombre y tipo. Se hizo de esta manera para simplificar el proyecto y no depender de una base de datos externa o un servicio de terceros (como la API de Pokemon). Sin embargo, se puede extender fácilmente para utilizar una base de datos real o un servicio de terceros.

## Tecnologías Utilizadas

- Python 3
- Flask
- Flask-JWT-Extended
- Docker
- JSON
- RESTful API
- JWT
- Git
- Curl

## Tabla de Contenidos

- [Instalación](#instalación)
- [Configuración](#configuración)
- [Uso](#uso)
- [Endpoints](#endpoints)
- [Autenticación](#autenticación)
- [Ejecutando la Aplicación](#ejecutando-la-aplicación)
- [Ejecutando con Docker](#ejecutando-con-docker)
- [Contribuyendo](#contribuyendo)
- [Licencia](#licencia)

## Requisitos

Para ejecutar este proyecto, necesitarás tener instalado Python 3 y pip. Se recomienda utilizar un entorno virtual para instalar las dependencias del proyecto.
Sin embargo, no es necesario instalar Python 3 y pip si se ejecuta el proyecto con Docker. En ese caso, solo necesitarás Docker (versión 26.1.1 o superior).

Para verificar si tienes Python 3, pip y Docker instalados, ejecuta los siguientes comandos en tu terminal:

```bash
python3 --version
pip --version
docker --version
```

**Aclaración**: Git es necesario para clonar el repositorio, pero no es necesario para ejecutar el proyecto con Docker. Si no tienes Git instalado, puedes descargar el código fuente como un archivo ZIP desde GitHub. Asimismo, `curl` es necesario para realizar solicitudes HTTP a la API desde la línea de comandos (también puedes utilizar Postman u otra herramienta similar).


## Instalación

Para instalar y ejecutar este proyecto localmente, sigue estos pasos:

1. Clona el repositorio:

   ```bash
   git clone https://github.com/lusayaniris/challengePoke.git
   cd challengePoke
   ```

2. Crea un entorno virtual y actívalo:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Instala las dependencias necesarias:

   ```bash
   pip install -r requirements.txt
   ```

## Configuración

Las configuraciones para este proyecto se gestionan utilizando variables de entorno. El archivo `config.py` maneja estas configuraciones, con valores predeterminados si las variables de entorno no están configuradas.

- `SECRET_KEY`: La clave secreta para tu aplicación Flask.
- `JWT_SECRET_KEY`: La clave secreta para firmar tokens JWT.
- `TOKEN_EXPIRY_MINUTES`: La duración de los tokens JWT en minutos (por defecto, 60 minutos).

Puedes configurar estas variables de entorno en tu terminal:

```bash
export SECRET_KEY='tu_clave_secreta'
export JWT_SECRET_KEY='tu_jwt_clave_secreta'
export TOKEN_EXPIRY_MINUTES=1440 # 24 horas

# Opcional: Utiliza un valor aleatorio para SECRET_KEY y JWT_SECRET_KEY
export SECRET_KEY=$(cat /dev/urandom |head -c 18 |base64)
export JWT_SECRET_KEY=$(cat /dev/urandom |head -c 48 |base64)
```

**IMPORTANTE**: Para producción, es importante configurar estas variables de entorno de manera segura en lugar de depender de los valores predeterminados.

## Uso

Esta API proporciona una variedad de endpoints para interactuar con los datos de Pokemon, incluyendo el get de Pokemon por tipo, el get del Pokemon con el nombre más largo de una clase determinada, entre otras.

### Endpoints

- `POST /login`: Autentica a un usuario y devuelve un token JWT.
- `GET /pokemon/count`: Obtiene el número total de Pokemon en la fuente de datos.
- `GET /pokemon/types`: Recupera todos los tipos únicos de Pokémon.
- `GET /pokemon`: Recupera todos los datos de los Pokemon.
- `GET /pokemon/type/<name>`: Obtiene el(los) tipo(s) de un Pokémon por su nombre.
- `GET /pokemon/random`: Obtiene un Pokemon aleatorio de un tipo específico.
- `GET /pokemon/shortest-name`: Obtiene el Pokemon con el nombre más corto de un tipo especifico.
- `GET /pokemon/longest-name`: Obtiene el Pokemon con el nombre más largo de un tipo específico.
- `GET /pokemon/names/<poke_type>`: Obtiene todos los nombres de Pokémon de un tipo específico.

### Autenticación

La autenticación se maneja utilizando tokens JWT. Después de iniciar sesión a través del endpoint `/login`, se incluye este token JWT en el header `Authorization` de las solicitudes posteriores.

El token JWT tiene una duración de 60 minutos por defecto, pero esto se puede configurar en el archivo `config.py`.

Ejemplo:

```bash
# Iniciar sesión y obtener un token JWT (reemplaza 'admin' y 'password' con tus credenciales)
MY_TOKEN=$(curl -s -X POST http://127.0.0.1:5000/login -H "Content-Type: application/json" -d '{"username": "admin", "password": "password"}' |jq -r '.access_token')

# Utilizar el token JWT en las solicitudes posteriores con el siguiente header
Authorization: Bearer $MY_TOKEN
```

Esto solo se puede ejecutar después de iniciar la aplicación Flask y asegurarse de que el servidor esté en funcionamiento.

## Ejecutando la Aplicación

Para ejecutar la aplicación Flask:

```bash
python api_pokemon.py
```

Esto iniciará el servidor en `http://127.0.0.1:5000/` por defecto.

### Ejemplos de Uso

1. **Autenticar y obtener un token**:

   ```bash
   curl -X POST http://127.0.0.1:5000/login -d '{"username": "admin", "password": "password"}' -H "Content-Type: application/json"
   ```

   Esto devolverá un token JWT que puedes usar para solicitudes autenticadas. Este token debe incluirse en el header `Authorization` de las solicitudes posteriores.


2. **Obtener el conteo total de Pokémon**:

   ```bash
   curl -H "Authorization: Bearer <tu_jwt_token>" http://127.0.0.1:5000/pokemon/count
   ```

3. **Obtener el tipo de un Pokémon específico**:

   ```bash
   curl -H "Authorization: Bearer <tu_jwt_token>" http://127.0.0.1:5000/pokemon/type/Charmander
   ```

4. **Obtener un Pokémon aleatorio de un tipo específico**:

   ```bash
   # Utilizamos query params para especificar el tipo de Pokemon
   curl -H "Authorization: Bearer <tu_jwt_token>" "http://127.0.0.1:5000/pokemon/random?type=fire"
   ```

5. **Obtener el Pokémon con el nombre más corto de un tipo específico**:

   ```bash
   # Utilizamos query params para especificar el tipo de Pokemon
   curl -H "Authorization: Bearer <tu_jwt_token>" "http://127.0.0.1:5000/pokemon/shortest-name?type=fire"
   ```

6. **Obtener el Pokémon con el nombre más largo de un tipo específico**:

   ```bash
   # Utilizamos query params para especificar el tipo de Pokemon
   curl -H "Authorization: Bearer <tu_jwt_token>" "http://127.0.0.1:5000/pokemon/longest-name?type=fire"
   ```

7. **Obtener todos los nombres de Pokémon de un tipo específico**:

   ```bash
   curl -H "Authorization: Bearer <tu_jwt_token>" http://127.0.0.1:5000/pokemon/names/fire
   ```

## Ejecutando con Docker

Para ejecutar esta aplicación utilizando Docker, sigue los siguientes pasos:

1. **Crea la imagen Docker:**

   Asegúrate de que el archivo `Dockerfile` esté en el directorio raíz del proyecto. Luego, buildea la imagen utilizando Docker Compose:

   ```bash
   docker compose build
   ```

   Podemos crear la imagen Docker utilizando el comando `docker build` y luego ejecutar el contenedor con `docker run`, pero Docker Compose simplifica este proceso.

   ```bash
   # Buildeamos la imagen Docker.
   docker build -t api-pokemon .

   # Ejecutamos el contenedor Docker en modo detached (en segundo plano), mapeando el puerto 5000 al puerto 5000 del host y eliminando el contenedor después de detenerlo.
   docker run -d --rm -p 5000:5000 api-pokemon
   ```

2. **Inicia la aplicación:**

   Ejecuta el siguiente comando para iniciar la aplicación con Docker Compose:

   ```bash
   # Iniciar la aplicación con Docker Compose en primer plano
   docker compose up
   # Iniciar la aplicación con Docker Compose en segundo plano (en caso de que quieras liberar tu terminal)
   docker compose up -d
   ```

   Esto iniciará la aplicación Flask en un contenedor Docker y la hará accesible en `http://127.0.0.1:5000`.


3. **Parar la aplicación:**

   Para detener la aplicación y el container de Docker asociado, utiliza:

   ```bash
   docker compose down
   ```

### Ejemplos de Uso con Docker

Puedes utilizar los mismos comandos `curl` mencionados anteriormente para interactuar con la API cuando esté ejecutándose en Docker.

## Contribuciones

¡Las contribuciones son bienvenidas! Por favor, haz un fork del repositorio y envía un pull request con tus cambios.

## Licencia

Este proyecto está licenciado bajo la Licencia Apache. Consulta el archivo [LICENSE](https://www.apache.org/licenses/LICENSE-2.0.txt) para más detalles.