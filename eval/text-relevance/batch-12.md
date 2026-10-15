# Embedding text relevance, batch 12 of 12 (albums 276–300 of 300)

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

This batch: **25 albums, 77 chunks**.

## Album 276: Serious Moonlight — David Bowie

- **album_id:** `c01a73de-7b5c-470b-b42b-091805076b66`
- **Tags (identification only):** new wave, pop rock, 1–4 wochen, art rock, blue eyed soul, blues, funk rock, offizielle charts
- **Chunks:** 1 (237 words)

### Album 276, chunk 1

```text
Serious Moonlight is a concert video by the English singer-songwriter David Bowie. Filmed in Vancouver on 12 September 1983, on the singer's "Serious Moonlight Tour", the video was released on VHS and laserdisc in 1984 and on DVD in 2006. The concert includes most of the songs from the concert although "Star", "Stay", "The Jean Genie", "Red Sails" and "Modern Love" were left off the 1984 release due to time constraints; the songs were not reinstated for the 2006 DVD release. A live version (audio only) of "Modern Love", recorded on 13 July 1983 at a show in Montreal and originally released as the B-side to the studio version of the same song, can be found elsewhere on the 2006 DVD release as background music for the photo gallery. The audio and exact setlist from the concert film was reused for the Serious Moonlight (Live '83) live album, included with the Loving the Alien (1983–1988) box set in 2018 and released separately the following year; the live album additionally includes the aforementioned live recording of "Modern Love" as the final track. The 2006 DVD release of Serious Moonlight also contains, as an extra, the 1984 documentary/ concert film Ricochet, chronicling Bowie's experiences in Hong Kong, Singapore, and Bangkok on the Asian leg of the Serious Moonlight tour. Ricochet was previously released to home video in the mid-1980s in a shorter version, separately from the Serious Moonlight video.
```

## Album 277: Electric — Pet Shop Boys

- **album_id:** `467d7c1f-ba26-4312-b124-dd5979cbfb8c`
- **Tags (identification only):** house, synth pop, dance pop, electro house, electronic, pop, synthpop
- **Chunks:** 5 (1187 words)

### Album 277, chunk 1

```text
Electric is the twelfth studio album by English synth-pop duo Pet Shop Boys. It was released on 14 July 2013 on the duo's own label, x2, through Kobalt Label Services as the duo's first album since their departure from Parlophone. Electric was the first in a trilogy of albums produced by Stuart Price, followed by Super and Hotspot. The single "Thursday" features a collaboration with English singer and rapper Example. Electric reached number three on the UK Albums Chart and number 26 on the US Billboard 200, the duo's highest chart performances in both territories in 20 years. The album was supported by the Electric Tour which visited 46 countries through 112 concerts. Electric was completed less than a year after the Pet Shop Boys' previous album, Elysium. They had several unused songs, including "Axis", "Vocal", "Inside a Dream", "Shouting in the Evening", and a cover version of Bruce Springsteen's "The Last to Die". Their intention was to make a dance record, and they enlisted Stuart Price, the music producer of their Pandemonium Tour, who had remixed the last single from Elysium, "Memory of the Future". As they added new material, the project developed into a full-fledged album. Price stated that his goal was for every track to have a "euphoric, fresh feel to it". The more dance-influenced nature of Electric was a response to the "reflective mood" of Elysium. Neil Tennant commented, "Elysium was about growing old; Electric is about remembering that sense of youthful excitement". The album title
```

### Album 277, chunk 2

```text
was chosen "because that's what it is—electronic music that we hope is exciting." Pet Shop Boys recorded the album between November 2012 and April 2013. They worked at Price's London studio for the first few months. Later in the process, Price was in Los Angeles, and the duo exchanged material with him from London and Berlin. Price decided to record the songs in alphabetical order, starting with "Axis" and ending with "Vocal", which was finished on the day the album was scheduled to be completed. "Fluorescent" was added as a ninth track during the last month of recording after Chris Lowe sent Tennant a demo. Price finished mixing the album in late April. Electric is the first Pet Shop Boys studio album that was not released through Parlophone, after 28 years with the label. Pet Shop Boys announced the launch of their own label, x2, in partnership with Kobalt Label Services, for Electric and future releases. Chris Lowe was given credit for the name x2, pronounced "times two". The album was released in the UK on 14 July 2013 on CD, digital download, and LP formats. Germany, Austria, Switzerland, Netherlands, Belgium, Luxembourg, Australia, and New Zealand had an earlier release date of 12 July; and in the United States, Canada, South America, Spain, and most other countries, the album was released 16 July. A limited-edition LP boxset from The Vinyl Factory was announced in July and released in December 2013. The five-disc coloured vinyl set had one song per side
```

### Album 277, chunk 3

```text
and a blank side signed by Tennant and Lowe. The pressing was limited to 350 copies, and The Electric Box became a collector's item, with one selling for $2,243 on Discogs in 2023. The album cover features a blue zigzag pattern on a white background. The pattern represents a lightning strike in an op art style. The artist name and album title do not appear on the cover. It was designed by Mark Farrow, with input from his colleague Fred Ross, with a focus on how the image would look on a smartphone screen. Tennant chose the colour blue as a reference to the lyric "Blue, blue, electric blue" in the David Bowie song "Sound and Vision" (1977). The limited-edition boxset included five heavyweight vinyl records in different fluorescent colours—orange, yellow, pink, green, and white—housed in a transparent, multi-coloured acrylic box with fluoroscent-edges. The intended effect was a glowing prism. The set came with assembly instructions and white gloves for handling the discs, along with an insert listing the tracks and credits. On 14 March 2013, Pet Shop Boys debuted a short trailer for Electric on YouTube. The entire album was made available for streaming in the United Kingdom via The Guardian on 9 July. In support of the album, the duo embarked on the Electric Tour, which began on 22 March 2013 at the Cumbre Tajín festival in Veracruz, Mexico, where they debuted two songs from the album: "Axis" and their cover version of Springsteen's "The Last to Die".
```

### Album 277, chunk 4

```text
The tour's first official date took place at the Movistar Arena in Santiago, Chile, on 13 May 2013. The setlist featured songs from the forthcoming album, including "Vocal" as the final encore. On 30 April 2013, immediately following the official album announcement, "Axis" premiered with a video and digital release. The Boys Noize remix of the song was released on 14 May. The single "Vocal" premiered on 1 June 2013 on DJ Dave Pearce's BBC Radio 2 show Dance Years, followed by a digital release on 3 June. A CD single and digital download were released on 29 July, featuring new remixes of the song, and a 12-inch vinyl single was released on 9 December. "Love Is a Bourgeois Construct" was released as a single on 2 September 2013. The single contains remixes and two B-sides, "Entschuldigung!" and "Get It Online". The single "Thursday" was released on 4 November 2013, with remixes and two B-sides, "No More Ballads", "Odd Man Out". The video footage for the video was shot in Shanghai. "Fluorescent" was released as a limited edition 12-inch vinyl to celebrate Record Store Day 2014 on 19 April. Electric received widespread acclaim from music critics. At Metacritic, which assigns a normalised rating out of 100 to reviews from mainstream publications, the album received an average score of 84, based on 28 reviews, which indicates "universal acclaim". Dorian Lynskey of Q praised several songs on the album and noted, "With Electric, Pet Shop Boys have succeeded spectacularly." Simon Price, music
```

### Album 277, chunk 5

```text
critic for the Independent on Sunday, described the album as "sublime". Neil McCormick of The Daily Telegraph commented that "Electric is the second really fantastic pop-dance blast of the year". The album debuted at number three in the United Kingdom on the UK Albums Chart, selling 15,715 copies in its first week, becoming Pet Shop Boys' highest-charting studio album in the UK since Very topped the chart in 1993. In the United States, Electric debuted at number 26 on the Billboard 200, with first-week sales of 11,000 copies, becoming the duo's highest-charting US album since Very peaked at number 20 in 1993. It also debuted at number two on Billboard's Dance/Electronic Albums chart. Elliot Gleave – vocals (8) Stuart Price – additional programming (all tracks); additional vocals (3) Andy Crookston – additional vocals (3) Pete Gleadall – additional vocals (3); additional programming (3, 6, 9) Luke Halls – additional vocals (3) Jessica Freedman – additional vocals (8) Katharine Anne Hoye – additional vocals (8) Adam Blake – handclaps (5) Stuart Price – production, engineering, mixing Pete Gleadall – additional engineering (3, 6, 9); additional vocals recording (3)
```

## Album 278: Hit to Death in the Future Head — The Flaming Lips

- **album_id:** `b98c6fbb-4e86-4ea5-9cb4-26a997f96198`
- **Tags (identification only):** psychedelic rock, rock, neo psychedelia, noise pop, alternative rock, drone, indie rock, noise
- **Chunks:** 2 (362 words)

### Album 278, chunk 1

```text
Hit to Death in the Future Head is the fifth studio album by American rock band the Flaming Lips, released on August 11, 1992, by Warner Bros. Records. "Talkin' 'Bout the Smiling Deathporn Immortality Blues (Everyone Wants to Live Forever)" was released as the lead track on the EP Yeah, I Know It's a Drag... But Wastin' Pigs Is Still Radical to promote the album. The title provided the inspiration for the name of the British band the Futureheads. Recorded in 1991 by the same lineup of the Flaming Lips that had been featured on In a Priest Driven Ambulance, the album's release was delayed for nearly a year due to the use of a sample from Michael Kamen's score for the 1985 film Brazil in the track "You Have to Be Joking (Autopsy of the Devil's Brain)", which required a lengthy clearance process. During the intervening period, both Nathan Roberts and Jonathan Donahue left the band (the latter resuming his duties in Mercury Rev). By the time of the album's release both Steven Drozd and Ronald Jones had joined, and performed on the subsequent tour. The album is known for a particularly long hidden track at the end of the CD that consists of a continuous burst of staccato noise that pans from channel to channel and lasts for nearly a half-hour. This track is omitted from the vinyl and cassette release. From contemporary reviews, Andrew Perry of Select gave Hit to Death in the Future Head a five
```

### Album 278, chunk 2

```text
out of five rating, noting the groups "gorgeously melodic garage pop is rarely short of breathtaking", and compared the band to Mercury Rev, declaring that if "Yerself Is Steam has seldom left your turntable, this won't either. Magnificent." From retrospective reviews, AllMusic's Jason Ankeny noted that even though the album's "not as conceptually tight as In a Priest Driven Ambulance", it's "no less cohesive or imaginative", and ultimately concluded that the album "serves as the bridge between the band's noisier, more hallucinatory indie work and the acid-bubblegum aesthetic perfected on their later Warner Bros. albums". Wayne Coyne – vocals, guitar Michael Ivins – bass Jonathan Donahue – guitar Nathan Roberts – drums
```

## Album 279: Stalled Flutes, means — Asian Glow

- **album_id:** `95e17b3b-c67b-4586-8c57-8e51a264edb3`
- **Tags (identification only):** emo, folktronica, noise pop, art rock, indie rock, indietronica, post rock, shoegaze
- **Chunks:** 1 (120 words)

### Album 279, chunk 1

```text
Stalled Flutes, Means (stylised in Stalled Flutes, means) is the third studio album by South Korean rock singer-songwriter Asian Glow. The album was released on 13 June 2022, and Sneezing: Seasonal Creators was released as a single prior to the album's release. JohnnyoftheWell of Sputnikmusic reviewed "Though tallest and most majestic, it’s just one moment on an album teeming with moments building and moments escaping: grasp one, however fleetingly and you can grasp them all." Jay Honeycomb, the critic of PopMatters and No Transmission described the album as "The confidence he has in his craft typically comes with hard-won struggles and failures. On the other hand, the songs have a youthful passion, like Asian Glow is really "going for it""
```

## Album 280: Hozier — Hozier

- **album_id:** `3708a0c7-d3fd-4bb3-86e2-18b5670c4457`
- **Tags (identification only):** blue eyed soul, blues, blues rock, chamber pop, alternative, indie rock, pop soul, rock
- **Chunks:** 8 (1803 words)

### Album 280, chunk 1

