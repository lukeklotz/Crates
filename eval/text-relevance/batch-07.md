# Embedding text relevance, batch 7 of 12 (albums 151–175 of 300)

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

This batch: **25 albums, 113 chunks**.

## Album 151: Treasure — Cocteau Twins

- **album_id:** `76adcd65-6453-4827-a02e-6b2d38895b0d`
- **Tags (identification only):** dream pop, ethereal wave, ethereal, rock, darkwave, post punk, gothic rock, misc
- **Chunks:** 3 (723 words)

### Album 151, chunk 1

```text
Treasure is the third studio album by Scottish rock band Cocteau Twins, released on 12 November 1984 by 4AD. With this album, the band settled on what would, from then on, be their primary lineup: vocalist Elizabeth Fraser, guitarist Robin Guthrie and bass guitarist Simon Raymonde. The album also reflected the group's embrace of the distinctive ethereal sound with which they became associated. The album reached number 29 on the UK Albums Chart, becoming the band's first UK Top 40 album, and charted for eight weeks. It also became one of the band's most critically successful releases, although the band considered it underdeveloped. The track "Lorelei" became a minor dance hit during the mid-1980s. The album was recorded from August to September 1984 at Palladium Studios in Edinburgh and at Rooster in West London. Record label executive Ivo Watts-Russell originally tried to hire Brian Eno and Daniel Lanois to produce the album. However, Eno felt the band did not need him and Guthrie ended up producing the album. Pitchfork noted that the album's drum machine backing added a sharp edge in contrast to the band's ethereal sound and Elizabeth Fraser's "angelic vocals". On the album's title, Fraser said, "I thought it was a really good idea because I thought, well, what are people gonna see in these names? They're gonna realise it’s got nothing to do with mythology and all that bollocks. Well, it's not bollocks, but I foolishly thought people wouldn't think that we were into that sort of
```

### Album 151, chunk 2

```text
thing". Treasure is considered by many fans to be the band's finest work, and has received critical acclaim. Upon its release, Smash Hits Ian Cranna gave the album an 8 out of 10 rating, finding Cocteau Twins on their third album in a "noticeably lighter mood. The songs are airier, almost swinging, with more delicate acoustic guitar than the familiar electric razzle" and noting Elizabeth Fraser's vocals that "soars, weaves or whispers through the instrumental mix (,,,) to build beguiling, impressionist pieces based on vaguely Victorian names." Steve Sutherland in Melody Maker described the album as "true brilliance" and stated that the band were "the voice of God". Retrospectively, Pitchfork wrote, "Cocteau Twins' third album was titled simply enough. Treasure was an adjective for the endlessly inventive melodic lines you'd find buried in these songs, and a verb for what you'd do with them for years to come", and noted that the record signalled the start of Cocteau Twins' "signature ethereality". Ned Raggett of AllMusic complimented its "accomplished variety", saying, "Treasure lives up to its title and then some as a thorough and complete triumph". BBC Online wrote, "Treasure was where the Cocteau Twins first got it 100 percent right". In March 2018, the album was repressed on 180g vinyl using new masters created from high definition files transferred from the original analogue tapes. Jeff Terich of Treblezine placed the album on his list of best dream pop albums, stating: "In contrast to the band's more abrasive post-punk albums that
```

### Album 151, chunk 3

```text
arrived earlier, Treasure is an exercise in making beauty seem alien, and making alienation seem sublime, for that matter". Slant Magazine listed the album at No. 74 on its list of the best albums of the 1980s, while NME named Treasure the 37th best album of 1984. Pitchfork listed Treasure as the 27th best album of the 1980s. Paste magazine's Josh Jackson listed the album at No. 38 on his list of "The 50 Best Post-Punk Albums", describing it as "the first full realization of the band's ethereal pop sound". PopMatters included it in their list of the "12 Essential 1980s Alternative Rock Albums" saying, "Fraser's ability to deliver her nonsensical lyrics with the diaphanous touch of a moth or with the muscle of a ravenous lion is astonishing". Jennifer Makowsky concluded that "Treasure is an aptly titled album". The album was included in the 2008 edition of 1001 Albums You Must Hear Before You Die. In Beautiful Noise, the shoegaze/dream pop documentary, Robert Smith of the Cure calls it one of the most romantic records ever recorded, so much that he played it as he was getting ready on his wedding day. Music critic Jim DeRogatis called Treasure the "strongest" of the band's early releases. Elizabeth Fraser – vocals, production Robin Guthrie – guitar, keyboards, production Simon Raymonde – bass guitar, production
```

## Album 152: The Ultimate Sin — Ozzy Osbourne

- **album_id:** `b96b87ae-aade-47af-b5ef-3a382164fac2`
- **Tags (identification only):** heavy metal, album rock, hard rock, metal, 80s, glam metal, rock
- **Chunks:** 3 (642 words)

### Album 152, chunk 1

```text
The Ultimate Sin is the fourth studio album by the English heavy metal singer Ozzy Osbourne, released on 24 January 1986. It is the second and last of Osbourne's albums to feature lead guitarist Jake E. Lee, the first to feature drummer Randy Castillo, and the only album to feature bassist Phil Soussan, who co-wrote the album's hit single "Shot in the Dark". It is also Osbourne's last album to feature his classic logo on the cover until 2010's Scream. The album was awarded Platinum status in May 1986 and was awarded Double Platinum status in October 1994 by the RIAA. Upon returning from the Betty Ford Center in 1985 where he had undergone treatment for substance abuse, Osbourne was presented with a substantial quantity of music written by guitarist Jake E. Lee. After having been cheated out of his writing and publishing claims for Osbourne's previous album, 1983's Bark at the Moon, Lee says this time he refused to contribute anything until he had a contract in front of him guaranteeing his writing credit and publishing rights. Much of this music would form the basis of the album. The album's lyrics were largely written by long-time Osbourne bassist and lyricist Bob Daisley. The album was Osbourne's first to not feature bass playing from Daisley. Daisley left the band prior to recording after having a disagreement with Osbourne, prompting the auditioning of Greg Chaisson. While he liked Chaisson’s playing, Osbourne decided his image did not fit the band; Chaisson would
```

### Album 152, chunk 2

```text
reunite with Lee a few years later in Badlands. Phil Soussan was ultimately hired just before recording commenced. At first, Daisley was not credited for his songwriting contributions on the initial 1986 pressing of the album, though Daisley did receive credit on subsequent pressings. Future Y&T, Suicidal Tendencies and Megadeth drummer Jimmy DeGrasso worked with Lee and Daisley on demos for the album, but this version of the band fell apart due to Osbourne's commitment to the Black Sabbath summer 1985 reunion concert at Live Aid; Castillo and Soussan ultimately replaced DeGrasso and Daisley once recording commenced. The working title for the album was Killer of Giants after the album's song of the same name. Osbourne opted to change the title to The Ultimate Sin at the last minute. On 1 April 1986, a live performance promoting the album in Kansas City, Missouri, was filmed and released later that year as the home video The Ultimate Ozzy. In 1987, after the various tours in support of the album had concluded, guitarist Lee was unexpectedly fired by Osbourne's wife and manager Sharon. The specific justification for Lee's dismissal remains unknown. Bassist Soussan also departed, with Bob Daisley once again entering the fold. At the time of its release, when heavy metal was enjoying a surge in popularity, The Ultimate Sin was Osbourne's highest-charting studio album. The RIAA awarded the album Platinum status on 14 May 1986, soon after its release; it was awarded Double Platinum status on 26 October 1994. The
```

### Album 152, chunk 3

```text
album sold over 2,000,000 copies worldwide. In the UK, it was the final of four Osbourne albums to attain Silver certification (60,000 units shipped) by the British Phonographic Industry, achieving this in April 1986. Despite its commercial success, Osbourne cites The Ultimate Sin as his least favorite solo album, saying "If there was ever an album I'd like to remix and do better, it would be The Ultimate Sin." Much of the vocalist's blame has been placed on the shoulders of producer Ron Nevison, saying "(He) didn't really do a great production job. The songs weren't bad, they were just put down weird. Everything felt and sounded the fucking same. There was no imagination." Ozzy Osbourne – vocals Jake E. Lee – guitars Phil Soussan – bass Randy Castillo – drums Mike Moran – keyboards Additional engineers – Martin White, Richard Moakes
```

## Album 153: Another Page — Christopher Cross

- **album_id:** `b49d9b18-b23b-4e55-877f-a5ee8b89bcbd`
- **Tags (identification only):** pop, pop rock, rock, adult contemporary, soft rock, yacht rock
- **Chunks:** 2 (540 words)

### Album 153, chunk 1

```text
Another Page is Christopher Cross's second studio album, recorded in 1982 and released in early 1983. It was not as commercially successful as its predecessor (it was certified Gold by the RIAA, but only after his self-titled debut album had already been certified Platinum by the time of the release of Another Page). The album reached number 1 in Japan in 1983. The album is known for its two hit singles, "All Right" and "Think of Laura". "All Right" is the first single to be released from the album. And it became a massive hit in 1983, with it reaching No. 12 on the Billboard Hot 100, No. 3 on the Adult Contemporary chart, and No. 1 in the RPM adult contemporary charts. "Think of Laura" is dedicated to the Denison University college student Laura Carter, who was assassinated by Gordon Newlin when he shot a stray bullet at her during gunfire in a gang war. "Think of Laura" managed to become a No. 1 hit on the Adult Contemporary chart and No. 9 on the Billboard Hot 100. "Think of Laura" also was featured on the television soap opera General Hospital. "Arthur's Theme (Best That You Can Do)" appeared as a bonus track on the cassette and later CD releases of the album. In his retrospective review, William Ruhlmann of AllMusic noted that Another Page closely followed the musical style of Christopher Cross's debut album, which had been a major commercial and critical success. Ruhlmann wrote that Another Page
```

### Album 153, chunk 2

```text
featured similarly smooth pop arrangements and romantic lyrics delivered in Cross's gentle, Brian Wilson-like tenor. Although the album lacked the emotional depth or edge of rock music, he stated that it was still commercially successful, producing two Top 40 hits—"All Right" and "No Time for Talk"—and earning a gold certification. Nearly a year after its release, the album gained renewed attention when the ballad "Think of Laura" was featured on the television soap opera General Hospital, leading to the song becoming a Top 10 hit. Christopher Cross – vocals, guitars, guitar solo (10), arrangements Rob Meurer – keyboards, synthesizer programming, percussion, arrangements Michael Omartian – keyboards, percussion, arrangements, string arrangements and conductor Jay Graydon – guitar solo (4) Steve Lukather – guitars, guitar solo (6) Abraham Laboriel – bass Mike Porcaro – bass Andy Salmon – bass Steve Gadd – drums Jeff Porcaro – drums Tommy Taylor – drums Lenny Castro – percussion Paulinho da Costa – percussion Tom Scott – saxophone (1) Ernie Watts – saxophone (3, 11) Michael McDonald – backing vocals (1, 6) Carl Wilson – backing vocals (2) Karla Bonoff – vocals (3) Don Henley – backing vocals (4, 8) JD Souther – backing vocals (4, 8) Art Garfunkel – backing vocals (7) Flamingo on cover - Flossy Producer – Michael Omartian Assistant Producers – Rob Meurer and Michael Ostin Engineer and Mixing – Chet Himes Additional Engineering – John Guess, Lee Herschberg, Mark Linett and Richard Mullen. Assistant Engineers – Stuart Gitlin and Margaret Gwynne Art Direction and Design – Christine Sauers Cover Illustration – Louise Scott Photography – Matthew Rolston Lettering – Mike Manoogian Direction for Front Line Management – Irving Azoff and Tim Neece Stylist – Laurie Warner Set Styling – Frances Moore
```

## Album 154: Magic Potion — The Black Keys

- **album_id:** `4067e9c8-b24c-4757-a7f4-fe6bb9304c91`
- **Tags (identification only):** blues rock, rock, alternative rock, garage rock, longing, male vocalist, raw
- **Chunks:** 1 (274 words)

### Album 154, chunk 1

```text
Magic Potion is the fourth studio album by American rock duo the Black Keys. It was released in 2006 and was their first record released on Nonesuch Records, the band's current label. This album marks the first time they wrote and composed entirely original material, unlike on previous albums and EPs. Like the group's first two albums, Magic Potion was recorded in the basement of drummer Patrick Carney; in his estimation, the record was made using "$5,000 worth of crappy equipment". The group's guitarist Dan Auerbach explained the decision behind the recording location: We like the sound of odd rooms. It's got concrete floors and walls. The upstairs floor is the ceiling. The mixing desk and computer are on top of the tool desk built by the old guy who used to live there. You can hear all of that. Lots of new records have no individuality to the sound. I wanted it to sound like a band in the basement of a house in the Midwest. Carney expressed disappointment in the quality of the finished record: We paid $350 to get it mastered, took it home and there was, like, no bass on it. And we just dropped it in a FedEx envelope, mailed it to Warner Brothers and were done with it. Of all things that we've ever done, that's my biggest regret—is that we just kind of were like, "Oh, OK." The cover art depicts a Fabergé egg. Inside the album is a picture of a fried egg. The back cover depicts a falcon. Dan Auerbach – guitar, 12 string guitar, slide guitar, lap steel, vocals Patrick Carney – drums, percussion
```

## Album 155: Master-View — Hexstatic

- **album_id:** `a3c304a9-e365-4c8b-ba10-5e28b14f7239`
- **Tags (identification only):** electronic, breakbeat, electro, abstract, dance and electronica, trip hop
- **Chunks:** 1 (271 words)

### Album 155, chunk 1

```text
Master-View is the second studio album by Hexstatic. The CD version of the album includes 2 discs - a CD and a DVD. The songs, "Chase Me" and "L-Virata" was used in Tiger Woods PGA Tour 07. "Living Stereo" was used in a Cartoon Network bumper. Chase Me was also used on UEFA Champions League 2004-2005 The DVD that accompanied the CD album contained the following tracks. A pair of 3-D film glasses were also included in the packaging for use with the 3D videos (tracks 13 - 18): Extra Life (2D video) Chase Me (2D video) Telemetron (2D video) L-Virata (2D video) Perfect Bird (2D video) Perfect Bird (Astroboy version) (2D video) Salvador (2D video) Living Stereo (2D video) Distorted Minds (2D video) That Track (2D video) Toys Are Us (2D video) Pulse (2D video) Telemetron (3D video) Salvador (3D video) Living Stereo (3D video) Distorted Minds (3D video) That Track (3D video) Pulse (3D video) Extra Life (DVD audio) Chase Me (DVD audio) Telemetron (DVD audio) L-Virata (DVD audio) Perfect Bird (DVD audio) Perfect Bird (Astroboy version) (DVD audio) Salvador (DVD audio) Living (DVD audio) Living Stereo (DVD audio) Living Stereo Eclectic Method remix (DVD audio) Distorted Minds (DVD audio) That Track (DVD audio) That Track instrumental (DVD audio) Toys Are Us (DVD audio) Pulse (video mix) (DVD audio) Pulse (CD mix) (DVD audio) Master Mix (mix of the 2D videos listed above) The DVD also contains the 3D version of the track "Deadly Media" from the previous album Rewind. It can only be viewed by directly accessing track 22 on the DVD using the DVD player's remote control.
```

## Album 156: What a Feelin’ — Irene Cara

- **album_id:** `862f4322-5930-4cbe-b7ba-bf57ae8a46c1`
- **Tags (identification only):** pop, dance pop, electronic, synth pop, disco
- **Chunks:** 9 (2220 words)

### Album 156, chunk 1

```text
What a Feelin' is the second studio album by American singer-songwriter Irene Cara. Released on November 2, 1983, this album is a continuation of the work that Cara began with producer Giorgio Moroder on the soundtrack to the 1983 film Flashdance. The dance-pop song she co-wrote with Moroder and Keith Forsey for the film, "Flashdance... What a Feeling", went to number one on Billboard magazine's Hot 100 and foreshadowed the style of this album, which was unlike her R&B-heavy debut. Although Cara was more accustomed to composing music, she relinquished most of those duties to Moroder here and shifted much of her songwriting focus to lyrics. The title of the album clued in record buyers to the inclusion of the soundtrack hit from the spring of that year, but another four songs would make the Hot 100, the first of which, "Why Me?", had been released in October. "The Dream (Hold On to Your Dream)" from the D.C. Cab soundtrack became the second new single when that movie was released in December, four months earlier than planned. Since the song was not on the original pressings of What a Feelin', those copies were removed from store shelves so that the album could be re-released to include it. The other two Hot 100 entries were Cara's last top ten hit, "Breakdance", and the one track on the album for which she did write the music, "You Were Made for Me". The album received mixed-to-positive reviews and was moderately successful, reaching number
```

### Album 156, chunk 2

```text
77 on Billboard's album chart. But while Cara was having hit records and receiving awards for "Flashdance... What a Feeling", she was also feeling ripped off by her record company, Network Records, and planning to sue. The lawsuit she filed resulted in a backlash that destroyed her reputation in the entertainment industry. It would be eight years before the courts would acknowledge the harm she suffered and she would begin receiving royalties for the recordings she had made since signing with the label. In March 1983, Casablanca Records released the first single from the soundtrack to the upcoming Paramount Pictures film Flashdance, the story of a young woman who works as a welder and nightclub performer and dreams of becoming a ballerina. The music for that song, "Flashdance... What a Feeling", was written by the composer of the score for the film, Giorgio Moroder, and Irene Cara, who performed the song, wrote the lyrics with Keith Forsey. Their collaboration spent six weeks at number one on the Billboard Hot 100, and Moroder and Cara together completed two more projects in 1983 that were initially separate: Cara's next album, What a Feelin', and a song for the soundtrack of the film D.C. Cab titled "The Dream (Hold On to Your Dream)". Moroder also composed the score for that film and produced the soundtrack album. He wrote the music for the song, and Cara again sang and co-wrote the lyrics. In a discussion of What a Feelin' with Billboard just after its
```

### Album 156, chunk 3

