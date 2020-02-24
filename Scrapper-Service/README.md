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
    * metadata.py
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
*   **metadata.py**
    * Metadata class
        * This class is used to encapsulate any information about the scrapper that is collecting the conference data and attach metadata about the data of the conference. Like from where it originated, which scrapper extracted it , date of access etc.

*   **db.py**
    *   Database class
        *   This class is responsible to establishing db connection and handling error related to it. Read the class docstring to know more

*   **scrapper.py**
    *   Scrapper class
        * Interface for other scrapper plugins to extends.

## Data Scheme

* The data schema used in mongo look like this

```json
{

        "_id" : NumberLong("6596203108960978438"),
        "title" : " InWeS  2020 : 11th International Conference on Internet Engineering & Web Services",
        "url" : "https://iccsea2020.org/inwes/index.html"
        "bulk_text" : "\n11th International Conference on Internet Engineering & Web Services (InWeS 2020) December 19 ~ .... ",
        "deadline" : ISODate("2020-02-22T00:00:00Z"),

        /*
            Below fields are optional.
        */

        "categories" : [
                "semantic web",
                "wireless",
                "web services",
                "internet"
        ],
        "date_range" : [
                ISODate("2020-12-19T00:00:00Z"),
                ISODate("2020-12-20T00:00:00Z")
        ],
        "finaldue" : ISODate("2020-07-01T00:00:00Z"),
        "location" : "Sydney, Australia",

        /*
            Non-optional metadata
        */

        "metadata" : {
            /*
                Data commited by individual scrappers for metadata
            */      
                "Scrappers" : {
                        "WikiCFP" : {
                                "date_extracted" : ISODate("2020-02-22T22:29:21.272Z"),
                                "website_url" : "http://www.wikicfp.com/cfp/servlet/event.showcfp?eventid=88588&copyownerid=46167",
                                "website" : "http://www.wikicfp.com",
                                "domain" : "wikicfp"
                        }
                }
        },
        "notificationdue" : ISODate("2020-06-22T00:00:00Z"),
        
}

```

**Index**   
1. url , unique
2. deadline



## How to Contribute ?

* Add new scrappers by implementing the interface Scrapper.py and add the new scrapper information inside the config.json file so that the main.py file can pick up the required class when starting

* Provide better implementation changes to the base design of the service.

* Follow up on the Issues tab for bugs and improvement requirements



