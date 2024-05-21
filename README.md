# Real-Time Task Manager with FastAPI

This project is a FastAPI-based real-time task management application. It provides endpoints for user authentication, managing tasks, and real-time task updates. The application leverages WebSocket for real-time communication and PostgreSQL for data persistence.

## Installation

1. **Clone the Repository**
   Clone the repository to your local environment using SSH or HTTPS:
   ```bash
   git clone https://github.com/your-username/TaskManager-with-FastAPI.git

2. **Set Up Docker Environment**
   
Build and run the Docker container with the following commands:
```bash
   docker build -t taskmanager .
   docker run -d --name taskmanager_instance -p 8000:8000 --env-file .env taskmanager
```
3. **Environment Variables**

Create a .env file in the root of the project containing necessary environment variables:
```bash
DATABASE_URL=postgresql://username:password@localhost/task_db
SECRET_KEY=your_secret_key
```
## Running the Project
1. **Accessing the Application**

The application will be accessible at http://localhost:8000. Interact with the API using tools like Postman or Swagger.

**API Endpoints**
-  **User Registration**
-  **Endpoint: /auth/register/**
-  **Method: POST**
-  **Request Body:**
```bash
{
  "username": "newuser",
  "password": "password123",
  "email": "newuser@example.com"
}
```
- **Response**
```bash
{
  "username": "newuser",
  "email": "newuser@example.com",
  "id": 1
}
```
**User Login**
-  **Endpoint: /auth/login/**
-  **Method: POST**
-  **Request Body:**
```bash
{
  "username": "newuser",
  "password": "password123"
}
```
- **Response:**
```bash
{
  "access_token": "your_token",
  "token_type": "Bearer"
}
```
**Create Task**
- **Endpoint: `/tasks/`**
- **Method: `POST`**
- **Authorization: `Bearer <your_token>`**
- **Request Body:**
```bash
{
  "title": "Sample Task",
  "description": "This is a sample task."
}
```
- **Response:**
```bash
{
  "id": 1,
  "title": "Sample Task",
  "description": "This is a sample task.",
  "is_completed": false,
  "created_at": "2024-05-22T14:22:23.382Z",
  "user_id": 1
}
```
**Docker Deployment**

This project is containerized using Docker, simplifying the setup and deployment process. Ensure Docker is running before building and launching the container as described in the setup steps.

## Contributing
If you'd like to contribute to this project, feel free to create a pull request or open an issue in the GitHub repository.

## Contact
For questions or support, contact rojcovictor1@gmail.com.