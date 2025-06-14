FROM python:3.10-slim

WORKDIR /app

# Install Poetry
RUN pip install poetry

# Copy poetry files and install dependencies
COPY pyproject.toml poetry.lock* ./
RUN poetry install --no-interaction --no-ansi --no-root

# Copy the rest of the code
COPY . .

# Run the bot using poetry's environment
CMD ["poetry", "run", "python", "bot.py"]
