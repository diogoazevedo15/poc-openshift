# Use a lightweight Python base image
FROM python:3.9-slim

# Create and switch to a working directory
WORKDIR /app

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY app.py .

# Expose the container port
EXPOSE 8000

# Run the application
CMD ["python", "app.py"]
