# Embedding text relevance, batch 9 of 12 (albums 201–225 of 300)

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

This batch: **25 albums, 75 chunks**.

## Album 201: Fixin to Thrill — Dragonette

- **album_id:** `357179e1-a16c-4071-a27b-36d5944eee0f`
- **Tags (identification only):** electronic, new wave, pop, rock, synth pop
- **Chunks:** 1 (92 words)

### Album 201, chunk 1

```text
Fixin to Thrill is the second studio album by Canadian electronic music band Dragonette, released on September 25, 2009, by Universal Music Canada. Martina Sorbara – vocals (all tracks); keyboards (tracks 2, 10–12) Dan Kurtz – keyboards, programming (all tracks); guitar (tracks 1, 3, 4, 6–11); bass (tracks 2, 3, 5–12); backing vocals (track 8); acoustic guitar (track 12) Joel Stouffer – drums (tracks 1, 2, 4–6, 8, 10–12); programming (tracks 1, 3, 7–10); percussion (tracks 2, 5, 6, 8, 11, 12); keyboards (track 10) Christopher Hugget – guitar (tracks 7, 9)
```

## Album 202: Universes — Birds of Tokyo

- **album_id:** `d5c5665b-7149-4070-bbc0-2b82b6185654`
- **Tags (identification only):** alternative rock, rock, alt rock, alternative, aussie, australian, indie rock, perth
- **Chunks:** 1 (223 words)

### Album 202, chunk 1

```text
Universes is the second album from Birds of Tokyo, independently released on 5 July 2008, through MGM Distribution. The album was recorded at Loop Studios in West Perth, Wing Command in Perth, Western Australia and in "a big beautiful wooden house by the sea" at Injidup (Yallingup, Western Australia). Mixing for the album took place in North Hollywood, California by Tim Palmer at Ameraycan Studios. During this mixing process the band filmed the music videos for "Broken Bones" and "Silhouettic" in Lancaster, California. These two music videos join together to form one complete story. However, the video for "Silhouettic", which features the second part of the story, was released first on the band's official website and their official Myspace page. The debut single from the album, "Silhouettic", was released as a free download from the band's official website on 14 April 2008. At the J Awards of 2008, the album was nominated for Australian Album of the Year. The third single off the album, "Wild Eyed Boy", received significant airplay and was shown on Channel V. Universes produced three songs on the Triple J Hottest 100, 2008 with "Wild Eyed Boy" at number 51, "Silhouettic" at number 22 and "Broken Bones" at number 20. Ian Kenny – vocals Adam Spark – guitars, vocals, keyboards Adam Weston – drums, percussion Anthonny Jackson – bass
```

## Album 203: Usher — Usher

- **album_id:** `596d9b8b-52be-4195-b775-587038553fa3`
- **Tags (identification only):** contemporary r and b, r and b, club/dance, electronic, pop, pop/rock, r b, urban
- **Chunks:** 4 (815 words)

### Album 203, chunk 1

```text
Usher is the debut studio album by American singer Usher. It was released on August 30, 1994, by LaFace Records and Arista Records. Executive producer Sean "Puffy" Combs largely set the tone for the album, handling most of the production alongside his Bad Boy affiliates, including Faith Evans, Herb Middleton, Alexander Richbourg, and Chucky Thompson, while additional production was provided by Darryl Pearson, DeVante Swing, Brian Alexander Morgan and Al B. Sure!, among others. The album received mixed reviews, earning praise for its standout tracks and seamless blend of R&B and hip-hop, while drawing criticism for its explicit lyrics, heavy production, and youthful delivery. Usher debuted at number 187 on the US Billboard 200 and later peaked at 167, also reaching number four on the Heatseekers Albums chart, ultimately selling over 500,000 copies as his subsequent success renewed interest. Of its three singles, the second, "Think of You," became the album's only top-ten R&B hit. At age 12, Usher's family moved from Chattanooga, Tennessee to Atlanta, Georgia where he joined the R&B boy group NuBeginning. The group recorded ten songs in 1991, which were later released on their self-titled album in 1993. Initially distributed regionally and through mail order, the project ultimately became the group's only release. Believing he was better suited as a solo artist, his mother, Jonetta Patton, removed him from the group at 13, later calling it "a bad experience." The same year, Usher met A.J. Alexander, then a bodyguard for Bobby Brown, who began promoting him
```

### Album 203, chunk 2

```text
at local shows. After performing on Star Search, Bryant Reid secured Usher an audition with his brother L.A. of LaFace Records, who signed him on the spot following his rendition of "End of the Road" by Boyz II Men. His first solo song, "Call Me a Mack", was recorded for the soundtrack album to the 1993 drama-romance film Poetic Justice. While preparing his debut album, Usher temporarily lost his voice due to puberty, leading Reid to consider dropping him. After persuading the label to keep him, he was sent to New York City in 1994 to live with Sean "Puffy" Combs to "attend" what Reid called "Puffy Flavor Camp," although Patton largely disapproved of her son hanging around Combs and the rest of the Bad Boy roster of artists. LaFace released three singles in support of the album. "Can U Get wit It," written and produced by DeVante Swing of Jodeci was issued as the album's lead single in July 1994. It peaked at number 13 on the US Hot R&B/Hip-Hop Songs chart and number 21 on the UK Hip Hop and R&B Singles Chart, but failed to crack the upper half of the US Billboard Hot 100. Second single "Think of You," co-written by singer Faith Evans and produced by Combs and Chucky Thompson, became Usher's first top ten hit in the United States, reaching number eight on the Hot R&B/Hip-Hop Songs chart. "The Many Ways", penned and produced by Dave Hall and Al B. Sure!, was released as
```

### Album 203, chunk 3

```text
the album's third and final single in January 1995, but reached number 42 on the US Hot R&B/Hip-Hop Songs chart only. Usher received mixed reviews from music critics, some of whom expressed concern that its lyrics were unusually explicit for a 14-year-old performer. Billy Johnson Jr. of Yahoo! Music praised the album as "an enjoyable ride," noting that Usher "delivered several standout tracks" on his debut. Similarly, The New York Amsterdam News called the album a "masterful blend of soul-stirring R&B complemented by a hip hop sensibility." Less impressed, Anderson Jones of Entertainment Weekly described the songs on Usher as "sophomoric" and "remarkably dull," concluding that "what really bogs [Usher] down is an unspectacular delivery. Unlike Tevin, Aaliyah, or even the young Michael Jackson, [he] sounds exactly like the 15-year-old he is." Likewise, Ebony characterized the album as "heavily produced." AllMusic gave the album three out of five stars, reflecting the overall mixed critical reception. Usher debuted at number 187 on the US Billboard 200 in the week of September 17, 1994. Spending twelve weeks on the chart, it peaked at number 167 in the week of October 29, 1994. The album also climbed to number 25 on Billboard's Top R&B/Hip-Hop Albums and number four on the Heatseekers Albums. Although its initial performance was modest, domestic sales eventually surpassed 500,000 copies, largely driven by renewed interest following his more commercially successful later releases. In retrospect, Usher expressed dissatisfaction with the album, suggesting it did not reflect his authentic artistic identity.
```

### Album 203, chunk 4

```text
He later stated: You have got to be true to who you are. You can't go out as a "fad" in the industry; you have to be true to who you are, and I figure that's the reason why, maybe, I didn't have as much success with the first album. That wasn't me. That’s something Puffy wanted me to do, and it was a fad."
```

## Album 204: The Metal Opera, Pt. II — Avantasia

- **album_id:** `d31c111c-b760-4e1f-b463-ffb7d23a742d`
- **Tags (identification only):** power metal, heavy metal, symphonic metal, 00s, german metal, metal, metal opera, rock
- **Chunks:** 1 (226 words)

### Album 204, chunk 1

```text
The Metal Opera Part. II is the second full-length album by Tobias Sammet's German supergroup project, Avantasia. It is a concept album and a metal opera. The songs carry on the story begun in The Metal Opera, with the same characters. Both albums were written over the course of a year, starting in the last quarter of 1998, and both were produced from October 1999 to June 2000, with the works being interrupted for some weeks so Sammet could produce The Savage Poetry with his other band Edguy. Tobias Sammet - Keyboards, Bass guitar (on track 10), Vocals (see "Singers") Henjo Richter - Guitars Markus Grosskopf - Bass guitar Alex Holzwarth - Drums Gabriel Laymann - Tobias Sammet - tracks 1–10 Lugaid Vandroiy - Michael Kiske - tracks 1 and 2 Brother Jakob - David DeFeis - tracks 1 and 5 Bailiff Falk von Kronberg - Ralf Zdiarstek - track 9 Anna Held - Sharon den Adel - track 10 Bishop Johann von Bicken - Rob Rock - tracks 1 and 6 Pope Clement VIII - Oliver Hartmann - track 1 Elderane the Elf - Andre Matos - tracks 1, 2 and 8 Regrin the Dwarf - Kai Hansen - tracks 1 and 8 Mysterious Voice of the Tower - Timo Tolkki - track 1 Tree of Knowledge - Bob Catley - tracks 3 and 4
```

## Album 205: Definition — D.R.I.

- **album_id:** `e7adca1f-0053-4f87-a61e-ff684cb66ed0`
- **Tags (identification only):** alternative/indie rock, american underground, crossover thrash, hardcore punk, heavy metal, pop/rock, punk metal, punk/new wave
- **Chunks:** 1 (63 words)

### Album 205, chunk 1

```text
Definition is the sixth album by the American crossover thrash band D.R.I. It was released in 1992. The band supported the album by touring with Testament. The Arizona Daily Star wrote that D.R.I.'s "combined fire is stoked by a thrash-metal style and controlled by a social conscience." Kurt Brecht – vocals Spike Cassidy – guitars John Menor – bass Rob Rampy – drums
```

## Album 206: Stars Dance — Selena Gomez

- **album_id:** `60783eb2-7d1e-4f4a-a2fc-65685d6b6b83`
- **Tags (identification only):** pop, brostep, dance pop, dubstep, electro house, electronic, electropop, teen pop
- **Chunks:** 15 (3698 words)

### Album 206, chunk 1

```text
Stars Dance is the debut solo studio album by American singer Selena Gomez. It was released on July 19, 2013, by Hollywood Records. Gomez began planning the project in 2012, at which time she announced that her band Selena Gomez & the Scene would be taking an indefinite hiatus, which by 2017 had become a permanent split. Stars Dance is an EDM and electropop album, incorporating elements of dubstep, techno, disco, electro house and worldbeat. Gomez worked on the album through March 2013 with producers such as Rock Mafia and the Cataracs. Upon its release, Stars Dance received generally mixed reviews from music critics, many of whom complimented Gomez's maturing image and the album's content both lyrically and vocally, but criticized the electronic-heavy production style. It marked her first album to debut at number 1 on the Billboard 200. The album sold 97,000 copies domestically in its first week of release. This achievement was surpassed by its successor, Revival (2015), which sold 117,000 units in its first week. Stars Dance became her fourth Top 20 entry in the United Kingdom, peaking at number 14. Elsewhere, Stars Dance topped the charts in Canada, Norway, Mexico, Taiwan and China. By 2017, the album had sold an estimated 410,000 copies in the United States. The album's lead single, "Come & Get It" featured heavy electronic and worldbeat themes, and became Gomez's first Top 10 entry in the United States, entering the Top 10 in the United Kingdom, Ireland, and Canada, among others. It
```

### Album 206, chunk 2

```text
was also successful on pop radio, reaching number 2 on the Mainstream Top 40 chart. The second single, "Slow Down", reached the Top 30 in the United States. It was met with success on pop radio, reaching the Top 10 of the Mainstream Top 40 chart. Gomez promoted the album through a number of high-profile performances, such as the 2013 Billboard Music Awards. She embarked on the Stars Dance Tour (2013) to further promote the release. Selena Gomez & the Scene's third studio album, When the Sun Goes Down (2011), was musically rooted in electropop and dance-pop, similar to the group's second album, A Year Without Rain (2010). Although reviews from contemporary music critics were mixed, the album was a commercial success. In January 2012, Gomez announced that she would put her music career on hold to focus on her acting career, and that the band would be taking a hiatus: "my band and I are going our separate ways for a while. This year is all about films and acting and I want my band to play music wherever with whoever. We will be back but, it will be a good while." Despite her earlier statements, Gomez first confirmed in October 2012 that work had begun on an upcoming album, and later said it would be her solo debut album, rather than her band's fourth album. Gomez announced in March that the album's lead single would be released the following month, and that the album would follow that summer.
```

