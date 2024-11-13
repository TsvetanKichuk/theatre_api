# Theatre API

# Theatre API Project

## Project Description

The Theatre API Project is a web application designed to manage theatre performances, ticket reservations, and actors.
The backend is built with Django, and the API interface is implemented using Django REST Framework.

## Technology Stack

- **Backend:** Python 3.12.7, Django 4.x, Django REST Framework
- **Database:** PostgreSQL
- **Testing:** Django Test Framework
- **Others:** Click, Pillow, PyYAML, psycopg2, pyflakes, pytz

## Installation

### System Requirements

- Python 3.12.7
- PostgreSQL
- pip (Python package installer)

### Installation Steps

1. Clone the repository:
    ```bash
    git clone https://github.com/TsvetanKichuk/theatre_api
    cd theatre_api
    ```

2. Set up a virtual environment:
    ```in to the terminal
    python -m venv venv
    source venv/bin/activate  # For Windows: venv\Scripts\activate
    ```

3. Install the dependencies:
    ```in to the terminal
    pip install -r requirements.txt
    ```
4. Create .env file:
   set DB_HOST=<your db hostname>
   set DB_NAME=<your db name>
   set DB_USER=<your db username>
   set DB_PASSWORD=<your db user password>
   set SECRET_KEY=<your secret key>

5. Configure your database settings in `settings.py`:
    ```python
     DATABASES = {
     "default": {
         "ENGINE": "django.db.backends.postgresql",
         "NAME": os.environ["POSTGRES_DB"],
         "USER": os.environ["POSTGRES_USER"],
         "PASSWORD": os.environ["POSTGRES_PASSWORD"],
         "HOST": os.environ["POSTGRES_HOST"],
         "PORT": os.environ["POSTGRES_PORT"],
     }
 }
      ```

6. Apply migrations and load data:
    ```in to the terminal
    python manage.py migrate
   python manage.py loaddata theatre_db_data.json
    ```

7. Run the development server:
    ```in to the terminal
    python manage.py runserver
    ```

8. Create a superuser to access the admin panel:
    ```in to the terminal
    python manage.py createsuperuser
    ```
   # Getting access

<ul>
  <li>Create user via /api/user/register/</li>
  <li>Get access token via /api/user/token/</li>
</ul>

## Run with docker

## Docker should be installed

```shell
    docker build -t <your login name/name of image> .
    docker-compose up
```

## Usage

After starting the server, the interface is available at: `http://127.0.0.1:8000`.

### API Endpoints

Major endpoints for interacting with the application:

- `/api/theatre/genres/` - Manage genres
- `/api/theatre/actors/` - Manage actors
- `/api/theatre/theatre-halls/` - Manage theatre halls
- `/api/theatre/plays/` - Manage plays
- `/api/theatre/performances/` - Manage performances
- `/api/theatre/reservations/` - Manage reservations
- `/api/theatre/tickets/` - Manage tickets

### Swagger API
- `/api/doc/swagger/`

### Interface Screenshots

(https://github.com/user-attachments/assets/c66822fa-b78d-45d7-9654-612bf3623fe7)
(https://github.com/user-attachments/assets/13f44dce-a3df-4c78-afa8-aaa7d2917b25)
(https://github.com/user-attachments/assets/6cd01006-fe57-4af8-be2f-0b5f167e19d8)
(https://github.com/user-attachments/assets/e82ecd8d-1d23-4c1e-a3c3-c42d7099e8b1)
(https://github.com/user-attachments/assets/235d347a-9f57-4243-9a77-de94e54a94a2)
(https://github.com/user-attachments/assets/1781b1a8-751f-4a54-8556-9cf547e403e1)
(https://github.com/user-attachments/assets/10047968-2072-4a18-b531-5bc270a3c68e)
(https://github.com/user-attachments/assets/f87068e6-b855-4b6b-a4e0-c410c21627b0)
(https://github.com/user-attachments/assets/22abd945-9efd-4ded-bfdd-ef6d2c2902e2)

## Testing

To run tests, execute:

```in to the terminal
python manage.py test
```