```text
release, Cara said, "I usually write music; it's only working with Giorgio that I've become a lyricist. I had no choice since he's a composer." Of the nine new tracks on the original album, Moroder wrote the music for six, but one of her compositions, "You Were Made for Me", made the final cut as the sole ballad and album closer. She insisted, "It's still very much Giorgio's album." Many of the same people who Moroder selected to work on "Flashdance... What a Feeling" joined her on this new project. Forsey assisted her with lyrics on four of the tracks, and the guitarist on her number-one hit, Richie Zito, arranged all of the new material, played instruments on most of the songs, and even co-wrote (with Arthur Barrow) the music on one of the other songs not composed by Moroder, "Keep On". The album also reunited Cara with two of her "Flashdance..." background vocalists, Joe Esposito and Stephanie Spruill, on the first new single from the album, "Why Me?". What a Feelin' was released by Geffen Records on November 2, 1983, without "The Dream", which was to be on the D.C. Cab soundtrack album by MCA Records. Since the film was originally scheduled to be released in April 1984, the soundtrack was going to hit store shelves in February. D.C. Cab told the story of a taxi service in the nation's capital, and one of the cabbies was played by Mr. T., whose new television show The A-Team was a
```

### Album 156, chunk 4

```text
top ten hit in the Nielsen ratings. The film's distributor, Universal Pictures, wanted to take advantage of his popularity by moving the film's release up from the April 1984 slot to December 16, 1983. The release of the soundtrack album was also now moved up to December, but the loss of those four months that had been available for publicizing the film disrupted the plans that the studio had to market it using members of the cast. One of the film's executive producers, Jon Peters, then arranged to have What a Feelin' pulled from store shelves and reissued to include "The Dream". What a Feelin' debuted on Billboard magazine's Top LPs & Tapes chart in the issue dated December 10, 1983, to start a 37-week run there and peaked at number 77 in the February 25, 1984, issue. AllMusic critic William Ruhlmann noted that the album struggled to stay in the top 100 of the 200 albums listed there and speculated that it was because people already had a copy of "Flashdance... What a Feeling" and "Cara never established a base beyond her individual hits." The album also spent 30 weeks on the magazine's Black LPs chart, where it made its highest showing at number 45 in the January 7 issue. "Why Me?", the first official single from the album, debuted on the Billboard Hot 100 in the issue of the magazine dated October 22, 1983, to begin a fifteen-week run and peaked at number 13 for two weeks, which
```

### Album 156, chunk 5

```text
began in the December 3 issue. Upon the release of her next single, "The Dream (Hold On to Your Dream)", the review in Cash Box magazine pointed out that "Why Me?" was "still making its way up the charts." The December 10 issues of that magazine and Billboard both included the debut of "The Dream" on their respective lists of the 100 most popular singles in the US and listed "Why Me?" with bullets indicating noteworthy airplay and sales gains, giving her two songs moving up the charts at the same time. "The Dream" peaked at number 37 on February 11, 1984, and stayed on the Hot 100 for a total of fourteen weeks. Her next single, "Breakdance", started its nineteen weeks there in the March 24, 1984, issue. It peaked at number eight in the June 9 issue and was her third and last top ten hit. "You Were Made for Me" was the final single from the album and her last song to make the Billboard Hot 100. It began its five weeks on the pop chart in the July 28, 1984, issue and peaked at number 78 in its third week there. Although a promotional video had not been planned for "Flashdance... What a Feeling", Flashdance distributor Paramount Pictures had the director Adrian Lyne compile clips exclusively from the film to create a music video for the song when the movie became a surprise hit in the spring of 1983. Cara did appear in the other two
```

### Album 156, chunk 6

```text
videos created for songs on What a Feelin', "Why Me?" and "The Dream". Both were directed and edited by Doug Dowdle and produced by Jeffrey Abelson. The character Cara portrays in the video for "Why Me?" juggles two plot lines: her frustration as a performer going to auditions at Broadway theaters and finally having success while at the same time ending one relationship and finding another. Because the story takes place in Manhattan, Cara is filmed at various landmarks and theaters as she lip-syncs the song. Billboard listed the clip in the New Videos Added section of its MTV Adds & Rotation column, which noted that it was added to the cable channel's playlist of music videos as of December 7 in the magazine's December 17 issue, eight weeks after its debut on the Hot 100. The video for "The Dream" used scenes from D.C. Cab alongside footage of Cara playing herself in her home and around the streets of London. The cabbies have sent her a note that reads, "We miss you, Irene! Your friends at D.C. Cab", and Cara lip-syncs and dances to the music as the comedic visual elements from the film are interwoven throughout. According to the MTV Adds & Rotation list, the video began airing on the cable channel on December 14, one week after "Why Me?" did. At the time of the album's release, Billboard Dance Trax columnist Brian Chin described it as "a well-executed piece of work on the part of both producer
```

### Album 156, chunk 7

```text
and artist" and made mention of the yet-to-be-released singles "Breakdance" and "The Dream (Hold On to Your Dream)" as "ace uptempo picks" that "beg for remixes." He added, "Cara should also please fans nostalgic for the robotic early [Donna] Summer sound with her slightly off, trance-like delivery of 'Romance '83' and 'Cue Me Up.'" Cash Box averred that "Flashdance... What a Feeling" and "Why Me?" were "just two of the sizzling singles from this consistent collection." They felt it was "strong on well-structured pop songs, often reminiscent of ABBA in 'Why Me?' and 'You Took My Life Away' with impeccable melodic turns." They concluded, "Many of the tunes sound suitable for follow-up singles because of their distinctive quality and Cara's vocal warmth." In a contemporary review for The Village Voice, music critic Robert Christgau gave the album a "C+" grade but confused Cara's educational background with that of her Fame character, Coco Hernandez: "I wish she'd gotten her training in church rather than at Performing Arts." In a retrospective review, AllMusic's William Ruhlmann gave it four-and-a-half out of five stars and said that, even though she sang and co-wrote the lyrics, Cara was mostly "the mouthpiece of Euro-disco producer Giorgio Moroder on these recordings." The Rolling Stone Album Guide found that the title song was its only redeeming feature. In a 2018 interview, Cara described how the time of receiving awards for "Flashdance... What a Feeling" in early 1984 was also quite painful. "Unfortunately, I was going through a lot
```

### Album 156, chunk 8

```text
of hassles with my record company… So on the outside, I was putting on a face of being on top of the world and being a success, and on the inside I was trying to figure out how to sue my label." Al Coury, the former RSO executive who signed Cara to his newly formed Network Records a few years earlier, was "acting like a manager, which he shouldn't have been doing," according to Cara. Her musical contribution to D.C. Cab, for example, was something that Coury arranged. She confronted him about not receiving financial compensation for her first album or for "Flashdance... What a Feeling" but was given the runaround. In 1985, Cara filed a lawsuit against Network Records and Al Coury, Inc., for, among other things, withholding most of the royalties she had earned from her recordings for the label. She claimed that the backlash she endured from taking action against Coury cost her her "future as a recording artist", and believed that the company discouraged the other record labels from working with her because of her legal actions; she described it as being blacklisted. From that point on, record executives and film producers would have nothing to do with her. "Rumors swirled mercilessly about rampant drug use, spreading the notion that, in her early twenties, this great talent already had been hollowed out." The first team of lawyers she hired proved ineffective, and the lawsuit laid dormant until the early nineties when she found a lawyer willing
```

### Album 156, chunk 9

```text
to address what happened. A Los Angeles County Superior Court awarded her $1.5 million in 1993 after concluding that her career was damaged as a result of the treatment she received, but her attorney, Tom Nunziato explained how actually getting the money was more complicated: "Because only the corporations [Al Coury Inc. and Network Records] were sued back in the beginning and not the individuals, the corporations just declared bankruptcy; supposedly they used all the money to pay attorneys… Irene was vindicated by the jury, but the legal system kind of fell down, and there was no way to compensate her." She did, however, begin earning royalties almost a decade after her last chart hit. Unidisc Music reissued What a Feelin' on compact disc in 1997 in an expanded edition that included dance remixes of "Flashdance... What a Feeling", "Why Me?", "The Dream", and "Breakdance" as well as an instrumental remix of the album's title song and the track that "The Dream" replaced on some editions of the 1983 reissue, "Talk Too Much". The dance remix of "Why Me?" was the only version of that song included, but the other four singles were presented as heard on their albums of origin instead of as the single edit or "radio edit" that the liner notes indicated. Irene Cara – lead vocals
```

## Album 157: Abandon — Deep Purple

- **album_id:** `9dc2c9f8-f889-491b-81c2-c05a994a6313`
- **Tags (identification only):** hard rock, classic hard rock, rock
- **Chunks:** 1 (263 words)

### Album 157, chunk 1

```text
Abandon is the 16th studio album by the English hard rock band Deep Purple, released on 25 May 1998. It was band's second album with guitarist Steve Morse and their last to feature founding member Jon Lord prior to his departure in 2002. The cover art was designed by acclaimed artist Ioannis Nikolaos Vasilopoulos. The album was followed by a successful 1998–1999 world tour, which saw Deep Purple visit Australia for the first time in 15 years. In 1999, a double live album and DVD, Total Abandon: Australia '99, recorded in Melbourne on 20 April was released. The album title is actually a pun from Ian Gillan – "A Band On" – and the album was followed by the "A Band on Tour". It featured a reworking of a previously recorded song – "Bloodsucker" from Deep Purple in Rock (here spelled "Bludsucker"). "Don't Make Me Happy" was mistakenly mastered in mono and not amended on the album, one of the two versions of the song released on a promotional single was mastered in stereo. "Any Fule Kno That" is the first song on Abandon. Vocalist Ian Gillan takes a spoken word approach in the verses, comparable to rapping. The title is a popular phrase from the Nigel Molesworth books. "Any Fule Kno That" became the band's last charting single in the US, peaked at number 25 on Billboard's Heritage Rock Chart. Ian Gillan – vocals Steve Morse – guitars Jon Lord – Hammond organ, Korg synthesiser Roger Glover – bass guitar Ian Paice – drums Assistant engineer – Kent Huffnagle with Shannon Brady
```

## Album 158: Off the Deep End — “Weird Al” Yankovic

- **album_id:** `7439e46e-15d7-4f92-997d-6b10e478ffd0`
- **Tags (identification only):** comedy, comedy rock, parody, pop rock, music comedy, novelty, pop/rock, song parody
- **Chunks:** 9 (2276 words)

### Album 158, chunk 1

```text
Off the Deep End is the seventh studio album by the American parody musician "Weird Al" Yankovic, released in 1992. This album was the first album self-produced by Yankovic, after six albums with Rick Derringer. Recorded between June 1990 and January 1992, the album was a follow-up to the unsuccessful soundtrack to Yankovic's 1989 film UHF. Off the Deep End and its lead single "Smells Like Nirvana" helped to revitalize Yankovic's career after a lull following his last hit single, "Fat", in 1988. The musical styles on Off the Deep End are built around parodies and pastiches of pop and rock music of the late 1980s and early 1990s, including the newly arisen grunge movement. Half of the album is made up of parodies of Nirvana, MC Hammer, New Kids on the Block, Gerardo, and Milli Vanilli. The other half of the album is original material, featuring many "style parodies", or musical imitations of existing artists. These style parodies include imitations of specific artists like the Beach Boys, James Taylor and Jan and Dean. Off the Deep End was met with mostly positive reviews and peaked at number 17 on the Billboard 200. The album also produced one of Yankovic's most famous singles, "Smells Like Nirvana", a parody of Nirvana's major rock hit "Smells Like Teen Spirit", which peaked at number 35 on the Billboard Hot 100. This song was Yankovic's second-highest charting single, after "Eat It", which was released in 1984. The cover also parodies the cover of Nirvana's
```

### Album 158, chunk 2

```text
album, Nevermind. The original had a naked baby in the water with a dollar bill cast by a fishing rod; Yankovic's replaced the baby with himself, and the dollar bill with a donut. Off the Deep End was Yankovic's fourth Gold record, and went on to be certified Platinum for sales of over one million copies in the United States. In addition, the album was later nominated for a Grammy Award for Best Comedy Recording in 1993. In 1989, Yankovic starred in a full-length feature film, co-written by himself and manager Jay Levey, and filmed in Tulsa, Oklahoma, called UHF. A satire of the television and film industries, also starring Michael Richards, Fran Drescher, and Victoria Jackson, it brought floundering studio Orion their highest test scores since the movie RoboCop. The movie was considered unsuccessful, only just making back its budget ($6 million at the box office compared to a budget of $5 million). Yankovic also released a quasi-soundtrack for the film in late 1989, entitled UHF – Original Motion Picture Soundtrack and Other Stuff, which featured songs (and commercials) from the movie as well as new unrelated studio material from Yankovic. The album failed to be successful, charting at only 146 on the Billboard 200 and quickly falling off. After the release of UHF, Yankovic returned to the studio to record his follow-up album. On June 6, 1990, recording for Off the Deep End officially began at Santa Monica Sound Recorders, in Santa Monica, California. The first recording session
```

### Album 158, chunk 3

```text
started with "Airline Amy". These recording sessions marked the first time Yankovic self-produced his songs, after six albums with Rick Derringer. The producer and musician had parted ways because Derringer found that Yankovic would not listen to his input, and Yankovic came to realize that he could do most of the production work himself. Subsequent studio albums would be produced by Yankovic. In regards to this split, Yankovic said: "We [i.e. Yankovic and his band] had a great run with Rick, he's a terrific guy—but I had become more and more of a control freak over the years, and I'd finally gotten to the point in my recording career where I felt that I could capably hold the reins all by myself." By late 1990 five originals—"Airline Amy", "Trigger Happy", "When I Was Your Age", "You Don't Love Me Anymore", and "Waffle King"—were recorded. "You Don't Love Me Anymore" was one of the last original songs recorded during the 1990 sessions. The song is written as a soft acoustic ballad. However, the lyrics are of a—literally—destructive relationship between Yankovic and an unnamed girl. Although they were formerly in love, the "flames died down" and they are no longer passionate—in fact the girl hates Yankovic to such an extent that she repeatedly attempts to kill him. In 1992, when the album was finally released, Yankovic desired to release the song as a single. His record label, Scotti Brothers, allowed it under the stipulation that the music video be a parody of
```

### Album 158, chunk 4

```text
another music video. "You Don't Love Me Anymore" was subsequently released to radio on June 19, 1992. While the song was an original composition, the video was a parody of "More Than Words" by Extreme. Yankovic later explained that when the song was released, many people erroneously believed it was a parody of "More Than Words", and thus, Yankovic crafted the music video to be a parody of the song. The single received moderate radio attention, which surprised Yankovic, because he had always thought that radio stations "usually just go for the parodies". One of the original songs recorded in the 1990 sessions was "Waffle King". However, when Yankovic resumed recording in 1992, he recorded a new original called "I Was Only Kidding". Originally, "Waffle King" was supposed to appear on Off the Deep End. However, by the time the recording of the parodies for this album began, Al had written all the original songs that were to appear on his next album, Alapalooza. Because he was concerned that one of the jokes from the song "I Was Only Kidding" might be dated by the time his next album would finally be released—a line that references the movie Wayne's World: "I really love you... not!"—Yankovic included "I Was Only Kidding" on Off the Deep End in place of "Waffle King". "Waffle King" was instead used as the b-side of the "Smells Like Nirvana" single and would later resurface on Alapalooza. The album also contains a hidden track at the end
```

### Album 158, chunk 5

```text
called "Bite Me". The "song", which consists of several seconds of loud music and Yankovic screaming, appears after 10 minutes of silence following "You Don't Love Me Anymore". According to Yankovic, the song was supposed to "come on [...] and scare you to death". Later pressings of Off the Deep End by Volcano and pressings outside the USA took away the hidden track and silence. The track is a nod to Nirvana: pressings of Nevermind featured the hidden track "Endless, Nameless". After recording the first batch of originals in 1990, Yankovic focused his attention on parodies. By early 1991, only three parodies had been recorded. Two of them, the cookie-inspired New Kids on the Block parody "The White Stuff" and the television-centric MC Hammer parody "I Can't Watch This", were slated to be released as singles. In fact, several cartons of promo singles were pressed, but they were deleted from the record company's catalogue at the last minute. These CDs were later discovered by Yankovic and his drummer, Jon "Bermuda" Schwartz, in a trash heap and have since become collector's items. "The Plumbing Song", a double parody of Milli Vanilli's hit singles "Baby Don't Forget My Number" and "Blame It on the Rain" was also recorded. In a 1992 interview with Dr. Demento, Yankovic said that he believed the parody to be "kind of redundant" at that point in time, given the lip-synching scandal that had effectively destroyed the band almost two years prior. In reference to this scandal, Yankovic
```

### Album 158, chunk 6

```text
also jokingly affirmed that he did indeed sing lead vocals on his parody. Yankovic waited for almost two years for the next "big thing" to emerge. "I don't have any really good reason why it took so long other than the fact that I was waiting for Michael Jackson's new album to come out," Yankovic explained. Unfortunately for Yankovic, the new album hit several snags. On November 26, 1991, Michael Jackson's new album, Dangerous was released. After hearing the hit single "Black or White", Yankovic approached Jackson about a potential parody entitled "Snack All Night". Although Jackson was a big supporter of Yankovic's work, he felt that a parody might be inappropriate, due to "Black or White" being about racial issues. Jackson told Yankovic that he could, if he wanted to, parody another song off his album, but just not "Black or White". Yankovic soon turned his attention in another direction. Guns N' Roses had just released a version of Wings's 1970s hit "Live and Let Die". Yankovic approached Paul McCartney, leader of Wings, about a parody idea entitled "Chicken Pot Pie". Although McCartney was a supporter of Yankovic's work and he wanted to give Yankovic the chance to parody one of his songs, he begrudgingly turned him down due to the fact that, as a vegetarian, he could not condone the eating of animal flesh. Yankovic, a fellow vegetarian, has stated that he respects McCartney's decision. It was around this time that Nirvana's Nevermind was making waves in the
```

### Album 158, chunk 7

