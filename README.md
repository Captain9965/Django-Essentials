# Django:
A python-based framework, often referred to as a batteries framework since it provides built-in features for everything including Django Admin interface and a default database, SQLite 3..

Its architecture is based on the MVT (Model View Template) pattern. Brief description:

1. Model- 

    This is the interface to the data. It is responsible for maintaining data.Generally a database.
2. View - 
    
    This is the user interface that the user interacts with..could be HTML/CSS/Js or ninja files.
3. Template - 

    This consists of the static parts of the desired HTML output.

## The case for Django:
1. It is easy to switch databases in Django
2. Has a built in admin interface
3. It is a fully functional framework that requires nothing else.
4. Thousands of additional packages available.
5. Very scalable.
6. Widely used with a huge support community. Used by many popular companies like Mozilla,Instagram, Pintrest, Spotify, Youtube etc..

## Django features:
1. Versatility - can be used to build any type of web app and works well with pretty much any client-side framework.
2. Security - Since it has been engineered to make it simple to use, it automatically does the right things to make the web app secure. for example, it does not store passwords in cookies, but hashes them instead.
3. Django web nodes have no stored states. Hence, it scales well horizontally.
4. Portability- written in python, hence inherently cross-platform.

## When to use Django:
1. When one needs a secure single-page web app.
2. Developing a web app or api backend.
3. for rapid development of a web app
4. When one needs to deploy fast and scale according to needs.
5. offers the perfect ORM for working with databases 

## Project structure:

On initialization, the project folder contains the following files by default which is enough to create a single page application:
ie.

> 1. manage.py -<br>
This allows one to interact with the project via the command line like start the serve, sync the database..
> 2. __init__.py-<br>
This executes package-initialization code.
>3. settings.py- <br>
This contains all the application settings like the database configuration, to register any application we create, and location of static files etc.
>4. urls.py- <br>
Stores all the links to the project and functions to call.
>5. wsgi.py-<br>
Helps the application communicate with the web server.

## Creating a project in Linux or:

Open the terminal and create a virtual environment using:

`python3 -m venv venv`

Activate the virtual enviromnemt using:<br>
`. venv/bin/activate`<br>
Install Django:

`pip install django`<br>
Create a project:<br>
`django-admin startproject projectName`

## Creating an application:

For every functionality, an app can be created like a completely independent module via the following command:<br>
`python manage.py startapp appName`


Then register the app in `settings.py` under `INSTALLED_APPS` 

## Creating a Django app:

The advantages of a django app are :

1. They are reusable...they can be used with multiple objects
2. Multilple developers can work on multiple projects
3. Debugging and organization is simplified.
4. Has inbuilt features like admin page which reduces the effort of building the same from scratch..










