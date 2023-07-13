# Use an official Python runtime as the base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /jagaad_test

# Copy the requirements file to the container
COPY requirements.txt .

# Install the project dependencies
RUN pip install -r requirements.txt

# Copy the project files to the container
COPY . .

# Expose the port that the Django development server will be listening on
EXPOSE 8000

# Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
