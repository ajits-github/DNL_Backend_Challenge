import requests
from bs4 import BeautifulSoup

from database.db_manager import store_to_db, data_exists

BASE_URL = "https://www.urparts.com/"

def fetch_categories(manufacturer_url):
    response = requests.get(manufacturer_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return [BASE_URL + link['href'] for link in soup.select('.c_container.allmakes.allcategories ul li a')]

def fetch_models(category_url):
    response = requests.get(category_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return [BASE_URL + link['href'] for link in soup.select('.c_container.allmodels a')]

def fetch_parts(model_url):
    response = requests.get(model_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract parts
    parts_data = []
    for item in soup.select('.c_container.allparts li a'):
        part_text = item.text
        
        if ' - ' in part_text:
            part_number, part_category = part_text.split(' - ', 1)
        else:
            part_number = part_text
            # part_category = "Unknown"
            part_category = ""

        parts_data.append({
            'part_number': part_number.strip(),
            'part_category': part_category.strip()
        })
    return parts_data

def scrape_website():
    manufacturers_url = BASE_URL + "index.cfm/page/catalogue"
    response = requests.get(manufacturers_url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # soup_lxml = BeautifulSoup(response.content, 'lxml')
    # print(soup_lxml.prettify())

    data = []

    for manufacturer in soup.select('div.c_container.allmakes a'):
        manufacturer_name = manufacturer.text.strip()
        manufacturer_url = BASE_URL + manufacturer['href']
        print("manufacturer_name......", manufacturer_name)
        
        for category_url in fetch_categories(manufacturer_url):
            for model_url in fetch_models(category_url):
                parts = fetch_parts(model_url)
                for part in parts:
                    entry = {
                        'manufacturer': manufacturer_name,
                        'category': category_url.split('/')[-2],
                        'model': model_url.split('/')[-2],
                        'part_number': part['part_number'],
                        'part_category': part['part_category']
                    }
                    data.append(entry)
                    break
    
    return data

if __name__ == "__main__":
    if not data_exists():
        scraped_data = scrape_website()
        store_to_db(scraped_data)
    else:
        print("Data already exists in the database. Exiting...")
    