```text
Hozier is the debut studio album by Irish musician Hozier. It was released on 19 September 2014 by Island Records and Rubyworks Records. Before the album's release, he attracted attention from his 2013 and 2014 EPs Take Me to Church (2013) and From Eden (2014), which contained songs that were later included on the album. Hozier collaborated with producer Rob Kirwan during its recording. Hozier has been described as a blues, soul and indie rock album with elements of gospel, R&B and folk music. Hozier received positive reviews from music critics, many of whom praised Hozier's songwriting and vocal performance. The record was also commercially successful, reaching top ten positions in several countries, including Ireland, the United Kingdom, the United States, Canada, Australia, New Zealand, the Netherlands, Denmark and Sweden. Five of the album's singles—"Take Me to Church", "From Eden", "Sedated", "Work Song", and "Someone New"—charted in the top-50 of the Irish Singles Chart. The album's lead single, "Take Me to Church", was a huge success worldwide and also earned a nomination for Song of the Year at the 57th Annual Grammy Awards in 2015. Following the release of the record, "Jackie and Wilson" and "Cherry Wine" were released as the album's sixth and seventh singles, respectively. Hozier began writing songs at the age of 15. He taught himself guitar and sang in his school choir. He later studied music education at Trinity College Dublin but was refused a year's deferral by the college after missing exams to record demos
```

### Album 280, chunk 2

```text
for a music label. While at Trinity, Hozier became involved with the Trinity Orchestra. He was a member of the choral ensemble Anúna from 2007 to 2012 and appears as a soloist on their 2014 release Illuminations singing "La Chanson de Mardi Gras". He toured and sang with the group internationally including performances in Norway and the Netherlands. Hozier played at Oxegen Festival in 2009 and 2010. In 2011, he opened up for a performance for Alex Winston in Dublin. In 2012, Hozier appeared as a backup singer for Billy Ocean. Hozier began writing the album after ending his first relationship, saying it forced him to "reflect" upon what being in love meant, having reasons to "distract" himself and "cultivate his ideas" before "turn(ing) them into music". Hozier has stated that there are "a lot of recurring themes" in the album dealing with "personal liberations - finding yourself, accepting yourself, and making sense of yourself" in trying to be honest about "the more wonderful and awful things of your day-to-day". He describes his initial efforts as "angsty, lonely songwriting that teenagers do". He wrote "Take Me to Church" in his parents' living room and recorded the song in a "makeshift attic studio" in Wicklow, collaborating with producer Rob Kirwan. At a live performance in Boston, Hozier explained that "Cherry Wine" was recorded at five in the morning in an old, abandoned hotel with a caved-in roof and walls covered in graffiti. The cover artwork is a painting made by Hozier's
```

### Album 280, chunk 3

```text
mother Raine Hozier-Byrne, who also did the artworks of the album's singles. Hozier is a blues, soul and indie rock record, featuring elements of gospel, R&B and folk. The album contains an "Americana-rock blend with oily guitar riffs, crashing high-hats, angelic choruses and sung-spoken verses...", characterized by subtle guitar, strong percussion, dark instrumentals, whimsical strings, "soulful" and raw vocals and "haunting" melodies". The standard edition of Hozier is just under an hour long, consisting of thirteen tracks, while the deluxe edition adds four bonus songs to the record. The album was solely written by Hozier, except "Someone New", which was co-written with his former girlfriend Sallay-Matu Garnett. The album was produced by Hozier and Rob Kirwan. Hozier opens with "Take Me to Church", a gospel-inflected mid-tempo blues song with "sweeping orchestral choruses" showcasing the artist's vocal range ascribing religious terminology to the nuances of a romantic relationship. "Angel of Small Death and the Codeine Scene" is a blues and indie-rock track, containing guitar riffs, clapping hands, and church organs with a half-time beat, describing a "temptress" in "stained-glass colors", lamenting the unavoidable "curse of being young in love". "Jackie and Wilson" is a bluesy, laid-back soulful rockabilly track, backed by an "angelic choir of harmonies, a tribute to American singer Jackie Wilson. It features "tongue-in-cheek" lyrics musing about a couple "naming their children Jackie and Wilson" while "rais[ing] them on rhythm and blues." "Someone New" is a pop-like whimsical spring-stepped indie-rock song with strong strings, a pizzicato bass and choral
```

### Album 280, chunk 4

```text
harmonies, discussing a wandering celebration of "renewed love" in the face of strangers. "To Be Alone" is melancholy blues song containing a simplistic drumbeat guitar licks and church organs, depicting the "euphoric" attraction of solitude with a partner. "From Eden" features a flamenco bridge, referencing the titular garden in its Biblical imagery and describing a journey to "find himself as much as the girl", with the narrator "slithering" to his lover's door. "In a Week" is a Celtic-inspired folk duet with breathy harmonies from Karen Cowley detailing pastoral fantasy about decomposing amongst the fauna of the Wicklow Mountains alongside his love. "Sedated" is a soulful track with tinkling piano and gospel melodies with depicts a "warning" of personal decay within a relationship. "Work Song" is a gothic-spiritual love song with murmurous vocals, tambourine, and a strong melodic bass, discussing a promise of devotion beyond the grave. "Like Real People Do" is an acoustic song in a "warm" higher key with keening vocals, its lyrics intertwining metaphors of insects and nature, while pleading for his sweetheart to kiss him in affection. "It Will Come Back" is a twangy track with "devilish" strings slide guitar riffs and tambourines with deviant notations while "Foreigner's God" has a soulful edge with loaded lyrical and religious allegories. "Cherry Wine" ends the album on an apologetic note with an intimate acoustic live-recording that juxtaposes the samples of chirping birds and soft guitar with the description of a tempestuous, abusive relationship. The album was available to pre-order
```

### Album 280, chunk 5

```text
in Europe upon its announcement with North American and Australian pre-order dates from July 2014. The album was released 19 September 2014. The album was distributed by Island Records in most of the world and by Columbia Records in the United States, Canada and Australia. "Take Me to Church" was announced by Hozier as the lead single from the album and was released on 13 September 2013. The song peaked at #2 on the Billboard Hot 100, becoming Hozier's highest-charting single in the U.S. to that date. The music video, alluding to themes of homophobia, was released that same month, having been created on a "shoestring budget" and filmed entirely in black-and-white. The video was shared by gay English actor Stephen Fry, which helped it reach the front page of Reddit and subsequently go viral. "Take Me to Church" saw Hozier's rise to prominence, with the song scoring top five positions around the world and gaining multi-platinum certifications; the song also garnered critical acclaim for its lyricism and messaging. "From Eden" was released as the second single from the album on 9 March 2014. The song peaked at #2 on the Irish Singles Chart. "Sedated" was released as the third single from the album on 20 May 2014. The song peaked at #3 on the Irish Singles Chart. "Work Song" was released as the fourth single from the album on 16 March 2015. "Someone New" was released as the fifth single from the album on 11 May 2015. The song
```

### Album 280, chunk 6

```text
peaked at #13 on the Irish Singles Chart. "Jackie and Wilson" was released as the sixth single from the album on 29 September 2015. "Cherry Wine" was released as the seventh single from the album on 14 February 2016. The track appeared in Zach Braff's movie Wish I Was Here, chosen for its "heartbreaking lyrics and poetry". It was later performed on the Late Late Show. Hozier toured the United States and Europe in support of the album across 2014 and 2015, with multiple shows featuring opening act Ásgeir. Irish band Wyvern Lingo opened for his performances in Ireland. Hozier received generally positive reviews from music critics. At Metacritic, which assigns a normalized rating out of 100 to reviews from mainstream critics, the album received an average score of 79, based on 10 reviews. AllMusic's Timothy Monger called the album "a strong debut", praising the singer's soulful voice and the quality of the material. "Like fellow Irishman Van Morrison did decades before, Hozier draws on the soul and R&B of Jackie Wilson and runs it through the mystery white-boy filter of Jeff Buckley, adding a touch of Bon Iver's rural indie aesthetic to mix into his own dark cocktail", he wrote. Sergiusz Królak of JazzSoul.pl claimed, "Hozier (...) revealed album with emotionally strong songs," adding that "acoustic-rock-ballad tracklist makes a great whole with deep-emotional vocal and strong lyrics". Simon Harper of Clash magazine commented that "His voice, more poitín-sweetened than whiskey-soaked, caresses delicate melodies and rougher rhythms alike with confidence
```

### Album 280, chunk 7

```text
– it lingers compellingly in the creeping blues of 'To Be Alone', whispers prettily in the folky 'Like Real People Do', and preaches fervently in the ragged R&B of 'Jackie And Wilson'. The Irishman's storytelling is suitably fluid, relying on the realism of true romance rather than affecting any impoverished Delta designs. As a result, 'Hozier' is an authentic portrait of an artist – soulful, spiritual and seductive – and is a deeply impressive first step." Rolling Stone magazine's Jon Dolan wrote, "Blessed with a sensual singing voice and a seemingly bottomless well of lapsed-Catholic-style conflict, Hozier channels Van Morrison's Celtic R&B, Southern soul and Black Keys-style garage blues into intimately roiling songs like 'Angel of Small Death and the Codeine Scene'." Helen Brown of The Telegraph noted, "Gospel choirs hum and swell tenderly beneath the rougher edges of his riffs. They add mature, universal gravitas and often a holy ecstacy to an intense, youthful lyrical tangling of religion and romantic obsession that regularly finds him poised 'between love and abuse'," adding that "Hozier mixes his tormented blues with sunny R&B." Hozier peaked at number two on the Billboard 200 and number three on the UK Albums and ARIA Charts. The album ranked at number one on the Rock Albums Chart and the Americana/Folk Chart. The album debuted at number two on the Canadian Albums Chart, selling 8,800 copies in its first week. Hozier also secured Top 15 chart positions in Belgium, Denmark, Holland, and Germany. As of March 2019,
```

### Album 280, chunk 8

```text
the album has sold 972,000 copies and has earned 2.6 million equivalent album units in the U.S. In Hozier's home country of Ireland, the record debuted at number one with 7,300 copies sold, making it the country's fastest-selling debut album by a male artist of the 2010s. It has sold 90,000 copies there.
```

## Album 281: Night Songs — Cinderella

- **album_id:** `ffa546d7-3c22-4243-a6d5-b15fa67462cc`
- **Tags (identification only):** hard rock, rock, 80s, glam metal, rock ballad
- **Chunks:** 3 (555 words)

### Album 281, chunk 1

```text
Night Songs is the debut studio album by American rock band Cinderella. It was released on June 9, 1986, by Mercury Records. Mercury issued the album worldwide, while Vertigo Records handled the album's release in the UK. The album peaked at No. 3 on the US charts on February 7, 1987, and was certified double platinum for shipping 2 million copies. In May 1991, it was certified triple platinum, having shipped 3 million copies. Leadoff single "Shake Me" failed to chart, but "Nobody's Fool" cracked the Top 20, reaching No. 13. Third single "Somebody Save Me" went to #66. On April 2, 1987, Cinderella filmed parts of their concert in Philadelphia. These live songs were, along with their three MTV videos, released on home video in August 1987 on Night Songs: The Videos. Night Songs sold several million copies due to a combination of Cinderella's breakthrough single "Nobody's Fool", MTV airplay, and an opening slot on labelmates Bon Jovi's tour, in support of their album Slippery When Wet. The album received mixed reviews. David Fricke, writing for Rolling Stone magazine, considered that "[Cinderella] need to jazz up their material and cut away the clichés if they're really interested in hard-rock immortality. Otherwise, their platinum dreams are going to turn into pumpkins". AllMusic reviewer Steve Huey called it "not bad, just generic". Canadian journalist Martin Popoff put on a par Cinderella's rise to prominence with Poison's success, judging them as "little more than vacant, colourful but life-affirming [Mötley] Crüe derivatives." He
```

### Album 281, chunk 2

```text
described the songs as "heavier than one might expect, but of course safe, shallow and watery like the kiddie pool." The album has been retrospectively considered a hair-metal classic, being ranked on a vast amount of "best of" lists. In 2015, "Sleazegrinder" of Louder included the song in his list of "The 20 Greatest Hair Metal Anthems Of All Time". The album cover was photographed by Mark Weiss at the Head House in the New Market and Head House district in Philadelphia. After the release of this album, the band slightly changed their sound to fit a more blues rock direction. In October 2014 for her birthday, guitarist Tom Keifer presented Lzzy Hale of Halestorm with the costume jewelry pin he wore on his right shoulder for the Night Songs album cover. Hale subsequently wore the pin on her right hip on the album cover for Halestorm's 2015 Into the Wild Life, to include a touch of tradition. In 2015, "Sleazegrinder" of Louder included the song "Shake Me" in his list of "The 20 Greatest Hair Metal Anthems Of All Time", placing it at number 14. In 2018, Collin Brennan of Consequence included the album in his list of "10 Hair Metal Albums That Don’t Suck". Tom Keifer – lead vocals, guitar, piano Jeff LaBar – guitar, vocals Eric Brittingham – bass, vocals Fred Coury – drums (does not play on the album, joined shortly after it was recorded) Barry Benedetta – lead guitar on "Back Home Again", "Nothin' for
```

