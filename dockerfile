# Use official Python image as base
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements if available
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Set default command (adjust as needed)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]