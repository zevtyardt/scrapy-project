
# Scrapy based Projects
These are collection of some of my web scraping projects with scrapy. Feel free to use them, modify them and suggest modifications.

## Requirements:
1. [Python3.x](https://www.python.org/)
2. [Scrapy framework](https://scrapy.org/)
3. [Sqlalchemy](https://sqlalchemy.org)

see: [requirements.txt](/requirements.txt)

## List Crawlers:
<details>
  <summary><b>kusonime</b></summary>

   | id | title | url | genre | thumbnail | japanese | seasons | producers | type | status | total_episode | score | duration | released_on | sinopsis | download_data |
   |---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
   | 1 | Hanabi-chan wa Okuregachi | https://kusonime.com/hanabichan-batch- [...] | Comedy, Spring 2022 | https://kusonime.com/wp- [...] | ハナビちゃんは遅れがち | Spring 2022 | N/A | TV Series | Ongoing | ? | 6.12 | 4 min. per ep. | Jul 10, 2022 | Musashi Shinonome, manajer baru yang akan [...] | {'name': 'Download Hanabi-chan wa Okuregachi [...] |
   | 2 | Tekken: Bloodline | https://kusonime.com/tekken-bloodline-batch- [...] | Action, Martial Arts, Anime ONA | https://kusonime.com/wp- [...] | Tekken: Bloodline | Anime ONA | N/A | ONA | Completed | 6 | 6.58 | 25 min. per ep. | Aug 18, 2022 | “Kekuatan adalah segalanya.” Jin Kazama [...] | {'name': 'Download Tekken: Bloodline Batch [...] |
   | 3 | Yuuki Yuuna wa Yuusha de Aru: Yuusha no Shou | https://kusonime.com/yuuki-yuuna-wa-yuusha- [...] | Drama, Fantasy, Magic, Slice of Life, Fall 2017 | https://kusonime.com/wp- [...] | 結城友奈は勇者である -勇者の章- | Fall 2017 | Pony Canyon | BD | Completed | 6 | 7.64 | 24 min. per ep. | Nov 25, 2017 | kelanjutan dari cerita Yuki Yuna atau season [...] | {'name': 'Download Yuuki Yuuna wa Yuusha de [...] |
   | 4 | TENSURA : Sukuwareru Ramiris | https://kusonime.com/sukuwareru-ramiris- [...] | Comedy, Fantasy, Anime ONA | https://kusonime.com/wp- [...] | 救われるラミリス | Anime ONA | N/A | ONA | Completed | 2 | 6.18 | 2 min. per ep. | Mar 19, 2022 | Episode spesial melalui streaming youtube [...] | {'name': 'Download TENSURA : Sukuwareru [...] |
   | 5 | Takt Op. Destiny | https://kusonime.com/takt-op-destiny-batch- [...] | Action, Fantasy, Music, Fall 2021 | https://kusonime.com/wp- [...] | takt op.Destiny | Fall 2021 | DeNA, Bandai Namco Arts | BD | Completed | 12 | 7.16 | 23 min. per ep. | Oct 06, 2021 | ceritanya sendiri, suatu hari meteorit hitam [...] | {'name': 'Download Takt Op. Destiny Batch BD [...] |

   _and more.._

</details>
<details>
  <summary><b>myanimelist:anime</b></summary>

   | id | title | url | synonyms | japanese | type | episodes | status | aired | premiered | broadcast | producers | licensors | studios | source | genres | themes | demographic | duration | rating | score | ranked | popularity | members | favorites | synopsis | german | spanish | french |
   |---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
   | 1 | Gintama: Enchousen | [...] | Gintama' (2012), Gintama' Overdrive, Kintama | 銀魂' 延長戦 | TV | 13 | Finished Airing | Oct 4, 2012 to Mar 28, 2013 | Fall 2012 | Thursdays at 18:00 (JST) | Aniplex, Dentsu, Miracle Bus, Shueisha, TV Tokyo | None found,, add some | Sunrise | Manga | Action, Comedy, Sci-Fi | Gag Humor, Historical, Parody, Samurai | Shounen | 24 min. per ep. | PG-13 - Teens 13 or older | 9.04 | #8 | #697 | 288,947 | 2,852 | While Gintoki Sakata was away, the Yorozuya [...] |  |  |  |
   | 2 | Hunter x Hunter | [...] | HxH (2011) | HUNTER×HUNTER（ハンター×ハンター） | TV | 148 | Finished Airing | Oct 2, 2011 to Sep 24, 2014 | Fall 2011 | Sundays at 10:55 (JST) | Nippon Television Network, Shueisha, VAP | VIZ Media | Madhouse | Manga | Action, Adventure, Fantasy |  | Shounen | 23 min. per ep. | PG-13 - Teens 13 or older | 9.04 | #9 | #10 | 2,446,642 | 187,337 | Hunters devote themselves to accomplishing [...] | Hunter x Hunter | Hunter x Hunter | Hunter X Hunter |
   | 3 | Fullmetal Alchemist: Brotherhood | [...] | Hagane no Renkinjutsushi: Fullmetal [...] | 鋼の錬金術師 FULLMETAL ALCHEMIST | TV | 64 | Finished Airing | Apr 5, 2009 to Jul 4, 2010 | Spring 2009 | Sundays at 17:00 (JST) | Aniplex, Mainichi Broadcasting System, [...] | Aniplex of America, Funimation | Bones | Manga | Action, Adventure, Drama, Fantasy | Military | Shounen | 24 min. per ep. | R - 17+ (violence & profanity) | 9.13 | #1 | #3 | 2,961,928 | 206,608 | After a horrific alchemy experiment goes [...] |  |  | Fullmetal Alchemist Brotherhood |
   | 4 | Legend of the Galactic Heroes | [...] | LoGH, LotGH, Gin'eiden, GinEiDen, [...] | 銀河英雄伝説 | OVA | 110 | Finished Airing | Jan 8, 1988 to Mar 17, 1997 |  |  | Kitty Films, TV Tokyo, Tokuma Japan [...] | Sentai Filmworks | Kitty Film Mitaka Studio | Novel | Drama, Sci-Fi | Adult Cast, Military, Space |  | 26 min. per ep. | R - 17+ (violence & profanity) | 9.03 | #11 | #705 | 286,476 | 14,879 | The 150-year-long stalemate between the two [...] |  |  | Les Héros de la Galaxie |
   | 5 | Fruits Basket: The Final Season | [...] | Fruits Basket 3rd Season, Fruits Basket [...] | フルーツバスケット The Final | TV | 13 | Finished Airing | Apr 6, 2021 to Jun 29, 2021 | Spring 2021 | Tuesdays at 01:30 (JST) | 8PAN, Avex Pictures, Hakusensha, Nihon Ad [...] | Funimation | TMS Entertainment | Manga | Drama, Romance, Supernatural |  | Shoujo | 23 min. per ep. | PG-13 - Teens 13 or older | 9.03 | #10 | #512 | 369,489 | 17,088 | Hundreds of years ago, the Chinese Zodiac [...] | Fruits Basket Staffel 3 | Fruits Basket: The Final Season | Fruits Basket Saison 3 |

   _and more.._

</details>
<details>
  <summary><b>myanimelist:manga</b></summary>

   | id | title | url | synonyms | japanese | type | volumes | chapters | status | published | genres | themes | demographic | serialization | authors | score | ranked | popularity | members | favorites | synopsis | french | german | spanish |
   |---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
   | 1 | 20th Century Boys | https://myanimelist.net/manga/3/20th_Century_Boys | 20 Seiki Shounen, Nijuu Seiki Shounen, [...] | 20世紀少年 | Manga | 22 | 249 | Finished | Sep 27, 1999 to Apr 24, 2006 | Award Winning, Drama, Mystery, Sci-Fi | Historical, Psychological | Seinen | Big Comic Spirits | (Story & Art), Urasawa, Naoki | 8.95 | #12 | #29 | 198,889 | 15,944 | As the 20th century approaches its end, [...] |  |  |  |
   | 2 | Vinland Saga | https://myanimelist.net/manga/642/Vinland_Saga |  | ヴィンランド・サガ | Manga | Unknown | Unknown | Publishing | Apr 13, 2005 to ? | Action, Adventure, Award Winning, Drama | Historical | Seinen | Afternoon | (Story & Art), Yukimura, Makoto | 8.99 | #10 | #23 | 238,524 | 25,402 | Thorfinn, son of one of the Vikings' [...] |  |  |  |
   | 3 | Grand Blue Dreaming | https://myanimelist.net/manga/70345/Grand_Blue |  | ぐらんぶる | Manga | Unknown | Unknown | Publishing | Apr 7, 2014 to ? | Comedy |  | Seinen | good! Afternoon | (Art), (Story),, Inoue, Kenji, Yoshioka, Kimitake | 9.03 | #9 | #50 | 150,624 | 15,316 | Among the seaside town of Izu's ocean waves [...] |  |  |  |
   | 4 | Berserk | https://myanimelist.net/manga/2/Berserk | Berserk: The Prototype | ベルセルク | Manga | Unknown | Unknown | Publishing | Aug 25, 1989 to ? | Action, Adventure, Award Winning, Drama, [...] | Gore, Military, Mythology, Psychological | Seinen | Young Animal | (Art), (Story & Art),, Miura, Kentarou, [...] | 9.46 | #1 | #2 | 561,072 | 105,605 | Guts, a former mercenary now known as the [...] |  |  |  |
   | 5 | キングダム | https://myanimelist.net/manga/16765/Kingdom |  |  | Manga | Unknown | Unknown | Publishing | Jan 26, 2006 to ? | Action, Award Winning | Historical, Military | Seinen | Young Jump | (Story & Art), Hara, Yasuhisa | 8.98 | #11 | #58 | 143,045 | 12,871 | During the Warring States period in China, [...] |  |  |  |

   _and more.._

</details>
<details>
  <summary><b>myanimelist:character</b></summary>

   | id | name | url | japanese | source | favorites | biodata | description |
   |---|---|---|---|---|---|---|---|
   | 1 | Levi | https://myanimelist.net/character/45627/Levi | リヴァイ | Shingeki no Kyojin | 131,621 | {'birthday': 'December 25', 'height': '160 [...] | Levi is known as humanity's most powerful [...] |
   | 2 | Light Yagami | https://myanimelist.net/character/80/Light_Yagami | 夜神 月 | Death Note | 89,887 | {'birthdate': 'February 28, 1986 (1989 in [...] | Age (during the series): 17-23 Light, born [...] |
   | 3 | Lelouch Lamperouge | [...] | ルルーシュ・ランペルージ | Code Geass: Hangyaku no Lelouch | 157,525 | {'age': '17 (first season), 18 (second [...] | Lelouch vi Britannia (ルルーシュ・ヴィ・ブリタニア, [...] |
   | 4 | Zoro Roronoa | https://myanimelist.net/character/62/Zoro_Roronoa | ロロノア・ゾロ | One Piece | 95,836 | {'age': '19; 21', 'birthdate': 'November 11, [...] | Bounty: Zoro was the first crew member to be [...] |
   | 5 | L Lawliet | https://myanimelist.net/character/71/L_Lawliet | エル ローライト | Death Note | 120,186 | {'birthday': 'October 31, 1979 (1982 in [...] | L, who also uses the aliases Hideki Ryuga, [...] |

   _and more.._

</details>
