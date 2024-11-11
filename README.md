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
(https://github.com/user-attachments/assets/c66822fa-b78d-45d7-9654-612bf3623fe7)
(https://github.com/user-attachments/assets/13f44dce-a3df-4c78-afa8-aaa7d2917b25)
(https://github.com/user-attachments/assets/6cd01006-fe57-4af8-be2f-0b5f167e19d8)
(https://github.com/user-attachments/assets/e82ecd8d-1d23-4c1e-a3c3-c42d7099e8b1)
(https://github.com/user-attachments/assets/235d347a-9f57-4243-9a77-de94e54a94a2)
(https://github.com/user-attachments/assets/1781b1a8-751f-4a54-8556-9cf547e403e1)
(https://github.com/user-attachments/assets/10047968-2072-4a18-b531-5bc270a3c68e)
(https://github.com/user-attachments/assets/f87068e6-b855-4b6b-a4e0-c410c21627b0)
(https://github.com/user-attachments/assets/22abd945-9efd-4ded-bfdd-ef6d2c2902e2)