### Album 206, chunk 3

```text
On April 15, Gomez revealed plans of her first world tour, known as the Stars Dance Tour. Gomez officially confirmed on June 3 that the album would be titled Stars Dance, and also revealed the album's track listing and cover art. On her return to music, Gomez stated "I miss it. I want to be able to write about things I've never talked about before and tell a story with this album, because I've never actually had time to go in and do that." For the album, Gomez made it with production team The Cataracs, as well as the Norwegian Stargate. Gomez also worked with Rock Mafia on numerous tracks on the album, having previously worked with them on previous singles with The Scene. For Stars Dance, Gomez attempted to have more creative control over her music, stating "It's definitely the hardest I have ever worked on a record, that's for sure. I wanted to have more creative control over the album's direction." Jason Evigan, who worked with Gomez on the album, said "She's not a little girl anymore. She wants to be like that and be respected like the great pop artists out there [...] And I think she is. I think this album is really gonna blossom her into a new realm of electronic pop dance artist." Prior to the album's release, Gomez announced she would be taking a musical hiatus after Stars Dance, commenting "I've been saying that I worked really hard on this record and I
```

### Album 206, chunk 4

```text
feel like it might be my last one for a while [...] I definitely love acting and I love film and I don't feel like I've done enough of that." Following the album's announcement, numerous sources began claiming that the majority of the album was written about Gomez's relationship with Canadian singer Justin Bieber. These rumors continued to rise in popularity following the release of "Come & Get It", and prompted Gomez to confirm that the song was not about Bieber. She later said, however, that the song "Love Will Remember" is about her relationship with Bieber; an early version that leaked online just prior to the release of the album included a voicemail at the start of the song by Bieber himself that was removed from the final track. She revealed the song was "the most personal track on the record", and added "I think it's a sweet way of releasing it. It's not an aggressive approach to what people are probably expecting. I'm sure he'll love mikey too." The song "Birthday" was the first song recorded for the album. Gomez has listed "Forget Forever" as one of her favorite tracks on the album saying, "It's a really beautiful song. It has meaning behind it and it was a really special time in the studio. I got to be with the writers and just enjoy being in that moment. That was a really fun emotional song for me to sing but then I just kind of wanted to dance
```

### Album 206, chunk 5

```text
after I released it because it felt like I got to release this feeling that I had and it's a beautiful song." She later spoke of "Forget Forever" by stating "It's forgetting all the troubles, about the past, just enjoying everything else." Recording artist Jennifer Lopez wanted to record the song "Save the Day" for her 2013 album, but failed to get it from Gomez. "Come & Get It" was initially recorded by Barbadian recording artist Rihanna for her sixth studio album Talk That Talk (2011), however, she decided against using the song. Musically, Stars Dance is an album rooted stylistically in EDM and pop, this later specifically showcased as electropop while also containing strong elements of dubstep, techno, disco and worldbeat. Jocelyn Vena of MTV News described the music on Stars Dance as "dance-song-heavy" dubstep, that contains "wobbly synths, loopy vocals, fist-pumping beats and crunchy breakdowns". The album contains a highly diverse musical composition, highlighted by Caroline Sullivan of The Guardian as "darting efficiently from EDM to Bollywood". The majority of the album contains dubstep breakdowns, requisite stabs of synths, and according to Jim Farber of New York Daily News, "features a frisson of sex previously absent from this good-girl singer's work." Jason Evigan said of the album's musical style, "She's got some really cool like ethnic influence, kind of tribally dance drums and stuff like that", stating that it was similar to music by Jennifer Lopez. August Brown of the Los Angeles Times called Stars Dance a "sassy"
```

### Album 206, chunk 6

```text
pop-EDM album, noting its composition included "oxygen-sucking" sub-bass, trap snares. Brown noted the influence of Spring Breakers on the album, saying that Gomez wasn't ready to leave the "neon-splattered emotional hellscape of Spring Breakers just yet". He further went on to say: "Stars Dance is exactly the kind of album one makes in 2013 if you want to keep the pop sugar of the Disney tween cabal but mix in some broken glass and a club bathroom nosebleed. Its productions are rooted in today's pop-EDM default mode, but as that stuff goes, 'Slow Down' is pretty capable, and the bhangra-appropriating 'Come & Get It' is guilelessly silly enough to work." The album's title track was described by Gomez as being "kind of sensual", while "Like a Champion" is said to feature Jamaican and reggae influences. When talking about the song "Save the Day", Gomez stated "Do you ever have moments where you don't ever want them to end? I've had those moments. It's about saving those moments and never wanting it to go away." The song "Write Your Name" is about the feeling of falling in love. Gomez described B.E.A.T. by saying "The song is cool and the lyrics are great, but it was more, 'I can't wait to perform this song onstage because I love the way I feel when I hear this song.' It's just dope." Gomez later stated that "Undercover" was her favorite song on the album, commenting "I've never had the confidence to do different licks
```

### Album 206, chunk 7

```text
and melody changes. I messed up a lot [while recording] that one." The album's lead single, "Come & Get It", has been described as featuring "Bollywood" influences, as well as tribal music. On-air personality Peter Dee noted that the song featured various electropop elements. "Slow Down" is noted as featuring various dubstep influences, while the song's lyrics speak of taking a relationship slowly rather than rushing into things. Gomez has listed Britney Spears and Janet Jackson as some of the album's biggest influences, and later cited Skrillex, Taylor Swift, and Christina Aguilera as major influences on the record. She listed dubstep producer Skrillex as an influence to the album, with him having previously worked on the soundtrack for Gomez's film Spring Breakers. She later stated "Doing Spring Breakers was really fun, because Skrillex and Cliff Martinez did the soundtrack, and [Skrillex] kind of inspired me with a baby dubstep, because I have a few songs that have that." In an interview with Teen Vogue, Gomez mentioned electropop singer-songwriter Ellie Goulding, while she described the sound of the record, stating: "they are all really fun, pop songs-a little Ellie Goulding-ish, a little island-y feel. It's a really fun pop record." Jim Farber of New York Daily News noted influences of Spears, Jennifer Lopez, and Janet Jackson, although going on to say "Gomez's writer and producers have aped other stars' tricks gamely enough to create a pretty good time. It helps that Gomez boasts a far richer voice than her idols, Britney,
```

### Album 206, chunk 8

```text
J.Lo and Janet." The album opens with "Birthday", an electropunk song which contains sparse drums, trap snares and vocal chants and has been described by Julia Rubin of Headlines and Global News as a "candy-coated, clap-happy club anthem with plenty of girl power and sex appeal, much like a bubblegum version of Rihanna's 'Cockiness (Love It)'." "Slow Down" is a high-octane, uptempo dance-pop and EDM song, that has been described as "wobbly club thumper" by Robert Copsey of Digital Spy. It features a dubstep chorus, funk guitars, a four on the floor beat, and a spoken word outro. Lyrically, the song speaks of "slowing down the song" so the party doesn't end. "Stars Dance", the album's title track, is a "breathy and sultry" dubstep song, which contains an orchestral-dubstep beat. According to Rubin, "Gomez's soft voice takes center stage over sexy synth-beats, icy choruses and wallowing melodies." "Stars Dance" has also received comparisons to the works of Britney Spears. "Like a Champion" is a dancehall song, with influences of funk, reggae, and soca music, and features Gomez singing the song in a Bajan accent. The song has received heavy comparisons to the works of Rihanna, with critics noting the song's breezy and carefree vocal delivery. "Come & Get It" is a tribal electropop and popstep song, which contains a Bhangra beat, sonic drops, and influences of Indian music. Lyrically, the song is about female lover's attempts to rekindle a previously ended romance. "Forget Forever" is a dance-pop and synthpop song
```

### Album 206, chunk 9

```text
which contains an EDM beat and house music breakdowns. Lyrically, the song is about a breakup. Sam Lansky of Idolator said the song is an "electrifying dance-pop banger with a monolithically great chorus and a storming, anthemic beat, plus a big house break." Nate Jones of Popdust called the song "bright and expansive", going onto say that Gomez's vocals "fly over an EDM beat that can't help getting us ready for summer." "Save the Day" is a "thumping" Latin pop and house music song "B.E.A.T." is a "sexy" urban hip-hop song described by Jon O'Brien of Yahoo! Music as "minimal spoken word electro". Christina Drill of Popdust said the song was "infectious and definitely racier than usual for Selena (the chorus: 'It's a big bad world but I'm not ashamed / I like the lights in my hand and the beat in my face')". "Write Your Name" has been described as an "exotic" sounding electronic dance and house music song. The song contains a rap verse by Gomez, as well as elements of dubstep. O'Brien of Yahoo! Music said that: "Forget Forever' and 'Write Your Name' both manage to tiptoe into 'hands in the air' territory without succumbing to the usual Guetta-style bombast." Gomez promoted the album through a number of interviews and televised live performances. She appeared on On Air with Ryan Seacrest on April 8, 2013, to promote "Come & Get It". She gave her first televised performance of the song at the 2013 MTV Movie Awards on
```

### Album 206, chunk 10

```text
April 14, 2013. The appearance saw Gomez in an "all-red, 'earthy'" outfit, and received a generally positive reception. She appeared on Dancing with the Stars on April 16 to perform "Come & Get It". On April 18, she performed the song again on The Ellen Degeneres Show. Gomez donned a bindi for these performances, and later came under fire by the Universal Society of Hinduism for her use of the religious symbol. Gomez appeared on The Late Show with David Letterman on April 25, where she performed "Come & Get It". On April 27, she performed the song yet again at the 2013 Radio Disney Music Awards. She did not perform the song again until May 19, when she performed at the 2013 Billboard Music Awards. Days later, she performed "Come & Get It" on The Graham Norton Show. Gomez appeared at the MuchMusic Headquarters on May 30, where she performed "Slow Down" for the first time. On July 4, Gomez performed both "Come & Get It" and "Slow Down" at the Macy's 4th of July Fireworks Spectacular. Gomez appeared on This Morning in the United Kingdom to perform "Come & Get It". To coincide with the release of Stars Dance, Gomez performed "Come & Get It", "Slow Down", and "Birthday" on Good Morning America. In September, Gomez appeared on Live! With Kelly and Michael to perform "Birthday". Following the release of "Slow Down", Gomez appeared on The View to perform the song. She performed the song again on The
```

### Album 206, chunk 11

```text
Late Show with David Letterman. She performed "Slow Down" on The X Factor in the United States. Gomez was selected to be the halftime performer during the Dallas Cowboys vs. Oakland Raiders game held on Thanksgiving. For the show, Gomez performed a medley of "Like a Champion", "Slow Down", and "Come & Get It". The tour was further promoted through her worldwide Stars Dance Tour (2013), which visited countries such as the United States and Asia. The tour became making over $36 million at the box office. Originally meant to feature dates in Australia and Japan, the tour was cancelled due to personal issues. "Come & Get It", was released as the lead single from the album on April 7, 2013. As of July 2013, the song became one of Gomez's most successful singles, peaking at number 6 of the US Billboard Hot 100 and the Canadian Hot 100 as well as being certified 3× Platinum by the RIAA. The music video premiered on MTV on May 7, 2013 and was directed by Anthony Mandler. "Slow Down", was released as a promomotinal single on June 3, 2013. via an instant digital download with the pre-order of the album on iTunes, and was co-produced by The Cataracs and David Kuncio. It was later released as the album's official second single on August 13, 2013. It peaked at number 27 on the Billboard Hot 100. The official video was uploaded to YouTube on July 19, 2013. Stars Dance received mixed reviews from
```

### Album 206, chunk 12

