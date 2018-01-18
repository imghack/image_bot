import scrapy

from scrapy.crawler import  CrawlerProcess
from scrapy.utils.project import get_project_settings

class ImageSpider(scrapy.Spider):
    name = "images_spider"
    #start_urls = ['https://www.pexels.com/search/nature/']

    def __init__(self, urls= None):
        self.start_urls= urls

    def parse(self, response):
        def extract_with_css(query):
            return response.css(query).extract_first().strip()
        for next_image in response.css('article.photo-item'):
            # print("-------------------------------------------------------------------------------------------")
            # print (next_image.extract_first())
            yield {
                    'title': next_image.css('img').xpath('@alt').extract_first(),
                    'link': next_image.css('img').xpath('@src').extract_first()
                  }

process = CrawlerProcess(get_project_settings())
process.crawl(ImageSpider, urls =['https://www.pexels.com/search/nature/'])
process.start()
