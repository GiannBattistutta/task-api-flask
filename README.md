# Task API with Flask

A beginner-friendly REST API for managing tasks, built with Python and Flask. This project demonstrates fundamental concepts of REST API development including CRUD operations, JSON file persistence, and proper error handling.

## Description

This Task API provides a simple but complete example of building a RESTful web service. It uses a JSON file as a lightweight database, making it perfect for learning without needing to set up a database server. The code is organized into separate modules following best practices:

- **app.py** - Main application entry point
- **routes.py** - API endpoint definitions
- **service.py** - Business logic layer
- **storage.py** - File handling and data persistence
- **tasks.json** - Data storage file

## Features

- Full CRUD (Create, Read, Update, Delete) operations
- JSON file-based data persistence
- Input validation for all endpoints
- Proper HTTP status codes (200, 201, 400, 404)
- Error handling with meaningful messages
- Clean, commented code for learning
- Modular architecture separating concerns

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/tasks` | Get all tasks |
| GET | `/tasks/<id>` | Get a specific task by ID |
| POST | `/tasks` | Create a new task |
| PUT | `/tasks/<id>` | Update an existing task |
| DELETE | `/tasks/<id>` | Delete a task |
| PATCH | `/tasks/<id>/complete` | Mark a task as completed |

### Task Object Structure

```json
{
    "id": 1,
    "title": "Task title",
    "description": "Task description",
    "completed": false,
    "created_at": 1234567890
}
```

## Installation

### 1. Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### 2. Install Dependencies

Navigate to the project directory and install the required packages:

```bash
pip install -r requirements.txt
```

This will install Flask, which is the only dependency needed for this project.

## Running the Project

### Start the Server

```bash
python3 app.py
```

You should see output like:

```
==================================================
Task API with Flask
==================================================
Server starting at http://127.0.0.1:5000
Press Ctrl+C to stop the server
==================================================
```

### Test the API

The server will start at `http://127.0.0.1:5000`. You can test it using the examples below.

## Example Requests

### Get All Tasks

```bash
curl -X GET http://127.0.0.1:5000/tasks
```

### Get a Specific Task

```bash
curl -X GET http://127.0.0.1:5000/tasks/1
```

### Create a New Task

```bash
curl -X POST http://127.0.0.1:5000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title": "Learn Flask", "description": "Build a REST API with Flask"}'
```

### Update a Task

```bash
curl -X PUT http://127.0.0.1:5000/tasks/1 \
  -H "Content-Type: application/json" \
  -d '{"title": "Learn Flask", "description": "Build a complete REST API"}'
```

### Mark Task as Completed

```bash
curl -X PATCH http://127.0.0.1:5000/tasks/1/complete
```

### Delete a Task

```bash
curl -X DELETE http://127.0.0.1:5000/tasks/1
```

## Expected Responses

### Success Responses

- **GET /tasks**: Returns array of all tasks
- **GET /tasks/<id>**: Returns single task object
- **POST /tasks**: Returns created task with 201 status
- **PUT /tasks/<id>**: Returns updated task
- **PATCH /tasks/<id>/complete**: Returns updated task
- **DELETE /tasks/<id>**: Returns success message

### Error Responses

- **400 Bad Request**: Invalid input data
- **404 Not Found**: Task with specified ID doesn't exist

Example error response:
```json
{
    "error": "Task not found"
}
```

## Project Structure

```
task-api-flask/
├── app.py          # Main entry point
├── routes.py       # API route definitions
├── service.py     # Business logic
├── storage.py     # File operations
├── tasks.json     # Data storage (created automatically)
├── requirements.txt # Python dependencies
└── README.md      # This file
```

## Learning Points

This project demonstrates:

1. **Flask Basics** - Setting up a Flask application
2. **RESTful Routes** - Defining API endpoints
3. **Blueprint** - Organizing routes into modular components
4. **JSON Handling** - Reading and writing JSON files
5. **Error Handling** - Returning proper HTTP status codes
6. **Input Validation** - Checking data before processing
7. **Separation of Concerns** - Dividing code into layers

## Extending the Project

Here are some ideas for extending the project:

- Add authentication with JWT tokens
- Add due dates and priorities to tasks
- Add categories or tags for tasks
- Implement pagination for large task lists
- Add search and filter functionality
- Switch to a real database (SQLite, PostgreSQL)

## License

This project is for educational purposes and is free to use and modify.

---

Built with Flask for learning REST API development