```text
music critics. Positive remarks went toward the overall production of the album, as well as its lyrics and Gomez's vocals. Mixed reviews went towards her inability to create her own musical identity; she was compared to singer Rihanna on several occasions. At Metacritic, which assigns a normalized rating out of 100 to reviews from critics, the album received an average score of 59, which indicates "mixed or average reviews". Tim Sendra from Allmusic awarded the album three-and-a-half stars out of five. As he pointed out "Slow Down", "Save the Day" and "Undercover" as highlights, he said "Selena's reliably strong vocals and the variety of sounds, it adds up to be another fine entry in her catalog and just another example of why Selena Gomez is one of the best pop stars making music in 2013." Stephen Unwin from Express.co.uk compared the new effort to Vanessa Hudgens and said "Both [Gomez and Hudgens] have now turned their attention to themes of a more adult nature, this new album of Selena's being one of them and she's just about pulled it off." Two Guardian reviews were issued. The first, observed by Kitty Empire, awarded the album three stars out of five. Conversely, the second Guardian review, observed by Hermione Hoby, was mixed and awarded it two stars out of five. She clarified that "if she really wants to be considered a grown-up pop star, Selena Gomez is going to have to find some better hit-makers." She compared the work, including "Like a
```

### Album 206, chunk 13

```text
Champion", to Rihanna. August Brown from the Los Angeles Times found that the album was "the kind of album one makes in 2013 if you want to keep the pop sugar of the Disney tween cabal but mix in some broken glass and a club bathroom nosebleed. Its productions are rooted in today's pop-EDM default mode [...]" Natalie Palmer from Entertainmentwise took perspective of other critics and commentators, saying the album should have been praised for "trying something new". She discussed "'Stars Dance' isn't what you would expect from a girl who was once a Disney princess. Many often go for the bubblegum pop or the angry rock chick but the 21-year-old has opted for an edgier genre and a unique sound." Matthew Horton from Virgin Media awarded the album two stars. He criticized her "lack of personality" in most songs and felt her vocal abilities on the album "doesn't help". He concluded saying "It's all too identikit, [and] could be anyone with a grasp of average dance-pop". Simon Price from The Independent awarded one star out of the five, criticizing the lack of effort saying that "Even given these facts, it's a pop record, which means one killer track would redeem everything. Predictably enough, it never comes." Ron Harris from The Huffington Post felt the album did not live up to expectations, citing Gomez as a "vibrant young woman of Disney pedigree [who] simply punched the clock and worked through an already cooked musical plot foisted upon her. Gomez
```

### Album 206, chunk 14

```text
might be an incredibly talented and interesting person with much to offer artistically, but we'll never find out at this rate." He also found the album to have less personality than her previous records with The Scene. Stars Dance debuted at number one on the Billboard 200, selling 97,000 copies in its first week of release. This made it Gomez's first album to reach the top of the chart, as well as her highest first sales week for an album, until surpassed by her second release Revival, which sold 117,000 its first week. The album fell to number eight on the chart during its second week, selling an additional 31,000 copies. These sales were a 68% drop from the previous week's sales. In its third week, the album fell to number thirteen. The album continued to decline on the chart the following week, landing at number eighteen. In its fifth week, the album fell to number twenty-five. The album rose to number twenty-four on the chart following this. Following this rise, the album had a 23% increase in sales, selling 17,213 copies and reaching number twenty-one. Despite this, the album dropped to number thirty-three the following week, selling just over 7,000 copies. Stars Dance spent a total of twenty-five weeks on the Billboard 200, with its last appearance being on the week ending January 25, 2014. The album debuted at number one on the Canadian Albums Chart, with sales of 16,500 copies in its first week. It was her first
```

### Album 206, chunk 15

```text
number one in the country, and sold more than 5,000 in its first week than her previous effort. On August 27, 2013, the album received a Gold certification from the CRIA, for sales exceeding 40,000. Stars Dance had its first chart entry on the New Zealand Albums Chart, entering in the top five at number five itself. In the United Kingdom, the album debuted and peaked at number fourteen; it spent a total of four weeks on the chart. It peaked at number nine in Ireland, and spent a total of six weeks on the chart. The record peaked at number eight in Australia. The album was more successful in international territories. In Mexico, the album debuted at number one on the Mexican Albums Chart, and later went on to be certified Gold in the country for selling 30,000 copies. Stars Dance reached number two in Portugal, and was certified Platinum in the country. The album peaked at number eight in Brazil, and also received a Platinum certification in the country. Mio Vukovic – A&R Sarah Yeo – A&R [Coordination] Dave Snow – Creative Director Brian Teefey – Management Mandy Teefey – Management Lincoln Wheeler – Management [Marketing]
```

## Album 207: Shoe String Symphonettes — Marc Ribot

- **album_id:** `945aaca1-9803-440b-8881-15cd78f92307`
- **Tags (identification only):** electronic, modern classical, rock, abstract, avant garde jazz, experimental, future jazz
- **Chunks:** 2 (478 words)

### Album 207, chunk 1

```text
Shoe String Symphonettes is a 1997 album of film music by Marc Ribot released on Tzadik Records. The album contains soundtracks for five short films; the earliest being Landlord Blues directed by Jacob Burkardt (1987), followed by Death by Unnatural Causes directed by Karen Bellone and Lisa Rinzler (1991); one track for Summer Salt directed By Charles Levi (1993); Ribot's music for the silent film Aelita Queen of Mars directed by Yakov Protazanov (1928) was a mixture of live recordings from the 1995 Meltdown Festival mixed with backing tracks recorded in London and a live recording from The Knitting Factory; and Pieces from an Incomplete Project directed by Joe Brewster (1996). Ribot stated "A lot of what I wrote was source music. In films, you write the score, but there's also source music. For example, if a scene takes place in a disco and the filmmaker doesn't want to shell out for rights to a disco hit, you write some disco. “Montuno” is a salsa tune. Jacob Burkhardt, the director, needed something that established a backyard on the Lower East Side. ... I gave it to the producer, J.D. Foster, to sequence, but I'm happy with the way he did it. I think it made the record as a whole more listenable. “Aelita” is pretty rough going; I chopped up the score into three suites. I don't mind mixing things up in that way. It's like making a salad, things rub off on each other". Allmusic awarded the album 3
```

### Album 207, chunk 2

```text
stars with reviewer Sean Cooper stating, "Symphonettes features some of Ribot's most compelling work to date, both creatively augmenting the originals and sketching out cinematic spaces more or less autonomous from the films they were inspired by". Marc Ribot – guitars, sampler, trumpet, banjo, E-flat horn Greg Cohen (1, 14) – bass Jill Jaffe (1, 7, 8, 10, 11, 14) – violin, viola Brad Jones (2, 4, 13) – bass Bill Ware (2, 4, 13) – vibraphone Curtis Fowlkes (2, 4, 13) – trombone Jim Nolet (2, 4, 13) – violin Roy Nathanson (2, 4, 13) – saxophone E.J. Rodriguez (2, 4, 13) – drums, percussion Gregory Ribot (2, 4, 13) – flute Paul Clarvis (3, 6, 12) – drums, percussion Dave Maric (3, 6, 12) – keyboards Phil Boyden (3, 6, 12) – violin Helen Thomas (3, 6, 12) – cello Mike Kearsey (3, 6, 12) – trombone Anthony Coleman (12b) – organ Ikue Mori (12b) – percussion Jim Staley (12b) – trombone Dave Douglas (7, 8, 10, 11) – trumpet Vicki Bodner (7, 8, 10, 11) – oboe Charlie Giordano (7, 8, 10, 11) – piano, keyboards Mauro Refosco (7, 8, 10, 11) – percussion Maxine Neuman (7, 8, 10, 11) – cello Tony Garnier (7, 8, 10, 11) – bass John Zorn (9) – saxophone Andy Haas (9) – saxophone Cyro Baptista (9) – drums
```

## Album 208: Razorblade Suitcase — Bush

- **album_id:** `e4f3844a-8b63-4f07-907f-65f1128b8eb4`
- **Tags (identification only):** alternative rock, grunge, rock, post grunge, alternative rock; post grunge
- **Chunks:** 6 (1425 words)

### Album 208, chunk 1

```text
Razorblade Suitcase is the second studio album by English rock band Bush. It was released on 19 November 1996 by Trauma and Interscope Records in the United States and Europe and on 20 January 1997 in the United Kingdom. The follow-up to their 1994 debut Sixteen Stone, it was recorded at Abbey Road Studios in London with engineer and producer Steve Albini. Its sound is more raw than that of its predecessor and has frequently been compared to Nirvana's In Utero (1993), which was also produced and engineered by Albini. Razorblade Suitcase debuted at number one on the US Billboard 200, selling 293,000 copies in its first week of sales in the United States. To date, it remains the only Bush album to top the Billboard 200. The twentieth anniversary of the album was marked with a reissue officially titled Razorblade Suitcase (In Addition) on 16 December 2016, including the remastered album and four rare bonus tracks: "Broken TV", "Old", "Sleeper" and "Bubbles". In 2025, Lauryn Schaffner of Loudwire named the album the best post-grunge release of 1996. Gavin Rossdale wrote most of the songs for Razorblade Suitcase in under one month. "Swallowed", along with others from the album, were written while on the road. In an interview with the Deseret News published on 2 January 1997, Rossdale explained: "I was trying to write songs while my life was falling apart. While my longtime girlfriend of five years was leaving and packing in one room, I was writing in the
```

### Album 208, chunk 2

```text
other room." The band chose Steve Albini to produce the album. In an interview with Spin during the final stages of the recording process Rossdale was quoted as saying that Albini "has been more important to me in terms of records I've listened to than any other person." Around the same time Albini declared that he put more time and energy into Razorblade Suitcase than he had with any previous albums. Described as a grunge album by Entertainment Weekly, Razorblade Suitcase invited strong comparisons to the music of Nirvana, whose final album In Utero had been produced by Albini in 1993. "Swallowed" and "Bonedriven" in particular conjured a description of "irresistibly reminiscent" of Nirvana. "Straight No Chaser" was opined by The A.V. Club to be the "sister ballad" to the band's earlier hit "Glycerine". Nicholas Slayton of Medium opined that the lyrics of Razorblade Suitcase "focused on three main ideas and problems": being trapped in situations with no way out, fallout from relationships, and loneliness. "Personal Holloway", according to Slayton, reflected lament for societal norms forced on women. In 1999, Gavin Rossdale stated that the song was about a female friend who attempted to commit suicide; the song contains references to paracetamol as a result. It contains the lyric "deaf and dumb with the lights on, married by signs", which was inspired by list of all the people who'd lived in an English country house, at which Rossdale stayed, for the past 300 years; one couple from around 200 prior
```

### Album 208, chunk 3

```text
were listed as "deaf and dumb, married by signs". Gavin Rossdale commented in 2017 that the lead-single, "Swallowed", reflected "massive success after failing for years". "Insect Kin" has been described by Rossdale as being "mood, pure mood". The song's lyrics mention vicodin, an opiate pain medication, and Red Stripe, a brand of lager beer, which Rossdale explained "were pretty much what I lived on when my stomach was really bad". "Insect Kin" contains references to Rossdale's previous love interest Courtney Love, particularly in the lyric "it's all the pain in the way she walks, it's all the pain in her wave goodbye". "Cold Contagious" musically has been compared to the work of Neil Young. Rossdale has introduced the song at live performances as being "about revenge", although Rossdale has stated that the song is about several subjects, including seeing households fall apart following the breakup of relationships. "History" was themed around abortion. In 1997, Bush embarked on a worldwide tour, the Razorblade Suitcase Tour, to promote the album. Stretching from late January into November of that year, it took the band through Europe, North America, South America, Asia, and Australia. It included stops at many major music festivals around the world, including Glastonbury Festival, Pinkpop Festival, Reading Festival, Rock am Ring, Rock im Park, and Pukkelpop. Razorblade Suitcase was released on November 19, 1996, through Trauma Records. It debuted at number one on the Billboard 200, selling 293,000 copies in its first week. It remained at number one during its
```

### Album 208, chunk 4

