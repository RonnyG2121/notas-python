import scrapy
from almacen_precios.items import ProductItem


class ProductSpider(scrapy.Spider):
    name = "product"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/"]

    def parse(self, response):
        item = ProductItem()
        for product in response.css("article.product_pod"):
            item["title"] = product.css("h3 > a::attr(title)").get()
            item["price"] = product.css(".price_color::text").get()
            item["url"] = product.css("h3 > a::attr(href)").get()
            yield item

        next_page = response.css("li.next > a::attr(href)").get()
        if next_page:
            next_page_url = response.urljoin(next_page)
            yield scrapy.Request(url=next_page_url, callback=self.parse)
