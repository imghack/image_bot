import scrapy
import re

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from image_scrapy.image_scrapy.items import  *
from image_scrapy.image_scrapy.scrapy_option import  get_options


class ImageSpider(scrapy.Spider):

    """ Params url for scrapy :
     url
     images_ selector
     image_selector
     image_link_selector
     image_title_selector
     image_keywords_selector
     next_page_selector
     """
    """ First site :
        url =  https://pixabay.com/en/editors_choice
        ????images_css ='div.flex_grid'
        image_css ='div.item a img'
        image_link_css = 'div.item a img scr' 
        image_title_css = 'div.item a img title' 
        image_keywords_css ='div.item a img alt' 
        next_page_css='div.paginator a.pure-button::attr(href)
        # self.start_urls = ['https://pixabay.com/en/editors_choice']
        #self.images_css = 'div.flex_grid'
        #self.image_css ='div.item a img'
        #self.image_link_css = 'img::attr(src)'
        # self.image_title_css = 'img::attr(title)'
        # self.image_keywords_css = 'img::attr(alt)'

        """
    name = "images_spider"
    #start_urls = ['https://www.pexels.com/search/nature/']

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
                # yield {
                #     'link': extract_with_css(next_image, self.image_link_css),
                #     'title': extract_with_css(next_image, self.image_title_css),
                #     'keywords': extract_with_css(next_image, self.image_keywords_css)
                # }

def start_spider(url):
    process = CrawlerProcess(get_project_settings())
    process.crawl(ImageSpider, urls=url)
    process.start()


if __name__ == '__main__':
    s= start_spider('https://pixabay.com/en/editors_choice')
    print(s)