```text
second week of release in the US. The album also debuted at number one in Canada, with first-week sales of 45,900 copies. Despite the album selling fewer copies than Sixteen Stone in the US, it marked a commercial peak for the band in their native Britain, where it reached number four on the UK Albums Chart. The band originally planned to release the album in early 1997 but decided it would be better for a late 1996 release, especially considering that U2's next album was pushed into 1997. The lead single from the album, "Swallowed", was released in October 1996 and was a huge success in the US, holding the number one spot on the US Billboard Modern Rock Tracks chart for 7 weeks. It remains the band's longest charting number one single. "Swallowed" also marked the commercial peak for the band in their native United Kingdom's singles charts, where it made number 7. "Greedy Fly" was the second single released from Razorblade Suitcase and reached number three on the US Modern Rock Tracks chart. The singles "Swallowed" and "Greedy Fly" peaked at number seven and number twenty-two, respectively, on the UK Singles Chart. "Bonedriven" and "Cold Contagious" followed as singles but did not make an impact on the charts. "Mouth" was remixed and later released as a single from the band's 1997 album Deconstructed. The remixed version reached number five on the US Modern Rock Tracks chart. "Mouth" is featured on the soundtrack and in the film An American
```

### Album 208, chunk 5

```text
Werewolf in Paris. The "Mouth" music video features Julie Delpy, who also starred in the film. The 20th anniversary of Razorblade Suitcase was marked by a reissue, officially titled Razorblade Suitcase (In Addition). It was released digitally on 16 December 2016, and on vinyl on 10 February 2017. The reissue includes the remastered album and four rare bonus tracks: "Broken TV", "Old", "Sleeper", and "Bubbles". Prior to the reissue, three of the four bonus tracks had been released as B-sides ("Broken TV" with "Swallowed" and "Old" with "Greedy Fly") or found on compilations, but "Sleeper" had never received a proper release. The vinyl release of the reissue is on 180-gram black-and-white swirl vinyl and comes housed in a metallic silver gatefold cover with re-interpreted artwork, a poster of lyrics (including the songs that weren't on the original), and liner notes from producer Steve Albini. Razorblade Suitcase received polarized reviews upon its release. Some critics dismissed the album because they felt that although the band attempted to distance themselves from bands like Nirvana and Pearl Jam in terms of their sound, they ultimately failed at creating a sound of their own. For example, Entertainment Weekly reviewer David Browne stated that some of the songs on the album could have easily been on the record Nirvana never made (due to Kurt Cobain's suicide). Andy Gill from The Independent also stated that portions of the album are very reminiscent of Nirvana, citing songs such as "Swallowed" and "Bonedriven" as irresistible reminders of Nirvana.
```

### Album 208, chunk 6

```text
Rolling Stone's Matt Diehl criticized the album at the time of its release, giving the album two out of five stars. Johnny Cigarettes from NME gave the album an extremely negative review, rating it 1/10 "for spelling their name right on the top of the record". However, Razorblade Suitcase was not criticized by all critics. Select magazine gave the effort three out of five stars. AllMusic's Stephen Thomas Erlewine stated: "The problem is that Gavin Rossdale has not come up with any hooks, which means that while Razorblade Suitcase is more pleasing and visceral on the surface, it offers no hooks to make it memorable, unlike the hit singles from Sixteen Stone." The album's working title was Ghost Medicine but was changed for unknown reasons. The title Razorblade Suitcase comes from the lyrics of the song "Synapse" and is lead singer Gavin Rossdale's interpretation of "emotional baggage." The album artwork was by Vaughan Oliver and Adrian Philpott. Oliver had previously created the artwork for the Pixies' Surfer Rosa, which was also produced by Steve Albini.
```

## Album 209: The Great American Bar Scene — Zach Bryan

- **album_id:** `694c3fdb-5cd1-4935-9ade-88fcb30d70f1`
- **Tags (identification only):** country, singer songwriter, alternative country, americana, contemporary folk, country folk, country rock, folk
- **Chunks:** 3 (685 words)

### Album 209, chunk 1

```text
The Great American Bar Scene is the fifth studio album by American singer-songwriter Zach Bryan, released on July 4, 2024, through Belting Bronco and Warner. The album was released just over 10 months after his self-titled 2023 album, and was preceded by the single "Pink Skies". It features guest appearances from Noeline Hofmann, John Moreland, John Mayer, Bruce Springsteen, and Watchhouse. On April 1, 2024, the website Whiskey Riff announced the release of the album for June and features from Mayer, Springsteen and the Avett Brothers as an April Fool's joke. Bryan officially announced the record the following month, with features from Mayer and Springsteen. The Great American Bar Scene received a score of 73 out of 100 on review aggregator Metacritic based on six critics' reviews, which the website categorized as "generally favorable" reception. Billboard's Melinda Newman felt that "the album feels less overstuffed than American Heartbreak, but could have still used a trim or two given the relative sameness in the sound of the tracks", although the songs "continue to deliver an emotional wallop thanks to his economical, but cinematic, trenchant lyrics". Chris Willman of Variety wrote that The Great American Bar Scene "actually feels a lot less stark than last year's self-titled record did" and there is "no mistaking how much the spirit of Springsteen looms over the album, as much as it has over much of Bryan's short, meteoric career to date". Claire Shaffer of Pitchfork felt that the album "adds to the Zach Bryan formula
```

### Album 209, chunk 2

```text
by taking on a wider lens, weaving his personal struggles and triumphs into the greater legacy of lost souls and camaraderie found in America's watering holes". Jonathan Bernstein of Rolling Stone acclaimed Bryan's "writing that blends endearing Kerouac cosplay, Instagram poetry, and Proustian profundity, sometimes from one line to the next" on tracks that "feel like a batch of old friends largely because of Bryan's other magical gift: his knack for absorbing and transforming his many influences into something that feels uniquely his own". Country Chord's Brennen Kelly wrote that "this record is not about the titular great, American bar scene but instead is about all of the stories swapped, memories made and people met there", noting that Bryan crafted narratives that would be brought up in quiet conversations at a bar. Reviewing the album for Paste, Tom Williams wrote that it "feels like a retread of Bryan's self-titled LP from last year—so much so that you wouldn't be surprised if the Oklahoman hitmaker were to announce that these songs were all B-sides from the Zach Bryan sessions". A Sputnikmusic staff review also stated that it "settle[s] into something of a familiar groove. He tries throwing John Mayer and Bruce Springsteen features into the mix, but the results are ultimately the same: more slow-to-mid tempo country crooners with results-may-vary emotional resonance". Stephen Thomas Erlewine of AllMusic stated that the songs on the album "are poetic, plump with purple imagery and plaintive rhymes" and praised the collaborations with Bruce Springsteen and
```

### Album 209, chunk 3

```text
John Mayer. Erlewine wrote that the tracks "Sandpaper" and "Better Days" helps to pull "Bryan's aspirations into focus: where the rest of the record seems caught in its own head, these tunes have a forward motion that makes the rest of The Great American Bar Scene seem relatively bereft of musical imagination". In the United States, The Great American Bar Scene debuted at number 17 on the Billboard 200 with 32,000 album-equivalent units—the low sales was due to the album being released during the end of a tracking week, on July 4, 2024. The following week on the Billboard 200, The Great American Bar Scene vaulted from number 17 to number 2—moving 137,000 album equivalent units (including 8,500 in pure album sales), marking Bryan's fourth top-ten charting effort on the Billboard 200. The album was blocked from the number-one position on the Billboard 200 by Taylor Swift’s The Tortured Poets Department—which was serving its 12th consecutive week at number one. The Great American Bar Scene dropped one position to number three the following week—its third Billboard 200 charting week, moving an additional 88,000 album-equivalent units.
```

## Album 210: Live in Hyde Park — Red Hot Chili Peppers

- **album_id:** `a10a7712-2332-43d3-87c6-1d6fb852f513`
- **Tags (identification only):** alternative rock, rock
- **Chunks:** 1 (262 words)

### Album 210, chunk 1

```text
Live in Hyde Park is the first live album released by the American rock band Red Hot Chili Peppers, recorded in Hyde Park, London, on June 19, 20 and 25, 2004 during the Roll on the Red Tour. These three concerts set records for the highest-grossing concerts at a single venue in history. This double album compiled from these three shows went straight to No. 1 in the UK and stayed there for two weeks, selling over 120,000 copies. Of the eight studio albums by the Red Hot Chili Peppers that were released prior to Live in Hyde Park, only three are actually represented in this album's set list – their fifth, Blood Sugar Sex Magik, seventh, Californication, and eighth, By the Way (the single "Fortune Faded", however, was featured solely on the band's Greatest Hits compilation). "Under the Bridge" and "Give It Away" were the only songs from Blood Sugar Sex Magik. The songs "Leverage of Space" and "Rolling Sly Stone" are exclusive to this collection. There are 4 songs that were also performed but are not included on this release, "I Like Dirt" and "My Lovely Man" were both performed on June 19, "Maybe" (The Chantels cover) on June 20 and "Mini-Epic (Kill for Your Country)" on June 25. "Mini-Epic" was originally planned for this release, but did not make it into the CD versions, probably due to delicate issues concerning the theme of the song. However, it was eventually officially released for the first time in 2015 on the Red Hot Chili Peppers' next live album, Cardiff, Wales: 6/23/04.
```

## Album 211: Something’s Going On — Frida

- **album_id:** `9a323c6f-9ecf-4105-8330-543749867cd6`
- **Tags (identification only):** contemporary pop/rock, pop, euro pop, pop/rock, rock
- **Chunks:** 6 (1327 words)

### Album 211, chunk 1

```text
Something's Going On is the third solo album by Swedish singer Anni-Frid Lyngstad (Frida), one of the founding members of the Swedish pop group ABBA and her first album recorded entirely in English. Her previous two albums had been recorded in Swedish. Recorded in early 1982 during the final months of ABBA, the album was released on 10 September of that same year. Produced by Phil Collins with Hugh Padgham, the album featured a harder-edged and more rock-oriented sound than the music she had previously recorded with ABBA and it included Collins' distinctive gated reverb drum sound. The record was met with a positive reception by both critics and the public, with sales in excess of 1.5 million copies, making it the best-selling solo record of any of the ABBA members to date. The album has since been re-released several times, including a 2005 remastered version that contained several bonus tracks. Promotional videos from the album are included in the DVD documentary titled Frida – The DVD. In 1982, Frida felt it was time to record a solo album again, this time in English and aimed at the international market. ABBA were spending less and less time together. Going through her divorce from fellow band member Benny Andersson, Frida had heard Phil Collins' "In the Air Tonight", (as recommended to her by her daughter) and then listened to the album it appears on, Face Value, "non-stop for eight months". As Collins himself put it in a TV interview: "Frida and
```

### Album 211, chunk 2

```text
I had something in common as far as our divorces were concerned. We were both the injured party." Polar Music approached Collins, asking if he would be interested in producing Frida's new solo album. He accepted the offer, thus making this his second album to be recorded at Polar Studios, the first being Genesis' Duke (1980). Polar Music sent out invitations to publishing companies around the world, announcing Frida's plans and asking for songs suitable for the project. The response was overwhelming; more than 500 songs came into the Polar Music offices in Stockholm. Elvis Costello (who submitted a song called "I Turn Around") was one of the many who had their work rejected. Among the composers who made it to the album's final track list were Bryan Ferry, Stephen Bishop, Rod Argent and Russ Ballard. The Giorgio Moroder/Pete Bellotte composition "To Turn the Stone" was originally written for Donna Summer's 1981 album I'm a Rainbow – a double set for Geffen Records which for various reasons would remain in the archives until 1996. Frida also asked Per Gessle, later of Roxette, to set Dorothy Parker's bittersweet poem "Threnody" to music. A re-interpretation of the Face Value track "You Know What I Mean" – a song especially close to her heart, both musically and lyrically – was also included. The song "Here We'll Stay" had previously been recorded and performed by singer Sonia Jones for the UK pre-selection for the 1980 Eurovision Song Contest. On the album, it was recorded
```

### Album 211, chunk 3

```text
as a duet with Phil Collins, although he wasn't credited. When it was decided to release the song as a single in 1983, Frida re-recorded the song as a solo version. Recording began at Polar Studios, Stockholm, on 15 February 1982 and continued until 31 March. Earth Wind & Fire's horn players (the Phenix Horns) – also an important part of the Face Value album – came to Stockholm for a two-day visit. Strings, orchestra, and harp were later recorded at George Martin's Air Studios in London in the attendance of both Martin and Paul McCartney. Produced at a time when most commercial recordings used only analog technology, the album was one of the few to be both digitally recorded and mixed, predating Dire Straits' Brothers In Arms by almost three years. At the time of recording Something's Going On Frida had wanted to distance herself from the "typical ABBA pop sound" (according to Lyngstad herself). She wanted to break away from being associated with the group and make a fresh start both as an artist and as an individual. The new songs, musicians and producer gave Frida a new identity. Collins' production and especially his gated drum sound heard throughout the album, as well as the rough and raw guitar riffs of the lead single "I Know There's Something Going On", contrasted with the sound of an ABBA record. All backing vocals were sung by Frida and Collins. The album closes with their duet "Here We'll Stay". Swedish Television,
```

