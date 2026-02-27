import scrapy
from scrapy_playwright.page import PageMethod


class GoogleFinanceSpider(scrapy.Spider):
    name = "google_finance"

    def start_requests(self):
        # Send a request to Google Finance with Playwright enabled
        yield scrapy.Request(
            url="https://www.google.com/finance/quote/GOOG:NASDAQ",
            meta={
                "playwright": True,  # Enables Playwright for JavaScript rendering
                "playwright_page_methods": [
                    # Wait for the stock price element to appear
                    PageMethod("wait_for_selector", "div.YMlKec"),
                ],
            },
            callback=self.parse,  # Call the parse method after the page loads
        )

    def parse(self, response):
        # Extract the stock price from the loaded page
        price = response.css("div.YMlKec::text").get()
        if price:
            self.log(f"Google stock price: {price}")
        else:
            self.log("Failed to extract the price.")
