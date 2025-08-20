import scrapy

class BooksSpider(scrapy.Spider):
    name = "books"
    start_urls = ["https://books.toscrape.com/"]

    def parse(self, response):
        for livro in response.xpath('//article[@class="product_pod"]'):
            yield{
                "imagem": livro.xpath('.//img[@class="thumbnail"]/@src').get(),
                "titulo":  livro.xpath('.//h3/a/@title').get(),
                "preco": livro.xpath('.//p[@class="price_color"]/text()').get(),
                "estoque": livro.xpath('//p[@class="instock availability"]/text()[2]').get().strip()
            }
            
