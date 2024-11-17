<h1>Amazon Best Sellers Books Scraper</h1>
This project scrapes best seller books from amazon.com, and stores the data into an Airtable

<h2>Pre-requisites</h2>
<ol>
  <li>Python3+</li>
  <li>ScrapingBee API key</li>
  <li>Airtable API key</li>
</ol>
<h2>Instructions</h2>
<ol>
  <li>Install requirements.txt\n
      `pip install -r requirements.txt
  </li>
  <li>Add ScrapingBee API key to settings.py\n
      `SCRAPINGBEE_API_KEY = 'Your API key'`
  </li>
  <li>Add Airtable API credentials to config.json\n
      `"api_token": "Your API Token"`\n
      `"base_id": "Your base ID"`\n
      `"table_name": "Table name"`\n
  </li>
  <li>Run the Scraper
      `scrapy crawl bs_books`\n
    or\n
      `scrapy crawl bs_books -o books.csv`\n
    (.csv, .json, and .xml are supported)
      
    
  </li>
  
</ol>
