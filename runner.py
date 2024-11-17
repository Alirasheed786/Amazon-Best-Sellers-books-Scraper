import time
import argparse

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from amazon_bs_books.spiders.bs_books import BsBooksSpider


def main(**kwargs):
    settings = get_project_settings()
    # settings['CONCURRENT_REQUESTS'] = 25
    # settings['JOBDIR'] = './job'

    process = CrawlerProcess(settings)

    process.crawl(BsBooksSpider, **kwargs)
    process.start()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="provide list of items to scrape as boolean (True/False)")
    parser.add_argument("-a", "--asin", help="for product asin", type=bool, default=False)
    parser.add_argument("-t", "--title", help="for product title ", type=bool, default=False)
    parser.add_argument("-s", "--shipped_by", help="for shipped by", type=bool, default=False)
    parser.add_argument("-r", "--average_rating", help="for average ratings", type=bool, default=False)
    parser.add_argument("-n", "--no_of_ratings", help="for number of ratings", type=bool, default=False)
    parser.add_argument("-p", "--product_price", help="for product price", type=bool, default=False)
    parser.add_argument("-v", "--product_availibility", help="for product availibility", type=bool, default=False)
    parser.add_argument("-sf", "--shipping_fee", help="for shipping fee", type=bool, default=False)
    parser.add_argument("-f", "--product_features", help="for product features", type=bool, default=False)
    parser.add_argument("-td", "--product_technical_details", help="for product technical details", type=bool, default=False)
    parser.add_argument("-c", "--customer_reviews", help="for customer reviews", type=bool, default=False)
    parser.add_argument("-b", "--best_sellers_rank", help="for best sellers rank", type=bool, default=False)
    parser.add_argument("-d", "--date_first_available", help="for date first available", type=bool, default=False)
    parser.add_argument("-i", "--images", help="for images", type=bool, default=False)
    parser.add_argument("-u", "--url", help="to get product URL", type=bool, default=False)

    args = parser.parse_args()

    arguments = {}
    # if args.asin:
    #     arguments.update({'asin': True})
    # if args.title:
    #     arguments.update({'product_title': True})
    # if args.shipped_by:
    #     arguments.update({'shipped_by': True})
    # if args.average_rating:
    #     arguments.update({'average_rating': True})
    # if args.no_of_ratings:
    #     arguments.update({'no_of_ratings': True})
    # if args.product_price:
    #     arguments.update({'product_price': True})
    # if args.product_availibility:
    #     arguments.update({'product_availibility': True})
    # if args.shipping_fee:
    #     arguments.update({'shipping_fee': True})
    # if args.product_features:
    #     arguments.update({'product_features': True})
    # if args.product_technical_details:
    #     arguments.update({'product_technical_details': True})
    # if args.customer_reviews:
    #     arguments.update({'customer_reviews': True})
    # if args.best_sellers_rank:
    #     arguments.update({'best_sellers_rank': True})
    # if args.date_first_available:
    #     arguments.update({'date_first_available': True})
    # if args.images:
    # arguments.update({'image_urls': True})
    # if args.url:
    #     arguments.update({'url': True})

    # if arguments:
    main(**arguments)