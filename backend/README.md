# ViraSearch Backend API

FastAPI backend for the ViraSearch application.

## Project Structure

```
backend/
├── app/
│   ├── routers/        # API route handlers
│   ├── models/         # Database models
│   ├── schemas/        # Pydantic schemas
│   └── config/         # Configuration settings
├── main.py             # Application entry point
├── requirements.txt    # Python dependencies
└── .env.example        # Environment variables template
```

## Setup

### Prerequisites

**Option 1: Docker (Recommended)**
- Docker
- Docker Compose

**Option 2: Local Python**
- Python 3.8 or higher
- pip

### Option 1: Running with Docker (with Hot Reload)

1. Create environment file:
```bash
cp .env.example .env
```

2. Build and start the container:
```bash
# From the project root directory
docker-compose up --build
```

Or run in detached mode:
```bash
docker-compose up -d
```

3. View logs:
```bash
docker-compose logs -f backend
```

4. Stop the container:
```bash
docker-compose down
```

The application will run with hot reload enabled - any changes to your code will automatically restart the server.

### Option 2: Local Installation

1. Create a virtual environment:
```bash
python -m venv venv
```

2. Activate the virtual environment:
```bash
# On Windows
venv\Scripts\activate

# On Linux/Mac
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create environment file:
```bash
cp .env.example .env
```

## Running the Application

### With Docker

See "Option 1: Running with Docker" section above.

### Without Docker (Local Development)

**Development Mode**

Run with auto-reload:
```bash
python main.py
```

Or using uvicorn directly:
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

**Production Mode**

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

## API Documentation

Once the server is running, access the interactive API documentation at:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Available Endpoints

- `GET /` - Root endpoint
- `GET /health` - Health check endpoint
- `GET /api/v1/example/` - Example endpoint (list)
- `GET /api/v1/example/{item_id}` - Example endpoint (detail)

## Development

### Adding New Routes

1. Create a new router file in `app/routers/`
2. Define your endpoints using FastAPI router
3. Import and include the router in `main.py`

### Adding Models

1. Create model classes in `app/models/`
2. Create corresponding Pydantic schemas in `app/schemas/`

### Configuration

Update settings in `app/config/settings.py` or via environment variables in `.env`

## Docker Features

### Hot Reload

The Docker setup includes hot reload functionality. Any changes you make to the Python files will automatically trigger a server restart without needing to rebuild the container.

### Accessing the Container

To access the running container's shell:
```bash
docker-compose exec backend bash
```

### Rebuilding After Dependency Changes

If you modify `requirements.txt`, rebuild the container:
```bash
docker-compose up --build
```

## Testing

Add tests using pytest:
```bash
pip install pytest pytest-asyncio httpx
pytest
```

With Docker:
```bash
docker-compose exec backend pytest
```
