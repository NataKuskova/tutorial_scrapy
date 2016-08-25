import scrapy
from scrapy.shell import inspect_response


class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['https://www.google.com.ua/search?q=scrapy']

    def parse(self, response):
        # inspect_response(response, self)
        # for url in response.css('ul li a::attr("href")').re('.*/category/.*'):
        #     yield scrapy.Request(response.urljoin(url), self.parse_titles)
        for item in response.xpath('//div[contains(@id, "search")]//div[contains(@class, "g")]'):
            yield {'href': item.xpath('h3[contains(@class, r)]/a').xpath('@href').extract(),
                   'text': item.xpath('div[contains(@class, s)]//span/text()').extract()}


