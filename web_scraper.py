import requests
from bs4 import BeautifulSoup
import logging

# Set up logging
logging.basicConfig(filename='scraping.log', 
                    level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Define the URL of the page you want to scrape
url = 'https://example.com'  # Replace with the actual URL

# Start the scraping process
logging.info(f'Starting to scrape the website: {url}')

try:
    # Send a GET request to the website
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        logging.info(f'Successfully retrieved the page: {url}')

        # Parse the page content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Example: Extract all the headings (h1, h2, etc.)
        headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
        
        logging.info('Extracted the following headings:')
        for heading in headings:
            logging.info(heading.get_text())

        # Example: Extract all the links (anchor tags)
        links = soup.find_all('a')
        
        logging.info('Extracted the following links:')
        for link in links:
            href = link.get('href')
            text = link.get_text()
            logging.info(f'Text: {text}, URL: {href}')
    else:
        logging.error(f'Failed to retrieve the page. Status code: {response.status_code}')

except requests.exceptions.RequestException as e:
    logging.error(f'Request failed: {e}')

logging.info('Scraping process completed.')