```text
rock and pop scene. As the popularity of 1980s pop gave way to grunge, Yankovic decided it was time to record a parody of the Seattle-based band's huge hit single "Smells Like Teen Spirit". Yankovic later said, "I wanted to make sure that when I came back after that long hiatus, it was with something strong, and it wasn't until Nirvana that I felt I had a real contender." To secure permission for the parody, Yankovic wanted to approve it with Kurt Cobain. After learning that Nirvana was to perform on Saturday Night Live, Yankovic called up his UHF co-star, Victoria Jackson, who was, at the time, a regular cast member on the show. Jackson got Cobain on the phone so that Yankovic could make his request. Cobain agreed, although he asked if the new parody was "going to be a song about food". Yankovic reassured him that it would actually be about how "no one can understand [the] lyrics" to the original, which Cobain thought was funny. After receiving permission, Yankovic wrote and recorded "Smells Like Nirvana" on January 27, 1992. After "Smells Like Nirvana", Yankovic recorded "Taco Grande", a Mexican food-themed parody of Gerardo's "Rico Suave". The latter features a cameo appearance from comedian Cheech Marin. Originally, Yankovic had wanted Marin to rap in Spanish, but it turned out that Marin knew only some basic Spanish. However, a bilingual secretary translated what Yankovic wanted him to say from English to Spanish and Marin read the resulting rap phonetically.
```

### Album 158, chunk 8

```text
One of the last songs to be recorded was the obligatory polka medley, "Polka Your Eyes Out". Yankovic had already performed the medley at Dr. Demento's 20th Anniversary Special on Comedy Central before the album had been released. The cover for Off the Deep End parodies the famous cover of Nirvana's album Nevermind, which depicts an infant in the deep end of a pool chasing after a dollar bill on a fishhook. The Off the Deep End cover shows Yankovic in the baby's place apparently swimming to catch a doughnut on a string. While the Nirvana cover has a fully nude baby, Yankovic instead wore a bathing suit in a way that his body position hid it; he later jokingly noted, "I never really anticipated going full-frontal on any of my album covers." The CD, liner notes, and artwork continue the parody of Nirvana's album, borrowing the same blue, wave-light graphics from the printed surface of Nevermind. Critical response to Off the Deep End was generally positive. Many critics praised not only Yankovic's parodies, but also his originals. Barry Weber, of AllMusic, wrote, "In addition to re-establishing his satirical craftsmanship, Deep End showcases some of Yankovic's best originals ever; "Trigger Happy," "When I Was Your Age," and "You Don't Love Me Anymore" prove to be the album's greatest songs." Christopher Thelen, of the Daily Vault, wrote, "In fact, it's strange to admit, but the originals on Off The Deep End actually are, at times, stronger than the parodies." In The
```

### Album 158, chunk 9

```text
Rolling Stone Album Guide, Off the Deep End was awarded 3.5 stars out of 5, denoting that the album averaged between good and excellent. Not all reviews were so positive, however. Entertainment Weekly reviewer David Browne noted that the video for Off the Deep End' lead single "Smells Like Nirvana" was "an old-fashioned laugh riot", but that half of Yankovic's humor was merely visual, meaning that the songs without videos were not as funny. The music video for "Smells Like Nirvana" achieved similar praise. Spy Magazine named it the "Video of the Year" in 1993, Rolling Stone ranked it as number 68 on their list of the Top 100 Videos of All Time, and it was nominated for the MTV Video Music Award for Best Male Performance in 1992. At the 35th Annual Grammy Awards in 1993, Off the Deep End was nominated for the Best Comedy Album. However, the album lost to Peter Schickele's Music for an Awful Lot of Winds and Percussion. Off the Deep End was released April 1992, and was subsequently named the Best Selling Comedy Recording of the year by National Association of Recording Merchandisers (NARM). Off the Deep End was certified gold. On January 25, 2006, the album was certified platinum. The album's lead-off single, "Smells Like Nirvana" was a hit on the Billboard Hot 100, charting at number 35. It also charted on Hot 100 Singles Sales at number 12 and the US Billboard Mainstream Rock Tracks chart at number 35. Both the album and hit single helped propel Yankovic into the 1990s. As of 2014, sales in the United States have exceeded 1,057,000 copies, according to Nielsen SoundScan.
```

## Album 159: Eat Me, Drink Me — Marilyn Manson

- **album_id:** `8667eb8b-1a5f-4342-ba38-f74ace387556`
- **Tags (identification only):** alternative metal, rock, alternative rock, electronic, heavy metal, alternative/indie rock, euro house, goth rock
- **Chunks:** 20 (4957 words)

### Album 159, chunk 1

```text
Eat Me, Drink Me (Stylized in all caps.) is the sixth studio album by American rock band Marilyn Manson. It was released on June 5, 2007, by Interscope Records. It was recorded in a rented home studio in Hollywood by lead vocalist Marilyn Manson and guitarist and bassist Tim Sköld, and was produced by Manson and Sköld. It was the band's first album not to be recorded as a five-piece, as John 5 departed from the group in 2004. Instead of replacing 5, Tim Sköld remained with bass and played the guitar, and the band continued as a four-piece. Manson has stated that he sang most of the album lying down on the studio floor with his hands cupping the studio microphone, resulting in a very distinctive vocal sound. Of Sköld's compositions, a further two are said to have been turned into fully-fledged songs with lyrics, music and vocals completed but were not put onto album for fear of making it overwrought. Upon its release, Eat Me, Drink Me was met with positive reviews from critics, and debuted at number eight on the US Billboard 200. The album was the last to feature band member Tim Sköld, and spawned two singles ("Heart-Shaped Glasses (When the Heart Guides the Hand)" and "Putting Holes in Happiness"). The band supported the album with the Rape of the World Tour. After spending time around the end of the Grotesk Burlesk Tour in severe depression and contemplating his permanent departure from the music industry, Manson
```

### Album 159, chunk 2

```text
had a change of heart and recorded a duet of "Don't You Want Me" with Shirley Manson. This was originally intended to support the forthcoming best-of release but was felt by both artists not to live up to their standards and has yet to see release. Lest We Forget: The Best Of was released on September 28, 2004, and was referred to by the singer as his "farewell" album; however, he insisted that it would not be the final Marilyn Manson album. After the release of the single "Personal Jesus", the band made a number of promotional appearances. Lest We Forget was certified Gold in 2005. When promotion for Lest We Forget concluded, the band returned to the studio and recorded eight embryonic songs—some of which had vocals, and one notably a tribute to Andy Warhol. It was supported by the Against All Gods Tour. The tour was marked by one release, a 2005 EP of "The Nobodies" featuring a new mix of the song (by Chris Vrenna) and other remixes. Manson began his recording sessions on the album in November 2005 but was focused on his film Phantasmagoria: The Visions of Lewis Carroll, the process of opening an art gallery and personal troubles relating to his marriage. It was after opening the gallery, the Celebritarian Corporation Gallery of Fine Art on Halloween night of 2006, that Manson really began his contribution as a singer by working out melodies and structures around Sköld's already existing compositions, writing lyrics quickly and
```

### Album 159, chunk 3

```text
usually recording on the same day. One result of this is that the album features six guitar solos from Sköld (comprising 3 minutes, 39 seconds of the album in total) and many other guitar moments while bass and keyboards—both played also by Sköld—feature much less than on a usual Marilyn Manson release. Manson explained that "[he] was writing in the way you would write a diary" and as a result thinks that the record was written from a "more mature musical point of view." This is the record I've worked all my life to get to. You always have to transform, or you can't continue as an artist, and this record has been the biggest transformation for me [...] It's better heard than described [...] On this record I really wanted to sing, and that has to come from a naked, emotional place. It's not a record about me crying, or songs about my woes, but I think this record will probably speak to more people in different ways, because of its total human element [...] If I had to do a record review, I'd say it's got a cannibal, consumption, obsessive, violent-sex, romance angle, but with an upbeat swing to it [...] The album's title [Eat Me, Drink Me] was also inspired by that story several years back of the German man who put out an ad that he wanted to be eaten, and the man who ate him. Although I can't relate to the relationship those two had,
```

### Album 159, chunk 4

```text
I found the story very compelling in a romantic way. It has been stated that there were originally around 20 embryonic songs, all written by Sköld, two of which (that did not make the album) Manson considered complete with lyrics and vocals. Manson stated that he had a difficult time cutting some of them, but felt he had to in order to prevent the album from being "diluted". On May 31, the entire album was uploaded for streaming on Marilyn Manson's Myspace page, five days prior to its American release. "Manson probably needed something to shake up his music, which started to become comfortably predictable in the wake of his popular/creative peak of Mechanical Animals, but the stab at soul-baring on Eat Me might not have been the way to do it. But Manson is such a true believer in rock & roll mythos that he's wound up embracing the cliché of the post-divorce confessional album, peppering this album with songs about "broken relationships and new love". Personal songs are unusual for Manson, but that doesn't mean he's abandoned his tendency to write about grand concepts. The difference is that this time around, Manson himself is the grand concept which may give him a lyrical hook, but not a musical one. On a sonic level, this is a bit of "Manson-by-numbers", but it feels as if his usual murky menace has lifted, with the music sounding clearer, less affected, and obtuse, while still retaining much of its gothic romanticism and
```

### Album 159, chunk 5

```text
churning heaviness. If anything, Eat Me is a bit too transparent, as its clean arena rock production makes the album sound safe, a bit too close to Manson cabaret for comfort, especially when he's penning songs whose very titles feel like unwitting self-parodies such as "If I Was Your Vampire", "You and Me and the Devil Makes 3" and "They Said That Hell's Not Hot", or when he lazily spews out profanity as the chorus to "Mutilation Is the Most Sincere Form of Flattery." The most prevalent literary influence of the album and Manson's state of being is that of Lolita by Vladimir Nabokov, one of the most notorious books of the Twentieth Century. The song "Heart-Shaped Glasses" is the most obvious nod to Lolita as, according to Manson, Evan Rachel Wood is also a huge fan of Nabokov and had deliberately worn heart-shaped sunglasses upon meeting for a tryst when their relationship became romantic. Connections to the novel are much deeper than simply the inside joke between Manson and Wood of the obvious age difference and the heart-shaped sunglasses as associated with Lolita appear only in the promotional poster and cover of Stanley Kubrick's film adaptation of the novel, not actually in the film itself or in Nabokov's novel. According to Manson, vampirism is just one of the dark themes running through Eat Me, Drink Me. "If I had to do a record review, I'd say it's got a cannibal, consumption, obsessive, violent-sex, romance angle, but with an upbeat
```

### Album 159, chunk 6

```text
swing to it." Aside from the obvious Lewis Carroll and Jesus Christ references, Manson says the album's title was also inspired by the story of Armin Meiwes, who placed an ad online for a person consenting to be eaten. The Vampire, whom Manson personified during "Eat Me, Drink Me", in one regard is an inversion of the mythology of Christ. Both entities rise from the dead but as Christ offers his body and blood for his disciples to feast upon in communion with him, the vampire as contrary to this, devours the flesh and blood of his victims in order to make them one with him. In 2007, Eat Me, Drink Me brought with it, for the first time in nearly over ten years, a symbol Manson adopted to represent himself with that did not have an immediate and apparent deeper connotation to the occult, mock-fascism or an artistic movement. This logo, later dubbed the "heart-shaped spiral" in official online store item descriptions, was minimalistically a roughly drawn heart which spiraled at its center. Manson revealed that it was an homage to Wood for inspiring him with love and creative drive which was the impetus needed to create the album. He elaborated that as it was tattooed on his left inner wrist. The Eat Me, Drink Me era's visuals, was inspired by the iconography of the 1935 Karl Freund film Mad Love. As can be seen within both the album artwork and repeated on the CD single for "Putting Holes
```

### Album 159, chunk 7

```text
in Happiness", we see a closeup of Manson's eye with a heart as the pupil signifying a romantic and newly inspired Manson with literal "hearts in his eyes". In very close relation to the film and artwork of Mad Love, which portrayed an insane and malformed monster of a man who is driven to create his mad abominations by the love of a woman, Manson's eyes can be seen to signify this theme likewise in reflecting how Evan inspired his resurgence of creativity needed to compose the album. Though not particularly esoteric or heavy in symbolism, the primary Eat Me, Drink Me Marilyn Manson logo were two blood dripping fang-like M's to represent the initials of the band. Fairly self-explanatory in representation, and included here for the sake of being all-inclusive, the dripping red M's are nonetheless an iconic logo in themselves and work effectively in illustrating the many vampiric themes of the album. The various lyric allusions of Eat Me, Drink Me and the imageries which are referenced by Manson, not visual in this case but in verse form. As Eat Me, Drink Me has been Manson's most personal album to date, the lyrics are full of self explorations of past themes which Manson has explored as well as many subtle allusions to the album's inspirations. The album opens with "If I Was Your Vampire", an industrial-goth song. Quiet ringing guitars are offset by heavy drums, owing as much musically to the Sisters of Mercy as it does to
```

### Album 159, chunk 8

```text
Nine Inch Nails. And the lyrics are as much Bauhaus as Ministry with talk of "blood-stained sheets in the shape of your heart". Majestic would be another way to describe it, as drenched in irony-deprived passion, Manson intones "Beyond the pale/ Everything is black/ No turning back." The lyrical auto-erotica that begins in the lead-off track ("Drive me off the mountain/ You'll burn, I'll eat your ashes/ Impossible wheels seducing our corpse") continues with the wailing "Just a Car Crash Away" and the stand-out "Are You the Rabbit?", which harkens back to the "glammy guitar feel" of Mechanical Animals. "Are You the Rabbit?" builds off of Manson's obsession with Lewis Carroll, while pulling fairy-tale like lyrics off in style with an all-around catchy song and hook. In what can only be seen as a way to maintain a buzz with the generation behind, his very public attachment to Evan Rachel Wood is flaunted throughout the peripheral of this release, from his personal artwork to the song and video for the Lolita-inspired first single, "Heart-Shaped Glasses (When the Heart Guides the Hand)". The song itself is a piece of militant drum cadence mixed with raw adolescent sexuality in both Manson's lyrics and delivery: "She'll never cover up what we did with her dress." The blustery guitar of "You and Me and the Devil Makes 3" revels in the repetition of the title alongside the menacing delivery of "There's not a word for what I want to do to you", but it's
```

### Album 159, chunk 9

```text
hard to take any song too seriously when it contains a "Murdercute happyrape" lyrical chorus. Although somewhat lyrically stunted, "The Red Carpet Grave" is an interesting song on the album, "The Red Carpet Grave" is perhaps the most confessional track, with Manson repeating the line, "I can't turn my back on you, but you're walking away." The new wave elements are present to a lesser extent on harder-rocking songs like "Mutilation Is the Most Sincere Form of Flattery". The latter song is one of several that touch on Manson's marriage and subsequent divorce from Dita von Teese, as Manson writes about his personal life in his music for the first time. Rumors also circulated for some time that Marilyn Manson wrote the song "Mutilation Is the Most Sincere Form of Flattery" as an attack on the band My Chemical Romance, for his Eat Me, Drink Me release (which he later denied, saying that it was aimed at people in general seeking to imitate him). In another interview Manson stated, "I'm embarrassed to be me because these people are doing a really sad, pitiful, shallow version of what I've done". On April 15, 2007, Marilyn Manson's Interscope Records-administered Myspace page went live with promotional artwork. The next day "If I Was Your Vampire" was added to the player as Myspace Music's "Single of the Week". Hours later, Manson's official website went through a revision to coincide with the imagery of the new album. Later still but on the same day, Interscope
```

### Album 159, chunk 10

```text
e-mailed out a press release containing the album artwork by Nela Koenig. Two days later Interscope opened a "VampireFreaks" account for Manson. The album leaked onto P2P networks on May 1, Manson said he was unconcerned by the leak as it mainly affects record companies and not the artists. To promote the album, Manson first traveled to France, the United Kingdom, and Germany, where he held both press conferences and listening parties. Similar listening parties for journalists and fan club administrators took place in other European countries and the United States. Measures taken to prevent an unauthorized recording or copy of the album from leaking included bag searching and the prohibition of recording devices and mobile phones. Manson appeared twice on BBC Radio 1; on April 17 on the Zane Lowe Show and on May 23 in the Live Lounge where he and Sköld performed an acoustic version of "Heart-Shaped Glasses" and a cover of Justin Timberlake's "What Goes Around Comes Around", having been given a choice by the station of Timberlake, Green Day, Amy Winehouse or Muse. The next significant promotion took place on May 18 with the uploading to the official website of the album's 16-page linear booklet. The uploading coincided with Manson's in store signing at Hot Topic in California where fans who had obtained an entry wristband days prior were given a copy of the booklet for Manson to sign though he signed other items on fans request for two hours. Also available at the event,
```

### Album 159, chunk 11

```text
and now available in Hot Topic stores and online shop, is an exclusive two-track "Heart-Shaped Glasses" single. All Hot Topic stores across the USA held listening parties for the album on May 25. The stores are also added three new official T-shirts to the racks to coincide with the party and Manson recorded linking material for the songs. Newbury Comics gave away licensed Eat Me, Drink Me pint glasses with each pre-order of the album. Further promotional oddities were to be found in the UK where boxes were distributed containing chocolates marked "Eat Me" and mini bottles of Tequila with "Drink Me" on the back. An official Eat Me, Drink Me mini-site was discovered through a link found in the European "Heart-Shaped Glasses (When the Heart Guides the Hand)" single. The site, www.marilynmansonvault.com, contains lyrics, a photo gallery, a mosaic, and the ability to stream up to two tracks per day starting on May 28, 2007. Upon completion of the mosaic, an Eat Me, Drink Me wallpaper becomes available for download, and three preview tracks ("Heart-Shaped Glasses (When the Heart Guides the Hand)", "If I Was Your Vampire", and "Evidence") become available for streaming. The official release of the single coincided with the opening of the vault itself (for those with the single) to access a screensaver, ringtone and two "classic tracks for download" ("Disposable Teens" and "The Dope Show"). The song "If I Was Your Vampire" was used in the soundtrack to the 2010 parody flick Vampires Suck. In
```

### Album 159, chunk 12

