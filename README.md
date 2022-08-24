
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
   | 1 | Yuuki Yuuna wa Yuusha de Aru: Washio Sumi no [...] | https://kusonime.com/yuuki-yuuna-wa-yuusha- [...] | Drama, Fantasy, Magic, Slice of Life, Anime Movie | https://kusonime.com/wp- [...] | 結城友奈は勇者である -鷲尾須美の章- 第３章「やくそく」 | Anime Movie | Studio Gokumi | Movie | Completed | 1 | 8.02 | 48 min | Jul 08, 2017 | Movie tiga dan juga terakhir dari trilogi. [...] | {'name': 'Download Yuuki Yuuna wa Yuusha de [...] |
   | 2 | Yuuki Yuuna wa Yuusha de Aru: Yuusha no Shou | https://kusonime.com/yuuki-yuuna-wa-yuusha- [...] | Drama, Fantasy, Magic, Slice of Life, Fall 2017 | https://kusonime.com/wp- [...] | 結城友奈は勇者である -勇者の章- | Fall 2017 | Pony Canyon | BD | Completed | 6 | 7.64 | 24 min. per ep. | Nov 25, 2017 | kelanjutan dari cerita Yuki Yuna atau season [...] | {'name': 'Download Yuuki Yuuna wa Yuusha de [...] |
   | 3 | Yuuki Yuuna wa Yuusha de Aru: Washio Sumi no Shou | https://kusonime.com/yuuki-yuuna-washio- [...] | Drama, Fantasy, Magic, Slice of Life, Fall 2017 | https://kusonime.com/wp- [...] | 結城友奈は勇者である -鷲尾須美の章- | Fall 2017 | Pony Canyon | BD | Completed | 6 | 7.67 | 24 min. per ep. | Oct 07, 2017 | pada tahun 298 dari era para dewa, Sumi [...] | {'name': 'Download Yuuki Yuuna wa Yuusha de [...] |
   | 4 | Shikong Zhi Xi (Time Space Rift) | https://kusonime.com/shikong-zhi-xi-batch- [...] | Action, Anime ONA | https://kusonime.com/wp- [...] | 时空之隙 | Anime ONA | B.CMAY PICTURES, bilibili | ONA | Completed | 13 | 6.49 | 21 min. per ep. | Apr 15, 2022 | Energi yang tidak stabil dari dunia saat ini [...] | {'name': 'Download Shikong Zhi Xi Batch [...] |
   | 5 | TENSURA : Sukuwareru Ramiris | https://kusonime.com/sukuwareru-ramiris- [...] | Comedy, Fantasy, Anime ONA | https://kusonime.com/wp- [...] | 救われるラミリス | Anime ONA | N/A | ONA | Completed | 2 | 6.18 | 2 min. per ep. | Mar 19, 2022 | Episode spesial melalui streaming youtube [...] | {'name': 'Download TENSURA : Sukuwareru [...] |

   _and more.._

