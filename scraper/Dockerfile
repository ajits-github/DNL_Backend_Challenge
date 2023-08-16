# Use an official Python runtime as the parent image
FROM python:3.7-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY scraper/requirements.txt .
# COPY scraper /app/scraper

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY scraper .
COPY database /app/database
COPY config_util.py .
COPY config.yml .

# Specify the command to run on container start
CMD ["python", "./main.py"]