```text
the film it opens the end credits. Marilyn Manson's 2007 to 2008 worldwide art exhibition named for its title-piece watercolor which had surfaced in mid-2006, at the period when Manson had been thoroughly immersed in the composition of his film project Phantasmagoria: The Visions of Lewis Carroll. As such, many of the paintings released simultaneously bore similar themes and re-interpretations of the nightmare world of Carroll's Alice in Wonderland. The title of the painting however evokes the much deeper and intricate reference of Charles Baudelaire's 1857 incendiary poetic collection during the era of Romanticism, Les Fleurs Du Mal (English: The Flowers of Evil). Manson announced via his website in mid-January that the record was "nearly finished", titled Eat Me, Drink Me, and that the band would be touring the world in support of the record that was scheduled for release on June 5, 2007. The album's artwork was wrapped up in early February 2007 thus bringing an end to the creative process in preparation for the imminent promotion and publication of details. Since the release of the album, Manson appeared in Rolling Stone four times: the March article "Manson's Dark Return", a further paragraph from the Smoking Section, a mention in the "50 Albums to Look Forward to This Summer" issue and a small snippet featuring an explicit picture of Manson and Evan Rachel Wood in a hotel after the "Heart-Shaped Glasses" video shoot in which a naked Wood lies over Manson who has his fingers in the vicinity of
```

### Album 159, chunk 13

```text
her anus. Other publications to include original content with Manson have been the April issue of UK magazine Rock Sound, the May issue of Revolver, an interview with French RockMag, an MTV online piece focusing on Manson's suicidal ideation, a longer, more in-depth interview in Rock Sound, a long, very descriptive and open piece in The Observer Magazine (The Life and Loves of a He-Devil), a partial transcript of a friendly chat with Alejandro Jodorowsky, an interview in Germany's lifestyle monthly BlondMag, the cover story of June's Spin magazine stretched out over eight pages entitled "The Last Rock Star?", an article in Rolling Stone from Austin Scaggs who spends a fair amount of time with Manson judging by the five pieces in four months he has contributed, The Sun newspaper's Something For The Weekend section. The cover art for Eat Me, Drink Me portrayed Manson as a vampire, dressed with a black-toned outfit, standing still looking at the camera next to a window covered with blood; the pose bearing a very strong resemblance to the artwork for Tubeway Army's 1979 album Replicas. The back of the cover features a photo of a woman with her eyes covered by a hand, possibly Manson's hand, with the track listing featured on the left side. In one of the booklet's page, Manson says: "I would like to thank the loyal few that waited, at the far end of the abyss, for me to make this record. My mother and father, my best friends
```

### Album 159, chunk 14

```text
(you know who you are). Tony, Bobby and everyone else who has forgiven me for my wrongdoings. This record is dedicated to those who stood by me. Most of all, this is for Evan." A tour shirt was released to the online market and it featured the cover of the album. The front cover was shot by Nela Koenig and the back cover by Anthony Silva. The inside photos were shot by Perou and Nela Koenig and all Polaroids by Manson and Wood. The Heart-Shaped Eyes were self-portrait by Manson and the art direction and design by Marilyn Manson and Liam Ward. The album was released in three physical formats. The standard jewel case CD release contained a single enhanced CD and a 16-page booklet. The limited edition CD featured bonus tracks with acoustic version of "Putting Holes in Happiness" and three other remixes of the single "Heart-Shaped Glasses". An edition including a bonus DVD was also released. It featured a bonus CD including seven remixes of "Putting Holes in Happiness", "Heart-Shaped Glasses" and "You And Me and the Devil Makes 3"; and a DVD, including the music videos of "Putting Holes in Happiness" and "Heart-Shaped Glasses" and a "Track by track interview" video. An instrumental version of the entire album entitled Bonus Track and Instrumentals from the Album Eat Me, Drink Me was leaked in late 2007 on YouTube. It features all tracks from the album without the vocal track and also includes a remix of "Heart-Shaped Glasses (When
```

### Album 159, chunk 15

```text
the Heart Guides the Hand)", which was released as a bonus track on most international versions of the album. It is not a sanctioned release by Interscope. Nevertheless, a FLAC version of the album was uploaded to torrents thereafter, which made availability more widespread due to the price and rarity of pressed, physical copies. On April 17, 2007, "Heart-Shaped Glasses (When the Heart Guides the Hand)" was released as the lead single of the album and was added to the Marilyn Manson's official Myspace page on April 24. On April 27, 2007, Marilyn Manson released a clip featuring the last 34 seconds of the then upcoming music video for "Heart-Shaped Glasses (When the Heart Guides the Hand)" on YouTube, and later on the official website. The song peaked at #24 on U.S. Modern Rock Tracks. "Putting Holes in Happiness" is Marilyn Manson's second single from the album. Written on his own birthday, Marilyn Manson describes the song as being "a romantic-misogynistic-cannibal-gothic-vampire ballad". A two-track promotional disc was released in June 2007, but no confirmation of the song as the album's second single followed until Marilyn Manson confirmed the next single to be "Putting Holes in Happiness" on August 7, 2007. The song has already appeared on the radio in France, where a promo of the single has been sent out to several major radio stations. The Guitar Hero Remix by Nick Zinner version of the single was featured on early special editions of Guitar Hero III: Legends of Rock. "You
```

### Album 159, chunk 16

```text
and Me and the Devil Makes 3" was released as a promotional single from the album in September 2007. Upon its release, the album met with positive reviews. At Metacritic, which assigns a normalized rating out of 100 to reviews from mainstream critics, the album received an average score 63, based on 23 reviews, which indicates "generally favorable reviews". AllMusic gave the album a mixed review and said that "[it] is a bit too transparent, as its clean arena rock production makes the album sound safe [...] Eat Me, Drink Me becomes an intriguing muddle, an interesting portrait of Manson at the cusp of middle-age melancholy even if as sheer music it's the least visceral or compelling he's ever been." The Los Angeles Times praised the album's concept, saying "The songs too are sculpted from the darkest stone with special care. Previous Manson guitarists will envy the solo space allotted Sköld; a number of exceptional ax workouts perfectly reflect moods that range from mounting pride to roiling anguish to moaning abjection." It also noted that "Putting Holes In Happiness" stands out as "one of Manson's greatest songs." Jamie Fullerton of NME gave the album a rating of 7 out of 10, and said that "[t]his album sees him rising from the hordes of spider-black hoodies, becoming a musical force beyond the Download ticket-holders. Eat him, drink him, but make sure you listen to him too." PopMatters also gave the album a rating of 7 out of 10, and commented that
```

### Album 159, chunk 17

```text
"Eat Me, Drink Me should return Manson to his former successes, and rightfully so. There is an earnestness in the music designed to speak directly to fucked-up adolescence while often inexplicably foregoing the pander. There is something to be said for knowing where the line is and when to cross it. Call Manson what you will—genius, has-been, shock rocker, freak—but like his best work, Eat Me, Drink Me is as fun as it is cartoonishly scary." Slant Magazine gave the album a favorable review and praised "'Putting Holes in Happiness' [as] the best of the autobiographical tracks, with a melancholic guitar riff that matches the song's appropriately plodding arrangement. Hardcore fans may take offense to the lack of any songs challenging God, government, or society in general, but it's their loss. Eat Me, Drink Me is a bona fide creative rebirth." Rolling Stone magazine gave the album a three out of five stars and said that Manson "hasn't exactly overhauled his identity, but with Eat Me, Drink Me, he's at least tweaked his approach a bit. [...] It's still plenty dark, with Manson dishing about vampires and mutilation in a horror-ific croak that's rougher than ever. [...] Some of Eat Me, Drink Me is ho-hum and bone-dry, with few hot choruses and even fewer chord changes. But unlike those breast implants he once had, it's nothing to be embarrassed about." On May 31, the entire album was uploaded for streaming on Marilyn Manson's Myspace page, five days prior to its
```

### Album 159, chunk 18

```text
American release. When released, it debuted at number eight on the US Billboard 200 with 88,000 copies sold in its first week. Elsewhere, Eat Me, Drink Me reached the top five in Austria, France, Germany, and Switzerland, and the top 10 in Australia, Canada, Finland, Spain, Sweden, and the United Kingdom. The album debuted at number 15 on the Oricon Albums Chart in Japan, selling over 17,000 copies in its first week. About.com nominated the album the 10th best rock album of 2007 and said: "One of Marilyn Manson's least calculatedly 'shocking' records, Eat Me, Drink Me may also be one of his best, favoring sturdy new wave hooks instead of cheap horror-movie theatrics. The welcome return to inspired songwriting also reinvigorates his dark introspection, such as on 'If I Was Your Vampire', a bloodcurdling tale that merges vampire lore with a story of a dangerously obsessive relationship. Eat Me, Drink Me is a reminder of what Manson does best: turning scary industrial rock noises into universal messages of fear and self-doubt." The Rape of the World Tour is the eleventh tour Marilyn Manson embarked on, under management of major record label Interscope Records. It was also the band's seventh tour to span over multiple legs. The band was on the tour from May 26, 2007, until March 2, 2008. During the North American dates the band toured with thrash metal band Slayer and metalcore band Bleeding Through. During the Australian dates, Manson was supported by Australian pop-punk band The
```

### Album 159, chunk 19

```text
Spazzys, who received harsh criticism from the crowds. During the Winter European tour leg the band was supported by Turbonegro. The support act for the Winter North American tour leg was OURS. For this tour Manson returned to the theatrics of the Grotesk Burlesk Tour, some influenced by Alice in Wonderland. Initially, Manson took to the stage wearing a leather jacket with cut off gloves and a black, long-sleeved shirt to perform the opener, "If I Was Your Vampire" and the follow-up, "Disposable Teens". When first performed as an encore on the European tour, Manson took to the stage for either "Are You the Rabbit?" or "The Nobodies" (and in the case of Paris, the album's title song), wearing a striped white-gold, long-sleeved shirt. Manson later replaced the long-sleeve shirt for a black T-shirt with cut off sleeves. When the butcher knife microphone debuted, Manson performed the first song like this but also wore black, elbow-length gloves. On certain dates, Manson wore silver pants with his black shirt. "If I Was Your Vampire" then began to be performed in a black frilly shirt and a black feather boa and pink gloves for "Are You the Rabbit?". Following his appearance with Alice Cooper, Manson began to take to the stage in a T-shirt depicting a cartoon of a bunny rabbit, or on later occasions, a cut-off T-shirt with a skeleton chest on. Costume changes on these dates after the distinctly nontheatrical European tour first leg featured a top hat and striped
```

### Album 159, chunk 20

```text
pants (occasionally a leather trench coat and jacket) for "Mobscene", a jacket with '333 HALF EVIL' patched onto it, and even at some dates, a boxing gown for "The Fight Song" with the iconic twisted heart on the front and the bleeding MM logo on the back, as well as a white jacket, reminiscent of Elvis Presley, for "Rock Is Dead" at later dates. Contrasting these changes, Manson still performed "Antichrist Superstar" in the black business suit/red shirt ensemble, sometimes changing into a silver version of the rabbit shirt for later performances of "The Beautiful People" on dates on the European tour. Limited edition tour posters sold during the January to March 2008 Winter tour became important for the album's promotion. Each poster, printed and designed by Print Mafia, was limited to 100 runs each with a unique design available for, and exclusively in, each city of the tour. The dark themed poster designs featured serial killers (namely many of which the band members adopted the latter half of their stage names from), models and actresses (a handful of which the band members adopted the first of their stage names from), martyrs, iconic figures which represent the themes of Eat Me, Drink Me and various horror films.
```

## Album 160: Baggariddim — UB40

- **album_id:** `7128967c-c6ad-42c7-b259-d5c37272fb6b`
- **Tags (identification only):** reggae, album rock, deejay, pop reggae, pop, pop/rock, reggae pop
- **Chunks:** 1 (199 words)

### Album 160, chunk 1

```text
Baggariddim is the sixth album by UB40, released in 1985. Most of the tracks are reworkings of previous UB40 recordings that originally appeared on Labour of Love and Geffery Morgan, here showcasing guest singers and "toasters" on vocals. Guest artists included Chrissie Hynde, the leader of The Pretenders, and Douglas Gilbert, lead trombonist with the London Symphony Orchestra (LSO). In the UK, Germany, the Netherlands and Belgium, this album was released in a gatefold sleeve containing an additional 3-track 12" EP. The album features two hits, "I Got You Babe"—a duet with Hynde that reached number one in the UK, Ireland and Australia—and the UK number-three follow-up "Don't Break My Heart", which was the 'B-side' of "I Got You Babe" ("Theme from Labour of Love") with vocals added. The album was not released in the US or Canada, where instead an EP entitled Little Baggariddim was released. Nick Phipps – tape op In 2021, UB40 released Bigga Baggariddim, their 20th album, which features collaborations with artists from the original Baggariddim and newer reggae artists. Songs on the new album include "Good Vibes Tonight" and "Message Of Love", while guests include Tippa Irie, KIOKO, House of Shem and Inner Circle.
```

## Album 161: It’s Hard — The Who

- **album_id:** `006984a4-1e2d-4a1e-982e-70619de38401`
- **Tags (identification only):** hard rock, rock, album rock, classic rock, freakbeat, mod, pop rock, rock opera
- **Chunks:** 5 (1088 words)

### Album 161, chunk 1

```text
It's Hard is the tenth studio album by the English rock band the Who. Released in September 1982, it was the final Who album to feature bassist John Entwistle, who died in 2002. It was also the second and final Who studio album with drummer Kenney Jones, as well as the last to be released on Warner Bros. Records in the US. It was released on Polydor Records in the UK, peaking at No. 11, and on Warner Bros. in the US where it peaked at No. 8 on the Billboard Pop Albums chart. The US rights to both this album and Face Dances subsequently reverted to the band, who then licensed them to MCA Records (later Geffen Records, itself once distributed by WB) for reissue. The album achieved gold status by the RIAA in the US in November 1982. It was their last album for over two decades until Endless Wire in 2006. The album cover, designed and photographed by Graham Hughes, depicts a young boy playing an Atari Space Duel arcade game. This is intended as a reference to the song "Pinball Wizard", from the album Tommy. The first track on the album, "Athena", peaked at No. 28 on the Billboard Pop Singles chart. "Dangerous", "It's Your Turn" and "One at a Time" were written by Entwistle, but he only sang lead vocals on "One at a Time" with Daltrey singing lead on the two others. In 1997, MCA Records re-released the album with new mixes for several
```

### Album 161, chunk 2

```text
songs, correcting problems evident in the original mixes for "Athena" and "Eminence Front". In 1994, Daltrey said "It's Hard should never have been released" and that he also had arguments with Townshend over the release of the album. He stated the record company wanted them to make a new record, then do a tour for the album, so in many ways they were forced to release it. In a 1985 interview, Townshend said, "Face Dances and It’s Hard were made by a band who were very unsure about whether or not they wanted to be making a record, and I think that’s a terrible doubt." Alternate takes exist of "Eminence Front" featuring Roger Daltrey on lead vocals and "One Life's Enough" featuring Pete Townshend on lead vocals. "I've Known No War" features the orchestra arrangement from the 1979 Quadrophenia film version of "I've Had Enough". Critical reviews on its release in 1982 were polarized. Parke Puterbaugh of Rolling Stone gave it the magazine's highest rating (5 stars) and commented that it was "their most vital and coherent album since [the 1971 album] Who's Next". Puterbaugh also proclaimed that the song "I've Known No War" was "a song that could become an anthem to our generation much the way 'Won't Get Fooled Again' did a decade ago." Robert Christgau, on the other hand, icily disparaged the "prolix" nature and "operatic pretensions" of Townshend's musical ideas, as well as his "book-club poetry". Stephen Thomas Erlewine of AllMusic considered the album to be
```

### Album 161, chunk 3

```text
an "undistinguished final effort" with "few memorable melodies and little energy". Just over half of this album has been played live over the course of the band's career, most of the performances coming from the then farewell tour in 1982 supporting the album. "Dangerous" was the first song from this album to be played live, as the third song on the band's first 1982 concert. Its live performances did not deviate too far from the studio cut. "Athena" was played sporadically on the 1982 tour, sometimes as an encore and at other times in the regular set. The band hated playing the song and thought that their performance on it was not up to their standards, so they dropped it mid-tour. "A Man Is a Man" was also played sporadically on the same tour, and its last performance also came during the same concert with the last performance of "Athena". "It's Hard" was played throughout the entire 1982 tour and regularly featured a short full-band jam at its conclusion. "Cooks County" was only played once, on 6 October 1982 at the Rosemont Horizon in Chicago, in place of "It's Hard". This was because the song was written by Townshend after seeing a television documentary on Chicago's Cook County Hospital. "Eminence Front" was one of two songs (the other being "Cry If You Want") from this album to last until after the 1982 tour, and the only one to become a staple of the band's concerts. It was played in the
```

### Album 161, chunk 4

```text
tours of 1982, 1989, 1999, 2002, 2004, 2006–2007, 2008, 2009, 2014, 2015, 2016, 2017, 2019, and 2022. "Cry If You Want" was played in every 1982 concert except one. These performances featured Townshend playing an extended guitar solo as an outro. In 2006, Daltrey requested that it be brought back, and it was for the first leg of the tour. However, it did not stay in the set list for long, only lasting three concerts. Later, the band would start incorporating it into their jams of "My Generation", albeit in a shorter and jazzier form, where it lasted until 2009. The song was briefly revived for The Who Hits 50! tour in late 2014. On 24 December 2011 the original mix of the album was reissued in Japan in a miniature replica of the original album art work. The album was remastered by Jon Astley for this reissue using Direct Stream Digital (DSD) to transfer the analog master tape to digital and included the bonus tracks added to the CD release of the album. The release was a limited edition in the SHM-CD format. The reissue included a picture of the original vinyl label. Roger Daltrey – lead vocals, rhythm guitar, backing vocals on "Eminence Front" and "One at a Time" Pete Townshend – lead and rhythm guitars, synthesisers on "Eminence Front" and "One Life's Enough", Yamaha E70 organ on "Eminence Front", piano on "One Life's Enough", backing vocals, lead vocals on "Eminence Front", co-lead vocals on "Athena" and "Cooks
```

