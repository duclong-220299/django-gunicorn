# Django Gunicorn Project

This project is a Django-based web application configured to use Gunicorn as the WSGI server. It also includes Django REST Framework and API key authentication for building RESTful APIs.

## Features

- **Django 4.2.3**: A high-level Python web framework.
- **Gunicorn 20.1.0**: A Python WSGI HTTP server for UNIX.
- **Django REST Framework**: For building RESTful APIs.
- **API Key Authentication**: Secure API access using `djangorestframework-api-key`.
- **Environment Configuration**: Managed using `django-environ`.

## Requirements

- Python 3.9 or higher
- PostgreSQL (if using `psycopg2-binary`)
- pip (Python package manager)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/django-gunicorn.git
   cd django-gunicorn
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r src/requirements.txt
   ```

4. Set up environment variables:

   Create a `.env` file in the `src` directory and configure your environment variables. Example:

   ```env
   DEBUG=True
   SECRET_KEY=your-secret-key
   DATABASE_URL=sqlite:///db.sqlite3
   ```

5. Apply migrations:

   ```bash
   python src/manage.py migrate
   ```

6. Run the development server:

   ```bash
   python src/manage.py runserver
   ```

## Running with Gunicorn

To run the application using Gunicorn:

```bash
gunicorn core.wsgi:application --bind 0.0.0.0:8000
```

## API Documentation

This project includes Django REST Framework for building APIs. You can access the API documentation (if configured) at:

```
http://127.0.0.1:8000/api/
```

## Deployment

For production, use Gunicorn with a reverse proxy like Nginx. Example Gunicorn command:

```bash
gunicorn core.wsgi:application --bind 0.0.0.0:8000
```

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
