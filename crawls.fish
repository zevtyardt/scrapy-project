for i in (scrapy list | grep -v "^[ I]")
    timeout -s SIGINT 10 scrapy crawl $i
end
