
**BDD Framework for API Automation using Python** 
------

This framework is designed for API automation testing using BDD and Python

In this framework, all CRUD(Create, Read, Update and Delete) operations are automated for the endpoint [cars-api app](https://cars-app.qxf2.com/cars) using API methods POST, GET, PUT and DELETE. Separate tests are written for API validation with BDD and without BDD.  
Before running the tests, make sure that you edit the payload as per your requirements.

If you are new to BDD, then this is a good start for you. First go through the test 'without BDD' and then move on to the 'with BDD test' and feature file. It will be easy to understand the BDD framework if both tests are compared. 

__Prerequisites__

a) Install Python 3.x

b) Add Python 3.x to your PATH environment variable

c) Install pip, if you don't already have it

d) `pip install behave` to install behave OR `pip install git+https://github.com/behave/behave` to obtain the most recent version

e) `pip install -r requirements.txt` to install dependencies


-------------------
Repository details
-------------------
a) Directory structure 

   ./

	|__conf: For all configurations, properties(credentials) and payloads

	|__features: BDD test and steps file

    |__tests: test without BDD

    |__utils: utility module to display results


---------------------------
Commands for Running Tests
---------------------------

__To Run the test without BDD__

1.Edit the payload in conf\payload.py 

2.Run the command `python .\tests\test_api_validation_without_bdd` 


__To Run the test with BDD__

1.Edit the payload in feature file features\api_validation_with_bdd.feature

2.Run the command `behave .\features\api_validation_with_bdd.feature` 
