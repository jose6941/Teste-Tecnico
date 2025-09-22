import scrapy

class QuotesSpider(scrapy.Spider):
    name = "videos"
    start_urls = ["https://sandbox.oxylabs.io/products"]

    def parse(self, response):
        for video in response.xpath('//div[@class="product-card.css-e8at8d.eag3qlw10"]'):
            yield {
                "texto": video.xpath('.//h4[@class="title.css-7u5e79.eag3qlw7"]').get(),
                "tags": video.xpath('.//p[@class="category.css-8fdgzc.eag3qlw9"]/a[@class="css-1pewyd6.eag3qlw8"]/text()').getall(),
                "descricao": video.xpath('.//p[@class="description.css-cput12.eag3qlw5"]/text()').get(),
                "estoque": video.xpath('.//p[@class="in-stock.css-1w904rj.eag3qlw1"]/text()').get(),
            }

        
