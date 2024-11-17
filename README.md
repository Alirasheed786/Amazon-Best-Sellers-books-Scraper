<h1>Amazon Best Sellers Books Scraper</h1>
This project scrapes best-seller books from amazon.com and stores the data in an Airtable table

<h2>Pre-requisites</h2>
<ol>
  <li>Python3+</li>
  <li>ScrapingBee API key</li>
  <li>Airtable API key</li>
</ol>
<h2>Instructions</h2>
<ol>
  <li>Install requirements.txt<br>
      `pip install -r requirements.txt`
  </li>
  <li>Add ScrapingBee API key to settings.py<br>
      `SCRAPINGBEE_API_KEY = 'Your API key'`
  </li>
  <li>Add Airtable API credentials to config.json<br>
      `"api_token": "Your API Token"`<br>
      `"base_id": "Your base ID"`<br>
      `"table_name": "Table name"`<br>
  </li>
  <li>Run the Scraper<br>
      `scrapy crawl bs_books`<br>
    or<br>
      `scrapy crawl bs_books -o books.csv`<br>
    (.csv, .json, and .xml are supported)
      
    
  </li>
  
</ol>
