Notes on creating an app using Django Framework.

Python: 3.6.3
Django: 1.11.7
Intro to Django: https://www.djangoproject.com/
Web Framework: collections of tools used to make website.
	ORM (Object Relational Mapping): Help us build database queries.
	URL Logic
	HTML Templating
	Form Handling and Unit Testing
	pytz - supports time zone
Start Project: django-admin.py startproject DjangoWebApp
Files Created:
	manage.py - run commands					//First three files no need to edit
	__init__.py - contains python files
	wsgi.py - hook for web servers
	settings.py - configures Django
	urls.py - routes requests based on URL
Start the server: \DjangoWebApp>python manage.py runserver (on localhost port: 8000)
Start the app: python manage.py startapp adoptions
When adding a new Django app, settings.py needs to be edit. Look for installed apps and add 'adoptoions' (name of app) there.
Files Created:
	apps.py - configuration 
	models.py - database handling
	admin.py - administrative interface
	urls.py - url routing
	views.py - control flow and takes http requests as an argument and provide http response
	tests.py - unit testing
	migrations - hold migration files
Migration is needed when:
	1. Adding models
	2. Adding field
	3. Removing field
	4. Changing field
Make Migrations: python manage.py makemigrations
Show Migrations: python manage.py showmigrations
Migrate: python manage.py migrate
Add csv and management folder to the project
Run command to load Data into sqlLite Database: python manage.py load_arrest_data
Next will work with admin.py
Create superuser: python manage.py createsuperuser
Run project: python manage.py runserver then in browser: http://localhost:8000/admin
        
