# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Install Poetry
# Using a specific version to ensure consistent builds
RUN pip install poetry==2.3.2

# Copy project files for dependency resolution
COPY pyproject.toml poetry.lock* /code/

# Install dependencies using Poetry
RUN poetry install --no-root --no-dev

# Copy the rest of the project code
COPY . /code/

# Expose the port the app runs on
EXPOSE 8000

# Run the application
# Replace my_app.wsgi with your actual wsgi module if it's different
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]