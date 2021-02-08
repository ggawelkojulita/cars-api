# Cars API

Cars API let you show list of cars and rate them.

DEMO

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




