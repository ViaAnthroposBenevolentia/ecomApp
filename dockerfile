# Use the official Python image.
FROM python:3.9-slim

# Set the working directory inside the container.
WORKDIR /app

# Copy the requirements file and install dependencies.
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the current directory into the container.
COPY . .

# Run the Django development server.
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
