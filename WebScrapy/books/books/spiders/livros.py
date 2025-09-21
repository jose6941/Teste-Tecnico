import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = ["https://quotes.toscrape.com/"]

    def parse(self, response):
        for quote in response.xpath('//div[@class="quote"]'):
            yield {
                "texto": quote.xpath('.//span[@class="text"]/text()').get(),
                "autor": quote.xpath('.//small[@class="author"]/text()').get(),
                "tags": quote.xpath('.//div[@class="tags"]/a[@class="tag"]/text()').getall(),
            }

        prox_pagina = response.xpath('//li[@class="next"]/a/@href').get()
        if prox_pagina:
            yield response.follow(prox_pagina, callback=self.parse)
