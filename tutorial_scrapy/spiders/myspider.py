import scrapy
from scrapy.shell import inspect_response
from tutorial_scrapy.items import TutorialScrapyItem


class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    allowed_domains = ['google.com.ua']
    start_urls = ['https://www.google.com.ua/search?q=scrapy']

    def parse(self, response):
        # inspect_response(response, self)
        sites = response.xpath(
            '//div[contains(@id, "search")]//div[contains(@class, "g")]'
        )
        for site in sites:
            item = TutorialScrapyItem()
            item['url'] = site.xpath(
                'h3[contains(@class, r)]/a').xpath('@href').extract()
            item['text'] = site.xpath(
                'div[contains(@class, s)]//span/text()').extract()
            yield item

        next_page = response.xpath(
            '//table[contains(@id, "nav")]//tr/td[last()]/a/@href').extract()
        page_4 = response.xpath(
            '//table[contains(@id, "nav")]//tr/td/a[text()="4"]/@href').extract()

        if next_page and next_page != page_4:
            url = response.urljoin(next_page[0])
            yield scrapy.Request(url, self.parse)

