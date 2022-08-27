import scrapy
import re


class AnimeplanetSpider(scrapy.Spider):
    name = 'anime-planet'
    allowed_domains = ['www.anime-planet.com']
    start_urls = ['http://www.anime-planet.com/anime/all']

    def parse(self, response):
        for li in response.css("ul li.card"):
            yield scrapy.Request(url="http://www.anime-planet.com" + li.css("a::attr(href)").get(), callback=self.parse_item)

        next_page = response.css("li.next a::attr(href)").get()
        if next_page:
            yield scrapy.Request(url="http://www.anime-planet.com" + next_page)

    def parse_item(self, response):
        type_, eps = re.search(r"\s*([^\s]+)\s*\(([^)]+)", response.css(".type::text").get()).groups()
        item = {
            "title": response.css("h1[itemprop='name']::text").get(),
            "alternative title": response.css(".aka::text").get("").strip()[11:],
            "studios": response.css("section.entryBar div a::text").get(),
            "type": type_,
            "episodes": eps,
            "year": response.css(".iconYear::text").get("").strip(),
            "season": response.css(".iconYear ~ a::text").get(),
            "average rating": response.css(".avgRating::attr(title)").get(),
            "rank": (response.css("section.entryBar div::text")[-1].get() or "").strip()[5:],
            "synopsis": response.css(".entrySynopsis p::text").get("").strip(),
            "notes": response.css(".entrySynopsis .notes p::text").get(),
            "tags": [tag.get().strip() for tag in response.css('[data-tooltip="tags"]::text')],
            "url": response.url
        }

        yield item
