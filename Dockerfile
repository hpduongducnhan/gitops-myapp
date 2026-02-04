# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Install system dependencies
RUN apt-get update && apt-get install -y \
    netcat-traditional \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry
# Using a specific version to ensure consistent builds
RUN pip install poetry==2.3.2

# Copy project files for dependency resolution
COPY pyproject.toml poetry.lock* /code/

# Install dependencies using Poetry
RUN poetry install --no-root

# Copy the rest of the project code
COPY . /code/

# Make entrypoint script executable
RUN chmod +x /code/entrypoint.sh

# Expose the port the app runs on
EXPOSE 8000

# Run the application with entrypoint script
CMD ["/code/entrypoint.sh"]