### Album 211, chunk 4

```text
SVT, documented the whole recording process from the first day in the studio to the release party after the album's completion. The resulting footage became a one-hour TV-special which included interviews with Frida and Phil Collins, Björn & Benny from ABBA, as well as all the musicians on the album. It was directed by Stuart Orme and executive produced by Phil Collins' manager, Tony Smith. This documentary is included in Frida – The DVD. In the summer of 1982, Frida unveiled the results of these recording sessions by releasing the single and video "I Know There's Something Going On". An extensive promotion tour of Europe and the United States followed. Frida performed both the single and other songs from the album on major TV-channels throughout Europe. The album received mixed reviews by critics. In Smash Hits the album was given only a 4 out of 10 rating: "It must have looked a good idea on paper. One pop dynamo — Frida of Abba — produced by another – Phil Collins. The result, however, is less than riveting. Phil has tried to produce an Abba album while Frida is trying to emulate Phil's ghostly singing voice." However, other reviews were more positive. Billboard wrote: "ABBA's auburn-haired songstress makes a bold solo-project a stunning success", whilst Mark Coleman described the album in the third edition of The Rolling Stone Album Guide as a "sharp, rock-oriented, delightfully eclectic album". Although it was stated that the album has a collection of songs that were
```

### Album 211, chunk 5

```text
designed for a soloist, The Sydney Morning Herald reviewed: "Unfortunately, it still sounds a little like ABBA with three members missing." They added that: "Perhaps the best tracks is the title song which has charted as a single. Others that will help Frida win new fans is a rock-jazz track titled "Tell Me It’s Over" a ballad titled "Threnody" and a Bryan Ferry number "The Way You Do". Audiences also accepted the new, rockier sound and both the album and its lead single soon started climbing the charts; Something's Going On reached No. 1 in Sweden and was a Top 10 success in several other European countries. It was also a Top 20 hit in the UK, peaking at No. 18. With sales in excess of 1.5 million copies worldwide, Something's Going On is the best-selling solo album of any of the ABBA members to date. The single "I Know There's Something Going On" reached No. 1 in Belgium and Switzerland, and was a Top 10 hit throughout most of Europe, as well as in Australia and South Africa (peaking at No. 5 in both countries). It also proved a success in the United States, reaching No. 13 on the Billboard Hot 100 chart and No. 9 on Radio & Records airplay, with the track's video being heavily promoted on MTV. The song was the 20th biggest-selling single in the US for 1983. Anni-Frid Lyngstad – lead vocals, backing vocals Phil Collins – drums, backing vocals, percussion Peter Robinson –
```

### Album 211, chunk 6

```text
keyboards Daryl Stuermer – guitars Mo Foster – bass guitar Don Myrick – saxophone Michael Harris – trumpet Rahmlee Michael Davis – trumpet Louis Satterfield – trombone The Martyn Ford Orchestra – strings Martyn Ford – conductor Skaila Kanga – harp Phil Collins – producer Hugh Padgham – engineer, assistant producer Leif Mases – mastering (at Polar Music Studios, Stockholm) Peter Robinson – string and horn arrangements Stig Anderson – executive producer Thomas Johansson – album coordinator
```

## Album 212: Viva! La Woman — Cibo Matto

- **album_id:** `246439ae-d800-4f44-9975-eea33629df9b`
- **Tags (identification only):** trip hop, electronic, pop, abstract, hip hop, rock
- **Chunks:** 4 (855 words)

### Album 212, chunk 1

```text
Viva! La Woman is the debut studio album by the band Cibo Matto, released on January 16, 1996, by Warner Bros. Records. The tracks "Birthday Cake" and "Know Your Chicken" were first released as singles in 1995. Following the release of Viva! La Woman, the latter was reissued as a single in July 1996. Music videos were produced for "Know Your Chicken" and "Sugar Water", directed by Evan Bernard and Michel Gondry, respectively. Warner Bros. Records signed Cibo Matto after the band's 1995 self-titled EP caught the label's attention. The tracks on Viva! La Woman, Cibo Matto's first album for the label, reflected the band's live performances, utilizing pre-recorded samples and loops. Cibo Matto instrumentalist Yuka Honda later expressed regret that she did not stand up for herself when others discouraged her from replacing the samples and loops with new recordings. Stereogum's James Rettig classified Viva! La Woman as a trip hop album. Throughout the album, vocalist Miho Hatori's alternately sung, rapped, and whispered performances are backed by Yuka Honda's hip hop-inspired sound collages. New York writer Chris Norris described Hatori and Honda as avant-pop musicians who on Viva! La Woman "weave found sounds, Muzak, and orchestral textures" into "atmospheric" songs. In The New Rolling Stone Album Guide, critic Rob Sheffield described the music as a mixture of hip hop, dub, lounge, and pop. The album's lyrics balance humorous themes in "Beef Jerky", "Birthday Cake", and "Know Your Chicken" with abstract, often emotional narrative-style wording in "Apple", "Sugar Water", and
```

### Album 212, chunk 2

```text
"Artichoke", as well as overall pop music fare in "White Pepper Ice Cream", "Theme", and "Le Pain Perdu". Several songs feature the group's well-known references to food, primarily present on this release. Honda explained: "Food is something you can't escape. It's there every day." The band would often go to restaurants after rehearsals, and according to Honda, "Cibo Matto grew out of those restaurant times." "Theme", unusual among Cibo Matto's discography for its length, is a track which features a relatively normal song sung in English with several Italian words before shifting into instrumental passages and leading into a second half that contains entire verses in Japanese and French. The album booklet contains illustrations and lyrics accompanying most of the songs. The only tracks for which the booklet features no lyrics are "The Candy Man", a cover of a song from the 1971 film Willy Wonka & the Chocolate Factory (presumably for copyright reasons; the song also has all lyrical references to Willy Wonka changed to "the candy man"), and "Jive", an 18-second hidden track primarily consisting of a recording of Miho Hatori tapping her thighs, for which she is also credited. Viva! La Woman was acclaimed by music critics. Michele Romero of Entertainment Weekly described Cibo Matto as "sonic savants who go nutty mixing disparate ingredients, like avant-garde trumpet with bossa nova bass lines and sugary non-sequitur lyrics", summarizing the album as "kitschy club music, as kooky and lovable as Hello Kitty." In The Guardian, Caroline Sullivan called Viva!
```

### Album 212, chunk 3

```text
La Woman "an ambitious confection of trickling beats and delicately comatose spoken vocals whose only hint of wackiness is the lyrics". Select's Andrew Male observed that despite its playful lyrics, the band is "far more musically adept than yer average guitar 'n' shouting comedy act", while Q's Martin Aston highlighted Cibo Matto's eclectic range. AllMusic's Heather Phares found Viva! La Woman, "all trendiness aside", to be "innovative and catchy" and "diverse and entertaining". Sandy Masuo offered qualified praise in the Los Angeles Times, finding that "some of the protracted jams are a bit aimless, but the food theme binds things together"; less impressed was critic Robert Christgau, who gave the album a "neither" grade without comment. At the end of 1996, Viva! La Woman was listed by Spin as the tenth-best album of the year. It was also voted as the year's 27th-best album in The Village Voice's annual Pazz & Jop critics' poll. The album spent six weeks at number one on CMJ's college radio charts. Some listeners perceived the album as a novelty, "partly because of the cutesy-pie assumptions attached to Asian women in pop and partly because of the band's propensity for writing songs about food", much to Cibo Matto's chagrin. In 1999, Spin ranked Viva! La Woman as the 90th-best album of the 1990s. Writing for The Quietus in 2014, Joe Sweeney regarded Viva! La Woman as "a food-obsessed avant-rap record that dared to be ridiculous at a time when full-throated earnestness ... was shipping millions."
```

### Album 212, chunk 4

```text
The album has been recognized as influential in the years since its release. Drowned in Sound positively discussed its impact within the history of Shibuya-kei music in a 2018 article. The site's Samuel Rosean credited the album with bringing Western listeners' attention to the sound, deeming it "one of the genre's first big international crossover moments". He praised Viva! as "a masterstroke of progressive electronic sounds" and called Cibo Matto's "abstract" fusion of Shibuya-kei with art pop and trip hop "artful and forward-thinking". Miho Hatori – vocals ("singing, howling, moaning, sighing"), finger snapping, thigh tapping Yuka Honda – keyboards, programming, beach guitar, coughs, finger snapping
```

## Album 213: The Hope Six Demolition Project — PJ Harvey

- **album_id:** `0767b2a9-2bdf-4c20-8c7d-18759f71558f`
- **Tags (identification only):** alternative rock, art rock, folk rock, rock, indie rock, singer/songwriter
- **Chunks:** 5 (1199 words)

### Album 213, chunk 1

```text
The Hope Six Demolition Project is the ninth studio album by the English singer-songwriter and musician PJ Harvey, released on 15 April 2016 on Island Records. It followed her acclaimed Mercury Prize-winning album Let England Shake, released in 2011. The record's demo collection was released on March 11, 2022, to conclude Harvey's chronological re-release campaign of vinyl reissues and demo session offerings beginning in 2020. At the 59th Annual Grammy Awards, the album was nominated for Best Alternative Music Album, her fourth nomination in that category and seventh nomination overall. The album's title is a reference to the HOPE VI projects in the United States, "where run-down public housing in areas with high crime rates has been demolished to make room for better housing, but with the effect that many previous residents could no longer afford to live there, leading to claims of social cleansing". The HOPE VI program is directly referenced in the album's opening track and second single, "The Community of Hope". The title is inspired by Harvey's trip to Washington D.C. with photographer/filmmaker Seamus Murphy where she was given a tour by Paul Schwartzman of The Washington Post, who directly influenced some of the lyrics on the song. Upon its release, the song drew criticism directly from politicians running for the council seat in Ward 7 in Washington, D.C. Harvey wrote the songs for The Hope Six Demolition Project as well as her poetry book The Hollow of the Hand during her travels to Kosovo, Afghanistan and
```

### Album 213, chunk 2

```text
Washington D.C. with photographer/filmmaker Seamus Murphy between 2011 and 2014. The album was created in sessions open to the public as part of an art installation at Somerset House in London called Recording in Progress. The sessions were forty-five minutes each in length and lasted for a month, beginning on 16 January 2015 and concluding on 14 February. Viewers could see Harvey create the album through one-way glass with producers Flood and John Parish, both of whom had worked on Harvey's previous album Let England Shake. Mobile phones and devices with recording capabilities were confiscated before entering and viewers were led to a basement-level room. During the first viewing, she was working on a song called "Near the Memorials to Vietnam and Lincoln", which is featured on the album. Harvey was reportedly playing violin, harmonica and hurdy-gurdy. It was also reported that she was joined by musicians Terry Edwards and James Johnston and that Seamus Murphy was filming the entire session. Both of the album's singles were premiered on BBC Radio 6 Music, each on the day before its release. "The Wheel" was premiered on Steve Lamacq's show on 21 January 2016. Lamacq also revealed the album's release date to be 15 April 2016. "The Community of Hope" was premiered on Shaun Keaveny's show on 10 March 2016. "The Orange Monkey" was released as the album's third single on 7 April 2016. The music video for "The Wheel" was released on 1 February 2016, and that for "The Community of
```

### Album 213, chunk 3

