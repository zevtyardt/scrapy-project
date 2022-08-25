
# Scrapy based Projects
These are collection of some of my web scraping projects with scrapy. Feel free to use them, modify them and suggest modifications.

## Requirements:
1. [Python3.x](https://www.python.org/)
2. [Scrapy framework](https://scrapy.org/)
3. [Sqlalchemy](https://sqlalchemy.org)

see: [requirements.txt](/requirements.txt)

## List Crawlers:
1. **kusonime**</br>
   | info |  |
   |:---:|:---:|
   | spider name | kusonime |
   | source | http://kusonime.com/ |

   <details>
     <summary><i>output example</i></summary>

      </br>

      | id | title | url | genre | thumbnail | japanese | seasons | producers | type | status | total_episode | score | duration | released_on | sinopsis | download_data |
      |:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
      | 1 | Hanabi-chan wa Okuregachi | https://kusonime.com/hanabichan-batch- [...] | [ "Comedy", "Spring 2022" ] | https://kusonime.com/wp- [...] | ハナビちゃんは遅れがち | Spring 2022 | N/A | TV Series | Ongoing | ? | 6.12 | 4 min. per ep. | Jul 10, 2022 | Musashi Shinonome, manajer baru yang akan [...] | [ { "name": "Download Hanabi-chan wa [...] |
      | 2 | Gaikotsu Kishi-sama Tadaima Isekai e Odekakechuu | https://kusonime.com/skeleton-knight-batch- [...] | [ "Action", "Fantasy", "Spring 2022" ] | https://kusonime.com/wp- [...] | 骸骨騎士様、只今異世界へお出掛け中 | Spring 2022 | Pony Canyon, AT-X, DAX Production, Docomo [...] | BD | Completed | 12 | 7.31 | 23 min. per ep. | Apr 07, 2022 | selain Ainz-sama ada juga tengkorak [...] | [ { "name": "Download Gaikotsu Kishi-sama [...] |
      | 3 | Xiao Mo Tou Baolu La! (Busted! Darklord) | https://kusonime.com/xiao-mo-tou-baolu-la- [...] | [ "Comedy", "Anime ONA" ] | https://kusonime.com/wp- [...] | 小魔头暴露啦！ | Anime ONA | N/A | ONA | Completed | 26 | 6.38 | 8 min. per ep. | Jan 15, 2022 | Dalam upaya untuk bertahan hidup, Yu Renjie, [...] | [ { "name": "Download Xiao Mo Tou Baolu La! [...] |
      | 4 | Takt Op. Destiny | https://kusonime.com/takt-op-destiny-batch- [...] | [ "Action", "Fantasy", "Music", "Fall 2021" ] | https://kusonime.com/wp- [...] | takt op.Destiny | Fall 2021 | DeNA, Bandai Namco Arts | BD | Completed | 12 | 7.16 | 23 min. per ep. | Oct 06, 2021 | ceritanya sendiri, suatu hari meteorit hitam [...] | [ { "name": "Download Takt Op. Destiny Batch [...] |
      | 5 | Steamboy | https://kusonime.com/steamboy-bd-subtitle- [...] | [ "Action", "Adventure", "Drama", [...] | https://kusonime.com/wp- [...] | スチームボーイ | Anime Movie | Bandai Visual, Dentsu, TBS, Imagica, Bandai, [...] | Movie | Completed | 1 | 7.33 | 2 hr. 6 min. | Jul 17, 2004 | Becerita tentang cowok 13 tahun bernama [...] | [ { "name": "Download Movie Steamboy BD [...] |

      _and more.._

   </details>

1. **myanimelist:anime**</br>
   | info |  |
   |:---:|:---:|
   | spider name | mal:anime |
   | source | https://myanimelist.net/topanime.php |

   <details>
     <summary><i>output example</i></summary>

      </br>

      | id | title | url | synonyms | japanese | german | spanish | french | type | episodes | status | aired | premiered | broadcast | producers | licensors | studios | source | genres | demographic | duration | rating | score | ranked | popularity | members | favorites | synopsis | themes |
      |:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
      | 1 | Hunter x Hunter | [...] | HxH (2011) | HUNTER×HUNTER（ハンター×ハンター） | Hunter x Hunter | Hunter x Hunter | Hunter X Hunter | TV | 148 | Finished Airing | Oct 2, 2011 to Sep 24, 2014 | Fall 2011 | Sundays at 10:55 (JST) | [ "Nippon Television Network", "Shueisha", "VAP" ] | VIZ Media | Madhouse | Manga | [ "Action", "Adventure", "Fantasy" ] | [ "Shounen" ] | 23 min. per ep. | PG-13 - Teens 13 or older | 9.04 | #9 | #10 | 2,446,844 | 187,345 | Hunters devote themselves to accomplishing [...] |  |
      | 2 | Gintama: The Very Final | [...] |  | 銀魂 THE FINAL | N/A |  |  | Movie | 1 | Finished Airing | Jan 8, 2021 |  |  | [ "TV Tokyo", "Warner Bros. Japan" ] | Eleven Arts | Bandai Namco Pictures | Manga | [ "Action", "Comedy", "Drama", "Sci-Fi" ] | [ "Shounen" ] | 1 hr. 44 min. | PG-13 - Teens 13 or older | 9.05 | #7 | #1652 | 110,801 | 3,723 | Two years have passed following the [...] | [ "Gag Humor", "Historical", "Parody", "Samurai" ] |
      | 3 | Fullmetal Alchemist: Brotherhood | [...] | Hagane no Renkinjutsushi: Fullmetal [...] | 鋼の錬金術師 FULLMETAL ALCHEMIST |  |  | Fullmetal Alchemist Brotherhood | TV | 64 | Finished Airing | Apr 5, 2009 to Jul 4, 2010 | Spring 2009 | Sundays at 17:00 (JST) | [ "Aniplex", "Mainichi Broadcasting System", [...] | [ "Aniplex of America", "Funimation" ] | Bones | Manga | [ "Action", "Adventure", "Drama", "Fantasy" ] | [ "Shounen" ] | 24 min. per ep. | R - 17+ (violence & profanity) | 9.13 | #1 | #3 | 2,962,116 | 206,616 | After a horrific alchemy experiment goes [...] | [ "Military" ] |
      | 4 | Fruits Basket: The Final Season | [...] | Fruits Basket 3rd Season, Fruits Basket [...] | フルーツバスケット The Final | Fruits Basket Staffel 3 | Fruits Basket: The Final Season | Fruits Basket Saison 3 | TV | 13 | Finished Airing | Apr 6, 2021 to Jun 29, 2021 | Spring 2021 | Tuesdays at 01:30 (JST) | [ "8PAN", "Avex Pictures", "Hakusensha", [...] | Funimation | TMS Entertainment | Manga | [ "Drama", "Romance", "Supernatural" ] | [ "Shoujo" ] | 23 min. per ep. | PG-13 - Teens 13 or older | 9.03 | #10 | #512 | 369,561 | 17,092 | Hundreds of years ago, the Chinese Zodiac [...] |  |
      | 5 | Gintama: Enchousen | [...] | Gintama' (2012), Gintama' Overdrive, Kintama | 銀魂' 延長戦 |  |  |  | TV | 13 | Finished Airing | Oct 4, 2012 to Mar 28, 2013 | Fall 2012 | Thursdays at 18:00 (JST) | [ "Aniplex", "Dentsu", "Miracle Bus", [...] | [ "None found,", "add some" ] | Sunrise | Manga | [ "Action", "Comedy", "Sci-Fi" ] | [ "Shounen" ] | 24 min. per ep. | PG-13 - Teens 13 or older | 9.04 | #8 | #697 | 288,977 | 2,851 | While Gintoki Sakata was away, the Yorozuya [...] | [ "Gag Humor", "Historical", "Parody", "Samurai" ] |

      _and more.._

   </details>

1. **myanimelist:character**</br>
   | info |  |
   |:---:|:---:|
   | spider name | mal:character |
   | source | https://myanimelist.net/character.php |

   <details>
     <summary><i>output example</i></summary>

      </br>

      | id | name | url | japanese | source | favorites | biodata | description |
      |:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
      | 1 | Edward Elric | https://myanimelist.net/character/11/Edward_Elric | エドワード・エルリック | Fullmetal Alchemist | 83,452 | { "age": "15-16 (series), 18 (movie, end of [...] | Winry Rockbell Pinako Rockbell Izumi Curtis [...] |
      | 2 | Lelouch Lamperouge | [...] | ルルーシュ・ランペルージ | Code Geass: Hangyaku no Lelouch | 157,536 | { "age": "17 (first season), 18 (second [...] | Lelouch vi Britannia (ルルーシュ・ヴィ・ブリタニア, [...] |
      | 3 | Killua Zoldyck | [...] | キルア=ゾルディック | Hunter x Hunter | 88,948 | { "age": "12 (Beginning), 14-15 (Current)", [...] | , Hunter Abilities: Killua Zoldyck is the [...] |
      | 4 | Naruto Uzumaki | [...] | うずまき ナルト | Naruto | 78,178 | { "age": "12-13 (Naruto part I), 15-17 (part [...] | Born in Konohagakure, a ninja village hidden [...] |
      | 5 | Rintarou Okabe | [...] | 岡部 倫太郎 | Steins;Gate | 89,317 | { "age": "18 (Steins;Gate), 19 (Steins;Gate [...] | Rintaro Okabe (岡部 倫太郎 Okabe Rintarō?), often [...] |

      _and more.._

   </details>

1. **myanimelist:manga**</br>
   | info |  |
   |:---:|:---:|
   | spider name | mal:manga |
   | source | https://myanimelist.net/topmanga.php |

   <details>
     <summary><i>output example</i></summary>

      </br>

      | id | title | url | japanese | type | volumes | chapters | status | published | genres | themes | demographic | serialization | authors | score | ranked | popularity | members | favorites | synopsis | french |
      |:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
      | 1 | Slam Dunk | https://myanimelist.net/manga/51/Slam_Dunk | SLAM DUNK | Manga | 31 | 276 | Finished | Sep 18, 1990 to Jun 4, 1996 | [ "Award Winning", "Sports" ] | [ "School", "Team Sports" ] | [ "Shounen" ] | Shounen Jump (Weekly) | [ "(Story & Art)", "Inoue, Takehiko" ] | 9.06 | #6 | #63 | 136,503 | 13,145 | Hanamichi Sakuragi, a tall, boisterous [...] |  |
      | 2 | Vagabond | https://myanimelist.net/manga/656/Vagabond | バガボンド | Manga | 37 | 327 | On Hiatus | Sep 3, 1998 to May 21, 2015 | [ "Action", "Adventure", "Award Winning" ] | [ "Historical", "Samurai" ] | [ "Seinen" ] | Morning | [ "(Story & Art),", "(Story)", "Inoue, [...] | 9.19 | #4 | #16 | 290,222 | 30,785 | In 16th-century Japan, Shinmen Takezou is a [...] |  |
      | 3 | Berserk | https://myanimelist.net/manga/2/Berserk | ベルセルク | Manga | Unknown | Unknown | Publishing | Aug 25, 1989 to ? | [ "Action", "Adventure", "Award Winning", [...] | [ "Gore", "Military", "Mythology", [...] | [ "Seinen" ] | Young Animal | [ "(Art)", "(Story & Art),", "Miura, [...] | 9.46 | #1 | #2 | 561,136 | 105,626 | Berserk: The Prototype |  |
      | 4 | Monster | https://myanimelist.net/manga/1/Monster | MONSTER | Manga | 18 | 162 | Finished | Dec 5, 1994 to Dec 20, 2001 | [ "Award Winning", "Drama", "Mystery" ] | [ "Adult Cast", "Psychological" ] | [ "Seinen" ] | Big Comic Original | [ "(Story & Art)", "Urasawa, Naoki" ] | 9.13 | #5 | #30 | 196,176 | 17,134 | Kenzou Tenma, a renowned Japanese [...] |  |
      | 5 | One Piece | https://myanimelist.net/manga/13/One_Piece | ONE PIECE | Manga | Unknown | Unknown | Publishing | Jul 22, 1997 to ? | [ "Action", "Adventure", "Fantasy" ] |  | [ "Shounen" ] | Shounen Jump (Weekly) | [ "(Story & Art)", "Oda, Eiichiro" ] | 9.20 | #3 | #3 | 509,903 | 100,996 | Gol D. Roger, a man referred to as the [...] |  |

      _and more.._

   </details>

