# Schemas project

Project for creating schemas and generating csv files with fake data according to the schemas  

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Installing

Create the project directory (for example 'schemas')
```
mkdir schemas
cd schemas
```

Clone the repository to this folder

```
git clone https://github.com/Vitamal/schemas
```

### Create a virtual environment to isolate our package dependencies locally
```
python3 -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
```

## Install dependencies

```
cd schemas
pip install -r requirements/develop.txt
```

## Now sync your database for the first time
```
python manage.py migrate
```
## Create an initial user named admin with a password ...

```
python manage.py createsuperuser --email admin@example.com --username admin
```

## Running the worker

...  celery -A schemas worker -l INFO

## Running the project

```
python manage.py runserver
```

## Create the schemas
In browser open http://127.0.0.1:8000/ 
Login.
Create schemas at your request.

## Generate csv files
Choose the scheme for generation and press 'generate' link.
Enter the rows' quantity to generate.
And press 'Generate data'.
then you can download file to look at the data.

## Built With

* [Django 3.1.3](https://pypi.org/project/Django/) - The web framework used
* [Python 3.8.5 ](https://www.python.org/doc/) 
* [redis 3.5.3](https://pypi.org/project/redis/)
* [celery 5.0.4](https://pypi.org/project/celery/)  
* [Faker 5.0.1](https://pypi.org/project/Faker/)
* [pip 20.2.4](https://pypi.org/project/pip/) - The tool for installing Python packages.
