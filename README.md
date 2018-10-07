This project is created for the sole purpose of learning.
It includes Generic API's(GET,POST,PATCH,DELETE) which carry out their respective operations of showing,creating,updating,deleting data from the database.

The Technologies used are : (a)Flask Microframework (b)Sqlite3 for database (c)HTML for basic frontend

FIRSTLY,CHANGE THE BELOW PATH OF DATABASE IN __init__.py WHICH CONTAINS THE MAIN CODE TO YOUR PATH app.config['SQLALCHEMY_DATABASE_URI']='sqlite:////Users/Kapil/Desktop/Kapil_Assignment/Kapil_Assignment/organization.db'
I HAVE CREATED A DB called organization.db WHICH CONTAINS SOME DUMMY VALUES FOR Employee_ID,First_name,Last_name,Device_ID

To run the project : 
(1) pip install flask flask-sqlalchemy 
(2) vitualenv for virtual environment
(3) set FLASK_APP=__init__.py (since I'm using windows)
(4) flask run
