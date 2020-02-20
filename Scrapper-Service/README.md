#### Structure of service
*   **Interfaces**
    * Scrapper.py
*   **Confuguration**
    *   BasicConfig.py
*   **DataModels**
    * Conference.py
    * ConferenceDB.py
*   **Scrappers**
    *   wikicfp.py
    *   someotherservice.py
*   **Database**
    *   mdb.py 
*   main.py
*   config.json

The main.py will be a service that will be running as a daemon in a amazon/gcp micro instance for filling information into a Mongo NOSQL db. The choise of MongoDB comes from due to lack of requirement of transaction but rather faster I/O.  

#### Import Data for conference

*   **Conference.py**   
    *   Conference class
        *   This class contains the container used for Conference information , to contain scrapped information from the individual Scrappers

*   **ConferenceDB.py**
    *   ConfernceDB class
        *   This class contains the container used for containing the Db information , along with the Conference information contained inside the db used.

#### How to Contribute ?

* Add new scrappers by implementing the interface Scrapper.py and add the new scrapper information inside the config.json file so that the main.py file can pick up the required class when starting

* Provide better implementation changes to the base design of the service.

* Follow up on the Issues tab for bugs and improvement requirements