### Album 281, chunk 3

```text
Nothin'" and "Push, Push" Jeff Paris – keyboards Jody Cortez – drums on all tracks Tony Mills – background vocals Jon Bon Jovi – background vocals on "Nothin' for Nothin'" and "In from the Outside" Bill Mattson – background vocals on "Shake Me" Andy Johns – producer, engineer, mixing at the Record Plant, Los Angeles
```

## Album 282: Blood Harmony — Larkin Poe

- **album_id:** `e55eccf3-0eb9-4429-9694-be2663b272b7`
- **Tags (identification only):** country rock, rock, southern rock, 1–4 wochen, blues, blues rock, english, jazzthing 146
- **Chunks:** 1 (97 words)

### Album 282, chunk 1

```text
Blood Harmony is the sixth studio album by American roots rock band Larkin Poe, released on 11 November 2022, by Tricki-Woo Records. Blood Harmony won the 2024 Grammy Award for Best Contemporary Blues Album. Rebecca Lovell – lead vocals, electric guitar; keyboards Megan Lovell – harmony vocals, lap steel; Dobro Tarka Layman – electric bass Tyler Bryant – programming, keyboards; electric bass Mike Seal – Hammond and Wurlitzer organs Caleb Crosby – drums; percussion Kevin McGowan – drums; percussion Trissa Lovell – harmony vocals Larkin Poe – producer Tyler Bryant – producer; engineer David Benyamin – mixing
```

## Album 283: Everything Goes Numb — Streetlight Manifesto

- **album_id:** `cae37969-b844-410c-a2bb-0ec43427c6d2`
- **Tags (identification only):** punk, ska, ska punk, alternative rock, alternative/indie rock, american, pop/rock, rock
- **Chunks:** 1 (162 words)

### Album 283, chunk 1

```text
Everything Goes Numb is the debut studio album by American ska punk band Streetlight Manifesto, released on August 26, 2003. It garnered critical acclaim, with critics commenting on the quality of the band's lyrics and their powerful energy. The album has since acquired a cult following among fans of the third wave ska movement. This is the first full-length album frontman and vocalist Tomas Kalnoky participated in since leaving the ska-punk band Catch 22. The track "If and When We Rise Again" quotes the melody of Hungarian Dance No. 5 by Johannes Brahms. Josh Ansley – bass guitar Jim Conti – alto saxophone, clarinet, tenor saxophone Jamie Egan – trombone, trumpet, tuba Tomas Kalnoky – lead vocals, guitar, layout, lyrics, music, photos, producer, recording Paul Lowndes – drum tracking, drums Dan Ross – alto saxophone, baritone saxophone Chris Bailey, Shane Thompson – auxiliary percussion Robbie Krieger – cello (track 12) Steve Ho, Lico, Jeff Davidson – gang vocals Jason Kanter – mixing
```

## Album 284: Love in the Time of Science — Emilíana Torrini

- **album_id:** `a5575cfa-81ac-440f-9c42-15baf4a5cbbf`
- **Tags (identification only):** electronic, trip hop, alternative rock, downtempo, alternative dance, dream pop, indie rock
- **Chunks:** 1 (293 words)

### Album 284, chunk 1

```text
Love in the Time of Science is the third studio album by Icelandic singer and songwriter Emilíana Torrini. It was her first album to be released internationally (her earlier albums being released only in her native Iceland). The album was recorded and released in 1999, and was produced by Roland Orzabal and Alan Griffiths of Tears for Fears, who also wrote two tracks for the album. It was recorded and mixed at Orzabal's own studio, Neptune's Kitchen, with additional recording done in Spain and Iceland. Orzabal also played and performed backing vocals on the album. Other collaborators included Eg White, Jóhann Jóhannsson, Siggi Baldursson and Mark Abis. The title of the album is a variation of the 1985 Gabriel García Márquez novel Love in the Time of Cholera. The song "Telepathy" was originally called "Love in the Time of Science" written by the Icelandic band Dip whom Torrini had previously worked with (Torrini sang on Dip's original version of the song, and Dip members Jóhann Jóhannsson and Sigtryggur Baldursson also appear on this album). The song would later be recorded under its original title by Marc Almond for his 2001 album Stranger Things, which was produced by Jóhannsson. "Dead Things" "Baby Blue" "To Be Free" (UK #44) "Easy" (UK #63) "Unemployed in Summertime" (UK #63) A series of remixes of the songs from Love in the Time of Science were released by FatCat Records, as free 128 kBps mp3s on the site www.e-rmx.com (now discontinued), and as a set of eight 7 inch singles. The singles were titled sequentially, E1 to E8. The songs were remixed by Grain, Process, Mice Parade, V/Vm, Múm, Smith & Ludlow, Stromba, Antenna Farm, Motion, Lucky Kitchen, Team Doyobi, Foehn, Chasm, Immense, Fonn, Di Lacuna and Transient Waves.
```

## Album 285: Chief — Eric Church

- **album_id:** `0bbea5cf-4a7a-4883-b4a9-6d31c196079f`
- **Tags (identification only):** country, contemporary country, neo traditionalist country, pop/rock
- **Chunks:** 2 (413 words)

### Album 285, chunk 1

```text
Chief is the third studio album by American country music artist Eric Church. It was released on July 26, 2011, via EMI Nashville. The album produced five singles, including Church's first two number one hits on the US Billboard Hot Country Songs chart—"Drink in My Hand" and "Springsteen", as well as the Top 10 hits "Creepin'" and "Like Jesus Does" and the Top 20 "Homeboy". In November 2024, the album was certified four-times Platinum by the RIAA, for having shipped over 4,000,000 records. As of April 2017, the album has sold 1,957,700 copies in the United States. The album received a nomination for Best Country Album at the 54th Grammy Awards and won Album of the Year at the CMA Awards and ACM Awards. In 2020, the album was ranked at 419 on Rolling Stone's 500 Greatest Albums of All Time list. Upon its release, Chief received generally positive reviews from most music critics. At Metacritic, which assigns a normalized rating out of 100 to reviews from mainstream critics, the album received an average score of 77, based on 9 reviews, which indicates "generally favorable reviews". AllMusic reviewer Thom Jurek gave it 5 stars out of 5, saying that it is "defiant, well-conceived, and more carefully executed than it sounds, with some excellent songs". In a review for Slant Magazine, critic Jonathan Keefe stated that "It just doesn't make a hell of a lot of sense to champion traditional country music while singing over hard-rock arrangements and occasionally Auto-Tuned vocal
```

### Album 285, chunk 2

```text
tracks. That's not to say he doesn't do a lot of things, particularly with his songwriting and with some risky production choices, awfully well here. Chief doesn't make him a country music Jesus, but it does back up a good deal of his braggadocio." Rolling Stone placed the album at number 19 on its Best Albums of 2011 list. The album debuted at number one on the US Billboard 200 and the Top Country Albums chart, selling 145,000 copies in its first week of release. In its second week, the album fell to number two on the Billboard 200 while still remaining at number one on the Top Country Albums chart. The album was certified Platinum by the Recording Industry Association of America (RIAA) on June 20, 2012, and triple platinum on August 31, 2016, for combined sales and streams of over three million units in the United States. As of August 2017, the album has sold 1,957,700 copies in the United States.
```

## Album 286: Chuck Person’s Eccojams, Vol. 1 — Chuck Person

- **album_id:** `7b37943b-f2a2-4e27-9748-e53d541d7f68`
- **Tags (identification only):** vaporwave, dolphin on cover, eccojams, animal on cover, electronic, experimental, genre in name, plunderphonics
- **Chunks:** 6 (1424 words)

### Album 286, chunk 1

```text
Chuck Person's Eccojams Vol. 1 is a 2010 album of remixes by American electronic musician Daniel Lopatin under the pseudonym Chuck Person. Its tracks consist of chopped and looped samples of various songs—including popular songs from the 1980s and 1990s—processed with effects such as delay, reverb, and pitch shifting; the results highlight mournful or existential moments from the sources. The album led to the emergence of a style known as "eccojams", which later influenced the internet microgenre vaporwave and came to be regarded as one of its early progenitors. Prior to Eccojams Vol. 1's release, Lopatin posted a series of videos that he called "eccojams" to a YouTube channel named "sunsetcorp". The album was released under the label The Curatorial Club in August 2010 on 100 cassette tapes. By the time an official remastered version was released for digital download in November 2016, recognition for Eccojams Vol. 1 had grown, with the original tapes selling on Discogs at three-digit prices. Prior to the release of Chuck Person's Eccojams Vol. 1, Daniel Lopatin ran the YouTube channel "sunsetcorp", where, beginning in 2009, Lopatin would upload music videos for tracks that he called "eccojams". These were collages of slowed-down looped samples of 1980s and 1990s popular songs—or original pieces of electronic music—and looped video clips taken from YouTube; many of them were initially created at his office job in the free audio editing program GoldWave, between 2004 and 2008. "Nobody Here" combines a looped sample from Chris de Burgh's "The Lady in
```

### Album 286, chunk 2

```text
Red" with a vintage computer-animated graphic called "Rainbow Road". Other examples include Fleetwood Mac's "Only Over You" for "Angel" and Roger Troutman's "Emotions" for "End Of Life Entertainment Scenario #1". Some of these eccojams were initially released as part of the 2009 audiovisual project Memory Vague under Lopatin's alias Oneohtrix Point Never. Eccojams Vol. 1 was an elaboration of that technique. A limited run of 100 cassette tapes was released under the label The Curatorial Club on August 8, 2010. Its artwork incorporates fragments of the cover art for the 1992 video game Ecco the Dolphin such as "a distorted view of a rocky shoreline and a pixelated shark." Lopatin released an official remaster for digital download from his website in November 2016 that was eventually removed. Chuck Person's Eccojams Vol. 1 has been described as plunderphonics, chopped and screwed, eccojams, and vaporwave. The tone has been described as "dystopian", "unnerving, often mournful", "vast and mysterious", and "somber-yet-tropical". The songs consist of looped samples of popular songs from the 1980s and 1990s distorted by effects such as delay, reverb, and pitch shifting, a technique derived from DJ Screw's chopped and screwed technique and likened to a "candy-coloured variation" of William Basinski's The Disintegration Loops. Most of the lyrics isolated in these loops are lyrics which differ from "overall tone and sentiment" of the original songs and often express negative feelings. An example would be "B4", which isolates the lyric "There's nobody here" from "The Lady in Red" to convey existentialism,
```

### Album 286, chunk 3

```text
which differs from the romantic tone of the original song. "A1", which stretches and loops the lyric "Hurry boy, she's waiting there for you" from Toto's "Africa", serves as the introduction. "A2" uses a phaser effect on "Only Over You". "A3" is a pitched-down looped sample of JoJo's "Too Little Too Late", creating "dense, compressed, overdubbed harmonies". "A4" samples a lyric from Michael Jackson's "Morphine" expressing horror at someone taking Demerol. The lyric is warped, creating the impression that the listener is intoxicated, before flanging is applied. "A5", which samples a song by the Byrds, is described by Spectrum Culture as "a creepy little skit so blurred in effects as to be unrecognizable". "A6" is taken from Janet Jackson's "Lonely". "A7" is taken from Aphrodite's Child's "The Four Horsemen", "injecting a bit of apocalyptic dread" from the song's themes and uncertain melody. "A8", after an R&B loop, ends with a crescendo of digital noise, akin to a blizzard. "B1" has a bleak tone, similar to a twisted dream, before transitioning to an uplifting loop of Kate Bush's voice from "Don't Give Up". "B2" is a "drunken, off-key" and slowed-down loop of "Gypsy". "B5" samples 2Pac's "Me Against the World". The final song, "B7", is a loop of "Woman in Chains" by Tears for Fears, that has a shimmering effect "approaching and receding", eventually "overtak[ing] the words" before the song fades out. Though Chuck Person's Eccojams Vol. 1 was released "with little fanfare", the videos Lopatin posted on YouTube became popular,
```

### Album 286, chunk 4