### Album 161, chunk 5

```text
County" John Entwistle – bass guitar, horns, backing vocals, lead vocals on "One at a Time", synthesisers on "Dangerous" and "One At A Time" Kenney Jones – drums Andy Fairweather Low – rhythm guitar on "It's Your Turn" Tim Gorman – synthesisers on "Dangerous", "One Life's Enough" and "One At A Time", organ on "Dangerous", Rhodes electric piano on "Eminence Front" Glyn Johns – Producer, engineer Jon Astley – Executive producer Chris Charlesworth – CD reissue executive producer Bill Curbishley – Executive producer Robert Rosenberg – Executive producer
```

## Album 162: Shout — DEVO

- **album_id:** `af8b9fa6-32e8-4c65-a2b6-077947292fe5`
- **Tags (identification only):** synth pop, electronic, electro, fairlight cmi, new wave, pop rock, rock
- **Chunks:** 5 (1229 words)

### Album 162, chunk 1

```text
Shout is the sixth studio album by American new wave band Devo, released on October 8, 1984, by Warner Bros. Records. Arriving two years after their previous studio album, Oh, No! It's Devo (1982), the album retained the synth-pop sound of their previous few records, with an extensive focus on the then-new Fairlight CMI, Series IIx digital sampling synthesizer. Despite the popularity of synth-pop in 1984, the album was a critical and commercial failure, peaking at only No. 83 on the U.S. Billboard 200 and ultimately leading to Warner Bros. dropping the band from their label. Shout was recorded during a period of creative differences, and tensions within the band for the first time, and most of the band members have since stated that they were not satisfied with the completed album and Devo subsequently went on hiatus for four years following its release. Additionally, Alan Myers, who had played drums for the band since 1976, departed after the release of the album, citing a lack of creative fulfillment stemming from the band's increasing use of drum machines and programming. Although Devo would go on to release two further studio albums through Enigma Records, they would not release another studio album through Warner Bros. until their ninth album, Something for Everybody (2010). Shout was recorded over a period of ten months between July 1983 and February 1984, in sessions that took place at the Record Plant in Los Angeles, California. Over the course of their career, Devo had been transitioning
```

### Album 162, chunk 2

```text
away from using analog synthesizers. Shout made extensive use of digital equipment such as the Fairlight CMI, as well as the LinnDrum, Emulator and the Synclavier II. Mark Mothersbaugh enjoyed the process of sampling real instruments, as well as blending acoustic samples from the Fairlight CMI's factory preset library with the band's synthesizer tracks. As such, the compositional process for the band became more insular for him. Gerald Casale has stated that Mothersbaugh purchased the Fairlight CMI with band money and introduced it into the sessions, and that Casale reluctantly agreed to its use because he'd heard that Depeche Mode had used one. After some experimentation, Casale and other band members were dissatisfied with the results, so he suggested centering the album on the use of bass, drums and guitar, reserving the Fairlight CMI for sequencer lines, "scary sounds" and "abstract element[s]". Mothersbaugh eventually rejected this idea, and as a result, Casale began withdrawing from the sessions. "Here to Go" was inspired by British-Canadian artist Brion Gysin's theory that constant change was the meaning of life and an essential component for humanity. Warner Bros. initially rejected the album and asked that the band include a cover version, with Casale suggesting the Jimi Hendrix Experience's "Are You Experienced?". Shout was the final studio album by the 1976–1985 line-up of Devo, with their third and most prominent drummer, Alan Myers, leaving the band shortly after the album's release. According to the book We Are Devo, Myers cited a lack of creative fulfillment
```

### Album 162, chunk 3

```text
as his reason for leaving the band, something that he had felt since Devo's move to Los Angeles in the late 1970s. Devo's increased use of drum machines and electronics through the years had greatly reduced Myers' role in the band, although Casale has said that he begged Myers not to leave. In a 2007 interview with Billboard magazine, Casale stated that Shout was the biggest regret of his career, "because the Fairlight just kind of took over everything on that record. I mean, I loved the songwriting and the ideas, but the Fairlight kind of really determined the sound." According to a 2005 interview with the band's guitarist, Bob Mothersbaugh, "Mark and Jerry kept saying in interviews that the guitar was obsolete and wanted to prove it with the Shout album." In 2016, Casale, in response to a question from a fan on Twitter, stated that recording the album was even "too painful to talk about." In 2025, Mark Mothersbaugh stated that "I don’t think any of us feel like we love it", adding that "by the time we got to Shout, me and Bob Casale were the only ones that were showing up for rehearsal and writing". The album's cover photograph, taken by Karen Filter, is a head shot of Timothy Leary's son Zachary Leary (credited as Zachary Chase) on a composite background with his left hand raised by his open mouth in a "shout" gesture. The album's back cover depicts a head shot photo of guitarist Bob
```

### Album 162, chunk 4

```text
Mothersbaugh's daughter Alex with her eyes focused upwards and her left hand raised by her ear in a listening gesture. It is notably their first studio album since 1978's Q: Are We Not Men? A: We Are Devo! not to feature any of the band's members on the outside cover. As with every Devo studio album, the band developed a new look for the album, eschewing the black T-shirts and slacks with white "Spud Ring" collars of the Oh, No! It's Devo (1982) period and replacing them with "Chinese—American Friendship Suits." The band was allotted $50,000 to make a music video for "Are You Experienced?". However, the band drew criticism that the video, which featured white Hendrix impersonator Randy Hansen emerging from a coffin, was "tasteless" and "disrespectful", which did not aid the album's reception. As a result, the band did not tour to promote the album, leading Warner Bros. to ultimately offer a termination of the band's new six-album contract in exchange for $250,000. Despite being one of Devo's most visually complex and expensive music videos, "Are You Experienced?" wasn't included on the 2003 DVD music video collection The Complete Truth About De-Evolution (although it had been included on the LaserDisc of the same title issued in 1993). In an interview with Gerald Casale for Ear Candy, he explained: E.C.: Speaking of de-evolution, why didn't the Hendrix estate give you permission to put the "Are You Experienced?" video on the DVD? Gerald Casale: Further de-evolution. You understand that the
```

### Album 162, chunk 5

```text
consortium of people that now represent the Hendrix estate are basically run by lawyers; the lawyer mentality. Lawyers always posit the worst-case scenarios. Though that video was loved for years by anybody who saw it including the man who commissioned it —Chuck Arroff, a luminary in the music business, who still claims to this day that it was one of his five most favorite videos ever—, they [the lawyers] didn't get it and assumed we were making fun of Jimi. That's like saying "Whip It" makes fun of cowboys. This is so stupid it's unbelievable. Writing for The Village Voice, music journalist Robert Christgau stated, "Marking time (actually, a computer marks it for them), they create the rock—no, new wave—equivalent of baseball's 'Play me or trade me.' I played it. Now I'm trading it." Mark Deming of AllMusic retrospectively called it a "forgettable, slick and glossy product with all human surfaces stripped away." Mark Mothersbaugh – vocals, keyboards, guitar Gerald Casale – vocals, bass guitar, keyboards Bob Mothersbaugh – lead guitar, vocals Bob Casale – rhythm guitar, keyboards, vocals Alan Myers – drums Devo – producer, graphic concept Mike Shipley – mixing (tracks 1–9) Jim Mothersbaugh – technical assistance Will Alexander – programming consultation Al Horvath – additional Emulator programs Bill Wolfer – additional Emulator programs Effective Graphics – computer graphics Clacton and Frinton – Devo's Chinese—American Friendship Suits
```

## Album 163: Off to See the Lizard — Jimmy Buffett

- **album_id:** `b011263b-b3f7-45bf-bb25-4e0e942f9957`
- **Tags (identification only):** rock, contemporary pop/rock, country rock, pop rock, pop/rock, tropical rock
- **Chunks:** 3 (562 words)

### Album 163, chunk 1

```text
Off to See the Lizard is the seventeenth studio album by the American music singer-songwriter Jimmy Buffett. Initially to be called Stranger than Fishing, it was released in June 1989 as MCA 6314 and was produced by Elliot Scheiner and Buffett. The album is the first to feature much of the current Coral Reefer Band. Following the release of this album, Buffett paused his normal output of one album every year or two and did not release another album until 1994's Fruitcakes. All but one of the album's songs were written or co-written by Buffett. "Mermaid in the Night" was written by Coral Reefer Band members Roger Guth and Jay Oliver. "Boomerang Love" also appeared on the soundtrack to the 1989 movie Always. Buffett recorded a live version of "The Pascagoula Run" for his 2003 greatest hits collection Meet Me in Margaritaville: The Ultimate Collection. Most of the songs are related to Jimmy's first book of stories, Tales from Margaritaville, released the same year. A music video for "Take Another Road" was filmed at the abandoned Islander Drive-In Theater on Stock Island, just outside of Key West, Florida. Off to See the Lizard reached No. 57 on the Billboard 200 album chart. The song "Take Another Road" hit No. 18 Adult Contemporary. Jimmy Buffett – vocals, rhythm guitar Jay Oliver – keyboards, percussion Peter Mayer – backing vocals, guitars Jim Mayer – bass Roger Guth – drums Robert Greenidge – steel drums Michael Utley – organ Greg "Fingers" Taylor –
```

### Album 163, chunk 2

```text
harmonica Ralph MacDonald – percussion "The Nuff Brothers" – Alan Rubin, Birch Johnson, Lou Marini – horns Diana Canova, Sheryl Crow, Frank Floyd, Timothy B. Schmit – backing vocals "Take Another Road" b/w "Off To See The Lizard" (7" single released on MCA 53675 in May 1989) "Carnival World" b/w ? (cassette single released on MCA ?) 1989 brought yet another summer tour, with all the usual stops, but this time Jimmy had brought back the Neville Brothers for an opening act. In April, Jimmy played Jazz Fest for the first time, while December brought the mini "Buffett Does Ballads" Tour with Mac McAnally and Larry Knight in support of the new book Tales from Margaritaville. Jimmy Buffett: Vocals and guitar Peter Mayer: Guitar Jim Mayer: Bass Roger Guth: Drums Michael Utley: Piano Greg “Fingers” Taylor – Harmonica, Background Vocals Robert Greenidge: Steel Drums Jay Oliver: Keyboards Dena Iverson: Vocals Every night "Carnival World" was the opener and "Volcano" was the set closer. "Gravity Storm" and "A Pirate Looks at Forty" were played during the encore, with the latter closing the show. More often than not, "Changing Channels" would be added to the set after "Pirate" and would end the show. The Randy Newman cover "Louisiana 1927" was added to the set after "Pirate" for the Austin, TX show, its only appearance of the tour. Average set list: "Carnival World" "Jolly Mon Sing" "Grapefruit—Juicy Fruit "Boat Drinks" "Cheeseburger in Paradise" "Off to See the Lizard" "That's My Story and I'm
```

### Album 163, chunk 3

```text
Stickin' to It" "Come Monday" "Son of a Son of a Sailor" "Changes in Latitudes, Changes in Attitudes" "Why Don't We Get Drunk" "Twelve Volt Man" "He Went to Paris" "Take Another Road" "Boomerang Love" "Margaritaville" "Pencil Thin Mustache" "Fins" "Some White People Can Dance" "Volcano" Encore: "Gravity Storm" "A Pirate Looks at Forty" "Changing Channels" (played about 4/7 of the time)
```

## Album 164: Give Us Barabbas — Masters of Reality

- **album_id:** `cb24f17f-6a56-4495-81fa-2b333fa49c3c`
- **Tags (identification only):** blues, blues rock, electric blues, folk rock, rock, acoustic, hard rock, heavy metal
- **Chunks:** 1 (142 words)

### Album 164, chunk 1

```text
Give Us Barabbas is the fifth studio album of the American rock band Masters of Reality, released in 2004. Material for the album comes from sessions for a planned release on Epic Records in the mid 1990s entitled The Ballad of Jody Frosty, which was shelved at the time, hence the change in line-up. The recording coincides with the live album How High the Moon, released in 1997. Chris Goss – vocals, guitar, keyboard Googe – bass guitar Victor Indrizzo – drums Chris Palmer – drums ("It's So Hard") Ginger Baker – drums ("The Desert Song") Scott Weiland – guest vocals ("Jindalee Jindalie") Lily Haydn – violin ("Brown House on the Green Road") Andy Kaulkin – electric piano ("Brown House on the Green Road") Brendon McNichol – mandolin and balalaika guitar ("Off To Tiki Ti", "Hey Diana", "I Walk Beside Your Love")
```

## Album 165: Back From the Edge — James Arthur

- **album_id:** `c76b75f4-e75b-4017-87f9-0a6ca3aa1b5a`
- **Tags (identification only):** pop, pop rock, rock, soul
- **Chunks:** 2 (474 words)

### Album 165, chunk 1

```text
Back from the Edge is the second studio album by British singer and songwriter James Arthur. It was released on 28 October 2016 by Columbia Records. The album reached number one on the UK Albums Chart and was certified platinum—denoting 300,000 sales—the following year, in September 2017. It includes the multi-platinum number-one single "Say You Won't Let Go". Following his self-titled debut studio album being released on 1 November 2013, peaking to number 2 on the UK Albums Chart, on 5 April 2014, several media outlets began to report that Arthur had been dropped from Syco, following a dispute regarding a song entitled, "Follow the Leader". He took to Twitter to deny the claims, however on 11 June 2014, Arthur announced via Twitter that he and Syco had parted ways by mutual agreement. During the summer of 2014, Arthur stated that he was working on his second album and was close to signing a new record deal. On 6 September 2015, he announced that he had signed with Columbia Records and that a new album was on the way. On 9 September 2016, he released "Say You Won't Let Go" as the official lead single from the album. The single peaked at the top of the UK Singles Chart, a position it maintained for three weeks. Outside the United Kingdom, the single has topped the charts in Australia, New Zealand, Sweden, Singapore, Indonesia and the Republic of Ireland. The music video was released in the same month and was directed
```

### Album 165, chunk 2

```text
by Felix Urbauer. On 10 February 2017, "Safe Inside" was released as the album's second single. The music video was released slightly before on 25 December 2016 and was directed by Frank Hoffman. Arthur performed the song at the 2017 National Television Awards. Four years later, the album track "Train Wreck" entered the top 20 on the UK Singles Chart after becoming popular in videos on the video app TikTok. On 8 January 2016, Arthur released a new song called "The Truth" on iTunes in the United States. Following the song's release, he took to Twitter and clarified that the song would feature on Family Therapy with Dr. Jenn, and that it was not the lead single, only a promotional single. On 21 October, a duet version of "Let Me Love the Lonely" was released as a promotional single only in Poland, featuring Polish singer Marina. The song was certified double Platinum in the country. Digital Spy gave the album 4 out of 5 stars, labeling it "the anti-X Factor album" and further stating that "This is the winner we all wanted". Back from the Edge debuted at number one on the UK Albums Chart, selling 40,906 copies during its first week of release. The album was certified platinum in September 2017 by the British Phonographic Industry, denoting sales of 300,000 in the UK.
```

## Album 166: Still Life — Van der Graaf Generator

- **album_id:** `6c386d97-4c02-4cce-af09-2f39376296c2`
- **Tags (identification only):** progressive rock, art rock, based, experimental, rock
- **Chunks:** 2 (421 words)

### Album 166, chunk 1

```text
Still Life is the sixth album by English progressive rock band Van der Graaf Generator, originally released in April 1976. It was their second album after reforming in 1975, the first being Godbluff. One live bonus track was added for the 2005 re-mastered re-release. A new remaster, along with new Stereo and 5.1 surround sound remixes by Stephen W Tayler, was released on 3 September 2021. The album front cover, photographed by Paul Brierley, shows a Lichtenberg figure. The image was described by journalist Geoff Barton in Sounds: "It's actually a frozen-in-action shot of an electrical discharge from a real Van de Graaff generator machine, set in acrylic." Geoff Barton of Sounds wrote: "Where 'Still Life' scores over past LPs is in its precise and accurate reproduction of leader Hammill's vocals. He never really sings, rather he murmurs, shouts, screams or speaks, and this wide range of tonality has presented in the past often insurmountable problems for engineers, technicians and suchlike. Here, however, every subtle nuance of the 'chords has been captured successfully, providing greater variation, an abundance of light and shade. ... 'Still Life' is an essential album. If you think you have problems, listen to Hammill's and you'll probably never be able to worry about anything insignificant ever again." Jonathan Barnett of New Musical Express, describing the songs on the album, wrote: "They start off with the kind of morbid over-sensibility, y'know ... smart ass existentialist one-liners like that, accompanied by furtive, lurching manic melodies that emphasise the
```

### Album 166, chunk 2

```text
personality disorientation of the whole thing." Steven McDonald, for AllMusic, notes that Hammill songs take "... a dead run at a grandiose concept or two – the consequences of immortality on the title track, and the grand fate of humanity on the epic "Childlike Faith in Childhood's End." McDonald concludes: "The true highlight, however, is the beautiful, pensive "My Room (Waiting for Wonderland)", with its echoes of imagination and loss. Hammill did not achieve such a level of painful beauty again until "This Side of the Looking Glass" on Over." Interviewed by Mojo in 2002, Hugh Banton said: "I remember doing Still Life, which is possibly my favourite Van der Graaf album of all, and Charisma came along and said 'Oh, this is just a stop-gap album'. The stop-gap album!? We don't make stop-gap albums!" Peter Hammill – vocals, guitar, piano David Jackson – tenor and soprano saxophones, flute Hugh Banton – Hammond organ, bass, Mellotron, piano Guy Evans – drums, percussion Pat Moran – engineer, mixing Arun – lacquer cut
```

## Album 167: Staying at Tamara’s — George Ezra

- **album_id:** `953dcc32-2faf-4595-869e-c6de8065777d`
- **Tags (identification only):** blues, folk rock, pop, pop rock, rock, folk, indie pop
- **Chunks:** 2 (542 words)

### Album 167, chunk 1

