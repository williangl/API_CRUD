# API_CRUD

## How to run Database container
1. Is strongly recommended clear all old container vestige on your environment
```
docker stop $(docker ps -q -a)
docker rm -f $(docker ps -q -a)
docker volume prune -f
docker image rm -f $(docker images -q -a)
```
2. Run database container
```
docker build -f Dockerfile-db -t api_crud .
docker run -p 5432:5432 -t api_crud
```

## Execute application
