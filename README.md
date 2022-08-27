
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
   |---|---|
   | spider name | kusonime |
   | source | http://kusonime.com/ |

   <details>
     <summary><i>output example</i></summary>

      </br>

      | id | title | url | genre | thumbnail | japanese | seasons | producers | type | status | total_episode | score | duration | released_on | sinopsis | download_data |
      |---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
      | 1 | Shingeki no Kyojin: The Final Season | https://kusonime.com/snk-s4-batch-subtitle- [...] | [ "Action", "Drama", "Fantasy", "Military", [...] | https://kusonime.com/wp- [...] | 進撃の巨人 The Final Season | Winter 2021 | Production I.G, Dentsu, Mainichi [...] | BD | Completed | 28 | 9.16 | 24 min. per ep. | Dec 07, 2020 | Shingeki no Kyojin: The Final Season | [ { "name": "Download Shingeki no Kyojin: [...] |
      | 2 | Shikong Zhi Xi (Time Space Rift) | https://kusonime.com/shikong-zhi-xi-batch- [...] | [ "Action", "Anime ONA" ] | https://kusonime.com/wp- [...] | 时空之隙 | Anime ONA | B.CMAY PICTURES, bilibili | ONA | Completed | 13 | 6.49 | 21 min. per ep. | Apr 15, 2022 | Shikong Zhi Xi (Time Space Rift) | [ { "name": "Download Shikong Zhi Xi Batch [...] |
      | 3 | Gaikotsu Kishi-sama Tadaima Isekai e Odekakechuu | https://kusonime.com/skeleton-knight-batch- [...] | [ "Action", "Fantasy", "Spring 2022" ] | https://kusonime.com/wp- [...] | 骸骨騎士様、只今異世界へお出掛け中 | Spring 2022 | Pony Canyon, AT-X, DAX Production, Docomo [...] | BD | Completed | 12 | 7.31 | 23 min. per ep. | Apr 07, 2022 | Gaikotsu Kishi-sama Tadaima Isekai e Odekakechuu | [ { "name": "Download Gaikotsu Kishi-sama [...] |
      | 4 | Steamboy | https://kusonime.com/steamboy-bd-subtitle- [...] | [ "Action", "Adventure", "Drama", [...] | https://kusonime.com/wp- [...] | スチームボーイ | Anime Movie | Bandai Visual, Dentsu, TBS, Imagica, Bandai, [...] | Movie | Completed | 1 | 7.33 | 2 hr. 6 min. | Jul 17, 2004 | Steamboy | [ { "name": "Download Movie Steamboy BD [...] |
      | 5 | Takt Op. Destiny | https://kusonime.com/takt-op-destiny-batch- [...] | [ "Action", "Fantasy", "Music", "Fall 2021" ] | https://kusonime.com/wp- [...] | takt op.Destiny | Fall 2021 | DeNA, Bandai Namco Arts | BD | Completed | 12 | 7.16 | 23 min. per ep. | Oct 06, 2021 | Takt Op. Destiny | [ { "name": "Download Takt Op. Destiny Batch [...] |

      _and more.._

   </details>

1. **hackernews**</br>
   | info |  |
   |---|---|
   | spider name | hackernews |
   | source | http://news.ycombinator.com/ |

   <details>
     <summary><i>output example</i></summary>

      </br>

      | id | title | url | from_site | rank | score | user | date |
      |---|---|---|---|---|---|---|---|
      | 32575723 | Demystifying the LFSR | https://www.moria.us/articles/demystifying- [...] | moria.us | 72 | 35 points | randkyp | 2022-08-24T06:50:09 |
      | 32578683 | Timothy Leary's Mind Mirror (1985) | https://scalar.usc.edu/works/timothy-leary- [...] | usc.edu | 32 | 45 points | ArtWomb | 2022-08-24T12:45:55 |
      | 32583151 | Hacking Photosynthesis | https://www.codonmag.com/p/hacking-photosynthesis | codonmag.com | 40 | 24 points | prostoalex | 2022-08-24T17:51:36 |
      | 32583868 | Panic at the Library | [...] | laphamsquarterly.org | 17 | 16 points | drdee | 2022-08-24T18:39:06 |
      | 32585830 | What Next? (2017) | https://graydon2.dreamwidth.org/253769.html | graydon2.dreamwidth.org | 19 | 5 points | dcminter | 2022-08-24T21:12:18 |

      _and more.._

   </details>

