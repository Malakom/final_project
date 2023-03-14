<center><h1>![img.png](img.png)</h1></center>
------------------------------------------------------------------------
------------------------------------------------------------------------
![tr](/static/tr.jpeg)<br>
_“The world is a book and those who do not travel read only one page.”

**Malak Mahameed**
__________________________________________________________________________________
This Flask application allows users to view the countries i visited  <br>Users can share his adventure add,update or delete in the details .



## Installation

1. Install the required packages: Flask , flask-sqlalchemy ,Flask-Migrate in my python project
2. Import the modules we need: Flask, render_template, request, redirect, url_for,Migrate, migrate,SQLAlchemy,os and webbrowser
3. Create the database and import the sample data 
4. Update the database configuration in the `config.py` file
5. Run the application: `python app.py`

## Usage

- Run the application by executing `python app.py`
- Open a web browser and navigate to `http://localhost:5000`
- View the photo list of the countries 
- There is an option to add new country to the list by "add_profile" page
- Click in one photo to open a page with the details of this country by "country_info" page.
- There is an option to add a review by the user in "country_info" page.
- There is an option to delete or change details in the "country_info" page by two buttons.
- The update button take the user to alter_info page where can he change or update new infomartion.


## Built With

- [Python](https://www.python.org/) - The programming language used
- [Flask](https://flask.palletsprojects.com/) - The web framework used
- [HTML] - Markup Language
- [Django] - Python web framework 
-  CSS framework used for styling


## Description

- Create Flask application
- Create database to your site subject
- The options of the site will be to charge an information about new country,like:
  1.  image
  2. Name country
  3. capital of country
  4. official language 
  5. video for best 10 places 
- On the homepage of the site will present all the images as a link for each one detail page.
- The detail page will contain all the data that belong for the same country with option to write a review

## Design 

This is a Flask web application that has functionality to store information about countries, such as name, position, capital name, official language, best 10 places, and a profile picture.<br>
This information is stored in a SQLite database using the SQLAlchemy library. The user can add, delete, or view information about a country.
The uploaded images are stored in a folder,<br>
and the path to the image is stored in the database. The file format of the images must be in 'png', 'jpg', 'jpeg' or 'gif'

## Table of Contents
Depending on the  project directory and the contents of the files, I will divide the contents:
1. README.md 
2. app.py - it contain code that sets uo the application
3. templates - it contain all the HTML files 
4. static - it contain the upload images and the CSS file
5. instance - file that contains configuration settings or data specific to an individual instance of a software application
6. migrations - is a versioned change to the database schema, used for version control and to keep track of changes made to the database over time.

## Tests

The following tests we may run in the application to ensure it's functioning correctly:
1. Unit tests: to test individual functions and modules
2. Integration tests: to test the interaction between different parts of the application.
3. Functional tests: to test end-to-end functionality of the application, simulating a user's actions.
4. Load tests: to test the performance and scalability of the application under heavy loads.
5. Security tests: to test for vulnerabilities and ensure data protection.
6. Usability tests: to test the user interface and the user experience of the application.






