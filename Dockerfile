# Start with a base Python environment
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy our app files into the container
COPY app.py .
COPY test_app.py .

# Install pytest (for running tests inside container)
RUN pip install pytest flask

# Tell Docker what to run when the container starts
CMD ["python", "app.py"]
