FROM python:3.10-slim

WORKDIR /app

# Install Poetry
RUN pip install poetry

# Copy poetry files and install dependencies
COPY pyproject.toml poetry.lock* ./
RUN poetry install --no-interaction --no-ansi --no-root

# Copy project files
COPY . .

# Entrypoint for migrations and superuser creation
RUN chmod +x docker-entrypoint.sh
ENTRYPOINT ["/app/docker-entrypoint.sh"]

# Start Django server
CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
