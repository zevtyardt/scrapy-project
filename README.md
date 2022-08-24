
# Scrapy based Projects
These are collection of some of my web scraping projects with scrapy. Feel free to use them, modify them and suggest modifications.

## Requirements:
1. [Python3.x](https://www.python.org/)
2. [Scrapy framework](https://scrapy.org/)
3. [Sqlalchemy](https://sqlalchemy.org)

see: [requirements.txt](/requirements.txt)

## List Crawlers:
1. **myanimelist:anime**
   | id | title | synonyms | japanese | french | type | episodes | status | aired | premiered | broadcast | producers | licensors | studios | source | genres | theme | demographic | duration | rating | score | ranked | popularity | members | favorites | synopsis | german | spanish |
   |---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
   | 1 | Fullmetal Alchemist: Brotherhood | Hagane no Renkinjutsushi: Fullmetal [...] | 鋼の錬金術師 FULLMETAL ALCHEMIST | Fullmetal Alchemist Brotherhood | TV | 64 | Finished Airing | Apr 5, 2009 to Jul 4, 2010 | Spring 2009 | Sundays at 17:00 (JST) | Aniplex, Mainichi Broadcasting System, [...] | Aniplex of America, Funimation | Bones | Manga | Action, Adventure, Drama, Fantasy | Military | Shounen | 24 min. per ep. | R - 17+ (violence & profanity) | 9.13 | #1 | #3 | 2,961,579 | 206,595 | After a horrific alchemy experiment goes [...] | None | None |
   | 2 | Gintama Season 5 | Gintama (2017) | 銀魂。 |  | TV | 12 | Finished Airing | Jan 9, 2017 to Mar 27, 2017 | Winter 2017 | Mondays at 01:35 (JST) | Aniplex, Dentsu, Shueisha, TV Tokyo | None found,, add some | Bandai Namco Pictures | Manga | Action, Comedy, Sci-Fi | Gag Humor, Historical, Parody, Samurai | Shounen | 24 min. per ep. | PG-13 - Teens 13 or older | 8.99 | #12 | #737 | 275,651 | 2,541 | After joining the resistance against the [...] | None | None |
   | 3 | Steins;Gate |  | STEINS;GATE |  | TV | 24 | Finished Airing | Apr 6, 2011 to Sep 14, 2011 | Spring 2011 | Wednesdays at 02:05 (JST) | AT-X, Frontier Works, Kadokawa Pictures [...] | Funimation | White Fox | Visual novel | Drama, Sci-Fi, Suspense | Psychological, Time Travel |  | 24 min. per ep. | PG-13 - Teens 13 or older | 9.08 | #4 | #13 | 2,287,759 | 174,432 | Eccentric scientist Rintarou Okabe has a [...] |  |  |
   | 4 | Gintama Season 4 | Gintama' (2015) | 銀魂° | Gintama Saison 4 | TV | 51 | Finished Airing | Apr 8, 2015 to Mar 30, 2016 | Spring 2015 | Wednesdays at 18:00 (JST) | Aniplex, Dentsu, TV Tokyo | Crunchyroll, Funimation | Bandai Namco Pictures | Manga | Action, Comedy, Sci-Fi | Gag Humor, Historical, Parody, Samurai | Shounen | 24 min. per ep. | PG-13 - Teens 13 or older | 9.08 | #3 | #338 | 550,710 | 14,869 | Gintoki, Shinpachi, and Kagura return as the [...] | Gintama Season 4 | Gintama Temporada 4 |
   | 5 | Kaguya-sama: Love is War - Ultra Romantic | Kaguya-sama wa Kokurasetai: Tensai-tachi no [...] | かぐや様は告らせたい-ウルトラロマンティック- |  | TV | 13 | Finished Airing | Apr 9, 2022 to Jun 25, 2022 | Spring 2022 | Saturdays at 00:00 (JST) | Aniplex, JR East Marketing & Communications, [...] | Aniplex of America | A-1 Pictures | Manga | Comedy, Suspense | Psychological, Romantic Subtext, School | Seinen | 23 min. per ep. | PG-13 - Teens 13 or older | 9.13 | #2 | #274 | 632,687 | 22,803 | The elite members of Shuchiin Academy's [...] |  |  |

   _and more.._

1. **kusonime**
   | id | title | url | genre | thumbnail | japanese | seasons | producers | type | status | total_episode | score | duration | released_on | sinopsis | download_data |
   |---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
   | 1 | Shikong Zhi Xi (Time Space Rift) | https://kusonime.com/shikong-zhi-xi-batch- [...] | Action, Anime ONA | https://kusonime.com/wp- [...] | 时空之隙 | Anime ONA | B.CMAY PICTURES, bilibili | ONA | Completed | 13 | 6.49 | 21 min. per ep. | Apr 15, 2022 | Energi yang tidak stabil dari dunia saat ini [...] | {'name': 'Download Shikong Zhi Xi Batch [...] |
   | 2 | Tekken: Bloodline | https://kusonime.com/tekken-bloodline-batch- [...] | Action, Martial Arts, Anime ONA | https://kusonime.com/wp- [...] | Tekken: Bloodline | Anime ONA | N/A | ONA | Completed | 6 | 6.58 | 25 min. per ep. | Aug 18, 2022 | “Kekuatan adalah segalanya.” Jin Kazama [...] | {'name': 'Download Tekken: Bloodline Batch [...] |
   | 3 | Gaikotsu Kishi-sama Tadaima Isekai e Odekakechuu | https://kusonime.com/skeleton-knight-batch- [...] | Action, Fantasy, Spring 2022 | https://kusonime.com/wp- [...] | 骸骨騎士様、只今異世界へお出掛け中 | Spring 2022 | Pony Canyon, AT-X, DAX Production, Docomo [...] | BD | Completed | 12 | 7.31 | 23 min. per ep. | Apr 07, 2022 | selain Ainz-sama ada juga tengkorak [...] | {'name': 'Download Gaikotsu Kishi-sama [...] |
   | 4 | TENSURA : Sukuwareru Ramiris | https://kusonime.com/sukuwareru-ramiris- [...] | Comedy, Fantasy, Anime ONA | https://kusonime.com/wp- [...] | 救われるラミリス | Anime ONA | N/A | ONA | Completed | 2 | 6.18 | 2 min. per ep. | Mar 19, 2022 | Episode spesial melalui streaming youtube [...] | {'name': 'Download TENSURA : Sukuwareru [...] |
   | 5 | Takt Op. Destiny | https://kusonime.com/takt-op-destiny-batch- [...] | Action, Fantasy, Music, Fall 2021 | https://kusonime.com/wp- [...] | takt op.Destiny | Fall 2021 | DeNA, Bandai Namco Arts | BD | Completed | 12 | 7.16 | 23 min. per ep. | Oct 06, 2021 | ceritanya sendiri, suatu hari meteorit hitam [...] | {'name': 'Download Takt Op. Destiny Batch BD [...] |

   _and more.._

