# Goal Garden

## Application Overview

This Flask application serves as a platform for users to interact with each other, set goals, join groups, and exchange messages. It provides various features such as user authentication, profile management, messaging, goal setting, group participation, and database querying.

## Application Structure

- `app.py`: Main file for the Flask application, containing route handling, database initialization, and error handling.
- `templates/`: Directory containing HTML templates for different pages of the application.
- `db/`: Directory containing database models and configurations.
- `static/`: Directory containing static files such as CSS stylesheets and client-side scripts.

## Features

**User Authentication**: Users can register, log in, and log out securely.
**Profile Management**: Users can view and edit their profiles, including personal information and bio.
**Messaging**: Users can send and receive messages to/from other users.
**Goal Setting**: Users can set personal goals and track their progress.
**Group Participation**: Users can join groups and interact with other members.
**Database Querying**: Supports ad-hoc querying of the database with custom SQL queries.

## Dependencies

- `Flask`: Web framework for building the application.
- `Flask-WTF`: Flask extension for handling forms.
- `Flask-SQLAlchemy`: Flask extension for ORM with SQLAlchemy.
- `Flask-Login`: Flask extension for user session management.
- `WTForms`: Library for form validation and rendering.
- `SQLAlchemy`: SQL toolkit and ORM for Python.
- `Python-dotenv`: Library for managing environment variables.
- `MySQL Database`: Database backend for storing application data.

## Installation

Clone the repository:
```
git clone https://github.com/your_username/your_repository.git
```
Install dependencies:
```
pip install -r requirements.txt
```

Set up the database:

Create a MySQL database and update the database connection parameters in `app.py`.

Run any database migrations or setup scripts provided in `db/`.

Run the application:
```
python app.py
```
Access the application in your web browser at `http://localhost:5000`.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

- Fork the repository on GitHub.
- Create a new branch with a descriptive name.
- Make your changes and test thoroughly.
- Commit your changes and push to your fork.
- Submit a pull request with a clear description of your changes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements

Flask Documentation: https://flask.palletsprojects.com/
SQLAlchemy Documentation: https://docs.sqlalchemy.org/
WTForms Documentation: https://wtforms.readthedocs.io/
