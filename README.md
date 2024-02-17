# my-django-app
My first web application using django framework.

## Installing important dependencies.
- Create virtual environment in Python.
    ```python3 -m venv venv```
- Activate the virtual environment. 
   For macOS / Linux: ```source venv/bin/activate```
   For Windows: ```.\venv\Scripts\activate```
  
## Django Dependencies
- Create virtual environment and install django:
    ```pipenv install django```
    ```pipenv shell```
- Another way to create pipenv environment:
    ```pipenv --python 3.x```

- Start the django project: 
    ```django-admin startproject .```

- Run the server with Django:
    ```python manage.py runserver```
    
- To turn off pipenv: 
    ```pipenv --rm```