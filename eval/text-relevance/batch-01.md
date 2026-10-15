# Embedding text relevance, batch 1 of 12 (albums 1–25 of 300)

## Task

Crate recommends albums by embedding text. For each album below you see the **exact text the embedding model reads**: the album's English Wikipedia article after Crate's cleaning step (track listings, charts, references and similar sections removed; credit lines that aren't purely crew kept), split into the 250-word chunks that are each embedded separately and then averaged. Nothing else is filtered.

The question is whether this text is relevant for finding **similar-sounding albums**. Grade every chunk:

| Grade | Meaning |
|---|---|
| 2 | Mostly describes the music: genre/style, instrumentation, production, vocals, tempo, mood, lyrical themes, or comparisons to other artists' sound. |
| 1 | Mixed: some real description of the music alongside unrelated material. |
| 0 | Not about the sound: release dates, labels, charts, sales, tours, band history or biography, studios, artwork, personnel lists, awards. |

Rules:
- Grade what the chunk says, not what you know about the album.
- Grade each chunk on its own. Text cut off mid-sentence at a chunk edge is normal.
- Tags are shown only to identify the album; don't grade them.

## Output format

Reply with **one fenced `jsonl` block**, one line per chunk, nothing else in the block. Copy `album_id` exactly; `chunk` is the chunk number shown. `note` is at most 12 words naming what the chunk is mostly about.

```jsonl
{"album_id": "<album id>", "chunk": 1, "grade": 0, "note": "release date, label, chart peaks"}
```

This batch: **25 albums, 114 chunks**.

## Album 1: He Poos Clouds — Final Fantasy

- **album_id:** `2b25433a-d520-49e8-9b15-851776db9708`
- **Tags (identification only):** indie rock, rock, 2006, canada, canadian, canadien, experimental, indie
- **Chunks:** 1 (173 words)

### Album 1, chunk 1

```text
He Poos Clouds is the second studio album by Canadian indie musician Owen Pallett, under the pseudonym Final Fantasy. It was released on June 13, 2006, on Blocks Recording Club in Canada and Tomlab internationally. The songs on the album (excluding the fifth and tenth tracks) are loosely connected to the eight schools of magic in the role-playing game Dungeons & Dragons, and the title track's lyrics ostensibly refer to the Nintendo video game series The Legend of Zelda, as well as The Chronicles of Narnia. Pallett has also said that the album is a reflection on how atheists confront death. The track "This Lamb Sells Condos" refers to the Toronto real estate developer Brad J. Lamb, who had previously used the song's title phrase as an advertising slogan. In the song, Pallett imagines an argument between the developer and his wife that alludes heavily to various fashion designers. The album cover art is by Robin Fry. The album was named the winner of the 2006 Polaris Music Prize on September 18, 2006.
```

## Album 2: Figure Number Five — Soilwork

- **album_id:** `b9425d98-9d83-4b77-953a-b679b2ec710f`
- **Tags (identification only):** death metal, melodic death metal, heavy metal, metal, nuclear blast records, rock, sweden, swedish
- **Chunks:** 2 (406 words)

### Album 2, chunk 1

```text
Figure Number Five is the fifth studio album by Swedish melodic death metal band Soilwork. The record was released on 22 April 2003 through Nuclear Blast label. On this release, the band introduces more elements of alternative metal into their melodic death metal style. This would be the last album with Henry Ranta on drums before he left the band after its release. A few different editions of this album existed upon release. The normal release with eleven tracks, as well as a limited edition release with a second CD including their 1997 demo In Dreams We Fall into the Eternal Lake plus two songs from the Steelbath Suicide demo session. The limited vinyl version of the album features two discs - this album and Natural Born Chaos, black and the other a white-colored vinyl. The Japanese version of the album includes one bonus track, entitled "Bursting Out". This album marked keyboardist Sven Karlsson's first attempts at songwriting for the band. While it is not necessarily interconnected with the keyboardist songwriting, this album features more use of the keyboard and lighter melodies. The album is considered a more commercial sound by most fans of Swedish death metal, but it arguably gives the music a broader appeal. However, vocalist Björn Strid has said the album has good melodies but lacks in intensity and could have been better composed; many fans and critics considered the album "rushed". Music videos were made for the songs "Rejection Role" and "Light the Torch". The music
```

### Album 2, chunk 2

```text
video for "Rejection Role" showed the band playing in a club and being constantly pestered and booed by the members of In Flames, with interspersed footage of other incidents between the two bands. In Flames's video for "Trigger" showed the situation vice versa, In Flames playing and Soilwork as the bullies. The colour is also reversed in each video: blue for In Flames, red for Soilwork. Both videos also had the other band riding in a pickup truck to and from the club. While some believed the tension between the two bands to be real, in reality the groups are close friends and devised the idea of a dual-video concept as a joke. This was the last album to feature Henry Ranta on drums. In 2005, Figure Number Five was ranked number 398 in Rock Hard magazine's book The 500 Greatest Rock & Metal Albums of All Time. Bryan Kaschak – Guitar on "Cranking the Sirens"
```

## Album 3: Dedication — Herbie Hancock

- **album_id:** `f9bfdd6f-12e1-48fd-ae3b-d617e212a128`
- **Tags (identification only):** jazz, electronic, experimental, funk, fusion, hard bop, jazz instrument, modal music
- **Chunks:** 1 (114 words)

### Album 3, chunk 1

```text
Dedication is the thirteenth album by American jazz pianist Herbie Hancock. It was recorded in Japan by Hancock alone in 1974 during a Japanese tour. Hancock performs "Maiden Voyage" and "Dolphin Dance" on piano, while "Nobu" and "Cantaloupe Island" were performed on electric keyboards and synthesizers. First released on LP by the Japanese CBS/Sony on September 21, 1974, it was not released on CD outside Japan until 2013, first as part of the 34 disc box set The Complete Columbia Album Collection 1972–1988. It was given an individual reissue in 2014 by Wounded Bird Records. Herbie Hancock - acoustic piano (#1–2), Fender Rhodes, ARP Pro Soloist, ARP Odyssey, ARP 2600, ARP String Ensemble (#3–4)
```

## Album 4: 13 — Die Ärzte

- **album_id:** `148918df-a667-403d-8f9f-29e634b1ced1`
- **Tags (identification only):** punk, deutsch, pop punk, pop rock, pregaptrack, punk rock, rock
- **Chunks:** 1 (149 words)

### Album 4, chunk 1

```text
13 is the eighth studio album by German rock band Die Ärzte, released on 25 May 1998. It is their most successful album, going platinum in Germany and gold in Austria and Switzerland. The 13th track, "Männer sind Schweine", is their most successful single. The CD version of the album features a hidden track in the pregap of the first song. This technique was later used frequently—on Geräusch, Jazz ist anders, Farin Urlaub's Am Ende der Sonne, and Bela B.'s Bingo. On vinyl versions of Jazz ist anders and Am Ende der Sonne though, the hidden tracks are not lost, but put after the last track. The album features many film and TV samples. Samples are used on tracks 1, 4, 5, 8, 10, 12, 13, 16, and on the hidden track. Farin Urlaub – guitar, vocals Bela Felsenheimer – drums, vocals Rodrigo González – bass guitar, guitar, vocals
```

## Album 5: Mr. Wonderful — Fleetwood Mac

- **album_id:** `536ca3e8-d380-4077-9692-add1c7ba09a9`
- **Tags (identification only):** blues rock, rock, blues, classic rock, country blues, pop rock, should be public domain, soft rock
- **Chunks:** 4 (1049 words)

### Album 5, chunk 1

```text
Mr. Wonderful is the second studio album by British blues rock band Fleetwood Mac, released on 23 August 1968. In the US, the album was not released, though around half of the tracks appeared on English Rose. An expanded version of Mr. Wonderful was included in the box set The Complete Blue Horizon Sessions. The album was broadly similar to Fleetwood Mac's self-titled debut album, albeit with some changes to personnel and recording method. The album was recorded live in the studio with miked amplifiers and PA system, rather than plugged into the board. The vocals were distorted with a Vox amplifier and most of the album was recorded in mono. A horn section was featured throughout the album and Christine Perfect (later Christine McVie) of Chicken Shack played keyboards. Mike Vernon, who served as the producer on the album, placed baffles and wooden partitions between the instruments to avoid audio spill. Peter Green's material on the album was recorded on 28 April 1968, the same day that the band re-recorded their cover of "Need Your Love So Bad". One song from that session, "Stop Messin' Round", was recorded in five takes. "Rollin' Man", "Love That Burns", "If You Be My Baby", and "Lazy Poker Blues" were also recorded that same day. Green remembered that Jeremy Spencer opted not to play on his tracks on Mr Wonderful. Clifford Davis received writing credits on Green's songs under the name C.G. Adams; Green told Guitar Player magazine in a 1994 interview that
```

### Album 5, chunk 2

```text
Davis did so as a "tax dodge". A second session was booked to record six tracks sung by Spencer, who granted the horn section leeway when determining what to play on his compositions, telling them to "just blow". The album took a total of four days to record. "Trying So Hard to Forget", the album's final song, was a duet between Green on guitar and Duster Bennett on harmonica. In a June 1968 interview, Green mentioned that he would not be only singing his own songs on the band's forthcoming album. A few months later, Green told Nick Logan in an interview with NME that the album would bear a greater resemblance to their live shows than their self-titled album. He said that his harmonica playing would be less prominent on Mr. Wonderful in comparison to the band's debut album and also mentioned that several other musicians, including Perfect and Stan Webb, would appear on his songs. On Mr Wonderful, four of the songs, "Dust My Broom", "Doctor Brown", "Need Your Love Tonight" and "Coming Home", all begin with an identical Elmore James riff. Spencer conducted an interview after the release of Mr Wonderful where he explained his creative output on the album, saying "At the time we did the Mr Wonderful album, there was a lot of Elmore James, but I wanted the chance to clear it all out of my system on record, which I have, almost." He then expressed interest in pivoting toward novelty music for future
```

### Album 5, chunk 3

```text
releases. Certain songs on Mr. Wonderful, including "Stop Messin' Round", "Lazy Poker Blues", and "Love That Burns", were performed live with members of the band Chicken Shack prior to the album's release. John Peel wrote some passages in the album's liner notes, which included commentary about the band members. The band originally wanted the album to be titled A Good Length, which would have featured an "obvious phallic symbol" on the album's front cover according to Fleetwood, although this idea was rejected as the label thought it would be too obscene. Udder Sucker was the next proposed title, and drummer Mick Fleetwood travelled to his godmother's farm to take a photo underneath a cow for the cover art, but the record label also turned this idea down. Bob Brunning, who was the original bassist of Fleetwood Mac, said that he suggested the name Mr. Wonderful while socialising with Green at a restaurant. He mentioned that they were "mimicking and satirising television talk-show hosts' tendencies to eulogise their guests by announcing them as 'the truly wonderful', etc. [Green] liked the title and it stuck". With the exception of a hat and some fig leaves, Fleetwood posed naked on the cover of Mr. Wonderful. The foldable album cover, which was photographed by Terence Ibbott, revealed Fleetwood's full body, which showed him holding a doll and a toy dog while wearing a loincloth made out of branches. Vernon mentioned that Ibbott "would come up with the most daft ideas, some of which were
```

### Album 5, chunk 4

```text
just vulgar to the point of being irresponsible and unusable". He also called Ibbott's work with the album cover "extraordinary". Compared to the huge success of the band's first album, Fleetwood Mac, the follow-up received mixed critical reviews. Allen Evans of New Musical Express noted the album's "deep, exciting blues sounds" and thought that the vocals of Green and Spencer had a "smack of the Deep South" on certain tracks. Writing for Record Mirror, Derek Boltwood thought that the songs were "all recognizably Fleetwood Mac" even with the additions of a saxophone section. He wrote that the song "Lazy Poker Blues" "isn't as lazy as the title suggests" and described "Need Your Love Tonight" as "psychedelic-Hawaiian blues". Melody Maker dismissed the album as "unadventurous" that paled in comparison to the work of band's contemporaries such as Ten Years After and Cream. In a retrospective review, Richie Unterberger wrote in AllMusic that the album as "a disappointment". He believed that "the limits of Jeremy Spencer's potential for creative contribution were badly exposed" and felt that Green's material failed to match his other material with Fleetwood Mac. Mojo characterised the album as a "misfire" and felt that the album lacked "the extraordinary spark that would soon ignite stand-alone singles 'Albatross' and 'Man of the World'". Tom Pinnock of Uncut described the album as "lacking in inspiration" and "old-fashioned...having more to do with the canny industry wiles of the mid-'60s than the brave new world of expansive music, expensive recordings and progressive blues". Peter Green – vocals, guitar Jeremy Spencer – vocals, slide guitar, piano John McVie – bass guitar Mick Fleetwood – drums Christine Perfect – piano Duster Bennett – harmonica Steve Gregory – alto saxophone Dave Howard – alto saxophone Johnny Almond – tenor saxophone Roland Vaughan – tenor saxophone
```

## Album 6: Invictus (Means) Unconquered — David Allan Coe

- **album_id:** `25c9ae27-2d1d-4001-91f9-666093167ce5`
- **Tags (identification only):** country, alternative, comedy, progressive country
- **Chunks:** 3 (688 words)

### Album 6, chunk 1

```text
Invictus (Means) Unconquered is an album released by country musician David Allan Coe. It was released in 1981 on Columbia. With its radio-friendly sound and guest duets, Coe's previous album I've Got Something to Say was an attempt to reach a wider country audience, and this process is continued on Invictus (Means) Unconquered, with producer Billy Sherrill couching the songs in tasteful instrumentation that put the spotlight squarely on Coe's voice. In his AllMusic review of the album, Thom Jurek calls the LP "arguably the finest album of his career" and singles out Coe's vocals for particular praise: True to form, Coe has always been underrated as a singer, and nowhere is this more evident than on Invictus. His co-write with Guy and Susanna Clark on "Ain't It Funny How Love'll Do Ya" is one of the most convincing vocal performances Coe ever recorded, ranking with "Mona Lisa Lost Her Smile" and "Would You Lay with Me (In a Field of Stone)”…The conviction in his voice is so present, it almost cracks, but he never quite allows himself to lose control. These are the words of a man who has stared into the face of broken love's void and lived to tell about it. Invitus is also noteworthy in that Coe only had a hand in writing just four of its ten songs, although considering the songwriter had produced ten albums of nearly all original material for Columbia in seven years, a creative dry spell was understandable. "A Boy Named
```

### Album 6, chunk 2

```text
Sue" songwriter Shel Silverstein contributes three songs, including "Someplace to Come When It Rains", which gets a sensitive reading from Coe, and the parting-of-the-ways tune "If You Ever Think of Me", which the pair composed together. They also collaborated with Karen Brooks on the lustful “The Best Game in Town,” and this song, along with the hopeful “As Far as This Feeling Will Take Us,” is sung by Coe and Brooks as duets in the classic George Jones-Tammy Wynette tradition. Coe wrote "Ain't It Funny the Way Love Can Do Ya" with songwriting couple Guy and Susanna Clark, and wrote the John Dillinger-inspired outlaw anthem “I Love Robbing Banks" with Guy Clark. Whether prompted by commercial aspirations or not, the covers that Coe and Sherrill chose to fill out the album were inspired. The opener, "Rose Knows", is the classic cheating tale filled with the paranoia of a man dreading that his wife is suspicious of his trysts, while the Bobby David-Ray Kennedy tune "The Purple Heart", which Sherrill infuses with the classic "Ray Price shuffle", uses war as a metaphor to show the bitterness and heartbreak of a love gone sour. ("You put me out of action so many times before and left me on the battlefield to bleed...") Coe also covers the outlaw classic "London Homesick Blues", popularised by Jerry Jeff Walker, and, more curiously, the Tammy Wynette classic "Stand by Your Man". Coe plays it straight on the song, which was written by Wynette and Sherrill, and
```

### Album 6, chunk 3

```text
is heartfelt and moving, taking on a new meaning in a man's voice - more of a plea than a declaration. (This would be taken to the extreme the following year when the heavy metal band Motörhead and Wendy O. Williams would also cover the song.) Released as the album's single, Coe's "Stand by Your Man" reached No. 88 on the charts. Like many Coe albums of this era, Invictus (Means) Unconquered was a mediocre commercial success, making it to No. 67 on the country albums chart. AllMusic wrote: "From top to bottom, Invictus Means Unconquered towers above most country records not only of the era, but of all time. It's a quintessential example of everything country music can achieve when it is honest, true, and from the center of a broken heart." David Allan Coe, Karen Brooks – vocals The Nashville Edition – background vocals Billy Sanford, Jimmy Capps, Tommy Allsup, Phil Baugh – guitar Pete Drake, Dale Seigfreid – steel guitar Henry Strzelecki, Joe Osborn – bass Kenny Malone, Jerry Carrigan – drums Hargus "Pig" Robbins – piano Farrell Morris – percussion Billy Sherrill – producer
```

## Album 7: Pure and Simple — Joan Jett and the Blackhearts

- **album_id:** `a0c4ea19-b8da-4f88-9f2a-4eea9b742693`
- **Tags (identification only):** rock, album rock, hard rock, pop/rock, rock and roll
- **Chunks:** 2 (521 words)

### Album 7, chunk 1

```text
Pure and Simple is the ninth studio album by American rock singer Joan Jett and the seventh to feature her backing band the Blackhearts. It was released on June 14, 1994 by Blackheart and Warner Bros. Records. The album includes several tracks co-written with Kathleen Hanna of Bikini Kill, including "Go Home", a response to the murder of Mia Zapata, lead vocalist and lyricist of the punk rock band the Gits. Pure and Simple was the first album to feature a new line up of the Blackhearts' members since the departure of longtime guitarist Ricky Byrd and bassist Kasim Sulton after the release of Jett's previous studio album, Notorious (1991). This new line up consisted of bassist Kenny Aaronson and lead guitarist Tony Rey. Pure and Simple would be Joan Jett and the Blackhearts' last studio album until 2006's Sinner. In 1995, both Aaronson and Rey went on to other projects. Aaronson would eventually become a member of the reunited New York Dolls – coincidentally taking over for bassist Sami Yaffa, his replacement in the Blackhearts and Rey became the musical director for Enrique Iglesias and Rihanna. The CD and other versions feature collaborations with performers from riot grrrl and riot grrrl-associated bands. On all editions, songs "Go Home", "Spinster", "Activity Girl", and "You Got a Problem" were written with Kathleen Hanna (Bikini Kill, the Julie Ruin, Le Tigre); on the vinyl release "Here to Stay" was written with Kat Bjelland (Babes in Toyland); on the Japanese edition "Hostility" was
```

### Album 7, chunk 2

```text
written with Donita Sparks (L7). "World of Denial" was also added to the Japanese pressings. The Japanese cover differs from the regular cover. "Get Off the Cross" was also recorded during these sessions. Concurrently released in the U.S. on LP, CD, and cassette, all versions varying slightly. The record album came with a hype sticker that read "All Rock. No Ballads", and omits both "As I Am" and "Brighter Day". A few seconds of "Here to Stay" are also heard on the cassette at the very end of side one before fading out. Jett independently put out "Spinster" as a 7-inch blue vinyl single in the U.S. with a picture sleeve. The B-sides were "Go Home" and "Hostility". The track "World of Denial" was eventually released in the U.S. on Jett's compilation album Fit to Be Tied (1997). Joan Jett – guitars, lead vocals, producer on "Hostility" Tony Rey – lead guitars Kenny Aaronson – bass Thommy Price – drums Ricky Byrd – guitar John Marshall – guitar Billy Karren – guitar Blake Brocksmith – harmonica on "Go Home" and "As I Am" Mike Howe – vocals Kathleen Hanna – vocals Chuck Kentis – keyboards Arno Hecht – saxophone Kenny Laguna – producer on all tracks Thom Panunzio – producer on tracks 1, 2, 4, 7, 9, 10 and bonus tracks, engineer, mixing Ed Stasium – producer on tracks 1 and 8 Jim Vallance – producer on tracks 2 and 4 Desmond Child – producer on tracks 6, 11 and 12 John Aiosa – engineer, digital editing Lance Clark – digital editing Bob Ludwig – mastering at Gateway Studios, Portland, Maine
```

## Album 8: Red Clay — Freddie Hubbard

- **album_id:** `f8a6c2c1-e6aa-40dc-94ba-f980972e07b5`
- **Tags (identification only):** jazz, soul jazz, hard bop, post bop
- **Chunks:** 1 (269 words)

### Album 8, chunk 1

```text
Red Clay is an album recorded in 1970 by jazz trumpeter Freddie Hubbard. It was his first album on Creed Taylor's CTI label and marked a shift toward the soul-jazz fusion sounds that would dominate his recordings in the later part of the decade. It entered at number 20 on Billboard’s Top 20 Best Selling Jazz LPs, on June 20, 1970. Bill Milkowski of JazzTimes commented: "...Red Clay, an album that would not only define Hubbard's direction over the next decade while setting the template for all future CTI recordings, but would also have a dramatic impact on a generation of trumpet players coming up in the ’70s. ’Red Clay’ would become Hubbard's signature tune throughout his career." Thom Jurek of AllMusic stated: "This may be Freddie Hubbard's finest moment as a leader, in that it embodies and utilizes all of his strengths as a composer, soloist, and frontman. On Red Clay, Hubbard combines hard bop's glorious blues-out past with the soulful innovations of mainstream jazz in the 1960s, and reads them through the chunky groove innovations of '70s jazz fusion... This is a classic, hands down." Tom Moon, in 1,000 Recordings to Hear Before You Die, wrote that "Red Clay is one of those records that mucks up the neat evolution narrative of jazz." Freddie Hubbard – trumpet Joe Henderson – tenor saxophone, flute (tracks 1–5) Herbie Hancock – electric piano, Hammond organ (tracks 1–5) Ron Carter – bass Lenny White – drums (tracks 1–5) Stanley Turrentine – tenor saxophone Johnny "Hammond" Smith – electric piano George Benson – guitar Billy Cobham – drums Airto Moreira – percussion
```

## Album 9: Your Little Secret — Melissa Etheridge

- **album_id:** `921cd95e-999b-413c-bf3a-dea0e9f6bc48`
- **Tags (identification only):** rock, adult alternative pop/rock, alternative rock, alternative/indie rock, blues rock, heartland rock, pop, pop rock
- **Chunks:** 2 (376 words)

### Album 9, chunk 1

```text
Your Little Secret is the fifth studio album by American singer-songwriter Melissa Etheridge, released by Island Records on November 14, 1995. It is her highest-charting album on the Billboard 200, where it peaked at No. 6. The album also contained three singles, "Your Little Secret", "I Want to Come Over", and "Nowhere to Go". "I Want to Come Over" went on to reach No. 22 on the Billboard Hot 100, and "Nowhere to Go" peaked at No. 40. As of 2010, the album has sold 1,348,000 copies in the United States alone, according to Nielsen SoundScan. Billboard praised the record, calling it a "superbly well-crafted album. Armed with her sharpest material to date, the tightest band with which she's ever recorded, and an in-your-face sound, Etheridge rocks even more passionately than on her previous smash, Yes I Am...Under pressure to follow up a multiplatinum, milestone album, Etheridge has delivered the goods and then some. A new plateau for an artist who has set the pace for female rockers of her generation." In their review, Cashbox noted that "on this, her fifth album, Etheridge continues to demonstrate the consistency that has made her a superstar. The disc kicks in with the grinding rocker/title track, then settles into a groove of anthem-like rockers, such as “I Really Like You,” “This War Is Over” and the record’s best track, the engaging “An Unusual Kiss.” Her ballad skills are underrated, but as “Nowhere To Go” and the opening half of “Shriner’s Park” prove, she
```

### Album 9, chunk 2

```text
is just as talented in that medium. The bottom line is Etheridge is a great singer with good songs, making every album a project worth embracing." Allmusic were more mixed in their review, stating that "Etheridge's challenge would be to grow as a writer, now that incessant touring and a string of good-but-not-great albums finally had brought her to the platinum threshold. Your Little Secret left the question about such growth open." Melissa Etheridge – acoustic guitar, electric guitar, keyboards, vocals John Shanks – acoustic guitar, electric guitar, keyboards Mark Browne – bass guitar Kenny Aronoff, Dave Beyer – drums, percussion Producers: Melissa Etheridge, Hugh Padgham Engineers: Greg Goldman, Hugh Padgham Assistant engineer: John Aguto Mastering: Bob Ludwig Post production: Cheryl Engels Art direction: Judy Troilo
```

## Album 10: Artificial Soldier — Front Line Assembly

- **album_id:** `99b440a8-0c24-4b11-87aa-43db3900b965`
- **Tags (identification only):** electronic, ebm, industrial, bill leeb, breakbeat, drum and bass, electro industrial
- **Chunks:** 3 (655 words)

### Album 10, chunk 1

```text
Artificial Soldier is the thirteenth full-length studio album by Vancouver industrial band Front Line Assembly, released in 2006. This is the first Front Line Assembly album to feature new member Jeremy Inkel. In 2016, Canadian label Artoffact reissued the album on vinyl. The tour in North America in support of Artificial Soldier started before the album was released. The North American leg was originally scheduled for June and July 2006. However, due to difficulties with the company that supplied the tour bus the band was forced to cancel parts of the tour. They could only play about half of their planned shows in the United States, dates in New York and Canada were cancelled. At the show in Philadelphia the band announced that this would be their last show of the tour. Tour drummer Adrian White made a statement on the Side-Line forum: "Digger international who handled the bus rental has fucked us. We were lied to since we were told we had a bus until July 6th, which was bullshit. They had planned to leave us in Philly without a bus to do the rest of the tour. They, the driver and tour manager filled us in on the scam last night just before our Philly show leaving us with a couple hours to find transportation for 11 people and all of our equipment." In an interview with Side-Line right after the shortened North American tour vocalist Bill Leeb said that the band intended to make up for the
```

### Album 10, chunk 2

```text
cancelled dates after they would return from the European leg. Asked what conclusions he had drawn from this experience, Leeb responded: "I will never get on a bus without seeing a written contract stating that I have the bus from point A to B. Let's just say I have never been fucked by a bus company before." Supporting band Stromkern blamed the booking agency for the problems, suggesting "the booking agency [...] pocketed the deposits and has vanished off the face of the earth." In August and September Front Line Assembly continued their tour in Europe. While electronic music band and Dependent label mates Stromkern opened for Front Line Assembly on both legs, DJ? Acucrack was support act only for the North American leg and Rhys Fulber's project Conjure One was guest on a few US shows. Reviews for Artificial Soldier were mixed. David Jeffries of Allmusic called the album "ferocious" and said, "Artificial Soldier is a return to form monster of an album that will pound the band back into the electro-industrial lover's heart." John Carlsson of Release Music Magazine called the album "a brutal and heavy affair" but said, "Their often marvelous knack for writing great hooks and choruses ... seems to have gone missing." He also stated, "There is also very little variation to be found," and finished by declaring "if you ... want your [Bill] Leeb furious and angry, this is right up your alley." Barcode Magazine's critic expressed his discontent over much of the album
```

### Album 10, chunk 3

```text
and wrote, "it's 23 minutes into the album before anything genuinely impressive happens", thereby referring to the track "Buried Alive". "With Artificial Soldier it's obvious that they've fallen into their own trap", was the magazine's verdict: "This is not only a parody of the genre but of Front Line Assembly itself, and I find that disappointing for a band that was once so creative and forward thinking." Bill Leeb – vocals (1–7, 10), keyboard (4, 5, 8–10) Rhys Fulber – keyboard (1, 2, 6, 8, 10), additional programming (3), additional keyboard (3, 7) Chris Peterson – programming (1–9), keyboard (1–9), additional programming (10) Jeremy Inkel – programming (3, 5, 7, 9), keyboard (3, 5, 7, 9), additional programming (1, 4, 8), additional keyboard (1, 4, 8) Jared Slingerland – guitar (4) Adrian White – guitar (6) Jean-Luc De Meyer – vocals (8) Eskil Simonsson – vocals (9), additional keyboard (9) Greg Reely – engineering, mixing
```

## Album 11: The Brand New Heavies — The Brand New Heavies

- **album_id:** `d423e445-06fb-4b12-8714-beb38b0f01ea`
- **Tags (identification only):** acid jazz, jazz funk, electronic, funk, hip hop
- **Chunks:** 3 (768 words)

### Album 11, chunk 1

```text
The Brand New Heavies is the debut album by British acid jazz group The Brand New Heavies. The album was originally released on 16 April 1990 on Acid Jazz Records. The album was reissued in 1991, featuring vocals by new group member N'Dea Davenport. Following the reissue, the album became more successful than its original release, debuting on the UK Albums Chart at number twenty-five and earning a silver-certification by the British Phonographic Industry (BPI). The album spawned six singles: "People Get Ready", "Dream Come True", "Never Stop", "Dream Come True '92", "Don't Let It Go to Your Head", and "Stay this Way '92"; the latter three of which peaked in the Top 40 on the UK Singles Chart. On 16 April 1990, The Brand New Heavies was released exclusively in the United Kingdom on Acid Jazz Records. Shortly after the release of the album, the group's lead vocalist Jaye Ella Ruth departed from the group and was replaced with American singer N'Dea Davenport. In March 1991, the group reissued the album in North America on Delicious Vinyl Records. The North American version featured an additional song titled "Never Stop". To promote the album, The Brand New Heavies appeared on various television shows from 1991 until late 1992. On 19 October 1991, The Brand New Heavies performed "Stay this Way" on American musical variety television show Soul Train. On November 9, 1991, the group performed "Never Stop" and "Stay this Way" on Showtime at the Apollo. On 20 February 1992,
```

### Album 11, chunk 2

```text
the group performed "Dream Come True" on British music chart television programme Top of the Pops. On 2 March 1992, The Brand New Heavies was released internationally on Full Frequency Range Recordings (FFRR). The international version omitted the song "Shake Down" and included two new songs: "Got to Give" and a cover version of "Don't Let It Go to Your Head". An expanded edition of the album was released on BGP Records in 2007. In 1989, The Brand New Heavies released the single "People Get Ready", which failed to chart. "Dream Come True" was released as the album's second single on 13 August 1990. The song peaked at number sixty-three on the US Hot R&B Singles chart. "Never Stop" was released as the first international single and third overall single from The Brand New Heavies on 23 September 1991. A commercial success, it peaked at number forty-three on the UK Singles Chart. The song became their first crossover hit, peaking at number fifty-four on the US Billboard Hot 100 and number four on the US Hot R&B Singles chart. The accompanying music video for "Never Stop" was directed by Douglas Gayeton. "Dream Come True" was reissued with vocals by N'Dea Davenport and released as the second international single and fourth overall single on 3 February 1992. The song peaked at number twenty-four on the UK Singles Chart and number forty-two on the US Hot R&B Singles. "Don't Let It Go to Your Head", a cover version of Jean Carn's song,
```

### Album 11, chunk 3

```text
was released as the fifth single on 20 July 1992, peaking at number twenty-four on the UK Singles Chart. "Stay this Way" was released as the sixth and final single from the album on 30 November 1992. The song peaked at number forty on the UK Singles Chart and number nineteen on the US Hot R&B Singles. AllMusic's Alex Henderson gave The Brand New Heavies a favourable review. He praised the album for its use of live instrumentation instead of synth instruments. Henderson commented, "Real horns -- not synthesizers made to sound like horns -- enrich those gems as well as the sweaty vocal funk of "People Get Ready" and "Put the Funk Back in It" and the jazz-influenced instrumental "BNH." Henderson also complimented group member N'Dea Davenport for her performance on "Stay this Way" and "Dream Come True". Marisa Fox of Entertainment Weekly rated the album two and a half stars out of four. The Brand New Heavies debuted at number twenty-five on the UK Albums Chart on 14 March 1992. The album spent eighteen weeks on the chart, gradually falling back to number fifty-eight before dropping off the chart. On 1 January 1993, the album received a silver-certification by the British Phonographic Industry (BPI). In the United States, the album peaked at number seventeen on the US Billboard Top R&B Albums chart. Simon Bartholomew – guitar, vocals N'Dea Davenport (1991) – vocals Lascelles Gordon (1991) – percussion, guitar Jan Kincaid – drums, keyboards Jaye Ella Ruth (1990) – vocals Andrew Levy – bass, keyboards, writer & producer Jim Wellman (1991) – tenor saxophone, soprano saxophone, keyboards
```

## Album 12: Emergency — Kool & the Gang

- **album_id:** `7bafe23e-9a89-40a2-be8a-dec1a73c2078`
- **Tags (identification only):** contemporary r and b, disco, electronic, funk, pop, pop soul, synth funk
- **Chunks:** 1 (249 words)

### Album 12, chunk 1

```text
Emergency is the sixteenth studio album by the American band Kool & the Gang, released in 1984. It became the group's biggest selling album, earning Double Platinum status in America, Platinum in Canada, and Silver in the UK. The album produced four US top 20 hit singles including "Fresh" (US No. 9); "Misled" (US No. 10); the title track "Emergency" (US No. 18); and the album's biggest hit, the million-selling "Cherish" (US No. 2). "Fresh", "Misled", and "Cherish" also cracked the top 40 in the UK reaching No. 11, No. 28, and No. 4, respectively, while "Emergency" reached No. 50. James "J.T." Taylor – lead vocals, backing vocals Curtis "Fitz" Williams – keyboards, Yamaha DX1, Yamaha DX7, Oberheim OB-Xa, Oberheim OB-8, Oberheim Xpander, Roland Juno-60 Ronald Bell – Oberheim OB-8, tenor saxophone, backing vocals Claydes Charles Smith – guitars Robert "Kool" Bell – bass guitar George "Funky" Brown – drums Dennis "Dee Tee" Thomas – alto saxophone Clifford Adams – trombone, additional backing vocals (1) Robert "Spike" Mickens – trumpet Michael Ray – trumpet Rick Iantosca – guitars (1–3, 5, 6) Kendal Stubbs – bass guitar (3), backing vocals Jimmy Maelen – percussion Starleana Young – backing vocals Kool & the Gang – producers Ronald Bell – producer, mixing Jim Bonnefond – producer, engineer, mixing Kendal Stubbs – engineer, mixing Gabe Vigorito – mixing, album coordinator Jose Rodriguez – mastering at Sterling Sound (New York, NY) Lumel/Whiteman Graphics Design – graphics Lazaro Arias – stylist Roz Burns – make-up
```

## Album 13: Life’s Not Out to Get You — Neck Deep

- **album_id:** `43d11250-05a5-4f69-a21a-5bd8cce884d7`
- **Tags (identification only):** pop punk, anthemic, bittersweet, breakup, energetic, male vocalist, melodic, optimistic
- **Chunks:** 7 (1724 words)

### Album 13, chunk 1

```text
Life's Not out to Get You is the second studio album by Welsh pop punk band Neck Deep. Following the success of their debut album, Wishful Thinking (2014), the majority of the band members quit their day jobs and vocalist Ben Barlow dropped out of university. Working with Jeremy McKinnon, Andrew Wade and Tom Denney, the band recorded their second album between December 2014 and January 2015. Following recording, the band immediately went on tour. Life's Not out to Get You was preceded by two singles: "Can't Kick Up the Roots" in May 2015 and "Gold Steps" in July. "Can't Kick Up the Roots" charted at number 16 in the UK on the Rock & Metal Singles chart. In early August, "Threat Level Midnight" was made available for streaming. It was released by Hopeless on 14 August. The album charted at number 8 in the UK, reached the top 20 in the US, and reached the top 40 in Ireland and Australia. It is the band’s final album to feature their full original lineup. Nine days after the release of the album, guitarist Lloyd Roberts left the band due to allegations of sexual misconduct, which were dropped soon after. Neck Deep and their tour manager went on a holiday to Florida. The group ended up playing two shows that were "crazy and sold out and packed", according to bassist Fil Thorpe-Evans. Videos of the shows ended up online, which were seen by Hopeless. Hopeless got in contact with the band's
```

### Album 13, chunk 2

```text
manager who put the label in contact with the band. The band signed to Hopeless in August 2013. Being signed to the label was "a dream come true" for the band. The band released their debut album, Wishful Thinking, in January 2014. The success of the album resulted in the band moved from a "fun, part-time [entity]", as Barlow called it, to a full-time thing. Also due to the success, Thorpe-Evans, guitarists Matt West and Lloyd Roberts quitting their jobs, drummer Dani Washington turning down a place at the Academy of Contemporary Music and Barlow dropping out of university. In October and November 2014 the band supported Real Friends on their tour of the US. Neck Deep began writing new material as early as December 2013 prior to the release of Wishful Thinking. Vocalist Ben Barlow said Neck Deep wanted their second album to sound "bigger and better" than Wishful Thinking. Barlow claimed that the new album is what Wishful Thinking "should've been". While reassuring that it sounds like the band, he stated it was more "polished and rounded." Barlow said that the album "has the potential to cement a legacy for this band and to establish us as one of the best pop-punk bands in the world." All of the songs on the album were credited to Neck Deep with Seb Barlow, Andrew Wade, Tom Denney and Jeremy McKinnon. The intro to "Citizens of Earth" features Thorpe-Evans breaking wind. "Can't Kick Up the Roots" is about Barlow's hometown, Wrexham,
```

### Album 13, chunk 3

```text
North Wales. Barlow mentioned that on one hand it is about how Wrexham "sucks" while on the other hand that is "what makes it ours." The "roots" part of name refers to the band's love of their hometown despite the flaws. The band wanted "Can't Kick Up the Roots" to be "a summer song" that "catch[es] people's ears straight away." "Kali Ma" is about a specific scene in the film Indiana Jones and the Temple of Doom (1984). Neck Deep demoed material on their tour bus while on the 2014 edition of Warped Tour. The band decided to move "out of our comfort zone" and worked "with someone we've always looked up to", Jeremy McKinnon of A Day to Remember. McKinnon's excitement stood out to the band: "not only is he someone who knows what they're doing" but looking forward to the album as much as the band were. McKinnon was working with Andrew Wade on The Ghost Inside's Dear Youth (2014) when Tom Denney had dropped by the studio. McKinnon had overheard Wade and Denney talking about having a meeting with Neck Deep to discuss their next album. The trio had met up with bassist Fil Thorpe-Evans and "we all hit it off", according to McKinnon. Eventually, Neck Deep contacted the trio to tell them that they were chosen. On 1 December 2014 it was announced the band had started recording, and on 21 January 2015 it was announced the band had finished recording. The group had entered the
```

### Album 13, chunk 4

```text
studio with 20 songs; they ended up with 12 songs on the finished version of the album. Life's Not Out to Get You was produced by McKinnon and Wade. Wade also helped with recording and mixing, while McKinnon provided guest vocals on "Kali Ma". The album was mastered by Alan Douches. Shortly after the band finished recording they went on tour in January and February. The artwork was created by Ricardo Cavolo. Barlow wanted the cover art to have a "really hand-drawn feel" to it and be "totally unlike any other artwork that's going on in the scene." The Devil depicted in the bottom-left handed cover is a comment on how a person should be making sure to not let the Devil on your shoulder win. Some of the items featured on the cover have been coincidences in relation to the lyrics as Cavolo made the art without hearing the album. For example, one of the songs on the album is titled "Serpents" and the art features snakes. Barlow and Cavolo created a comic book based on the artwork that includes lyrics from the album turned into the comic's story. The comic book was made available through pre-orders. The story features a character called June "who faces all these obstacles throughout his life". June's goal is to reach a house on a hill in spite of all the problems that might arise. Barlow claims that this is a metaphor "for the idea of always persevering and trying your best", a
```

### Album 13, chunk 5

```text
concept which is featured in the album. The album comes in a cardboard gatefold sleeve. On 5 May 2015 Neck Deep announced their second album, Life's Not out to Get You, and revealed the track listing and artwork. On 11 May, "Can't Kick Up the Roots" was premiered on BBC Radio 1's Rock Show programme. A day later, a music video was released for the song, which was directed by Daniel Broadley. The music video was filmed back in March. On the same day, the song was released as a single. The band played on the 2015 edition of Warped Tour. "Gold Steps" was premiered on BBC Radio 1 on 19 July, and was released as a single a day later. A music video for the song was released on 21 July. It was directed by Kyle Thrash. On 10 August, "Threat Level Midnight" was made available for streaming. The album was released on 14 August through Hopeless. The HMV and Target editions of the album included three bonus tracks: a full band version of "December", and acoustic versions of "Can't Kick Up the Roots" and "Lime St.". A day later, the album was made available for streaming. Following allegations of sexual misconduct towards a minor; on 23 August, Roberts parted ways with the band, not wanting the allegations to tarnish the band's reputation and also to focus on family life. The band supported All Time Low and Sleeping with Sirens in October and November on their Back to the
```

### Album 13, chunk 6

```text
Future Hearts Tour. The band supported Bring Me the Horizon in the UK in November. On 18 December, it was announced that Sam Bowden joined the band as Roberts' replacement. On 1 January 2016, a music video was released for "Smooth Seas Don't Make Good Sailors", which was filmed throughout 2015. On 27 January, a music video was released for "Kali Ma", directed by Elliott Ingham. The band went on a co-headlining UK tour with State Champs in February, with support from Creeper and Light Years. This would be followed by a tour of the US with support from Knuckle Puck and Like Pacific. On 10 March, a music video was released for "Serpents", directed by Miguel Barbosa. On 18 March 2016, an EP was released featuring "Serpents" and "Can't Kick Up the Roots" as well as remixes of both songs by Mark Hoppus of Blink-182. The band toured the UK again in April with support from Creeper and WSTR. On 17 July, two new versions of "December" were released as a single – one featuring Hoppus and the other featuring Chris Carrabba of Dashboard Confessional. Rock Sound editor Ryan Bird wrote that Life's Not out to Get You is the kind of "pop-punk album you just don't hear any more." Bird compared the music to early 2000s "through and through", and some of the songs to the likes of Sum 41 and New Found Glory. He noted that this sets the band apart from their peers. "Can't Kick Up
```

### Album 13, chunk 7

```text
the Roots", "Lime St." or "Kali Ma" could be classed as the "song of the summer". Bird mentioned Barlow's vocals have "never been better, sounding stronger, smoother and more controlled." The album was ranked at number 10 in Alternative Press's "10 Essential Records of 2015" list. Matt Crane of Alternative Press remarked "Ear-candy choruses [...] and touching acoustic ballads [...] make it rain pizza as far as the eye can see." The album was included at number 3 on Rock Sound's top 50 releases of 2015 list. Life's Not out to Get You was nominated for Album Of The Year at the 2016 Alternative Press Music Awards and for Best Album at the 2016 Kerrang! Awards. "Can't Kick Up the Roots" charted in the UK at number 9 on the Independent Singles Breakers chart, number 16 on the Rock & Metal Singles chart, and number 45 on the Independent Singles chart. Life's Not out to Get You sold 26,251 copies, charting at number 8 in the UK and number 17 in the US. It also charted at number 15 in Ireland, number 28 in Australia and number 87 in Belgium. "Can't Kick Up the Roots" was nominated for "Independent Track of the Year" at the Association of Independent Music awards. As of July 2020 the album has sold over 60,000 copies in the UK.
```

## Album 14: Végétal — Émilie Simon

- **album_id:** `1e1da73b-a3a0-41f0-ba19-edf2b3fe3ba3`
- **Tags (identification only):** france, pop, 2006, arranger, electronic, electronica, experimental, francophone
- **Chunks:** 1 (228 words)

### Album 14, chunk 1

```text
Végétal is the second studio album by singer-songwriter Émilie Simon. Overall, it is her third album, the soundtrack to the French version of March of the Penguins included. The album has a floral theme running through it. All the lyrics relate to plants and there are also sounds taken from actual plants. The CD can be used in Émilie Simon's official website to access exclusive content such as bonus tracks, remixes, and a music video for "Fleur De Saison". A special edition of the album was released in December 2006, featuring bonus tracks, remixes of "Fleur De Saison" and Opium, an exclusive short film on the making of the album and the video clip for "Fleur De Saison" on a bonus CD. So far, 5 editions of Végétal exists, each one different from each other through the inclusion of extras and bonuses. The release was accompanied by the single "Fleur de Saison", which was released on 6 February 2006. The title means "Seasonal Flower" in English. It is from her second studio album Végétal. The music video for the song was directed by nObrain, that also directed the "Flowers" music video, and produced by COSA. In 2006, Végétal sold a total of 77,376 copies in France. She ranked 84th overall in the year-end French sales chart and 34th in the year-end download chart with 2,306 full album downloads.
```

## Album 15: Listen Without Prejudice, Volume 1 — George Michael

- **album_id:** `9eb3410b-db57-426c-a907-d766e8dc5269`
- **Tags (identification only):** adult contemporary, pop, downtempo, dance pop, electronic, rock, synth pop, urban
- **Chunks:** 7 (1692 words)

### Album 15, chunk 1

```text
Listen Without Prejudice Vol. 1 is the second solo studio album by the English singer-songwriter George Michael, released on 3 September 1990 by Epic Records in the UK and on 11 September by Columbia Records in the US. The album was Michael's final album of all-new material on Columbia until 2004's Patience. Listen Without Prejudice was a stark departure from Michael's previous album, 1987's Faith, with largely acoustic instrumentation and a sombre intensity in many of the lyrics and melodies. While the album topped the UK Albums Chart, disappointing sales in the United States led to Michael's legal battle against Sony Music, in which he accused the corporation of not fully supporting him as an artist. Listen Without Prejudice was reissued across a number of formats on 20 October 2017 and again topped the UK Albums Chart, 27 years after it first reached number one on the chart. After the massive success of George Michael's 1987 album Faith, expectations for his follow-up album were also high. Michael wanted to be taken more seriously as a songwriter, which resulted in a more thoughtful, often moody recording. Like Faith, each track was produced and arranged by Michael himself. The recording sessions commenced in July 1989 at producer Chris Porter's house, near Guildford, before being moved to Metropolis Studios in Chiswick, London. According to Tony Parsons, Listen Without Prejudice was originally conceived as a double album, with "around sixteen strong originals" written by Michael. By late September 1989, these plans were scrapped in
```

### Album 15, chunk 2

```text
favor of two separate albums, both scheduled for release in 1990. Listen Without Prejudice Vol. 1 was released in September 1990. The album sold approximately eight million copies worldwide. The album entered the Billboard 200 at number 22 and peaked at number two. The album spent the rest of 1990 in the top ten, with a total of 42 weeks on the entire chart. In the United Kingdom, the album was a huge success, eclipsing sales of Faith. Listen Without Prejudice debuted on the UK Albums Chart at number one. It stayed at number two for the following two weeks. It spent 34 consecutive weeks in the top 20, and jumped from number 13 to number three in its 24th week. It spent a total of 88 weeks on the chart, and was certified quadruple platinum by the British Phonographic Industry on 2 January 1992. The follow-up album Listen Without Prejudice Vol. 2 (ostensibly scheduled to follow in June 1991) was scrapped for reasons known only to Michael and his record company. Three of the tracks intended for that album appear on the 1992 charity compilation Red Hot + Dance, while a fourth ("Crazy Man Dance") turned up on the B-side of that compilation's first single, "Too Funky". The first single from Listen Without Prejudice Vol. 1, "Praying for Time", was released in August 1990, reaching number six on the UK Singles Chart and number one on the US Billboard Hot 100—Michael's final US number one as a solo artist.
```

### Album 15, chunk 3

```text
The second single (third in the US), "Waiting for That Day", was issued over a month after the album's release. Owing to a borrowed lyric from the Rolling Stones' hit "You Can't Always Get What You Want", co-writer credits were given to Mick Jagger and Keith Richards. It reached number 23 in the UK, and, after being released there in spring 1991, number 27 in the US. In the US, "Mother's Pride", the "Waiting for That Day" B-side, reached number 46; given its subject matter, it received considerable airplay on American radio during the Gulf War. The album's third single (second in the US), "Freedom! '90", became one of Michael's signature songs. It was a great success in the US, where it reached number eight and earned a gold certification from the Recording Industry Association of America. It charted lower in Michael's homeland, where it peaked at number 28. The fourth single, "Heal the Pain", peaked at number 31 in the UK in February 1991. The fifth single from Listen Without Prejudice, "Cowboys and Angels", entered the UK Singles Chart in March and peaked at number 45. "Soul Free" was commercially released as the sixth and final single in North America, Japan, and Australia, where it charted at number 95. Michael refused to appear in the music videos for the album's singles. Accordingly, the video for "Praying for Time" consisted of the song's lyrics projected onto a dark background, while the video for "Freedom! '90", directed by David Fincher, featured
```

### Album 15, chunk 4

```text
several supermodels lip syncing its lyrics, and the destruction by fire and explosion of several icons from Michael's recent Faith period. Listen Without Prejudice Vol. 1 was reissued on 20 October 2017 as Listen Without Prejudice / MTV Unplugged. The reissue was first announced in September 2016. The 2CD version includes the original remastered album on the first disc, and Michael's MTV Unplugged concert, recorded at 3 Mills Studios, London on 11 October 1996, on the second disc. MTV Unplugged contains performances of "I Can't Make You Love Me" and "The Strangest Thing" that are identical to those previously released as B-sides to the single "Older", and the 2017 version of "Fantasy", reworked by Nile Rodgers and released as a single in September 2017. The 3CD+DVD deluxe edition includes two more discs: a CD with B-sides, remixes and rarities, and a DVD with a documentary and music videos. Rarities on the third disc include: "If You Were My Woman" (recorded live at the Nelson Mandela 70th Birthday Tribute concert in 1988 and featured on the "Praying for Time" single), "Crazy Man Dance", and "Do You Really Want to Know" and "Happy" (from Red Hot + Dance). The original remastered album was also reissued on vinyl. Listen Without Prejudice / MTV Unplugged entered the UK Albums Chart at number one with first-week sales of 56,088 copies, 27 years after the original album first topped the chart. Listen Without Prejudice Vol. 1 received widespread acclaim reactions from music critics upon release. In
```

### Album 15, chunk 5

```text
a rave review for Q, Mat Snow commented that the album "should prove" Michael's talent "to any lingering doubters". Writing for the Chicago Tribune, Greg Kot found that Michael "makes a convincing case that he's more than just another pretty voice, another disposable pinup", particularly complimenting the album's sparse sound, which he welcomed as a contrast to the more dance-leaning music dominating pop radio. James Hunter of Rolling Stone said that Listen Without Prejudice generally "succeeds in its effort to establish Michael's seriousness and deliver him from caricature." Los Angeles Times critic Chris Willman wrote that, "some self-seriousness aside", the album "is an impressive piece of work in which Michael's rich feel for melodies and instinctively perfect production skills have finally met up with songs that have the ring of personal, not commercial, passion." Stuart Maconie opined in NME that it lacks "enough irresponsibility or hooks", but conceded that "it's hard to begrudge George his coming of age." Entertainment Weekly's Greg Sandow was less enthusiastic, finding Listen Without Prejudice less "vital" and "fun" than Faith, "and, for all its noble sentiment, entirely unchallenging". In The Village Voice, Robert Christgau dismissed it as "cocktail music" and was unmoved by Michael's reflections on fame, saying that they merely indicate that "he doesn't know as much about stardom as he thinks". Listen Without Prejudice won the award for Best British Album at the 1991 Brit Awards. Listen Without Prejudice Vol. 1 was included in the book 1001 Albums You Must Hear Before You
```

### Album 15, chunk 6

```text
Die. The album was also included in Apple Music's 100 Best Albums list at number 91. In 2003, Slant Magazine's Sal Cinquemani called the album "a starkly personal statement that effectively set the artist's professional downfall into motion", suggesting that its "overall heaviness" failed to resonate with listeners expecting uptempo material in the vein of Michael's past work; he concluded that "the fact that there was never a Vol. 2, which was rumored to be the feel-good dance record said fans were probably waiting for, makes this one seem all the more sacred." The publication also included the record on its 2003 list of 50 Essential Pop Albums. AllMusic reviewer Stephen Thomas Erlewine found the album flawed, noting that Michael downplays his gift for "effortless hooks and melodies" and that his "socially conscious lyrics tend to be heavy-handed", but concluded that its best songs "make a case for his talents as a pop craftsman." Reviewing the album's 2017 reissue, Pitchfork writer Alfred Soto situated Listen Without Prejudice in the context of the then-burgeoning HIV/AIDS pandemic: "[George Michael] understood black music as the product of a familiarity with death leavened by the banalities of earth: love, sex, comfort. Something was happening that autumn to gay artists closeted from their fans. In October [1990], Neil Tennant and Chris Lowe released Behaviour, the quietest album of the Pet Shop Boys' career. The unceasing piling up of bodies killed by HIV had made, for the moment, the bacchanal into a gauche if not repulsive
```

### Album 15, chunk 7

```text
gesture of sentimentality." According to Soto: "For those of us too young for the plague years—who can imagine, at least, a life lived instead of convulsing in agony on a hospital bed—chastising Michael for leaning on elegies and ballads in 1990 strikes me as glib. In its original form, Listen Without Prejudice Vol. 1 was the follow-up that Faith demanded; in this new incarnation, it's a miscellany unruffled by notions of coherence, an attempt to make art out of George Michael's quarrels with himself." George Michael – vocals, keyboards (1, 6, 9), acoustic guitar (4, 7, 8), keyboard bass (2, 5), bass guitar (4, 9), programming, percussion (2, 5), backing vocals, horn arrangements, production Danny Cummings – drums (5), percussion (2, 8, 9) Tony Patler – keyboards (9, 10) Ian Thomas – drums, percussion Deon Estus – bass guitar (1, 5, 6, 8), backing vocals (6) Phil Palmer – acoustic guitar, electric guitar Chris Cameron – keyboards (2, 3, 7), piano (2, 5), horn arrangements, string arrangements (5) Emily Burridge – cello Andy Hamilton – saxophone (5) Alfia Nakipbekova – cello Pete Gleadall – sequencer, programming Shirley Lewis – backing vocals (2)
```

## Album 16: Wish You Were Here — Pink Floyd

- **album_id:** `08ba43ba-41f6-45f4-816a-e10832870cd5`
- **Tags (identification only):** progressive rock, art rock, psychedelic rock, rock, concept album, longing, melancholic, progressive
- **Chunks:** 17 (4095 words)

### Album 16, chunk 1

```text
Wish You Were Here is the ninth studio album by the English rock band Pink Floyd, released on 12 September 1975 through Harvest Records in the United Kingdom and a day later in the United States through Columbia Records, as the band's first album for the label. Based on material composed while performing in Europe, Wish You Were Here was recorded over numerous sessions throughout 1975 at EMI Studios in London. The lyrics express longing, alienation, and sardonic criticism of the music industry. The bulk of the album is taken up by "Shine On You Crazy Diamond", a nine-part tribute to Syd Barrett, a Pink Floyd co-founder who had left seven years earlier due to his deteriorating mental health; Barrett coincidentally visited the studio during recording. As with their previous release, The Dark Side of the Moon (1973), Pink Floyd employed studio effects and synthesisers. Guest singers included Roy Harper, who sang lead on "Have a Cigar", and Venetta Fields and Carlena Williams, who sang backing vocals on "Shine On You Crazy Diamond". To promote the album, Pink Floyd released the double A-side single "Have a Cigar" / "Welcome to the Machine". Wish You Were Here topped charts in several countries, including the UK Albums Chart and US Billboard 200. It was certified gold in the UK and US in its year of release, and by 2004, it had sold an estimated 13 million copies worldwide. Upon release, it received mixed reviews from critics, who found its music "uninspiring" and
```

### Album 16, chunk 2

```text
"inferior" to the group's previous work. However, it has later been acclaimed as one of the greatest albums of the 1970s and of all time, with Rolling Stone ranking it number 264 in their 2020 revision of their "500 Greatest Albums of All Time" list. Keyboardist Richard Wright, drummer Nick Mason, and guitarist David Gilmour have cited it as their favourite Pink Floyd album, while bassist Roger Waters called it their "most complete" album. In 1974, Pink Floyd sketched out three new songs, "Raving and Drooling", "You Gotta Be Crazy", and "Shine On You Crazy Diamond". These songs were performed during a series of concerts in France and England, the band's first tour since 1973's The Dark Side of the Moon. As Pink Floyd had never employed a publicist and kept themselves distant from the press, their relationship with the media began to sour. Nick Mason said later that a critical NME review by Nick Kent, who Mason felt preferred the band's earlier music, may have influenced the band to return to the studio during the first week of 1975. Wish You Were Here is the second Pink Floyd album with a conceptual theme, mostly at Roger Waters's direction, reflecting his feeling that the previous communal structure of the band had disappeared in favour of more professional musicianship. "I had some criticisms of Dark Side of the Moon", noted David Gilmour, saying that "[o]ne or two of the vehicles carrying the ideas were not as strong as the ideas that
```

### Album 16, chunk 3

```text
they carried. I thought we should try and work harder on marrying the idea and the vehicle that carried it, so that they both had an equal magic [...] It's something I was personally pushing when we made Wish You Were Here." The album begins with a long instrumental introduction shifting from ambient music to the main refrain of "Shine On You Crazy Diamond", the lyrics of which were penned as a tribute to Syd Barrett, whose mental breakdown had forced him to leave the group seven years earlier. Wish You Were Here also features lyrical criticism of the rock music industry and the then-recent mainstream perception of the band. "Shine On" crosses seamlessly into "Welcome to the Machine", a song that begins with an opening door (described by Waters as a symbol of musical discovery and progress betrayed by a music industry more interested in greed and success) and ends with a party, the latter epitomising "the lack of contact and real feelings between people". Similarly, "Have a Cigar" scorns record industry "fat-cats" with the lyrics repeating a stream of clichés heard by rising newcomers in the industry, and including the question "by the way, which one's Pink?"; this was derived from an actual interaction with an agent who asked this of the band. The lyrics of the next song, "Wish You Were Here", relate both to Barrett's absence and to the dichotomy of Waters' character, with greed and ambition battling with compassion and idealism as the popularity of
```

### Album 16, chunk 4

```text
the band was growing. Alan Parsons, the EMI Studios (now Abbey Road Studios) staff engineer for Pink Floyd's previous studio album, The Dark Side of the Moon, declined to continue working with them due to the recent formation of his own group and working on their first album. Pink Floyd had worked with the engineer Brian Humphries on More, recorded at Pye Studios, and again in 1974 when he replaced an inexperienced concert engineer. Humphries, being a stranger to EMI's Abbey Road set-up, encountered some early difficulties. On one occasion, Humphries inadvertently spoiled the backing tracks for "Shine On", a piece that Waters and drummer Nick Mason had spent many hours perfecting, with echo. The entire piece had to be re-recorded. The sessions for Wish You Were Here at EMI's Studio Three lasted from January until July 1975, recording on four days each week from 2:30 pm until very late in the evening. The group found it difficult at first to devise any new material, especially as the success of The Dark Side of the Moon had left all four physically and emotionally drained. The keyboardist Richard Wright later described these sessions as "falling within a difficult period", and Waters recalled them as "torturous". Mason found the process of multi-track recording to be "tedious", while Gilmour was more interested in improving the band's existing material. Gilmour was also becoming increasingly frustrated with Mason, whose failing marriage had brought on a general malaise and sense of apathy, both of which interfered
```

### Album 16, chunk 5

```text
with his drumming. Gilmour said the band had realised their dreams of becoming rich and famous musicians, and so had to "reassess what [they] were in it for thereafter, and it was a pretty confusing and sort of empty time for a while". Humphries recalled days of inactivity: "I don't think they knew what they wanted to do. We had a dartboard and an air rifle and we'd play these word games, sit around, get drunk, go home and return the next day. That's all we were doing until suddenly everything started falling into place." After several weeks, Waters began to visualise another concept. The three new compositions from the 1974 tours were at least a starting point for a new album, and "Shine On You Crazy Diamond" seemed a reasonable choice as a centrepiece for the new work. Mostly an instrumental 20-minute-plus piece similar to "Echoes", the opening four-note guitar phrase reminded Waters of Barrett. Gilmour had composed the phrase while improvising, but was encouraged by Waters's positive response to make it the focus of the song. A subtle refrain performed by Wright, lifted from "See Emily Play", is also audible towards the end. Waters wanted to split "Shine On You Crazy Diamond", and sandwich two new songs between its two halves. Gilmour disagreed, but was outvoted three to one. "Welcome to the Machine" and "Have a Cigar" were attacks on the music business, their lyrics working with "Shine On" to provide a summary of the rise and fall
```

### Album 16, chunk 6

```text
of Barrett; Waters, on the reason of Barrett's experiences as a subject of these, said: "Because I wanted to get as close as possible to what I felt ... that sort of indefinable, inevitable melancholy about the disappearance of Syd." "Raving and Drooling" and "You've Got To Be Crazy" had no place in the new concept, and were set aside until the following album, 1977's Animals. On 5 June 1975, on the eve of the second North American leg of their Wish You Were Here Tour, Gilmour married his first wife, Ginger. That day, the band were completing the mix of "Shine On You Crazy Diamond" when an overweight man with a shaven head and eyebrows entered, carrying a plastic bag. Waters did not recognise him, and Gilmour presumed he was an EMI staff member. Wright presumed he was a friend of Waters, but realised it was Barrett. Mason also failed to recognise him, and was "horrified" when Gilmour identified him. In Mason's memoir Inside Out, he recalled Barrett's conversation as "desultory and not entirely sensible". Storm Thorgerson would later reflect on Barrett's presence: "Two or three people cried. He sat round and talked for a bit but he wasn't really there." According to Gilmour, Barrett "came two or three days and then he didn't come any more." Waters was reportedly reduced to tears by the sight of his former bandmate. Fellow visitor Andrew King asked Barrett how he had gained weight; he said that he had been overeating while
```

### Album 16, chunk 7

```text
living in isolation. He showed an unexpected enthusiasm for participating in the recording of the album, but while listening to the mix of "Shine On", showed no signs of understanding its relevance to him. Barrett also joined Gilmour's wedding reception in the EMI canteen, but left unnoticed. Apart from Waters seeing Barrett in Harrods a couple of years later, it has been agreed by biographers and journalists to be the last time any member of the band saw him alive. This series of events is regarded to have tonally influenced the final version of "Shine On You Crazy Diamond". Waters said later that "'Shine On' is not really about Syd – he's just a symbol for all the extremes of absence some people have to indulge in because it's the only way they can cope with how fucking sad it is, modern life, to withdraw completely. I found that terribly sad." As with The Dark Side of the Moon, the band used synthesizers such as the EMS VCS 3 (on "Welcome to the Machine"), but softened with Gilmour's acoustic guitar, and percussion from Mason. The beginning of "Shine On" contains remnants from a previous but incomplete studio recording by the band known as Household Objects. Wine glasses had been filled with varying amounts of fluid, and recordings were made of a wet finger circling the edge of each glass. These recordings were multi-tracked into chords. The jazz violinist Stéphane Grappelli and the classical violinist Yehudi Menuhin were performing in another
```

### Album 16, chunk 8

```text
studio in the building, and were invited to record a piece. Menuhin watched as Grappelli played on "Wish You Were Here"; however, the band later decided his contribution was unsuitable and Mason has erroneously stated that the piece was wiped. In actuality Grappelli's playing was included, but so low in the final mix that the band presumed it would be insulting to credit him. He was paid £300 (equivalent to £2,300 in 2025). The saxophonist Dick Parry, who had performed on The Dark Side of the Moon, performed on "Shine On You Crazy Diamond". The opening bars of "Wish You Were Here" were recorded from Gilmour's car radio, with Gilmour turning the dial (the classical music heard is the finale of Tchaikovsky's Fourth Symphony). Recording sessions had twice been interrupted by US tours (one in April and the other in June 1975), and the final sessions, which occurred after the band's performance at Knebworth, proved particularly troublesome for Waters. He struggled to record the vocals for "Have a Cigar", requiring several takes to perform an acceptable version. His problems stemmed in part from the stresses placed upon his voice while recording the lead vocals of "Shine On You Crazy Diamond". Gilmour was asked to sing in his place, but declined, and eventually the colleague and friend Roy Harper was asked to stand in. Harper was recording his own album in another of EMI's studios, and Gilmour had already performed some guitar licks for him. Waters later regretted the decision, believing
```

### Album 16, chunk 9

```text
he should have performed the song. The Blackberries recorded backing vocals for "Shine On You Crazy Diamond". Before releasing the album, the band embarked on a short tour of North America. The tour featured the live debut of "Have a Cigar" and "Shine On You Crazy Diamond". The other two songs from Wish You Were Here (the title track and "Welcome to the Machine") wouldn't be played live until their In the Flesh concert series of 1977. The final performance of the tour took place in the UK on 5 July 1975, two months before the release of the album, at the Knebworth Festival. Harper, performing at the same event, on discovering that his stage costume was missing, proceeded to destroy one of Pink Floyd's vans, injuring himself in the process. This delayed the setup of the band's sound system. As a pair of World War II Spitfire aircraft had been booked to fly over the crowd during their entrance, the band were not able to delay their set. The result was that a power supply problem pushed Wright's keyboards completely out of tune, damaging the band's performance. At one point he left the stage, but the band were able to continue with a less sensitive keyboard, a piano and a simpler light show. Following a brief intermission, they returned to perform The Dark Side of the Moon, but critics displeased about being denied access backstage savaged the performance. Wish You Were Here was sold in one of the more
```

### Album 16, chunk 10

```text
elaborate packages to accompany a Pink Floyd album. Storm Thorgerson had accompanied the band on their 1974 tour and had given serious thought to the meaning of the lyrics, eventually deciding that the songs were, in general, concerned with "unfulfilled presence", rather than Barrett's illness. This theme of absence was reflected in the ideas produced by his long hours spent brainstorming with the band. Thorgerson had noted that Roxy Music's Country Life was sold in an opaque green cellophane sleeve – censoring the cover image – and he copied the idea, concealing the artwork for Wish You Were Here in a black-coloured shrink-wrap (therefore making the album art "absent"). The concept behind "Welcome to the Machine" and "Have a Cigar" suggested the use of a handshake (an often empty gesture), and George Hardie designed a sticker containing the album's logo of two mechanical hands engaged in a handshake, to be placed on the opaque sleeve (the mechanical handshake logo would also appear on the labels of the vinyl album this time in a black and blue background). The cover images were photographed by Aubrey Powell, Thorgerson's partner at the design studio Hipgnosis, and inspired by the idea that people tend to conceal their true feelings, for fear of "getting burned", and thus two businessmen were pictured shaking hands, one man on fire. "Getting burned" was also a common phrase in the music industry, used often by artists denied royalty payments. Two stuntmen were used (Ronnie Rondell Jr. and Danny Rogers),
```

### Album 16, chunk 11

```text
the former dressed in a fireproof suit covered by a business suit. His head was protected by a hood, underneath a similarly fireproof wig, and fire-resistant gel was applied to him. The photograph was taken at Warner Bros. Studios in California, known at the time as The Burbank Studios. While the first fourteen takes were successful, Rondell suffered minor burns when the wind changed direction on the fifteenth, singeing his moustache. The two stuntmen changed positions, and the image was later reversed. The back cover depicts a faceless "Floyd salesman", in Thorgerson's words, "selling his soul" in the desert (shot in the Yuma Desert in California again by Powell). The absence of wrists and ankles signifies his presence as an "empty suit". The inner sleeve shows a veil concealing a nude woman in a windswept Norfolk grove, and a splash-less diver at Mono Lake – titled Monosee (the German translation of Mono Lake) in the liner notes – in California (again emphasising the theme of absence). Various releases on vinyl included a postcard with this image. The decision to shroud the cover in black plastic was not popular with the band's US record company, Columbia Records, which insisted that it be changed but was over-ruled. EMI was less concerned; the band were reportedly extremely happy with the end product, and when presented with a pre-production mockup, they accepted it with a spontaneous round of applause. Wish You Were Here was released on 12 September 1975 in the UK, and on
```

### Album 16, chunk 12

```text
the following day in the US. It was Pink Floyd's first album with Columbia Records, an affiliate of CBS; the band and their manager Steve O'Rourke had been dissatisfied with the efforts of EMI's US label Capitol Records. The band remained with EMI's Harvest Records in Europe. In Britain, with 250,000 advance sales, the album debuted at number three and reached number one the following week. Demand was such that EMI informed retailers that only half of their orders would be fulfilled. With 900,000 advance orders (the largest for any Columbia release) it reached number one on the US Billboard chart in its second week. Wish You Were Here was Pink Floyd's fastest-selling album ever. It was certified silver and gold (60,000 and 100,000 sales respectively) in the UK on 1 August 1975, and Gold in the US on 17 September 1975. It was certified seven-times platinum in the US on 12 December 2025, and by 2004 had sold an estimated 13 million copies worldwide. "Have a Cigar" was chosen by Columbia as the first single, with "Welcome to the Machine" on the B-side in the US. Wish You Were Here initially received mixed reviews. Ben Edmonds wrote in Rolling Stone that the band's "lackadaisical demeanor" leaves the subject of Barrett "unrealised; they give such a matter-of-fact reading of the goddamn thing that they might as well be singing about Roger Waters's brother-in-law getting a parking ticket". Edmonds concluded the band is "devoid" of the "sincere passion for their 'art'"
```

### Album 16, chunk 13

```text
that contemporary space rock acts purportedly have. Melody Maker's reviewer wrote: "From whichever direction one approaches Wish You Were Here, it still sounds unconvincing in its ponderous sincerity and displays a critical lack of imagination in all departments." In The Village Voice, Robert Christgau wrote: "The music is not only simple and attractive, with the synthesizer used mostly for texture and the guitar breaks for comment, but it actually achieves some of the symphonic dignity (and cross-referencing) that The Dark Side of the Moon simulated so ponderously." Years later, he wrote that Wish You Were Here was his favourite Pink Floyd album: "It has soul [...] It's Roger Waters's lament for Syd, not my idea of a tragic hero but as long as he's Roger's that doesn't matter." Paul Stump, in his 1997 History of Progressive Rock, argued that critical disappointment with Wish You Were Here was likely inevitable due to the monumental expectations of what "was (at the time) the most eagerly anticipated rock album ever released. Even the announcement of its issue date was headline news. These hosannas were grounded on no more than the fact that it was simply the Floyd's follow-up to [The] Dark Side of the Moon, which represented, for many, the acme of the genre to date." He was critical of the dominance of synthesiser textures, saying it often made Wish You Were Here sound like a showcase for Wright's new equipment. Wish You Were Here has been frequently named one of the greatest
```

### Album 16, chunk 14

```text
albums and one of the greatest progressive rock albums. In 2003, it was ranked at number 209 on Rolling Stone's list of the 500 greatest albums of all time, ranked at number 211 in a 2012 revised list, and ranked at number 264 in a 2023 revised list. In 2015, Rolling Stone named it the fourth-greatest progressive rock album. In 2014, Prog readers voted it the seventh-greatest progressive rock album. In 1998, Q readers voted Wish You Were Here the 34th-greatest album. In 2000, Q placed it at number 43 in its list of the 100 Greatest British Albums Ever. In 2000, it was voted number 38 in Colin Larkin's All Time Top 1000 Albums. In 2007, one of Germany's largest public radio stations, WDR 2, asked its listeners to vote for the 200 best albums of all time. Wish You Were Here was voted number one. In 2004, Wish You Were Here was ranked number 36 on the Pitchfork list of the Top 100 albums of the 1970s. IGN rated Wish You Were Here as the eighth-greatest classic rock album, and Ultimate Classic Rock placed Wish You Were Here as the second-best Pink Floyd album. Wright and Gilmour cited Wish You Were Here as their favourite Pink Floyd album. Wright said: "It's an album I can listen to for pleasure, and there aren't many Floyd albums that I can." Gilmour said: "The end result of all that, whatever it was, definitely has left me an album I can live
```

### Album 16, chunk 15

```text
with very very happily. I like it very much." Waters said Wish You Were Here and The Dark Side of the Moon were the "most complete" Pink Floyd albums, and that Wish You Were Here and their next album, Animals (1977), "signalled the end of the band as it had been before". Wish You Were Here has been remastered and re-released on several formats. In the UK and US it was re-issued in quadraphonic using the SQ format in 1976, and in 1980 a special Hi-Fi Today audiophile print was released in the UK. It was released on CD in Japan in October 1982, in the US in 1983, and in the UK in 1985, and again as a remastered CD with new artwork in 1994. In the US, Columbia's CBS Mastersound label released a half-speed mastered audiophile LP in 1981, and in 1994 Sony Mastersound released a 24-carat gold-plated CD, remastered using Super Bit Mapping, with the original artwork from the LP in both longbox and jewel case forms, the latter with a cardboard slipcover. The album was included as part of the box set Shine On, and three years later Columbia Records released an updated remastered CD, 17 seconds longer than the EMI remasters from 1994, giving a running time of 44:28. The label was a recreation of the original machine handshake logo, with a black and blue background. Wish You Were Here was rereleased in 2000 for its 25th anniversary, on the Capitol Records label in the
```

### Album 16, chunk 16

```text
US. It was re-released and remixed in 2011. The Wish You Were Here – Immersion Box Set includes the new stereo digital remaster (2011) by James Guthrie on CD, a previously unreleased 5.1 Surround Mix (2009) by James Guthrie on DVD and Blu-ray, a Quad Mix (which had been released only on vinyl LP and 8-track tape) on DVD, as well as the original stereo mix (1975) on DVD and Blu-ray. This campaign also featured the 2011 stereo remaster on 180g heavyweight vinyl, as well as the 2011 stereo remaster and the 5.1 surround sound mix (2009) as a hybrid Super Audio CD (SACD). In 2016, the 180g vinyl was rereleased on Pink Floyd Records (with distribution by Warner Music and Sony Music), remastered by James Guthrie, Joel Plante and Bernie Grundman. In September 2025, Sony announced a 50th-anniversary box set, with a new Dolby Atmos mix, additional tracks and live performances, and a hardcover book. David Gilmour – lead vocals (tracks 2, 4), vocal harmonies (tracks 1–2, 4–5), electric lead guitar (1, 3, 5), electric rhythm guitar (tracks 1, 3, 5), acoustic guitar (tracks 2, 4), Twelve-string guitar (track 4), pedal steel guitar (tracks 4–5), bass (track 5), EMS VCS 3 (tracks 2–3) Nick Mason – drums (tracks 1, 3–5), timpani and cymbals (track 2) Roger Waters – lead vocals (tracks 1, 5), vocal harmonies (track 1), bass (all tracks), EMS VCS 3 (tracks 1–4) Richard Wright – vocal harmonies (tracks 1, 5), keyboards (all tracks), Steinway piano (tracks
```

### Album 16, chunk 17

```text
1, 4–5), vibraphone (track 1), Minimoog (all tracks), EMS VCS 3 (track 1) Venetta Fields, Carlena Williams – backing vocals (tracks 1, 5) Dick Parry – saxophones (track 1) Roy Harper – lead vocals (track 3) Stéphane Grappelli – violin (track 4; mixed down to an almost inaudible level on original release, restored only on Experience Edition) Unidentified musician(s) – singing glasses (tracks 1, 5), sound effects (tracks 1, 5), EMS VCS 3 (track 5) Pink Floyd – producer Phil Taylor – road manager/equipment technician. Additional photography(remaster & 50th anniversary edition) George Hardie – graphics
```

## Album 17: GO:OD AM — Mac Miller

- **album_id:** `7f22644a-6442-46df-b6e8-fbc86bb3bc2d`
- **Tags (identification only):** hip hop, east coast hip hop, pop rap, abstract, abstract hip hop, bittersweet, boastful, bright
- **Chunks:** 5 (1178 words)

### Album 17, chunk 1

```text
GO:OD AM is the third studio album by American rapper Mac Miller. It was released on September 18, 2015, by REMember Music and Warner Bros. Records. The album features guest appearances from Ab-Soul, Chief Keef, Lil B, Miguel, and Little Dragon. GO:OD AM was supported by two singles: "100 Grandkids" and "Weekend". Miller began his international tour in support of the album on September 20, 2015, which started at his hometown of Pittsburgh, Pennsylvania. The album received generally positive reviews from critics, and debuted at number four on the US Billboard 200. On January 14, 2014, Miller announced that he was parting ways with Rostrum Records. On May 11, 2014, Miller released his eleventh mixtape Faces. On October 21, 2014, news surfaced that Miller signed a recording contract with Warner Bros. Records, including a distribution deal for his label REMember Music. On July 30, 2015, Miller announced that he had completed his third studio album. On August 5, 2015, he revealed the album title, release date, as well as a music video for the lead single "100 Grandkids". On September 4, 2015, Miller released a mobile app that functions as an alarm and plays snippets of new music leading up to the album's release. Fans can also purchase a Breakfast Special Edition of the LP, packaging in a cereal box complete with cereal, a plastic cereal bowl, and a surprise item in addition to the CD and digital download. In the days leading up to the album's release, Miller hosted
```

### Album 17, chunk 2

```text
a series of free social events to promote the album, deemed Homecoming Weekend. The festival culminated with the album release show and subsequent international tour. Miller toured internationally in support of the album on The GO:OD AM Tour, and it started at his hometown of Pittsburgh, Pennsylvania. A 10th anniversary edition of the album, featuring 3 additional songs, was released on October 3, 2025. The album's first single, "100 Grandkids", was released on August 7, 2015. On August 7, 2015, the music video was released for "100 Grandkids". The album's second official single, "Weekend" featuring Miguel, was released January 11, 2016. The album's first promotional single, "Break the Law", was released on August 17, 2015. The album's second promotional single, "Clubhouse", was released on September 10, 2015. GO:OD AM was met with generally positive reviews. At Metacritic, which assigns a normalized rating out of 100 to reviews from professional publications, the album received an average score of 71, based on 14 reviews. Aggregator AnyDecentMusic? gave it 6.7 out of 10, based on their assessment of the critical consensus. David Jeffries of AllMusic said, "Getting sober and ridding himself of depression are topics that GO:OD AM touches upon, but rather than his past, the 'show and prove' Miller is driven by his rebirth on an interesting and infectious LP that's also his strongest to date". Meghan Garvey of Billboard said, "On major-label debut GO:OD AM, his third and best studio album, Miller grapples frankly with fame, addiction, recovery and the struggle
```

### Album 17, chunk 3

```text
to be a decent person over taut, melancholy production that channels both bleary inebriation and hard-fought optimism". Andrew Gretchko of HipHopDX said, "If Miller's second album was a stepping stone that allowed him to climb above his partying past, GO:OD AM serves as a wakeup call for those that think his music is still best suited for frat parties. With a bright future ahead of him, Miller has positioned himself for career longevity, so long as he can keep his demons behind him". Chris Dart of Exclaim! stated, "If there's one flaw with this album, it's its length. If you make a 70-minute album, all 70 of those minutes better be phenomenal, and that's not the case here. Dropping two or three songs would be enough to turn this very good record into a brilliant one". Brian Duricy of PopMatters said, "Relying on his individuality yields his greatest results, but the album's most passable moments too". Tayler Montague of Pitchfork said, "We might not learn a lot of specifics about him, but there's a lot of honesty in his music if you look for it". C. J. Rucker of The Source said, "GO:OD AM is the most transparent music Mac Miller has ever made and in doing so he has created a sonically cohesive and impressive album". Michael Madden of Consequence said, "Beyond rapping, producing, and singing, Mac must see himself as a total package, and at 70 minutes long, GO:OD AM was always bound to have a lot of
```

### Album 17, chunk 4

```text
elements clashing for space. Somehow, it still feels balanced. It's essentially an offbeat stoner rap album, but there's still plenty of melody, in Mac's own singing and the guest appearances from the likes of Miguel on "Weekend" and Nagano on "The Festival", as well as in the EDM of "Jump" at the end of the album". Lanre Bakare of The Guardian said, "It's musically adventurous in a way that recalls Chance the Rapper's Surf project, but takes fewer detours into psych and jazz". Michael G. Barilleaux of RapReviews said, "At the end of the day Mac Miller is without a doubt capable of bringing more to the table than shallow, boring rap. Unfortunately, he doesn't do much to prove that on GO:OD AM". Christopher R. Weingarten of Rolling Stone said, "GO:OD A.M. is a 70-minute studio album that would have been better served as two mixtape diary entries until the sober Miller discovered a smarter way to channel his newfound enthusiasm". In the United States, GO:OD AM debuted at number four on the Billboard 200, selling 73,000 copies in its first week. It was the third highest selling album in the United States during its debut week. As of October 2015, the album has sold 92,000 copies domestically. GO:OD AM earned 14,000 album-equivalent units in the week following Mac Miller's death on September 7, 2018, thus allowing the album to re-enter the Billboard 200 at number 32. On December 11, 2024, the album was certified platinum by the Recording Industry
```

### Album 17, chunk 5

```text
Association of America (RIAA) for combined sales and streams in excess of 1,000,000 units in the United States. Thundercat – bass (tracks 2, 10) Stuart Bogie – saxophone (tracks 2, 16) Christian Wunderlich – guitar (tracks 3, 5–7, 11) Nice Rec – scratching (tracks 3, 8) Ben Adamson – synthesizer (track 3), organ (track 5), trumpet (tracks 5, 7), flugelhorn (track 6) Robert Wooten III – bass (track 4) Jake Troth – guitar (track 4) Will Miller – trumpet (track 4) Jaslyn Taylee-Edgar – choir (tracks 5, 11) Jordan Dame – choir (tracks 5, 11) Nikki Leonti – choir (tracks 5, 11) Ryan Edgar – choir (tracks 5, 11) Alexander Sowinski – drums (track 11; uncredited) Chester Hansen – bass guitar, piano (track 11; uncredited) Taylor Graves – piano (track 13) Vic Wainstein – recording (tracks 1, 7) Big Jerm – recording (tracks 2, 5, 12, 15) Andrew Klein – recording (track 3) Josh Berg – recording (tracks 4, 5, 7–14, 16) Larry Fisherman – recording (track 6) E. Dan – mixing (all tracks), recording (tracks 4, 17)
```

## Album 18: BELOVED — GIVĒON

- **album_id:** `8c17ce9a-b141-485a-b836-a735f3a4cc0e`
- **Tags (identification only):** r and b, soul, contemporary r and b, english, 1–4 wochen, adult contemporary r and b, funk / soul, offizielle charts
- **Chunks:** 8 (1974 words)

### Album 18, chunk 1

```text
Beloved (stylized in all uppercase) is the second studio album by American singer-songwriter Giveon. Released through Epic Records and Not So Fast on July 11, 2025, production was handled by a variety of record producers, including Matthew Burnett, Jahaan Sweet, Gitty, Sevn Thomas, and Maneesh. Recorded with a live band, Beloved draws from 1970s rhythm and blues and soul music, and the music evokes Al Green, Isaac Hayes, The Delfonics, and Philadelphia soul. With Beloved, Giveon intended to convey where he is as an artist sonically and the time he built on his craft, and to add to the Black American male perspectives on relationships in music. An autobiographical album, the album tells a raw and realistic love story inspired by multiple relationships Giveon had. It was preceded by two singles, "Twenties" and "Rather Be". It debuted and peaked at number eight on the Billboard 200 and at number four on the Billboard Top R&B/Hip-Hop Albums chart, and received positive reviews. Rolling Stone and Variety ranked the album number 57 and nine on their Best Albums of 2025 lists. The album was nominated at the 68th Annual Grammy Awards for Best R&B Album and the 57th NAACP Image Awards for Outstanding Album. The album was promoted with Dear Beloved, The Tour, which ran internationally from October 2025 to March 2026. On May 15, 2026, Giveon released a deluxe version of the album subtitled Act II which includes five additional tracks with features from Kehlani, Leon Thomas, Sasha Keable, and Teddy
```

### Album 18, chunk 2

```text
Swims. Simultaneously, the groovy, energetic opener titled "Jezebel" was released as a single with a music video. For his sophomore album Beloved, Giveon wanted to convey his position sonically as an artist and the three years he worked to build on his craft. He also wanted to add to the male point of view in rhythm and blues, as he viewed that while the genre has predominant perspectives from women, "seeing love through the male lens can get lost now", further specifying that a Black American male perspective on relationships is lacking across any genre. Wanting to keep the rawness and authenticity, Giveon created the album as a realistic love story, which he stated is far from how a fairy tale would go. The album is autobiographical, and was inspired by multiple relationships he had, such as with singer Justine Skye. In the album's recording, Giveon used the same group of instrumentalists for every song to ensure its cohesiveness. Beloved channels 1970s rhythm and blues and soul music. Rolling Stone and Variety noted that the album's sound is influenced by Philadelphia soul, such as Teddy Pendergrass, The Delfonics, and "TSOP (The Sound of Philadelphia)", and also by Al Green, Isaac Hayes, and Marvin Gaye. Giveon named the album from a term that he stated captures the "warm and classic and '70s inspired and soulful" feel of the music, "beloved", which was what he heard his grandfather call his grandmother. The album opens with "Mud", which starts with a symphony before
```

### Album 18, chunk 3

```text
transitioning to a "smooth beginning" that evokes Teddy Pendergrass. As someone who refers to movies frequently, Giveon intended the beginning to consist of "heavy drums and powerful strings" to draw the listener in and to evoke the feeling of a film's big opening scene before it rewinds to tell how the story led up to that sequence. Lyrically, it centers on a confrontation with an ex who smeared his name and characterized him as the antagonist in their relationship. "Rather Be" is a soul ballad with vintage production about Giveon preferring to remain a fool with a past lover than to begin anew with some other person, believing that no one else can come close to what he had. The song's instrumentation evokes Al Green, Philadelphia soul, and Memphis soul. The next song, "Twenties", is another soul ballad with vintage production, in which Giveon sings of mourning the time spent on a past relationship that lasted throughout his twenties, accompanied by instrumentation consisting of bass, strings, choral arrangements, piano, an electric sitar, and drums. Giveon sings "Thought I was learning myself, I was just learning you / Is anything black and white when you're barely 22?", encapsulating the "slight disorientation and philosophical reasoning" that drives the album. "Strangers" comes next, and was the first track made for the album, after which Giveon realized the album's direction. In "Strangers", a defeated Giveon learns that his ex is now in a relationship with another, proclaiming "Yes, I'm taking this hard" through a
```

### Album 18, chunk 4

```text
"pained, zigzag" riff, and by the next song, the Delfonics-inspired "Numb", Giveon recounts his inability to feel, admitting "I’ve been here before" over "angelic background coos". "I Can Tell" is a more hopeful track where Giveon makes his case as a better option for a woman who shows signs that she is unhappy with her present lover. "Diamonds For Your Pain" and "Keeper" lyrically center on Giveon "slyly working his way out of the doghouse". The former is the shortest track on the album, being an interlude, and it focuses on Giveon's attempt at some accountability by being aware of the turbulence he created, but instead of finding real solutions, he gifts her materialistic things such as jewelry. It starts with staccato strings that build up, as Giveon intended it to feel "cinematic and big". Giveon aimed to conceal the topic of its lyrics through pretty-sounding music. In "Backup Plan", an anxious Giveon takes the emotional distance from his lover as evidence of him being replaced, and he watches as she contemplates departure. Andy Kellman of AllMusic described the track as a "smudged, extended, and downcast coda to Isaac Hayes' version of 'The Look of Love'". In "Bleeding", Giveon questions his relationship's future, hurt by his lover's fixation on her ex. "Avalanche", a track that depicts "a moment before it went sour", features groovy production and is "sung from a place of promise and not repair". Giveon delusionally states with naivete, "Intuition says we’re way too young to start a
```

### Album 18, chunk 5

```text
family / But I’ve been thinking about forever, my dear", in a dense mix that hints at a "looming threat". Giveon ends the album with a track about a couple dedicated to together overcoming conflict in "Good Bad Ugly", as he sings, "I'll even let you run me down to the ground / Watching you while you run your mouth / I stick around / I love you ’cause you love me / Through the good, bad, and ugly". The lead single of the album, "Twenties", was released on February 7, 2025. In an interview with Billboard on March 28, 2025, Giveon said that he is "excited for people to hear" his next album and feels that he has "a responsibility with this music because I see how it touches and helps people". The second single, "Rather Be", was released on May 16, 2025. Giveon announced the album sixteen days later along with its cover art and release date, revealing that he spent over one thousand days recording it. On July 1, 2025, he revealed the official tracklist through a letter similar to a "breakup note", with each song title in all caps and embedded within "emotional reflections" which offer a glimpse into the album's themes. The album was released on July 11, 2025; at the same time, Giveon released "I Can Tell" as a single with a music video. Directed by Sahra Zadat, the 1970s-inspired video opens with a classic cinematic trope: a "train station farewell" between Giveon and
```

### Album 18, chunk 6

```text
his lover. On July 10, 2025, Giveon told Rolling Stone how the album, which was created live, was meant to be performed live, and described his upcoming tour as his best. He expressed his wish to do "a full eight to 10 piece [backing band]" depending on the stages' sizes and for the night to feel like a movie like his album. On July 22, 2025, Giveon announced "Dear Beloved, The Tour". The North American leg ran from October 1, 2025 (Seattle) to November 6, 2025 (New York City), with Free Nationals, Charlotte Day Wilson, and Sasha Keable as opening acts. The Australian, Asian, and European legs of the tour were announced subsequently, and ran from January 18 to March 26, 2026. On April 10, 2026, Giveon announced a deluxe version of the album, subtitled Act II, through a teaser that depicts a woman named Jezebel leaving Giveon voicemails. It was released on May 15, 2026, and included five new songs with features from Kehlani, Leon Thomas, Sasha Keable, and Teddy Swims. Uptempo album opener "Jezebel" was released simultaneously as a single with a music video directed by Loris Russier. "Jezebel" is a track with a groovy, "more energetic, almost pop-inspired sound"; Rated R&B called it a descendant of The Gap Band's "Outstanding" and Frankie Beverly's "We Are One". Both Rated R&B and HotNewHipHop described the track as a standout. In "Save Some For Me" featuring Kehlani, the two plead with a love interest to "give them the chance to
```

### Album 18, chunk 7

```text
love them the way they deserve." Tallie Spencer of HotNewHipHop stated that the deluxe "continues the strong chemistry Giveon has built with collaborators throughout the BELOVED era, with each feature blending naturally into the project's warm and cinematic R&B sound." Giveon described the standard version, which he labeled as Act I, as a conversation with himself or with a romantic interest, and described Act II as "a conversation with friends now about the situation" and "more communal". Beloved received positive reviews from music critics. AllMusic's Andy Kellman wrote that the album "is filled with many other dramatic, tear-stained expressions of regret, frustration, and heartache" and that although it isn't "an out-and-out throwback, it draws substantially from the '70s", comparing the record to Philadelphia soul music, the music released by Hi Records, and "less so from maestros such as Barry White and Isaac Hayes". He concluded that "Giveon might view his six-year relationship as misspent, but there's no second-guessing the time he devoted to converting it into art". Writing for Rolling Stone, Mankaprr Conteh wrote that Beloved is "almost barren of the hip-hop flourishes that peppered his earlier work" and that Giveon "instead leans all the way into the orchestral R&B of another time, lush with searing strings and the crash of real hi-hats". Similarly to Kellman, Conteh wrote that "Beloved feels indebted to Al Green, Philly soul, The Jackson 5, and Blaxploitation soundtracks". Conteh continued that "Giveon offers a stunning, panoramic view of romantic relationships in their toughest places" and
```

### Album 18, chunk 8

```text
that the album particularly shines when Giveon "embraces how complicated heartache can be". Jem Aswad of Variety stated that Beloved accomplished the rare feat of accurately recreating the sound of a certain period or genre and bringing it to the present. Rated R&B's Keithan Samuels wrote that the album "is an ode to classic soul from the ’70s, with its lush instrumentation — cinematic strings, regal horns, stirring bass and warm drums — paired with emotive storytelling." Rolling Stone ranked number 57 on their Best Albums of 2025 list, while a critic from Variety ranked it number 9. Rated R&B placed the album at number five for their 25 Best R&B Albums of 2025 list. Beloved debuted at number eight on the Billboard 200 chart, earning 44,000 album-equivalent units (including 8,000 in pure album sales) in its first week. The album also accumulated a total of 47.78 million on-demand streams of the album's songs. John Kercy – mixing Hayden Duncan – engineering (2, 5, 6, 8, 10) Garrett Duncan – engineering assistance (1–3, 6, 8, 10, 11, 13) Collin Clark – engineering assistance (1, 2, 4–6, 8, 12, 14) Terena Dawn – engineering assistance (2, 3, 8, 10, 12) Ivan Marcelo – engineering assistance (2, 4–8, 10, 13, 14) Danforth Webster – engineering assistance (3, 4, 11) Dereck Negron – engineering assistance (5, 11)
```

## Album 19: (Breach) — The Wallflowers

- **album_id:** `c56abf2b-27c7-40c7-829d-f95ee9dadac8`
- **Tags (identification only):** adult alternative pop/rock, alternative rock, soundtrack, alternative/indie rock, american trad rock, americana, folk rock, pop/rock
- **Chunks:** 2 (530 words)

### Album 19, chunk 1

```text
Breach (stylized as (Breach)) is the third studio album by the Wallflowers. The album's first single was "Sleepwalker", the video of which poked fun at lead singer Jakob Dylan's "rock star" status following the success of Bringing Down the Horse (1996). Guests on the album included Elvis Costello, who performed vocals on "Murder 101". Despite positive critical reception, the album failed to match the commercial success of Bringing Down the Horse, seeing a commercial decline. (Breach) peaked at number 13 on the Billboard 200 and received gold certification by the Recording Industry Association of America (RIAA). “Sleepwalker”, however, peaked at 73 on the Billboard Hot 100. A Spin magazine article looking back on Jakob Dylan's 30-year career noted that Breach alludes to his mixed feelings about his lineage and fame more than any other album in his discography. Spin commented that "Dylan addresses the cynics on lead single 'Sleepwalker,' a catchy rocker that reflects how Dylan felt at the height of his fame: like a dazed character drifting through his own life." They similarly point to "Hand me Down", where "Dylan sings self-effacingly about the perception of having failed to live up to his pedigree." As part of an interview for the piece, Dylan told Spin that "I like that record a lot. It’s more complicated than Bringing Down The Horse, and I think I started getting better as a songwriter.” In another retrospective interview with Uproxx, Dylan said that while this was a "difficult record to make," he feels
```

### Album 19, chunk 2

```text
it features some of his best songwriting. He told music critic Steven Hyden that "By Breach, I knew there was going to be scrutiny on some of the songs and I decided that I was just going to not care about it." Despite weak album sales, Breach received strong reviews from critics. AllMusic said of the album: "On the surface, there's not much different between this album and its predecessor, but the songs are stronger, sharper, and the performances are lean, muscular, and immediate." Rolling Stone was also receptive of the album, stating: "The slow stuff might be a bit ponderous, but the first six or seven songs manage a rare trick: They're incandescent enough to jump out at you on the radio, yet are steeped in a type of introspective inquiry that was once integral to rock & roll, and has nearly vanished." Mario Calire – drums Jakob Dylan – lead and backing vocals, rhythm guitar Rami Jaffee – keyboards, vibes, backing vocals Greg Richling – bass guitar, percussion, backing vocals Michael Ward – lead guitar, backing vocals Matt Chamberlain – drums Greg Leisz – additional musician Jon Brion – additional musician Lenny Castro – percussion Mike Campbell – guitar Elvis Costello – backing vocals Michael Penn – backing vocals Chris Penn – backing vocals Frank Black – backing vocals Gary Louris – backing vocals Buddy Judge – backing vocals Joul Derouin – strings Suzie Katayama – strings Karie Prescott – strings Michele Richards – strings Greg Adams – horns Kenneth Kugler – horns Nicholas Lane – horns Salvator Cracchiolo – horns Mitchell Froom – horns arranger Michael Penn – production Andrew Slater – production Tom Lord-Alge – mixing
```

## Album 20: Infinity on High — Fall Out Boy

- **album_id:** `f9307f47-001b-4a5c-91c3-62032b214005`
- **Tags (identification only):** rock, alternative pop/rock, pop punk, pop rock, punk pop, alternative, alternative punk, emo
- **Chunks:** 21 (5092 words)

### Album 20, chunk 1

```text
Infinity on High is the third studio album by American rock band Fall Out Boy, released on February 6, 2007, by Island Records. Recorded from July to October 2006 at Pass Studios in Los Angeles, California, its music was composed by lead singer and guitarist Patrick Stump and the lyrics were penned by bassist Pete Wentz. The album features collaborations with new producers and guest artists, such as Babyface and Jay-Z, and sees the band experimenting with genres including R&B, soul, and flamenco. Fall Out Boy also utilized instruments such as horns, violins, and pianos, which had not been used on previous releases. As reported by Billboard, the band "[drifted] further from its pop punk roots to write increasingly accessible pop tunes", a slight departure from the group's previous sound. Critics felt that its lyrics served as a response to the band's rise to fame. Fall Out Boy embarked on several tours to promote the album, including the Friends or Enemies Tour, the Honda Civic Tour, and the Young Wild Things Tour. Infinity on High debuted at number one on the US Billboard 200, selling over 260,000 copies in its first week of sales and becoming the band's first number-one album. It also reached number one in New Zealand and peaked within the top-five of countries including Canada, the United Kingdom, and Australia. Five songs were released as singles, four of which charted on the US Billboard Hot 100; the second single, "This Ain't a Scene, It's an Arms Race",
```

### Album 20, chunk 2

```text
peaked at number two. The album received generally positive reviews from critics, with many praising Stump's vocals and the band's new musical direction, and has sold over two million copies worldwide and over 1.4 million in the United States alone. After taking a two-month break following the band's Black Clouds and Underdogs tour in promotion of their 2005 album From Under the Cork Tree, Fall Out Boy returned to the studio to begin work on their follow-up effort. The band began writing songs for the new album while touring, and intended to quickly make a new album in order to keep momentum in the wake of their breakthrough success. Vocalist Patrick Stump stated that he wished to begin working on the record earlier, but the group's management urged the members to take time off to recuperate from their constant touring schedule. The band's label, Island Records, underwent changes while the group prepared to record, which postponed the studio schedule for three weeks. Bassist/lyricist Pete Wentz asserted that "We're definitely writing all the time, so we're not going to try to squeeze every last drop out of the stone. That's part of what's been wrong with the rock industry: they keep fans waiting far too long, and bands go away and disappear off the face of the planet. That's not the way it's going to be for Fall Out Boy." During this time off, Fall Out Boy contributed a cover of the song "What's This?" for the 2006 rerelease of The
```

### Album 20, chunk 3

```text
Nightmare Before Christmas soundtrack, as well as a remix of their song "Of All the Gin Joints in All the World" for the Snakes on a Plane soundtrack. Wentz also purchased a house in Los Angeles, where he spent much time writing lyrics to new songs. While writing the album, Fall Out Boy began searching for potential producers. The band sought out R&B singer/producer Babyface, as they admired his work on the soundtrack to the 2001 film version of Josie and the Pussycats. Babyface saw one of the interviews in which the band discussed its desire to work with him and contacted the group. Babyface produced two of the songs, "I'm Like a Lawyer with the Way I'm Always Trying to Get You Off (Me & You)" and "Thnks fr th Mmrs". Neal Avron, who also produced the band's previous album, handled production for eleven of Infinity on High's fourteen tracks. Before recording, the band began with six weeks of pre-production, which was encouraged by Avron. This period included both rehearsals and writing, as well as working out all the sounds and arrangements. It began in Chicago before the group relocated to the Swing House studios in Los Angeles. Additionally, some rough recordings of songs were created to be used in the studio as a future reference. Infinity on High was recorded from July to October 2006 at the Pass Studios in Los Angeles. Much of the writing process was done individually by the band members. Generally, Wentz would write
```

### Album 20, chunk 4

```text
his lyrics first and send them to Stump, who would create a melody by playing guitar along to the words to "find a groove". Stump's goal with his songs was to create his music while changing Wentz's original lyrics as little as possible. After a melody was written, Stump would create a general rhythm for the song. Although Fall Out Boy has no specific rhythm or lead guitar roles, Stump viewed himself as more of a rhythm guitarist on the album due to his experience as a drummer in previous bands. Guitarist Joe Trohman often wrote his guitar parts after hearing Stump's work, filling in the "empty spaces" in the songs with "tons of guitars and Johnny Marr-type atmospheric parts". The group felt that this writing process helped create a more full sound. Upon listening to the finished tracks, the members selected guest appearances they felt would work with the songs. The group "aim[ed] for the stars" on its choices of collaborators, with Wentz stating, "I want to bring in people who no one would expect...This year it's like, we made some new friends, like Lil Wayne. Or let's get Jay-Z on there." Wentz commented on working with Jay-Z, saying "It was insane. We called him up and thought we were gonna talk to his assistant. Then he answers the phone, like, 'Yo, this is Hov,' and we were like, 'Um ...' It just happened like that. And it was pretty crazy." Jay-Z recorded his introduction to the album's opening
```

### Album 20, chunk 5

```text
song "Thriller" while on tour in Australia and sent it to the band, who later put the vocal on the album. At a fashion show in Los Angeles, Wentz met rapper Kanye West, who invited Wentz and Stump to his home to share new music. West then agreed to create a remix of "This Ain't a Scene, It's an Arms Race" three weeks before the scheduled release of the album. The band was unable to include the remix on the album due to time constraints, but a remix of West's version featuring Lil Wayne, Lupe Fiasco, Travis McCoy, Paul Wall and Tyga was released in July 2007. During the recording of the album, the band members pursued other various activities. Stump, who co-produced "Don't You Know Who I Think I Am?" from Infinity on High, was also working on fellow Fueled By Ramen act The Hush Sound's album Like Vines. Wentz was conceiving a social networking website called FriendsOrEnemies.com as well as designing for his clothing line, Clandestine Industries. Wentz was often interviewed about the album at Clandestine fashion shows. The album marked a departure in Fall Out Boy's sound in which the band implemented a diverse array of musical styles. As reported by Billboard, Fall Out Boy "drifts further from its hardcore punk roots to write increasingly accessible pop tunes," a slight departure from the group's previous more pop-punk sound. Infinity on High has been compared to the work of pop-punk bands such as Green Day, with Ann Powers
```

### Album 20, chunk 6

```text
of the Los Angeles Times commenting, "Whatever snot and feedback courses through these songs, sweetness always triumphs, carried forth by bubblegum bass lines, snappy drums and tunes as comforting as lullabies." Stump explained that the album contains a variety of different moods: "It’s one of those things where you get older as a band and you do your own thing...The older Fall Out Boy elements, from the early records, are definitely there, and this album is an extension of that." The album opens with the song Thriller, which was named after the 1982 Michael Jackson album Thriller, and which itself led with a spoken introduction from Jay-Z, who owned the record label that produced the album, Def Jam Recordings. Pete Wentz told the music television channel MTV that the band called Jay Z on the phone to get his introduction for the song. In an interview with Fall Out Boy, drummer Andy Hurley stated that the opening parts in "Thriller" were copied from "Islands to Burn" by Racetraitor, a band he once drummed for. The song was created as an reflection on the band's previous two years. Some lyrics reflect on previous mediocre album reviews the band received. The lyrics also call out the rise of the band's popularity, "But by fall we were a cover story". In context the song's opening lines are, "Last summer we took threes across the board, but by fall we were a cover story now in stores. Make us poster boys for your scene,
```

### Album 20, chunk 7

```text
but we are not making an acceptance speech." The song also features the lyric "Fix me in 45" which refers to the way singles were released on vinyl records. Some reviewers complained that the album did not have a hardcore edge, but the song "Thriller" was an exception. Slant Magazine said the song features "a crunching, emo-fied knockoff of the riff from Metallica’s "One"", while Jack Phinney of the Northern Valley Suburbanite reviewed the album and called the song "spectacular". Alternative Press opined in February 2023 that the song was dominated by the soaring vocals of Patrick Stump and his pop arrangement, and described it as the tenth heaviest song in the Fall Out Boy body of work. Writing in August 2023, Tamzin Kraftman wrote that the song's "chugging pulse", played by Fall Out Boy guitarist Joe Trohman, "electrifies the track". In February 2013, the band led a concert at Webster Hall with the track; Rolling Stone's Andy Greene opined that, upon launching into the song, the audience's "squeals were deafening". Stump called "This Ain't a Scene, It's an Arms Race" the "funkiest thing we’ve ever done", and attributes the change in musical style to his love of soul music, which he acquired by listening to oldies stations as a child. Wentz describes the song "a bit of '70s funk mixed with [the band’s 2003 album] Take This to Your Grave with tight verses and big, fat choruses". The song closing sing-along was influenced by Justin Timberlake's "Señorita". Cory Apar
```

### Album 20, chunk 8

```text
of Allmusic compared the Babyface-produced track "I'm Like a Lawyer with the Way I'm Always Trying to Get You Off (Me & You)" to Maroon 5. Wentz characterized Stump's vocal performance on the song as "straight-up Motown", continuing to say "If there wasn't a rock band playing, it'd be straight R&B, and he'd go on tour with just an upright bass and a drum and open up for R. Kelly." "The Carpal Tunnel of Love" has been referred to as "a prime slab of what the boys have become famous for: highly caffeinated pop-punk mixed with a little white-boy soul and some hard-core yelping." The song features Stump singing in a falsetto in the chorus over Trohman's "crunchy" guitars, as well as a breakdown in which Wentz employs death growl-style vocals. The band also used instruments that did not appear on previous albums, such as horns and violins. The members became more open to experimentation, but attempted to not over-produce the album; Stump stated that he "had to resist the temptation to use a lot of strings." "Golden" consists exclusively of vocals, piano and organ, and Stump dubbed the song "much softer than anything we’ve ever done". The group utilizes a full horn section on "I've Got All This Ringing in My Ears and None on My Fingers", a track which has been likened to Queen. Violins are used on both "Thnks fr th Mmrs", in addition to an acoustic guitar strummed flamenco-style, and "The (After) Life of the Party",
```

### Album 20, chunk 9

```text
which also features electronic-influenced sounds. Commenting on the instruments used on "Thnks fr th Mmrs", Stump stated "I never thought I'd get a euphonium onto a Fall Out Boy record". "You're Crashing, But You're No Wave" features a gospel choir, while "Thriller" contains a spoken-word intro from Jay-Z. Barry Nicolson of NME referred to the song as a "towering, Foo Fighters-esque slice of thunderous rhythm and radio-friendly melody." Critics have described the album as being a pop-punk, pop rock, pop, and alternative rock album. While writing the album, Wentz drew lyrical inspiration from rapper Lil Wayne, whom he called "the best lyricist of [2006]." Speaking of Infinity on High's lyrical themes, Wentz stated, "On the last record, the lyrics were about 'This is where we're going to be a year from now, and this is what you're going to be saying about us.' But this time, we realized that a lot of bands should spend less time running their mouths and more time writing their songs." In 2013, Wentz reflected, "on a record like Infinity on High, I feel like I tried really hard to explain my perspective – and when I look back on it in hindsight I think it’s an extremely unrelatable record. Critics felt that much of the lyrics address the band's rise to fame and the pressure of maintaining a loyal fanbase. Sasha Frere-Jones of The New Yorker commented that "The only top-ten acts that talk about fame as much as Fall Out Boy does are
```

### Album 20, chunk 10

```text
rappers, although their take on selling records is less conflicted." Cory Apar of Allmusic opined that "Wentz' lyrics are oftentimes resentful, full of fame-induced angst, and really emphasize his need to drive home his position that stardom has not changed the band." "Thriller" serves as an autobiographical recap of the two years following From Under the Cork Tree's release, referencing the band's mediocre CD reviews and breakout success, as well as thanking their "diehard" fans. The song discusses the band's Best New Artist Grammy loss, and Wentz calls it the "most narcissistic song on the album". The line "Fix me in forty-five" is a reference to the length of a therapy session. On "This Ain't a Scene, It's an Arms Race", Wentz uses wartime-inspired metaphors to discuss their newfound popularity; he called the song "kind of a tongue-in-cheek look at the way we are so addicted and obsessed with new arts, cultures and loves – to the point where it just becomes oversaturated." "I'm Like a Lawyer..." has been described as "about as close to a love song as you'll get from this band, a rare moment of tenderness among songs about blog entries, guest lists, and therapy sessions." In a tribute to the politicized Chicago hardcore scene, Wentz describes the story of a rigged court case of African-American civil rights activist Fred Hampton Jr. in "You're Crashing, But You're No Wave". The song has been described as a "very well-written track, a welcome respite from the one-liners which permeate
```

### Album 20, chunk 11

```text
the majority of the record." The album's title is taken from a letter written by Vincent van Gogh to his brother Theo in 1888, in which he describes his renewed health and the positive effect it has had on his painting. Originally written in Dutch, Van Gogh's phrasing has been translated as "Be clearly aware of the stars and infinity on high. Then life seems almost enchanted after all". Speaking of the title shortly after its announcement in November 2006, Wentz stated "As for what that means in relation to the record, we'll just let it unfold when people hear it." While Wentz declined to reveal the relationship between the title and the album's songs, MTV reporter James Montgomery opined that "It's not difficult to see it as a statement about the band rising above detractors and finding strength within themselves." The photography for the album was done by Pamela Littky, and the sets on the album artwork were designed by Todd Fjelsted. Chuck Anderson of NoPattern designed the artwork for the album. A winged sheep named Franklyn is depicted on the cover of the album in a bedroom with the moon and stars in the background, while the inside of the CD booklet features "tarot card" designs with photos of each of the band members. Promotion for the album began in November 2006 with the band performing "This Ain't a Scene, It's an Arms Race" for the first time at the American Music Awards on November 21. The song
```

### Album 20, chunk 12

```text
was shipped to radio the same night as the performance. In the week following the performance, the single was the top added track at Pop and Alternative radio. While the song was the first song revealed from the album, it would not receive an official single release until January 2007. "The Carpal Tunnel of Love" was released as a digital single in December 2006. It was a minor hit in the United States, peaking at 81 on the Billboard Hot 100. The band then began the Friends or Enemies Tour in January 2007 to build interest in the album. The tour consisted of intimate club shows in fifteen cities throughout the United States, with New Found Glory, The Early November, Permanent Me and Lifetime. Two weeks before Infinity on High was released, the album was leaked online, which led to rumors on the band's message boards that the album would be released a week early. Although these rumors were incorrect, Fall Out Boy responded to the leak by including an exclusive live EP, Leaked in London, recorded in London's Hammersmith Palais at their sold-out show on January 29, 2007, with each purchase to encourage fans to buy the album. The EP could be downloaded from the band's website between Tuesday, February 6, 2007, and Tuesday, February 13, 2007, using CDPass software along with inserting a physical copy of Infinity on High into the CD-ROM drive of one's computer. Infinity on High was the final release from Rabid Neurosis, a warez
```

### Album 20, chunk 13

```text
organization responsible for leaking 20,000 albums before their release. On February 6, 2007, the day of the album's release, Fall Out Boy played three free shows, each in a different city in the United States. The day started with a morning performance in Times Square in New York City, followed by a gig in the band's hometown of Chicago, and then a late-night show in Los Angeles. In March 2008, Fall Out Boy attempted to enter The Guinness Book of World Records for being the only band to perform in all seven continents in nine months, planning to perform in Antarctica for an audience of scientists while working with Greenpeace to raise awareness about global warming. However, the group was unable to make the flight from Punta Arenas, Chile to Antarctica due to poor weather. Instead, Wentz and Stump went on to break the world record for the most interviews conducted by a duo in a 24-hour period, setting the mark at seventy-four. To promote the album after its release, Fall Out Boy embarked on an extensive tour schedule, with concerts across the United States, Canada, Australia, New Zealand, South Africa, Europe and Asia. It began with the 2007 Honda Civic Tour with Paul Wall, +44, The Academy Is..., and Cobra Starship. The tour was originally planned to begin on April 18, 2007, but the band decided to postpone the date until May 11, citing health issues and exhaustion. Wentz stated "It's a health issue, but not a health issue
```

### Album 20, chunk 14

```text
that anyone needs to worry about. It's not life-threatening, it's more about being overworked and worn down." In honor of the tour, the group designed a custom Honda Civic Hybrid which was given away to a fan in a contest. Wentz described the tour as "our biggest show ever", with Stump adding that "We've been working really hard to make this show look and sound the best it's ever been for Fall Out Boy." For a Kiss-inspired fan contest, Wentz's brother created prints of images based on the record, created with ink mixed with the band members' blood. The band gave away prints to winners at every stop on the Honda Civic Tour. Wentz hoped that the contest would serve to "[shed] some light on the much-needed support for blood drives." A live concert CD and DVD recorded at a show in Phoenix was later released in 2008, entitled Live in Phoenix. The band also headlined the Young Wild Things Tour, an international arena tour featuring Gym Class Heroes, Plain White T's and Cute Is What We Aim For. Of the thirty one dates, twenty nine were in the US with two in Canada. The tour was inspired by Maurice Sendak's 1963 children's book Where the Wild Things Are, and included sets designed by artist Rob Dobi containing images from the book. Commenting on the decision to incorporate elements from the book, Wentz explained "Where the Wild Things Are is a great narrative. It encapsulates pretty much every FOB song
```

### Album 20, chunk 15

```text
ever written: You know, tantrums and monster islands and all." Four songs were released as singles from the album's fourteen tracks, of which three charted on the US Billboard Hot 100 and all reaching international charts. Infinity on High was spurred on by the lead single "This Ain't a Scene, It's an Arms Race", which became the highest-charting song for band and their first to chart worldwide. Wentz commented on the band's decision to pick "This Ain't a Scene..." as a single, saying "There may be other songs on the record that would be bigger radio hits, but this one had the right message." It was sent to radio weeks before its digital release in January 2007; upon digital release the track debuted and peaked at number two on the Hot 100 where it stayed at that position for two consecutive weeks, spending nine weeks in the top ten. The single sold 162,000 digital downloads in its opening week, breaking various music industry records and becoming the highest debut of 2007. With this total it was the largest opening-week tally for a group since Nielsen SoundScan began tracking digital sales in 2003 and set a new record for the highest bow for a band since radio only titles joined the chart in 1998. It also reached number one on the defunct-Pop 100, number one on Billboard Digital Songs and came at number eight on Alternative Songs. Internationally, "This Ain't a Scene..." debuted and peaked inside the top ten of many
```

### Album 20, chunk 16

```text
charts. It reached number one in New Zealand, number two in the UK, number four and Platinum status in Australia, number four on the Canadian Hot 100 and in Ireland, and placed at number nine on the European Hot 100. "Thnks fr th Mmrs" was released as the second single in the US in March 2007. It peaked at number eleven on the Hot 100 with twenty-eight chart weeks before it was retired. It came at number five on Digital Songs, but performed weaker on the Radio Songs chart at number forty. It reached the two-million sales mark week ending December 27, 2009 in the US. Its highest charting was in Australia where it peaked at number three on the Australian ARIA chart and achieved Platinum status in the region. In New Zealand, the UK, Canada and Ireland "Thnks fr th Mmrs" reached the top twenty. ""The Take Over, the Breaks Over"" was released in August 2007 in the US as the third single and failed to chart on the Hot 100, although it did reach number 48 on the UK Singles Chart, with its highest position at number seventeen in Australia, becoming the third consecutive top twenty hit from Infinity on High in that region. The fourth and last single, "I'm Like a Lawyer with the Way I'm Always Trying to Get You Off (Me & You)" managed to reach number 68 in the US and made the top 30 in Australia. "The Carpal Tunnel of Love" was not
```

### Album 20, chunk 17

```text
an official single but it was released online by the band before Infinity's release and was later given as an exclusive download to iTunes; it managed to reach number eighty-one on the Hot 100. Critical response for Infinity on High was generally positive, with many praising Stump's vocals and the album's new musical direction. At Metacritic, which assigns a normalized rating out of 100 to reviews from mainstream critics, the album received an average score of 75, based on 23 reviews, which indicates "generally favorable reviews". Jody Rosen of Entertainment Weekly commended the band's "new sense of swing" on its R&B-influenced songs and noted that Stump "has evolved into a superb frontman." Dave de Silva of Sputnikmusic agreed about Stump's new vocal style, saying that "his tone is smoother and more well-rounded, he’s cut out the borderline screechy high-end which made parts of the previous album unlistenable and, though occasionally still nasally, his tones are far more varied and adaptable to different styles" as well as calling Wentz' lyrics "as sharp as ever". Andrew Blackie of PopMatters called the album "wildly exciting and experimental" and felt it greatly improved upon From Under the Cork Tree. Aaron Burgess of The A.V. Club enjoyed the disc's new pop direction and felt that the songs that were more typical of Fall Out Boy's original sound, such as "The Carpal Tunnel of Love" undermined the album's potential. Sven Philipp of Billboard called Infinity on High a "shamelessly melodic, wild and powerful pop record" and
```

### Album 20, chunk 18

```text
referred to Stump as the album's "true surprise". The album was ranked No. 38 on Q's 50 Best Albums of 2007. However, some critics felt that the album was overly ambitious and that the band's musical departure may alienate listeners. Chad Grischow of IGN felt that the album's dramatic hooks seem "bloated" at times: "The band does a great of focusing on what they do best, but the album does drown itself a bit with all the overwhelming enormity of it all." Scott Shetler of Slant disliked the "melodramatic" undertones of "I've Got All This Ringing in My Ears and None on My Fingers" and "Golden", writing "they don't handle that style quite as well as Panic! at the Disco". Cory Apar of AllMusic opined that the album's pop direction contradicts the band's lyrical claims of wishing to stick to their roots. He called the album's various styles "hit and miss", yet commented that "Once Infinity on High sinks in, it's indeed a fun record. But for a band that was once so self-assured and able to utilize its talents so compellingly, the album is regrettably haphazard." Caroline Sullivan of The Guardian believed that the album was overly sullen, but noted that "They may not be happy, but they haven't forgotten to be catchy." Barry Nicholson of NME found the number of guest producers to be unnecessary and disliked some of the songs, but admired the album's "infectious" nature. Infinity on High was a major commercial success, debuting at number
```

### Album 20, chunk 19

```text
one on the US Billboard 200 chart, with first week sales of 260,000 copies in the United States, according to Nielsen SoundScan. As of February 2013, Infinity has sold 1.4 million copies in the US. It was the band's first US number one album and second consecutive top ten effort, as its previous release, From Under the Cork Tree, peaked at number nine. The album spent its first six weeks in the top ten, out of a total of fifty two chart weeks. Infinity on High also opened at number one on Billboard's Rock Albums, Tastemaker Albums, and Digital Albums charts, with over 27,000 digital sales making up the total first week tally. In its second week, it fell to number five on the Billboard 200, selling 119,000 copies with a 54% decline during a post-Grammy week. The album rose to number three in its third week with 79,000 units sold. In its fourth week, the disc slipped to number four and sold 67,000 copies. Infinity on High's sales again fell in its fifth week, moving 58,000 copies and descending to number eight on the chart. In its sixth and last week in the top ten it fell to number nine and sold 43,000 copies. In April 2007, the album was certified Platinum by the Recording Industry Association of America (RIAA), denoting the shipment of one million copies. It finished the year at number twenty-one on IFPI's list of the "Top 50 Global Best Selling Albums of 2007". Infinity on
```

### Album 20, chunk 20

```text
High has shipped over two million copies worldwide. The album also charted inside the top five worldwide, making it the band's most successful and breakthrough album internationally. Infinity on High charted all over Europe, debuting at number eight on Billboard's European Albums chart. In Australia, it debuted at its peak of number four on the Australian ARIA Albums Chart. It remained on the Australian chart for a total of fifty weeks, spending its first seven weeks in the top ten. In its 31st chart week it broke into the top ten again where it remained for another six weeks in a row, accumulating a total of thirteen weeks in the top ten. The CD was certified Double Platinum by the Australian Recording Industry Association (ARIA), denoting shipments of 140,000 copies. Infinity on High debuted at number one in New Zealand, and remained at the top position for six consecutive weeks, logging a total of thirty-seven chart weeks, making it the fifth longest chart sitter on the New Zealand charts in 2007. After marking its first twelve weeks in the top ten, it went on to spend a combined total of twenty-six weeks inside the top twenty and received a Platinum accreditation from the Recording Industry Association of New Zealand (RIANZ) for 15,000 shipments. In the United Kingdom, the album debuted at number three with 64,054 first week sales and made nine weeks in the top twenty, being certified Platinum by the British Phonographic Industry (BPI) for 300,000 units shipped. It
```

### Album 20, chunk 21

```text
went on to sell 446,807 in the UK to date January 2015. The album debuted at number two in Canada with 21,000 first week sales. Infinity was certified Platinum by Music Canada for shipments of 100,000 units. In Ireland, the record peaked at number six according to the Irish Recorded Music Association with fourteen weeks within the top twenty, and also went Platinum there. After entering the French albums chart at number 64, Infinity on High reached its peak of number 17 and held on for 64 weeks in the top 150.
```

## Album 21: System of a Down — System of a Down

- **album_id:** `fb12f1ec-5a35-4056-a037-1f040f6d4642`
- **Tags (identification only):** alternative metal, nu metal, metal, angry, avant garde metal, heavy, manic, political
- **Chunks:** 2 (361 words)

### Album 21, chunk 1

```text
System of a Down is the debut studio album by the American heavy metal band System of a Down, released on June 30, 1998, by American Recordings and Columbia Records. The album was certified Gold by the Recording Industry Association of America in February 2000. After the success of the band's following album, Toxicity (2001), System of a Down was certified platinum and has since gone double platinum. In 2022, Eli Enis of Revolver included the song "Suite-Pee" in his list of the "10 Heaviest Nu-Metal Songs of All Time". In 2025, Rae Lemeshow-Barooshian of Loudwire included the album in her list of "the top 50 nu-metal albums of all time", ranking it third. The album is generally considered nu metal and alternative metal, frequently utilizing low guitar tunings such as drop C. The song "Suite-Pee" is a criticism of pedophilia within the Catholic Church and religious extremism. "Sugar" is about the world's population's over use and reliance on drugs and other substances, as well as the predatory state of media like the news, while "P.L.U.C.K" is about the Armenian genocide. The cover artwork is from a 1928 anti-fascist poster designed by visual artist John Heartfield for the Communist Party of Germany. The text on the original poster translates as: "A hand has 5 fingers! With these 5 grab the enemy!" This slogan inspired part of the text contained on the back of the album: "The hand has five fingers, capable and powerful, with the ability to destroy as well
```

### Album 21, chunk 2

```text
as create". Later, it is written in bold letters: "Open your eyes, open your mouths, close your hands and make a fist." Serj Tankian later reused the phrase in the song "Uneducated Democracy" from his 2012 album Harakiri. System of a Down received acclaim from music critics. Q called it "an excellent starting point for this most curious band". The album is featured in the book 1001 Albums You Must Hear Before You Die. Loudwire included the album in its list of The Best Metal Debut Albums, at number 22. Serj Tankian – lead vocals, keyboards, samples Daron Malakian – guitars, backing vocals Shavo Odadjian – bass John Dolmayan – drums
```

## Album 22: Harmlessness — The World Is a Beautiful Place & I Am No Longer Afraid to Die

- **album_id:** `00a46abb-8d90-41c8-823a-247c22f4ab2e`
- **Tags (identification only):** emo, indie, indie rock, post hardcore, post rock, punk, alternative, atmospheric
- **Chunks:** 2 (339 words)

### Album 22, chunk 1

```text
Harmlessness is the second studio album by American indie rock band The World Is a Beautiful Place & I Am No Longer Afraid to Die. It was announced on August 4, 2015, and was released on September 25, 2015. The title of the album is a play on the name of the band's first EP, Formlessness. Harmlessness charted at number 11 on the Heatseekers Albums chart, and at number 46 on the Independent Albums chart. Upon release, the album received critical acclaim. At Metacritic, which assigns a normalized rating out of 100 to reviews from specialized critics, the album received an average score of 84, based on 6 reviews. Stereogum placed the album at number 13 on their top 50 albums of 2015 list. James of Stereogum wrote: "It's not the kind of music that will change the world, but it might just change your life." Aaron Mook of AbsolutePunk wrote: "Harmlessness is ambitious and intimidating in scope; it is not an easy listen, but with the right amount of time and dedication, it is easily one of the most rewarding listens of 2015." "January 10th, 2014" appeared on a best-of emo songs list by Vulture. In 2017, Harmlessness placed seventh on Spin's list of the emo revival's 30 best albums, with writer Ian Cohen dubbing it "one of the most stunningly accomplished indie rock records of the past decade." Several months later, Cohen called it "an astonishing redirection" for indie rock, seeing it anticipate the genre's impending fusion of
```

### Album 22, chunk 2

```text
the late 90's Pacific Northwest scene's "experimental and expanse" with mid-00s Canadian indie's "grandeur" that would give way to the emo revival. In 2021, Exclaim!'s Adam Feibel wrote that the album had "frequently been held up as [the band's] crowning achievement". David Bello - vocals Nicole Shanholtzer - guitar, vocals Josh Cyr - bass guitar, acoustic guitar Katie Dvorak - synthesizer, vocals Steven Buttery - percussion Chris Teti - production, engineering, mixing, guitar, vocals, percussion Nick Kwas - violin Tyler Bussey - guitar, banjo, vocals Greg Horbal - guitar
```

## Album 23: Does Humor Belong in Music? — Frank Zappa

- **album_id:** `e2984707-4fc5-4205-9f2b-ddf39f1c01fa`
- **Tags (identification only):** jazz, rock, 1986, art rock, avant garde, avantgarde, comedy rock, experimental
- **Chunks:** 1 (284 words)

### Album 23, chunk 1

```text
Does Humor Belong in Music? is a live album by American musician Frank Zappa. The title comes from a question Zappa was asked while being interviewed by Dave Tarbert (The Man on Music) a reporter from television station WEWS in Cleveland, Ohio. The album features concert recordings from October–December 1984. It was the first album by Zappa to be released on CD only (although it was bootlegged on vinyl for listeners who did not own CD players). In 1995, it was reissued by Rykodisc in an extremely remixed form, with significantly improved dynamic range and new artwork. The 1995 edition includes an extra minute of percussion effects during "Let's Move to Cleveland" that had been excised from the EMI edition. In 2012 the (remixed) album was reissued as a part the Zappa Reissue Program. It was a part of "The 4th set of 12" released on October 30, 2012 and featured the original artwork without the white stain in the bottom left. A home video (later reissued on DVD) of the same name was released. "Zoot Allures", "Tinsel Town Rebellion", "Trouble Every Day" and "Whipping Post" appear on both, but are different performances. Fragments of "Hot-Plate Heaven" also appear in the video (with only the verses of the song left intact). The cover art of the original CD release and video release, however, are the same. Frank Zappa – lead guitar, vocals Ray White – rhythm guitar, vocals Ike Willis – rhythm guitar, vocals Bobby Martin – keyboards, saxophone, vocal, french horn Allan Zavod – keyboards, solo on "Cleveland" Scott Thunes – bass guitar Chad Wackerman – drums, solo on "Cleveland" Dweezil Zappa – lead guitar on "Whipping Post" Frank Zappa – producer, arranger
```

## Album 24: A Shipwreck in the Sand — Silverstein

- **album_id:** `908af8c8-3e17-4a53-97da-e5203a6fab0f`
- **Tags (identification only):** emo, post hardcore, alternative/indie rock, pop/rock, punk, rock, screamo
- **Chunks:** 5 (1213 words)

### Album 24, chunk 1

```text
A Shipwreck in the Sand is the fourth studio album by the Canadian post-hardcore band, Silverstein, released March 31, 2009 through Victory. Although not as an official member, this marks the first album to feature future guitarist Paul Marc Rousseau (who would later go on to replace guitarist Neil Boshart), providing group vocals, among others. It was their final studio album and second to last release on Victory after completing their four-album contract, with their 10-year anniversary live album, Decade (Live at the El Mocambo) being their last release on the label a year later. A Shipwreck in the Sand was recorded at Metalworks Studios, in Mississauga, Ontario, Canada, with producer Cameron Webb, who also engineered and mixed it. Silverstein returned to Discovering the Waterfront (2005) producer Cameron Webb, after being disappointed with the recording process of their previous album, Arrivals & Departures (2007), which was produced by Mark Trombino. Mixing took place at Maple Studios in Santa Ana, California, U.S. Sergio Chavez provided additional engineering, while Kevin Dietz was assistant engineer at Metalworks Studios. The album was mastered by Brian Gardner at Bernie Grundman Mastering. The album features a much heavier sound. With some tracks that are soft, it also has some very heavy tracks and is considered their heaviest album. The album contains influences from post-hardcore, emo, hardcore punk and heavy metal. The album features a conceptual storyline, written by lead vocalist Shane Told. Prior to the release of the album, an official album website was revealed, which
```

### Album 24, chunk 2

```text
told the tale of a vessel which set sail to find resources, and begin a new world, but when no new land is to be found, the crew revolts and turns against their captain. As time passed by, there was no new land to be found. As the days grew shorter, and the nights grew longer and colder, the crew became more and more skeptical about the captain's vision. Originally passionate and committed, true and faithful, they now began to revolt. The website also carried the tagline, "Betrayal. Arson. Infidelity. True Love.". The album is divided into four chapters: It Burns Within Us All (tracks 1–3), Liars, Cheaters and Thieves (tracks 4–7), Fight Fire with Fire (tracks 8–10), and Death and Taxes (tracks 11–14). Upon release of the album, it was revealed the story of the ship and its captain was a metaphor of betrayal, similar to that faced by the protagonist in the main storyline. Alongside the main storyline, some songs tackle individual issues, such as "Born Dead", which talks about the problems with the American health system. "The protagonist of the story is sick, terminally ill, and can't get health care," says Told. "That's a big reason for the problems that he's facing in his life." The track, "We Are Not The World" attacks the government and the problems of war. In an interview filmed for the Decade (Live at the El Mocambo) live album, Shane Told states the following; The concept of the record "The Shipwreck In
```

### Album 24, chunk 3

```text
The Sand" is complicated, and there's a lot of stuff going on. And I like that about it, that it is not obvious and that a lot of people can take something out of it that's their own. The reason I wanted to do a concept record was because of the way the world is right now, with the economy being messed up, people losing jobs and families losing their life savings, and not knowing what they are going to do in the future. Ten years ago, everything was going so well, people were not as concerned and now it's a really scary time. There's a lot of underlying political issues within the record about what governments all over the world are spending money on, what their focus is on. There's also a lot of social issues I wanted to talk about as well; people that watch reality TV and think Cribs is the way their house needs to look or they need to look like people from a Cosmopolitan magazine. There's just so many problems that face society right now and I really wanted to tackle them all. Each song just dives into a different issue; you know the issue of health care right now in America, and how it's so divided when it should be so obvious. On October 3, 2008, the band posted a demo titled "Broken Stars" online. The song was originally written during the sessions for the band's previous album, Arrivals & Departures. In October
```

### Album 24, chunk 4

```text
and November, the band went on a co-headlining tour of the US with Chiodos. They were supported by Escape the Fate. On January 28, 2009, the album's track listing and artwork was revealed. The following day, the accompanying story to the album's concept was revealed. In February, the band went on a Brazilian tour, followed by a tour of Australia as part of the Soundwave festival in February and March. On March 5, the band posted a clip of new track, titled "Vices". On March 15, they posted a clip of "Born Dead". On March 17, they shot a music video for "Vices" with director Robby Starbuck. On March 19, the band posted a clip of "American Dream". On March 23, "Vices" was posted on the group's Myspace profile. The following day, the album was made available for streaming on Myspace, before being released on March 31 through Victory Records. A CD/DVD version was also released. In March and April, the band went on a tour of the US alongside Norma Jean, Blessthefall and Before Their Eyes. Norma Jean left the tour in early April and were replaced by A Static Lullaby. Further dates were added, extending the tour into May, prior to an appearance at The Bamboozle and Slam Dunk festivals. In June and July, the band went on performed a handful of shows in Canada and the US. The Canadian dates were played with I Am Committing a Sin and Desperate Union, while the US dates were with
```

### Album 24, chunk 5

```text
Poison the Well, the Sleeping and Oceana. Following this, the band performed two stints on Warped Tour in mid-July and mid-to-late August. In October and November 2009, they embarked on another US tour, with support from Madina Lake, I See Stars and the Word Alive. On May 19, 2010, a music video was released for "American Dream". A Shipwreck in the Sand received mainly positive reviews from music critics and fans alike. It peaked at number thirty three on the Billboard 200 album chart, a position higher than 2005's Discovering the Waterfront, however not reaching the height of its predecessor, Arrivals & Departures. Daniel Thompson of Music Emissions suggested the album "may very well be the band's best album to date", and praised the diversity of musical styles present on the album, however criticized the repetitiveness of the lyrics stating, "it gets annoying hearing about the same thing in every song". Drew Beringer of AbsolutePunk also gave a mainly positive review, calling it an "enjoyable, catchy album that digs deeper than most bands in its genre", giving the album an overall rating of 77% and saying although "musically, the album doesn’t implement a new sound or direction" it is "a refinement and polishing of the things the band has tried over the years".
```

## Album 25: Rocks — Aerosmith

- **album_id:** `57622677-17cf-4808-bcc2-fecf01a8b5ea`
- **Tags (identification only):** hard rock, rock, album rock, arena rock, blues rock, 70s, classic rock, contemporary pop/rock
- **Chunks:** 12 (3010 words)

### Album 25, chunk 1

```text
Rocks is the fourth studio album by American rock band Aerosmith, released on May 13, 1976, through Columbia. AllMusic described Rocks as having "captured Aerosmith at their most raw and rocking." Rocks was ranked number 366 on the updated Rolling Stone's list of the 500 Greatest Albums of All Time in 2020. It has influenced many hard rock and heavy metal artists, including Guns N' Roses, Metallica, and Nirvana. The album was a commercial success, charting three singles on the Billboard Hot 100, two of which reached the Top 40 ("Back in the Saddle" and "Last Child"). The album was one of the first to ship platinum when it was released, and has since gone quadruple platinum. Previously, Aerosmith had recorded three albums: Aerosmith (1973), Get Your Wings (1974), and their breakthrough Toys in the Attic (1975), which produced the hits "Walk This Way" and "Sweet Emotion". Although often derided by critics, the band had amassed a loyal fanbase from relentless touring and their ferocious live shows. Producer Douglas explains, "The only thing we were talking about a few months before Rocks was that it was going to be a real hard-rock album. And we might go back to the format of the first album, which was to rock out on every tune. And again, keep it real raw. And make it as live sounding as we possibly could." By the time of the album's sessions, the group had already begun living the rock-and-roll lifestyle to the hilt, indulging their
```

### Album 25, chunk 2

```text
already considerable appetite for drugs. However, their hedonistic lifestyle did not appear to hamper them creatively; Rocks was considered by many fans, critics, and fellow musicians to be one of the highlights of their career. Guitarist Joe Perry later recalled, "There's no doubt we were doing a lot of drugs by then, but whatever we were doing, it was still working for us." In the 1997 band memoir Walk This Way, guitarist Brad Whitford states that the band began work on the album by backing the Record Plant's mobile recording truck into their rehearsal space, named the Wherehouse, and "let fly ... We were living the high life and not paying attention to anything except making this record. I had the beginnings of "Last Child" and "Nobody's Fault." Tom had "Uncle Tom's Cabin" that became "Sick as a Dog." We had 'Tit for Tat' ... which turned into 'Rats in the Cellar.' We cut all the basic tracks except two there." Producer Jack Douglas later insisted: Rocks was the album where Tom and Brad had a lot more input and songs ... This was a big album for Aerosmith. It had to make a big statement about how loud and hard they were, how unapologetic they felt about being who they were – this brash, rude, sexual, hard-core rock band. The album's opening track, "Back in the Saddle" was written by Perry on six-string bass. In 1997, Perry explained to Alan Di Perna of Guitar World that he was inspired
```

### Album 25, chunk 3

```text
by Peter Green to write the riff on a Fender Bass VI and admitted that he was "very high on heroin when I wrote 'Back in the Saddle.' That riff just floated right through me." He further describes it as "the kind of riff and instrumentation that falls outside the normal formula of a rock song. I wrote it on a six string bass. It was one of those songs that really opened things up for us." Tyler explains that the song uses the "saddle image as a way of saying, 'Here's another album, folks, and we're gonna rock out and I've really got my spurs on'." He continues in his memoir, "Back in the Saddle" I hoped would be nostalgic, hearkening to the spirit of every Spaghetti Western I ever saw. The band played like the gods they were. Jack mixed it with Jay in the way you hear it today." "Last Child" is credited to guitarist Brad Whitford and Tyler. Tyler explains, "Brad wrote, 'Take me back to sweet Tallahassee, home sweet home…'" recalled Tyler. "Whatever he put into 'Last Child', that's his moment. He can take that, and that's his, forever." The song evolved from a riff Whitford titled "Soul Saver", a recording of which was released on Pandora's Box in 1991. "Sick as a Dog" is credited to Tyler and Tom Hamilton. The bassist explains, "I think I came up with the verse part first. And then I did the parts for the intro, the B
```

### Album 25, chunk 4

```text
to E part, and then came up with this little, jangling arpeggio thing ... I'm such a Byrds fan; it comes from that." As Hamilton later remembered, it was "Mr. Tambourine Man" that was especially influential on him personally when it came to his eventual contributions to the song that became "Sick as a Dog." "It really embedded in my mind that love of hearing [guitar sounds like that], especially when it was combined with a hard rock beat. Perry shared how they ended up dividing things up instrumentally in the studio: "Tom played rhythm guitar on "Sick as a Dog." I played bass for the first half of the song. Then I put the bass down and played guitar in the end, and Steven picked up the bass and played it for the rest of the song – all live in the studio! One take. Hamilton remembers Douglas' assistance in developing the song: "Jack is a very open person. He always has time for what people come up with. "Sick" started on guitar and I wasn't sure about it but playing it for Jack, I realized it had a lot of potential. We recorded it last, and I'm glad because everybody was hot then." "Rats in the Cellar" evolved from Fleetwood Mac's "Rattlesnake Shake", a staple of the band's early setlists. In his memoir, Tyler states that the title "Rats in the Cellar" is a "tip of the hat, or an answer to 'Toys in the Attic' ... Meanwhile,
```

### Album 25, chunk 5

```text
in real life, 'Rats' was more like what was actually going on. Things were coming apart, sanity was scurrying south, caution was flung to the winds, and little by little the chaos was permanently moving in." "Nobody's Fault" remains a favorite of the band's, with Tyler calling it "one of the highlights of my creative career" and Kramer insisting "it's some of the best drumming I did." According to Tyler, the lyrics: "have to do with earthquakes, which we were scared of, along with flying". "Lick and a Promise" is about the band's determination to deliver a rocking live show. "Combination" features Perry sharing lead vocal duties with Tyler for the first time, and the guitarist admitted in 1997 that the song was "about heroin, cocaine, and me". In his memoir, Tyler calls the line "Walkin' on Gucci wearing Yves St. Laurent/Barely stay on 'cause I'm so goddamn gaunt" the best lyric Perry ever wrote: "It was the truth, it was clever, and it described us to a tee". Regarding his vocal on the song, Perry later commented, "This was touchy because singing was Steven's jealously guarded territory ... Beyond that, anytime the spotlight shone on me I detected a bit of jealousy from the other guys. After a while, though, the band came around and supported me, as long as I sang the song as a semi-duet with Steven." "Home Tonight" features Tyler on piano, Perry on a lap steel guitar as a lead guitar and his Les Paul
```

### Album 25, chunk 6

```text
for the rhythm guitar, and has drummer Joey Kramer, Tom Hamilton, and producer/arranger Jack Douglas performing backing vocals. Of the song Perry recalled, "Steven could always be counted on to come up with some little piano riff that would be our ballad for the record. And that was it." Unlike their previous two records, which were recorded at the Record Plant studios in Manhattan, for Rocks, the group rented a rehearsal space in suburban Massachusetts, the Wherehouse and employed a mobile studio to cut the record. Backing tracks for six of the songs were completed at the Wherehouse. Douglas explains: "It's the one record, of all the records that I've done, where every element is right and in its place. Every lyric, every key, every sound. Everything is right about that record, for what it is. Because it was written and conceived and recorded in the same place, in A. Wherehouse in Waltham, Mass. So we had the place where they used to rehearse. It was done in the dead of winter, and they would come in to record with nothing but a few licks...and we would develop these tunes." He continues, "we cut all the basics at their rehearsal space, the Wherehouse, in Boston's suburbs. A big, metal, roaring, huge room. I used stage monitors in with them to blow the sound right back at them. And that's when they started to stretch out. Joe would ask what he ought to be listening to and I'd hip him to
```

### Album 25, chunk 7

```text
John Coltrane for solo ideas - and he'd try to get that! Even in pre-production, I knew it was great. I have cassettes of the evolution of every song on that record, and you should hear "Back In The Saddle" as it evolved from Joe's basic lick to the monster it became. Wanna know what the secret to Rocks was? Distortion. Everything is totally over-loaded. When I brought it to the record company, they panicked at first, but not for long." At the end of February 1976, the band resumed sessions at the Record Plant to complete the remaining backing tracks and record vocals for the album. Writing lyrics for the songs proved to be the most difficult stage in the album's production. Douglas explains, "Steven moves in with me when we're working on an album. In the morning, I wake him up with a cassette and a cup of coffee; most of the melody lines have all been worked out and he's singing phonetically. I'll suggest a thing to him here and there, give him a kick this way and he starts to come around. He's really the main drive of the band" "Back in the Saddle" features the sound of a whip by whirling a thirty-foot cord in the middle of six Neumann mikes and adding a cap gun for the cracking sound effect. A real bullwhip was intended to be used for the whip effects and hours were spent trying to get it to crack. The band
```

### Album 25, chunk 8

```text
members ended up cut up and hurt without making any progress. The first verse features the sound of clinking spurs, which was actually produced using bells and tambourines strapped to Tyler's cowboy boots by Perry and New York Dolls singer David Johansen. The song is also notable for the slow buildup of the drum beat and guitar riff in the beginning of the song, as well as the sound effects of a galloping horse. Tyler achieved the hoofbeat sound using coconuts from a percussion kit he ordered from SIR Studio Instrument Rentals. Producer Douglas acknowledges the pervasiveness of drug use during the album's sessions: "Labels were giving them drugs. It was written into the project, and in the case of Columbia, they had guys who delivered it to you. And they finally got busted for that, people lost their jobs and it became a huge scandal. Columbia Records: If they could keep you doing coke, then the records would get done faster. That was their philosophy. And you know, for those guys, they did quite a bit. But then you gotta come down, and you gotta find something to come down with. So it's either pills or heroin. So through Toys, everything was fine, it was working. Rocks, that's a pretty drug-fueled record, but it was really working. It was a dark record, too." Bassist Tom Hamilton remembers the dangers, "There is something about being high that makes you look at things differently. But that period for some people can
```

### Album 25, chunk 9

```text
be relatively short. I think [drugs] all gave us energy and concentration. It was beneficial for a while. But in a few years it became so destructive. It was just so awful. We worked hard to be able to play with feelings and really tight, and then after Rocks, it fell apart. We started making a lot of money, and that was the beginning of the end." Douglas expresses his satisfaction with the album's production and sound: "Rocks was done in Waltham, Massachusetts, in a warehouse. The keys the songs were written in were all dependent on the environment we were in. After a couple of weeks of rehearsal, the room started to sound really good. The very thought of moving it out of that room seemed like it would destroy everything about where we were. It was 100 percent written in the room—not including the lyrics because the lyrics always came last—but Steven's melodies. That record, when I put it on, sounds like truth. To this day, I still feel that that album is closest to a really true statement and it was because the environment in which it was written was the same environment in which it was recorded." Perry remembers, "With Rocks we had more confidence. We still had to write stuff on the spot, but that was the one where we had more of a handle on the creativity. Not to say that the pressure wasn't on. We were touring constantly, we only took time off
```

### Album 25, chunk 10

```text
to go in the studio. No one said: 'Take a month off, go write some songs.' It was like: 'Go in the studio with whatever ideas you have.' That was how it was. Toys was kind of the softball album, and Rocks was the one were we felt: 'Wow, we're there'." Contemporary reviews were mixed. John Milward of Rolling Stone wrote that "the material is Rocks’ major flaw, mostly pale remakes of their earlier hits"; concluding that the return to the "ear-boxing sound" of Get Your Wings and Tyler's vocal performance cannot save the album from mediocrity. In The Village Voice, Robert Christgau wrote that Aerosmith were doing a good job of imitating Led Zeppelin, and that after this album the band began to lose steam. Modern reviews are very positive. Greg Prato of AllMusic describes Rocks as "a superb follow-up to their masterwork Toys in the Attic" that captures "Aerosmith at their most raw and rocking". He writes that "Back in the Saddle and Last Child are among their most renowned songs, but all the tracks prove essential to the makeup of the album". Ben Mitchell of Blender said that the members' drug use actually helped Rocks. He also called the album "raw." On November 24, 1994, Los Angeles Times review of Rocks, Jon Matsumoto opined that the record "arguably is the best heavy metal opus ever concocted". Canadian journalist Martin Popoff described the album as "a screamin' mercury-shattering rock festival, live, overblown, decadent, and very American", concluding that
```

### Album 25, chunk 11

```text
"on Rocks the band's talent is anything but wasted." Many musicians have cited Rocks as a favorite: Rocks was one of Kurt Cobain's favorite albums, as he listed in his Journals. In 2003, the album was ranked number 176 on Rolling Stone magazine's list of The 500 Greatest Albums of All Time, maintaining the rating in a 2012 revised list, before it was dropped to 366 in a 2020 revised list. Mötley Crüe songwriter and bassist Nikki Sixx refers to Aerosmith frequently in his book The Heroin Diaries. Metallica leader James Hetfield has identified Rocks, as well as Aerosmith, as important influences in his music, stating that the band was the reason why he wanted to learn guitar. Slash says Rocks was the album that inspired him to learn guitar, and that the album changed his life: I was in seventh grade and just going through the whole 1978 music thing that was happening for kids – which was like Cheap Trick and the Cars. Anyway, there was this chick that I was going after that was considerably older than me ... I'd been trying to be cool enough to take her out and have my way with her ... Finally, I sort of weaseled my way into her apartment. So we're hanging out and she put Rocks by Aerosmith on, and I was mesmerised by it. It was like the be-all-and-end-all, best-attitude, fuckin' hard rock record ... I'd grown up with music, but this was like my record. I
```

### Album 25, chunk 12

```text
must have listened to it about half a dozen times, completely ignored her, and then got on my bike and rode. I was totally in there. I was at least gonna get a decent French kiss out of it, and I completely dropped the ball for Aerosmith, and that was that. It's probably one of the records that sums up my taste in hard rock bands to this day. Meanwhile, she's out there somewhere and I missed it. But it was worth it. In his autobiography Rocks, Joe Perry states the driving purpose of Rocks "was to reidentify us as America's ultimate garage band, with blistering guitars, blistering vocals, balls-to-the-wall smash-your-eardrums production ... The cover showed five diamonds, one for each of us. We saw that record as a jewel, the culmination of all our angst and anger and excitement and joy as go-for-broke rock and rollers." Steven Tyler — vocals, bass guitar on "Sick as a Dog" (outro only), piano on "Home Tonight" Joe Perry — guitars, vocals, six-string bass on "Back in the Saddle", bass guitar on "Sick as a Dog", co-lead vocals on "Combination", lap steel guitar on "Home Tonight" Brad Whitford — guitars (except "Sick as a Dog") Tom Hamilton — bass guitar (except "Sick as a Dog"), guitar on "Sick as a Dog", backing vocals on "Home Tonight" Joey Kramer — drums, percussion, backing vocals on "Home Tonight" Paul Prestopino – banjo on "Last Child" Jack Douglas – producer, arrangements, backing vocals on "Home Tonight" Aerosmith – production, arrangements David Hewitt – remote truck director
```
