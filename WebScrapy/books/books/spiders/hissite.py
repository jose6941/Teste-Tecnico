import scrapy


class HissiteSpider(scrapy.Spider):
    name = "hissite"
    start_urls = ["https://www.scrapethissite.com/pages/"]

    def parse(self, response):
        for box in response.xpath('//div[@class="page"]'):
            yield{
                "titulo": box.xpath('.//h3[@class="page-title"]/a/text()').get(),
                "descricao": box.xpath('.//p[@class="lead session-desc"]/text()').get().strip()
            }