```text
Staying at Tamara's is the second studio album by English singer-songwriter George Ezra. It was released on 23 March 2018. The album reached number one in the UK as well as the top ten of several other countries including Australia and New Zealand. The album includes the singles "Paradise" and "Shotgun", which peaked at number two and number one on the UK Singles Chart, respectively. It was the UK's best-selling artist album of the year in 2018 and was nominated for British Album of the Year at the 2019 Brit Awards. In support of the album, Ezra embarked on a 2018 world tour entitled, Staying at Tamara's Tour, mostly visiting cities across North America and Europe. Ezra finished touring his debut album Wanted on Voyage (2014) in December 2016. Following this, he realised "he had to write another record". He went to Barcelona for a month, but instead of booking a hotel or apartment, he found a stranger on the Internet whose name was Tamara. "[She] was renting her spare room," he told The Sydney Morning Herald. "I thought, if she's a bit crazy, if she's a bit unhinged, I can just leave. Her friends were all musicians, artists and designers and her apartment really felt like their HQ. It helped slow me down. There was a point about halfway through the trip where I was like, this trip has proved to be really important ... and the album's name came to me like that. I love it." Five singles
```

### Album 167, chunk 2

```text
have been released from the album. "Don't Matter Now" was released as the lead single on 16 June 2017. It was a moderate success in Belgium, Iceland and the Netherlands and gave Ezra his seventh top 75 entry on the UK Singles Chart. The second single released from the album was "Paradise", which peaked at number two, being kept off the top spot by Rudimental's "These Days". It also reached the top ten in Ireland, Belgium, Austria and Scotland. "Shotgun" was released as the third single from the album on 18 May 2018; it reached number one on the UK Singles Chart on 29 June 2018 and gave Ezra his first UK number-one single. "Hold My Girl" was released as the fourth single from the album in late-September. "Pretty Shining People" was released as the fifth single in early-March. "Pretty Shining People" was released as the first promotional single from the album on 2 March 2018; it reached number 54 on the UK Singles Chart.The track was later selected as the album's fifth single in March 2019. "Hold My Girl" was released as the second and final promotional single on 9 March 2018, and reached number 81 on the UK Singles Chart. The track was later selected as the album's fourth single, and impacted radio in September 2018. At Metacritic, which assigns a normalised rating out of 100 to reviews from mainstream critics, the album has an average score of 61 based on seven reviews, indicating "generally favorable reviews". Cam Blackwood – production (all tracks), engineering (tracks 2, 6) Fred – production (track 8) Dan Grech-Marguerat – mixing (tracks 1–7, 9–11) Michael H. Brauer – mixing (track 8) Charles Hicks – mixing assistance (1–7, 9–11) Joel Davies – mixing assistance (1–7, 9–11)
```

## Album 168: Sacrifice — Gary Numan

- **album_id:** `c30a8328-fe16-464d-82e4-9d82195ca525`
- **Tags (identification only):** electro, electronic, experimental electronic, industrial, new romantic, new wave, pop/rock, punk/new wave
- **Chunks:** 2 (413 words)

### Album 168, chunk 1

```text
Sacrifice is the twelfth solo studio album by the English musician Gary Numan, released in October 1994 by Numa Records. Its release is often cited as marking the start of a critical and artistic rejuvenation for Numan. The album was released in the US in 1997 with a different title, Dawn, based on the comic book character Dawn. It also carried cover art by Joseph Michael Linsner. A number of tracks displayed an antipathy towards religion, a stance that had been noted in isolated songs from early in Numan's career but which became more pronounced on this album and its successors, Exile (1997) and Pure (2000). While Exile was a fictional story, Numan later stated that "Sacrifice looks at my actual beliefs." An "extended" version of Sacrifice, approximately twenty five minutes longer than the original, was released in 1995. The same year, most of the tracks appeared on Dark Light, Numan's live recording from the Sacrifice tour. The album was released in 1999 with extra tracks in the US and UK by Eagle Records (Cleopatra Records). The US edition has a somewhat different selection of extra tracks in addition to new artwork, just like earlier reissues of albums that were first published on Numa Records. Sacrifice began as a follow-up to Machine & Soul continuing with producer Kipper. This initial project was abandoned when Numan decided to instead self-produce the album and adapt several tracks from his 1994 soundtrack, The Radial Pair: Video Soundtrack. "Metal Beat", later released as a
```

### Album 168, chunk 2

```text
bonus track, was a demo intended for this earlier version of the album, where it would have been the title track, "Vicious". In a 2000 interview, Numan described his approach to the recording. Prior to Sacrifice, "I spent quite a few years just trying to write songs that would get me back on the radio". For the new album, "I just went right back to the way I was when I was a teenager, first time writing songs, with all the enthusiasm for it". The resultant music, whilst not a commercial success, garnered Numan his best notices in years and coincided with the beginnings of a critical reassessment of his career and acknowledgment of his influence on such artists as Nine Inch Nails, Foo Fighters, Marilyn Manson, The Magnetic Fields, The Prodigy and Afrika Bambaataa. Gary Numan – all instruments and vocals, production, arrangements Kipper – additional guitar on "Scar", synth bass on "Love and Napalm" TJ Davis – backing vocals on "Scar"
```

## Album 169: In Ribbons — Pale Saints

- **album_id:** `08a7f7c5-b46e-43cc-9c98-0d42f0ca72cc`
- **Tags (identification only):** shoegaze, alternative rock, dream pop, easy listening, jangle pop, noise pop, rock, rock pop
- **Chunks:** 1 (120 words)

### Album 169, chunk 1

```text
In Ribbons is the second studio album by English alternative rock band Pale Saints, released on 23 March 1992 by 4AD. It peaked at number 61 on the UK Albums Chart. Jack Rabid of Trouser Press called In Ribbons "alluring and attractive, rich in complexity and raw emotion." Martin C. Strong wrote that "the subtlety of its shredding chords and sporadic sonic dreamscapes were let loose all over the shop." MusicHound Rock: The Essential Album Guide wrote that the album "immaculately balances wide-screen guitars and soft melodies." Spin included In Ribbons in a 2007 list of "essential" shoegaze albums. In 2016, Pitchfork ranked In Ribbons at number 34 on its list of the 50 best shoegaze albums of all time.
```

## Album 170: Lemonade and Brownies — Sugar Ray

- **album_id:** `4ad12dce-4a79-46f7-91fe-87e9d4251e3c`
- **Tags (identification only):** funk metal, alternative metal, alternative rock, nu metal, punk rock, rap metal, rap rock, rock
- **Chunks:** 19 (4638 words)

### Album 170, chunk 1

```text
Lemonade and Brownies is the debut studio album by the American rock band Sugar Ray, released on April 4, 1995, by Atlantic Records. It was far less successful than the band's later releases on Atlantic. The debut album and the band's next album Floored also featured less of a pop-influenced sound than their later work. When the band got signed to Atlantic Records they had only four to five songs, including "Caboose" and "Big Black Woman" (which were featured on Lemonade and Brownies) and two other songs called "Lick Me" and "Gold Digger". Prior to getting signed, they had primarily been a cover band, and were known as Shrinky Dinx. In 1993, Shrinky Dinx created their own video for "Caboose", with their director friend Joseph McGinty "McG" Nichol, who went on to become a director for Hollywood films such as Charlie's Angels. At this point, McG served as their de facto manager and he helped them sign with the new management company of Lee Heiman and Chip Quigley, who in turn helped negotiate the subsequent deal with Atlantic. Shrinky Dinx had signed a five-year exclusive artist management deal with Heiman and Quigley, and one of the clauses that they put in the contract was that they would get them a record contract within six months. Shortly after signing with Heiman and Quigley, the "Caboose" video found its way to Atlantic Records executive Doug Morris. Drummer Stan Frazier later recalled that "Doug Morris [from Atlantic] saw the live energy in the
```

### Album 170, chunk 2

```text
video and said, 'Sign that band, this is entertaining.'" They agreed to a two million dollar deal with Atlantic, with the deal being signed at a local pizza shop in Newport Beach. California. One of the reasons Morris wanted to sign Shrinky Dinx was since he saw star potential in singer Mark McGrath, who he referred to as "the kid" during a meeting with Heiman and Quigley. Morris was so impressed by the video that he signed the band without having even heard a demo tape of theirs. McGrath believes another reason they got signed was since major labels were more willing to take chances on bands at that time, following the success of Nirvana. Once getting signed, they changed their name to Sugar Ray (after the boxer Sugar Ray Leonard), due to threats of legal action from the Milton Bradley Company, maker of the Shrinky Dinks toy. The band chose this name since they were fans of boxing and other sports. Heiman said that he had initially opposed the name Sugar Ray, since he was "afraid that everyone would just know the name from the boxer and it wouldn't work." Work on Lemonade and Brownies would begin in mid-1994, with McG serving as producer. DJ Lethal from rap group House of Pain served as a co-executive producer. Sugar Ray asked DJ Lethal to work on their album as they were a fan of the House of Pain song "Jump Around". DJ Homicide appears on a few of the album's
```

### Album 170, chunk 3

```text
tracks, and was credited as a guest musician, being excluded from a group shot of the band on the back of the album, which shows them riding a rollercoaster. He later became an official touring member of Sugar Ray. Prior to becoming involved with Sugar Ray, DJ Homicide had been working as a hip hop radio DJ in Los Angeles, and was briefly a member of rap group Tha Alkaholiks. In a July 1997 interview promoting their next album Floored, McGrath reflected that "Homicide came in toward the end of the last album and he's a clown like us. We grew up listening to Kiss and AC/DC and he's from a totally different background, so it's a great exchange." Guitarist Rodney Sheppard said in a June 1997 interview, "DJ Homicide, he's not really a killer. He's a nice guy. I call him Craig. We live together and it's unfit at the dinner table to go, 'Hey Homicide, pass the rolls'." The album title originated after recording was finished, and was inspired by an ad in a pornographic magazine, which featured a near-naked woman and the slogan "try our lemonade and brownies". The band found the magazine after moving into a house in the Los Angeles suburb of Hancock Park, which they shared during the making of this album and Floored. There were numerous other pornographic magazines in the house, since the old tenant was a collector of them. The band liked "lemonade and brownies" as an album title since it
```

### Album 170, chunk 4

```text
differs from the more conventional term "milk and brownies", which they thought reflected how their music didn't conform to just a single genre. Some reviewers believed that the album's title was a reference to urine and feces. The title is reminiscent of Ween's Chocolate and Cheese, which was released in September 1994 while Lemonade and Brownies was being made, and whose title was similarly chosen to represent that band's contrasting musical styles. The artwork for the two albums also feature similar images of scantily clad women. In 2013, bassist Murphy Karges said that he was aware of Chocolate and Cheese when it came out in 1994, and was a fan of the artwork. Karges reflected, "we just figured that a potentially controversial cover might get more people to check us out." Actress Nicole Eggert is featured on the cover of Lemonade and Brownies. On the photo, she is naked on a white fluffy rug, which resembles a cloud. She was then known for appearing on the television series Baywatch, and McGrath was dating her best friend. He said in October 1997 that the cover art helped the album gain more exposure, saying "I can't tell you how many program directors have told me they played our record because of that photo. They'd tell me that a typical CD that comes across their desk ends up in the trash, but our cover grabbed them and they put it on. And Nicole wouldn't even take a cent for it." On the album's
```

### Album 170, chunk 5

```text
liner notes the band members are credited under pseudonyms rather than their real names. McGrath is credited as "Liar", Sheppard is credited as "Traitor", Frazier is credited as "Cheat" and Karges is credited as "Sellout". Sugar Ray initially began as a hardcore punk band in 1986, but had gone through several style changes by the time they got signed to Atlantic Records, including at one point being a glam metal band. The Rolling Stone Encyclopedia of Rock & Roll (2001) states that on their first two albums, Sugar Ray were influenced by "a variety of sounds: Red Hot Chili Peppers-style punk-funk, reggae grooves, metal, hip hop, and a little bit of retro new wave." The songs on Lemonade and Brownies have been described as having elements of heavy metal, hardcore punk, funk, speed metal, blues rock, R&B, hip hop, acid jazz, arena rock, country, disco and sketch comedy. In 1999, Corey Moss of the Iowa State Daily compared their sound on this album to Faith No More. AllMusic labelled Lemonade and Brownies as being "sub-Chili Peppers shuck-and-jive." In her 2000 Sugar Ray biography book, author Anna Louise Golden states that people at the time considered the band's sound to be "putting the funk into music that was perilously close to metal", adding that "at that time, more than anything, people considered them to be heavily under the influence of the Red Hot Chili Peppers." She also said that "the music was hard, but it was fun. There was none of
```

### Album 170, chunk 6

```text
that gloom, doom and angst that permeated so much of the alternative scene." Golden categorized the song "Big Black Woman" as being a cross between blues rock and speed metal. This song was originally titled "Big Butt Woman", and McGrath told his bandmates that it was based on his humorous experience of getting hit on by a black transvestite woman. The version on Lemonade and Brownies is faster and heavier than the early Shrinky Dinx version of the song, which had more of a standard punk sound. The song "Danzig Needs a Hug" references the punk/metal singer Glenn Danzig, who is known for his dark image. It features falsetto vocals from McGrath and backing vocals from Janine Harris, a member of R&B group Slapbak, who were signed to a Warner Music Group label like Sugar Ray. Golden describes the song as being "close to disco lite". When the song came out, an interviewer asked Glenn Danzig about the song, and all he said back to the interviewer was "Sugar Ray can suck my dick", with Murphy Karges saying this was the response they expected from him. In addition to "Danzig Needs a Hug". Lemonade and Brownies also included other similarly light R&B-influenced songs, such as "Hold Your Eyes" and "Scuzzboots", with McGrath comparing these lighter songs to Boyz II Men in 1997. "Danzig Needs a Hug", "Hold Your Eyes" and "Scuzzboots" were not done in the style of short interludes, instead running the same length of time as the rock
```

### Album 170, chunk 7

```text
songs. Karges said in 2019 that he and his bandmates would call these lighter non-rock songs "vibe tracks". He added that the reason why these songs are on the album was because they "just thought it was funny" to include them. The album ends with a hidden country-influenced acoustic track, titled "One Brave Cowboy". The hidden country track follows "Streaker", one of the heaviest songs of the band's discography, which itself follows "Scuzzboots", one of the light R&B songs. Sugar Ray would later explore country music again on their 2001 self-titled album, with the track "Just a Little", while in 2015 McGrath would also go on to join the bro-country supergroup Uncle Ezra Ray, which featured him, Uncle Kracker and Better than Ezra singer Kevin Griffin. "Streaker" samples a riff from the 1979 song "Richie Dagger's Crime" by punk rock band Germs, and lyrically references MC Hammer's 1994 music video for "Pumps and a Bump", which featured him only in underwear with a group of scantily clad women. The synthesizers used throughout "Scuzzboots" were sampled from the 1977 song "Let Me Love You", by R&B musician Michael Henderson. Karges said the sound of "Scuzzboots" was reminiscent of soul singer Isaac Hayes. He added that its title jokingly references the "scuzzy little rings" people have around their ankles when they use a broken shower with dirty water, even though the lyrics in the song itself appear to be about a man who has been cheated on by a woman. Regarding their
```

### Album 170, chunk 8

```text
influences on the album, McGrath reflected in 2009, "we're such fans of all kinds of music. I love Slayer, I love The Beach Boys and everything in between. When you have five guys who write in the band — like we all do — you're going to get a lot of influences. Back then when we started we were like kids in a candy store. We were just throwing things against the wall." In a 2015 interview, McGrath said he considered their sound during this period to be a "pre nu-metal type rap/rock thing." He added, "yes, people look back on it as a 'metal record'. But if you listen to that record, there are R&B songs, soul, I'm singing falsetto on a song. If you hear the record you're hearing a band in its cocoon stage, going 'who are we?' [...] We were kind of a jokey metal/rock/punk/funk/thrash... we were the Chili Peppers with zero talent." McGrath has also said that the band were all fans of The Beastie Boys, who were known for jumping between genres on albums, with McGrath saying in 2009 that they were doing both "hardcore stuff" and "mellow stuff" on their albums. "Caboose" has a glam metal/arena rock-influenced sound, since it was written before the band got signed, and it is the only rock song on the album with guitars that were in standard tuning. It includes samples of the 1970 song "I'll Say It Again" by R&B singer Linda Tillery and the 1990
```

### Album 170, chunk 9

```text
song "Fuck tha Police" by hip hop group N.W.A. The track opens with a sound clip of a hockey announcer calling a close match. "Drive By" is a comedic skit which revolves around the band trying to order a taco from a drive-through. Despite having musical elements, Karges claimed in 2019 that he doesn't consider it to be a proper song, reflecting "we just thought it would be funny to do [...] we always just thought of like what we could do that's really stupid and funny". It has similarities to the Ween song "Pollo Asado", from their 1991 album The Pod, which is also a comedic musical skit about ordering a taco from a restaurant. The band were considering going to a real Del Taco drive-through to record the skit, although they decided against this since it would be too logistically difficult to do so. They ended up recreating the skit themselves, and used Karges's 1968 Dodge Charger to record the sounds of the vehicle in the track. To record the Dodge Charger, they had to stick a microphone to the muffler. The skit has a drumbeat playing throughout, which originated through Jason Roberts, a mixer on Lemonade and Brownies. The band had tried to incorporate this drumbeat in other songs, but had difficulty doing so, which is why they included it on "Drive By". The album opener "Snug Harbor" has been labelled as acid jazz. It uses a jazz loop that DJ Lethal had found, and the band
```

### Album 170, chunk 10

