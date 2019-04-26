# SI 507 Final Project - Refined Movie Data Application

Benjamin Tse-Bung Yu

[Link to this repository](https://github.com/Bezluin/SI507_final_project)

---

## Project Description

This project is a Flask application that allows users to manipulate and retrieve data for movies. The application sources its data both from a pre-existing CSV file and also from
user input.  
Using the application, users can view information regarding movies such as the movie name, its director, and its rating. Users may also add new movie data to the existing database.  
The application can be run locally on any computer as long as all the files for the project are included and the requirements in the requirements.txt file are installed.

## How to run

1. First, you should install all requirements with `pip install -r reqiorements.txt`
2. Second, you should run `python final_project.py` in the terminal
3. The application should be running and hosted on ` http://127.0.0.1:5000/` now. **Note that due to the design of the application, on the initial run, it may take longer for the
landing page and some other pages to load (the program should be importing data from a CSV file and storing them into a database at this time)**

## How to use

1. Once the landing page finishes loading, the user should see this screen: ![landing page](images/landingpage.png)
2. A useful second step here
3. (Optional): Markdown syntax to include an screenshot/image: ![alt text](image.jpg)

## Routes in this application
- Route 1: '/'   →   
  This page will display the landing page of the app, which welcomes the user and briefly describes what the user can do.

- Route 2: '/quotes/all/'  →   
  This page will display the complete collection of quotes.

- Route 3: '/quotes/<author>/'  →   
  This page will display the quotes attributed to a specific person.

- Route 4: '/quotes/<tag>'  →
   This page will display all quotes tagged with the user input.  

## How to run tests
1. First... (e.g. access a certain directory if necessary)
2. Second (e.g. any other setup necessary)
3. etc (e.g. run the specific test file)
NOTE: Need not have 3 steps, but should have as many as are appropriate!

## In this repository:
- Directory Name
  - File in directory
  - File in directory
- File name
- File name

---
## Code Requirements for Grading
Please check the requirements you have accomplished in your code as demonstrated.
- [x] This is a completed requirement.
- [ ] This is an incomplete requirement.

Below is a list of the requirements listed in the rubric for you to copy and paste.  See rubric on Canvas for more details.

### General
- [ ] Project is submitted as a Github repository
- [ ] Project includes a working Flask application that runs locally on a computer
- [ ] Project includes at least 1 test suite file with reasonable tests in it.
- [ ] Includes a `requirements.txt` file containing all required modules to run program
- [ ] Includes a clear and readable README.md that follows this template
- [ ] Includes a sample .sqlite/.db file
- [ ] Includes a diagram of your database schema
- [ ] Includes EVERY file needed in order to run the project
- [ ] Includes screenshots and/or clear descriptions of what your project should look like when it is working

### Flask Application
- [ ] Includes at least 3 different routes
- [ ] View/s a user can see when the application runs that are understandable/legible for someone who has NOT taken this course
- [ ] Interactions with a database that has at least 2 tables
- [ ] At least 1 relationship between 2 tables in database
- [ ] Information stored in the database is viewed or interacted with in some way

### Additional Components (at least 6 required)
- [ ] Use of a new module
- [ ] Use of a second new module
- [ ] Object definitions using inheritance (indicate if this counts for 2 or 3 of the six requirements in a parenthetical)
- [ ] A many-to-many relationship in your database structure
- [ ] At least one form in your Flask application
- [ ] Templating in your Flask application
- [ ] Inclusion of JavaScript files in the application
- [ ] Links in the views of Flask application page/s
- [ ] Relevant use of `itertools` and/or `collections`
- [ ] Sourcing of data using web scraping
- [ ] Sourcing of data using web REST API requests
- [ ] Sourcing of data using user input and/or a downloaded .csv or .json dataset
- [ ] Caching of data you continually retrieve from the internet in some way

### Submission
- [ ] I included a link to my GitHub repository with the correct permissions on Canvas! (Did you though? Did you actually? Are you sure you didn't forget?)
- [ ] I included a summary of my project and how I thought it went **in my Canvas submission**!
