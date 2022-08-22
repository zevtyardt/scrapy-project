import scrapy


class KusonimeSpider(scrapy.Spider):
    name = 'kusonime'
    allowed_domains = ['kusonime.com']
    start_urls = ['http://kusonime.com/']

    def parse(self, response):
        for i in response.css(".episodeye a::attr(href)"):
            yield scrapy.Request(url=i.get(), callback=self.parse_content)

        next_page = response.css("link[rel='next']::attr(href)")
        if next_page:
            yield scrapy.Request(url=next_page.get())

    def parse_content(self, response):
        yield {"title": response.css("title::text").get().split(" |")[0]}
