import scrapy


class UrbandictionarySpider(scrapy.Spider):
    name = 'urbandictionary'
    allowed_domains = ['www.urbandictionary.com']
    start_urls = ['http://www.urbandictionary.com/']

    unique_key = "id"
    outputs = ["id", "text"]

    def parse(self, response):
        for definition in response.css(".definition"):
            author, date = definition.css(".contributor ::text").getall()[1:]
            yield {
              "id": definition.css("::attr(data-defid)").get(),
              "text": "".join(definition.css(".word ::text").getall()),
              "meaning": "".join(definition.css(".meaning ::text").getall()),
              "example": "".join(definition.css(".example ::text").getall()).replace("\r", "\n"),
              "author": author.strip(),
              "date": date.strip()
            }

        next_page = response.css("a[rel='next']::attr(href)").get()
        if next_page:
            yield scrapy.Request(url=self.start_urls[0] + next_page)
