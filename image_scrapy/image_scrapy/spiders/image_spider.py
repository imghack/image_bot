import scrapy
import re

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from image_scrapy.image_scrapy.items import  *
from image_scrapy.image_scrapy.scrapy_option import  get_options


class ImageSpider(scrapy.Spider):

    """ Params url for scrapy :
     url
     image_selector
     image_link_selector
     image_title_selector
     image_keywords_selector
     next_page_selector
     """

    name = "images_spider"

    def __init__(self, urls=None):
        self.option = get_options(urls)
        self.start_urls = [self.option['url']]

    def parse(self, response):

        def extract_with_css(image_respons,query):
            return image_respons.css(query).extract_first()

        for next_image in response.css(self.option['imagecss']):
            if re.match('http',extract_with_css(next_image, self.option['imagelinkcss'])) != None:
                item = ImageScrapyItem()
                item['link'] = extract_with_css(next_image, self.option['imagelinkcss'])
                item['title'] = extract_with_css(next_image, self.option['imagetitlecss'])
                item['keywords'] = extract_with_css(next_image, self.option['imagekeywordscss'])
                yield item

        for next_image in response.css(self.option['nextpagecss']):
            yield response.follow(next_image, self.parse)


def start_spider(url):
    process = CrawlerProcess(get_project_settings())
    process.crawl(ImageSpider, urls=url)
    process.start()


if __name__ == '__main__':
   start_spider('https://pixabay.com/en/editors_choice')
