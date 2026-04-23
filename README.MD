# Vigilia MED MVP

## Project Description

Vigilia MED MVP is a medical shifts application consisting of a React-based frontend and a FastAPI-built backend. The application enables [short description of functionality, e.g., patient management, health monitoring, etc. - adjust as needed].

## Prerequisites

- Node.js (version 16 or newer)
- Python (version 3.8 or newer)
- pip (Python package manager)

## Installation

### Backend (FastAPI)

1. Navigate to the `api` folder:
   ```
   cd api
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

### Frontend (React)

1. Navigate to the `pwa` folder:
   ```
   cd pwa
   ```

2. Install dependencies:
   ```
   npm install
   ```

## Running the Application

### Backend

In the `api` folder, start the server:
```
uvicorn main:app --reload
```

The backend will be available at `http://localhost:8000`.

### Frontend

In the `pwa` folder, start the application:
```
npm start
```

The frontend will be available at `http://localhost:3000`.

## Project Structure

- `api/` - FastAPI backend code
- `pwa/` - React frontend code (Progressive Web App)

## API Documentation

After starting the backend, API documentation is available at `http://localhost:8000/docs` (Swagger UI).

## License

[Specify license, e.g., MIT]