# Technical Assessment for Industry Dive

## Installation and Execution

* Clone the repo to the directory of your choice
* Install [Docker](https://docs.docker.com/get-docker/) if needed
* Run ``docker-compose up -d`` to setup and build the application
* Run ``docker-compose run web python manage.py migrate`` to initialize the database if you haven't done so before
* Go to http://localhost:8000
* Run ``docker-compose down`` when done

## Acknowledgement

* Implemented [wait-for-it.sh](https://github.com/vishnubob/wait-for-it) to address container race conditions