```text
came up with the lyric "hey, get up, have some fun tonight", which is repeated throughout the track. The name "Snug Harbor" is a reference to a bar that the band used to frequent at Newport Beach. The track was meant to resemble a game show intro, and was recorded at the backroom of Image Studios in Hollywood. The band liked this as an opener since it was "full of energy" and "stupid". "Dance Party USA" includes backing vocals from producer McG. His vocals weren't originally intended to appear on the track, and they were of him trying to instruct McGrath on how to sing the song. The song includes the lyric "I'm like the real world, I start in New York I'm in L.A. then Frisco", which is a reference to the MTV reality series The Real World. It is primarily built around a "big, dumb riff" which the band liked, and was regularly played live on the tour for Lemonade and Brownies. However, it quickly fell out of their setlists once Floored was released. The idea for "Iron Mic" originated through McG during a rehearsal. He wanted them to use a bassline similar to "Walk on the Wildside" by Lou Reed, and the band started developing the rest of the song from there. Karges noted that the bassline to "Walk on the Wildside" is a very common chord progression that can be heard in numerous other songs, saying in 2019 "if you're writing it's okay to take a
```

### Album 170, chunk 11

```text
very, very common chord progression, I mean how many chords and notes are there, there aren't that many. It's how your band or artist approaches playing it and plays it." McGrath wrote the lyrics to "Iron Mic", and they revolved around boxer Mike Tyson. The main guitar riff to the lead single "Mean Machine" was written by Karges, and it was directly inspired by the riff from "Who Was in My Room Last Night?", by the Butthole Surfers. In April 1995, the band described the song as lyrically being a tribute to McGrath's "barf green" vintage Cadillac car. McGrath said, "I'm psychotically in love with that car, so I had to incorporate it into the album somehow". In April 1995, McGrath claimed the other single "10 Seconds Down" lyrically revolved around his sexual inadequacy, with the song's "remote control" lyric referring to using a television remote control while in bed. He said, "I'm really bad in the sack. The problem is that I only last for about 10 seconds and I can only do it once. Seriously. Afterwards, I'll immediately need the remote control so I can switch on SportsCenter." "The Greatest" was one of the band's favorite songs to play live around this period, with Karges saying that it was the song that best showcased what each member brought to the band's sound. He also said that the song translated better in live performances than in the studio version, since the parts for the studio version were pieced together.
```

### Album 170, chunk 12

```text
The Australian and Japanese editions of the album both included songs which were not on the American version. The Japanese edition features four bonus tracks, including a live performance of a song called "Dr J". The other tracks were covers of "White Minority" and "Wasted" by the hardcore punk bands Black Flag and Circle Jerks, and a cover of the 1980 song "Wango Tagno" by Ted Nugent. Karges had previously toured with Circle Jerks in 1990, when he was temporarily part of Los Angeles punk band The Weirdos. Karges came up with the music to "Dr J", with McGrath adding comedic lyrics to the song. This live version of "Dr J" is the only one available on any of the band's releases, since a studio recording was never made for it. Rob Hillis, a friend of the band, shouts "come on horseys, run" at the beginning of "Wasted", and the band can be heard laughing as he says this. The band brought Hillis to the studio the day they recorded this cover, and were drinking budweiser beers. They asked Hillis to "go say something", which is how this line originated. Hillis later suffered a double stroke in early 2000, and that year the band did a benefit concert to help him pay for his six-figure medical bills. During the Lemonade and Brownies era, the band wrote a 1 minute song called "The Club", which is stylistically a fast hardcore punk song that incorporates electronic keyboard sounds. A live version of
```

### Album 170, chunk 13

```text
"The Club" was included on the CD single for "10 Seconds Down" in 1995. A studio version of "The Club" was also recorded for the 1998 Nintendo 64 game Road Rash 3D, appearing in both the game and its official soundtrack album. The band shot a music video for "Mean Machine" with McG, which was based on the "Caboose" video that helped them get signed to Atlantic. They later shot another video with McG in Los Angeles for "10 Seconds Down". On the album, neither of those songs used DJ Homicide and turntables, but he still appeared in the video for "10 Seconds Down", where he was pretending to perform over the pre-recorded track, since he had become a member of the band by the time it was shot. The music video for "Mean Machine" was featured in a 1995 Beavis and Butt-Head episode titled "Bang the Drum Slowly Dumbass". They also performed "10 Seconds Down" on a 1995 episode of MTV's alternative program 120 Minutes. In 1996, "10 Seconds Down" was included on the soundtrack for Escape from L.A.. That same year, "Iron Mic" was included on the soundtrack for the Ruby-Spears-produced Mega-Man cartoon. It is rumored that Mark McGrath did voice-over work for one of the show's episodes. "Hold Your Eyes", one of the lightest songs on the album, was featured in the erotic thriller film Wild Things. The film was released in 1998, the year after Sugar Ray's commercial breakthrough with Floored. "Hold Your Eyes" plays in
```

### Album 170, chunk 14

```text
a scene where Suzie (Neve Campbell) is smoking while being visited by Duquette (Kevin Bacon). Upon release, the album experienced some minor success in Europe, where similar bands like downset. and Rage Against the Machine were popular. It did not chart in the United States and was considered a commercial and critical failure for Atlantic Records. For Lemonade and Brownies, the band did seven tours in Europe, but in the United States they did only a single tour to mostly empty clubs. Since the band were playing so many shows in Europe, they used to joke to each other that "Europe loves the hard stuff". On February 2, 1996, they performed "Iron Mic" on British talk program The Girlie Show, a program which mainly featured pop artists as musical guests, such as the Spice Girls. Before they performed "Iron Mic" on the program, McGrath showed host Sara Cox how he was able to set parts of his pubic hair on fire. The previous year, they had performed "Streaker", "Mean Machine" and "Dance Party USA" on French television channel M6. Between 1995 and 1996, the band played roughly 200 shows in support of Lemonade and Brownies. During the tour, they covered Gary Numan's 1979 synth-pop song "Cars", and used the 1982 funk song "West Coast Poplock" by Ronnie Hudson during intermission breaks. During some of their songs, McGrath would occasionally mix in lyrics from new songs by other artists, such as "You Are Not Alone" by Michael Jackson and "Roots Bloody
```

### Album 170, chunk 15

```text
Roots" by Sepultura. They also performed a song called "I Love My Television" which was inspired by Van Halen's "Ain't Talkin' 'bout Love". In a recording session during the Floored era, they made a studio version of this song, along with a Weezer homage song called "Rivers" (which appeared on the Scream 2 soundtrack), but the studio version of "I Love My Television" was never released. In 2016, former manager Lee Heiman said the band became tighter musicians during the tour for Lemonade and Brownies, and were having a fun time playing at small clubs, adding that "everything was going according to plan, yet the album sales were not happening." When Sugar Ray had initially signed their two million dollar deal with Atlantic, Heiman and his partner Chip Quigley put a clause in the contract that Atlantic had to release a second record, no matter how poorly the first may have done. Heiman described this clause as a "firm two-year commitment." However, the label were considering buying out their contract due to the underperformance of Lemonade and Brownies. Sugar Ray ended up staying on Atlantic for Floored, as part of their sublabel Lava (which was established in 1995). They subsequently experienced huge success in the summer of 1997, after the release of their reggae/pop-influenced single "Fly". In September 1997, three months after Floored was released, Lemonade and Brownies had only sold 48,000 copies according to SoundScan, which was then considered a very low number for a band on a major
```

### Album 170, chunk 16

```text
label. Their newfound success with Floored and later albums help slightly raise sales over time. McGrath said in 2015 that it had sold roughly 100,000 copies by that point. Heiman claimed in 2016 that it had sold 70,000 copies. Lemonade and Brownies received a generally mixed response from critics upon its release. AllMusic's Stephen Thomas Erlewine wrote that the album is "a competent set of alternative funk/metal", but noted that "nothing on Lemonade & Brownies is particularly distinctive." In June 1995, Mike Boehm of the Los Angeles Times labelled it "juvenile", and cited it as having "the dumb-fun appeal that's the essence of frat rock." Boehm adds "with the album's cheesecake artwork and infantile, toilet-humor title, it's clear Sugar Ray is factoring its appeal down to lowest denominators with this debut CD." Kirk Miller of The Michigan Daily wrote in September 1995 that "Sugar Ray is the same feeling as having the munchies at 3 a.m. and running out to Denny's." He adds that the album is "a big ooey-gooey-chocolatey binge of phat punk-funk metal. Oh and the singer looks like Brad Pitt. Yum?". In August 1995, CMJ New Music Monthly wrote that the album "jumps hyperactively between rap, hardcore, arena rock and funk with a lot more skill and strength than you might expect (although, like so many white boys, they sound like they're trying a bit too hard to be funk-ay)". The publication further stated that, "The Beastie Boys (there's even a "Cookie Puss"-style prank phone call), Bad
```

### Album 170, chunk 17

```text
Brains and Van Halen loom large here. Although its Beasties/Peppers personality sometimes overpowers the music, Sugar Ray manages to pull it off throughout most of this LP." In April 1995, David Beran of the Gavin Report similarly wrote, "dangling their feet in the streams of hard rock and funk, Sugar Ray manage to do what the Beasties and Chilis have done." In his August 1995 review, Scott Iwasaki of the Deseret News described Sugar Ray as a "hardcore hip-metal act resembling Beastie Boys and Red Hot Chili Peppers", and said that the album has "a couple of innovative surprises". He described the opening track "Snug Harbor" as being "a little acid jazz" and said that "'Hold Your Eyes' sounds so urban you'd think Dr. Dre played a hand in the mix." New Zealand publication Rip It Up wrote in their November 1995 review that the album has "excursions into [various] musical genres, combined with a sense of humor and quirkiness." They add that, "shuffled in their deck of harder songs are laidback funk songs 'Danzig Needs a Hug' and 'Hold Your Eyes', which could easily pass as the product of a cheesy combo fitted with polyester lounge suits." David Jenison of In Music We Trust claimed in 1999 that with Lemonade and Brownies, "Sugar Ray only had three things going for them: 1) a good looking singer, 2) punk rock influences, and 3) being from Orange County, home to bands like No Doubt and the Offspring. But Sugar Ray also
```

### Album 170, chunk 18

```text
had a big problem — they didn't have any real songs." In April 1999, shortly after the release of Sugar Ray's third album 14:59, the Daily Press reflected on Lemonade and Brownies, saying that it "included songs that more closely resembled the raunchy punk-funk of the Red Hot Chili Peppers than either of Sugar Ray's [current] hits." The Rolling Stone Album Guide (2004) gave the album two out of five stars, saying "early on, Sugar Ray had a bunch of musical ideas — funk-metal, ska-pop, like that. Unfortunately, better bands had had the same ideas years before." In 2016 former Sugar Ray manager Lee Heiman said that he considered it to be their best album, in spite of its commercial failure. In 2021, Louder Sound had a positive view of the album compared to their later pop-oriented material, writing that "[Lemonade and Brownies] and its 1997 follow-up Floored are actually worth investing a little bit of your time to", adding that "we get why they 'sold out', but damn, we could have done with more of this before they went for the big pay day." In 2019, Rani Baker of Grunge.com included Sugar Ray on a list titled "Bands That Don't Sound Anything Like They Used To". She called Lemonade and Brownies a "messy funk-punk effort", and noted that, "to many folks, Sugar Ray was [just] another blonde-frosted late-'90s nothing of a band whose songs showed up in sitcoms and romcoms." Due to its sensual nature, the cover has been
```

### Album 170, chunk 19

```text
included in several lists focusing on sexual album artwork. In 2012, Danielle Bacher of the LA Weekly placed it third on a list titled "The Top Ten Sexiest Album Covers We've Ever Seen", while Ultimate Classic Rock placed it 19th on their list of "Rock's 50 Sexiest (And Maybe NSFW) Album Covers". British tabloid the Daily Star also included it on their list of "The 21 Naughtiest Album Covers" in 2023. Mark McGrath - lead vocals (credited as "Liar") Rodney Sheppard - guitars, backing vocals (credited as "Traitor") Murphy Karges - bass, backing vocals (credited as "Sellout") Stan Frazier - drums, backing vocals (credited as "Cheat") DJ Lethal - turntables, samples DJ Homicide - additional scratches Janine Harris - additional vocals on "Danzig Needs a Hug" McG - producer DJ Lethal - executive producer Jason Roberts - mixing
```

## Album 171: No Parlez — Paul Young

- **album_id:** `cf4d680a-8296-4110-948f-942d4ea177c4`
- **Tags (identification only):** pop, rock, blue eyed soul, electronic, new wave, sophisti pop
- **Chunks:** 5 (1064 words)

### Album 171, chunk 1

```text
No Parlez is the debut solo studio album by English singer Paul Young. Released in 1983, it reached number one on the UK Albums Chart (for a non-consecutive total of 5 weeks) and remained in the UK Top 100 for 119 weeks. The album has been certified quadruple platinum by the BPI for UK sales in excess of 1.2 million copies. Initially, the first two singles, "Iron Out the Rough Spots" and a remake of "Love of the Common People", had no success, but the third, a cover of the Marvin Gaye song "Wherever I Lay My Hat (That's My Home)", was No. 1 on the UK Singles Chart for three weeks in July and August 1983, and the first of Young's 14 UK Top 40 singles. Similar success followed in continental Europe. In the UK, the follow-up single "Come Back and Stay" reached No. 4, and the re-release of "Love of the Common People" made it to No. 2 in late 1983. The album was released the year after the introduction of CDs with their potential for a longer playing time. The CD edition of No Parlez featured one extra track ("Behind Your Smile") not on the vinyl release. Additionally, five of the other 11 tracks were extended versions compared to the vinyl edition. The album featured eight cover versions alongside two tracks written by Young and keyboard player Ian Kewley and one written by the guitarist in Young's band at the time, Steve Bolton. Three of the cover
```

### Album 171, chunk 2

```text
versions were written by Jack Lee who also wrote "Hanging on the Telephone" which was a big hit for Blondie. The album was released with a different cover with two tracks ("Come Back and Stay" and "Love Will Tear Us Apart") shorter in length in North America, and a new video for the single "Come Back and Stay" was made. Writing for Sounds, Garry Bushell called Young "a real prospect" and No Parlez "a creditable collection and a worthy launching pad" whose "well-varied contents prove he doesn't want to get stuck in any 'revivalist' rut." Claire Sheaff of Smash Hits commented that although Young's "velvet voice" rarely "seems to take off" on the album, she was hopeful "that this pop star will mature into a fully-fledged soul man. The potential is there." In a retrospective review for AllMusic, Dave Thompson deemed No Parlez "one of the most assured debut albums of the mid-'80s, and one of the finest pop-soul confections of all time". Laurie Latham – producer, engineer Tim Young – mastering CBS Studios (London) – mastering location Jason Bakx – sleeve artwork Eric Watson – photography Barry Watts – inner sleeve photography, Mark Irving – inner sleeve photography Martin Serene – inner sleeve photography Ged Doherty – inner sleeve photography, management Paul Young – lead vocals, backing vocals, guitars (1, 10), arrangements Ian Kewley – acoustic piano, Oberheim OB-X, E-mu Emulator, vocoder, atmospheric sounds, strings, marimbas, bells, backing vocals, arrangements Matt Irving – ARP synthesizer, Roland MC-4 Microcomposer, guitars,
```

### Album 171, chunk 3

```text
bass guitar (2, 7), backing vocals Steve Bolton – acoustic piano doodlings, guitars, lap steel guitar Pino Palladino – bass guitar (1, 3–6, 8, 10, 11, 12), Chapman Stick (1, 10) Mark Pinder – drums, Simmons drums, Roland TR-808, percussion, cowbells Rico Rodriguez – trombone (7, 11) Laurie Latham – arrangements Kim Lesley – backing vocals, congas (12) Marilyn "Maz" Roberts – backing vocals Eyethu [Nimsa Calliza, Dagmar Krause, Chief Dawethi, Eyethu, Zundi Lekau, Wally Loate, Jabu Mbato, Fats Mogoboya and Norman Zulu] – backing vocals (5) The album was re-released on 30 June 2008 in the UK and worldwide on 5 August 2008 as a 25th-anniversary edition. It contains the original 11 tracks as well as a bonus 10-track disc with a combination of B-sides, remixes and live tracks. Although the booklet claims that this is the original vinyl album on CD, three songs are shortened from their UK vinyl release; "Come Back and Stay", "Love Will Tear Us Apart" and "Love of the Common People", all of which use the respective single edits found on the original US and Canadian pressings of the album. The original UK vinyl versions of these tracks remain unreleased on CD. The Extended Club mixes of "Wherever I Lay My Hat" and "Sex", the full version of "Love Will Tear Us Apart" and the Scratch Mix of "Come Back and Stay", which were all included on the original CD and cassette release, were not included on the 25th anniversary edition. However, In 2013
```

### Album 171, chunk 4

```text
they were all included on the compilation album Remixes and Rarities. "Come Back and Stay" (Jack Lee) (single edit) – 4:24 "Love Will Tear Us Apart" (Ian Curtis, Peter Hook, Stephen Morris, Bernard Sumner) (single edit) – 4:17 "Wherever I Lay My Hat (That's My Home)" (Marvin Gaye, Barrett Strong, Norman Whitfield) – 5:18 "Ku Ku Kurama" (Steve Bolton) – 4:20 "No Parlez" (Anthony Moore) – 4:54 "Love of the Common People" (John Hurley, Ronnie Wilkins) (single edit) – 4:00 "Oh Women" (Jack Lee) – 3:34 "Iron Out the Rough Spots" (Steve Cropper, Booker T. Jones, David Porter) – 4:47 "Broken Man" (Ian Kewley, Paul Young) – 3:55 "Tender Trap" (Ian Kewley, Paul Young) – 4:31 "Sex" (Jack Lee) – 4:49 "Come Back and Stay" (Extended Club Mix) – 7:34 [different remix compared to the original CD release] "Iron Out the Rough Spots" (Extended Club Mix) – 7:28 [same version as on the original CD release] "Love of the Common People" (Extended Mix) – 5:51 [same version as on the original CD release] "Behind Your Smile" – 4:10 [same as on the original CD release] "I've Been Lonely for So Long" – 3:37 "Yours" – 5:39 [extended club mix, B-side from "Come Back and Stay") "Sex" (Demo Version) – 3:49 "Pale Shelter" (Demo Version) – 3:50 "Better to Have and Don't Need" (Live Version) – 5:57 (B-side from "Love of the Common People" 12 inch) "Wherever I Lay My Hat (That's My Home)" [Live Version] – 5:59 (B-side from "Love
```

