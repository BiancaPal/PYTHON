import scrapy


class FreelancerSpider(scrapy.Spider):
    name = 'freelancer'
    allowed_domains = ['freelancer.com']
    start_urls = ['https://www.freelancer.com/jobs/']

    def parse(self, response):
        self.log('I just visited: '+ response.url)
        for service in response.css('div.JobSearchCard-item'):
            item =  {
                'name_job': service.css('a.JobSearchCard-primary-heading-link::text').extract(),
                'price': service.css(' div.JobSearchCard-secondary-price::text').extract(),
                'bids': service.css(' div.JobSearchCard-secondary-entry::text').extract(),
            }
            yield item

        # follow pagination link
        next_page_url = response.css('li.Pagination-item > a::attr(href)').extract()
        if next_page_url:
            next_page_url = response.urljoin(next_page_url)
            yield scrapy.Request(url=next_page_url, callback=self.parse)
