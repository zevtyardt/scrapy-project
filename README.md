
# Scrapy based Projects
These are collection of some of my web scraping projects with scrapy. Feel free to use them, modify them and suggest modifications.

## Requirements:
1. [Python3.x](https://www.python.org/)
2. [Scrapy framework](https://scrapy.org/)
3. [Sqlalchemy](https://sqlalchemy.org)

see: [requirements.txt](/requirements.txt)

## List Crawlers:
1. **kusonime**
   | id | title | url | genre | thumbnail | japanese | seasons | producers | type | status | total_episode | score | duration | released_on | sinopsis | download_data |
   |---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
   | 1 | Shikong Zhi Xi (Time Space Rift) | https://kusonime.com/shikong-zhi-xi-batch- [...] | Action, Anime ONA | https://kusonime.com/wp- [...] | 时空之隙 | Anime ONA | B.CMAY PICTURES, bilibili | ONA | Completed | 13 | 6.49 | 21 min. per ep. | Apr 15, 2022 | Energi yang tidak stabil dari dunia saat ini [...] | {'name': 'Download Shikong Zhi Xi Batch [...] |
   | 2 | Gaikotsu Kishi-sama Tadaima Isekai e Odekakechuu | https://kusonime.com/skeleton-knight-batch- [...] | Action, Fantasy, Spring 2022 | https://kusonime.com/wp- [...] | 骸骨騎士様、只今異世界へお出掛け中 | Spring 2022 | Pony Canyon, AT-X, DAX Production, Docomo [...] | BD | Completed | 12 | 7.31 | 23 min. per ep. | Apr 07, 2022 | selain Ainz-sama ada juga tengkorak [...] | {'name': 'Download Gaikotsu Kishi-sama [...] |
   | 3 | Yuuki Yuuna wa Yuusha de Aru: Washio Sumi no [...] | https://kusonime.com/yuuki-yuuna-wa-yuusha- [...] | Drama, Fantasy, Magic, Slice of Life, Anime Movie | https://kusonime.com/wp- [...] | 結城友奈は勇者である -鷲尾須美の章- 第３章「やくそく」 | Anime Movie | Studio Gokumi | Movie | Completed | 1 | 8.02 | 48 min | Jul 08, 2017 | Movie tiga dan juga terakhir dari trilogi. [...] | {'name': 'Download Yuuki Yuuna wa Yuusha de [...] |
   | 4 | Steamboy | https://kusonime.com/steamboy-bd-subtitle- [...] | Action, Adventure, Drama, Historical, [...] | https://kusonime.com/wp- [...] | スチームボーイ | Anime Movie | Bandai Visual, Dentsu, TBS, Imagica, Bandai, [...] | Movie | Completed | 1 | 7.33 | 2 hr. 6 min. | Jul 17, 2004 | Becerita tentang cowok 13 tahun bernama [...] | {'name': 'Download Movie Steamboy BD [...] |
   | 5 | Xiao Mo Tou Baolu La! (Busted! Darklord) | https://kusonime.com/xiao-mo-tou-baolu-la- [...] | Comedy, Anime ONA | https://kusonime.com/wp- [...] | 小魔头暴露啦！ | Anime ONA | N/A | ONA | Completed | 26 | 6.38 | 8 min. per ep. | Jan 15, 2022 | Dalam upaya untuk bertahan hidup, Yu Renjie, [...] | {'name': 'Download Xiao Mo Tou Baolu La! [...] |

   _and more.._

1. **myanimelist:anime**
   | id | title | synonyms | japanese | french | type | episodes | status | aired | premiered | broadcast | producers | licensors | studios | source | genres | theme | demographic | duration | rating | score | ranked | popularity | members | favorites | synopsis | german | spanish |
   |---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
   | 1 | Fullmetal Alchemist: Brotherhood | Hagane no Renkinjutsushi: Fullmetal [...] | 鋼の錬金術師 FULLMETAL ALCHEMIST | Fullmetal Alchemist Brotherhood | TV | 64 | Finished Airing | Apr 5, 2009 to Jul 4, 2010 | Spring 2009 | Sundays at 17:00 (JST) | Aniplex, Mainichi Broadcasting System, [...] | Aniplex of America, Funimation | Bones | Manga | Action, Adventure, Drama, Fantasy | Military | Shounen | 24 min. per ep. | R - 17+ (violence & profanity) | 9.13 | #1 | #3 | 2,961,579 | 206,595 | After a horrific alchemy experiment goes [...] |  |  |
   | 2 | Legend of the Galactic Heroes | LoGH, LotGH, Gin'eiden, GinEiDen, [...] | 銀河英雄伝説 | Les Héros de la Galaxie | OVA | 110 | Finished Airing | Jan 8, 1988 to Mar 17, 1997 |  |  | Kitty Films, TV Tokyo, Tokuma Japan [...] | Sentai Filmworks | Kitty Film Mitaka Studio | Novel | Drama, Sci-Fi | Adult Cast, Military, Space |  | 26 min. per ep. | R - 17+ (violence & profanity) | 9.03 | #11 | #705 | 286,444 | 14,876 | The 150-year-long stalemate between the two [...] |  |  |
   | 3 | Hunter x Hunter | HxH (2011) | HUNTER×HUNTER（ハンター×ハンター） | Hunter X Hunter | TV | 148 | Finished Airing | Oct 2, 2011 to Sep 24, 2014 | Fall 2011 | Sundays at 10:55 (JST) | Nippon Television Network, Shueisha, VAP | VIZ Media | Madhouse | Manga | Action, Adventure, Fantasy |  | Shounen | 23 min. per ep. | PG-13 - Teens 13 or older | 9.04 | #9 | #10 | 2,446,284 | 187,307 | Hunters devote themselves to accomplishing [...] | Hunter x Hunter | Hunter x Hunter |
   | 4 | Fruits Basket: The Final Season | Fruits Basket 3rd Season, Fruits Basket [...] | フルーツバスケット The Final | Fruits Basket Saison 3 | TV | 13 | Finished Airing | Apr 6, 2021 to Jun 29, 2021 | Spring 2021 | Tuesdays at 01:30 (JST) | 8PAN, Avex Pictures, Hakusensha, Nihon Ad [...] | Funimation | TMS Entertainment | Manga | Drama, Romance, Supernatural |  | Shoujo | 23 min. per ep. | PG-13 - Teens 13 or older | 9.03 | #10 | #512 | 369,388 | 17,082 | Hundreds of years ago, the Chinese Zodiac [...] | Fruits Basket Staffel 3 | Fruits Basket: The Final Season |
   | 5 | Fate/stay night: Heaven's Feel - III. Spring Song | Fate/stay night Movie: Heaven's Feel 3 | 劇場版「Fate/stay night [Heaven's Feel] [...] | Fate/stay night: Heaven's Feel - III. Spring Song | Movie | 1 | Finished Airing | Aug 15, 2020 |  |  | Aniplex, Kadokawa, Notes | Aniplex of America | ufotable | Visual novel | Action, Fantasy, Supernatural |  |  | 2 hr. 2 min. | R - 17+ (violence & profanity) | 8.70 | #50 | #704 | 286,927 | 7,092 | The Fifth Holy Grail War in Fuyuki City has [...] |  |  |

   _and more.._

