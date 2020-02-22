# SCRAPPER-SERVICE

It's the service responsible for scrapping information about conferences and dumping all these information into the db storage. 

#### Dev Environment Requirement
*   Any MongoDB installation (ATLAS / Local)
*   Python 3.6+

#### Python packages required
* pymongo driver
* Beautiful Soup
* Requests
* logging (python default)

#### Structure of service
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

The main.py will be running as a daemon in a micro instance for filling information into a Mongo NOSQL db. The choice of MongoDB comes from due to lack of requirement of transaction but rather faster I/O.  

#### Class files

*   **conference.py**   
    *   Conference class
        *   This class contains the container used for Conference information , to contain scrapped information from the individual Scrappers
*   **db.py**
    *   Database class
        *   This class is responsible to establishing db connection and handling error related to it.

#### How to Contribute ?

* Add new scrappers by implementing the interface Scrapper.py and add the new scrapper information inside the config.json file so that the main.py file can pick up the required class when starting

* Provide better implementation changes to the base design of the service.

* Follow up on the Issues tab for bugs and improvement requirements



