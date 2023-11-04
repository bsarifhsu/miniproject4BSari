### INF601 - Advanced Programming with Python
#### Bunyamin Sari
#### miniproject4BSari

## Description
This project will be using Django to deploy a small web app of your choice. The goal here is to come up with a small web application.

## Pip Install Instructions
Please run the following: 
```
pip install -r requirements.txt
```
## Create SQL entries for the database
This will create any SQL entries that need to go into the database. In a terminal windows, please type the following:
```
python manage.py makemigrations
```
## Apply the Migrations
This will apply the migrations. In a terminal windows, please type the following:
```
python manage.py migrate
```
## Create Super User
This will create the administrator login for your /admin side of your project. In a terminal windows, please type the following:
```
python manage.py createsuperuser
```
## How to run
In a terminal windows, please type the following:
```
python manage.py runserver
```








python manage.py makemigrations (this will create any SQL entries that need to go into the database)
python manage.py migrate (this will apply the migrations)
python manage.py createsuperuser (this will create the administrator login for your /admin side of your project)
