import scrapy

class BooksSpider(scrapy.Spider):
    name = "books"
    start_urls = ["https://books.toscrape.com/"]

    def parse(self, response):
        for livro in response.css('.product_pod'):
            yield{
                "imagem": livro.css('.thumbnail ::attr(src)').get(),
                "titulo":  livro.css('.product_pod h3 a ::text').get(),
                "preco": livro.css('.price_color ::text').get(),
                "estoque": livro.xpath('//p[@class="instock availability"]/text()[2]').get().strip()
            }
            
