import scrapy
from database.db_manager import store_to_db

BASE_URL = "https://www.urparts.com/"

class PartsSpider(scrapy.Spider):
    name = 'parts'
    start_urls = [BASE_URL + "index.cfm/page/catalogue"]

    def parse(self, response):
        # Extract manufacturers and yield new requests
        for manufacturer in response.css('div.c_container.allmakes a'):
            manufacturer_name = manufacturer.css('::text').get().strip()
            manufacturer_url = response.urljoin(manufacturer.attrib['href'])
            yield scrapy.Request(manufacturer_url, callback=self.parse_categories, 
                                 meta={'manufacturer_name': manufacturer_name})

    def parse_categories(self, response):
        manufacturer_name = response.meta['manufacturer_name']
        for category in response.css('.c_container.allmakes.allcategories ul li a'):
            category_url = response.urljoin(category.attrib['href'])
            yield scrapy.Request(category_url, callback=self.parse_models, 
                                 meta={'manufacturer_name': manufacturer_name, 'category': category_url.split('/')[-2]})

    def parse_models(self, response):
        manufacturer_name = response.meta['manufacturer_name']
        category = response.meta['category']
        for model in response.css('.c_container.allmodels a'):
            model_url = response.urljoin(model.attrib['href'])
            yield scrapy.Request(model_url, callback=self.parse_parts, 
                                 meta={'manufacturer_name': manufacturer_name, 'category': category, 'model': model_url.split('/')[-2]})

    def parse_parts(self, response):
        manufacturer_name = response.meta['manufacturer_name']
        category = response.meta['category']
        model = response.meta['model']

        parts_data = []
        for item in response.css('.c_container.allparts li a'):
            part_text = item.css('::text').get()
            
            if ' - ' in part_text:
                part_number, part_category = part_text.split(' - ', 1)
            else:
                part_number = part_text
                part_category = ""

            entry = {
                'manufacturer': manufacturer_name,
                'category': category,
                'model': model,
                'part_number': part_number.strip(),
                'part_category': part_category.strip()
            }
            parts_data.append(entry)

        # Save data to the database
        store_to_db(parts_data)
