# Amazon Best Sellers Books Scraper

This project scrapes best-seller books from amazon.com and stores the data in an Airtable table

## Pre-requisites

1. Python3+
2. ScrapingBee API key
3. Airtable API key

## Instructions

1. Install requirements.txt
   ```
   pip install -r requirements.txt
   ```

2. Add ScrapingBee API key to settings.py
   ```
   SCRAPINGBEE_API_KEY = 'Your API key'
   ```

3. Add Airtable API credentials to config.json
   ```
   "api_token": "Your API Token"
   "base_id": "Your base ID"
   "table_name": "Table name"
   ```

4. Run the Scraper
   ```
   scrapy crawl bs_books
   ```
   or
   ```
   scrapy crawl bs_books -o books.csv
   ```
   (.csv, .json, and .xml are supported)
