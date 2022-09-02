
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
      | 2 | Tekken: Bloodline | https://kusonime.com/tekken-bloodline-batch- [...] | [ "Action", "Martial Arts", "Anime ONA" ] | https://kusonime.com/wp- [...] | Tekken: Bloodline | Anime ONA | N/A | ONA | Completed | 6 | 6.58 | 25 min. per ep. | Aug 18, 2022 | Tekken: Bloodline | [ { "name": "Download Tekken: Bloodline [...] |
      | 3 | Horimiya | https://kusonime.com/horimiya-la-2021-batch- [...] | [ "Comedy", "Romance", "School", "Shounen", [...] | https://kusonime.com/wp- [...] | ホリミヤ |  | TBS | TV Series | Completed | 7 | 7.90 (Mydramalist) | 30 min. per ep. | Feb 16, 2021 | Horimiya | [ { "name": "Download Horimiya Live Action [...] |
      | 4 | Xiao Mo Tou Baolu La! (Busted! Darklord) | https://kusonime.com/xiao-mo-tou-baolu-la- [...] | [ "Comedy", "Anime ONA" ] | https://kusonime.com/wp- [...] | 小魔头暴露啦！ | Anime ONA | N/A | ONA | Completed | 26 | 6.38 | 8 min. per ep. | Jan 15, 2022 | Xiao Mo Tou Baolu La! (Busted! Darklord) | [ { "name": "Download Xiao Mo Tou Baolu La! [...] |
      | 5 | Shikong Zhi Xi (Time Space Rift) | https://kusonime.com/shikong-zhi-xi-batch- [...] | [ "Action", "Anime ONA" ] | https://kusonime.com/wp- [...] | 时空之隙 | Anime ONA | B.CMAY PICTURES, bilibili | ONA | Completed | 13 | 6.49 | 21 min. per ep. | Apr 15, 2022 | Shikong Zhi Xi (Time Space Rift) | [ { "name": "Download Shikong Zhi Xi Batch [...] |

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
      | 32575393 | Why do some humans love chili peppers? | https://www.sapiens.org/culture/chili- [...] | sapiens.org | 114 | 110 points | Petiver | 2022-08-24T05:53:54 |
      | 32575668 | Things people blamed on bicycles | [...] | twitter.com/paulisci | 111 | 759 points | the-archivist | 2022-08-24T06:43:06 |
      | 32575723 | Demystifying the LFSR | https://www.moria.us/articles/demystifying- [...] | moria.us | 84 | 37 points | randkyp | 2022-08-24T06:50:09 |
      | 32578152 | Email Innovation Timeline [pdf] | [...] | computerhistory.org | 34 | 28 points | bookofjoe | 2022-08-24T11:55:04 |
      | 32578683 | Timothy Leary's Mind Mirror (1985) | https://scalar.usc.edu/works/timothy-leary- [...] | usc.edu | 83 | 52 points | ArtWomb | 2022-08-24T12:45:55 |

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
      | 1 | Fullmetal Alchemist: Brotherhood | [...] | Hagane no Renkinjutsushi: Fullmetal [...] | 鋼の錬金術師 FULLMETAL ALCHEMIST | Fullmetal Alchemist Brotherhood | TV | 64 | Finished Airing | Apr 5, 2009 to Jul 4, 2010 | Spring 2009 | Sundays at 17:00 (JST) | [ "Aniplex", "Mainichi Broadcasting System", [...] | [ "Aniplex of America", "Funimation" ] | Bones | Manga | [ "Action", "Adventure", "Drama", "Fantasy" ] | [ "Military" ] | [ "Shounen" ] | 24 min. per ep. | R - 17+ (violence & profanity) | 9.13 | #1 | #3 | 2,963,531 | 206,712 | After a horrific alchemy experiment goes [...] |  |  |
      | 2 | Gintama Season 5 | https://myanimelist.net/anime/34096/Gintama | Gintama (2017) | 銀魂。 |  | TV | 12 | Finished Airing | Jan 9, 2017 to Mar 27, 2017 | Winter 2017 | Mondays at 01:35 (JST) | [ "Aniplex", "Dentsu", "Shueisha", "TV Tokyo" ] | [ "None found,", "add some" ] | Bandai Namco Pictures | Manga | [ "Action", "Comedy", "Sci-Fi" ] | [ "Gag Humor", "Historical", "Parody", "Samurai" ] | [ "Shounen" ] | 24 min. per ep. | PG-13 - Teens 13 or older | 8.99 | #12 | #737 | 275,880 | 2,540 | After joining the resistance against the [...] |  |  |
      | 3 | March Comes In Like A Lion 2nd Season | https://myanimelist.net/anime/35180/3- [...] | Sangatsu no Lion Second Season | 3月のライオン 第2シリーズ | March Comes in like a Lion Saison 2 | TV | 22 | Finished Airing | Oct 14, 2017 to Mar 31, 2018 | Fall 2017 | Saturdays at 23:00 (JST) | [ "Aniplex", "Asmik Ace", "Dentsu", [...] | Aniplex of America | Shaft | Manga | [ "Drama", "Slice of Life" ] | [ "Childcare", "Iyashikei", "Strategy Game" ] | [ "Seinen" ] | 25 min. per ep. | PG-13 - Teens 13 or older | 8.95 | #13 | #532 | 360,008 | 14,379 | Now in his second year of high school, Rei [...] | March Come in Like a Lion Staffel 2 | March Comes in like a Lion Temporada 2 |
      | 4 | Gintama | https://myanimelist.net/anime/918/Gintama | Gin Tama, Silver Soul, Yorinuki Gintama-san | 銀魂 |  | TV | 201 | Finished Airing | Apr 4, 2006 to Mar 25, 2010 | Spring 2006 | Thursdays at 18:00 (JST) | [ "Aniplex", "Audio Highs", "Dentsu", [...] | [ "Crunchyroll", "Sentai Filmworks" ] | Sunrise | Manga | [ "Action", "Comedy", "Sci-Fi" ] | [ "Gag Humor", "Historical", "Parody", "Samurai" ] | [ "Shounen" ] | 24 min. per ep. | PG-13 - Teens 13 or older | 8.95 | #14 | #134 | 962,349 | 55,505 | Edo is a city that was home to the vigor and [...] |  |  |
      | 5 | Gintama Season 4 | https://myanimelist.net/anime/28977/Gintama° | Gintama' (2015) | 銀魂° | Gintama Saison 4 | TV | 51 | Finished Airing | Apr 8, 2015 to Mar 30, 2016 | Spring 2015 | Wednesdays at 18:00 (JST) | [ "Aniplex", "Dentsu", "TV Tokyo" ] | [ "Crunchyroll", "Funimation" ] | Bandai Namco Pictures | Manga | [ "Action", "Comedy", "Sci-Fi" ] | [ "Gag Humor", "Historical", "Parody", "Samurai" ] | [ "Shounen" ] | 24 min. per ep. | PG-13 - Teens 13 or older | 9.08 | #3 | #338 | 551,114 | 14,885 | Gintoki, Shinpachi, and Kagura return as the [...] | Gintama Season 4 | Gintama Temporada 4 |

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
      | 1 | Lelouch Lamperouge | [...] | ルルーシュ・ランペルージ | Code Geass: Hangyaku no Lelouch | 157,607 | { "age": "17 (first season), 18 (second [...] | Lelouch vi Britannia (ルルーシュ・ヴィ・ブリタニア, [...] |
      | 2 | Levi | https://myanimelist.net/character/45627/Levi | リヴァイ | Shingeki no Kyojin | 131,669 | { "birthday": "December 25", "height": "160 [...] | Levi is known as humanity's most powerful [...] |
      | 3 | Luffy Monkey D. | [...] | モンキー・D・ルフィ | One Piece | 120,240 | { "age": "17; 19", "birthdate": "May 5, [...] | Bounty: Luffy is the captain of the Straw [...] |
      | 4 | Guts | https://myanimelist.net/character/422/Guts | ガッツ | Kenpuu Denki Berserk | 68,459 | { "eyes": "brown", "hair": "black", [...] | Weight: Guts is the protagonist of the [...] |
      | 5 | Kurisu Makise | [...] | 牧瀬 紅莉栖 | Steins;Gate | 61,763 | { "age": "18", "birthdate": "July 25 (Leo)", [...] | The female protagonist. Kurisu is a research [...] |

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

      | id | title | url | synonyms | japanese | type | volumes | chapters | status | published | genres | themes | demographic | serialization | authors | score | ranked | popularity | members | favorites | synopsis | french | german | spanish |
      |---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
      | 1 | Berserk | https://myanimelist.net/manga/2/Berserk | Berserk: The Prototype | ベルセルク | Manga | Unknown | Unknown | Publishing | Aug 25, 1989 to ? | [ "Action", "Adventure", "Award Winning", [...] | [ "Gore", "Military", "Mythology", [...] | [ "Seinen" ] | Young Animal | [ "(Art)", "(Story & Art),", "Miura, [...] | 9.46 | #1 | #2 | 561,639 | 105,732 | Guts, a former mercenary now known as the [...] |  |  |  |
      | 2 | Fullmetal Alchemist | [...] | Full Metal Alchemist, Hagane no [...] | 鋼の錬金術師 | Manga | 27 | 116 | Finished | Jul 12, 2001 to Sep 11, 2010 | [ "Action", "Adventure", "Award Winning", [...] | [ "Military" ] | [ "Shounen" ] | Shounen Gangan | [ "(Story & Art)", "Arakawa, Hiromu" ] | 9.04 | #7 | #18 | 266,618 | 28,664 | Alchemists are knowledgeable and naturally [...] |  |  |  |
      | 3 | Grand Blue Dreaming | https://myanimelist.net/manga/70345/Grand_Blue |  | ぐらんぶる | Manga | Unknown | Unknown | Publishing | Apr 7, 2014 to ? | [ "Comedy" ] |  | [ "Seinen" ] | good! Afternoon | [ "(Art)", "(Story),", "Inoue, Kenji", [...] | 9.03 | #9 | #50 | 150,741 | 15,337 | Among the seaside town of Izu's ocean waves [...] |  |  |  |
      | 4 | キングダム | https://myanimelist.net/manga/16765/Kingdom |  |  | Manga | Unknown | Unknown | Publishing | Jan 26, 2006 to ? | [ "Action", "Award Winning" ] | [ "Historical", "Military" ] | [ "Seinen" ] | Young Jump | [ "(Story & Art)", "Hara, Yasuhisa" ] | 8.98 | #11 | #58 | 143,187 | 12,887 | During the Warring States period in China, [...] |  |  |  |
      | 5 | One Piece | https://myanimelist.net/manga/13/One_Piece |  | ONE PIECE | Manga | Unknown | Unknown | Publishing | Jul 22, 1997 to ? | [ "Action", "Adventure", "Fantasy" ] |  | [ "Shounen" ] | Shounen Jump (Weekly) | [ "(Story & Art)", "Oda, Eiichiro" ] | 9.20 | #3 | #3 | 510,370 | 101,091 | Gol D. Roger, a man referred to as the [...] |  |  |  |

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

      | id | name | url | image_url | given_name | birthday | member_favorites | hometown | blood_type | favourite_animal | favourite_mangaka | favourite_music | description | alternate_names | height | weight | hobbies | sports | specialty | skills |
      |---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
      | 1 | Oda, Eiichiro | https://myanimelist.net/people/1881/Eiichiro_Oda | [...] | 栄一郎 | Jan 1, 1975 | 47,774 | Kumamoto, Japan | A | Big gentle dogs | Akira Toriyama | '70s soul music | Favourite Real-Life Pirate: Edward Teach [...] |  |  |  |  |  |  |  |
      | 2 | Takahashi, Rie | https://myanimelist.net/people/34785/Rie_Takahashi | [...] | 李依 | Saitama Prefecture, Japan | 46,629 |  |  |  |  |  | She is apart of the seiyuu unit Earphones, [...] | Rieri, Rii-chan |  |  |  |  |  |  |
      | 3 | Miyazaki, Hayao | https://myanimelist.net/people/1870/Hayao_Miyazaki | [...] | 駿 | Jan 5, 1941 | 66,988 |  |  |  |  |  | Miyazaki, the second of four brothers, was [...] |  |  |  |  |  |  |  |
      | 4 | Kamiya, Hiroshi | https://myanimelist.net/people/118/Hiroshi_Kamiya | [...] | 浩史 | Matsudo, Chiba Prefecture, Japan | 103,279 |  | A |  |  |  | Kamiya Hiroshi went to Aoni Juku and decided [...] | ヒロC, HiroC, Kamiyan | 167 cm (5'6") | 53 kg (117 lbs) |  |  |  |  |
      | 5 | Hanazawa, Kana | https://myanimelist.net/people/185/Kana_Hanazawa | [...] | 香菜 | Feb 25, 1989 | 98,748 | Tokyo, Japan | AB |  |  |  | Kana Hanazawa used to be a junior idol in [...] | HanaKana, KanaHana | 156 cm |  |  |  |  |  |

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
      | 1607410 | have a cow | A frequent utterance of Bart Simpson, "Don't [...] | Jimmy Joe had a cow when he learned that his [...] | MsLi | January 29, 2006 |
      | 1921133 | google earthing | What I do when I have nothing else to do. I [...] | I have some time to kill, I think I will go [...] | kginatl | August 16, 2006 |

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

      | id | title | alternative_title | studios | type | episodes | year | season | average_rating | rank | synopsis | notes | tags | content_warnings | url |
      |---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
      | 1 | Demon Slayer: Kimetsu no Yaiba - [...] | Kimetsu no Yaiba: Yuukaku-hen | ufotable | TV | 11 eps | 2021 - 2022 | Fall 2021 | 4.6 out of 5 from 15,932 votes | #1 | Tanjiro and his friends accompany the [...] | Source: Viz | [ "Action", "Adventure", "Fantasy", [...] | [ "Explicit Violence" ] | https://www.anime-planet.com/anime/demon- [...] |
      | 2 | Haikyuu!! Second Season |  | Production I.G | TV | 25 eps | 2015 - 2016 | Fall 2015 | 4.509 out of 5 from 34,240 votes | #13 | After losing to Aoba Johsai at the Inter- [...] | Source: Crunchyroll | [ "Shounen", "Sports", "School Club", [...] |  | https://www.anime-planet.com/anime/haikyuu- [...] |
      | 3 | Haikyuu!! Karasuno High School vs [...] | Haikyuu!! Karasuno Koukou vs Shiratorizawa [...] | Production I.G | TV | 10 eps | 2016 | Fall 2016 | 4.528 out of 5 from 27,284 votes | #9 | Picking up where the second season ended, [...] | Source: Crunchyroll | [ "Shounen", "Sports", "Animeism", "School [...] |  | https://www.anime-planet.com/anime/haikyuu- [...] |
      | 4 | Demon Slayer: Kimetsu no Yaiba Movie - Mugen Train | Kimetsu no Yaiba Movie: Mugen Ressha-hen | ufotable | Movie | 1 ep x 117 min | 2020 |  | 4.522 out of 5 from 24,454 votes | #10 | Tanjirou and the group have completed their [...] | Source: Official Site | [ "Action", "Drama", "Fantasy", "Shounen", [...] | [ "Mature Themes,", "Suicide,", "Violence" ] | https://www.anime-planet.com/anime/demon- [...] |
      | 5 | Violet Evergarden Movie |  | Kyoto Animation | Movie | 1 ep x 140 min | 2020 |  | 4.501 out of 5 from 6,270 votes | #15 | As the world moves on from the war and [...] | Source: Netflix | [ "Drama", "Melancholy", "War", "Based on a [...] | [ "Violence" ] | https://www.anime-planet.com/anime/violet- [...] |

      _and more.._

   </details>


## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'feat: Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

