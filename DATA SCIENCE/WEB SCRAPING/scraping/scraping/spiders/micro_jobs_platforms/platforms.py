import scrapy


class PlatformsSpider(scrapy.Spider):
    name = 'platforms'
    allowed_domains = ['bloggingcage.com'] 
    start_urls = ['https://www.bloggingcage.com/make-money-online-by-doing-micro-jobs/']
    
    def parse(self, response):
        self.log('I just visited: '+ response.url)
        for webpage in response.css('ul.ez-toc-list-level-3'):
            web = {
                'rank' : webpage.css('li.ez-toc-heading-level-3 > a::text').extract(),
                'links' : webpage.css('li.ez-toc-heading-level-3 > a::attr(href)').extract(),
            }
            yield web
    