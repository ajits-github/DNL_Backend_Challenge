# Decisions Made During the Project

Throughout the development of this project, various decisions were made to ensure effective scraping of data, the optimal structure of the database, and the smooth execution of the API. This document outlines those key decisions.

## Choice of FastAPI
Even though it was an initial recommendation, FastAPI emerged as the preferred framework for the API development because of its speed, efficiency, and ease of use. A notable advantage of FastAPI is the automatic generation of Swagger UI which simplifies the testing and documentation of the API endpoints.

## Database Structure
SQLite was employed given its lightweight nature and ease of setup. It offered a rapid prototyping advantage and negated the need for an external server setup.

The table structure was tailored to accommodate data derived from the scraping process, capturing attributes like manufacturer, category, model, part_number, and part_category.

## Scraping Strategy

### BeautifulSoup Implementation
The website's structure to be scraped influenced the decision to use the BeautifulSoup library due to its flexibility and efficiency. 

To achieve cleaner code and facilitate debugging and potential expansions, the scraper was architectured modularly. Distinct functions were dedicated to scraping manufacturers, models, and parts.

### Transition to Scrapy
Recognizing the demand for faster and more concurrent scraping, the project incorporated Scrapy. As a powerful scraping framework, Scrapy offers advantages in speed, concurrency, and handling complex scraping requirements.

## Configuration and Environment Consistency
The introduction of `config.yml` allowed for centralization of key configurations like the database path. This ensures easier manageability and adaptability.

## Dockerization
Docker was utilized to containerize both the scraper (Beautiful Soup and Scrapy versions) and the API. This strategy guaranteed a consistent environment, simplifying the setup process and minimizing disparities between development and production environments.

## Logging
To keep track of the scraping processes, especially with the Scrapy implementation, logging was incorporated. This allows for better monitoring, debugging, and understanding of the scraper's behavior. The verbosity and settings of the logger can be easily adjusted to suit the need.

## Future Considerations
Considering future requirements, the project might pivot to a robust database like PostgreSQL if the volume of scraped data surges substantially.
