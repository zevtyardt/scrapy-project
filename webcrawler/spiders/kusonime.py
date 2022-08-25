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
        item = {
            "title": (
                response.css(".clear ~ p strong::text").get() or
                response.css(".wp-post-image::attr(title)").get()
            ).strip(),
            "url": response.url,
            "genre": response.css("a[rel='tag']::text").extract(),
            "thumbnail": response.css(".wp-post-image::attr(src)").get()
        }

        for info in response.css(".info p"):
            data = info.css("::text").getall()
            if data[0].strip() == "Genre":
                continue

            if len(data) > 2:
                k, v = data[0], data[-1]
            else:
                k, v = data
            item[k.strip()] = v.strip(": ")
        item["sinopsis"] = response.css(".clear ~ p ::text").get().strip()

        downloads = []
        for ddl in response.css(".smokeddl"):
            name = ddl.css(".smokettl::text").get()
            if not name:
                continue

            data = []
            for smokeurl in ddl.css(".smokeurl"):
                data.append({
                  "desc": smokeurl.css("strong::text").get(),
                  "url": smokeurl.css("a::attr(href)").extract()
                })
            downloads.append({
                "name": name,
                "link": data})
        item["download_data"] = downloads
        yield item