```text
Hope" on 18 March 2016. Both videos were directed by Seamus Murphy. The Hope Six Demolition Project received generally positive reviews from critics. At Metacritic, which assigns a normalized rating out of 100 to reviews from mainstream publications, the album received an average score of 79, based on 34 reviews. Greg Kot of the Chicago Tribune praised the album, writing that it "builds masterfully to a powerful, closing one-two punch". Vice journalist Robert Christgau was more reserved in his praise, briefly describing the record as "politics according to Polly, meaning keen observation, analytic detachment, and paradoxically forgiving melodies scarred again and again by baked-in pessimism and misanthropy". The album was named Mojo's ninth-best album of 2016 and Uncut's sixth-best album of 2016. Upon its release, the opening track and second single, "The Community of Hope", drew criticism directly from politicians running for the council seat in Ward 7 in Washington, D.C., with former DC Mayor Vincent C. Gray saying "I will not dignify this inane composition with a response", and his campaign treasurer Chuck Thies insulting Harvey with "PJ Harvey is to music what Piers Morgan is to cable news." Grant Thompson, a pastor and former Congressional staffer running for the Ward 7 council seat, stated that Harvey "needs to see more of the city". At times, The Hope Six Demolition Project's lyrical content was criticized for being political without literally proposing government policy. Laura Snapes of Pitchfork asked, "By pointing out the problems in these three communities, but proposing
```

### Album 213, chunk 4

```text
no solutions, is she (Harvey) just as responsible for their desertion as the global powers that came before her?" The album debuted at number one on the UK Albums Chart. It sold 11,436 copies and became PJ Harvey's first number-one album in the United Kingdom. In its second week, the album sold 3,372 copies and fell twenty-two places to number twenty-three. It registered the third-largest drop in chart history for a number one album; Christina Aguilera's Bionic (2010) had fallen twenty-eight places and The Vamps's Night & Day had fallen thirty-four places. PJ Harvey – vocals (all tracks), guitar (2, 5, 6, 8–10), tenor saxophone (2 & 9), alto saxophone (7 & 8), violin (6), bass harmonica & auto harp (9), hand claps (10), piano & shaker (15) John Parish – backing vocals (all tracks), guitar (1, 3, 6, 7, 10, 14, 15), percussion (2–13), keyboards (2), variophon (3–5, 7, 9, 11), accordion (6), mellotron vibes (6, 11), baritone guitar & synth bass (8), autoharp (9), hand claps (10), piano & synthesizer (12), bass (12, 15), drums (15) Flood – production, backing vocals (1, 2, 4–6, 8–10, 12–14), synth bass (3), Sonic Maverick (9) Mick Harvey – backing vocals (2, 5, 7, 10), percussion (2, 7, 8, 10), Taurus pedals (2, 7, 9), slide guitar (3), keyboards (3, 7, 10, 11), bass (9), guitar & hand claps (10) Jean-Marc Butty – backing vocals (2, 5, 7), percussion (7, 8, 11) Linton Kwesi Johnson – vocals (2) Terry Edwards – backing
```

### Album 213, chunk 5

```text
vocals (1, 4–6, 8, 9, 11, 13, 14), percussion (1, 4, 8, 13), baritone saxophone (1, 4), keyboards (5), guitar, flute & bass harmonica (6), saxophones (8, 9, 11), melodica (9), guitar (12) Mike Smith – backing vocals (1, 2, 4, 7, 10, 11, 14), baritone saxophone (1, 4, 7, 10), piano (1), keyboards (2, 4, 7), saxophones (2), percussion (7), hand claps (10) James Johnston – backing vocals (1, 3–6, 11–14), keyboards (1, 5), violin (4, 6), guitar (6, 8), organ (11, 13) Alain Johannes – backing vocals (1–4, 7, 10, 11, 14), guitar (1, 2, 7, 10), saxophone (2), keyboards (4), percussion (4, 7), hand claps (10) Kenrick Rowe – backing vocals (1, 4, 9, 10, 12, 14), percussion (1–4, 9, 10, 12), hand claps (10) Enrico Gabrielli – backing vocals (1, 4, 14), percussion (1), bass clarinet (1–4), swanee whistle (4), basset clarinet (12) Alessandro Stefana – backing vocals (1, 4, 12, 14), guitars (1–4, 12, 14) Adam 'Cecil' Bartlett – backing vocals (1, 4, 6, 10), bass (1, 4, 10) Ramy Essam – vocals & acoustic guitar (15) Flood – producer, mixing John Parish – producer Drew Smith – mixing Rob Kirwan – recording, engineering
```

## Album 214: Próxima estación: Esperanza — Manu Chao

- **album_id:** `66522e5e-7fc5-41dd-ab5d-25d3007ca899`
- **Tags (identification only):** rock, latin, folk rock, latino, pop, 00s
- **Chunks:** 2 (424 words)

### Album 214, chunk 1

```text
Próxima Estación: Esperanza (English: Next Station: Hope) is the second studio album by French latin artist, Manu Chao. The album was released originally in Europe on 12 May 2001 and was later released in the United States and surrounding regions on 5 June 2001 by Virgin Records. The album title comes from a sample of an announcement for the Esperanza station of Madrid Metro's Line 4; in Spanish "esperanza" means "hope". Another Line 4 station, named Avenida de la Paz (literally "Peace Avenue") is also mentioned several times on the album, but the two stations are actually several blocks apart, and the sample used by Chao actually consists of two separate announcements pasted together. The voice actor Javier Dotú and a Metro announcer later sued for infringement of intellectual property rights over the use of their voices. Chao and features sing in Arabic, English, French, Galician, Portuguese and Spanish on various songs on the record. The backing track to "Homens", a tight rap about various kinds of men, written and performed by Brazilian journalist Valeria dos Santos Costa, is identical to the backing track for "Bongo Bong", Chao's successful single from four years earlier; however, in the short documentary film Infinita tristeza (included within the bonus section of his 2002 live DVD Babylonia en Guagua), Chao stated that "Homens" was the song for which the well-known backing track was originally recorded. The same backing track also underpins "Mr. Bobby" on this album and "Je ne t'aime plus" on Clandestino (1998).
```

### Album 214, chunk 2

```text
"La Primavera" likewise shares its backing music with "Me Gustas Tú", into which it fades directly on the album. The final song on the album, "Infinita Tristeza", does not contain any vocals by Chao, but it consists of the same backing track as "Me Gustas Tú", over which several samples and soundbites are layered; most of them come from a cartoon-based TV documentary film about pregnancy and childbirth, produced in 1977 by TVE and aimed at children. A number of voice samples from the documentary are looped and repeated throughout the track in Chao's typical fragmented style. Próxima Estación: Esperanza received a Grammy nomination for Best Latin Rock/Alternative Performance. In 2010 Esperanza was listed at #65 in Rolling Stone's "Best Albums of the Decade." In 2012, the magazine listed it at No. 474 on its list of the 500 greatest albums of all time, saying "this gem gave Americans a taste of [Chao's] wild-ass greatness. Chao rocks an acoustic guitar over horns and beat-boxes while rambling multilingually about crucial topics from politics to pot."
```

## Album 215: Pigs of the Roman Empire — Melvins

- **album_id:** `7e180337-94fc-402b-b81e-e2b53377010f`
- **Tags (identification only):** alternative rock, dark ambient, electronic, rock, experimental, hard rock, hardcore punk
- **Chunks:** 1 (235 words)

### Album 215, chunk 1

```text
Pigs of the Roman Empire is an album by the American rock band Melvins and electronic musician Lustmord, which was released in 2004 through Ipecac Recordings. Adam Jones, guitarist for Tool, also makes substantial contributions to the album. Speaking to Kerrang! in 2008, Melvins singer/guitarist King Buzzo remembered: I'd always liked what Lustmord did and I thought that doing a record with him would be a really good thing to do. A far as it being a collaboration, there are things on that record that are strictly 'us' and strictly 'him' but we never said which was which because we didn't want people to have any preconceived ideas. For example, [with the title track] we gave him 11 minutes of music and he came back with 22, which was exactly what we wanted him to do. But some parts are just me and Dale nearing the end of our tether with Kevin [Rutmanis, Melvins bassist who left the band soon after] and there are things that critics blamed Lustmord for when he's not even on the track! If I had to say 'buy these 5 records', then this would be one of them. King Buzzo - vocals, guitar, bass guitar, electronics Dale Crover - drums Kevin Rutmanis - bass guitar, slide bass, electronics, guitar, keyboards Adam Jones - guitar B. Lustmord - sound design, programming, production Sir David Scott Stone - additional electronics & keyboards
```

## Album 216: Welfare Jazz — Viagra Boys

- **album_id:** `7039984c-bc46-4d67-bae8-f0a93ce8bdf8`
- **Tags (identification only):** post punk, rock, 1–4 wochen, art punk, dance punk, english, indie rock, offizielle charts
- **Chunks:** 2 (515 words)

### Album 216, chunk 1

```text
Welfare Jazz is the second studio album by Swedish post-punk band Viagra Boys. It was released on 8 January 2021, through YEAR0001. The album was produced by Pelle Gunnerfeldt, Daniel Fagerström, Justin Raisen, Fabian Berglund aka DJ Haydn, and Patrik Berger. In a press release, lead vocalist Sebastian Murphy said of the album: "We wrote these songs at a time when I had been in a long-term relationship, taking drugs every day, and being an asshole. I didn't really realise what an asshole I was until it was too late, and a lot of the record has to do with coming to terms with the fact that I'd set the wrong goals for myself." In comparison to their debut, Welfare Jazz is less claustrophobic and oppressive, however, the song "Girls & Boys" manages to pushe these qualities to the extreme. The back-and-forth vocal duet on "In Spite Of Ourselves" draws a comparison to The White Stripes' song "It's True That We Love One Another". Lyrically, "This Old Dog", "Secret Canine Agent", and "Girls and Boys" bridges an analogy between likable canine behaviour and less desirable human qualities. On 15 October 2020, Viagra Boys announced the release of their second studio album. The first single "Ain't Nice" was released on 14 October 2020. On 2 December 2020, Viagra Boys released the second single, "Creatures". The third single "In Spite of Ourselves" was released on 16 December 2020. The single is a cover of American country folk musician John Prine's song of
```

### Album 216, chunk 2

```text
the same name, and features Australian musician Amy Taylor of Amyl and the Sniffers. The fourth single "Girls & Boys" was released on 6 January 2021. Welfare Jazz was met with "generally favorable" reviews from critics. At Metacritic, which assigns a weighted average rating out of 100 to reviews from mainstream publications, this release received an average score of 78 based on 16 reviews. At AnyDecentMusic?, the album received a 7.8 out of 10 based on 22 reviews. The song "Creatures" was singled out as the high point of Welfare Jazz. It's one of the cleanest and more melodic songs, the "finest example" where the band explore their style, "find something that sticks, [and] exploit the hell out of it". Writing for Clash, Josh Gray said: "Much like their 2018 debut Street Worms, Welfare Jazz concerns itself with the internal lives of the scuzziest dregs of humanity: no-good drifters who lug their vintage calculator collections from couch to couch, self-deceiving junkies who regale hallucinatory conversations they have with their dogs with the listener, alcoholics who scream and ramble on about their problems and other assorted bottom feeders." In a review for Exclaim!, Sarah Morrison gave the album an 8 out of 10, saying "the album occasionally takes the foot off the gas, to great effect. As Viagra Boys have done on previous releases, Welfare Jazz also features a handful of interludes, a breath of fresh air from the smoky, heavy din of its basement mosh pits." She also went on to say the album is "a massive shift from previous releases, both musically and lyrically.
```

## Album 217: C’mon, C’mon — Sheryl Crow

- **album_id:** `88498de8-d331-437a-a1ba-8701f842235d`
- **Tags (identification only):** rock, alternative rock, country rock, adult alternative pop/rock, alternative/indie rock, american trad rock, contemporary pop/rock, contemporary singer/songwriter
- **Chunks:** 1 (168 words)

### Album 217, chunk 1

```text
C'mon, C'mon is the fourth studio album by American singer-songwriter Sheryl Crow, released on April 8, 2002, in the United Kingdom and April 16, 2002, in the United States. Lead single "Soak Up the Sun" peaked at No. 1 on the Billboard Adult Contemporary chart and No. 17 on the Billboard Hot 100, becoming one of her biggest hits since "All I Wanna Do". The album was arguably her most pop-influenced to date, a big departure from the folk and rock sound on her previous release, The Globe Sessions. C'mon, C'mon debuted at No. 2 on the UK Albums Chart and on the US Billboard 200, with first-week sales of 185,000 copies in the United States. The album has been certified Platinum in the US and Japan, selling 2.1 million units in the US as of January 2008. The song "Safe and Sound" is dedicated to Crow's former boyfriend Owen Wilson and is an account of their relationship. "Steve McQueen" "Soak Up the Sun" "Safe and Sound" (live)
```