```text
with "Nobody Here" amassing 30,000 views over several months. Music critic Simon Reynolds highlighted the videos' "conceptual framework" as "relat[ing] to cultural memory and the buried utopianism within capitalist commodities, especially those related to consumer technology in the computing and audio/video entertainment area". Anthony Fantano mentioned Eccojams Vol. 1 in his 2012 review of Macintosh Plus's Floral Shoppe, saying he found Eccojams Vol. 1 to be "more bold with its editing and its looping and its stretching" of music samples than Floral Shoppe. According to Tiny Mix Tapes, Eccojams Vol. 1 would lead to Lopatin's 2011 Oneohtrix Point Never album Replica. In 2012, Lopatin released a box set of four 7-inch singles titled Chuck Persons A.D.D., consisting of 30 eccojams. Each disc is designed to have grooves that would make them play infinitely. On the 2015 Oneohtrix Point Never album Garden of Delete, the song "EccojamC1" was included as a tribute to Eccojams Vol. 1. In a 2013 Reddit Ask Me Anything (AMA), when inquired about a follow-up album to Eccojams Vol. 1, Lopatin revealed that he had many eccojams in a "cryotank set to defrost in the distant future." Retrospectively, Eccojams Vol. 1 is widely considered influential in vaporwave, a music genre characterized by slowed-down samples from 1980s and 1990s music. Released before vaporwave's 2012 rise in popularity, the album would serve as a template for artists such as Vektroid and Mediafired to produce what would become vaporwave music. According to Stereogum's Miles Bowe, vaporwave artists "mash the chopped
```

### Album 286, chunk 5

```text
and screwed plunderphonics of Dan Lopatin ... with the nihilistic easy-listening of James Ferraro's Muzak-hellscapes on Far Side Virtual". In 2013, the music blog Girls Blood described Eccojams Vol. 1, along with Far Side Virtual and Skeleton's Holograms, as "Proto Vaporwave" in a post about "Vaporwave Essentials". Regarding the influx of vaporwave producers that came after Eccojams Vol. 1, Lopatin said in a 2017 AMA: Well—the entire point of Eccojams was that it was a DIY practice that didn't involve any specialized music tech knowledge and for me it was a direct way of dealing with audio in a mutable, philosophical way that had very little to do with music and everything to do with feelings and I'm happy to see that it actually turned out to be true, that people make the stuff and find connection and meaning through that practice is all I could ever hope for. It's folk music now. Originally "relatively unacknowledged", by the time of the 2016 re-release, original copies of Eccojams Vol. 1 were highly valued, selling on Discogs for a median cost of US$250 and as high as $400. Kirk Bowman of Sputnikmusic rated Eccojams Vol. 1 highly for its poignancy and found it to be a rare example of a repetitive album that he wanted to listen to repeatedly. Spectrum Culture lauded the album for "feel[ing] so vast and mysterious". Marvin Lin of Tiny Mix Tapes described the album as "plundering the depths of pop music and uncovering short musical segments or
```

### Album 286, chunk 6

```text
particularly existential lyrical moments" to create "a simple yet wholly ecstatic listening experience". Fact listed "A3" as among the best songs by Lopatin, Fantano ranked Eccojams Vol. 1 at number 153 on his list of best albums of the 2010s, and Tiny Mix Tapes named Eccojams Vol. 1 the top album of the 2010s; Pat Beane said that was because, "we at Tiny Mix Tapes couldn't get enough of music. And Eccojams, of music, begat more music". In 2020, the 33⅓ series published a book of essays on underrated albums titled The 331⁄3 B-Sides, which included a Lin piece on Eccojams Vol. 1. In 2025, Pitchfork reviewed the album stating, "[Lopatin] was at the vanguard of the American noise scene in the hazy years when it retreated from feedback-soaked harshness into an unkanny kosmische. Alongside artists like Emeralds, Yellow Swans, Skaters, and Carlos Giffoni, noise music was starting to sound less like The Texas Chain Saw Massacre and more like Tarkovsky's Stalker—and Lopatin was quietly training to become the house DJ for the 'Zone'."
```

## Album 287: Mayday Parade — Mayday Parade

- **album_id:** `408f7c2a-9bfb-4967-8ad0-6ed769645a74`
- **Tags (identification only):** alternative rock, pop punk, alt rock, emo, emo pop, pop, rock
- **Chunks:** 5 (1252 words)

### Album 287, chunk 1

```text
Mayday Parade is the third studio album by American rock band Mayday Parade. It was released by Fearless on October 4, 2011. It was also released through Independent Label Group, after the band departed Atlantic Records. Produced by Zack Odom and Kenneth Mount, the album sees the band writing all the material again, compared to their previous album Anywhere but Here (2009). The album debuted at number 12 on the U.S. Billboard 200, selling near to 27,000 copies in its first week, becoming the band's second highest charted album to date. It also reached number four on the US Top Alternative Albums and number five on the US Top Rock Albums charts. In March 2009, it was announced Mayday Parade had signed to Atlantic. While working on their major label debut, Anywhere but Here (2009), Atlantic expected the band to make a pop album. While the band attempted to follow this direction, they were weighed down by "so much overbearing pressure", according to guitarist Brooks Betts. Vocalist Derek Sanders later recalled that "there was a lot of outside influence" from Atlantic that resulted in "a lot of co-writes". In retrospect, Sanders said the band simply recorded songs that they "didn't care about as much or love as much". Brooks pointed out that it wasn't "the best representation [of the band]." The album was written by the band during early 2011, at a beach house in Panacea, Florida. For this album, the band wrote all of the material. "Stay" is about
```

### Album 287, chunk 2

```text
pain experienced when losing a loved one. The album was recorded over the course of two months, they began recording with Zack Odom and Kenneth Mount in February, and the record was reportedly completed "[the band's] way," not "someone else's way," on April 18. Recording took place at Vinatage Song Studio in Alpharetta, Georgia and at Tree Sound Studios in Norcross, Georgia. Sanders said the band "pushed themselves outside of their typical boundaries," creatively expanding on the instrumentals. The group brought in a string section for certain tracks. He also spoke about doing the process their way, stating, "I think we've found the perfect formula for how to do it. We'll probably do the same thing in the future — it'll be us in a beach house in Florida for about a month and write most of the album there [...] getting away from everything and having no distractions." The album's artwork was created by Jerrod Landon Porter and the CD booklet features an eight panel comic book. On July 6, 2011, Mayday Parade was announced for release and the track listing was revealed. In July and August, the band supported All Time Low on their North America tour. "Oh Well, Oh Well" was made available for streaming via Alternative Press on July 27. On July 31, the artwork was revealed. "Oh Well, Oh Well" was released as a single on August 1. On September 8, "When You See My Friends" was made available for streaming via MTV, and was
```

### Album 287, chunk 3

```text
released as a single a day later. Short clips of every song on the album were made available for steaming on September 22. On October 3, Mayday Parade was made available for streaming, and was released a day later through ILG. On October 7, a music video was released for "Oh Well, Oh Well", which was directed by Thunder Down Country. In October and November, the band went on The Noise Tour with support from We Are the in Crowd, There for Tomorrow, You Me at Six, The Make and Sparks the Rescue. In January 2012, the band filmed a music video for "Stay" in Ohio. In February and March, the band went on a co-headlining tour with We the Kings, with support from The Downtown Fiction and Anarbor. The band supported You Me at Six on their tour of the UK in March and April. On April 4, the "Stay" music video was released, which was directed by Thunder Down Country. On April 12, the band released an acoustic version of "When You See My Friends" as a free download. The band went on the 2012 edition of Warped Tour. In early June, the band toured Japan on the 2012 edition of the Beyond [The] Blue tour. In September, the group performed at the Bazooka Rocks Festival in the Philippines, along with The Maine, Forever the Sickest Kids, The Pretty Reckless, A Skylit Drive and Marianas Trench. The band went on co-headlining tour with The Maine, with support from
```

### Album 287, chunk 4

```text
The Postelles, in October and November. In December, the band went on a short Australian tour with We Are the in Crowd and Heroes for Hire. On December 4, the band released a live music video for "When You See My Friends". 'Mayday Parade was met with positive reviews from music critics. Many critics praised the songwriting on the album, which had been written by the band, compared to Anywhere but Here, their previous album. Jason Lymangrover of AllMusic said, "The most notable change is that the songs on their third outing were written solely by the band. However, with the same production team behind their sound, the same bouncy four-chord blueprint, and the same prevalence for soft verses vs. loud choruses, the changes behind the curtain are barely noticeable." Alternative Addiction wrote, "Mayday Parade going independent allowed them to be able to write all of their own material again. That's something that fits best with what they do. Because of this, the songs sound more appropriate to what the band does well. It doesn't feel like they're trying to do something they're not capable of." Pär Winberg of Melodic felt that it was their "best album to date," stating, "you can't be anything else than impressed by the band who penned all the tracks themselves." Writing for Sputnikmusic, Davey Boy stated, "While the choruses here are all made for being easily recited en masse, they are strangely not as instantly infectious as some of the band's past work. Promisingly,
```

### Album 287, chunk 5

```text
this is more a sign of improved song-craft which gives this album greater replay value than its predecessor Anywhere But Here." A staff writer from The Music remarked, "With their third full length, Mayday Parade has definitely returned to form. They have left behind all the big technical production elements that hindered their last release and have taken it back to basics, showing fans what they do best by creating a solid pop rock album full of massive hooks played out through back and forth dual vocals and upbeat instrument lines." The album was ranked at number 4 on PopMatters' best pop punk releases of 2011 list. Reflecting on the album, Derek Sanders described it as "a big turning point for the band." With the first two albums, he said the band "hadn't planted our roots yet," though by the third album, "we knew exactly what we wanted and who we were as a band. Everything fell into place; it was the right time, the right songs and when I think back over all our records, it's the one that really stands out for me." Mayday Parade was projected to sell 25,000 copies, it eventually sold near to 27,000 copies in the first week, an increase of 30% over their previous album's first week sales. The album debuted at number 12 on the Billboard 200. "Stay" charted at number 26 on the Rock Digital Songs chart in the U.S. The album has sold over 100,000 copies in the US as of 2014.
```

## Album 288: Bone Against Steel — 38 Special

- **album_id:** `71789053-fe42-466c-b912-2f62dca4e79d`
- **Tags (identification only):** southern rock, album rock, aor, pop rock, pop/rock, rock, soft rock
- **Chunks:** 2 (355 words)

### Album 288, chunk 1

```text
Bone Against Steel is the ninth studio album by the southern rock band 38 Special, released in 1991. It was their last album until their 1997 comeback and the last album to feature the vocalist and keyboard player Max Carl. It would also be their last album with long time guitarist and founding member Jeff Carlisi and drummer Jack Grondin. The album itself was a modest commercial success and only reached #170 on the Billboard 200 album chart. However, the single "The Sound of Your Voice" (also known as "Sound of Your Voice"), was a major hit, and one of three songs co-written by Survivor's Jim Peterik for the album. The song reached #2 on the Billboard Mainstream Rock chart and #33 on the Billboard Hot 100 (their last Top 40 hit and last appearance on that chart to date), while the second of the three Peterik songs, "Rebel to Rebel", only reached #30 on the Billboard Mainstream Rock chart. Max Carl – keyboards, lead vocals (1, 2, 4, 6, 7, 9, 11, 13) backing vocals Jeff Carlisi – guitars Danny Chauncey – guitars Larry Junstrom – bass Jack Grondin – drums Donnie Van Zant – lead vocals (3, 5, 8, 10, 12), backing vocals Scott Meeder – drum programming, percussion, cymbals Michael Hoskin – alto saxophone, baritone saxophone Larry Jackson – tenor saxophone Gordon Vernick – trumpet The Six Groomers (the band) – backing vocals Robert White Johnson – backing vocals Jack Blades – backing vocals (9) Brian Howe
```

### Album 288, chunk 2

```text
– backing vocals (9) Rodney Mills – producer, recording, mixing Tag George – recording assistant, mix assistant Edd Miller – recording assistant Phil Tan – recording assistant Bob Ludwig – mastering Masterdisk (New York City, New York) – mastering location Mark Rogers – tape operation Norman Moore – art direction, design John Halpern – band photography Peter Miller – cover photography In a review of Bone Against Steel, Alex Henderson of AllMusic regarded "The Sound of Your Voice" as one of the "Tame, run-of-the-mill corporate rock tunes" which he commented "sound like third-rate Journey, and don't hold a candle to some of Special's earlier efforts."
```

## Album 289: Black Classical Music — Yussef Dayes

- **album_id:** `1f77d7b5-dde6-413f-8640-d42c909f0d25`
- **Tags (identification only):** jazz, 1–4 wochen, afrobeats, contemporary jazz, dancehall, english, offizielle charts, ph 3 stars
- **Chunks:** 1 (253 words)

### Album 289, chunk 1

