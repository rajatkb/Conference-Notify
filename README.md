# Conference-Notify

## [![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/dwyl/esta/issues)

Conference-Notify will be an open source web based application that will aggregate conference information from wikicfp , guide2research and other such websites to create a single point of aggregated information and build index over the same. These information can then be searched by users through plain text queries. On finding relevant conferences the user can create recurring notifiers for themselves for the date reminders which can be enabled on both mobile devices and through browser notification.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system. You can also refer to this [helper document](https://docs.google.com/document/d/1gAd7DHDg7xybD6H72HAGCQFdPDTqC9SDejJCdPK0wd4/edit?usp=sharing)

### Prerequisites

* Mongodb installation (Local / Atlas)
* Python 3.6+ environment
* [Pymongo client](https://www.mongodb.com/blog/post/getting-started-with-python-and-mongodb)  
* node.js
* Angular 6+

Pymongo client installation
```shell
python -m pip install pymongo

```

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


## 👨 Project Admin

- Rajat Kanti Bhattacharjee  <p>[<img src="https://img.icons8.com/color/32/000000/github-2.png" display = "inline-block">](https://github.com/rajatkb) [<img src="https://img.icons8.com/doodle/32/000000/linkedin-circled.png" display = "inline-block">](https://www.linkedin.com/in/rajatkb/)</p>

## 👬  Mentors
| Name | Point of Contact |
| ------- | ------- |
| Maham Arif     |      <p float = "center">[<img src="https://img.icons8.com/color/32/000000/github-2.png" display = "inline-block">](https://github.com/MahamArif)  [<img src="https://img.icons8.com/doodle/32/000000/linkedin-circled.png" display = "inline-block">](https://www.linkedin.com/in/maham-arif/)</p> |
| Anoop Singh  |      <p float = "center">[<img src="https://img.icons8.com/color/32/000000/github-2.png" display = "inline-block">](https://github.com/anoopsingh1996)   [<img src="https://img.icons8.com/doodle/32/000000/linkedin-circled.png" display = "inline-block">](https://linkedin.com/in/anoopsingh1996)</p> |
| Sagar Sehgal  |   <p float = "center">[<img src="https://img.icons8.com/color/32/000000/github-2.png" display = "inline-block">](https://github.com/sagar-sehgal) [<img src="https://img.icons8.com/doodle/32/000000/linkedin-circled.png" display = "inline-block">](https://www.linkedin.com/in/sagar-sehgal/)</p> |


Feel free to ask your queries!! 🙌


#### Contributors  

Waiting for some 🧐

## License

This project is licensed under the GPL License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgement


<centre>
<img src="gssoc_black.png"></img>
</centre>


A big thanks to GirlScript foundation for having this project under [GirlScript Summer of Code](https://www.gssoc.tech/)
