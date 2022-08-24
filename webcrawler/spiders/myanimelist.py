import scrapy


class MyanimelistAnimeSpider(scrapy.Spider):
    name = 'mal:anime'
    allowed_domains = ['myanimelist.net']
    start_urls = ['https://myanimelist.net/topanime.php']

    def parse(self, response):
        for tr in response.css("tr.ranking-list"):
            href = tr.css("a::attr(href)").get()
            if href:
                yield scrapy.Request(url=href, callback=self.parse_item)

        next_page = response.css("a.next::attr(href)").get()
        if next_page:
            if next_page.startswith("?"):
                next_page = self.start_urls[0] + next_page
            yield scrapy.Request(url=next_page)

    def parse_item(self, response):
        item = {"title": None}
        for data in response.css("table .spaceit_pad"):
            if data.css("span"):
                _, key, *value = data.css("::text").extract()
                if key.endswith(":"):
                    key = key[:-1].strip().lower()

                # cleaning up
                value = list(map(lambda y: y.strip(),
                    filter(lambda x: x.strip("\n ,"), value)))

                if len(value) == 1 or key in ("score", "ranked"):
                    value = value[0]
                else:
                    value = ", ".join(sorted(set(value)))
                item[key] = value

        if item.get("english"):
           item["title"] = item.pop("english")
        elif item.get("japanese"):
           item["title"] = item.pop("japanese")

        item["synopsis"] = response.css("*[itemprop='description']::text").get()
        yield item

class MyanimelistMangaSpider(MyanimelistAnimeSpider):
    name = "mal:manga"
    start_urls = ['https://myanimelist.net/topmanga.php']

    def parse_item(self, response):
        pass

class MyanimelistCharacterSpider(MyanimelistAnimeSpider):
    name = "mal:character"
    start_urls = ['https://myanimelist.net/character.php']

    def parse_item(self, response):
        pass

class MyanimelistPeopleSpider(MyanimelistAnimeSpider):
    name = "mal:people"
    start_urls = ['https://myanimelist.net/people.php']

    def parse_item(self, response):
        pass
