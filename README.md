# Requirements
- python 3.9

# Set up development environment
 - python3 -m venv .venv
 - source .venv/bin/activate
 - switch to development branch
 - pip install -r requirements.txt

# Start the development server from /src
 - python manage.py runserver --host=0.0.0.0

# Run pytest
- python -m pytest tests/