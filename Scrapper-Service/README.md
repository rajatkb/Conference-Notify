# SCRAPPER-SERVICE

It's the service responsible for scrapping information about conferences and putting all these information into the db storage. Currently the default The `main.py` will be running as a daemon in a micro instance for filling information into a Mongo NOSQL db. The choice of MongoDB comes from due to lack of requirement of transaction but rather faster I/O.    



## Dev Environment Requirement
*   Any MongoDB installation (ATLAS / Local)
*   Python 3.6+

## Python packages required
* pymongo driver
* Beautiful Soup
* Requests
* logging (python default)


## Deploying the service

```shell

>> cd Scrapper-Service/

>> python main.py -h
usage: main.py [-h] [-c CONFIG] [-l LOG_LEVEL]

optional arguments:
  -h, --help            show this help message and exit
  -c CONFIG, --config CONFIG
  -l LOG_LEVEL, --log LOG_LEVEL
```

## Structure of service
*   **Interfaces**
    * scrapper.py
*   **DataModels**
    * conference.py
*   **Scrappers**
    *   WikiCFP.py
    *   someotherservice.py
*   **Database**
    *   db.py 
*   main.py
*   config.json

 

## Class files

*   **conference.py**   
    *   Conference class
        *   This class contains the container used for Conference information , to contain scrapped information from the individual Scrappers. It's part of the datamodel. Read the class doc string to know more.

*   **db.py**
    *   Database class
        *   This class is responsible to establishing db connection and handling error related to it. Read the class docstring to know more

*   **scrapper.py**
    *   Scrapper class
        * Interface for other scrapper plugins to extends.

## How to Contribute ?

* Add new scrappers by implementing the interface Scrapper.py and add the new scrapper information inside the config.json file so that the main.py file can pick up the required class when starting

* Provide better implementation changes to the base design of the service.

* Follow up on the Issues tab for bugs and improvement requirements



