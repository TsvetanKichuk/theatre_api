# Theatre API
API service for theatre management written on DRF
## Installing using GitHub
Install PostgresSQL and create db
```shell
    git clone https://github.com/TsvetanKichuk/theatre_api
    cd cinema_API
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    python manage.py loaddata theatre_db_data.json
    set DB_HOST=<your db hostname> 
    set DB_NAME=<your db name> 
    set DB_USER=<your db username> 
    set DB_PASSWORD=<your db user password> 
    set SECRET_KEY=<your secret key> 
    python manage.py migrate 
    python manage.py runserver
```
# Run with docker
## Docker should be installed
```shell
    docker build -t <your login name/name of image> .
    docker-compose up
```
# Getting access 
<ul>
  <li>create user via /api/user/register/</li>
  <li>Get access token via /api/user/token/</li>
</ul>
