import scrapy
from scrapy_playwright.page import PageMethod
from almacen_precios.items import BackmarketItem


class BackmarketSpider(scrapy.Spider):
    name = "backmarket"
    allowed_domains = ["www.backmarket.es"]
    start_urls = ["https://www.backmarket.es/es-es"]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(
                url,
                meta={
                    "playwright": True,
                    "playwright_include_page": True,
                    "playwright_page_methods": [
                        # Esperamos a que aparezca el contenedor de productos real
                        PageMethod(
                            "wait_for_selector", 'div[data-test="product-card"]'
                        ),
                        PageMethod("wait_for_timeout", 2000),
                    ],
                },
                callback=self.parse,
            )

    async def parse(self, response):
        self.logger.info(f"Parseando: {response.url}")

        # Selector de tarjeta actualizado según el HTML
        for card in response.css('div[data-test="product-card"]'):
            # El título está en un h2 o span con data-test="product-title"
            name = card.css('[data-test="product-title"]::text').get()

            # El precio se encuentra en un contenedor con data-spec="price"
            # Usamos un selector que busque el símbolo € si el específico falla
            precio = card.css('[data-spec="price"] span::text').get()
            if not precio:
                precio = card.xpath('.//*[contains(text(), "€")]/text()').get()

            # La URL está en el enlace que envuelve o contiene el producto
            url = card.css('a[href*="/p/"]::attr(href)').get()

            if name and precio and url:
                item = BackmarketItem()
                item["nombre"] = name.strip()
                # Limpiamos caracteres extraños como el espacio no divisible (\xa0)
                item["precio"] = precio.replace("\xa0", " ").strip()
                item["url"] = response.urljoin(url.strip())
                yield item

        # ---------- PAGINACIÓN ----------
        # Buscamos el enlace "Siguiente" en la navegación
        next_page = response.css(
            'nav[aria-label="Pagination"] a[rel="next"]::attr(href)'
        ).get()

        if next_page:
            next_page = response.urljoin(next_page)
            self.logger.info(f"Siguiente página: {next_page}")

            yield scrapy.Request(
                next_page,
                callback=self.parse,
                meta={
                    "playwright": True,
                    "playwright_page_methods": [
                        PageMethod(
                            "wait_for_selector", 'div[data-test="product-card"]'
                        ),
                        PageMethod("wait_for_timeout", 2000),
                    ],
                },
            )
