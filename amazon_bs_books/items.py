# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonBsBooksItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    category = scrapy.Field()
    genre = scrapy.Field()
    image_url = scrapy.Field()
    url = scrapy.Field()
    amazon_link = scrapy.Field()
    author = scrapy.Field()
    publication_date = scrapy.Field()
    total_pages = scrapy.Field()
    publisher = scrapy.Field()
    isbn = scrapy.Field()
    stars = scrapy.Field()
    catone = scrapy.Field()
    cattwo = scrapy.Field()
    catthree = scrapy.Field()
    # recommendone = scrapy.Field()
    recommendtwo = scrapy.Field()
    recommendthree = scrapy.Field()
    # reauthone = scrapy.Field()
    reauthtwo = scrapy.Field()
    reauththree = scrapy.Field()
    about_author = scrapy.Field()
    
