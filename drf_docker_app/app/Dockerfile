FROM python:3.12-alpine

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Create a non-root user and group
RUN addgroup -S appgroup && adduser -S appuser -G appgroup

# Copy the application files into the container
COPY . /backend/

WORKDIR /backend

# Update Alpine package list and install system dependencies (including libpq)
RUN apk update && \
    apk add --no-cache gcc musl-dev postgresql-dev libffi-dev libpq && \
    # Install Python dependencies and clean up unnecessary packages
    pip install --no-cache-dir -r requirements.txt && \
    apk del gcc musl-dev postgresql-dev libffi-dev

# Change ownership of the files to the non-root user
RUN chown -R appuser:appgroup /backend

# Switch to the non-root user
USER appuser