```text
Black Classical Music is the debut solo album by English drummer and record producer Yussef Dayes. It was released on 8 September 2023 through Brownswood Recordings and Nonesuch Records. It includes guest appearances from Shabaka Hutchings, Tom Misch, Chronixx, Masego, Jahaan Sweet and Leon Thomas, among others, and a posthumous appearance from Barbara Hicks. The album received acclaim from critics. Black Classical Music received a score of 86 out of 100 on review aggregator Metacritic based on five critics' reviews, indicating "universal acclaim". Thom Jurek of AllMusic described the album as "sprawling" and "a culmination of his aesthetic travels, and points squarely at his goal: a seamless musical whole", concluding that the "music is lush, advanced, and welcoming, and comes off without a trace of bloat or conceit. This is easily a top pick for best albums of 2023". Uncut called it "an expansive, soulful set that embraces modern West Coast fusion, Hancock-style funk, psychedelic soul-jazz and more". John Garratt of PopMatters wrote that Dayes "takes the listener on a highly groovy and ultimately fulfilling ride through the peaks and valleys inside of [his] musical brain". Clash's Robin Murray concluded that "taken as a whole, however, Black Classical Music is a unique experience, a true journey, the musical autobiography of a musician central to the ongoing development of UK jazz". A staff review at Sputnikmusic remarked that the album is "packed with so many details and flourishes that AI won't be able to generate anything of its ilk until quantum computing develops itself".
```

## Album 290: Stay on These Roads — a‐ha

- **album_id:** `424d2e98-273c-4590-804c-2ad243e9a282`
- **Tags (identification only):** pop, pop/rock, synth pop, electronic, new wave, pop rock, punk/new wave, rock
- **Chunks:** 2 (368 words)

### Album 290, chunk 1

```text
Stay on These Roads is the third studio album by Norwegian synth-pop band a-ha, released on 3 May 1988 by Warner Bros. Records. Six singles were released from the album. A Synclavier, Sequential Circuits Prophet 5, Yamaha DX-7, Roland D-50, and Roland Juno-60 or Roland Juno-106 synthesizers were used in the recording of this album, as was a Yamaha RX-5 drum machine. The album peaked at number 148 on the US Billboard 200. It was another big hit by A-ha internationally, selling over 4 million copies worldwide. Stay on These Roads achieved Platinum status in Brazil and Gold in the UK, Switzerland, the Netherlands and Germany and Double Platinum status in France. It reached number two in the European top-100 albums sales chart. William Ruhlmann of AllMusic said "in the U.K., the album became the group's third straight to peak at number two, though it charted for a shorter period than the first two albums, and there were four Top 25 hits—the title track, 'The Blood That Moves the Body,' 'Touchy!,' and 'You Are the One'." Also included was a re-recording of A-ha's 1987 theme from the James Bond movie The Living Daylights, which, in its single version, was a U.K. number five that missed the U.S. charts. In the positive review of the NME, David Quantick writes : "Life is sad and so is Pal Waaktaar. Pal, writer or co-writer of all these songs, seems over-run by melancholy. His lyrics are about crying, going away and yearning, and even
```

### Album 290, chunk 2

```text
the happier songs seem riddled with resignation rather than out-and-out pop joy". Lead single "Stay on These Roads", number one in Norway, was a hit across Europe, including top-five showings in the UK, France, Austria and Ireland and top-ten chartings in Germany, the Netherlands, Sweden and Switzerland. Stay on These Roads includes three more hit singles, "The Blood That Moves The Body", "Touchy!" and "You Are the One", though a final single, "There's Never a Forever Thing", was released only in Brazil. Morten Harket – lead and backing vocals Magne Furuholmen – keyboards, bass and drum programming, backing vocals Paul Waaktaar – guitars, strings, bass and drum programming, backing vocals Alan Tarney – producer John Hudson – mixing
```

## Album 291: AmeriKKKa’s Most Wanted — Ice Cube

- **album_id:** `ba8e34c6-47cd-4bf9-9aa0-21da5c50bae4`
- **Tags (identification only):** hip hop, gangsta rap, hardcore hip hop, west coast hip hop
- **Chunks:** 6 (1447 words)

### Album 291, chunk 1

```text
AmeriKKKa's Most Wanted is the debut studio album by American rapper Ice Cube, released on May 16, 1990, by Priority Records. It was his first solo album, after an acrimonious split from his former group N.W.A. Primarily produced by Public Enemy's production team the Bomb Squad, the album was a commercial success, peaking at 19 on the Billboard 200, and was certified platinum in the United States on June 23, 1990. It received widespread acclaim upon its release, and is regarded as a hip hop classic and one of the best albums of the 1990s. After departing from Ruthless Records and the West Coast–based group N.W.A, Ice Cube immediately moved to record his own album. Cube maintains that originally, he and N.W.A producer Dr. Dre still wanted to collaborate for Cube's debut solo, but the move was nixed by label powers: When I went solo, I wanted Dr. Dre to do AmeriKKKa's Most Wanted, but Jerry Heller vetoed that...and I'm pretty sure Eazy didn't want Dre to do it. But Dre did want to do it; we gotta put that on record. Dre wanted to do my record, but it was just too crazy with the break-up [of N.W.A]. Linking up with Sir Jinx, Dr. Dre's cousin, Cube made use of pre-written notebooks of songs meant for N.W.A member/Ruthless co-founder Eazy-E. After relocating to New York, they worked on the songs, which included "Once Upon a Time in the Projects", "Get Off My Dick & Tell Yo' Bitch to Come
```

### Album 291, chunk 2

```text
Here" and "Gangsta's Fairytale", among others. Ice Cube also recorded the song "Jackin' for Beats", using beats allegedly planned for use on the next N.W.A album, though he would use this several months later on the Kill at Will EP. After contacting Public Enemy's production team the Bomb Squad, they completed the album. The album received a fair share of production credited to various Bomb Squad members, with an appearance by Public Enemy frontman Chuck D, despite Jinx's claims that the only Bomb Squad member fully present was Eric Sadler. Hank Shocklee spoke on meeting and working with Ice Cube in a Cool'eh Magazine interview: Cube contacted me wanting to know if we could do a few tracks for his solo album after the whole NWA thing came to what it was and I was like, I'll do it if I can do the whole album. And he said, that's what I was hoping you would say…y'know…and when we were in the studio he showed up with notebooks and notebooks full of new rhymes, a bag full of rhymebooks. With socio-political conscious and gangsta rap content, its songs delve into the issues of ghetto life, drug addiction, racism and poverty. Throughout the album, Ice Cube incessantly attacks institutional racism, as well as social norms which directly or indirectly allowed the oppression of those living in the ghettos of Los Angeles to continue. On "Endangered Species (Tales from the Darkside)", he predicts that his neighborhood would become a flash point for
```

### Album 291, chunk 3

```text
violence before 1992's scandal over the beating of Rodney King, and takes police to task for the policies that would later lead to the L.A. riots that resulted. Throughout the album, Cube takes some controversial stands, referring to certain types of African-Americans as "Oreo cookies", an epithet implying that they appear black on the outside, but have, internally, negative white tendencies. Arsenio Hall is specifically mentioned as being a "sell-out". Cube also heavily criticizes R&B and hip hop radio stations for watered-down broadcasting. The title song directly parodies the television show America's Most Wanted, alleging bias and denouncing the glee the program displays in arresting African-American men. A later skit, "The Drive By", returns to the same theme at the end, with newscaster Tom Brokaw reporting on rioting, stating: "Outside the south central area, few cared about the violence because it didn't affect them." He also addressed gender relations on "It's a Man's World", a duet between Cube and rapper Yo-Yo. Cube and Yo-Yo verbally spar and trade sexist barbs back and forth in an exposé of sexism between men and women. Amidst critics' accusing Ice Cube of sexism, Peter Watrous of The New York Times wrote, in review of a live show at New York's Apollo Theater: ...no one came out ahead; any new sense of cultural violence or sexism promoted by the record had dissolved into a traditional battle of the sexes, no better or no worse. AmeriKKKa's Most Wanted initially charted without the support of a lead
```

### Album 291, chunk 4

```text
single or video, although the title track would later receive a pressing, and a rare video for "Who's the Mack?" eventually surfaced. It was directed by Alex Winter. The title track was the first official single from the album - the B-side for the song was "Once Upon a Time in the Projects". "Who's the Mack?" was released as a promo single and music video. A remix of the album track "Endangered Species (Tales From The Darkside)" was later released as a single the EP Kill at Will. In The Washington Post, David Mills wrote that with the album, "Ice Cube has now proven that he was N.W.A.'s crucial element. He's an unusually gifted rhymer ... And his delivery is even more self-assured than it was when he dissed every cop in the nation." The Source commented that Ice Cube's performances are given "the perfect backdrop" by the Bomb Squad, who the magazine said had "really outdone" themselves by integrating "funky pimp type grooves" into their "metallic bum-rush style of beats". Steven Wells of NME felt that while Ice Cube's "political awareness and eloquence" are undermined by his "cock-waving machismo", the latter is somewhat tempered by his "self-deprecating sense of humour", with Wells ultimately calling the album "alternately appalling, refreshing, confused and dynamic". Writing for Entertainment Weekly, Greg Sandow viewed AmeriKKKa's Most Wanted as "an important social document, but not necessarily cohesive art", nonetheless acknowledging that "Ice Cube emerges as a rapper most original for his uncompromising tone." While deeming
```

### Album 291, chunk 5

```text
the album musically "as original as A Tribe Called Quest, and probably doper", The Village Voice's Robert Christgau found Ice Cube's lyrics generally distasteful "despite his gift for rhyme and narrative". Rolling Stone critic Alan Light declared the album "a disappointment" and said that "the relentless profanity grows wearisome, the Bomb Squad beats lose steam, and Cube's attitudes toward women are simply despicable." Over the years, the album has received further critical praise, with many regarding it as a hip-hop classic. In a retrospective review, David Jeffries from AllMusic called AmeriKKKa's Most Wanted "a timeless, riveting exercise in anger, honesty, and the sociopolitical possibilities of hip-hop" showing Ice Cube "at his most inspired", crediting the album with helping to "boost the role of the individual in hip-hop." In the 2004 Rolling Stone Album Guide, Peter Relic praised it as "an album of menacing, unflinchingly fierce rhymes that took millions of listeners deep into the terrors of South Central L.A." Alan Light reappraised the album in the liner notes of its 2003 reissue, noting its "musical sophistication, brutal imagery, and relentless intensity" and deeming it "one of the most loved, hated, and pivotal albums in the history of hip-hop." Pitchfork's Eric Harvey called it a "groundbreaking" record that ushered hip hop into "the tabloid decade", concluding that "it was AmeriKKKa as much as Nation of Millions and Straight Outta Compton that laid the groundwork for hip-hop's brief and dramatic evolution into an expansive truth-telling media spectacle." (*) signifies unordered lists Ice
```

### Album 291, chunk 6

```text
Cube's social and political commentary, delivered in an incisive manner, has influenced numerous rappers since AmeriKKKa's Most Wanted, particularly in the gangsta rap and political rap subgenres. Focusing on the hardships of life in South Central, Los Angeles, as well as criticizing the American Justice System and race relations in the United States, Cube became an outspoken voice of U.S. injustice against young Black Americans. Many notable rappers have been influenced by AmeriKKKa's Most Wanted. His style of rapping about real life sentiment and socio-political awareness influenced the music of West Coast rappers, including that of Tupac Shakur, Ras Kass, and Xzibit, as well as East Coast rappers Nas, The Notorious B.I.G., and more recently, Saigon, JPEGMafia and Southern rapper Young Jeezy. East Coast rapper Redman also covered "Once Upon a Time in the Projects" on his album Doc's Da Name 2000, with the song "Jersey Yo!". AmeriKKKas Most Wanted debuted at number 19 on the US Billboard 200 chart. It was certified gold by the Recording Industry Association of America (RIAA) two weeks after it was released for sales of over 500,000 copies. The album was eventually certified platinum four months later on September 16, 1990.
```

## Album 292: Sun City — Artists United Against Apartheid

- **album_id:** `dba6eb1b-2559-40da-8cb2-bb7c3dfd2de1`
- **Tags (identification only):** pop rock, blues, blues rock, contemporary jazz, electro, electronic, hip hop, jazz
- **Chunks:** 5 (1157 words)

### Album 292, chunk 1

```text
Sun City is the only studio album by Artists United Against Apartheid, released on October 25, 1985, by EMI Manhattan Records. The Little Steven–led project features contributions from more than 50 artists from the rock, hip hop, soul, funk, jazz, reggae, Latin, and world music genres. The album contains two versions of the "Sun City" protest song against apartheid in South Africa as well as other selections in the same vein from that project. Initially intending to record the song "Sun City" for his third solo album Freedom – No Compromise, Little Steven (real name Steven Van Zandt) instead approached producer Arthur Baker to help record a "We Are the World"-inspired anti-apartheid protest single. In the song, Van Zandt urges artists to boycott the Sun City resort in South Africa, where artists such as Queen, Elton John, Linda Ronstadt and Rod Stewart have accepted invitations to perform. Van Zandt's mission was to raise awareness of the racial segregation enforced by the white government in South Africa, and to encourage the cultural boycott the United Nations had imposed in the early 1980s. "I had been doing research on American foreign policies," Van Zandt said, "and South Africa was on my list of engagements we were involved with, which I felt our government was on the wrong side of. By then, I had heard Peter Gabriel's "Biko," which was just a terrific inspiration." With assistance from ABC News journalist Danny Schechter, Van Zandt and Baker assembled a wide variety of artists from
```

