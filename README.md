## Getting Started

**Terminal**
```
uvicorn --port 8000 --reload main:app
```

**Docker**
```
docker build -t fastapi-headstart --target development .
docker run -p 0.0.0.0:8000:8000 fastapi-headstart
```

**Docker Compose**
```
docker compose up
```

