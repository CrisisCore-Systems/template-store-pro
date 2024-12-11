# Template Store Pro

Professional digital template marketplace built with Django.

## Features
- Digital product management
- Secure payment processing
- Automated delivery system
- User authentication
- Admin dashboard

## Setup
1. Clone the repository
2. Create virtual environment: `python -m venv venv`
3. Activate virtual environment: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Run migrations: `python manage.py migrate`
6. Create superuser: `python manage.py createsuperuser`
7. Run development server: `python manage.py runserver`

## Project Structure
```
template-store-pro/
├── apps/
│   ├── core/
│   ├── products/
│   ├── payments/
│   └── delivery/
├── config/
├── static/
├── media/
└── templates/
```

## Contributing
1. Fork the repository
2. Create feature branch
3. Commit changes
4. Push to branch
5. Create pull request
