
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
      | 1 | Hanabi-chan wa Okuregachi | https://kusonime.com/hanabichan-batch- [...] | [ "Comedy", "Spring 2022" ] | https://kusonime.com/wp- [...] | ハナビちゃんは遅れがち | Spring 2022 | N/A | TV Series | Ongoing | ? | 6.12 | 4 min. per ep. | Jul 10, 2022 | Hanabi-chan wa Okuregachi | [ { "name": "Download Hanabi-chan wa [...] |
      | 2 | Yuuki Yuuna wa Yuusha de Aru: Yuusha no Shou | https://kusonime.com/yuuki-yuuna-wa-yuusha- [...] | [ "Drama", "Fantasy", "Magic", "Slice of [...] | https://kusonime.com/wp- [...] | 結城友奈は勇者である -勇者の章- | Fall 2017 | Pony Canyon | BD | Completed | 6 | 7.64 | 24 min. per ep. | Nov 25, 2017 | Yuuki Yuuna wa Yuusha de Aru: Yuusha no Shou | [ { "name": "Download Yuuki Yuuna wa Yuusha [...] |
      | 3 | Xiao Mo Tou Baolu La! (Busted! Darklord) | https://kusonime.com/xiao-mo-tou-baolu-la- [...] | [ "Comedy", "Anime ONA" ] | https://kusonime.com/wp- [...] | 小魔头暴露啦！ | Anime ONA | N/A | ONA | Completed | 26 | 6.38 | 8 min. per ep. | Jan 15, 2022 | Xiao Mo Tou Baolu La! (Busted! Darklord) | [ { "name": "Download Xiao Mo Tou Baolu La! [...] |
      | 4 | TENSURA : Sukuwareru Ramiris | https://kusonime.com/sukuwareru-ramiris- [...] | [ "Comedy", "Fantasy", "Anime ONA" ] | https://kusonime.com/wp- [...] | 救われるラミリス | Anime ONA | N/A | ONA | Completed | 2 | 6.18 | 2 min. per ep. | Mar 19, 2022 | TENSURA : Sukuwareru Ramiris | [ { "name": "Download TENSURA : Sukuwareru [...] |
      | 5 | Steamboy | https://kusonime.com/steamboy-bd-subtitle- [...] | [ "Action", "Adventure", "Drama", [...] | https://kusonime.com/wp- [...] | スチームボーイ | Anime Movie | Bandai Visual, Dentsu, TBS, Imagica, Bandai, [...] | Movie | Completed | 1 | 7.33 | 2 hr. 6 min. | Jul 17, 2004 | Steamboy | [ { "name": "Download Movie Steamboy BD [...] |

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
      | 1 | Fullmetal Alchemist: Brotherhood | [...] | Hagane no Renkinjutsushi: Fullmetal [...] | 鋼の錬金術師 FULLMETAL ALCHEMIST | Fullmetal Alchemist Brotherhood | TV | 64 | Finished Airing | Apr 5, 2009 to Jul 4, 2010 | Spring 2009 | Sundays at 17:00 (JST) | [ "Aniplex", "Mainichi Broadcasting System", [...] | [ "Aniplex of America", "Funimation" ] | Bones | Manga | [ "Action", "Adventure", "Drama", "Fantasy" ] | [ "Military" ] | [ "Shounen" ] | 24 min. per ep. | R - 17+ (violence & profanity) | 9.13 | #1 | #3 | 2,962,215 | 206,625 | After a horrific alchemy experiment goes [...] |  |  |
      | 2 | Attack on Titan Season 3 Part 2 | [...] |  | 進撃の巨人 Season3 Part.2 | L'Attaque des Titans Saison 3 Partie 2 | TV | 10 | Finished Airing | Apr 29, 2019 to Jul 1, 2019 | Spring 2019 | Mondays at 00:10 (JST) | [ "Dentsu", "Kodansha", "Mainichi [...] | Funimation | Wit Studio | Manga | [ "Action", "Drama" ] | [ "Gore", "Military", "Survival" ] | [ "Shounen" ] | 23 min. per ep. | R - 17+ (violence & profanity) | 9.07 | #5 | #28 | 1,907,439 | 52,330 | Seeking to restore humanity's diminishing [...] | Attack on Titan Staffel 3 Teil 2 | Ataque a los Titanes Temporada 3 Parte 2 |
      | 3 | Hunter x Hunter | [...] | HxH (2011) | HUNTER×HUNTER（ハンター×ハンター） | Hunter X Hunter | TV | 148 | Finished Airing | Oct 2, 2011 to Sep 24, 2014 | Fall 2011 | Sundays at 10:55 (JST) | [ "Nippon Television Network", "Shueisha", "VAP" ] | VIZ Media | Madhouse | Manga | [ "Action", "Adventure", "Fantasy" ] |  | [ "Shounen" ] | 23 min. per ep. | PG-13 - Teens 13 or older | 9.04 | #9 | #10 | 2,446,950 | 187,355 | Hunters devote themselves to accomplishing [...] | Hunter x Hunter | Hunter x Hunter |
      | 4 | Gintama: The Very Final | [...] |  | 銀魂 THE FINAL |  | Movie | 1 | Finished Airing | Jan 8, 2021 |  |  | [ "TV Tokyo", "Warner Bros. Japan" ] | Eleven Arts | Bandai Namco Pictures | Manga | [ "Action", "Comedy", "Drama", "Sci-Fi" ] | [ "Gag Humor", "Historical", "Parody", "Samurai" ] | [ "Shounen" ] | 1 hr. 44 min. | PG-13 - Teens 13 or older | 9.05 | #7 | #1651 | 110,809 | 3,723 | Two years have passed following the [...] | N/A |  |
      | 5 | Fruits Basket: The Final Season | [...] | Fruits Basket 3rd Season, Fruits Basket [...] | フルーツバスケット The Final | Fruits Basket Saison 3 | TV | 13 | Finished Airing | Apr 6, 2021 to Jun 29, 2021 | Spring 2021 | Tuesdays at 01:30 (JST) | [ "8PAN", "Avex Pictures", "Hakusensha", [...] | Funimation | TMS Entertainment | Manga | [ "Drama", "Romance", "Supernatural" ] |  | [ "Shoujo" ] | 23 min. per ep. | PG-13 - Teens 13 or older | 9.03 | #10 | #512 | 369,591 | 17,092 | Hundreds of years ago, the Chinese Zodiac [...] | Fruits Basket Staffel 3 | Fruits Basket: The Final Season |

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
      | 1 | Lelouch Lamperouge | [...] | ルルーシュ・ランペルージ | Code Geass: Hangyaku no Lelouch | 157,542 | { "code geass": "Fukkatsu no Lelouch", [...] | Remove from Favorites Add to Favorites [...] |
      | 2 | Rintarou Okabe | [...] | 岡部 倫太郎 | Steins;Gate | 89,325 | { "age": "18 (Steins;Gate), 19 (Steins;Gate [...] | Remove from Favorites Add to Favorites [...] |
      | 3 | Light Yagami | https://myanimelist.net/character/80/Light_Yagami | 夜神 月 | Death Note | 89,899 | { "death note": "Rewrite", "birthdate": [...] | Remove from Favorites Add to Favorites [...] |
      | 4 | Zoro Roronoa | https://myanimelist.net/character/62/Zoro_Roronoa | ロロノア・ゾロ | One Piece | 95,845 | { "one piece": "Roronoa Zoro, Umi ni Chiru", [...] | Remove from Favorites Add to Favorites [...] |
      | 5 | Killua Zoldyck | [...] | キルア=ゾルディック | Hunter x Hunter | 88,951 | { "hunter x hunter": "Greed Island Final", [...] | Remove from Favorites Add to Favorites [...] |

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
      | 1 | Berserk | https://myanimelist.net/manga/2/Berserk | Berserk: The Prototype | ベルセルク | Manga | Unknown | Unknown | Publishing | Aug 25, 1989 to ? | [ "Action", "Adventure", "Award Winning", [...] | [ "Gore", "Military", "Mythology", [...] | [ "Seinen" ] | Young Animal | [ "(Art)", "(Story & Art),", "Miura, [...] | 9.46 | #1 | #2 | 561,175 | 105,629 | Guts, a former mercenary now known as the [...] |  |  |  |
      | 2 | Vagabond | https://myanimelist.net/manga/656/Vagabond |  | バガボンド | Manga | 37 | 327 | On Hiatus | Sep 3, 1998 to May 21, 2015 | [ "Action", "Adventure", "Award Winning" ] | [ "Historical", "Samurai" ] | [ "Seinen" ] | Morning | [ "(Story & Art),", "(Story)", "Inoue, [...] | 9.19 | #4 | #16 | 290,247 | 30,782 | In 16th-century Japan, Shinmen Takezou is a [...] |  |  |  |
      | 3 | キングダム | https://myanimelist.net/manga/16765/Kingdom |  |  | Manga | Unknown | Unknown | Publishing | Jan 26, 2006 to ? | [ "Action", "Award Winning" ] | [ "Historical", "Military" ] | [ "Seinen" ] | Young Jump | [ "(Story & Art)", "Hara, Yasuhisa" ] | 8.98 | #11 | #58 | 143,069 | 12,875 | During the Warring States period in China, [...] |  |  |  |
      | 4 | Grand Blue Dreaming | https://myanimelist.net/manga/70345/Grand_Blue |  | ぐらんぶる | Manga | Unknown | Unknown | Publishing | Apr 7, 2014 to ? | [ "Comedy" ] |  | [ "Seinen" ] | good! Afternoon | [ "(Art)", "(Story),", "Inoue, Kenji", [...] | 9.03 | #9 | #50 | 150,649 | 15,320 | Among the seaside town of Izu's ocean waves [...] |  |  |  |
      | 5 | ジョジョの奇妙な冒険 Part7 STEEL BALL RUN | [...] | JoJo's Bizarre Adventure Part 7: Steel Ball [...] |  | Manga | 24 | 96 | Finished | Jan 19, 2004 to Apr 19, 2011 | [ "Action", "Adventure", "Mystery", [...] | [ "Historical" ] | [ "Seinen", "Shounen" ] | Ultra Jump | [ "(Story & Art)", "Araki, Hirohiko" ] | 9.28 | #2 | #27 | 212,356 | 35,943 | In the American Old West, the world's [...] | Steel Ball Run |  |  |

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

      | id | name | url | image_url | given_name | birthday | member_favorites | description | alternate_names | height | weight | blood_type | hometown | favourite_animal | favourite_mangaka | favourite_music | hobbies | skills | pets | debut_role | agency | dislikes | places_he_wants_to_visit | awards |
      |---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
      | 1 | Miyazaki, Hayao | https://myanimelist.net/people/1870/Hayao_Miyazaki | [...] | 駿 | Jan 5, 1941 | 66,974 | Miyazaki, the second of four brothers, was [...] |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
      | 2 | Kamiya, Hiroshi | https://myanimelist.net/people/118/Hiroshi_Kamiya | [...] | 浩史 | Matsudo, Chiba Prefecture, Japan | 103,260 | Kamiya Hiroshi went to Aoni Juku and decided [...] | ヒロC, HiroC, Kamiyan | 167 cm (5'6") | 53 kg (117 lbs) | A |  |  |  |  |  |  |  |  |  |  |  |  |
      | 3 | Oda, Eiichiro | https://myanimelist.net/people/1881/Eiichiro_Oda | [...] | 栄一郎 | Jan 1, 1975 | 47,763 | Favourite Real-Life Pirate: Edward Teach [...] |  |  |  | A | Kumamoto, Japan | Big gentle dogs | Akira Toriyama | '70s soul music |  |  |  |  |  |  |  |  |
      | 4 | Miyano, Mamoru | https://myanimelist.net/people/65/Mamoru_Miyano | [...] | 真守 | Jun 8, 1983 | 86,711 | Mamoru Miyano won Best Voice Actor award in [...] |  | 182 cm | 70 kg | B | Saitama, Japan |  |  |  | singing, soccer | harmonica, harp |  |  |  |  |  |  |
      | 5 | Hayami, Saori | https://myanimelist.net/people/869/Saori_Hayami | [...] | Saori Matsuo (松尾 沙織) | May 29, 1991 | 57,364 | Member of duet "Blue Drops" with Yoshida [...] | Saori Matsuo, 松尾 沙織 | 164 cm |  | AB | Tokyo, Japan |  |  |  |  |  |  |  |  |  |  |  |

      _and more.._

   </details>