## Album 218: We Are Not Alone — Breaking Benjamin

- **album_id:** `3c5ee784-6c20-4129-abbf-09694bfa6dea`
- **Tags (identification only):** rock, hard rock, post grunge, alternative metal, nu metal, alternative rock, heavy metal, metal
- **Chunks:** 1 (177 words)

### Album 218, chunk 1

```text
We Are Not Alone is the second studio album by American rock band Breaking Benjamin. It was released on June 29, 2004. Three singles were released from the album, "So Cold", "Sooner or Later", and the full-band version of "Rain". The album's name is a reference to a James Hilton novel of the same name. We Are Not Alone sold 48,000 copies in its first week and was certified platinum by the RIAA on June 13, 2005. Despite not being the first Breaking Benjamin album with explicit music, it was the first to receive a Parental Advisory label. A Live EP was released with limited editions of the album, containing live recorded versions of "Sugarcoat," "Water," "Medicate," and "Next to Nothing" from their first album Saturate. We Are Not Alone is the last studio album to feature drummer Jeremy Hummel. The track "Firefly" was featured in the 2004 video games WWE SmackDown! vs. Raw and WWE Day of Reckoning. According to AllMusic critic Johnny Loftus, the album stylistically incorporates early Tool's sound through post-grunge's more accessible melodics.
```

## Album 219: Suzi Quatro — Suzi Quatro

- **album_id:** `54b9ddf8-19c8-458d-b56c-b88e7489ac6b`
- **Tags (identification only):** rock, english, glam rock, hard rock, laut.de, pop/rock/indie/electronic, proto punk, rock and roll
- **Chunks:** 2 (406 words)

### Album 219, chunk 1

```text
Suzi Quatro is the debut solo studio album by the American singer-songwriter and bass guitarist of the same name. The LP was originally released in October 1973, by the record label Rak in most territories. The album was released under Bell Records in the United States and Canada, EMI Records in Japan, and Columbia Records in some European countries. It was titled Can the Can in Australia. The album was a critical and commercial success, achieving international popularity upon its release, reaching the top 50 in the charts in several territories, peaking at number 32 in the UK Albums Chart, number 4 in Germany, number 5 in the Netherlands, and number 2 in Australia. The LP also achieved minor success in the United States, entering the top 150 in the charts there. The single "Can the Can", which was included on the album in most countries, became Quatro's most successful hit, reaching number one in the charts in several European countries and Australia, and had modest success in the US, peaking at 56 in the charts in 1976 when it was re-released in that country a few years later. The album also spawned her second single "48 Crash" which also achieved commercial success, reaching the top ten in several countries, including the UK where it went to number 3. The Elvis Presley cover "All Shook Up" was given a limited release as a single in the United States, peaking at number 85 on the Billboard Hot 100. Quatro would later
```

### Album 219, chunk 2

```text
claim that Presley himself contacted her and told her that her cover of his song was "the best since [his] own". Village Voice critic Robert Christgau said, "nothing in her own songwriting equals the one-riff rock of the two Chapman-Chinn singles, especially "48 Crash," and the last time I got off on someone dressed entirely in leather was before John Kay started repeating himself." In a retrospective review for AllMusic, Dave Thompson gave the album four and half stars and wrote that "Suzi Quatro remains one of the most nakedly sexual albums of the entire glam rock epoch -- and one of the hottest debuts of the decade." Suzi Quatro – bass, lead vocals Len Tuckey – guitars, backing vocals, slide guitar Alastair McKenzie – piano, backing vocals, electric piano, Mellotron Dave Neal – drums, backing vocals Engineer – Pete Coleman Mastering – Chris Blair Producer – Mike Chapman, Nicky Chinn Cover photography – Gered Mankowitz
```

## Album 220: Social Dancing — bis

- **album_id:** `22919d5e-4b88-49b1-a87d-2b9e24b384fc`
- **Tags (identification only):** electronic, synth pop, indie rock, pop, rock
- **Chunks:** 1 (178 words)

### Album 220, chunk 1

```text
Social Dancing is the second studio album by the Scottish musical trio Bis, released in 1999. The Austin Chronicle thought that "while Social Dancing is enjoyable as a hyperactive whirl through Brit-pop forms of the Eighties and early Nineties, this homage to the material world lacks the rebel edge of the band's earlier work." Rolling Stone noted that "this time the guitars are tuned, the drum-machine beats are smoother, and the pep-rally yelps are more determinedly melodic." Tim Sendra of AllMusic wrote that Bis "tried a whole bunch of different stuff, from more punky rave-ups to slinky trip-hop, and if the end result is a little scattered, it's also an enjoyable mess." Lois Maffeo – vocals on "Detour" Vincent Flaming – violin on "Theme from Tokyo" Alan Mason – violin on "Theme from Tokyo" Helen Mosherry – cello on "Theme from Tokyo" Martin Wiggins – viola on "Theme from Tokyo" Andy Gill – occasional guitar and keyboards Rik Flick – occasional guitar and keyboards Richie Dempsey – drum kit sample Andy Gill – producer Bob Kraushaar – mixing
```

## Album 221: Live! — The Police

- **album_id:** `52a97cc7-57e6-404e-869b-2916318af577`
- **Tags (identification only):** rock, pop rock, pop, 1995, new wave, the police
- **Chunks:** 3 (681 words)

### Album 221, chunk 1

```text
Live! is a live album by the Police, released in 1995 on compact disc and cassette tape. It is the band's first live album and one of only two covering their initial period of activity before 1986, the other being Around the World (2022). A live album from the reunion tour, Certifiable: Live in Buenos Aires, was released in 2008. According to Andy Summers, the idea of releasing an album of live material by The Police went back as far as 1982. Up until that point, a few live tracks had only surfaced on B-sides and compilations such as Urgh! A Music War (1980). The plan was to have a new album of the band to act as a stopgap between Ghost in the Machine (1981) and Synchronicity (1983). The record was mixed and mastered in Canada but never released. Similar plans took place in 1984 at the tail of the band's Synchronicity tour, but the project was shelved again, this time in favour of a greatest hits album (Every Breath You Take: The Singles). In 1995, thanks to the technical possibilities and greater running time offered by the CD format, the idea regained momentum and Summers was invited to produce. The album features the band performing at two very distinct periods of its career. Disc one contains almost the complete concert on 27 November 1979 at the Orpheum Theatre in Boston, Massachusetts. It features mostly material from the first two albums, Outlandos d'Amour and Reggatta de Blanc, as well
```

### Album 221, chunk 2

```text
as songs only released as singles or B-sides such as "Fall Out" and "Landlord". The performance was broadcast by the WBCN (FM) radio in Boston. Disc two contains excerpts from two concerts on 2–3 November 1983 in Atlanta, Georgia at The Omni during the Synchronicity tour for the album of the same name. On this occasion the band was augmented by three backing vocalists. Both shows were widely known to fans as they had been circulating in bootleg format for many years. The 1983 shows were also featured in the 1984 Synchronicity Concert VHS and the 2005 DVD release, and a live version of "Tea in the Sahara" had been released as the B-side of "King of Pain" in 1984. Live! contributed to refresh the popularity of The Police about a decade after their break-up. It also had the merit of showcasing the band's live activity, and their propensity for rearranging and extending known songs such as "Roxanne" and "Walking on the Moon". An edited version of "Can't Stand Losing You" from the Boston performance was released as a single and reached number 27 in the UK charts, while the album itself reached number 25. Live! was generally well received. David Sinclair in Q magazine noted how the album added an important dimension to the band's recorded legacy by offering a reminder of why The Police were one of the great performing acts of their day. Paul Colbert from Encore Magazine wrote: "It may have taken 10 years for a
```

### Album 221, chunk 3

```text
live album to materialise, but these two CDs were worth the wait, capturing two essential periods, two indispensable sets of material". Andrew Abrahams emphasised the difference between the two performances, observing how the one in Boston "captures a hungry rock band on its ascent" while the one in Atlanta "is more predictable, revealing a super-group that has settled into fame and commercial acceptability". In a November 1993 interview with Q magazine, Sting seemed to agree on this point: "I remember those small gigs so much better than the stadium shows. I can remember pretty well every night of the first tour: which gigs had tricky stairs to negotiate with the gear; what was said in the dressing room; which encores we did. But a stadium just looks like a stadium". Sting – lead vocals, bass, synthesizers, Taurus pedals, pan flute, oboe Andy Summers – guitar, synthesizers, Taurus pedals, backing vocals, lead vocals on "Be My Girl – Sally" Stewart Copeland – drums, percussion, xylophone, backing vocals Michelle Cobb – backing vocals Dolette McDonald – backing vocals Tessa Niles – backing vocals
```

## Album 222: Fishing for Fishies — King Gizzard & the Lizard Wizard

- **album_id:** `ee196816-df24-4eec-8f7c-58cf2996e442`
- **Tags (identification only):** psychedelic rock, boogie rock, neo psychedelia, fish, progressive rock, psychedelic pop, punk blues, rock
- **Chunks:** 3 (629 words)

### Album 222, chunk 1

```text
Fishing for Fishies is the fourteenth studio album by Australian psychedelic rock band King Gizzard & the Lizard Wizard. It was released on 26 April 2019 by Flightless and ATO Records. The announcement of the album was accompanied by the release of the title track and its video. At the ARIA Music Awards of 2019, the album was nominated for Best Blues and Roots Album, losing to The Teskey Brothers for Run Home Slow. Fishing for Fishies was first teased by the band on 21 January 2019—over a year after the release of the last of their five 2017 albums, Gumboot Soup—when they posted a picture of themselves in the studio on social media with the caption "new music coming soon". Shortly afterward, they released the album's first single, "Cyboogie", as a 7" single with "Acarine" as the B-side, along with an accompanying music video. In March 2019, details of the album were apparently leaked to webstores, including the album title, cover, and track listing, which included both "Cyboogie" and "Acarine", as well as the entire title track and minute-long previews of the other tracks. The band confirmed the leak on 11 March, officially announcing the album through social media. The next day, the title track was officially released as a music video on YouTube. The album's third single, "Boogieman Sam," was released on 28 March. Regarding the album, band frontman Stu Mackenzie said, "We tried to make a blues record. A blues-boogie-shuffle-kinda-thing, but the songs kept fighting it—or maybe
```

### Album 222, chunk 2

```text
it was us fighting them. Ultimately though we let the songs guide us this time; we let them have their own personalities and forge their own path. Paths of light, paths of darkness. This is a collection of songs that went on wild journeys of transformation." Sections of the album were recorded at a house owned by members of Tropical Fuck Storm. During these sessions, members of both bands recorded a large jam known as the "Hat Jam"—elements of which were later reused and incorporated into the first single of King Gizzard's 2022 album Omnium Gatherum, "The Dripping Tap", and Tropical Fuck Storm's joint EP with King Gizzard Satanic Slumber Party. Shortly before the release of Fishing for Fishies, a short behind-the-scenes documentary titled How to Gut a Fishie was uploaded to YouTube by the band, showcasing clips of the recording sessions of Fishing for Fishies and Hat Jam. The album received mostly positive reviews, though Sophie Kemp of Pitchfork rated it 4.8 out of 10 and wrote that the album "is vaguely about the environment, but mostly about goofing off with expensive equipment in service to the concept of 'boogie oogie ooging'". NME rated it four stars, saying that the album was "their most accessible and immediate album to date". DIY's Connor Thirlwell gave the album three and a half out of five stars, noting that "King Gizzard and the Lizard Wizard still know how to kick ass". Stu Mackenzie – vocals (1–4, 6, 8, 9), electric guitar (1,
```

### Album 222, chunk 3

