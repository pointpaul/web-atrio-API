# FastAPI Person and Job Management API

This project is a RESTful API built with FastAPI for managing persons and their jobs. It allows you to create, read, and manage persons and their associated jobs, with features such as filtering jobs by date and listing persons by company.

## Features

- **Create Person**: Add a new person with a first name, last name, and birth date. Only persons younger than 150 years can be registered.
- **Add Job to Person**: Assign a job to a person with details like company name, position, and start date. The end date is optional for current jobs.
- **List All Persons**: Retrieve all registered persons, sorted alphabetically, along with their age and current jobs.
- **List Persons by Company**: Get all persons who have worked for a specific company.
- **List Jobs for Person Between Dates**: Retrieve jobs for a person within a specified date range.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/pointpaul/web-atrio-API
   cd web-atrio-API
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   uvicorn api.main:app --reload
   ```

## Usage

- Access the API documentation at `http://localhost:8000/docs` for interactive exploration of the endpoints.
- Use tools like Postman to test the API endpoints.

## Endpoints

- **POST /persons/**: Create a new person.
- **POST /persons/{person_id}/jobs/**: Add a job to a person.
- **GET /persons/**: List all persons.
- **GET /companies/{company_name}/persons/**: List persons by company.
- **GET /persons/{person_id}/jobs/**: List jobs for a person between two dates.

## Database

The application uses SQLite for data storage. The database is configured in `api/database.py`.

## Code Structure

- `api/main.py`: Contains the FastAPI application and endpoint definitions.
- `api/models.py`: Defines the SQLAlchemy models for Person and Job.
- `api/schemas.py`: Contains Pydantic models for request and response validation.
- `api/crud.py`: Implements the CRUD operations for interacting with the database.
- `api/database.py`: Configures the database connection and session.
