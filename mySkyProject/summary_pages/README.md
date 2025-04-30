# Dhanjo - Health Monitoring System

Dhanjo is a Flask-based web application for health monitoring and metric tracking. It provides a comprehensive platform for managing health metrics, generating alerts, and visualizing data through dashboards.

## Features

- User authentication and authorization
- Health metric tracking and management
- Configurable alerts and notifications
- Admin dashboard for system management
- Real-time data visualization

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/dhanjo.git
cd dhanjo
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your configuration
```

5. Initialize the database:
```bash
flask db init
flask db migrate
flask db upgrade
```

## Running the Application

```bash
flask run
```

The application will be available at `http://localhost:5000`

## Project Structure

```
dhanjo/
├── app.py                  # Main application entry point
├── config.py              # Configuration settings
├── models.py              # Database models
├── forms.py               # Form definitions
├── auth.py                # Authentication routes
├── metrics.py             # Metric management routes
├── admin.py               # Admin interface routes
├── requirements.txt       # Dependencies
└── templates/             # HTML templates
    ├── base.html          # Base template
    ├── auth/              # Authentication templates
    ├── metrics/           # Metric templates
    └── admin/             # Admin templates
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 