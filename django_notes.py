'''
1. Django: Python web framework for building interactive websites

2. Setting up a project:
	- To work with Django I need to set up a virtual environment
		- When the virtual environment is set up I can use it to install packages and isolate them from all other Python packages
		- Separating the libarires is beneficial when deploying the project to the server.
		- To set up the virtual environment (in Unix):
			> cd into the desired directory where the environment will be set up  
			> virtualenv -p python3 virtualenvname - this commands creates the virtual environment
			> source bin/activate - this command activates the virtual environment (I can also cd to bin and use source activate)
			> deactivate - exits the environment

	- After the virtual environment is active I can start working with Django
		- Before Django can be run, I must install it using the command: pip install Django
		- django-admin startproject projectname . - this command starts a new project with a specified project name
			> The dot at the end creates the new project with a directory structure
			> This makes it easier later to deploy the app to a server
			> when the command is run Django creates a directory with specified name and a manage.py file
			> manage.py takes in commands and runs them using Django
		- The directrory created using the startproject command contains four files:
			> settings.py - file controlling how Django interacts with the system and manages a project
			> urls.py - file telling Django which pages to build in response to browser requests
			> wsgi.py - file helping Dango serve the files it creates (wsgi = web server gateway interface)
			> asgi.py - file providing standard interface for asynchronous and synchronous apps [https://asgi.readthedocs.io/en/latest/]
		- Most of the project infromation is stored in a database, so one needs to be created first:
			> python manage.py migrate - the migrate command is used to modify a database (modifying the database = migrating the database)
			> when the migrate command is run for the first time Django creates a new Database
			> Django creates a db.sqlite3 file - a SQLite database running of a single file - very useful for simple apps

3. Viewing the project:
	- To check if the project was set up properly I can use the command: python manage.py runserver
		> The output should be (ignoring the comments): 
			Watching for file changes with StatReloader
			Performing system checks...

			System check identified no issues (0 silenced). # here Django checks if the project was set up properly 
			June 22, 2022 - 11:39:18
			Django version 4.0.5, using settings 'django_toolkit.settings' # here I can see the version of Django used, can differ in the future
			Starting development server at http://127.0.0.1:8000/ # this URL is where the project server is (the project listens for requests on port 8000 on my machine which is localhost)
			Quit the server with CONTROL-C.
		> localhost is a server that only processes requests on my system

4. Starting an app:
	- Apps in Django are components of the whole project
	- The apps work together to create the project
		> python manage.py startapp appname - creates directory and files needed to build an app
		> the appname directory contains several files used for building the app, including:
			models.py, admin.py, apps.py, tests.py, views.py
	
	- models.py file stores the data that will be managed in the app
		> A model tells Django how to handle and work with the data stored in the app
		> A model is just a class - has attributes and methods
		> To use models the app must be included in the overall project -> an app must be added to INSTALLED_APPS in settings.py
		> After that Django should also modify the database using the command: python manage.py makemigrations appname
		> This command uses Django to modify the database to store the data associated with new models defined
		> Then apply the migration using: python manage.py migrate
	- migrations algorithm:
		> modify models.py
		> python manage.py makemigrations appname
		> python manage.py migrate

5. Django Admin Site
	- Admin site allows the user to work easier with the models
	- Only the administrators can use the admin site (not general users)
	- Django has an option to create a superuser - a user with all privileges available on the site
	- python manage.py createsuperuser - creates a superuser
	- For the admin to be able to see created the models they need to be added in admin.py

6. Model Relationships
	- models will have relatioships between each other that define how they interact - like in databases
	- for example if I have a learning log with topics, one topic may have many entries -> many to one relationship
			but one entry will (should) have only one topic
	
7. Django Shell
	- The data entered on the website can be examined through an interactive terminal session
	- Django Shell helps greatly test and troubleshoot the project
	- the command to run it is: python manage.py shell

8. Making Pages
	- Making Pages in Django has 3 steps (can be done in any order preferable):
		> define URLs
		> write views
		> write templates
	- A URL pattern describes the way the URL is laid out -> tells Django what to look for when matching a browser request with a site URL
	- Each URL maps to a particular view -> view retrieves and processes the data needed for that page
	- view often renders the page using a template, which contains the overall structure of the page

	- Mapping a URL:
		> Users request pages by entering URLs into a browser and clicking links
		> I have to decide what URLs are needed
		> Usually the home page URL is first -> it is https://localhost:8000/ if nothing was modified
		> It is the base URL and returns default Django site
		> To change that base URL must be mapped to a desired page
	
	- Writing a View:
		> A view function takes requests and prepares data to generate a page, then sends it back
		> Often uses a template to define the look of a page
		> When a URL request matches a defined pattern Django looks for a specific function in views.py
			and runs that function with the request.
		> To build a page a template function can be used
	
	- Writing a Template:
		> Template = look of the page
		> First a folder must be created to store the templates
		> Templates can be written as HTML files
		> When building a webpage some elements will be common on all pages, so I can write a base template with
			repeating elements and then have each page inherit from the base
		> To accomplish that I can create a parent template that all pages will inherit from
X. Sources:
	- Python Crash Course, 2nd Edition by Eric Matthes
'''