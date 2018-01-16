import scrapy

class QuotesSpider(scrapy.Spider):
    name = "images"
    start_urls = ['https://www.pexels.com/search/nature/']