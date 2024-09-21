# Todo API

> This repository used for demo Docker

### Documentation

1. Install Docker

[Docker Desktop](https://docs.docker.com/desktop/install/windows-install/)

2. Run MongoDB Docker

```sh
# Create Docker volume
docker volume create mongodbdata
# Start Mongodb container
docker run --rm -d --name mongodb -p 27017:27017 -v mongodbdata:/data/db mongodb/mongodb-community-server:latest
```

3. Create Docker for FastAPI

4. Run Docker

- Build Docker Image

```sh
docker build -t todo_api .
```

- Run Docker Container

```sh
docker run --rm --name todo_api_container -e GOOGLE_API_KEY=AI... -p 7860:7860 todo_api
```

- Push to Docker Hub

```sh
# Login to Docker Hub
docker login

# Create tag with prefix is your Docker hub username
docker tag todo_api:latest mingdoan/todo_api:v1.0

# Push to Docker Hub
docker push mingdoan/todo_api:v1.0
```

- Run on other machine

```sh
docker run --rm --name todo_api_service -e GOOGLE_API_KEY=AI... -p 7860:7860 mingdoan/todo_api:v1.0
```

6. Run with Docker Compose

- Create `docker-compose.yml` file

- Run Docker compose

```sh
docker compose up
```
