# Big Rob Coffee Flask Application

![Big Rob](https://res.cloudinary.com/dalqykxs4/image/upload/c_scale,w_74/v1485962518/GitHub/bigrob-transparant.png)

## Introduction

Over the last year or so I have testing and running demos on a number of platforms and environments. While a basic 'Hello Word' app would do its a little bit boring. As a result I have created a number of examples that I can use to learn or highlight the capabilities of these environments.

The idea ia that the appication can be deployed standalone to show how thinsg are packaged up and configured for use on the differnet platforms, it can also use used to show interaction with other compoenets like Redis or MySQL etc.


The thoughts that I had around deployments where using traditional server/virtual machine deployments and also container based making use of microservices. The platforms that I had in mind;

* Pivotal Cloud Foundry (PCF)
* Pivotal Web Services
* OSS Cloud Foundry
* Cisco Shipped
* Cisco Mantl
* Cisco Cloud Center
* Cisco Metacloud
* Docker
* Traditional Application
* Mircoservice Application

### What is the app
When the application is running you will be presented with a simple web page with the option to vote for you favourite coffee bean (the vote function doesnt work yet!). It will also provide information about what container/host the page is being serverd by, this is useful when scaling the application out.

![Vote app](https://res.cloudinary.com/dalqykxs4/image/upload/v1485962497/GitHub/Big-Rob-Coffee.png)

### Configuration

The directory structure is;

```
.
├── Dockerfile
├── Procfile
├── README.md
├── app.py
├── requirements.txt
├── static
│   ├── images
│   │   ├── bigrob.png
│   │   ├── el-salvador.jpg
│   │   ├── ethiopia.jpg
│   │   └── rwanda.jpg
│   ├── js
│   │   ├── freelancer.js
│   │   └── freelancer.min.js
│   └── stylesheets
│       ├── bootstrap.min.css
│       ├── cover.css
│       ├── font-awesome.min.css
│       ├── freelancer.css
│       ├── freelancer.min.css
│       └── style.css
└── templates
    └── index.html
```
The ```static/``` directory contains the images, javascript and CSS files used by the application. The ```templates/``` directory contains the basis for the HTML page.

The ```app.py``` is the main code for the applicaton.

## Getting started



### Cloud Foundry

![](https://www.google.co.uk/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=0ahUKEwiGgrflou_RAhVBShQKHUWfDnQQjRwIBw&url=https%3A%2F%2Fblog.hazelcast.com%2Fcloud-foundry%2F&psig=AFQjCNGALK-NGGaH09PxUfF84Tk32QlxCg&ust=1486051312029611)

To run on Cloud Foundry, I tested on [PWS](http://run.pivotal.io)

```
git clone https://github.com/clijockey/vote-app-flask.git
cd vote-ap-flask
cf push br-coffee
```

You obviously need to be logged into your cloud foundry instance.
The cf CLI should then kick of the process to deploy your application on Cloud Foundry.

The important file in the directory for this is the ```Procfile``` file, it specifies what command is required to run the Python application in the container.

#### Running

Browse to the URL presented back you after the ```cf push``` command has complete.

To check it's running issue the ```cf apps``` command;

```
tmp/vote-app-flask [ cf apps                                                                                                                             master ] 3:44 PM
Getting apps in org ######## / space redwards as ##########...
OK

name        requested state   instances   memory   disk   urls
br-coffee   started           1/1         512M     512M   br-coffee.cfapps.io

```

To get more detail about the running app use the ```cf app <app name>``` command;

```
tmp/vote-app-flask [ cf app br-coffee                                                                                                                    master ] 3:44 PM
Showing health and status for app br-coffee in org ####### / space redwards as #########...
OK

requested state: started
instances: 1/1
usage: 512M x 1 instances
urls: br-coffee.cfapps.io
last uploaded: Wed Feb 1 14:51:03 UTC 2017
stack: cflinuxfs2
buildpack: python 1.5.14

     state     since                    cpu    memory          disk           details
#0   running   2017-02-01 03:16:01 PM   0.0%   16.5M of 512M   116M of 512M
```

#### Remove

To remove the application if you no longer need it run ```cf delete <app name>```;

```
tmp/vote-app-flask [ cf delete br-coffee             master ] 3:41 PM

Really delete the app br-coffee?> y
Deleting app br-coffee in org ####### / space redwards as ##########...
OK
```

### Docker

![](https://www.google.co.uk/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=0ahUKEwjTkdrzou_RAhXCuRQKHUJmBPYQjRwIBw&url=https%3A%2F%2Fcommons.wikimedia.org%2Fwiki%2FFile%3ADocker_(container_engine)_logo.png&bvm=bv.145822982,d.ZGg&psig=AFQjCNEwoscxIJeGYXATInJLz5aufYHT0A&ust=1486051371672328)

NOTE: Since migrating the voting component to an individual repo this need to be be retested. A working version is [here](https://github.com/clijockey/miggins-vote-app).
-----

Download [Docker for Mac or Windows](https://www.docker.com/products/overview).

```
git clone https://github.com/clijockey/vote-app-flask.git
cd vote-ap-flask
docker build -t br-coffee .

```


The app will be running at [http://localhost:5000](http://localhost:5000).

## Architecture

This repo holds the front-end voting compoents however the following architecture is what I had in mind. You can see a single repo [here](https://github.com/clijockey/miggins-vote-app) 
![Architecture diagram](https://res.cloudinary.com/dalqykxs4/image/upload/v1485963209/GitHub/architecture.png)

* A Python webapp which lets you vote between two options
* A Redis queue which collects new votes
* A .NET worker which consumes votes and stores them in…
* A Postgres database backed by a Docker volume
* A Node.js webapp which shows the results of the voting in real time

## Credit

I have to give credit to a number of different sources. Firstly I used as the base of my voting app something that [Docker created](https://github.com/docker/example-voting-app) and adapted a bootstrap theme called [freelancer](https://github.com/BlackrockDigital/startbootstrap-freelancer).
