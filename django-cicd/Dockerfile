# Lightweight Python base image for ARM64
FROM python:3.12-slim

# Working directory inside the container
WORKDIR /app

# Copy dependencies first (optimizes Docker cache)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project
COPY . .

# Port exposed by the container
EXPOSE 8000

# Command to start Django with Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "config.wsgi:application"]