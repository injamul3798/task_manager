# Django Task Manager

**Developed by**: Md. Injamul Haque

This project is a Django-based Task Management System that allows users to create, edit, delete, and manage tasks. The system features a responsive interface and robust backend that facilitates task tracking and management. 

## Features

- **Task CRUD**: Create, Read, Update, Delete tasks.
- **Task Completion Tracking**: Mark tasks as completed or incomplete.
- **Dynamic User Interface**: A user-friendly UI built with Bootstrap, featuring real-time task updates and modal dialogs for editing and deleting tasks.
- **Search and Filter**: Filter tasks based on their completion status.

## CI/CD Integration

This project integrates a Continuous Integration (CI) pipeline using GitHub Actions for automated testing. Each push and pull request to the `main` branch triggers the CI pipeline to ensure code quality and functionality through the following steps:

1. **Database Setup**: A PostgreSQL database is spun up for isolated testing.
2. **Dependency Installation**: Python dependencies are installed based on the `requirements.txt` file.
3. **Database Migrations**: Migrations are applied to set up the test database schema.
4. **Automated Tests**: Django unit tests are executed, validating the application's core functionalities.

This CI pipeline ensures any changes to the codebase do not break existing functionality and helps maintain a stable, reliable codebase.

## Installation and Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/task-manager.git
   cd task-manager