1. **myanimelist:anime**</br>
   | info |  |
   |---|---|
   | spider name | mal:anime |
   | source | https://myanimelist.net/topanime.php |

   <details>
     <summary><i>output example</i></summary>

      </br>

      | id | title | url | synonyms | japanese | french | type | episodes | status | aired | premiered | broadcast | producers | licensors | studios | source | genres | theme | demographic | duration | rating | score | ranked | popularity | members | favorites | synopsis | german | spanish |
      |---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
      | 1 | Fullmetal Alchemist: Brotherhood | [...] | Hagane no Renkinjutsushi: Fullmetal [...] | 鋼の錬金術師 FULLMETAL ALCHEMIST | Fullmetal Alchemist Brotherhood | TV | 64 | Finished Airing | Apr 5, 2009 to Jul 4, 2010 | Spring 2009 | Sundays at 17:00 (JST) | [ "Aniplex", "Mainichi Broadcasting System", [...] | [ "Aniplex of America", "Funimation" ] | Bones | Manga | [ "Action", "Adventure", "Drama", "Fantasy" ] | [ "Military" ] | [ "Shounen" ] | 24 min. per ep. | R - 17+ (violence & profanity) | 9.13 | #1 | #3 | 2,963,304 | 206,685 | After a horrific alchemy experiment goes [...] |  |  |
      | 2 | Fruits Basket: The Final Season | [...] | Fruits Basket 3rd Season, Fruits Basket [...] | フルーツバスケット The Final | Fruits Basket Saison 3 | TV | 13 | Finished Airing | Apr 6, 2021 to Jun 29, 2021 | Spring 2021 | Tuesdays at 01:30 (JST) | [ "8PAN", "Avex Pictures", "Hakusensha", [...] | Funimation | TMS Entertainment | Manga | [ "Drama", "Romance", "Supernatural" ] |  | [ "Shoujo" ] | 23 min. per ep. | PG-13 - Teens 13 or older | 9.03 | #10 | #512 | 369,915 | 17,102 | Hundreds of years ago, the Chinese Zodiac [...] | Fruits Basket Staffel 3 | Fruits Basket: The Final Season |
      | 3 | Gintama Season 5 | https://myanimelist.net/anime/34096/Gintama | Gintama (2017) | 銀魂。 |  | TV | 12 | Finished Airing | Jan 9, 2017 to Mar 27, 2017 | Winter 2017 | Mondays at 01:35 (JST) | [ "Aniplex", "Dentsu", "Shueisha", "TV Tokyo" ] | [ "None found,", "add some" ] | Bandai Namco Pictures | Manga | [ "Action", "Comedy", "Sci-Fi" ] | [ "Gag Humor", "Historical", "Parody", "Samurai" ] | [ "Shounen" ] | 24 min. per ep. | PG-13 - Teens 13 or older | 8.99 | #12 | #737 | 275,850 | 2,541 | After joining the resistance against the [...] |  |  |
      | 4 | Gintama: Enchousen | [...] | Gintama' (2012), Gintama' Overdrive, Kintama | 銀魂' 延長戦 |  | TV | 13 | Finished Airing | Oct 4, 2012 to Mar 28, 2013 | Fall 2012 | Thursdays at 18:00 (JST) | [ "Aniplex", "Dentsu", "Miracle Bus", [...] | [ "None found,", "add some" ] | Sunrise | Manga | [ "Action", "Comedy", "Sci-Fi" ] | [ "Gag Humor", "Historical", "Parody", "Samurai" ] | [ "Shounen" ] | 24 min. per ep. | PG-13 - Teens 13 or older | 9.04 | #8 | #697 | 289,102 | 2,854 | While Gintoki Sakata was away, the Yorozuya [...] |  |  |
      | 5 | Gintama Season 4 | https://myanimelist.net/anime/28977/Gintama° | Gintama' (2015) | 銀魂° | Gintama Saison 4 | TV | 51 | Finished Airing | Apr 8, 2015 to Mar 30, 2016 | Spring 2015 | Wednesdays at 18:00 (JST) | [ "Aniplex", "Dentsu", "TV Tokyo" ] | [ "Crunchyroll", "Funimation" ] | Bandai Namco Pictures | Manga | [ "Action", "Comedy", "Sci-Fi" ] | [ "Gag Humor", "Historical", "Parody", "Samurai" ] | [ "Shounen" ] | 24 min. per ep. | PG-13 - Teens 13 or older | 9.08 | #3 | #338 | 551,077 | 14,879 | Gintoki, Shinpachi, and Kagura return as the [...] | Gintama Season 4 | Gintama Temporada 4 |

      _and more.._

   </details>

1. **myanimelist:character**</br>
   | info |  |
   |---|---|
   | spider name | mal:character |
   | source | https://myanimelist.net/character.php |

   <details>
     <summary><i>output example</i></summary>

      </br>

      | id | name | url | japanese | source | favorites | biodata | description |
      |---|---|---|---|---|---|---|---|
      | 1 | Lelouch Lamperouge | [...] | ルルーシュ・ランペルージ | Code Geass: Hangyaku no Lelouch | 157,590 | { "age": "17 (first season), 18 (second [...] | Lelouch vi Britannia (ルルーシュ・ヴィ・ブリタニア, [...] |
      | 2 | Edward Elric | https://myanimelist.net/character/11/Edward_Elric | エドワード・エルリック | Fullmetal Alchemist | 83,474 | { "age": "15-16 (series), 18 (movie, end of [...] | Winry Rockbell Pinako Rockbell Izumi Curtis [...] |
      | 3 | Luffy Monkey D. | [...] | モンキー・D・ルフィ | One Piece | 120,217 | { "age": "17; 19", "birthdate": "May 5, [...] | Bounty: Luffy is the captain of the Straw [...] |
      | 4 | Levi | https://myanimelist.net/character/45627/Levi | リヴァイ | Shingeki no Kyojin | 131,653 | { "birthday": "December 25", "height": "160 [...] | Levi is known as humanity's most powerful [...] |
      | 5 | Killua Zoldyck | [...] | キルア=ゾルディック | Hunter x Hunter | 88,978 | { "age": "12 (Beginning), 14-15 (Current)", [...] | , Hunter Abilities: Killua Zoldyck is the [...] |

      _and more.._

   </details>

1. **myanimelist:manga**</br>
   | info |  |
   |---|---|
   | spider name | mal:manga |
   | source | https://myanimelist.net/topmanga.php |

   <details>
     <summary><i>output example</i></summary>

      </br>

      | id | title | url | japanese | type | volumes | chapters | status | published | genres | themes | demographic | serialization | authors | score | ranked | popularity | members | favorites | synopsis | french | german | spanish |
      |---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
      | 1 | Vagabond | https://myanimelist.net/manga/656/Vagabond | バガボンド | Manga | 37 | 327 | On Hiatus | Sep 3, 1998 to May 21, 2015 | [ "Action", "Adventure", "Award Winning" ] | [ "Historical", "Samurai" ] | [ "Seinen" ] | Morning | [ "(Story & Art),", "(Story)", "Inoue, [...] | 9.19 | #4 | #16 | 290,521 | 30,818 | In 16th-century Japan, Shinmen Takezou is a [...] |  |  |  |
      | 2 | One Piece | https://myanimelist.net/manga/13/One_Piece | ONE PIECE | Manga | Unknown | Unknown | Publishing | Jul 22, 1997 to ? | [ "Action", "Adventure", "Fantasy" ] |  | [ "Shounen" ] | Shounen Jump (Weekly) | [ "(Story & Art)", "Oda, Eiichiro" ] | 9.20 | #3 | #3 | 510,297 | 101,074 | Gol D. Roger, a man referred to as the [...] |  |  |  |
      | 3 | Berserk | https://myanimelist.net/manga/2/Berserk | ベルセルク | Manga | Unknown | Unknown | Publishing | Aug 25, 1989 to ? | [ "Action", "Adventure", "Award Winning", [...] | [ "Gore", "Military", "Mythology", [...] | [ "Seinen" ] | Young Animal | [ "(Art)", "(Story & Art),", "Miura, [...] | 9.46 | #1 | #2 | 561,563 | 105,709 | Berserk: The Prototype |  |  |  |
      | 4 | Monster | https://myanimelist.net/manga/1/Monster | MONSTER | Manga | 18 | 162 | Finished | Dec 5, 1994 to Dec 20, 2001 | [ "Award Winning", "Drama", "Mystery" ] | [ "Adult Cast", "Psychological" ] | [ "Seinen" ] | Big Comic Original | [ "(Story & Art)", "Urasawa, Naoki" ] | 9.13 | #5 | #30 | 196,340 | 17,137 | Kenzou Tenma, a renowned Japanese [...] |  |  |  |
      | 5 | Real | https://myanimelist.net/manga/657/Real | リアル | Manga | Unknown | Unknown | Publishing | 1999 to ? | [ "Drama", "Sports" ] | [ "Psychological", "Team Sports" ] | [ "Seinen" ] | Young Jump | [ "(Story & Art)", "Inoue, Takehiko" ] | 8.90 | #20 | #186 | 67,455 | 2,927 | Tomomi Nomiya, former captain of his high [...] |  |  |  |

      _and more.._

   </details>

1. **myanimelist:people**</br>
   | info |  |
   |---|---|
   | spider name | mal:people |
   | source | https://myanimelist.net/people.php |

   <details>
     <summary><i>output example</i></summary>

      </br>

      | id | name | url | image_url | given_name | birthday | member_favorites | description | alternate_names | height | weight | blood_type | hometown | hobbies | skills | pets | favourite_animal | favourite_mangaka | favourite_music | debut_role | dislikes | places_he_wants_to_visit | agency |
      |---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
      | 1 | Miyazaki, Hayao | https://myanimelist.net/people/1870/Hayao_Miyazaki | [...] | 駿 | Jan 5, 1941 | 66,984 | Miyazaki, the second of four brothers, was [...] |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
      | 2 | Araki, Hirohiko | https://myanimelist.net/people/2619/Hirohiko_Araki | [...] | 飛呂彦 | Sendai, Miyagi Prefecture, Japan | 39,092 | Hirohiko Araki left school before graduation [...] | Araki Toshiyuki, 荒木 利之 | 169.5 cm | 61 kg | B |  |  |  |  |  |  |  |  |  |  |  |
      | 3 | Kamiya, Hiroshi | https://myanimelist.net/people/118/Hiroshi_Kamiya | [...] | 浩史 | Matsudo, Chiba Prefecture, Japan | 103,275 | Kamiya Hiroshi went to Aoni Juku and decided [...] | ヒロC, HiroC, Kamiyan | 167 cm (5'6") | 53 kg (117 lbs) | A |  |  |  |  |  |  |  |  |  |  |  |
      | 4 | Miyano, Mamoru | https://myanimelist.net/people/65/Mamoru_Miyano | [...] | 真守 | Jun 8, 1983 | 86,738 | Mamoru Miyano won Best Voice Actor award in [...] |  | 182 cm | 70 kg | B | Saitama, Japan | singing, soccer | harmonica, harp |  |  |  |  |  |  |  |  |
      | 5 | Takahashi, Rie | https://myanimelist.net/people/34785/Rie_Takahashi | [...] | 李依 | Saitama Prefecture, Japan | 46,624 | She is apart of the seiyuu unit Earphones, [...] | Rieri, Rii-chan |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

      _and more.._

   </details>

1. **urbandictionary**</br>
   | info |  |
   |---|---|
   | spider name | urbandictionary |
   | source | http://www.urbandictionary.com/ |

   <details>
     <summary><i>output example</i></summary>

      </br>

      | id | text | meaning | example | author | date |
      |---|---|---|---|---|---|
      | 61580 | second breakfast | invented by hobbits, second breakfast is [...] | We'll just have time for second breakfast [...] | Sienna | March 17, 2003 |
      | 349729 | munch | A low-pressure, social gathering at a [...] | Well, if you don't feel ready for a play [...] | Peter | November 14, 2003 |
      | 795231 | sweet nothing | a sweet nothing is a complementary statement [...] | He whispered sweet nothings into her ear [...] | Spencer | August 16, 2004 |
      | 5168051 | FOBI | Fear of Being Involved/Included/Invited | The antithesis to FOMO. FOBI refers to [...] | papillonnosilla | August 19, 2010 |
      | 7808664 | Douchergheist | (Noun) A spirit that embodies pure douche [...] | "Gayrod used to be cool but he got possessed [...] | SaxeGotha | June 26, 2014 |

      _and more.._

   </details>

1. **animeplanet**</br>
   | info |  |
   |---|---|
   | spider name | anime-planet |
   | source | http://www.anime-planet.com/anime/all |

   <details>
     <summary><i>output example</i></summary>

      </br>

      | id | title | alternative_title | studios | type | episodes | year | season | average_rating | rank | synopsis | notes | tags | url |
      |---|---|---|---|---|---|---|---|---|---|---|---|---|---|
      | 1 | Demon Slayer: Kimetsu no Yaiba - [...] | Kimetsu no Yaiba: Yuukaku-hen | ufotable | TV | 11 eps | 2021 - 2022 | Fall 2021 | 4.6 out of 5 from 15,915 votes | #1 | Tanjiro and his friends accompany the [...] | Source: Viz | [ "Action", "Adventure", "Fantasy", [...] | https://www.anime-planet.com/anime/demon- [...] |
      | 2 | SPY x FAMILY |  | WIT Studio | TV | 12 eps | 2022 | Spring 2022 | 4.564 out of 5 from 15,045 votes | #4 | Master spy Twilight is the best at what he [...] | Source: VIZ | [ "Action", "Comedy", "Shounen", [...] | https://www.anime-planet.com/anime/spy-x-family |
      | 3 | Kaguya-sama: Love is War - Ultra Romantic | Kaguya-sama wa Kokurasetai: Ultra Romantic | A-1 Pictures | TV | 13 eps | 2022 | Spring 2022 | 4.552 out of 5 from 5,216 votes | #6 | The third season of |  | [ "Comedy", "Drama", "Romance", "Seinen", [...] | https://www.anime-planet.com/anime/kaguya- [...] |
      | 4 | Jujutsu Kaisen |  | MAPPA | TV | 24 eps | 2020 - 2021 | Fall 2020 | 4.539 out of 5 from 41,600 votes | #8 | Although Yuji Itadori looks like your [...] | Source: Viz | [ "Action", "Horror", "Shounen", "Body [...] | https://www.anime-planet.com/anime/jujutsu-kaisen |
      | 5 | Fruits Basket the Final Season | Fruits Basket the Final | TMS Entertainment | TV | 13 eps | 2021 | Spring 2021 | 4.598 out of 5 from 7,480 votes | #2 | The final arc of |  | [ "Drama", "Fantasy", "Romance", "Shoujo", [...] | https://www.anime-planet.com/anime/fruits- [...] |

      _and more.._

   </details>

