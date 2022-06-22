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
		
Using Django:
	- django-admin: allows for more things than just starting a new project
	- python manage.py runserver: gives useful things about the project
	- python manage.py createsuperuser: creates a user with access to the admin
										// django creates a user that's in the database

Apps:
	- Apps in Django are components of the whole project - they hold code but they are not
		like the regular apps on the phones
	- python manage.py startapp appname: creates an app with designated name
		- each app should do a designated and separate thing -> should be narrow and focused
	- some files created in the app:
		- models.py: stores the data that will be managed in the app


X. Sources:
	-
'''