# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import json
from pyairtable import Table


class AmazonBsBooksPipeline:

    with open("./config.json", mode="r") as f:
        raw_json = json.load(f)

    api_key = raw_json["api_token"]
    base_id = raw_json["base_id"]
    table_name = raw_json["table_name"]

    def open_spider(self, spider):
        self.table = Table(self.api_key, self.base_id, self.table_name)
        self.records = self.table.all()

    def process_item(self, item, spider):
        for i in self.records:
            if (i.get("fields").get("isbn") != None) and (item.get("isbn") != None):
                if item.get("isbn") in i.get("fields").get("isbn"):
                    return item

            elif (not item.get("isbn")) and (item.get("title") != None):
                if item.get("title") in i.get("fields").get("Name"):
                    return item

        temp_dict = {
            "Name": item.get("title"),
            "Book Title": item.get("title"),
            "Category": item.get("category"),
            "Genre": item.get("genre"),
            "Book Picture": [
                {
                    "url": item.get("image_url")
                }
            ] if item.get("image_url") else "",
            "URL": item.get("url"),
            # "Amazon Link": item.get("amazon_link"),
            "Author": item.get("author"),
            "publication date": item.get("publication_date"),
            "total pages": item.get("total_pages"),
            "publisher": item.get("publisher"),
            "isbn": item.get("isbn"),
            "stars": item.get("stars"),
            "catone": item.get("catone"),
            "cattwo": item.get("cattwo"),
            "catthree": item.get("catthree"),
            "recommendtwo": item.get("recommendtwo"),
            "recommendthree": item.get("recommendthree"),
            "about author": item.get("about_author"),
            "recauthtwo": item.get("reauthtwo"),
            "recauththree": item.get("reauththree")
        }

        self.table.create(temp_dict)

        return item