```text
2, 4–6, 8), keyboards (1, 2, 6, 9), mellotron (1–3, 6–8), piano (3, 6–8), synthesizer (8, 9), organ (3, 5), bass (2, 3, 5–7), flute (3, 4, 8), drums (2, 8), vibraphone (5, 7), percussion (2, 8) Ambrose Kenny-Smith – vocals (1, 2, 4–6, 8), harmonica (1, 2, 4–8), mellotron (2), piano (6), keyboards (9), percussion (5, 6) Joey Walker – electric guitar (1, 5, 7), bass (2, 4, 6), synthesizer (7–9), keyboards (7), acoustic guitar (7), percussion (4), vocals (4, 7) Cook Craig – electric guitar (1, 2, 7), bass (1, 3, 5), synthesizer (9), vocals (4) Michael Cavanagh – drums (1–9), percussion (3–5, 7), vocals (4) Lucas Skinner – bass (5), synthesizer (9), shaker (4), vocals (4) Eric Moore – drums (1, 6) Han-Tyumi – vocals (9)
```

## Album 223: The Sound of Madness — Shinedown

- **album_id:** `a5cb0c7a-0f4e-4db0-962b-fbe8f43d6d48`
- **Tags (identification only):** hard rock, alternative metal, rock, post grunge, pop rock, grunge
- **Chunks:** 5 (1148 words)

### Album 223, chunk 1

```text
The Sound of Madness is the third studio album by American rock band Shinedown, released June 24, 2008, via Atlantic Records. The album's lead single, "Devour", was released to radio on May 5, 2008. It is their first release to feature Eric Bass and Zach Myers, their only release to feature Nick Perri, and their only album as a five-piece. A deluxe version was released on November 23, 2010. The album's lyrics explore diverse subject matter as opposed to their previous albums; "Devour" explores political and anti-war themes, "If You Only Knew" is a love ballad about singer Brent Smith's then-fiancée and son, and "What a Shame" tells the story about the death of Smith's uncle, and how he and his cousin, professional wrestler Olivia Smith, dealt with it. Shinedown's tour to support the album subsequently started with the band playing a few festival shows before the release of The Sound of Madness. The Sound of Madness is Shinedown's most successful album, and has issued one multi-platinum single ("Second Chance"), two platinum singles ("Sound of Madness" and "If You Only Knew"), as well as all other singles going gold ("Devour", "The Crow & the Butterfly", "Diamond Eyes (Boom-Lay Boom-Lay Boom)", and "Call Me"). The album has since been certified 2× Platinum by the both RIAA and Music Canada, and Gold by the BPI. Work on a third studio album began in early 2007; while the record label requested an album to be created in six months, Smith declined, stating that
```

### Album 223, chunk 2

```text
he was not happy with the results of working under the time restraints on the last album, and wished to take his time on the album. The label agreed to this, ultimately allowing Smith to take eighteen months to prep the album. Part of the long development time was due to internal issues within band members; during this time, Smith fired both Stewart and Todd from the band. Smith let Stewart go due to disagreements with the direction of the band, feeling that Stewart was no longer happy or committed to the band. Todd was fired due to major disagreements with Smith, and personal problems that were getting in the way of the band. Then-touring guitarist Zach Myers later recounted that both Smith and Todd were going through significant substance abuse issues at the time with drugs and alcohol, which lead to much infighting between the two. The band almost broke up during the period, but Smith firing Todd and stopping his drug use helped eliminate the internal issues, and helped the band move forward. Smith spent much of 2007 writing new material, alone, for the third album. Sessions were prolific, with Smith writing over 60 songs during the period, though the fact that he now lacked a guitarist and bassist was a constant concern. Smith recruited a number of studio musicians for its recording sessions; Dave Bassett contributing most of the album's guitars, Tim Pierce, contributing some additional guitar, and Chris Chaney contributing most of the album's bass guitar.
```

### Album 223, chunk 3

```text
The rough demos were sent from the record label to music producer Rob Cavallo, who, upon hearing them, told Smith he wanted to produce the album. The final result, The Sound of Madness was released on June 24, 2008. The first single, "Devour", was released on May 6, 2008, and was the band's second No. 1 on the active rock chart. In order to start touring in support of the album, Smith assembled a new official lineup for the band, consisting of Nick Perri of Silvertide on lead guitar, Eric Bass on bass guitar, and upgrading touring member Meyers to a permanent rhythm guitarist position. Perri toured only briefly with the band in 2008, before leaving to pursue a solo career, a move Smith was fine with, as he felt the band operated better as a quartet, leaving Myers as the primary guitarist. Through multiple successful single releases, and extensive touring, the album ended up being the band's best-selling, staying on the Billboard 200 charts for 120 consecutive weeks, and eventually being certified double platinum in the United States, indicating two million units sold. Six singles were released from the album: "Devour", "Second Chance", "Sound of Madness", "If You Only Knew", "The Crow & the Butterfly", and "Diamond Eyes (Boom-Lay Boom-Lay Boom)", each one topping a Billboard rock music chart. Of particular note was "Second Chance", which crossed over to the top 10 of the Billboard Hot 100, peaking at number 7, and eventually being certified triple platinum, indicating three
```

### Album 223, chunk 4

```text
million units of the single sold. The band, with its new lineup, once again toured extensively in support of the album release, spending over two years on live performances. Tours include a European tour with Disturbed in 2008, the "Stimulate This!" tour with Staind, Chevelle, Halestorm, and Lo-Pro, in 2009, the Download Festival, in the United Kingdom, in 2009. The band continued touring into 2010, including headlining the "Carnival of Madness" tour, which involved larger, 10,000 capacity arena venues, and a later "Anything and Everything Tour", which involved acoustic performances in smaller venues and Q&A sessions with the crowd. Somewhere in the Stratosphere, a live album/DVD, was released in May 2011, documenting performances from both tours. The Sound of Madness received positive reviews. Tim Grierson at About.com stated "Though hard rock remains Shinedown's forte, this new record suggests that the band members are more than willing to pursue other sonic territory in order to better express themselves." and referred to "Devour" and the title track as the album's "most explosive" songs. The album is referred to as Shinedown's best one by Alternative Addiction, who also called it one of the best albums of 2008. Ed Thompson of IGN wrote a positive review, stating that "There really is nothing new or Earth-shatteringly original included here. But likewise, there really isn't a weak track on the record." However, Stephen Thomas Erlewine of AllMusic gave a mixed review, noting that "Shinedown serve up what they always have: active modern rock embodying the sound
```

### Album 223, chunk 5

```text
of post-grunge in the new millennium without offering much that is memorable, either for better or for worse." In 2024, Loudwire staff elected it as the best hard rock album of 2008. Brent Smith – lead vocals Zach Myers – rhythm guitar Nick Perri – lead guitar Eric Bass – bass Barry Kerch – drums Chris Chaney – bass Tim Pierce – rhythm guitar Dave Bassett – rhythm guitar Bobby Huff – rhythm guitar and keyboards on "Breaking Inside" Dale Oliver – guitar on "Breaking Inside" Rob Cavallo – rhythm guitar and piano on "Call Me" David Campbell – string arrangements and orchestration Jamie Muhoberac – keyboards Lzzy Hale – guest vocals on 2010 deluxe re-issue version of "Breaking Inside" Rob Cavallo – producer Doug Mckean – engineer, mixing (track 2) Chris Lord-Alge – mixing (tracks 1, 3–11) Ted Jensen – mastering at Sterling Sound in NYC, NY
```

## Album 224: Dark Comedy — Open Mike Eagle

- **album_id:** `4381b55c-5275-464a-9419-cd5521c9bee5`
- **Tags (identification only):** hip hop, abstract hip hop, abstract, anxious, conscious, drugs, eclectic, existential
- **Chunks:** 1 (160 words)

### Album 224, chunk 1

```text
Dark Comedy is a studio album by American hip hop artist Open Mike Eagle. It was released via Mello Music Group on June 10, 2014. It includes guest appearances from Kool A.D. and Hannibal Buress. Music videos were created for "Qualifiers", "A History of Modern Dance", "Doug Stamper (Advice Raps)", "Dark Comedy Morning Show", and "Informations". At Metacritic, which assigns a weighted average score out of 100 to reviews from mainstream critics, the album received an average score of 73, based on 7 reviews, indicating "generally favorable reviews". Jessica Rew of HipHopDX gave the album a 4.0 out of 5, saying, "Even with its melancholy closing, Dark Comedy is an incredibly fulfilling listen." Nate Patrin of Pitchfork gave the album an 8.0 out of 10, saying, "Whether it's through casual observation or the to-the-bone identity struggles, Open Mike Eagle's overlap between amusing insights and uncomfortable truths makes for one of the most compelling indie-rap listens of the year so far."
```

## Album 225: I’m Wide Awake, It’s Morning — Bright Eyes

- **album_id:** `c4d25c07-9f77-4519-86b6-afa4c1e5dd0f`
- **Tags (identification only):** alternative punk, indie rock, rock, country, country rock, emo folk, indie, indie folk
- **Chunks:** 3 (615 words)

### Album 225, chunk 1

```text
I'm Wide Awake, It's Morning is the sixth studio album by American band Bright Eyes, released on January 25, 2005, by Saddle Creek Records (the same day as their seventh album, Digital Ash in a Digital Urn). The album was reissued by Dead Oceans alongside a six-track companion EP on November 11, 2022. The music video for "First Day of My Life" was directed by John Cameron Mitchell. This was the first Bright Eyes album to feature Nate Walcott, who is now a permanent member of the band. "Road to Joy" contains an interpolation of Beethoven's "Ode to Joy". The title of the album is taken from a lyric in this song. Bright Eyes achieved success on the US charts when the singles "Lua" and "Take It Easy (Love Nothing)" (the latter from Digital Ash) took the top two positions on the Billboard Hot Singles Sales chart in 2004. In 2005, the band set off on a two-part world tour to promote the album along with Digital Ash in a Digital Urn, with the first half of the tour centring on the folk-influenced first album, and the latter half featuring the more electronic second album. Both records made it into the top 20 of the Billboard albums charts, with I'm Wide Awake, It's Morning peaking at number 10 on the Billboard 200 and at number 2 on the Billboard Independent Albums chart. The tour was captured on the album Motion Sickness, released later in the year. I'm Wide Awake, It's
```

### Album 225, chunk 2

```text
Morning received widespread acclaim from music critics. At Metacritic, the album received an average score of 85 out of 100, based on 33 reviews, which indicates "universal acclaim". Los Angeles Times describes it as "An album with the simmering glow of a masterpiece." Drowned in Sound critic Sean Adams called the album a "thing of awe", praising the lyrics and "calculated attention to detail". Pitchfork's Chris Dahlen gave the album 8.7 out of 10 and states "I'm Wide Awake weaves the personal and the political more fluidly than most singers even care to try, and the consummate tunefulness just strengthens those moments where he pinches a nerve." In a less positive review, Stephen Thomas Erlewine of AllMusic criticized Oberst's "heavy-handed pretension in the words and [...] affectedness in his delivery", calling the album proof that "instead of reaching musical maturity, he's wallowing in a perpetual adolescence." Up to 2014, the album had sold 522,000 copies in US. In 2007 it was awarded a gold certification from the Independent Music Companies Association, which indicated sales of at least 100,000 copies throughout Europe. The album was ranked on several lists for best albums released during the year 2005. It was also ranked at number 50 on Rolling Stone list of "Top 100 Albums of the Decade" and at number 31 on NME's "Top 100 Greatest Albums of the Decade". Conor Oberst – guitar, vocals Mike Mogis – mandolin (tracks 1, 2), pedal steel (tracks 3, 5, 7, 9), 12 string guitar (track
```

### Album 225, chunk 3

```text
10) Nate Walcott – trumpet (tracks 2, 3, 8, 10) Nick White – piano (tracks 2, 8), organ (tracks 3, 7, 9, 10), Rhodes (track 5), vibraphone (track 8) Jesse Harris – guitar (tracks 1, 2, 5–8) Alex McManus – guitar (track 3, 10) Tim Luntzel – bass (tracks 1, 3, 6, 7, 8) Matt Maginn – bass (tracks 2, 5, 9, 10) Jason Boesel – drums (tracks 2, 3, 5, 7, 9) Clark Baechle – drums (tracks 3, 7, 10) Jim James – vocals (track 1) Emmylou Harris – vocals (tracks 2, 7, 8) Maria Taylor – vocals (tracks 3, 9) Andy LeMaster – vocals (track 3) Jake Bellows – harmonica, vocals (track 5)
```
