# Cars API

Cars API let you show list of cars and rate them.

DEMO

## Available endpoints
POST /cars
* Request body should contain car make and model name
* Based on this data, its existence is checked here https://vpic.nhtsa.dot.gov/api/
* If the car doesn't exist - an error is returned, if the car exists - the new car is saved

POST /rate
* Add a rate for a car from 1 to 5

GET /cars
* Fetch list of all cars already present in application database with their current average rate

GET /popular
* Fetch top cars already present in the database ranking based on number of rate


## Prerequisites
 - Docker
 - Docker Compose
 - make (optional)

## Installation

```
 git clone git@github.com:ggawelkojulita/cars-api.git
 cd cars-api
```
### 1. Build:

```make build``` 

or
```
docker-compose build
docker-compose run --rm cli python manage.py migrate
```

### 2. Run migrations
```
make migrate
```
or

```
docker-compose run --rm cli python manage.py migrate
```

### 3.Run:
```
make run
```
or
```
docker-compose up -d
```

##Heroku:




