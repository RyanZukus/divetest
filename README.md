# Technical Assessment for Industry Dive

## Installation and Execution

* Clone the repo to the directory of your choice
* Install [Docker](https://docs.docker.com/get-docker/) if needed
* Run the following commands

```
docker-compose up -d
docker-compose run web python manage.py migrate
```

* Go to http://localhost:8000 or http://0.0.0.0:8000

## Acknowledgement

* Implemented [wait-for-it.sh](https://github.com/vishnubob/wait-for-it) to address container race conditions