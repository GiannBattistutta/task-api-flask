# Task API Flask

A REST API for task management built with Python, Flask and SQLite.  
This project demonstrates backend development fundamentals, including CRUD operations, REST endpoints, data persistence, modular code organization and API deployment.

## Live API

https://task-api-flask.onrender.com

## Features

- Create, list, update, complete and delete tasks
- RESTful API routes
- SQLite database for data persistence
- JSON responses
- Input validation
- Error handling with proper HTTP status codes
- Modular project structure
- Deployed online using Render

## Technologies Used

- Python
- Flask
- SQLite
- Git
- GitHub
- Render

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Check if the API is running |
| GET | `/tasks` | Get all tasks |
| GET | `/tasks/<id>` | Get a specific task by ID |
| POST | `/tasks` | Create a new task |
| PUT | `/tasks/<id>` | Update a task |
| PATCH | `/tasks/<id>/complete` | Mark a task as completed |
| DELETE | `/tasks/<id>` | Delete a task |

## Example Task Object

```json
{
  "id": 1,
  "title": "Study Flask",
  "description": "Build a REST API with Python and Flask",
  "completed": false
}
