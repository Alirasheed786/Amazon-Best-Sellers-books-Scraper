import json
import scrapy
import scraper_helper as sh
from scrapy.loader import ItemLoader
from ..items import AmazonBsBooksItem
from scrapy_scrapingbee import ScrapingBeeSpider, ScrapingBeeRequest
from itemloaders.processors import TakeFirst


class BsBooksSpider(ScrapingBeeSpider):
    name = "bs_books"
    
    base_url = "https://www.amazon.com"

    headers = sh.get_dict(
    '''
    accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
    accept-encoding: gzip, deflate, br
    accept-language: en-US,en;q=0.9
    cache-control: no-cache
    cookie: session-id=135-0977884-7912814; session-id-time=2082787201l; i18n-prefs=USD; skin=noskin; ubid-main=134-8892929-3300361; lc-main=en_US; session-token=+2pmzzMqgPw6KEOY6CiandbMvwnCrlbA25xRnf6tHFJaArtl88ApjbtQ+s9ZhRHH45fH6Ngdp/fg/zHfC7up8TSF1UO/0wOjFX2t4SoNSc2c/6pgLh2eY35fcBaxbulDwsZ3hPz2mLx/ED+1sT4RMCN+4ZItenqymcBSGEXNEruw105zYgONWLPHIy36ZRPi; csm-hit=tb:8QCT5J68S0VPD43XDD03+s-4854Q6ZNY1KX2KPW74GD|1624962978059&t:1624962978059&adb:adblk_no
    downlink: 1.3
    ect: 3g
    pragma: no-cache
    rtt: 300
    sec-ch-ua: " Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"
    sec-ch-ua-mobile: ?0
    sec-fetch-dest: document
    sec-fetch-mode: navigate
    sec-fetch-site: same-origin
    sec-fetch-user: ?1
    upgrade-insecure-requests: 1
    user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36
    '''
    )

    def start_requests(self):
        url = "https://www.amazon.com/best-sellers-books-Amazon/zgbs/books/ref=zg_bs_unv_books_1_4736_1"
        yield ScrapingBeeRequest(
            url,
            params={
                "render_js": False
            },
            headers=self.headers,
            callback=self.parse,
        )

    def parse(self, response):
        # open_in_browser(response)
        for cat in response.xpath("//span[contains(@class, 'selected')]/parent::node()/following-sibling::node()//div[@role='treeitem']/a/@href").getall():
            yield ScrapingBeeRequest(
                url=self.base_url + cat,
                params={
                    "render_js": False
                },
                headers=self.headers,
                callback=self.parse_level_1,
            )

    def parse_level_1(self, response):
        category = response.xpath("//span[contains(@class, 'selected')]/text()").get()
        for cat in response.xpath("//span[contains(@class, 'selected')]/parent::node()/following-sibling::node()//div[@role='treeitem']/a/@href").getall():
            yield ScrapingBeeRequest(
                url=self.base_url + cat,
                params={
                    "render_js": False
                },
                headers=self.headers,
                callback=self.parse_level_2,
                cb_kwargs={
                    "category": category
                }
            )

        for link in response.xpath("//div[@id='gridItemRoot']//span[contains(text(), 'Paperback') or contains(text(), 'Hardcover')]/parent::node()/parent::node()/a[@tabindex='-1']/@href").getall():
            yield ScrapingBeeRequest(
                url=self.base_url + link,
                params={
                    "render_js": False
                },
                headers=self.headers,
                callback=self.parse_book,
                cb_kwargs={
                    "category": category,
                    "genre": category
                }
            )

        next_page = response.xpath("//a[contains(text(), 'Next')]/@href").get()
        if next_page:
            yield ScrapingBeeRequest(
                url=self.base_url + next_page,
                params={
                    "render_js": False
                },
                headers=self.headers,
                callback=self.parse_level_1,
            )

    def parse_level_2(self, response, category):
        genre = response.xpath("//span[contains(@class, 'selected')]/text()").get()
        for link in response.xpath("//div[@id='gridItemRoot']//span[contains(text(), 'Paperback') or contains(text(), 'Hardcover')]/parent::node()/parent::node()/a[@tabindex='-1']/@href").getall():
            yield ScrapingBeeRequest(
                url=self.base_url + link,
                params={
                    "render_js": False
                },
                headers=self.headers,
                callback=self.parse_book,
                cb_kwargs={
                    "category": category,
                    "genre": genre
                }
            )

        next_page = response.xpath("//a[contains(text(), 'Next')]/@href").get()
        if next_page:
            yield ScrapingBeeRequest(
                url=self.base_url + next_page,
                params={
                    "render_js": False
                },
                headers=self.headers,
                callback=self.parse_level_2,
                cb_kwargs={
                    "category": category
                }
            )

    def parse_book(self, response, category, genre):
        loader = ItemLoader(AmazonBsBooksItem(), response=response)
        loader.default_output_processor = TakeFirst()

        loader.add_xpath("title", "//h1/span[@id='productTitle']/text()")
        loader.add_xpath("title", "//span[@id='productTitle']/text()")
        loader.add_value("category", category)
        loader.add_value("genre", genre)
        loader.add_value("url", response.url)
        # loader.add_value("amazon_link", f"{response.url}&tag=bksum-20")
        loader.add_xpath("author", "//div[contains(@class, '_about-the-author')]//h2/text()")
        loader.add_xpath("author", "//span[@class='author notFaded']/a/text()")
        loader.add_xpath("publication_date", "(//div[@id='rpi-attribute-book_details-publication_date']/div)[3]/span/text()")
        loader.add_xpath("total_pages", "(//div[@id='rpi-attribute-book_details-fiona_pages']/div)[3]/span/text()")
        loader.add_xpath("publisher", "(//div[@id='rpi-attribute-book_details-publisher']/div)[3]/span/text()")
        loader.add_xpath("publisher", "((//div[@id='detailBullets_feature_div'])[1]//span[contains(text(), 'Publisher')]/following-sibling::node())[2]/text()")
        loader.add_xpath("isbn", "((//div[@id='detailBullets_feature_div'])[1]//span[contains(text(), 'ISBN')]/parent::node()/span)[2]/text()")
        loader.add_xpath("stars", "(//span[contains(text(), 'out of 5')]/parent::node()/span)[3]/text()", re="\d.\d")
        loader.add_xpath("catone", "(//ul[@class='a-unordered-list a-nostyle a-vertical zg_hrsr']/li/span/a/text())[1]")
        loader.add_xpath("cattwo", "(//ul[@class='a-unordered-list a-nostyle a-vertical zg_hrsr']/li/span/a/text())[2]")
        loader.add_xpath("catthree", "(//ul[@class='a-unordered-list a-nostyle a-vertical zg_hrsr']/li/span/a/text())[3]")
        loader.add_xpath("recommendtwo", "(//span[contains(@class, 'fbt_fbt-desktop_title')])[2]/text()")
        loader.add_xpath("recommendthree", "(//span[contains(@class, 'fbt_fbt-desktop_title')])[3]/text()")
        loader.add_xpath("reauthtwo", "(//span[contains(@class, 'fbt_fbt-desktop_detail-row-element')])[3]/text()")
        loader.add_xpath("reauththree", "(//span[contains(@class, 'fbt_fbt-desktop_detail-row-element')])[5]/text()")
        loader.add_xpath("about_author", "//div[@class='a-cardui _about-the-author-card_carouselItemStyles_expander__3Fm-M']//p/text()")
        loader.add_xpath("image_url", "//div[@id='img-canvas']/img/@src")
        loader.add_xpath("image_url", "//div[@id='imgTagWrapperId']/img/@src")

        yield loader.load_item()

