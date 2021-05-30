# UOCIS322 - Project 6 #
Brevet time calculator with AJAX, MongoDB, and a RESTful API!

## Recall Project 4

### Overview

Reimplement the RUSA ACP controle time calculator with Flask and AJAX.

### ACP controle times

Controls are points where a rider must obtain proof of passage, and control[e] times are the minimum and maximum times by which the rider must arrive at the location. In other words, essentially replacing the calculator here [https://rusa.org/octime_acp.html](https://rusa.org/octime_acp.html).   

## Recall Project 5

### Overview

Store control times from Project 4 in a MongoDB database.

### Difference with project 4

1. Add two buttons `Submit` and `Display` in the ACP calculator page.

2. Upon clicking the `Submit` button, the control times should be inserted into a MongoDB database.

3. Upon clicking the `Display` button, the entries from the database should be displayed in a new page.

4. Will shows error if inputed control distance is wrong or empty, detailed error response rule reference [https://rusa.org/octime_acp.html](https://rusa.org/octime_acp.html).

## Functionality for this project

This project has following four functionality. 

* 1.
    * "http://<host:port>/listAll" should return all open and close times in the database
    * "http://<host:port>/listOpenOnly" should return open times only
    * "http://<host:port>/listCloseOnly" should return close times only

* 2.
    * "http://<host:port>/listAll/csv" should return all open and close times in CSV format
    * "http://<host:port>/listOpenOnly/csv" should return open times only in CSV format
    * "http://<host:port>/listCloseOnly/csv" should return close times only in CSV format

    * "http://<host:port>/listAll/json" should return all open and close times in JSON format
    * "http://<host:port>/listOpenOnly/json" should return open times only in JSON format
    * "http://<host:port>/listCloseOnly/json" should return close times only in JSON format

* 3.
    * "http://<host:port>/listOpenOnly/csv?top=3" should return top 3 open times only (in ascending order) in CSV format 
    * "http://<host:port>/listOpenOnly/json?top=5" should return top 5 open times only (in ascending order) in JSON format
    * "http://<host:port>/listCloseOnly/csv?top=6" should return top 5 close times only (in ascending order) in CSV format
    * "http://<host:port>/listCloseOnly/json?top=4" should return top 4 close times only (in ascending order) in JSON format

* 4.
    * A consumer programs.

## Identifying Information

Author: Haoran Zhang, hzhang9@uoregon.edu
