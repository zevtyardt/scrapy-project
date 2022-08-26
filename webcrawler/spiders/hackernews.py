import scrapy


class HackernewsSpider(scrapy.Spider):
    name = 'hackernews'
    allowed_domains = ['news.ycombinator.com']
    start_urls = ['http://news.ycombinator.com/']

    unique_key = "id"
    outputs = ["title"]

    def parse(self, response):
        itemlist = response.css(".itemlist")
        for tr in itemlist.css("tr.athing"):
            id_ = tr.css("::attr(id)").get()
            titlelink = tr.css(".titlelink")

            url = titlelink.css("::attr(href)").get()
            if not url.startswith("http"):
                url = self.start_urls[0] + url

            yield {
                "id": id_,
                "title": titlelink.css("::text").get(),
                "url": url,
                "from site": tr.css(".sitestr::text").get(),
                "rank": tr.css(".rank::text").get().strip("."),
                "score": itemlist.css(f"#score_{id_}::text").get(),
                "user": itemlist.css(f"#score_{id_} ~ a.hnuser::text").get(),
                "date": itemlist.css(f"#score_{id_} ~ span::attr(title)").get()
            }

        next_page = response.css("a[rel='next']::attr(href)").get()
        if next_page:
            yield scrapy.Request(self.start_urls[0] + next_page)
