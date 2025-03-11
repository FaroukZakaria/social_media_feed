# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Environment variables to prevent Python from writing pyc files and buffering stdout/stderr
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the rest of the application code
COPY . .

# Optional: collect static files if using them
RUN python manage.py collectstatic --noinput

# Expose the port the application will run on
EXPOSE 8000

# Use Gunicorn for production (don't use "python manage.py runserver")
CMD gunicorn backend.wsgi:application --bind 0.0.0.0:$PORT
