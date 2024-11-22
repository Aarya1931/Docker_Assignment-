# Stage 1: Use a lightweight Python base image
FROM python:3.10-slim as base

# Set the working directory inside the container
WORKDIR /app

# Copy only the required files
COPY calculator.py .

# Install required Python packages (if any)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Final image to run the app
FROM base as final

# Command to run the calculator
CMD ["python", "calculator.py"]
