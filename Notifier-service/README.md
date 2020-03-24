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

### MongoDb Replication setup
* For development purpose , you will have to setup your mongodb , with replication.
* You can resort to using single replication for now , which can scale later on.
* To create replication after installing in windows you can follow [this](https://stackoverflow.com/questions/48139224/mongodb-change-stream-replica-set-limitation)
* For linux , follow the official [docs](https://docs.mongodb.com/manual/reference/configuration-options/#replication-options) , and restart the mongod service or start it with replication option. For quick help look [here](https://www.tutorialspoint.com/mongodb/mongodb_replication.htm)



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

>> npm run build

>> npm start 

//For prod

>> npm run build

>> npm run deploy

```
    