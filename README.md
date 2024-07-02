# QuizMaster

QuizMaster is a web application designed to create and take quizzes. This application is built using Flask and provides a user-friendly interface for quiz administration and participation.

## Features

- User Registration and Authentication
- Quiz Creation and Management
- Taking Quizzes and Viewing Results
- Responsive Design for Mobile and Desktop

## Setup

### Prerequisites

- Python 3.8+
- Flask
- SQLite

### Installation

1. Clone the repository:
    ```bash
    git clone <your-repo-url>
    cd quizmaster
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

4. Set up the database:
    ```bash
    flask db init
    flask db migrate -m "Initial migration."
    flask db upgrade
    ```

5. Run the application:
    ```bash
    flask run
    ```

### Usage

- Navigate to `http://127.0.0.1:5000` in your web browser to access the application.
- Register for a new account or log in with existing credentials.
- Create, manage, and take quizzes from the dashboard.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License.

