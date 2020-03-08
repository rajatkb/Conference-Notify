# NOTIFIER-SERVICE

It's the service responsible for exposing the scrapped data about the conferences to any kind of frontend through a rest API.The service will also contain a the service for 

**Notify for**
*   Notiying user for specific conference,  based on subscribtion for  
*   Notify user for Conference categories or topics , based on subscribtion

**Notfifaction on** 
*   Change in deadline
*   Submission Reminders

note: *may add more feature*

## Dev Environment Requirement
* NodeJs
* Mongodb (remote/local)

## Installation

**Development**
```shell
>> cd Notifier-Service
>> npm install
```

**Deployment**
```shell
>> cd Notifier-Service
>> npm install --only=prod
```




## Deploying the service

```shell

>> cd Notifier-Service

//For dev

>> npm run-script build

>> npm start 

//For prod

>> npm run-script build

>> npm run-script run

```
    