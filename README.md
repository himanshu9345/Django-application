# Django-application
Learning Django

[![codecov](https://codecov.io/gh/himanshu9345/Django-application/branch/master_with_testcases/graph/badge.svg)](https://codecov.io/gh/himanshu9345/Django-application)

[![Latest Code](https://github.com/himanshu9345/Django-application/workflows/Python%20application/badge.svg?branch=master_with_testcases)](https://github.com/himanshu9345/Django-application/actions?query=workflow%3A%22Python+application%22)


Created a User Portfolio builder website using Django from the ground up using prebuild HTML and CSS template. 

### I have learned </br>
- How to created a postgres sql database, organize URL paths, and design the interface to communivate between html page and data. 
- How to include static files, setting up a Postgres database, models, and using the admin interface.
* How models, URL patterns, views and templates are used together to create powerful modular code for a web application.
* How Django Forms makes task of collecting and validating data from a user easy. I have used native form framework and Model form. Model forms, which allow you to automatically create a form from an existing model which helped me efficient data entry.

### Continous Integration
- when new testcases/changes are push via master_with_testcases branch, Github actions build and run testcases.
- If all the test cases are passed, this way I ensure that code in master_with_testcases branch is stable.
- When i want to deploy changes, I create pull request from master_with_testcases branch then master runs integration test using github actions integrate.yml. 
- It test whether new pull request is disrupting any exisiting master's test cases, If not then code will get merged with master
 
