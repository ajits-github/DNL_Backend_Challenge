# # Use Python 3.7 as the parent image
# FROM python:3.7-slim

# # Set the working directory in the container
# WORKDIR /app

# # Copy the current directory contents into the container at /app
# COPY . /app

# # Install necessary packages and libraries
# RUN pip install --no-cache-dir requests beautifulsoup4

# # Command to run the scraper
# CMD ["python", "scraper/main.py"]


# FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

# # Set the working directory
# WORKDIR /app

# # Install dependencies
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# # Copy the content of the local src directory to the working directory
# COPY ./scraper /app/scraper
# COPY ./api_server.py /app/

# # Specify the command to run on container start
# CMD ["uvicorn", "api_server:app", "--host", "0.0.0.0", "--port", "8000"]