### Album 292, chunk 2

```text
Bruce Springsteen, Bob Dylan and Lou Reed to Gil Scott-Heron, Miles Davis and Africa Bambaataa. Rock critic Dave Marsh called it "the most diverse line up of popular musicians ever assembled for a single session." However, the recordings quickly became an album-length project of its own, and the Sun City album was recorded in summer 1985 at 15 different recording studios in New York, Los Angeles, Boston, Dublin and London. In addition to the title track, other songs were recorded at the time to complete an album's worth of material. Drummer-musician Keith LeBlanc and Danny Schechter came up with "Revolutionary Situation", an audio-collage set to music that took its title from the words of South Africa's then-interior minister Louis Nel condemning the state of the country. Amid a background of yapping police dogs, sounds of mayhem and revolt in the township, LeBlanc and Schechter mixed in angry declarations by activists like Alan Boesak, Bishop Archbishop Desmond Tutu and Nelson Mandela's daughter Zindzi, looped with what was at that time the most recent interview with her father, recorded in 1961. "No More Apartheid" is an improvisational piece featuring Peter Gabriel and Indian violinist L. Shankar. "Peter Gabriel came in and just started chanting. Weird African chant, out of nowhere ... Then he started harmonizing with himself," Van Zandt recalled. Drummer Keith LeBlanc then added drums to the chant, and Van Zandt put down guitar and synthesizer parts. Inspired by meetings with other artists who volunteered, Bono of U2 went back to
```

### Album 292, chunk 3

```text
his hotel room and wrote "Silver and Gold" the same evening. The song was quickly recorded, with guitarists Keith Richards and Ron Wood of the Rolling Stones, and drummer Steve Jordan. Wood's guitar work is notable for using Keith's switchblade as a slide. "Silver and Gold" was also distributed separately as a promotional single. A last-minute inclusion, the song was left off the track listings of the original 1985 album and cassette pressings and considered to be a hidden track. Bono later explained, in an appearance on the US syndicated radio show "Rockline" with Bob Coburn, that he submitted the tape of the song after the album's artwork had been printed by EMI Manhattan Records. When Razor and Tie reissued the album in 1993, the song was included on the track listings. U2 also recorded two versions of the song: a live version in the Rattle and Hum film and album, and a studio version on the B-side of "Where the Streets Have No Name". "The scariest encounter of the Sun City project had to be Miles Davis," recalled Van Zandt. "I wrote the intro for him to play… He's just not friendly. He makes Lou Reed look like a pussycat… He came in, sat down and I played him the "Silver and Gold" tape. He's sitting next to me, and he talks real low and slow, and right in my ear: "Hey man, do you want me to fucking play or what?" So he does his take, and I
```

### Album 292, chunk 4

```text
asked him to redo it with the mute on. I went and reassembled his old quintet with Herbie Hancock, Ron Carter on bass and Tony Williams on drums." "Let Me See Your I.D." – based on a line from Gil Scott-Heron's "Johannesburg" – features vocal contributions from Scott-Heron and various rappers and singers. All were told to feel free to express their feelings about the subject any way they wanted lyrically. Then audio from news footage, excerpts from Nelson Mandela's speeches, and sound effects were added, and turned into an anti-apartheid montage. Music critic Robert Christgau felt that each side of the album closes with "a well-meaning failure", writing that "Revolutionary Situation"'s "collage of indistinct South African voices over Keith LeBlanc humdrum is an object lesson in political correctness that might have made a collectible B, and Bono's country blues is simply ignorant." He added that Gil Scott-Heron's "superrap" on "Let Me See Your I.D." "is as astute and moving rhythmically as it is ideologically," and that "No More Apartheid" is a "worthy successor" to Peter Gabriel's "Biko." Christgau also highlighted the two versions of the title track, which he felt "can grow on you in a big way." AllMusic's Stephen Thomas Erlewine wrote retrospectively that the album is "extremely listenable," saying, "it's one of the few charity or protest albums that stands up to repeated listenings, thanks to the extended instrumental workouts." Unlike Robert Christgau, Erlewine felt that "Silver and Gold" was "the finest moment" on the album. Trouser
```

### Album 292, chunk 5

```text
Press called the album "a powerful record given weight by the cause and the challenge." Sun City was a modest success, reaching #31 on the Billboard 200 pop albums chart. It did much better in terms of critical reaction, placing at #5 on the Pazz & Jop Critics Poll for albums for that year. Sun City got the final spot on Rolling Stone's list of the best 100 albums of the 1980s in 1989 and 2016. The album was issued on CD by Razor & Tie in 1993 – but, after the end of apartheid in 1994, eventually went out of print. In 2019, the album was remastered for release as part of Van Zandt's career-spanning box set Rock N Roll Rebel: The Early Work. The digital deluxe edition of the album was released on December 6, 2019, containing four bonus tracks. The digital deluxe edition also includes the reissued Let Me See Your I.D. bonus EP.
```

## Album 293: Songs of Faith and Devotion: Live — Depeche Mode

- **album_id:** `8c1cca16-430c-4936-8fb6-20110bbcaae3`
- **Tags (identification only):** alternative pop/rock, alternative dance, dance rock, electronic, pop, pop/rock, rock, synth pop
- **Chunks:** 4 (898 words)

### Album 293, chunk 1

```text
Songs of Faith and Devotion Live is the second live album by the English electronic music band Depeche Mode, released on 6 December 1993 by Mute Records in the UK. Recorded during the band's 1993 Devotional Tour, the album consists mainly of performances recorded in Liévin, France, with tracks recorded in Copenhagen, Milan and New Orleans. It was a track-by-track live duplication of Depeche Mode's eighth studio album, Songs of Faith and Devotion, which was released earlier in 1993. The album was poorly received by critics and performed moderately on the charts, reaching number 46 on the UK Albums Chart and number 193 on the US Billboard 200. A near-complete concert of the Devotional Tour was released on the Devotional video album in 1993, which attained more commercial success. Depeche Mode had recorded Songs of Faith and Devotion in 1992, released in 1993. To support the album, the band embarked on the Devotional Tour, originally planned only to run through the end of 1993 but extended into mid-1994. The album was recorded during the European leg of the 1993 Devotional Tour, with recordings taken from three shows: 27 May 1993 in Copenhagen, 4 June 1993 in Milan, and 27 July 1993 in Liévin. However, none of the performances of "One Caress" using live musicians were satisfactory according to band member Alan Wilder, who said, "We couldn't find a decent version of 'One Caress' using the various 'real' string quartets, which accounts for the sampled one [on the album]. Most of
```

### Album 293, chunk 2

```text
the hired musicians played astonishingly poorly." The live version of "One Caress" was recorded on 8 October 1993 in New Orleans during the US leg of the tour. Recorded by the band's sound engineer Steve Lyon, Lyon and Wilder went to Windmill Lane Studios in Dublin in August 1993 between legs of the tour to mix the album. Additional, final mixing of the album took place at Studio Guillaume Tell in Paris and Olympic Studios in Paris. The decision was made by Mute Records to have the album mirror the running order of the studio album, in what Wilder called "a deliberate – and some might say cynical – attempt to prolong sales of the studio album of the same name. Having the identical running order meant that it could be given the same catalogue number – hence the elongated chart position. I also think the general consensus was that it was too soon after 101 to do another similar live album, and, anyway, we were putting together [the] Devotional video that would give an ever greater feeling of a [Depeche Mode] live show." Some songs, such as "I Feel You" and "Condemnation" were pitched down a semitone so that lead singer Dave Gahan could sing them more easily. Said Wilder, "The only way to do this successfully was to adjust each sound individually. The tempo remained the same [as the original studio tracks], so any non-musical part didn't need to be changed." Of Gahan's performance on the live album,
```

### Album 293, chunk 3

```text
Wilder said, "There is a degradation in [Gahan's] vocals during some of the live performances from [the] Devotional Tour, but this is partly down to the stresses and strains of extensive touring and perfectly understandable. That said, I would rather hear a cracked and rough sounding voice that is full of emotion [rather than] one that is technically perfect, but bland and lifeless." Songs of Faith and Devotion Live was released on 6 December 1993 by Mute Records in the UK and given catalogue number LSTUMM106, to mirror Songs of Faith and Devotion's catalogue number STUMM106. The album spent a single week on the Billboard charts in the US, and while it did better in the UK, it was at that point the only Depeche Mode album released that failed to crack the UK's top ten album list. As of April 2006, it had sold 114,000 copies in the United States. In 1994, to help promote the tour's swing through Oceania, Liberation Records of Australia released a limited double pack release of the original Songs of Faith and Devotion and Songs of Faith and Devotion Live combined into a single package with a unique sleeve, given catalogue number D93398. In comparison to Songs of Faith and Devotion, Songs and Faith and Devotion Live received less acclaim from music critics; AllMusic rated the album two stars out of five. The A.V. Club rated Songs of Faith and Devotion Live as the "Least Essential Live Album" of the 1990s, saying, "Depeche Mode
```

### Album 293, chunk 4

```text
has plugged in plenty of DAT and drum machines during its live performances, thereby allowing the band to crank out note-perfect versions of its studio hits. Featuring every track on Songs of Faith and Devotion, played live and in order, the album's live counterpart is monumentally unnecessary." In the same feature, the album was listed as one of ten nominees for "Least Essential Album" of the decade with the comment, "It's not like Depeche Mode is inclined to rely on radical instrumental improvisation live." Hildia Campbell – backing vocals Samantha Smith – backing vocals Alan Wilder – production, mixing Steve Lyon – production, mixing, recording Peter Brandt – recording assistance Rob Kirwan – mixing assistance Alex Firla – mixing assistance Jeremy Wheatley – mixing assistance JD Fanger – album coordination Daryl Bamonte – album coordination Pepe Jansz – album coordination Anton Corbijn – visuals, art direction, sleeve design
```

## Album 294: MTV Unplugged: Summer Solstice — a‐ha

- **album_id:** `c0568c54-f551-4eb2-8d23-36a82e19e2d7`
- **Tags (identification only):** pop, electronic, europop, new wave, pop rock, rock, synth pop
- **Chunks:** 1 (99 words)

### Album 294, chunk 1

```text
MTV Unplugged: Summer Solstice is a live album by the Norwegian synth-pop band a-ha, released on 6 October 2017 as part of the MTV Unplugged series. It was recorded live at the Harbour Hall at Ocean Sound Recordings in Giske Municipality, Norway, on 22 and 23 June 2017. The album debuted at number six on the UK Albums Chart with 6,982 units sold in its first week, becoming A-ha's seventh top-10 album in the United Kingdom. Morten Harket – vocals Magne Furuholmen – upright piano, harpsichord, celesta, acoustic guitar, flute, backing vocals Paul Waaktaar-Savoy – acoustic guitar, backing vocals
```

## Album 295: Twilight of the Thunder God — Amon Amarth

- **album_id:** `3e915a72-2d6d-49ee-a0fc-138c837f64b7`
- **Tags (identification only):** melodic death metal, 00s, death metal, viking metal, extreme metal, metal, rock, vyrzukhisuc album
- **Chunks:** 2 (520 words)

### Album 295, chunk 1

```text
Twilight of the Thunder God is the seventh studio album by Swedish melodic death metal band Amon Amarth. Twilight of the Thunder God was released in September 2008. The album's name and title track refer to Thor's slaying of the Midgard Serpent Jörmungandr. In anticipation of this album, there was a series of six vlog-format studio diaries which displayed the recording process of this album in the studio. The first focused on Fredrik Andersson recording the drums. The second vlog focused on Olavi Mikkonen recording the rhythm guitar position. The third vlog focused on Ted Lundström recording bass guitar and band members preparing food. The fourth episode focused on Johan Hegg recording vocals. The fifth video was Johan Söderberg performing and recording guitar solos. The final vlog featured Olavi Mikkonen and Ted Lundström packing up the studio, as well as an album preview. A series of 8-page comics were made during the production of the album, eponymously entitled "Twilight of the Thunder God", released in magazines throughout Europe. On 27 June 2008, the title of this album was announced. Twilight of the Thunder God features several guest appearances featuring Entombed vocalist Lars-Göran Petrov on "Guardians of Asgaard", Children of Bodom and Stone guitarist Roope Latvala who contributes a solo on the track "Twilight of the Thunder God", and Finnish cello metal band Apocalyptica guesting on "Live for the Kill". Approximately a month later on 25 July 2008, the album artwork was revealed, featuring Thor, the Norse God of Thunder, in
```

