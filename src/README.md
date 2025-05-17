# README for the Core Django Project

This is the core Django project that includes two main applications: `api` and `website`. 

## Project Structure

The project is organized as follows:

```
core/
├── apps/
│   ├── api/            # API application
│   └── website/        # Website application
├── core/               # Core project files
├── manage.py           # Command-line utility for Django
└── README.md           # Project documentation
```

## Applications

### API
The `api` application is designed to handle all API-related functionalities. It includes models, views, and tests specific to the API.

### Website
The `website` application is responsible for the web interface of the project. It contains models, views, and tests tailored for the website.

## Getting Started

To get started with this project, ensure you have Django installed. You can then run the following commands:

1. Set up the database:
   ```
   python manage.py migrate
   ```

2. Run the development server:
   ```
   python manage.py runserver
   ```

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.