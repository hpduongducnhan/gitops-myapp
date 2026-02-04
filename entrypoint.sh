#!/bin/bash
set -e

echo "Starting Django application..."

# Wait for PostgreSQL to be ready
echo "Waiting for PostgreSQL..."
while ! nc -z ${DB_HOST:-localhost} ${DB_PORT:-5432}; do
  sleep 0.5
done
echo "PostgreSQL is ready!"

# Run migrations
echo "Running database migrations..."
poetry run python manage.py makemigrations --noinput
poetry run python manage.py migrate --noinput

# Collect static files (optional, uncomment if needed)
# echo "Collecting static files..."
# poetry run python manage.py collectstatic --noinput

# Create superuser if needed (optional)
# echo "Creating superuser..."
# poetry run python manage.py createsuperuser --noinput || true

echo "Starting server..."
exec poetry run python manage.py runserver 0.0.0.0:8000
