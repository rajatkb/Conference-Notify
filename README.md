# Conference-Notify

## [![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/dwyl/esta/issues)

Conference-Notify will be an open source web based application that will aggregate conference information from wikicfp , guide2research and other such websites to create a single point of aggregated information and build index over the same. These information can then be searched by users through plain text queries. On finding relevant conferences the user can create recurring notifiers for themselves for the date reminders which can be enabled on both mobile devices and through browser notification.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system. You can also refer to this [helper document](https://docs.google.com/document/d/1gAd7DHDg7xybD6H72HAGCQFdPDTqC9SDejJCdPK0wd4/edit?usp=sharing)

## Prerequisites

### MongoDB Installation
#### Local 
This runs MongoDB in your own local machine.
1. Download [MongoDB](https://www.mongodb.com/download-center/community)
2. Install MongoDB by the following installation instructions.

#### Atlas
* MongoDB Atlas is the global cloud database service for modern applications.
1. Go to [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)
2. Create an account or sign in into your mongoDB account.
3. Depending on the usage, select various features.    
For more information, Visit [MongoDB Atlas Docs](https://docs.atlas.mongodb.com/)

### Python 3.6 Installation:

#### Windows:

1. Download [Python](https://www.python.org/downloads/)
2. Install it and ensure that the interpreter will be placed in your execution path.

#### Linux:

1. Ubuntu 17.10, Ubuntu 18.04 (and above) come with Python 3.6 by default. You should be able to invoke it with the command python3.

2. Ubuntu 16.10 and 17.04 do not come with Python 3.6 by default, but it is in the Universe repository. You should be able to install it with the following commands:  

`sudo apt-get update`  
`sudo apt-get install python3.6`  

You can then invoke it with the command python3.6.  

3. If you are using Ubuntu 14.04 or 16.04, Python 3.6 is not in the Universe repository, and you need to get it from a Personal Package Archive (PPA). For example, to install Python from the “deadsnakes” PPA, do the following:

`sudo add-apt-repository ppa:deadsnakes/ppa`  
`sudo apt-get update`  
`sudo apt-get install python3.6`  

As above, invoke with the command python3.6.  

#### MacOS / MacOS X

1. Install Homebrew by pasting the below code in terminal
`/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"`  
2. Accept the required permissions and finish the installation.  
3. Install python 3.6 from   
`brew install python3`

### Pymongo Client
1. Install the Pymongo from the command line using  
`python -m pip install pymongo`  
For various driver installations, Check [Installation](https://pymongo.readthedocs.io/en/stable/installation.html)
2. For more information, Visit [Pymongo client](https://www.mongodb.com/blog/post/getting-started-with-python-and-mongodb)

### Node.js
Download [node.js](https://nodejs.org/en/download/) and install it.

### Angular 6+
Download Angular 6+ from command line  
`npm install -g @angular/cli`  

For more information about Angular, Visit [Docs](https://angular.io/guide/setup-local)

### Installing

The project is divided into several components, i.e services

* Notifier-Service
* Scrapper-Service
* Search-Service

None of this services requires any instllation and can be executed on the fly

**Other services coming soon**



## Deployment

**Scrapper-Service**  
Note: Make sure the configuration file is properly configured for usage, since app.py is reading configuration from the file

```
>> cd Scrapper-Service

>> python app.py --help
usage: app.py [-h] [-c CONFIG] [-l {debug,warn,error,info}] [-t TEST]
               [-ls {console,file}]

optional arguments:
  -h, --help            show this help message and exit
  -c CONFIG, --config CONFIG
                        Specify config.json file ,default: config.json
  -l {debug,warn,error,info}, --log {debug,warn,error,info}
                        Specify the debug level ,default: debug
  -t TEST, --test TEST  Specify whether to test app initialization or run the
                        scrappers ,default: True
  -ls {console,file}, --logStream {console,file}
                        Specify whether to print logs on terminal or to file
                        ,default: console

>> python -m unittest test
It will run all the unit tests written and kept under test folder

```

**Notifier-Service**

```shell

>> cd Notifier-Service

//For dev

>> npm run-script build

>> npm start 

//For prod

>> npm run-script build

>> npm run-script run

```


## Built With

* [pymongo](https://api.mongodb.com/python/current/) - Mongo client for python



## Contributing

Please read [CONTRIBUTING.md](https://github.com/rajatkb/Conference-Notify/blob/master/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Authors

* **Rajat Kanti Bhattacharjee** - *Initial work* - [rajatkb](https://github.com/rajatkb)

#### Contributors  

Waiting for some 🧐

## License

This project is licensed under the GPL License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgement


<centre>
<img src="gssoc_black.png"></img>
</centre>


A big thanks to GirlScript foundation for having this project under [GirlScript Summer of Code](https://www.gssoc.tech/)
