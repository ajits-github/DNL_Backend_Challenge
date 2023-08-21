# Use an official Python runtime as the parent image
FROM python:3.7-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY api/requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY api .
COPY config_util.py .
COPY config.yml .
COPY .env .

# Specify the command to run on container start
CMD ["uvicorn", "api_server:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]