# Use a Python base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy all files from current dir into /app in container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port (if app listens on 8000)
EXPOSE 8000

# Default command to run your app
CMD ["python", "app.py"]
