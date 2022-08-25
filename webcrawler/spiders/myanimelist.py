import scrapy
import re


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
        item = {"title": None, "url": response.url}
        for data in response.css("table .spaceit_pad"):
            if data.css("span"):
                # cleaning up
                data = list(map(lambda y: y.strip(),
                                filter(lambda x: x.strip("\n ,"),
                                       data.css("::text").extract()
                                       )))

                key, *value = data
                if key.endswith(":"):
                    key = key[:-1].strip().lower()

                if len(value) == 1 or key in ("score", "ranked"):
                    value = value[0]
                else:
                    value = list(sorted(set(value)))
                item[key] = value

        if item.get("english"):
            item["title"] = item.pop("english")
        elif item.get("japanese"):
            item["title"] = item.pop("japanese")

        item["synopsis"] = "".join(response.css(
            "*[itemprop='description']::text").getall())
        yield item


class MyanimelistMangaSpider(MyanimelistAnimeSpider):
    name = "mal:manga"
    start_urls = ['https://myanimelist.net/topmanga.php']


class MyanimelistCharacterSpider(MyanimelistAnimeSpider):
    name = "mal:character"
    start_urls = ['https://myanimelist.net/character.php']
    unique_key = "name"

    def parse_item(self, response):
        item = {"name": (response.css(
            ".breadcrumb ~ .normal_header::text").get() or "").strip()}
        item["url"] = response.url
        item["japanese"] = (response.css(
            ".breadcrumb ~ .normal_header small::text").get() or "").strip("()")

        source = re.search(
            f"[^(]+\(([^)]+)", response.css("title::text").get() or "")
        if source:
            item["source"] = source.group(1)

        desc, bio = [], {}
        for i in response.css("table td::text"):
            text = i.get().strip()
            if not text:
                continue
            chara_info = re.search("^([a-zA-Z ]+): ([^>]+)", text)
            if chara_info:
                k, v = chara_info.groups()
                bio[k.lower()] = v.strip()
            else:
                desc.append(text)
        item["favorites"] = bio.pop("member favorites")
        item["biodata"] = bio
        item["description"] = "\n\n".join(desc)
        yield item


"""
class MyanimelistPeopleSpider(MyanimelistCharacterSpider):
    name = "mal:people"
    start_urls = ['https://myanimelist.net/people.php']

    def parse_item(self, response):
        pass
"""
