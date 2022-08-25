
# Scrapy based Projects
These are collection of some of my web scraping projects with scrapy. Feel free to use them, modify them and suggest modifications.

## Requirements:
1. [Python3.x](https://www.python.org/)
2. [Scrapy framework](https://scrapy.org/)
3. [Sqlalchemy](https://sqlalchemy.org)

see: [requirements.txt](/requirements.txt)

## List Crawlers:
1. **kusonime**</br>
   |     |     |
   | --- | --- |
   | spider name | kusonime |
   | source | http://kusonime.com/ |

   <details>
     <summary><i>output example</i></summary>

      | id | title | url | genre | thumbnail | japanese | seasons | producers | type | status | total_episode | score | duration | released_on | sinopsis | download_data |
      |---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
      | 1 | Hanabi-chan wa Okuregachi | https://kusonime.com/hanabichan-batch- [...] | [ "Comedy", "Spring 2022" ] | https://kusonime.com/wp- [...] | ハナビちゃんは遅れがち | Spring 2022 | N/A | TV Series | Ongoing | ? | 6.12 | 4 min. per ep. | Jul 10, 2022 | Musashi Shinonome, manajer baru yang akan [...] | [ { "name": "Download Hanabi-chan wa [...] |
      | 2 | Shikong Zhi Xi (Time Space Rift) | https://kusonime.com/shikong-zhi-xi-batch- [...] | [ "Action", "Anime ONA" ] | https://kusonime.com/wp- [...] | 时空之隙 | Anime ONA | B.CMAY PICTURES, bilibili | ONA | Completed | 13 | 6.49 | 21 min. per ep. | Apr 15, 2022 | Energi yang tidak stabil dari dunia saat ini [...] | [ { "name": "Download Shikong Zhi Xi Batch [...] |
      | 3 | Gaikotsu Kishi-sama Tadaima Isekai e Odekakechuu | https://kusonime.com/skeleton-knight-batch- [...] | [ "Action", "Fantasy", "Spring 2022" ] | https://kusonime.com/wp- [...] | 骸骨騎士様、只今異世界へお出掛け中 | Spring 2022 | Pony Canyon, AT-X, DAX Production, Docomo [...] | BD | Completed | 12 | 7.31 | 23 min. per ep. | Apr 07, 2022 | selain Ainz-sama ada juga tengkorak [...] | [ { "name": "Download Gaikotsu Kishi-sama [...] |
      | 4 | Steamboy | https://kusonime.com/steamboy-bd-subtitle- [...] | [ "Action", "Adventure", "Drama", [...] | https://kusonime.com/wp- [...] | スチームボーイ | Anime Movie | Bandai Visual, Dentsu, TBS, Imagica, Bandai, [...] | Movie | Completed | 1 | 7.33 | 2 hr. 6 min. | Jul 17, 2004 | Becerita tentang cowok 13 tahun bernama [...] | [ { "name": "Download Movie Steamboy BD [...] |
      | 5 | Xiao Mo Tou Baolu La! (Busted! Darklord) | https://kusonime.com/xiao-mo-tou-baolu-la- [...] | [ "Comedy", "Anime ONA" ] | https://kusonime.com/wp- [...] | 小魔头暴露啦！ | Anime ONA | N/A | ONA | Completed | 26 | 6.38 | 8 min. per ep. | Jan 15, 2022 | Dalam upaya untuk bertahan hidup, Yu Renjie, [...] | [ { "name": "Download Xiao Mo Tou Baolu La! [...] |

      _and more.._

   </details>

1. **myanimelistanime**</br>
   |     |     |
   | --- | --- |
   | spider name | mal:anime |
   | source | https://myanimelist.net/topanime.php |

   <details>
     <summary><i>output example</i></summary>

      | id | title | url | synonyms | japanese | french | type | episodes | status | aired | premiered | broadcast | producers | licensors | studios | source | genres | theme | demographic | duration | rating | score | ranked | popularity | members | favorites | synopsis | german | spanish |
      |---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
      | 1 | Fullmetal Alchemist: Brotherhood | [...] | Hagane no Renkinjutsushi: Fullmetal [...] | 鋼の錬金術師 FULLMETAL ALCHEMIST | Fullmetal Alchemist Brotherhood | TV | 64 | Finished Airing | Apr 5, 2009 to Jul 4, 2010 | Spring 2009 | Sundays at 17:00 (JST) | [ "Aniplex", "Mainichi Broadcasting System", [...] | [ "Aniplex of America", "Funimation" ] | Bones | Manga | [ "Action", "Adventure", "Drama", "Fantasy" ] | [ "Military" ] | [ "Shounen" ] | 24 min. per ep. | R - 17+ (violence & profanity) | 9.13 | #1 | #3 | 2,962,010 | 206,610 | After a horrific alchemy experiment goes [...] |  |  |
      | 2 | Gintama Season 4 | https://myanimelist.net/anime/28977/Gintama° | Gintama' (2015) | 銀魂° | Gintama Saison 4 | TV | 51 | Finished Airing | Apr 8, 2015 to Mar 30, 2016 | Spring 2015 | Wednesdays at 18:00 (JST) | [ "Aniplex", "Dentsu", "TV Tokyo" ] | [ "Crunchyroll", "Funimation" ] | Bandai Namco Pictures | Manga | [ "Action", "Comedy", "Sci-Fi" ] | [ "Gag Humor", "Historical", "Parody", "Samurai" ] | [ "Shounen" ] | 24 min. per ep. | PG-13 - Teens 13 or older | 9.08 | #3 | #338 | 550,787 | 14,871 | Gintoki, Shinpachi, and Kagura return as the [...] | Gintama Season 4 | Gintama Temporada 4 |
      | 3 | Fate/stay night: Heaven's Feel - III. Spring Song | [...] | Fate/stay night Movie: Heaven's Feel 3 | 劇場版「Fate/stay night [Heaven's Feel] [...] | Fate/stay night: Heaven's Feel - III. Spring Song | Movie | 1 | Finished Airing | Aug 15, 2020 |  |  | [ "Aniplex", "Kadokawa", "Notes" ] | Aniplex of America | ufotable | Visual novel | [ "Action", "Fantasy", "Supernatural" ] |  |  | 2 hr. 2 min. | R - 17+ (violence & profanity) | 8.70 | #50 | #704 | 287,013 | 7,089 | The Fifth Holy Grail War in Fuyuki City has [...] |  |  |
      | 4 | Steins;Gate | https://myanimelist.net/anime/9253/Steins_Gate |  | STEINS;GATE |  | TV | 24 | Finished Airing | Apr 6, 2011 to Sep 14, 2011 | Spring 2011 | Wednesdays at 02:05 (JST) | [ "AT-X", "Frontier Works", "Kadokawa [...] | Funimation | White Fox | Visual novel | [ "Drama", "Sci-Fi", "Suspense" ] | [ "Psychological", "Time Travel" ] |  | 24 min. per ep. | PG-13 - Teens 13 or older | 9.08 | #4 | #13 | 2,288,040 | 174,453 | Eccentric scientist Rintarou Okabe has a [...] |  |  |
      | 5 | Kaguya-sama: Love is War - Ultra Romantic | https://myanimelist.net/anime/43608/Kaguya- [...] | Kaguya-sama wa Kokurasetai: Tensai-tachi no [...] | かぐや様は告らせたい-ウルトラロマンティック- |  | TV | 13 | Finished Airing | Apr 9, 2022 to Jun 25, 2022 | Spring 2022 | Saturdays at 00:00 (JST) | [ "Aniplex", "JR East Marketing & [...] | Aniplex of America | A-1 Pictures | Manga | [ "Comedy", "Suspense" ] | [ "Psychological", "Romantic Subtext", "School" ] | [ "Seinen" ] | 23 min. per ep. | PG-13 - Teens 13 or older | 9.13 | #2 | #274 | 633,220 | 22,828 | The elite members of Shuchiin Academy's [...] |  |  |

      _and more.._

   </details>

1. **myanimelistcharacter**</br>
   |     |     |
   | --- | --- |
   | spider name | mal:character |
   | source | https://myanimelist.net/character.php |

   <details>
     <summary><i>output example</i></summary>

      | id | name | url | japanese | source | favorites | biodata | description |
      |---|---|---|---|---|---|---|---|
      | 1 | Lelouch Lamperouge | [...] | ルルーシュ・ランペルージ | Code Geass: Hangyaku no Lelouch | 157,531 | { "age": "17 (first season), 18 (second [...] | Lelouch vi Britannia (ルルーシュ・ヴィ・ブリタニア, [...] |
      | 2 | Levi | https://myanimelist.net/character/45627/Levi | リヴァイ | Shingeki no Kyojin | 131,616 | { "birthday": "December 25", "height": "160 [...] | Levi is known as humanity's most powerful [...] |
      | 3 | Luffy Monkey D. | [...] | モンキー・D・ルフィ | One Piece | 120,134 | { "age": "17; 19", "birthdate": "May 5, [...] | Bounty: Luffy is the captain of the Straw [...] |
      | 4 | L Lawliet | https://myanimelist.net/character/71/L_Lawliet | エル ローライト | Death Note | 120,189 | { "birthday": "October 31, 1979 (1982 in [...] | L, who also uses the aliases Hideki Ryuga, [...] |
      | 5 | Holo | https://myanimelist.net/character/7373/Holo | ホロ | Ookami to Koushinryou | 26,747 | { "age": "Unknown", "height": "160 cm", [...] | Holo is a wolf harvest deity originally from [...] |

      _and more.._

   </details>

1. **myanimelistmanga**</br>
   |     |     |
   | --- | --- |
   | spider name | mal:manga |
   | source | https://myanimelist.net/topmanga.php |

   <details>
     <summary><i>output example</i></summary>

      | id | title | url | synonyms | japanese | type | volumes | chapters | status | published | genres | themes | demographic | serialization | authors | score | ranked | popularity | members | favorites | synopsis | french | german |
      |---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
      | 1 | Berserk | https://myanimelist.net/manga/2/Berserk | Berserk: The Prototype | ベルセルク | Manga | Unknown | Unknown | Publishing | Aug 25, 1989 to ? | [ "Action", "Adventure", "Award Winning", [...] | [ "Gore", "Military", "Mythology", [...] | [ "Seinen" ] | Young Animal | [ "(Art)", "(Story & Art),", "Miura, [...] | 9.46 | #1 | #2 | 561,107 | 105,616 | Guts, a former mercenary now known as the [...] |  |  |
      | 2 | ジョジョの奇妙な冒険 Part7 STEEL BALL RUN | [...] | JoJo's Bizarre Adventure Part 7: Steel Ball [...] |  | Manga | 24 | 96 | Finished | Jan 19, 2004 to Apr 19, 2011 | [ "Action", "Adventure", "Mystery", [...] | [ "Historical" ] | [ "Seinen", "Shounen" ] | Ultra Jump | [ "(Story & Art)", "Araki, Hirohiko" ] | 9.28 | #2 | #27 | 212,316 | 35,940 | In the American Old West, the world's [...] | Steel Ball Run |  |
      | 3 | 〈物語〉シリーズ ファーストシーズン | [...] | Bakemonogatari, Monster Tale, [...] |  | Light Novel | 6 | 107 | Finished | Nov 1, 2006 to Jul 28, 2010 | [ "Action", "Comedy", "Mystery", "Romance", [...] | [ "Vampire" ] |  | Mephisto | [ "(Art)", "(Story),", "NISIO, ISIN", "VOFAN" ] | 8.95 | #13 | #255 | 52,740 | 2,850 | This is a story, a "ghostory" of sorts, [...] |  |  |
      | 4 | One Piece | https://myanimelist.net/manga/13/One_Piece |  | ONE PIECE | Manga | Unknown | Unknown | Publishing | Jul 22, 1997 to ? | [ "Action", "Adventure", "Fantasy" ] |  | [ "Shounen" ] | Shounen Jump (Weekly) | [ "(Story & Art)", "Oda, Eiichiro" ] | 9.20 | #3 | #3 | 509,853 | 100,992 | Gol D. Roger, a man referred to as the [...] |  |  |
      | 5 | Vagabond | https://myanimelist.net/manga/656/Vagabond |  | バガボンド | Manga | 37 | 327 | On Hiatus | Sep 3, 1998 to May 21, 2015 | [ "Action", "Adventure", "Award Winning" ] | [ "Historical", "Samurai" ] | [ "Seinen" ] | Morning | [ "(Story & Art),", "(Story)", "Inoue, [...] | 9.19 | #4 | #16 | 290,208 | 30,783 | In 16th-century Japan, Shinmen Takezou is a [...] |  |  |

      _and more.._

   </details>

