# FastAPI CQRS

FastAPI CQRS is an open-source project that demonstrates the implementation of the Command Query Responsibility Segregation (CQRS) pattern in a FastAPI application.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.11
- Docker
- Poetry

### Installation

Clone the repository:

```bash
git clone https://github.com/maxbeaudoin/fastapi-cqrs.git
cd fastapi-cqrs
```
Activate the virtual environment:

```bash
poetry shell
```

Install dependencies using Poetry:
```bash
poetry install
```

## Setup

Before running the application, you need to set up your environment variables. 

Navigate to `/src` directory and create a `.env` file:

```bash
cd src
touch .env
```

Open `.env`, add your API key:

```properties
API_KEY=your_api_key
```

Replace `your_api_key` with your actual API key.

### Running the Application

**Terminal**

Start the FastAPI server:
```bash
uvicorn --port 8000 --reload --factory main:create_app
```

**Docker**

Build and run the Docker image:
```bash
docker build -t fastapi-cqrs --target development .
docker run -p 8000:8000 fastapi-cqrs
```

**Docker Compose**

Start the services defined in the Docker Compose configuration:
```bash
docker compose up
```

### Contributing
Please read CONTRIBUTING.md (TBD) for details on our code of conduct, and the process for submitting pull requests to us.

### License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Acknowledgments
- FastAPI
- Docker
- Poetry
