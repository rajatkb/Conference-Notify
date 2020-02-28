# CONTRIBUTING

Thank you for considering to contribute to this project. I came up with the idea personally when I felt that I needed some personalised single source solution of recuring reminder and manager for scientific conferences. So came the idea of conference-notify. In order to contribute do go through the architecture section and then to some basic coding stadards , issue tracking and PR standards.


# Understanding the Architecture of the Services

Irrespective of the deployment strategy the core acrhitecture shall remain this way.

<centre>
<img src="BasicArch.jpg"></img>
</centre>

The project is built in a microservice fashion with each service exposing some sort of rest api for delivering the information except Scrapper-Service. The scrapper service currently needs to be run as an independent process. The services mostly rely on a common MongoDb and a Elastic Search service for information retrieval and storage.   

The services themselves are written in Python and JavaScript primarily.


### Scrappper-Service

Move to [Scrapper-Service](https://github.com/rajatkb/Conference-Notify/tree/master/Scrapper-Service)

### Notifier-Service

Not yet updated keep tabs on issue and project board

### Search-Service

Not yet updated keep tabs on issue and project board

### User-Application

Not yet updated keep tabs on issue and project board

### ATTENTION

When contributing to this repository, please first discuss the change you wish to make via issue, email, or any other method with the owners of this repository before making a change.

Please note we have a code of conduct, please follow it in all your interactions with the project.
Pull Request Process

 
    1.  Create your own branch with convention 
        "name_task" convention. Do changes and commits from 
        your end and create a pull request to add the branch.
    
    2.  Do verify the changes in branch are localised to 
        issues  addressed in your own system. Before a brach push
        or PR, do a pull from remote master to get recent changes

    3.  Once the PR is submitted the branch will be verified
        and merged to master

    4.  Update the README.md if needed accordingly. 
        Every change must mention if readme requires change.

    [Under GSSOC]
    5.  Make sure to label your PR with beginner,
        easy, medium, hard. According to the issue it is targetting. 

    