### Album 295, chunk 2

```text
battle with Jörmungandr. On 27 August 2008, Amon Amarth released the information that they had recently finished work on a video clip for the title track of the album. The video clip was shot in Jomsborg, Poland. The band notes that while they were there, a heavy storm came through the town, resulting in the roughest conditions the band has ever shot a music video in. The album debuted at number 50 on the Billboard 200, and debuted at number 11 on the Swedish album charts. This makes the band's first album to chart on the top 200, and also the band's highest chart debut in their native country of Sweden, debuting 10 places higher than their previous release, With Oden on Our Side. Initial critical response to Twilight of the Thunder God was positive. At Metacritic, which assigns a normalized rating out of 100 to reviews from mainstream critics, the album has received an average score of 80, based on 5 reviews. The album was ranked number six on Metal Hammer's Top 50 Albums of 2008. Swedish power metal band Sabaton covered "Twilight of the Thunder God" as a bonus track on various renditions of their 2012 album Carolus Rex. In 2013, Corvus Corax released a cover of "Twilight of the Thunder God" on their album Gimlie. In 2017, Swiss metal band Rage of Light released a cover version of "Twilight of the Thunder God". In 2021, Feuerschwanz released a cover of "Twilight of the Thunder God" on the Deluxe Edition of their album Memento Mori. Ronny Milianowicz – horns, brass, choir vocals on “Tattered Banners and Bloody Flags”
```

## Album 296: Kilroy Was Here — Styx

- **album_id:** `9ff043bc-e7de-453f-a801-8112a96b78bf`
- **Tags (identification only):** pop rock, aor, arena rock, hard rock, progressive rock, rock, rock opera, todd in the shadows
- **Chunks:** 4 (801 words)

### Album 296, chunk 1

```text
Kilroy Was Here is the eleventh studio album by the American rock band Styx, released on February 22, 1983. A concept album and rock opera about a world where rock music is outlawed, it is named after a famous World War II graffiti tag, "Kilroy was here". It was the last album of original material to be released by the "classic" lineup of Dennis DeYoung, Tommy Shaw, James "J.Y." Young, John Panozzo, and Chuck Panozzo. The album spawned two hit singles, the synth-pop "Mr. Roboto" which later became one of their signature songs, and the power ballad "Don't Let It End". Both of them were major hits in 1983, peaking at No. 3 and No. 6 respectively, on the US Billboard Hot 100. The album is certified platinum by the RIAA. It is the most recent studio album by the band to be certified platinum. In 2022, Rolling Stone ranked the album #50 on their list of the 50 Greatest Concept Albums of All Time. The band created the album Kilroy Was Here partly to mockingly respond to Christian groups and other anti-rock-music activists who had previously influenced the Arkansas State Senate to pass a bill requiring that all records containing backmasking be labeled as such by the manufacturer. Cited in the legislation were albums by the Beatles, Pink Floyd, Led Zeppelin, Electric Light Orchestra, Queen, and Styx themselves. ELO similarly responded with its own 1983 album Secret Messages. The hard rocker "Heavy Metal Poisoning", the fifth track on the
```

### Album 296, chunk 2

```text
album, begins with the backmasked Latin words "annuit cœptis, novus ordo seclorum". Translated from the Latin, these words mean "[he] has favored our undertakings, a new order of the ages." These are the two mottoes from the Great Seal of the United States on the reverse side of the United States one-dollar bill. The album's somewhat rock-operatic story tells of a future in which a fascist and theocratic government and the "MMM (the Majority for Musical Morality)" have outlawed rock music. The story's protagonist, Robert Orin Charles Kilroy (the initials of which spell out "ROCK", played by DeYoung), is a former rock star who has been imprisoned by MMM leader Dr. Everett Righteous (Young). He escapes using a disguise (according to the album's song "Mr. Roboto") when he becomes aware that a young musician, Jonathan Chance (Shaw), is on a mission to bring rock music back. Vocalist and keyboardist Dennis DeYoung conceived Kilroy Was Here as an album and accompanying stage show, which opened with a short film of the same name. According to the episode of Behind the Music featuring Styx, the early part of the supporting tour was a financial disaster, due to the fact that Styx had booked small, theater-sized venues for a more intimate experience, while later tour dates saw the group performing in large arenas to sold-out crowds. The album debuted at No. 10 on the Billboard 200 in its first week and sold over 1 million copies (although some sources say 2.5 million copies)
```

### Album 296, chunk 3

```text
and peaked at No. 3 on the US charts; however, it broke the streak of multi-platinum albums for Styx, and ushered in a more keyboard-oriented, theatrical direction. In an interview with the Chicago Tribune, James Young talked about the creative differences in the band, and what led to their breakup: "Dennis really wanted to do these soft, intimate love ballads, and that was against the grain for me and Tommy Shaw, so our differences got magnified, because Dennis was insisting on going outside the boundaries we lived with. He's an assertive and strongly opinionated guy." Despite the album's financial and chart success, after the Kilroy tour, the songs were not performed live by Styx (which fired DeYoung in 1999) in subsequent tours (with the exception of segments from "Mr. Roboto" and "Heavy Metal Poisoning" performed in the "Cyclo-medley"), until "Mr. Roboto" reappeared in full in their encore on May 30, 2018, as a cover of the Protomen's cover of the song. DeYoung does perform the songs "Mr. Roboto" and "Don't Let It End" regularly during his solo tours. The James Young Group performed "Heavy Metal Poisoning" and "Double Life" as well on their tour in 1993. Three of the four videos for the album, "Mr. Roboto", "Don't Let It End", and "Heavy Metal Poisoning", were filmed at the same time and used footage from the minifilm. A fourth video, "Haven't We Been Here Before", was filmed a few months after the album was released; it did not interact with the
```

### Album 296, chunk 4

```text
album's story. Dennis DeYoung – vocals, keyboards, accordion James "JY" Young – vocals, guitars, vocoder Tommy Shaw – vocals, guitars, shamisen, vocoder Chuck Panozzo – bass John Panozzo – drums, percussion Steve Eisen – saxophone Dan Barber – horn Mike Halpin – horn Michael Mossman – trumpet Mark Ohlsen – horn
```

## Album 297: Closer to the Truth — Cher

- **album_id:** `2150ce77-206e-449f-a4e9-18206ba26f5a`
- **Tags (identification only):** pop, dance pop, electronic, house, rock
- **Chunks:** 9 (2163 words)

### Album 297, chunk 1

```text
Closer to the Truth is the twenty-fifth studio album by American singer and actress Cher. It was released on September 20, 2013, by Warner Bros. Records. Opting to re-establish her music career, she began planning the project in 2011, shortly after her appearance in the movie Burlesque and the conclusion of her residency show at Caesars Palace. Work continued into 2012 and 2013. While the album was initially planned to be pop rock-oriented, Closer to the Truth ultimately became a prominently dance-inspired record. As executive producer, she enlisted longtime collaborator Mark Taylor to work alongside new producers such as Paul Oakenfold, Billy Mann, Timbaland and MachoPsycho to achieve Cher's desired sound. Described by Cher as "very eclectic" and "her best album ever", Closer to the Truth is primarily a dance-pop record, yet it includes a broader range of various musical genres such as house, synth-pop, EDM, soft rock and country and contains influences by the music of the 1990s. The lyrical themes revolve largely around romance, feminism, individualism and self-empowerment. The album also features additional vocals and songwriting duties from several new partners, including singers Pink and Jake Shears. The album received generally positive reviews from contemporary music critics, and was a success commercially, debuting and peaking at number three on the U.S. Billboard 200 with first-week sales of 63,000 copies, becoming Cher's highest-peaking solo album on that chart. However, with her album Dancing Queen (2018) debuting at number three on the Billboard 200 with sales of 153,000 copies in
```

### Album 297, chunk 2

```text
its first week, that record is now a tie. As of February 2014, Closer to the Truth has sold 285,000 copies in the country according to Nielsen SoundScan. It was certified gold by Music Canada and silver by BPI. It charted within the top ten in Canada, Germany, Russia, Scotland, the UK, and the US as well as moderately throughout several other international territories. "Woman's World" was released as the lead single from Closer to the Truth on June 18, 2013, in the United States and Canada, and peaked at number one on the US Billboard Hot Dance Club Songs. The second single, "I Hope You Find It", was released on October 4, 2013, and charted strongly in several European national record charts. It was followed by singles "Take It Like a Man" and "I Walk Alone", both peaking at number two on the US Billboard Hot Dance Club Songs. Cher promoted Closer to the Truth with several television appearances and performances worldwide. She garnered widespread media attention when declined the invitation to perform at the 2014 Winter Olympics because of Russia's anti-LGBT sentiments. Later, Cher embarked on her sixth concert tour titled the Dressed to Kill Tour on March 22, 2014. On March 30, 2024, it was announced by Dion Singer via Instagram that Closer to the Truth would be re-released on vinyl on June 28, 2024. It was also announced that “Will You Wait for Me” would be included on the digital super deluxe edition of the album.
```

### Album 297, chunk 3

```text
On May 13, 2024, at midnight, the super deluxe edition of Closer to the Truth was unexpectedly released to all streaming services. Cher's last album, 2001's Living Proof, was supported by her record-breaking world tour, which ended in 2005. After a three-year hiatus, she began a Las Vegas residency and it was then that discussions of a new album began. In December 2008, she was said to be planning a record of 1960s covers, but in 2010 instead turned her attention to a movie comeback in Burlesque. For the film, she recorded two songs, "Welcome to Burlesque" and "You Haven't Seen the Last of Me". During promotion for Burlesque, Cher confirmed she was working on a new album in Nashville. The project's genre was described as southern rock and even country. However, after the success of "You Haven't Seen the Last of Me" on the US Hot Dance Club Songs chart (her seventh number one on that chart), the musical direction of the album changed to dance-oriented pop. Cher collaborated with Diane Warren, Timbaland, Mark Taylor (who produced her 1998 hit, "Believe") and Kuk Harrell in putting the album together. In 2011, she recorded Lady Gaga's unreleased song, "The Greatest Thing", which was turned into a duet with Gaga and was produced by RedOne. Originally expected for release in September 2011, the song was eventually dropped from the album. A rough demo of the song was leaked on August 13, 2013. With the release of "Woman's World", Cher announced that
```

### Album 297, chunk 4

```text
the album's working title was Closer to the Truth. The track list includes "Lie to Me" and "I Walk Alone", both written by pop star Pink, and one featuring her vocals; "Take It Like a Man"; and a song written by Cher and Shirley Eikhard called "Lovers Forever". Originally intended for the soundtrack of the 1994 film Interview with the Vampire, it was recorded by Eikhard for her 2005 album Pop, and was produced for Closer to the Truth by Mark Taylor. Cher worked with hip-hop producer Timbaland on "I Don't Have to Sleep to Dream" and covered three songs: "Sirens" by singer-songwriter Nell Bryden, "Dressed to Kill" by Preston and "I Hope You Find It" by Miley Cyrus, from the soundtrack of the 2010 film The Last Song. Three versions of the album were released. The original version of "You Haven’t Seen the Last of Me" from Burlesque is featured on the deluxe edition as a bonus track. Closer to the Truth was also released on white vinyl. This marks her first vinyl album release since 1991's Love Hurts and 1992's Greatest Hits: 1965–1992. According to critics reactions following an exclusive listening party on August 1, 2013, Closer to the Truth is "a healthy mix between punchy, uptempo dance tracks and big, emotional balladry", while the first half is "stacked with dance-floor anthems", and the latter features "mid-tempo songs and slower numbers, where the lyrics and melodies are highlighted". Closer to the Truth was promoted a few times for
```

### Album 297, chunk 5

