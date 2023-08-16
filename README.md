# DNL Project

This project involves scraping data from a website using both Beautiful Soup and Scrapy, storing the scraped data in a SQLite database, and providing an API built with FastAPI to access and query this data.

## Table of Contents
- [DNL Project](#dnl-project)
  - [Table of Contents](#table-of-contents)
    - [Getting Started](#getting-started)
      - [Setup](#setup)
      - [Configuration](#configuration)
      - [Running the Services](#running-the-services)
      - [Accessing the API](#accessing-the-api)
    - [Components](#components)
      - [Database](#database)
      - [Scrapers](#scrapers)
        - [Beautiful Soup Scraper](#beautiful-soup-scraper)
        - [Scrapy Spider](#scrapy-spider)
      - [API](#api)
    - [API Usage](#api-usage)
      - [Fetching Parts\_Data (Table)](#fetching-parts_data-table)
      - [Swagger UI](#swagger-ui)
    - [Structure](#structure)
    - [Logger](#logger)
    - [Contributing](#contributing)

-----------------------------------------------------------

### Getting Started

#### Setup
- Ensure Docker and Docker Compose are installed on your machine.
- Clone the repository to your local system:
 ```https://github.com/ajits-github/DNL_Backend_Challenge.git```

#### Configuration
Configuration values, such as the path for the SQLite database, are maintained in config.yml in the project repository. Make sure to check and modify, if necessary, before running the services.

#### Running the Services
- From the project's root directory, use the following command to start the services:
  `docker-compose up --build`
The scraper services will begin, scraping the required data and populating the SQLite database. Following this, the API service will be accessible.

#### Accessing the API
- With the services running, access the FastAPI Swagger UI at `http://127.0.0.1:8000/docs`.
- Here, you can test and interact with the available API endpoints.

-----------------------------------------------------------

### Components

#### Database
- SQLite, a file-based database system, serves as the project's database solution. This eliminates the need for separate database services. The SQLite database file is created and populated when the scraper runs.

#### Scrapers

##### Beautiful Soup Scraper
- Located in the `scraper/` directory, this scraper executes once upon initiation. It fetches the required data using Beautiful Soup and stores it in the SQLite database.
- If you want to run locally and create the database so that can be mounted as volume in docker-compose, execute the below command at a terminal.
`python ./scraper/main.py`

##### Scrapy Spider
- Found within the `scraper_spider/` directory, this scraper uses Scrapy to fetch necessary data and stores it in the SQLite database.
- If you want to run locally and create the database:
`python ./scraper_spider/main.py`

#### API
- Hosted in the `api/` directory, the API taps into the populated SQLite database to deliver data through its endpoints. The FastAPI Swagger UI allows direct interaction and testing of the API.

-----------------------------------------------------------

### API Usage

#### Fetching Parts_Data (Table)
- Endpoint: `/parts`
- Refine results using query parameters, e.g., `?manufacturer=Ammann`.

#### Swagger UI
- Test the API endpoints by accessing the FastAPI Swagger UI at `http://127.0.0.1:8000/docs`.

-----------------------------------------------------------

### Structure

- `scraper/`: Houses the Beautiful Soup scraping logic.
- `scraper_spider/`: Contains the Scrapy logic responsible for web scraping.
- `api/`: Contains the FastAPI server and API logic.
- `database/`: Manages database operations and holds the SQLite file.
- `docker/`: Keeps the Dockerfile and relevant configurations for containerization.

-----------------------------------------------------------

### Logger

Logging is integrated into the application, helping in tracking and debugging activities. You can modify the logging level and format in the Scrapy settings to filter the type of information captured and displayed. This can be especially helpful in identifying issues or optimizing scraper performance.

-----------------------------------------------------------

### Contributing

To contribute to this project, please fork the repository and submit a pull request.
