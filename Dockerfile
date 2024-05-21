# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Copy custom environment file
COPY api_keys.env .env

# Set the PYTHONPATH environment variable
ENV PYTHONPATH=/app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8000 for the API
EXPOSE 8000

# Run the API when the container launches
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