```text
its North America release of September 24, 2013, and in Europe for its worldwide unveiling a week later. In October 2012, clips from the unannounced lead single leaked online. "Woman's World" was officially made available for online streaming on Thanksgiving 2012 and eventually released on June 18, 2013. Written by Matt Morris, Paul Oakenfold and Anthony Crawford, the single went to no. 1 on the Billboard dance chart. Cher performed it on the season finale of, The Voice; at New York City's gay pride event, Dance on the Pier; and at Macy's 4th of July Fireworks Spectacular. A music video, directed by Ray Kay, was released on August 20, 2013. The second single, "I Hope You Find It", premiered on September 23, 2013, during Cher's Today Show concert, where she also performed "Woman's World" and "Believe". It was further performed on the Late Show with David Letterman on September 24, 2013, on Live! with Kelly and Michael on October 1, 2013, and on German TV show Wetten, dass..? on October 5, 2013. She then continued promotion of the single in the UK, performing on The X Factor on October 13, 2013, on The Graham Norton Show on October 18, 2013, and then on Vivement dimanche! in Paris on November 24, 2013. An official lyric video for the single was released on September 24, 2013. In 2014 "I Hope You Find It" debuted on Billboard's Adult Contemporary chart at number 24, becoming Cher's 31st entry on that chart during the course
```

### Album 297, chunk 6

```text
of five decades. "Take It Like a Man" was released as a digital single with four remixes and an instrumental on November 8, 2013, in Germany and three days later worldwide. Cher garnered media attention with a music video for the 7th Heaven Remix, released on November 20, 2013. It features Andrew Christian underwear models as well as several gay porn stars, such as Antonio Biaggi. A remixes edition with eight further remixes of "Take It Like a Man" was released digitally on January 28, 2014. It peaked at number two on the US Dance Club Songs chart, as well as number nine on the US Hot Dance Singles Sales and number 23 on the US Hot Dance/Electronic Songs chart. "Sirens" was included in the digitally-released album Songs for the Philippines, a fund-raising project for the victims of Typhoon Haiyan in the country. "I Walk Alone" was sent to UK pop radio stations in early 2014. On March 14, 2014, Tracy Young's "Ferosh Reconstruction Remix" of "I Walk Alone" premiered on Billboard's official website, being serviced to dance clubs and DJs the following week. An Extended play featuring nine remixes of "I Walk Alone" was released to digital retailers on April 25, 2014. It peaked at number two on the US Dance Club Songs Chart. The Dressed to Kill Tour in support of Closer to the Truth, which launched on March 22, 2014, in Phoenix, Arizona, was officially announced on September 23, 2013. It is titled after the album's song
```

### Album 297, chunk 7

```text
of the same name. The tour went on to gross over $55 million and attracted over 600,000 fans. Closer to the Truth garnered generally positive reviews from music critics. At Metacritic, which assigns a normalized rating out of 100 to reviews from mainstream critics, the album has an average score of 61 based on six reviews, indicating "generally favorable reviews". At USA Today, Jerry Shriver told that the release was "huge fun, lyrically substantive (as these things go) and emotionally wide-ranging, and it appeals beyond her fan base." Jim Farber of New York Daily News wrote that "The material isn't quite so individual", yet noted that "At root, the new disc pleases by this sole measure: It's deeply, madly Cher." At Newsday, Glenn Gamboa evoked that "Cher doesn't just survive here, she thrives." Kevin Catchpole of PopMatters affirmed that "Cher has provided a welcome return to the music world with Closer to the Truth." Gay Times felt the album was "a fantastic, if long-overdue, return from one of the greatest singers of our time." At So So Gay, Ed Brody highlighted that the release was "anything but a meek return to the spotlight for one of pop's most enduring and resilient emissaries", and proclaimed this was "a fantastically strong renaissance album." Bill Lamb of About.com called it "well balanced with the first half amounting to an uptempo dance suite and the second half explore more ballad territory." However, AllMusic told that the album was "not terrible by any stretch, but
```

### Album 297, chunk 8

```text
the first half of the album is so much fun that this half suffers in comparison. An entire album of disco ball-shattering dance songs may have been too much and worn out its welcome." At The Montreal Gazette, Mark J. LePage felt that the release was "kind of like a miracle, and kind of sad and kind of heroic that it even exists." Slant Magazine's Sal Cinquemani wrote that the album "not only perpetuates this exhausted (and exhausting) formula, but fails to attempt to reinvent it in even the most minute ways." At The Guardian, Caroline Sullivan said that "The first half of the album is a similar campstravganza – Take It Like a Man indeed – but the second peters out into MOR." At The Boston Globe, Michael Andor Brodeur gave a mixed review, when he highlighted that the album was "presumably designed for the drive home from the club, seems to insist she’s more than a remix ingredient or Auto-tune fodder." Philip Matusavage of MusicOMH criticized much of the album as "generic" and "formulaic", describing it as lacking invention while finding some of its later material more effective. In the United States, Closer to the Truth sold 63,000 copies in its first week of release and debuted at number three on the Billboard 200, becoming Cher's highest-charting solo album. However, with her album Dancing Queen (2018) debuting at number three on the Billboard 200 with sales of 153,000 copies, that record is now a tie. It spent three
```

### Album 297, chunk 9

```text
out of its first four weeks on the Billboard 200 within the top ten. As of February 2014 the album has sold over 285,000 copies in the US. In the UK the album debuted at number four, giving Cher her first top-five studio album there since 1991's Love Hurts, with 14,621 copies, and was still in the top ten the next two weeks selling respectively 8,281 and 7,829 copies, ultimately receiving a Silver certification by the BPI for the sales of over 60,000 copies. The album was certified Gold in Canada in November 2013 for the sales of 40,000 copies. As of March 2017 the album has sold 585,000 copies worldwide. The album was nominated for a World Music Award for World's Best Album. During the week of July 7, 2024, Closer To the Truth re-entered the Scottish albums chart at number 97. It also re-entered the physical albums chart at number 92, and debuted at number 34 on the vinyl albums chart.
```

## Album 298: Profound Mysteries III — Röyksopp

- **album_id:** `d917b9ef-dc9f-4ac6-a890-9802b9b466dd`
- **Tags (identification only):** electronic, synth pop, 1–4 wochen, ambient, electro, english, house, offizielle charts
- **Chunks:** 1 (249 words)

### Album 298, chunk 1

```text
Profound Mysteries III is the eighth studio album by Norwegian electronic music duo Röyksopp, and is the third and last album in the Profound Mysteries series of albums. The album was released on 18 November 2022. It was released with collections of short films (each by a different director) and animated visualizations (by artist Jonathan Zawada) created to accompany each track. Profound Mysteries III received generally positive reviews from music critics. At Metacritic, which assigns a normalised rating out of 100 to reviews from mainstream publications, the album received an average score of 71, based on 5 reviews. Thomas Bedenbaugh of Slant Magazine stated that "Röyksopp concludes their Profound Mysteries trilogy with some of their most ambitious songs to date", and further noted that the track "Speed King" is the centerpiece of the album and described that "the song serves as the boldest and most memorable composition in the trilogy." NRK's Shana Fevang Mathai noted that the range of songs might require a "generous ear" to appreciate. Sebas E. Alonso of Jenesaispop praised "the fact that [Röyksopp] offers us something different in this storm of overwhelming news that the music world has become every Friday." Bernt Erik Pedersen of Dagsavisen described the tracks of the album as going "from dramatic heights to quiet introspection, from the low whispering to the grandly symphonic, with both orchestral strings and sweeping synth strings. At the same time, there is light and dewy synthpop [...] with Astrid S on Just Wanted To Know."
```

## Album 299: Velociraptor! — Kasabian

- **album_id:** `7f333b10-b826-45de-b7aa-862787f5cf60`
- **Tags (identification only):** indie rock, rock, alternative rock, alternative dance, brit pop, neo psychedelia, psychedelic rock
- **Chunks:** 3 (719 words)

### Album 299, chunk 1

```text
Velociraptor! is the fourth studio album by English rock band Kasabian, released on 16 September 2011. The album has been described as expanding upon the neo-psychedelic feel of their previous album West Ryder Pauper Lunatic Asylum with a stronger emphasis on experimental song structures and instrumentation. It was released to critical acclaim and became their third UK number-one album. "Switchblade Smiles" was made available as a free download to anybody who pre-ordered the album from the band's official website store from 7 June 2011. The track is also available as a free download on the band's fanpage on Facebook. The album cover is an edited picture of all four band members covered in feathers (as Velociraptors were traditionally feathery) and screaming, edited from the "Switchblade Smiles" music video. Music videos for "Days Are Forgotten", "Re-Wired", "Goodbye Kiss", "Man of Simple Pleasures" and "Neon Noon" were also produced and released through the band's Vevo page on YouTube. The album has been noted for its blend of styles, combining Middle Eastern influences, rock and electronica, with Slant Magazine claiming the album is a "departure from the loutish club-rock with which Kasabian first made their name." The album opens with "Let's Roll Just Like We Used To", which begins with a gong, and features a Mexican trumpet riff, a 'funky, spy-movie bassline', and elements of mod. The second track and lead single "Days Are Forgotten" is a blues rock-leaning song boasting a 'filthy riff' alongside a 'trademark vowel-murdering, stadium-shaking chorus' and has also
```

### Album 299, chunk 2

```text
drawn comparisons to Led Zeppelin's "Immigrant Song". Described as a 'sublime ballad', "Goodbye Kiss" is atypical of the band's familiar style, and was covered by American singer Lana Del Rey for BBC Radio One's Live Lounge. "La Fee Verte" is named after the historical nickname for absinthe that translates into 'the green fairy' and was originally written and sung by Sergio Pizzorno for the soundtrack to London Boulevard. The song has drawn heavy comparisons to the Beatles and was described by Pizzorno as 'retro, but still sounds modern'. The title track has been labelled as an 'energetic rave-up' with 'grimy guitars, absurd lyrics and an air-punching chorus.' "Acid Turkish Bath (Shelter From the Storm)" has been regarded as the biggest showcase of the album's Middle Eastern influences, featuring a 'wordless intro chant to the cutting strings and the brutal Bonham drumbeat'. The song was used in the end credits to the movie Killer Elite. "I Hear Voices" has been branded as 'Kraftwerk-inspired' electronica and has drawn comparisons to the 1982 sci-fi film Tron. The second single "Re-Wired" is an electronic rock and disco-inspired song and has been linked to the White Stripes. Fourth single "Man of Simple Pleasures" was described by Pizzorno as a 'country song played by zombies' and has been likened to Oasis as well as the track "Thick as Thieves" from the band's previous album West Ryder Pauper Lunatic Asylum. The pre-released free download track "Switchblade Smiles" has been regarded as a bridge between rock and electronica,
```

### Album 299, chunk 3

```text
featuring 'grungy guitar riffs threatening to smash the dance floor to bits.' The song was featured on the soundtrack for FIFA 12. The closing track "Neon Noon" is a 'reverb-drenched slow-burner' combining acoustic guitars, strings and electronic elements. Velociraptor! received a strong critical reception and is often considered by fans and critics to be one of the band's strongest albums. On Metacritic, Velociraptor! has the band's highest rating with a score of 79 out of 100 based on 23 reviews, indicating "generally favorable reviews". Their previous best album score was 68, held by West Ryder Pauper Lunatic Asylum (2009). NME reviewed the album positively, praising its ridiculousness and despite concluding that it falls short to its predecessor, it is "an album with 'much to love about it". Antiquiet gave it 4 1/2 stars out of 5 and declared that "Kasabian has found a way to channel everything you love about The Rolling Stones, Led Zeppelin and Radiohead while still keeping the unique sound that sets them apart from the contemporaries like Coldplay, Muse and The Killers." The album debuted at number one on the UK Albums Chart, selling over 90,000 copies in its first week. In 2011, Velociraptor! sold 279,000 copies in the UK. With little support from Sony Music, the album failed to chart in the United States.
```

## Album 300: Wake Up Call — John Mayall

- **album_id:** `611b4c69-223a-4106-860f-84bc8efdeab8`
- **Tags (identification only):** blues rock, blues, rock
- **Chunks:** 1 (163 words)

### Album 300, chunk 1

```text
Wake Up Call is an album by British bluesman John Mayall (also called a John Mayall & the Bluesbreakers album) with various special guest appearances by Buddy Guy, Mick Taylor, Mavis Staples and other musicians, released on 6 April 1993. John Mayall - lead vocals, piano, harp, guitar, flute, Hammond organ Coco Montoya - lead and rhythm guitar Rick Cortes - bass guitar Joe Yuele - drums Buddy Guy - vocal and lead guitar on "I Could Cry" Mavis Staples - vocal on "Wake Up Call" Mick Taylor - lead guitar on "Wake Up Call" and "Not at Home" Albert Collins - lead guitar on "Light the Fuse" and "I'm a Sucker for Love" David Grissom - rhythm and lead guitar Michael Bruno - percussion Joe Sublett - saxophone Darrell Leonard - trumpet Maggie Mayall - backing vocals Tom Canning - Hammond organ R.S. Field - Producer John Gabrysiak - Executive Producer Ron Kaplan - Executive Producer Dave McNair - Engineer and Producer
```
