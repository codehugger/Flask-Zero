Flask-Zero
==========

Flask-Zero is a Flask (Python microframework) template/bootstrap/boilerplace application.

The layout and code in this project is heavily influenced by projects like Fbone (https://github.com/imwilsonxu/fbone) and Flask-Empty (https://github.com/italomaia/flask-empty).

Why?
----

I felt that the other skeletons available for Flask did not provide a clear structure for dealing with assets and blueprints so I made my own :)


How?
----

You simply clone the project and remove the .git folder and start hacking away :)

Example on how to get started:

    $> git clone https://github.com/codehugger/Flask-Zero.git awesome_app
    $> cd awesome_app
    $> rm -rf .git

Then to install requirements and run

    $> pip install -r requirements.txt
    $> ./manage.py seed_db
    $> ./manage.py runserver


What?
-----

In this application skeleton I have included all the nuts and bolts that I find myself using for every single web application I write. They are (excluding Flask itself of course)

* Flask-SqlAlchemy
* Flask-Login
* Flask-Wtf
* Flask-Assets
* Flask-Testing
* Flask-Script
* py-bcrypt

The project itself is structured as follows

* **Flask-Zero**
    * **myapp** (holds the flask application itself)
      * **apps** (container for all blueprints)
         * **blog** (an example application blueprint with authentication requirements, less, javascript and templates)
      * **models** (your model files just remember to include your models in the __init__.py so you can reference them directly)
      * **static** (css, images, javascript and all their friends)
      * **templates** (the base templates e.g. signin.html and index.html)
      * **commands.py** (contains custom commands that can be used to register with Flask-Script)
      * **config.py** (contains default, development and testing configuration and most importantly your blueprint entry points)
      * **database.py** (contains database functions for creating, seeding and dropping)
      * **decorators.py** (contains custom decorators for myapp)
      * **extensions.py** (contains all extensions that are directly applied to the app instance like Flask-Login and Flask-Assets)
      * **forms.py** (contains common forms like the sign-in form)
      * **main.py** (contains the application factory i.e. app_factory)
    * **tests** (the tests duh!)
    * **manage.py** (the access point to myapp here you can run commands like runserver, createdb and shell)
