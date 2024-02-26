# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Install pipenv
RUN pip install pipenv

# Copy the Pipfile and Pipfile.lock into the container
COPY Pipfile* /usr/src/app/

# Install dependencies from the Pipfile
RUN pipenv install --deploy --ignore-pipfile

# Copy the rest of the application files into the container
COPY . /usr/src/app

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Set environment variable for Flask environment
# ENV FLASK_ENV=production
ENV FLASK_ENV=development

# Define environment variables for Flask app
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Run app.py using pipenv when the container launches
CMD ["pipenv", "run", "flask", "run"]
