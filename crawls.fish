for i in $argv
    timeout -s SIGINT 5 scrapy crawl $i
end
