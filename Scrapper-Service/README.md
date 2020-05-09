# :books: SCRAPPER-SERVICE

It's the service responsible for scrapping information about conferences and putting all these information into the db storage. Currently the default The `app.py` will be running as a daemon in a micro instance for filling information into a database. Current choice of db is Mongo. THe application can later be extended for different db and index service later.     

## :gear: Dev Environment Requirement
*   Any [MongoDB installation](https://docs.mongodb.com/guides/server/install/) (ATLAS / Local)
*   [Python 3.6+](https://www.python.org/downloads/)

## :package: Python packages required
* pymongo driver
* Beautiful Soup
* Requests
* logging (python default)
* unittest (for unit test of course)

All the above requirements along with their versions are present in  `requirements.txt` and can be installed as 

```bash
$ pip install -r requirements.txt
```


## :rocket: Deploying the service

```shell
>> cd Scrapper-Service/
>> python app.py --help
usage: app.py [-h] [-c CONFIG] [-l {debug,warn,error,info}] [-t TEST]
              [-ls {console,file}]

optional arguments:
  -h, --help            show this help message and exit
  -c CONFIG, --config CONFIG
                        Specify config.json file
  -l {debug,warn,error,info}, --log {debug,warn,error,info}
                        Specify the debug level ,default: debug
  -t TEST, --test TEST  Specify whether to test app initialization or run the
                        scrappers ,default: True
  -ls {console,file}, --logStream {console,file}
                        Specify whether to print logs on terminal or to file
                        ,default: console
(base)
```

## Deploying Scraper service in different modes

```bash
# running the scraper with a custom configuration file
>> python app.py -c <path/to/config.json>
or
>> python app.py --config <path/to/config.json>

# running the scraper service with logs of specific type
>> python app.py -l debug # for only debug logs
>> python app.py -l warn # for only warn logs
>> python app.py -l error # for only error logs
>> python app.py -l info # for only info logs

# running the scraper service with different test modes
>> python app.py --t False
or 
>> python app.py --test False 

# running the scraper service with different logstream settings
>> python app.py -ls console # for logging to console
>> python app.py -ls file # to save logs to file
```

Jump to `demo.py` for implementing a scrapper from scratch and configuring it to run. 

## :detective: Test
We are focusing on doing test driven development, so downn the line things are not unpredicatable.  

Before deploying the current build , it's recommended that you run the test suite once. 

```shell

>>  python -m unittest test -v
test__getitem__ (test.metadata_test.MetadataTestCase) ... ok
test__str__ (test.metadata_test.MetadataTestCase) ... ok
test_data (test.metadata_test.MetadataTestCase) ... ok
test_query_dict (test.metadata_test.MetadataTestCase) ... ok

----------------------------------------------------------------------
Ran 4 tests in 0.002s

OK
(base)


```

If this succeeds , you can move forward with deployment. If this fails. Please mark the build number and raise an issue. Althouth it should not happen because builds and PR is maintained by the author. But in case things blow up you know where to raise issue, 😉😉.

## :pen: How to Contribute ?

* Add new scrappers by implementing the interface Scrapper.py and add the new scrapper information inside the config.json file so that the `app.py`  file can pick up the required class when starting

* Provide better implementation changes to the base design of the service.

* Follow up on the Issues tab for bugs and improvement requirements



