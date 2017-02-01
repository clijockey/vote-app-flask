# Big Rob Coffee Flask Application


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

## Getting started

### Cloud Foundry

Download [Docker for Mac or Windows](https://www.docker.com).

Run in this directory:

    $ docker-compose up

The app will be running at [http://localhost:5000](http://localhost:5000), and the results will be at [http://localhost:5001](http://localhost:5001).

## Architecture

This repo holds the front-end voting compoents however the following architecture is what I had in mind. You can see a single repo [here](https://github.com/clijockey/miggins-vote-app)
![Architecture diagram](architecture.png)

* A Python webapp which lets you vote between two options
* A Redis queue which collects new votes
* A .NET worker which consumes votes and stores them in…
* A Postgres database backed by a Docker volume
* A Node.js webapp which shows the results of the voting in real time

## Credit

I have to give credit to a number of different sources. Firstly I used as the base of my voting app something that [Docker created](https://github.com/docker/example-voting-app) and adapted a bootstrap theme called [freelancer](https://github.com/BlackrockDigital/startbootstrap-freelancer).
