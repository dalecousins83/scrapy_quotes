import scrapy
import pandas as pd
from datetime import datetime

class QuoteSpider(scrapy.Spider):
    name="quotes"
    start_urls = [f"https://quotes.toscrape.com/page/{i}" for i in range(1,2)]

    def parse(self, response):

        quotes = response.css("div.quote")

        self.logger.info(f"found {len(quotes)} quotes")

        for quote in quotes:
            text = quote.css("span.text::text").get()
            author = quote.css("span small.author::text")

            yield{
                "text": text,
                "author": author
            }
