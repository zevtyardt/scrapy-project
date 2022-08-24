
# Scrapy based Projects
These are collection of some of my web scraping projects with scrapy. Feel free to use them, modify them and suggest modifications.

## Requirements:
1. [Python3.x](https://www.python.org/)
2. [Scrapy framework](https://scrapy.org/)
3. [Sqlalchemy](https://sqlalchemy.org)

see: [requirements.txt](/requirements.txt)

## List Crawlers:
1. **myanimelist:anime**
   | id | title | synonyms | japanese | french | type | episode | statu | aired | premiered | broadcast | producers | licensors | studio | source | genre | theme | demographic | duration | rating | score | ranked | popularity | members | favorite |
   |---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
   | 1 | Fullmetal Alchemist: Brotherhood | Hagane no Renkinjutsushi: Fullmetal [...] | 鋼の錬金術師 FULLMETAL ALCHEMIST | Fullmetal Alchemist Brotherhood | TV | 64 | Finished Airing | Apr 5, 2009 to Jul 4, 2010 | Spring 2009 | Sundays at 17:00 (JST) | Aniplex, Mainichi Broadcasting System, [...] | Aniplex of America, Funimation | Bones | Manga | Action, Adventure, Drama, Fantasy | Military | Shounen | 24 min. per ep. | R - 17+ (violence & profanity) | 9.13 | #1 | #3 | 2,961,372 | 206,576 |
   | 2 | Gintama: Enchousen | Gintama' (2012), Gintama' Overdrive, Kintama | 銀魂' 延長戦 |  | TV | 13 | Finished Airing | Oct 4, 2012 to Mar 28, 2013 | Fall 2012 | Thursdays at 18:00 (JST) | Aniplex, Dentsu, Miracle Bus, Shueisha, TV Tokyo | None found,, add some | Sunrise | Manga | Action, Comedy, Sci-Fi | Gag Humor, Historical, Parody, Samurai | Shounen | 24 min. per ep. | PG-13 - Teens 13 or older | 9.04 | #8 | #697 | 288,900 | 2,851 |
   | 3 | Fate/stay night: Heaven's Feel - III. Spring Song | Fate/stay night Movie: Heaven's Feel 3 | 劇場版「Fate/stay night [Heaven's Feel] [...] | Fate/stay night: Heaven's Feel - III. Spring Song | Movie | 1 | Finished Airing | Aug 15, 2020 |  |  | Aniplex, Kadokawa, Notes | Aniplex of America | ufotable | Visual novel | Action, Fantasy, Supernatural |  |  | 2 hr. 2 min. | R - 17+ (violence & profanity) | 8.70 | #50 | #704 | 286,887 | 7,090 |
   | 4 | ヴィンランド・サガ |  |  |  | TV | 24 | Finished Airing | Jul 8, 2019 to Dec 30, 2019 | Summer 2019 | Mondays at 00:10 (JST) | Dentsu, Kodansha, Production I.G, Twin Engine | Sentai Filmworks | Wit Studio | Manga | Action, Adventure, Drama | Historical | Seinen | 24 min. per ep. | R - 17+ (violence & profanity) | 8.73 | #44 | #95 | 1,155,351 | 34,908 |
   | 5 | 86 Eighty-Six Part 2 |  | 86―エイティシックス― |  | TV | 12 | Finished Airing | Oct 3, 2021 to Mar 19, 2022 | Fall 2021 | Sundays at 00:00 (JST) | Aniplex, Bandai Spirits, Kadokawa | None found,, add some | A-1 Pictures | Light novel | Action, Drama, Sci-Fi | Mecha, Military |  | 23 min. per ep. | R - 17+ (violence & profanity) | 8.72 | #45 | #571 | 339,645 | 9,963 |

   _and more.._

1. **kusonime**
   | id | title | url | genre | thumbnail | japanese | seasons | producers | type | status | total_episode | score | duration | released_on | sinopsis | download_data |
   |---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
   | 1 | Shikong Zhi Xi (Time Space Rift) | https://kusonime.com/shikong-zhi-xi-batch- [...] | Action, Anime ONA | https://kusonime.com/wp- [...] | 时空之隙 | Anime ONA | B.CMAY PICTURES, bilibili | ONA | Completed | 13 | 6.49 | 21 min. per ep. | Apr 15, 2022 | Energi yang tidak stabil dari dunia saat ini [...] | {'name': 'Download Shikong Zhi Xi Batch [...] |
   | 2 | Yuuki Yuuna wa Yuusha de Aru: Washio Sumi no Shou | https://kusonime.com/yuuki-yuuna-washio- [...] | Drama, Fantasy, Magic, Slice of Life, Fall 2017 | https://kusonime.com/wp- [...] | 結城友奈は勇者である -鷲尾須美の章- | Fall 2017 | Pony Canyon | BD | Completed | 6 | 7.67 | 24 min. per ep. | Oct 07, 2017 | pada tahun 298 dari era para dewa, Sumi [...] | {'name': 'Download Yuuki Yuuna wa Yuusha de [...] |
   | 3 | Yuuki Yuuna wa Yuusha de Aru: Washio Sumi no [...] | https://kusonime.com/yuuki-yuuna-wa-yuusha- [...] | Drama, Fantasy, Magic, Slice of Life, Anime Movie | https://kusonime.com/wp- [...] | 結城友奈は勇者である -鷲尾須美の章- 第３章「やくそく」 | Anime Movie | Studio Gokumi | Movie | Completed | 1 | 8.02 | 48 min | Jul 08, 2017 | Movie tiga dan juga terakhir dari trilogi. [...] | {'name': 'Download Yuuki Yuuna wa Yuusha de [...] |
   | 4 | Yuuki Yuuna wa Yuusha de Aru: Yuusha no Shou | https://kusonime.com/yuuki-yuuna-wa-yuusha- [...] | Drama, Fantasy, Magic, Slice of Life, Fall 2017 | https://kusonime.com/wp- [...] | 結城友奈は勇者である -勇者の章- | Fall 2017 | Pony Canyon | BD | Completed | 6 | 7.64 | 24 min. per ep. | Nov 25, 2017 | kelanjutan dari cerita Yuki Yuna atau season [...] | {'name': 'Download Yuuki Yuuna wa Yuusha de [...] |
   | 5 | TENSURA : Sukuwareru Ramiris | https://kusonime.com/sukuwareru-ramiris- [...] | Comedy, Fantasy, Anime ONA | https://kusonime.com/wp- [...] | 救われるラミリス | Anime ONA | N/A | ONA | Completed | 2 | 6.18 | 2 min. per ep. | Mar 19, 2022 | Episode spesial melalui streaming youtube [...] | {'name': 'Download TENSURA : Sukuwareru [...] |

   _and more.._