### Album 171, chunk 5

```text
of the Common People" 12 inch) Tracks are the same versions unless stated in the notes column. It is possible to create the original vinyl version of the album by using a combination of the original UK and US CD releases together with the 'Full length' version of Come Back and Stay which is included on the 2015 Tomb of Memories career-spanning box set.
```

## Album 172: My Cute Fiend Sweet Princess — Kimya Dawson

- **album_id:** `38aba2ca-e8e1-4762-9c29-40f3890c2748`
- **Tags (identification only):** folk, rock, alternative country, anti folk, country folk, emo, experimental, folk punk
- **Chunks:** 1 (19 words)

### Album 172, chunk 1

```text
My Cute Fiend Sweet Princess is Kimya Dawson's third solo album, released concurrently with Knock Knock Who? in 2003.
```

## Album 173: Transparent Things — Fujiya & Miyagi

- **album_id:** `b32b1843-84b7-45da-aaac-0fafa19783bb`
- **Tags (identification only):** krautrock, alternative rock, disco, electronic, indie, indie rock, post rock, rock
- **Chunks:** 1 (58 words)

### Album 173, chunk 1

```text
Transparent Things is the second studio album by British band Fujiya & Miyagi, released in May 2006 by Tirk. It was re-released in 2007 by Deaf Dumb & Blind Communications in the US, with different artwork and the bonus track "Reeboks in Heaven". The title of the album comes from Vladimir Nabokov's 1972 novel of the same name.
```

## Album 174: Radio K.A.O.S. — Roger Waters

- **album_id:** `bdca939b-a5f9-45df-8aec-7a6e66fea752`
- **Tags (identification only):** concept album, rock, classic rock, electronic, progressive rock, rock and roll, rock opera
- **Chunks:** 9 (2074 words)

### Album 174, chunk 1

```text
Radio K.A.O.S. is the second solo studio album by the English singer-songwriter Roger Waters. Released on 15 June 1987 in the United Kingdom and 16 June in the United States, it was Waters' first solo studio album after his formal departure from the band Pink Floyd in 1985. Like his previous and future studio albums and many works of his during his time with Pink Floyd, the album is a concept album, based on a number of key topical subjects of the late 1980s, including monetarism and its effect on citizens, popular culture of the time, and the events and consequences of the Cold War. It also makes criticisms of Margaret Thatcher's government, much like Pink Floyd's The Final Cut (1983), another album conceived by Waters. The album follows Billy, a mentally and physically disabled man from Wales, forced to live with his uncle David in Los Angeles after his brother Benny is sent to prison following an act intended to support striking coal miners which results in the death of a taxi driver, and his dismissal from his mining job due to "market forces". The album explores Billy's view of the world through an on-air conversation between him and Jim, a disc jockey (DJ) at a fictitious local radio station named Radio KAOS. In 1979, Waters met American disc jockey Jim Ladd for a radio documentary on The Wall album, beginning a friendship which remained until Ladd's death in 2023. Ladd was an inspiration as he brought some light
```

### Album 174, chunk 2

```text
into Waters's dim view of L.A. life, initially through listening to the bizarre Fish Report from KMET. Waters became increasingly interested in Ladd's plight with his radio station KMET, and his eventual sacking to change the programming format of the station in search of market-researched profits. In 1985, Waters wrote a song called "Get Back to Radio," which seemed to be partly based on the experiences of Ladd, and partly from childhood memories – Waters fondly remembers listening to Radio Luxembourg well into the night as a child. An event from the 1985 miners' strike in Britain where a striking worker threw a concrete block off a motorway bridge, killing a taxi driver who was taking a strikebreaker to his job, seemed to register in Waters's subconscious, emerging in the second song written, "Who Needs Information" and later, "Me or Him." The album, with a working title of Home, took only three months to record, developed from 16 songs throughout 1986 and was worked into a now familiar Waters concept album. The Ronald Reagan campaign advertisements during "Me or Him" are sampled from an actual 1980 political advertisement of Reagan's. Billy is a 23-year-old Welshman from the South Wales Valleys. He is mentally and physically disabled as a result of cerebral palsy, uses a wheelchair and is only able to work his upper body. Though he is perceived as mentally challenged, his disability has actually made him not only a genius, but also superhuman, as he also has the ability
```

### Album 174, chunk 3

```text
to literally hear radio waves throughout all frequencies without aid. Billy was living with his twin brother Benny, who was a coal miner, wife Molly, and their children. Unfortunately, Benny has lost his job in the mines due to the "market forces." One night, Benny and Billy are out on a pub crawl when they pass a shop full of TV screens broadcasting Margaret Thatcher's "mocking condescension." Benny vents his anger on this shop and steals a cordless phone. Next, drunk and looking for fun, Benny poses on a footbridge and considers dropping a cinder block on the passing cars, but they decide against it ("Who Needs Information" - track 2). Later the same night, someone is killed by a concrete block dropped from a similar bridge by Benny ("Me or Him" – track 3). The police question Benny, who hides the phone in Billy's wheelchair. Benny is taken to prison, and Molly, unable to cope, sends Billy to live with his uncle David in Los Angeles, California, United States. Since Billy can hear radio waves in his head ("Radio Waves" – track 1), he begins to explore the cordless phone, recognising its similarity to a radio. He experiments with the phone and is able to access computers and speech synthesizers, and learns to speak through them. He calls a radio station in L.A. named Radio K.A.O.S. and tells them of his life story about his brother being in jail ("Me or Him" – track 3), about his sister-in-law not
```

### Album 174, chunk 4

```text
being able to cope and sending him to L.A. to live with his uncle Dave ("Sunset Strip" – track 5). Billy eventually hacks into a military satellite and fools the world into thinking nuclear ICBMs are about to hit major cities all over the world while deactivating the military's power to retaliate ("Home" – track 6, and "Four Minutes" – track 7). The album concludes with a song about how everyone, in thinking they were about to die, realises that the fear and competitiveness peddled by the mass media is much less important than their love for family and the larger community. ("The Tide Is Turning" – track 8). In the sleeve notes, Waters dedicated the album "to all those who find themselves at the violent end of monetarism." The album was recorded at Waters' own personal studio in London called The Billiard Room and mixed at Odyssey Studios in London. Recording was done with the aid of Roger Waters' backing band the Bleeding Heart Band. Morse code is a central theme in the art and style of the album, visually and audibly. The artwork for the album, designed by Kate Hepburn, are written Morse code sentences in green imprinted on a black background. The translation spans both the front and the back of the sleeve. The front cover reads ROGER/WATERS/RADIO/KAOS/WHONE/EDSINF/ORMA/TIONTH. The back cover reads EPOWE/RSTHAT/BEHO/METHETI/DEISTU/RNING/RADIO/WAVES. When translated as a whole, the artwork spells out the name of the artist, the album, and five tracks from the album. It reads:
```

### Album 174, chunk 5

```text
Roger Waters, Radio K.A.O.S., "Who Needs Information," "The Powers That Be," "Home," "The Tide Is Turning" and "Radio Waves." The code on the artwork is also heard throughout the album itself, most notably at the beginning and end of the album, book-ending the piece in the same manner as the heartbeat from Pink Floyd's The Dark Side of the Moon (1973) and the Bleeding Heart Band from The Wall (1979). Aside from eight songs that were used on the released album, additional songs appeared as B-sides. The lead single from the album, "Radio Waves", was released on 11 May 1987 as a 7" single, a 12" extended play single, and a CD single. The b-side was a non-album track called "Going to Live in L.A.". "Radio Waves" briefly went into both the American and British charts in the month of release, reaching No. 74 on the UK singles chart and No. 12 on the US Billboard Mainstream Rock chart. "Sunset Strip" was released as the second single in September 1987. The B-side included a demo of the song "Get Back to Radio" and a live version of Pink Floyd's "Money". Despite "Sunset Strip" not being released as a promo to American and British radio stations, and competing against Waters's former band whose single "Learning to Fly" was topping the US Billboard Mainstream Rock chart, it managed to go as high as No. 15. "The Tide Is Turning" was released as the third single in the United Kingdom and Australia. Without
```

### Album 174, chunk 6

```text
direct competition from Waters's former band, Pink Floyd, the single was a small commercial success in Europe. It peaked at No. 54 on the UK singles chart. "Who Needs Information?" was released in the United States in December 1987 as the fourth and final single, backed with the live exclusive "Molly's Song", another previously unreleased song. The single was in direct competition with Pink Floyd's "On the Turning Away". While Pink Floyd's singles topped the US Mainstream Rock charts back to back, "Who Needs Information?" failed to chart, despite a radio promotional release. Waters even once said in an interview that he might even release an EP with some unreleased songs from this project for those who might be interested, but this never appeared. The record was first announced via a press release from EMI on 6 April 1987, confirming Waters's new album, its details and release date. The press release mentioned that the project was conceived to be a full-out rock opera, complete with a stage show, film and live album, much like Waters's original vision for the album. Waters also made a Video EP for this album featuring the songs "Radio Waves," "Sunset Strip," "Fish Report," "Four Minutes" and "The Tide Is Turning (After Live Aid)." The Radio K.A.O.S. tour aka K.A.O.S. On the Road ran from mid-August 1987 to the end of November of the same year. It was entirely in North America except for the final two shows from Wembley, England. The tour, the largest of
```

### Album 174, chunk 7

```text
Waters's career up to that point, featured extravagant staging, props and video. The entirety of the concert was presented as a K.A.O.S. radio special, "K.A.O.S. on the Road", and featured disc jockey (DJ) Jim Ladd introducing the songs, conversing with Billy, or simply complimenting Waters and the band on their performance. The screen used for the tour displayed video of Waters, Ladd, and various other actors playing out aspects of the narrative, as well as animations and video illustrating the songs. The concert was 'interrupted' at one point each night by Billy, who played the video to the début Pink Floyd single "Arnold Layne", in remembrance of Syd Barrett. Prior to each show, Jim Ladd took calls from people in a booth and these calls were then answered by Waters. The person in each booth was usually chosen via a competition on local radio stations, in keeping with the theme of the concert. The setlist included the entire Radio K.A.O.S. album, with popular Waters-composed Pink Floyd songs mixed into the sequence, and typically lasted more than two and a half hours. The tour went heavily into debt and Waters used his own money at one point to underwrite the expense, as there were massive overruns and delays. The tour was proposed to go worldwide, but due to financial considerations these discussions never went any further, and the tour ended. Released on 15 June 1987 in the United Kingdom and the United States, the album was met with mixed reviews. It
```

### Album 174, chunk 8

```text
peaked at number 25 in the United Kingdom, 33 in Australia, and 50 in the United States. J. D. Considine of Rolling Stone magazine gave a positive review, describing the album as "by no means perfect" but "powerful". Although the themes and style of the album were criticised, he deemed it an improvement on its predecessor The Pros and Cons of Hitch Hiking (1984). Robert Christgau from The Village Voice wrote: "In which Waters's wheelchair-bound version of the deaf, dumb and blind boy learns to control the world's computers with his cordless phone, then simulates impending nuclear holocaust just to scare the shit out of the powers that be. I have serious reservations about any record that can't be enjoyed unless you sit there reading the inner sleeve, but this is not without its aural rewards – a coverable song or two and some nice comping on shakuhachi, as well as the deep engineering that made Floyd famous. As pretentious goes, not stupid." Waters has since expressed dislike for the album and the effort of creating it. "Between Ian Ritchie and myself, we really fucked that record up," he remarked. "We tried too hard to make it sound modern. Also, the part where Billy pretends that he's just started the Third World War I now find faintly embarrassing. And I dislike the backing vocals on 'The Tide Is Turning'." In addition to being dissatisfied with the production, Waters regretted trimming the album from a double to a single one, thus
```

### Album 174, chunk 9

```text
losing much of the concept. In a retrospective review, Mike DeGagne of AllMusic gave the album three-and-a-half stars, stating that, unlike some of Waters's other works, it conveys the music more than the narrative, but "while both The Pros and Cons of Hitch Hiking and Amused to Death convey his talented use of concept, imagination, and lyrical mastery, this album seems to be nothing more than a fictional tale with a blatantly apparent message".
```

## Album 175: Let’s Get Free — dead prez

- **album_id:** `39ae2571-b8f3-4cb7-a9ca-c7ee9df54240`
- **Tags (identification only):** hip hop, electronic, political hip hop, alternative rap, conscious, hardcore rap, rap, southern hip hop
- **Chunks:** 5 (1121 words)

### Album 175, chunk 1

```text
Let's Get Free is the debut studio album by hip-hop duo dead prez. It was released on February 8, 2000, on Loud Records. The album is mainly produced by dead prez, along with additional production from Lord Jamar of Brand Nubian, Hedrush, and Kanye West. The album is supported by its five singles: "Police State", "Hip-Hop", "It's Bigger Than Hip-Hop", "I'm a African", and "Mind Sex". The album peaked at number 73 on the U.S. Billboard 200 and number 22 on the U.S. Top R&B/Hip-Hop Albums chart. The album dives deep into topics such as the public education system, racism, freedom of speech and police brutality. Let's Get Free was followed up with their second studio album, RBG: Revolutionary But Gangsta in 2004, but after the duo started releasing independent work and strayed away from the mainstream. During Stic.man attendance at Florida Agricultural and Mechanical University in the mid-90s, he met M-1. Once relocating to Brooklyn after FAMU, due to their mutual love for music and similar political ideology (leftist), they both formed a rap duo in 1996. In the same year that dead prez was formed, they signed a record deal with label Loud Records. In a 2010 interview with HipHopDX, M-1 goes in depth about the beginning of the process of recording Let's Get Free. According to me, it started when I met [stic.man]. The reason I always put it in that context is because we were soon to be revolutionaries. On the mission to make sense of
```

### Album 175, chunk 2

```text
what was happening inside the world, I met stic and I'd just moved to Florida to start a new chapter in my life. My family was being destroyed by crack cocaine just like [he] was and so many families were around us. We started to put together our analysis of the world which then came to include the analysis of a revolutionary party called the Uhuru Movement and from there, I was able to put on a new set of glasses that would inform me of how I would need to move in the future in order to change these circumstances and so on and so forth. So all of this growth is what you hear on Let's Get Free. The actually recording of the album didn't happen until six years after we met. The album goes deep into topics and issues that affect the hip hop community through the duo's political view, such as the public education system, racism, freedom of speech and police brutality. Let's Get Free exposes stories such as Fred Hampton Jr having the possibility of being framed and both members relationship with Christianity. Let's Get Free is mainly produced by dead prez, along with the help of producers Hedrush, Lord Jamar, and Kanye West. The opening track of Let's Get Free, "Wolves", is centered around an metaphor by Uhuru Movement’s Chairman Omali Yeshitela related to white people distributing crack in the black community to hunters in the Arctic fooling wolves into cutting themselves and, subsequently,
```

### Album 175, chunk 3

```text
bleeding themselves to death. This metaphor explains how life under capitalism and white supremacy has engulfed the Black community in self-destructive cycles, and asks us to turn our attention to our true adversary, "the oppressor." The second track, "I'm a African", embraces a clear truth that should be apparent, but through American conditioning, it is often lost in the mind of Black folks whose family lines have resided in America for generations. M-1's verse starts with, "No, I wasn't born in Ghana, but Africa is my momma," and the rest of the song is a tribute to enslaved Africans of the past and freedom fighters such as South African anti-apartheid activist Steve Biko. Following "I'm a African", "They Schools" discusses the ways in which schools "reify the status quo, perpetuating social, state, and governmental control" and "ultimately providing lackluster education to inner city youth." The song is appropriately named to signal that public schools "belong to the government and not the people." This track encourages Black people to take control of their communities and schools as a step towards achieving true freedom. The fourth and most well-known track, "Hip-Hop", served as the opening music for Chappelle's Show (the instrumental version was used). The next track, "Police State", peeks into the situation of mass incarceration of Black men partly due to social and economic disadvantages. "Be Healthy", a mellow Spanish-guitar-driven song which is centered around the morals of veganism and the consequences of industrialized diets. One of the duo's most recognizable
```

### Album 175, chunk 4

```text
songs, "It's Bigger Than Hip-Hop", provides a critical view of the commodification of hip hop artists and music. The song exposes the government for its treatment of working-class people while at the same time, critiquing the way that the hip hop music industry "respect money over talent" and that "real music scares people." The cover art of the album depicts an open call for armed revolution by aligning "contemporary, capitalist, repressive America with colonial-era Africa in the form of an armed village preparing to strike," as stated by The Guardian. Consequently, the cover was censored in many outlets across the United States. Although the production was derided by some critics as a "dull musical backdrop" (such as Dave Heaton from PopMatters), Pound wrote that Let's Get Free was called a "return to politically conscious rap." Rolling Stone gave the album four stars and lauded its equation of "classrooms with jail cells, the projects with killing fields and everything from water to television with conduits for brainwashing by the system". Rawiya Kameir from Pitchfork wrote that "Let’s Get Free wasn't built around the aesthetics of consciousness—like some of their incense-lighting, kufi-wearing peers in the late-'90s "conscious-rap" boom [...] but around the politics of liberation." Cassie Balfour for The Michigan Daily was impressed by the album, quoting "the group's militancy, unapologetic anger and complete rejection of the commercialism — not just of hip hop (which is just a symptom of something deeper) but of American culture in general." Balfour would go on
```

### Album 175, chunk 5

```text
to state that "Dead Prez still isn’t to a lot of people’s tastes, and many would accuse the group of advocating violence. But I would argue that’s a superficial take on Let’s Get Free." Some reviewers were notably critical of the album, such as Andy Capper for NME stating that the album "sometimes [get] a little too po-faced for its own good." and tracks "like 'Mind Sex' and 'Be Healthy', while worthy in sentiment, lack the musical invention or lyrical dexterity to match the message." During an interview with the Juan EP Is Dead podcast, Stic.man revealed that Nipsey Hussle told him that he "wanted to redo Let’s Get Free and wanted [dead prez's] permission" one year before he was murdered.
```