1. **myanimelist:anime**
   | id | title | url | japanese | type | episodes | status | aired | premiered | broadcast | producers | licensors | studios | source | genres | themes | duration | rating | score | ranked | popularity | members | favorites | synopsis | german | spanish | french | demographic |
   |---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
   | 1 | Steins;Gate | https://myanimelist.net/anime/9253/Steins_Gate | STEINS;GATE | TV | 24 | Finished Airing | Apr 6, 2011 to Sep 14, 2011 | Spring 2011 | Wednesdays at 02:05 (JST) | AT-X, Frontier Works, Kadokawa Pictures [...] | Funimation | White Fox | Visual novel | Drama, Sci-Fi, Suspense | Psychological, Time Travel | 24 min. per ep. | PG-13 - Teens 13 or older | 9.08 | #4 | #13 | 2,287,908 | 174,441 | Eccentric scientist Rintarou Okabe has a [...] |  |  |  |  |
   | 2 | Gintama Season 4 | https://myanimelist.net/anime/28977/Gintama° | 銀魂° | TV | 51 | Finished Airing | Apr 8, 2015 to Mar 30, 2016 | Spring 2015 | Wednesdays at 18:00 (JST) | Aniplex, Dentsu, TV Tokyo | Crunchyroll, Funimation | Bandai Namco Pictures | Manga | Action, Comedy, Sci-Fi | Gag Humor, Historical, Parody, Samurai | 24 min. per ep. | PG-13 - Teens 13 or older | 9.08 | #3 | #338 | 550,757 | 14,869 | Gintama' (2015) | Gintama Season 4 | Gintama Temporada 4 | Gintama Saison 4 | Shounen |
   | 3 | Fullmetal Alchemist: Brotherhood | [...] | 鋼の錬金術師 FULLMETAL ALCHEMIST | TV | 64 | Finished Airing | Apr 5, 2009 to Jul 4, 2010 | Spring 2009 | Sundays at 17:00 (JST) | Aniplex, Mainichi Broadcasting System, [...] | Aniplex of America, Funimation | Bones | Manga | Action, Adventure, Drama, Fantasy | Military | 24 min. per ep. | R - 17+ (violence & profanity) | 9.13 | #1 | #3 | 2,961,826 | 206,610 | Hagane no Renkinjutsushi: Fullmetal [...] |  |  | Fullmetal Alchemist Brotherhood | Shounen |
   | 4 | Hunter x Hunter | [...] | HUNTER×HUNTER（ハンター×ハンター） | TV | 148 | Finished Airing | Oct 2, 2011 to Sep 24, 2014 | Fall 2011 | Sundays at 10:55 (JST) | Nippon Television Network, Shueisha, VAP | VIZ Media | Madhouse | Manga | Action, Adventure, Fantasy |  | 23 min. per ep. | PG-13 - Teens 13 or older | 9.04 | #9 | #10 | 2,446,533 | 187,333 | HxH (2011) | Hunter x Hunter | Hunter x Hunter | Hunter X Hunter | Shounen |
   | 5 | Kaguya-sama: Love is War - Ultra Romantic | https://myanimelist.net/anime/43608/Kaguya- [...] | かぐや様は告らせたい-ウルトラロマンティック- | TV | 13 | Finished Airing | Apr 9, 2022 to Jun 25, 2022 | Spring 2022 | Saturdays at 00:00 (JST) | Aniplex, JR East Marketing & Communications, [...] | Aniplex of America | A-1 Pictures | Manga | Comedy, Suspense | Psychological, Romantic Subtext, School | 23 min. per ep. | PG-13 - Teens 13 or older | 9.13 | #2 | #274 | 632,966 | 22,819 | Kaguya-sama wa Kokurasetai: Tensai-tachi no [...] |  |  |  | Seinen |

   _and more.._

1. **myanimelist:manga**
   | id | title | url | japanese | type | volumes | chapters | status | published | genres | themes | demographic | serialization | authors | score | ranked | popularity | members | favorites | synopsis | french | german | spanish |
   |---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
   | 1 | Vagabond | https://myanimelist.net/manga/656/Vagabond | バガボンド | Manga | 37 | 327 | On Hiatus | Sep 3, 1998 to May 21, 2015 | Action, Adventure, Award Winning | Historical, Samurai | Seinen | Morning | (Story & Art),, (Story), Inoue, Takehiko, [...] | 9.19 | #4 | #16 | 290,158 | 30,775 | In 16th-century Japan, Shinmen Takezou is a [...] |  |  |  |
   | 2 | Grand Blue Dreaming | https://myanimelist.net/manga/70345/Grand_Blue | ぐらんぶる | Manga | Unknown | Unknown | Publishing | Apr 7, 2014 to ? | Comedy |  | Seinen | good! Afternoon | (Art), (Story),, Inoue, Kenji, Yoshioka, Kimitake | 9.03 | #9 | #50 | 150,615 | 15,315 | Among the seaside town of Izu's ocean waves [...] |  |  |  |
   | 3 | One Piece | https://myanimelist.net/manga/13/One_Piece | ONE PIECE | Manga | Unknown | Unknown | Publishing | Jul 22, 1997 to ? | Action, Adventure, Fantasy |  | Shounen | Shounen Jump (Weekly) | (Story & Art), Oda, Eiichiro | 9.20 | #3 | #3 | 509,794 | 100,986 | Gol D. Roger, a man referred to as the [...] |  |  |  |
   | 4 | ジョジョの奇妙な冒険 Part7 STEEL BALL RUN | [...] |  | Manga | 24 | 96 | Finished | Jan 19, 2004 to Apr 19, 2011 | Action, Adventure, Mystery, Supernatural | Historical | Seinen, Shounen | Ultra Jump | (Story & Art), Araki, Hirohiko | 9.28 | #2 | #27 | 212,290 | 35,932 | JoJo's Bizarre Adventure Part 7: Steel Ball [...] | Steel Ball Run |  |  |
   | 5 | Berserk | https://myanimelist.net/manga/2/Berserk | ベルセルク | Manga | Unknown | Unknown | Publishing | Aug 25, 1989 to ? | Action, Adventure, Award Winning, Drama, [...] | Gore, Military, Mythology, Psychological | Seinen | Young Animal | (Art), (Story & Art),, Miura, Kentarou, [...] | 9.46 | #1 | #2 | 561,030 | 105,593 | Berserk: The Prototype |  |  |  |

   _and more.._

