
# Magic 
### Monitoring Attraction Guest flow with Interactive Charts - Web Application

This project serves to satisfy project requirements for Seminar in Advanced Software Development CEN-4930C

## Authors

- [@John Sapp](https://www.linkedin.com/in/johnsapp150/)

## Abstract

Seminar in Advanced Software Development CEN-4930c, offered by Valencia College, seeks to culminate previous coursework into one working application.

The application delivered at the end of this course must:
* Collect data from an API endpoint
* Store the collected data
* Display the data visually

The project architecture, pipelines, and technologies are decided by the student. The student is to design a system that satisfies the requirements above. 

Topics covered in this project include **Back-end development, Front-end development, Data collection, API interactions, JSON handling, Database storage/retrieval, Data manipulation** and **Data visualization**.

## Technologies used
* Back-end "Python and Django"
* Front-end "Django and Bootstrap"
* Database "MySQL"
* API data collection "Python"
* Data collection automation "Apache Airflow"
* Data manipulation "Python"
* Data visualization "Plotly"

## Overview
Magic is a Wait time visualization platform currently displaying Attraction wait time data from the four Walt Disney World parks. In the current project state, the web app gathers wait time data via an API, stores the data, and then displays the data visually via a line graph. 

* Future development
    * AWS deployment
    * Animated HeatMaps
    * Crowd level index
## Project structure

* Data collection   
    * Python script that calls the Queue Times [API](https://queue-times.com/en-US). Parses the JSON response into Objects that are then stored in a MySQL Database. 
    * Using Apache Airflow **Automation** DAGs (Directed Acyclic Graphs). The API Python script is run once every 10 minutes from 8 AM to 10:59 PM

* Back-end
    * Built with Python and Django
    * Makes SQL queries to the MySQL Database to retrieve requested data

* Front-end
    * Built with Django and Bootstrap 4 
    * Displays HTML files using templating from base and nav HTML files. 

* Data visualization
    * Graphs built using the [Plotly](https://plotly.com/python/) library, displayed on web pages via django views
