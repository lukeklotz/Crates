# Embedding text relevance, batch 5 of 12 (albums 101–125 of 300)

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

This batch: **25 albums, 78 chunks**.

## Album 101: A Thousand Leaves — Sonic Youth

- **album_id:** `fee7c606-5a57-49a3-89c7-238e5a98290a`
- **Tags (identification only):** rock, alternative rock, no wave, animal on cover, art rock, avantgarde, experimental rock, hamster on cover
- **Chunks:** 7 (1645 words)

### Album 101, chunk 1

```text
A Thousand Leaves is the tenth studio album by American rock band Sonic Youth, released on CD and cassette on May 12, 1998, by DGC Records. A double-LP vinyl issue had been released three weeks earlier, on April 21, 1998, by My So Called Records. It was the band's first album recorded at their own studio in Lower Manhattan, which was built with the money they had made at the 1995 Lollapalooza festival. Since the band had an unlimited amount of time to work in their studio, the album features numerous lengthy and improvisational tracks that were developed unevenly. The highly experimental extended plays Anagrama, Slaapkamers met slagroom, and Invito al ĉielo were recorded simultaneously with the album. A Thousand Leaves reached number 85 on the US Billboard 200 and number 38 on the UK Albums Chart. It received generally favorable reviews from critics, who praised the lengthy, quiet guitar interplay between band members Thurston Moore and Lee Ranaldo. However, some criticized the forced vocal delivery of member Kim Gordon and found several tracks to be unnecessarily long and poorly constructed. The song "Sunday" was released as a single with a music video directed by Harmony Korine and starring American actor Macaulay Culkin. A Thousand Leaves is the follow-up to Sonic Youth's 1995 album Washing Machine, which was released shortly after the band concluded their stint headlining the 1995 Lollapalooza music festival. With the money they had made at the festival, the band decided to build a recording studio, called
```

### Album 101, chunk 2

```text
Echo Canyon, on Murray Street in Lower Manhattan. The span of nearly three years between Washing Machine and A Thousand Leaves also represented the longest gap between studio albums in Sonic Youth's career at the time. Singer and guitarist Thurston Moore explained that the band needed a break, noting that they had been touring non-stop for 16 years. He said, "We're having children, we're getting older, let's just cool out a little bit and build this workshop, and go that way, work that route." In their new studio, the band began writing new songs from extended improvisations in rehearsal. Several instrumental jams were released as extended plays through the band's own record label, Sonic Youth Recordings, and distributed by Smells Like Records, an independent record label previously formed by drummer Steve Shelley. These include Anagrama, Slaapkamers met slagroom and Invito al ĉielo. Since A Thousand Leaves was the first Sonic Youth album that was recorded in their own studio, the band had more time and freedom to work on it. As a result, the songs evolved unevenly and were recorded from an early stage of development. According to guitarist Lee Ranaldo, the album is "a reflection of where we were at the time. We weren't into making anything concise. We were just playing what we felt like playing. We really didn't feel like what we needed to be doing was producing another record like Goo." The 11-minute song "Hits of Sunshine (For Allen Ginsberg)" was initially intended to be released
```

### Album 101, chunk 3

```text
on one of the EPs as an instrumental track, but it was ultimately included on the album with vocals. The album was co-produced by the band and Confusion Is Sex producer Wharton Tiers and mastered by Greg Calbi at Masterdisk in New York City. Musically, A Thousand Leaves was considered more expansive and relaxed than previous Sonic Youth albums, with less feedback and more guitar playing and improvisation. According to David Browne, the record explored post-rock sounds that were "subtler" and "quirkier" than most mainstream rock at the time. The title of the album was inspired by Walt Whitman's Leaves of Grass. According to Moore, "The same way he improvises with images and words, we improvise with sounds and notes". He also attributed the style of the album to the fact that the band was getting older, commenting, "You also become much involved with your thoughts about life experience in general. Having children is incredible in that way." The song "Snare, Girl" explored these topics. The longest song on the album, "Hits of Sunshine (For Allen Ginsberg)", referenced American poet Allen Ginsberg and contains an instrumental interlude that was described as "a subtle, drawn-out passage of Morse code guitar lines and lazy afternoon with wah-wah pedal licks—bliss in slow motion." Like previous Sonic Youth albums, A Thousand Leaves also contains songs that deal with gender roles and stereotypes. The song "Female Mechanic Now on Duty", sung by band member Kim Gordon, was a reaction to how journalists categorize female musicians.
```

### Album 101, chunk 4

```text
It was inspired by Meredith Brooks's hit "Bitch". Similarly, in "The Ineffable Me", Gordon expressed her opposition to such limitations. The song "Karen Koltrane", sung by Ranaldo, is about a lover from his college days who had "a far less extraordinary adulthood" than he had first thought, while "Hoarfrost", which was originally titled "Woodland Ode", was inspired when Ranaldo and his wife Leah Singer went for a walk in the snow during a visit they made to Singer's parents in Winnipeg, Manitoba, Canada. The track "Sunday" is generally considered the album's most accessible song. It was originally recorded for Richard Linklater's 1997 film SubUrbia, but was later re-recorded for A Thousand Leaves. A Thousand Leaves was released on vinyl, CD, and cassette formats on May 12, 1998, by DGC Records. The album cover features an artwork by artist Marnie Weber, which depicts a hamster and Weber herself at age 12 sporting animal horns. According to Moore, the image is a reference to the Unlimited Edition compilation album by German experimental rock band Can. Originally, the album was titled Mille Feuille (French for A Thousand Leaves) and was intended to feature an image of Moore holding a pastry as the cover art. To promote the album, a radio edit version of "Sunday" was released as a single to modern rock, college, and public radio in April 1998. The band also supported the album with a tour across the US and Canada from May to June 1998. Upon release, A Thousand Leaves
```

### Album 101, chunk 5

```text
reached No. 85 on the US Billboard 200 and No. 38 on the UK Albums Chart. The album also charted in other countries, including France, Belgium, Sweden and Norway. The single "Sunday" reached No. 72 in the UK Singles Chart and was eventually released on vinyl and CD on July 14, 1998, containing a Nirvana cover, "Moist Vagina", as one of its B-sides. A music video directed by Harmony Korine and starring Macaulay Culkin was made for the single. The band chose Korine due to his work on the films Kids (1995) and Gummo (1997), the first of which featured several young actors who previously appeared in the music video for the band's 1993 single "Sugar Kane", including American actress Chloë Sevigny. As of July 1999, the album had sold 54,000 copies in the United States according to Nielsen SoundScan. And as of 2005, the album had sold 66,000 copies. A Thousand Leaves was well received by critics, some of whom regarded it as one of Sonic Youth's best albums yet. Writing for AllMusic, Stephen Thomas Erlewine described the album as "the band's most challenging and satisfying record in years" and praised its quiet guitars and unpredictable twists, which kept the lengthy songs captivating. Pitchfork editor Brent DiCrescenzo cited "Hits of Sunshine (For Allen Ginsberg)" as the album's centerpiece and highlighted the album's jamming, improvising, and guitar interplay between Moore and Ranaldo. David Stubbs of Spin criticized Gordon's weak singing and forced guitar playing on "Contre le sexisme", "Female Mechanic
```

### Album 101, chunk 6

```text
Now on Duty", and "The Ineffable Me", but nevertheless judged the "continually inventive fretboard effects" of Moore and Ranaldo, which "[sparkle] gold-plating adornments that cut open and irritate [the album] at every turn." Other reviews were less enthusiastic. Sara Scribner from the Los Angeles Times said that A Thousand Leaves was a monotonous "experimental, psychedelic record" that felt "like a passionless, less thoughtful shadow of [the band's] former self". J.D. Considine of Entertainment Weekly stated similar cons, calling the record "the sort of thing that gives art rock a bad name." Ben Ratliff of Rolling Stone found the songs to be unnecessarily long and sluggish, commenting that the album "really does sound like a demo — eleven songs waiting for better organization and cliché removal". Similarly, Stephen Thompson of The A.V. Club felt that the album rarely contained fully formed songs and that the band should start "completing its ideas before recording them for posterity." Orlando Weekly criticized Gordon's "contrived and annoying" vocal delivery, saying that many songs are "merely lengthy feedback collages with pasted-on vocals and gobs of art-school pretension", but also admitted that the album contains some "hidden gems" like "Sunday" and "Wildflower Soul". In a very positive review for The Village Voice, Robert Christgau called A Thousand Leaves a mature and beautiful record, commenting: "It's the music of a daydream nation old enough to treasure whatever time it finds on its hands. Where a decade ago [Sonic Youth] plunged and plodded, drunk on the forward notion of
```

### Album 101, chunk 7

```text
the van they were stuck in, here they wander at will, dazzled by sunshine, greenery, hoarfrost and machines that go squish in the night." Although the album was not ranked in the Top 40 of The Village Voice's Pazz & Jop critics' poll for 1998, Christgau, the poll's creator, placed it at No. 3 in his own "Dean's List". He would later name it one of the 10 best records of the 1990s. Similarly, the editors of NME placed the album at No. 40 in their year-end top 50 list. The Wire named the album its record of the year in its year-end critics' poll. Thurston Moore – guitar, vocals, production Kim Gordon – guitar, bass, vocals, production Lee Ranaldo – guitar, vocals, production Steve Shelley – drums, production Wharton Tiers – production Don Fleming – additional production Mark Borthwick – sleeve photography and typography
```

## Album 102: Give the People What They Want — The Kinks

- **album_id:** `33feda6b-565b-4fa7-8b52-bd7e25d84b45`
- **Tags (identification only):** rock, pop rock, album rock, aor, hard rock, power pop
- **Chunks:** 1 (221 words)

### Album 102, chunk 1

```text
Give the People What They Want is the nineteenth studio album by the English rock band the Kinks. It was released on 15 August 1981, through Arista Records. Produced by Ray Davies, the album followed up the successful Low Budget (1979) and expanded on that record's hard rock style. The initial release of the album in the UK was delayed because lead singer Ray Davies wanted to produce a full-length video for the album but financing fell through. Also scrapped were plans to remix the album for the European market. Upon the reissue of the album on CD with the rest of the Kinks' six Arista studio albums, Give the People What They Want was the only one that did not contain bonus tracks, despite the existence of non-album tracks: the single version of "Better Things" was slightly longer than the album version (previously included on the Come Dancing with The Kinks compilation) and the British b-side of "Better Things" was a non-album track, "Massive Reductions", which was different from the version from the band's 1984 album Word of Mouth. Ray Davies – guitar, keyboards, vocals Dave Davies – guitar, vocals Jim Rodford – bass Mick Avory – drums Ian Gibbons – keyboards Chrissie Hynde – vocals on "Predictable", "Add It Up", "Art Lover" and "A Little Bit of Abuse" (uncredited)
```

## Album 103: Shadow Zone — Static‐X

- **album_id:** `a9881aad-fee3-42ef-bf43-788df4ea1ee3`
- **Tags (identification only):** alternative metal, industrial metal, heavy metal, industrial, nu metal, post grunge, rock
- **Chunks:** 5 (1252 words)

### Album 103, chunk 1

```text
Shadow Zone is the third studio album by American industrial metal band Static-X, released on October 7, 2003. Marked by many personnel and stylistic changes, the album sports a much more melodic sound than any other work in their catalog, while still staying in the confines of their industrial metal and nu metal sound. It was the first of two albums to feature guitarist Tripp Eisen, and is the band's only album to not feature an official drummer, due to the departure of Ken Jay just prior to the album's recording sessions; drumming duties were subsequently handled by Josh Freese. In 2002, Static would be contacted by Jonathan Davis of the nu metal band Korn. Davis had recently signed on to provide the soundtrack for the Queen of the Damned film soundtrack, but due to contract limitations with Sony, was legally unable to actually perform the music he had written for the soundtrack. As a remedy of this, Davis contacted a number of metal vocalists, Static included, to sing on the songs he had written. Static provided vocals for one track, "Not Meant for Me", with the Queen of the Damned soundtrack releasing in February 2002. Meanwhile, prior to starting up sessions for a third album, tensions had grown high within the band. The band found success with their platinum-selling debut album, Wisconsin Death Trip in 1999, but dissatisfaction grew in the band in creating the follow-up, Machine in 2001. With their first album, the band had created it together,
```

### Album 103, chunk 2

```text
led by Static, whereas with the follow-up, the album was completely written by Static alone. Static had felt anxiety in being able to recreate the success of the first album, and resented the band for not helping him work on the second while touring. Concurrently, the rest of the band resented Static for leaving them out of the process when telling him they'd rather focus on touring. The move led original guitarist Koichi Fukuda to leave the band, and left the rest of the members largely upset with Static. Guitarist Tripp Eisen was brought in to replace Fukuda. Work on the album started in early 2002, and would span well over a year. Writing sessions began during the last of the band's touring in support of Machine. By March 2002, the band had started their first jam sessions of the new material. Material would be demoed by the band in Static's home studio in Burbank, California. However, Static would concede that his early demos sounded very different from the album's eventual new direction. Static's contribution to the Queen of the Damned soundtrack would prove to be a turning point for the band. The track, which was much more melodic than much of the band's music up until that point, would attract the attention of Warner Bros. executive Tom Whalley, who pressured the band as a whole to pursue a melodic sound. Personnel and line-up changes would further alter the band's sound. The label would not allow the band to work
```

### Album 103, chunk 3

```text
again with record producer Ulrich Wild as they had for their prior two albums, instead arranging for them to work with Josh Abraham, a producer known for working with more commercially melodically mainstream bands such as Staind, Filter, and Velvet Revolver. The album would also be the only album to feature Josh Freese of the band A Perfect Circle, on drums. Freese was a last minute addition to recording, after the resignation of drummer Ken Jay, who quit two days before the band was scheduled to enter the studio to start the recording process, due to being unhappy with the direction the album was heading. All of this would fundamentally change how the band had worked on prior albums. The album would be the first to feature Eisen's songwriting contributions and performances, which was a change for the band, since Fukuda had not historically written material for the band, and Static had performed all guitar parts on Machine. Eisen wrote around half of the material for the album, though it was largely described by him as "a lot of collaborative efforts" between band members. Static enjoyed collaborating with Eisen in the sessions stating that his "punk rock attitude" was refreshing and brought a new approach and sound to the album; while Static typically was more of a "big picture" person, with this album, he let Eisen take control of many of the musical ideas while he focused more so on vocals. The band had amassed over 20 songs by March
```

### Album 103, chunk 4

```text
2003, with five being revealed by name - "Shadow Zone", "The Only", "New Pain", "Deliver Me", and "Breathe". Freese joined the sessions later, once the band had ironed out which songs were likely to make the cut. Prior albums employed the use of drum machines with Jay's live cymbals edited in afterwards, whereas for Shadow Zone, the band opted to do the opposite; they wrote and demoed the songs with a drum machine, but chose to use Freese's live drums after being very impressed with his work. Freese completed all of his drum parts in three days, even though he had never heard a single song prior to the sessions. Static explained his experience with Freese: The dude is just amazing. It changed my life and it changed my perspective on drummers. We played the demo for him twice and he'd take down a couple of notes and then we'd run through the songs three times and then that was it and then we'd move onto the next song. We did three or four songs a day and then in three days we were done. I really got goose bumps on some of the shit he was doing. That was why I was willing to change things up and have the drummer come in and really be a part of things. Everything kind of changed and went in that different direction." Recording sessions wrapped up by June 2003. While the band was unable to retain Wild as a producer, they
```

### Album 103, chunk 5

```text
were able to secure him for the album's final mixing process. While the album was still described commonly as industrial metal, nu metal, alternative metal, much like the rest of their work, Shadow Zone focused much more on melody than any other album in their catalog. Static's vocal performance on Shadow Zone was commonly compared by journalists as similar to Jonathan Davis of Korn. Allmusic also felt that his vocals on the second single, "So", sounded similar to the vocals of Layne Staley of Alice in Chains. Recording the album wrapped up in June 2003, Nick Oshiro, prior drummer of the band Seether, joined the band shortly after the recording process to tour in support of the album, as Freese was always meant to just be a temporary session drummer for the album’s creation. The album's first single, "The Only", was released to radio in August 2003. Shadow Zone was released on October 7, 2003. A second single, "So", was later released in 2004. The album debuted at no. 20 on the Billboard 200 charts, selling 48,418 copies in its first week, just over half the number of their prior album, Machine. By January 2004, the album had sold 179,051 copies. Wayne Static – lead vocals, rhythm guitar, keyboards, programming Tripp Eisen – lead guitar Tony Campos – bass, backing vocals Nick Oshiro – drums (credited but does not perform) Josh Freese – drums Ken Jay – additional keyboards Josh Abraham – production Ulrich Wild – mixing Tom Whalley – executive producer
```

## Album 104: We Are the Void — Dark Tranquillity

- **album_id:** `803cc12f-9082-4078-9dc8-c3bb6b9b3c49`
- **Tags (identification only):** melodic death metal
- **Chunks:** 1 (293 words)

### Album 104, chunk 1

```text
We Are the Void is the ninth studio album by Swedish melodic death metal band Dark Tranquillity. It is their first and only album with bassist Daniel Antonsson, who joined in 2008 and left in 2013. The band began writing for this album in late 2008 (except for the majority of "Iridium" which was written sometime between 1996 and 1998 but was left out until this album). Stylistically, it is similar to their previous album Fiction; the band used the same Drop B tuning as well as clean melodic vocals that were re-introduced on Fiction. The band also began to release songs from this album on their MySpace page starting with "Dream Oblivion" on 21 December 2009, "At the Point of Ignition" on 14 January 2010 and finally the entire album was available for free streaming on 19 February 2010. Music videos were released for "Shadow in Our Blood" on 10 February 2010 and "In My Absence" on 22 February 2012. Kyle Ward of Sputnikmusic, described the album: "If you take Fiction, cut out the awesome guitar riffs, increase the keyboard presence tenfold, and then make it more depressed-sounding, you will have exactly what We Are The Void delivers." Metal Underground said that the album is "Excellent melodic death metal, but it feels like Dark Tranquillity has released the same album three times in a row now." Mikael Stanne – vocals, lyrics Martin Henriksson – guitars, sound recording Niklas Sundin – guitars, album artwork Anders Jivarp – drums Martin Brändström – electronics, engineering Daniel Antonsson – bass guitar, guitar solo (on "Shadow in Our Blood" (1st part) and "At the Point of Ignition"), engineering Tue Madsen – mixing (October–November 2009) & mastering (Antfarm Studio in Århus) Anders Björler – filmed "Studio Report 2009"
```

## Album 105: What If It’s You — Reba

- **album_id:** `7887d854-0176-4d12-878e-cb11d32bbc4a`
- **Tags (identification only):** country, contemporary country, neo traditionalist country, pop, rock
- **Chunks:** 1 (250 words)

### Album 105, chunk 1

```text
What If It's You is the twenty-first studio album by American country music artist Reba McEntire. It was released on November 5, 1996, and would peak at #1 on the Billboard country chart and #15 on the Billboard 200. It is certified 2× Multi-Platinum by the RIAA. What If It's You was the first album in which McEntire did not use session musicians; relying instead on her touring band. The album produced four singles in "The Fear of Being Alone", "How Was I to Know", "I'd Rather Ride Around with You" and "What If It's You", which respectively reached #2, #1, #2, and #15 on the Billboard country charts. The album peaked at #1 on the Billboard Top Country Albums chart and #15 on the Billboard Top 200 Albums chart. Reba McEntire – vocals Paul Hollowell – acoustic piano Doug Sisemore – keyboards Biff Watson – acoustic guitars Steve Gibson – acoustic guitar (2) Kent Wells – electric guitars Terry Crisp – steel guitar Larry Franklin – fiddle, mandolin Chopper Anderson – bass Scott Hawkins – drums, percussion Joe Chemay – backing vocals Liana Manis – backing vocals Reba McEntire – producer, make-up John Guess – producer, recording, mixing Derek Bason – recording, mix assistant Scott Ahaus – recording assistant Patrick Murphy – recording assistant Marty Williams – mastering at The Work Station (Nashville, Tennessee) Carole Ann Mobley – production coordinator Sandi Spika – hair, wardrobe stylist Mary Beth Felts – hair, make-up Narvel Blackstock for Starstruck Entertainment – management
```

## Album 106: Hurry Up, We’re Dreaming — M83

- **album_id:** `9f3bad09-c5a1-447e-a3f7-06578214a96f`
- **Tags (identification only):** dream pop, electronic, ambient pop, shoegaze, synth pop, rock, 1–4 wochen, ambient music
- **Chunks:** 7 (1611 words)

### Album 106, chunk 1

```text
Hurry Up, We're Dreaming (stylised as HurryUp,We'reDreaming.) is the sixth studio album by French electronic music band M83. The album was released on 18 October 2011, by Naïve Records in France and by Mute Records in the United States. The album was the last M83 album with keyboardist Morgan Kibby before her departure, and the band's first full double album. The album received generally favourable reviews from critics. It debuted at number 15 on the US Billboard 200 with first-week sales of 21,000 copies, making it M83's highest-charting album to date. It sold 300,000 copies in the United States as of March 2016. The album was nominated for Best Alternative Music Album at the 2013 Grammy Awards and was ranked at number 134 on Pitchfork's list of "The 200 Best Albums of the 2010s" in October 2019. Prior to recording Hurry Up, We're Dreaming, M83 frontman Anthony Gonzalez moved from France to Los Angeles, United States. Describing the move in an interview, Gonzalez said, "Having spent 29 years of my life in France, I moved to California a year and a half before the making of this album and I was excited and inspired by so many different things: by the landscape, by the way of life, by live shows, by movies, by the road trips I took alone... I was feeling alive again and this is, I feel, something that you can hear on the album." Gonzalez toured with the Killers, Depeche Mode, and Kings of Leon before recording,
```

### Album 106, chunk 2

```text
which influenced the album. He was also influenced by his road trips to Joshua Tree National Park. Gonzalez cited the ambitiousness of albums such as Mellon Collie and the Infinite Sadness by the Smashing Pumpkins as the reason Hurry Up, We're Dreaming was made a double album. He described the two discs as brother and sister, with each track having a sibling on the other disc. Gonzalez created the album to remember his childhood. Gonzalez explained to Spin that Hurry Up, We're Dreaming is "mainly about dreams, how everyone is different, how you dream differently when you're a kid, a teenager, or an adult. I'm really proud of it. If you're doing a very long album, all the songs need to be different and I think I've done that with this one." In an interview with musicOMH, he described the album as "a reflection of my 30 years as a human being" and something he dedicated to himself. The album was recorded in Los Angeles at Sunset Sound and the Sound Factory. Because of budget constraints and union issues, the string and brass players who contributed to the album were not paid and were credited with pseudonyms. The album features contributions from Medicine's Brad Laner and Zola Jesus. Anthony Gonzalez compared Hurry Up, We're Dreaming's sound to two of his previous releases, describing it as a mix between the synth-pop used on Saturdays = Youth (2008) and the ambient of Before the Dawn Heals Us (2005). The album includes instruments
```

### Album 106, chunk 3

```text
previously unused by M83, such as the acoustic guitar, flute and saxophone. Critics have noted musical influences from 1980s artists, including Kraftwerk, Simple Minds, Peter Gabriel and Harold Faltermeyer, as well as synth-pop band Cut Copy. Hurry Up, We're Dreaming was first teased on 23 June 2011 in a YouTube video titled "Echoes...", which also announced dates for a North American tour. The album's lead single, "Midnight City", premiered online on 19 July 2011, and was officially released on 16 August 2011. On 10 October 2011, the album became available to be streamed in its entirety on the Urban Outfitters website. Urban Outfitters also hosted a simultaneous listening party at all of its stores the Saturday before Hurry Up, We're Dreaming's release. On 17 October 2011, the music video for "Midnight City" was released. The album was released on 18 October 2011, by Naïve Records in France and by Mute Records in the United States. On 30 May 2012, a music video for the album's second single, "Reunion", was released. The video is a follow-up to the "Midnight City" music video. M83 released a music video for "Steve McQueen" on 25 October 2012. On 5 November 2012, a three-disc deluxe edition featuring remixes of "Midnight City", "Reunion" and "Steve McQueen" was announced. On 5 December 2012, a music video for "Wait" was released. The album's closer "Outro" was used in the extended trailer for 2012 film Cloud Atlas as well as other trailers and films over the following years. Hurry
```

### Album 106, chunk 4

```text
Up, We're Dreaming received generally positive reviews from music critics. At Metacritic, which assigns a normalised rating out of 100, derived from reviews from mainstream critics, the album received a score of 76, based on 38 reviews. Pitchfork's Ian Cohen gave the album its "Best New Music" accolade, considering it the band's best record to date. Cohen also noted the reduction of the "heavily saturated synths" of Anthony Gonzalez's earlier work in favour of more accessible songs, adding that "the traditionally structured songs here are some of the most thrilling pop music released this year." Similarly, The Daily Telegraph's James Lachno felt that the album "finally fuses his innate ingenuity with an accessible, commercial edge." Rudy Klapper of Sputnikmusic praised the influence of 1980s music on the album, and called the record "near flawless, an essential distillation of the sounds of Gonzalez's youth, nostalgia and melancholy and happiness all mixed up into a sparkling pop stew." Simon Price of The Independent called the album "a towering city of sparkling synth edifices simultaneously summoning the best of the 1980s (New Order, The Cure) and the current breed (The Knife, Empire of the Sun)". Under the Radar's Laura Studarus described Hurry Up, We're Dreaming as a "remarkable accomplishment" and a "double album of stunningly ambitious, synth-soaked dreams". Jamie Crossan of NME compared the album's "guileless and dreamy" nature to the title character of the 1943 novella The Little Prince and admitted that this comparison would be "quite a bold statement to make,
```

### Album 106, chunk 5

```text
but this is an album of equal valor." Reef Younis of BBC Music felt that while "some consistency may have been sacrificed in favor of a space-filling selection of tracks, this set still represents a heaving, breathing journey through the introspective and the bombastic, the striving and the exhaustive. It is the undeniable sound of one man's triumphant dreams." Heather Phares of AllMusic wrote that while the album "may not be quite as striking as Saturdays = Youth, it delivers a welcome mix of classic sounds and promising changes." David Marchese of Spin felt that Hurry Up, We're Dreaming is "full of goose-bump moments", but that the "lack of something as enjoyably plain (and relatively calm) as 'Kim & Jessie'... makes Gonzalez's insistence on oversize emotions feel a tad restrictive." In a similarly mixed review, Timothy Gabriele of PopMatters criticised M83 for "focusing too much on magnitude throughout and too little on depth" on the album, but noted that the "totality of sound" on the album "has a way of blinding even the most critical listener to the problems that underline many of the album's lesser songs". The A.V. Club's Christian Williams found the album underwhelming, writing, "for an album of such impressive scale and nanoscopic attention to detail, Dreams [sic] leaves a surprisingly light impression." Kevin Liedel of Slant Magazine criticised the album for rehashing sounds from earlier M83 albums and felt that it sounded "much more like an M83 wannabe's poor imitation than the real deal." Hurry Up,
```

### Album 106, chunk 6

```text
We're Dreaming appeared on several end-of-year lists. Filter named it the best album of 2011. Paste named the album as the ninth best album of 2011, writing "As with everything the Frenchman's done so far, the album is lush and ably produced, crescendo after crescendo." Pitchfork named it the third best album of 2011, with Jayson Greene writing: "Hurry Up We're Dreaming doesn't just draw liberally from the spirit of the massive rock albums Gonzalez name-checked, it practically swallows them whole, regurgitating and redistributing them into something listeners from every corner of the music universe can hear a piece of their lives in." Popmatters ranked the album as number five on its list of "The 75 Best Albums of 2011", while Spin ranked the album number 19 on its end-of-year list. Online music retailer eMusic ranked the album number two on its "Best Albums of 2011" list. The lead single "Midnight City" was singled out for praise. Paste named it the second-best song of the year. PopMatters named it the best song of 2011, with Ryan Reed writing: "On this transcendent standout [...] Anthony Gonzalez and co-synth-scientist Justin Meldal-Johnsen build layer upon layer of keys, arena-sized drums, and vocal atmospherics (not mentioning one of the tastiest sax solos this side of a Springsteen record). The result? The synth Sistine Chapel." Prior to touring for Hurry Up, We're Dreaming, Anthony Gonzalez posted an open audition on M83's website for a multi-instrumentalist who could play guitar, bass and keyboards to join him
```

### Album 106, chunk 7

```text
on tour. Jordan Lawlor of Sparta Township, New Jersey was hired from the audition. The tour for the album began in Mexico City on 15 October 2011 and ended on 1 December 2011 in London, England. The second leg of the tour began on 12 January 2012 in Los Angeles and was set to end on 8 August 2012 in New York City, but was later extended, ending in London on 8 November 2012. During the second leg, M83 performed at the 2012 Coachella Valley Music and Arts Festival on 13 and 20 April, at the St Jerome's Laneway Festival in Australia and New Zealand, and at Lollapalooza in Chicago, Illinois.
```

## Album 107: The Audience’s Listening — Cut Chemist

- **album_id:** `ef1235b8-476d-4419-9788-de5b0bf01a6d`
- **Tags (identification only):** electronic, hip hop, beats, cut up dj, hip hop rap, instrumental hip hop, rap and hip hop
- **Chunks:** 1 (182 words)

### Album 107, chunk 1

```text
The Audience's Listening is the debut studio album by Cut Chemist, released on Warner Bros. Records on July 11, 2006. It features guest appearances from Hymnal, Edan, Mr. Lif, and Thes One. After leaving Jurassic 5 in 2004, Cut Chemist spent 18 months working exclusively on the album, which he had already been working on for 2 years. He spent almost a year clearing samples. At Metacritic, which assigns a weighted average score out of 100 to reviews from mainstream critics, the album received an average score of 79% based on 15 reviews, indicating "generally favorable reviews". David Jeffries of AllMusic gave the album 3.5 stars out of 5 and described it as "a well-crafted, highly enjoyable effort that overcomes the 'all samples cleared' challenge all big-label turntablist albums must face." Jeff Vrabel of PopMatters gave the album 7 stars out of 10, saying, "It's DJ music for the casual fan, something you don't need to be a knob-twiddler or connoisseur of the break beat to appreciate or enjoy." In 2015, Vice named it the 49th greatest dance album of all time.
```

## Album 108: Another Hostile Takeover — Hanoi Rocks

- **album_id:** `0919ba2e-81e2-42a2-9786-3c7444a46084`
- **Tags (identification only):** glam, hard rock, heavy metal, finland, finnish, rock
- **Chunks:** 1 (101 words)

### Album 108, chunk 1

```text
Another Hostile Takeover is the seventh studio album by the Finnish rock band Hanoi Rocks, released in 2005. This was the second album which the "reborn" Hanoi Rocks released in the new millennium. When it was released, critics praised the album, but fan reactions were mixed. Michael Monroe – lead vocals, harmonica, saxophone, guitars, keyboards, bass, castanet, percussion, Jew's harp, drums Andy McCoy – lead, rhythm, acoustic and 12-string guitars, backing vocals, bouzouki, mandolin, clavinet Conny Bloom – lead and rhythm guitars, backing vocals Andy Christell – bass, backing vocals Lacu – drums, percussion Eepo Mänty-Sorvari – drums on track 15
```

## Album 109: Lonely and Blue — Roy Orbison

- **album_id:** `98adfd61-7ddc-47e4-896e-2f674e99d003`
- **Tags (identification only):** rock, country pop, pop, rock and roll, rockabilly, brill building, countrypolitan, doo wop
- **Chunks:** 2 (390 words)

### Album 109, chunk 1

```text
Lonely and Blue is the debut studio album by Roy Orbison, released on Monument Records in January 1961, and was available both in stereo and mono. It entered the UK albums chart two years later, on June 30, 1963 and reached number 14 over the course of eight weeks. The track, "Come Back to Me (My Love)", features an almost identical intro to "Only the Lonely" because this is where the vocal figure of "Only the Lonely" came from. The album also features multiple covers of songs from Don Gibson, The Everly Brothers, Gene Pitney, and Johnnie Ray" The album was released on compact disc by Monument Records in 1993 as tracks 1 through 12 on a pairing of two albums on one CD with tracks 13 through 24 consisting of Orbison's 1962 album, Crying. Bear Family included also the album in the 2001 Orbison 1955-1965 box set. Sony Music label included this CD in the 2013 Roy Orbison The Monument Box Set. Avid Rock 'n' Roll labels included this CD in the 2017 3 Classic Albums Plus Box Set. After a two-year stint at Sun Records, Roy Orbison signed up with RCA Records in 1958, but left after two singles. In early 1959 Orbison's manager Wesley Rose asked producer and owner Fred Foster if he was interested in signing him for Monument Records. Foster said yes. The album was recorded at RCA Studio B using two- and three-track tape machines. Bruce Eder of AllMusic said that the album "packed
```

### Album 109, chunk 2

```text
with great moments and different permutations of that sound: the powerful lead vocal and the Boots Randolph sax break on "I'll Say It's My Fault"; the haunting Orbison-Melson "Come Back to Me (My Love)," a vest-pocket romantic melodrama sung with operatic depth and played to a light rock & roll beat; Don Gibson's "I'd Be a Legend in My Time", and "I Can't Stop Loving You". Billboard magazine identified the album as a "Spotlight Winner of the Week" in its review from January 1961, described the album as "a Spinnable Album". Cashbox appreciated the effort. "Good material and a striking delivery add up to strong merchandise." Variety wrote that "his previous single chicks, Only The Lonely', 'Blue Angel', and 'I'm Hurtin' are included here as well as some other Nashville originated songs that take popsterws will find easy to take.".
```

## Album 110: Illumination — Earth, Wind & Fire

- **album_id:** `0dc7c897-6d52-444a-a1bf-d164da9c8af9`
- **Tags (identification only):** contemporary r and b, soul, disco, pop, quiet storm, r and b, smooth soul, urban
- **Chunks:** 4 (971 words)

### Album 110, chunk 1

```text
Illumination is the nineteenth studio album by American band Earth, Wind & Fire. It was released on September 20, 2005 by Sanctuary Records. Guest artists Big Boi, Kenny G, Kelly Rowland, will.i.am, Floetry and Brian McKnight are featured on Illumination. The album rose to number eight on the US Top R&B/Hip-Hop Albums chart and number 32 on the US Billboard 200 chart. Illumination was also Grammy nominated within the category of Best R&B Album. It is the final Earth, Wind & Fire album to feature their founder and co-lead vocalist Maurice White. "The Way You Move" featuring Kenny G was issued as the album's lead single. it reached number 12 on the US Billboard Adult Contemporary Songs chart. Second single "Show Me the Way" featuring Raphael Saadiq rose to number 16 on the Adult R&B Songs chart. "Pure Gold," Illumination's third singles, rose to number 23 on Billboard's Adult Contemporary singles chart and number 15 on the Adult R&B Songs chart. Fourth and final single "To You," which featured Brian McKnight, reached number 16 upon the US Adult R&B Songs chart and number 29 on the US Smooth Jazz Songs chart. Illumination was met with generally positive reviews. At Metacritic, which assigns a normalized rating out of 100 to reviews from professional publications, the album received an average score of 79, based on 12 reviews. Bill Lamb of About gave the album a four out of five star rating. He found that Illumination was a "truly classic package" that "effortlessly
```

### Album 110, chunk 2

```text
straddles the divide between classic and contemporary R&B." Dave Simpson of The Guardian gave a four out of five star rating, describing the album as "an often storming return to form." Steve Jones of USA Today noted that with Illumination Earth, Wind & Fire was "as vibrant as ever." Jim Farber of The New York Daily News felt that "their latest work features production and/or guest appearances from current hit makers like Will I. Am from the Black Eyed Peas, Big Boi from OutKast, Kelly Rowland from Destiny's Child, plus Jimmy Jam and Terry Lewis, Raphael Saadiq and others. All these guests haven't overwhelmed Maurice White's great band. They've just freshened it up. Singer Philip Bailey sounds as buttery as ever, and the band's tart horn arrangements and melodies extend the buoyancy and pleasure of their hits." Ben Thompson of The Daily Telegraph wrote "Illumination does find them successfully holding their own alongside some of the biggest names of the 21st century." David Wild of Rolling Stone proclaimed "Illumination, taps into Santana's now-familiar Supernatural formula: Give a veteran great a hip replacement by surrounding it with lots of gifted youngbloods. On Illumination, the formula works well largely because the parties involved — including Jimmy Jam and Terry Lewis, Raphael Saadiq and Black Eyed Peas' Will.i.am — seem to sincerely treasure the EWF sound. " Geoffrey Himes, writing for Washington Post, found that Illumination has "the right material and the right producers [...] The Earth, Wind & Fire voices and horns
```

### Album 110, chunk 3

```text
are given contagious hooks for their retro sound, while underneath, the producers cook up new beats for a new century." Raymond Fiore of Entertainment Weekly declared Illumination "a fluid, unforced marriage of modern beats and retro, horn-lined soul," while Antony Hatfield of BBC Music called the album a "great all star team effort, which should appeal to fans of all concerned." Illumination was Grammy nominated in the category of Best R&B Album. The album was also nominated for a Soul Train Music Award in the category of Best R&B/Soul Album – Group, Band or Duo. As well Earth, Wind & Fire was nominated for an NAACP Image Award in the category of Outstanding Duo or Group. "Show Me the Way" was also Grammy nominated in the category of Best R&B Performance by a Duo or Group with Vocals. The album debuted and peaked at number 32 on the US Billboard 200 and number eight on the Top R&B/Hip-Hop Albums chart, with first week sales of 29,000 copies. It was Earth, Wind & Fire's highest-charting album since 1987's Touch the World. The album also peaked at number 61 on the Oricon Charts in Japan. "This Is How I Feel" was featured in the movie Hitch and "Love's Dance" was featured in the feature film Robots. "Pure Gold" was featured in the movie Roll Bounce. Damien Smith – executive producer, A&R direction Philip Bailey – executive producer Maurice White – executive producer Montina Cooper – vocal producer for Kelly Rowland (6) Glenn
```

### Album 110, chunk 4

```text
Standridge – production coordinator (5, 7, 8) Dee Dee Murray – production coordinator (6, 9) Goldfinger C.S. – design Heavyweight – cover art Pamela Springsteen – photography, album image inspiration Davett Singletary – marketing consultant Mark Young – publicist Wayman Jones – promotion Technical credits Brian Gardner – mastering at Bernie Grundman Mastering (Hollywood, California) Cameron Marcarelli – recording (1, 6, 9, 11, 12), horn recording (2, 4), mixing (11) Neal Pogue – mixing (1, 6, 9), recording (6, 9) Ian Cross – recording (2, 4) Matt Marrin – mixing (2, 4) Gerry Brown – recording (5) John Tanksley – recording (5) Manny Marroquin – mixing (5) Danny Romero – mixing (5, 7, 8), recording (7, 8) Chris Bell – recording (6, 9) Sean Davis – recording (6, 9) Cha Cha Jones – recording (6, 9) Ray Murray – recording (6, 9) Jimi Randolph – recording (6, 9, 12) Darren Henson – recording (10) Keith Pelzer – recording (10) Serban Ghenea – mixing (10) Chris Wood – recording (12) Dave Pensado – mixing (12) James Tanksley – assistant engineer (5, 7, 8) Chris Lowry – recording assistant (6) Alex Reverberi – recording assistant (6, 9) Tim Wentzlaff – assistant engineer (7) Nicolas Fournier – mix assistant (6, 9) John Hanes – mix assistant (10) Mary Ann Souza – assistant engineer (12)
```

## Album 111: The Way It Is — Bruce Hornsby and the Range

- **album_id:** `64f3faa9-2cdf-40ed-8bc3-fd7677a6bec7`
- **Tags (identification only):** rock, pop, soft rock
- **Chunks:** 3 (713 words)

### Album 111, chunk 1

```text
The Way It Is is the debut album by Bruce Hornsby and the Range, released by RCA Records in 1986. Led by its hit title track, the album achieved multi-platinum status and contributed to the group winning the Grammy Award for Best New Artist. Other notable tracks from the album include "Mandolin Rain" and "Every Little Kiss". Huey Lewis appears on harmonica and provides vocals on "Down the Road Tonight." Lewis also co-produced this track, along with "The Long Race" and "The River Runs Low." Bruce Hornsby formed The Range in 1984 while in Los Angeles, having previously spent time as a session musician for Sheena Easton and a songwriter for 20th Century Studios' music publishing company. The band sent a series of demo tapes to various record companies, initially with no success. Huey Lewis, who had befriended Hornsby a few years prior to the creation of The Range, advocated on Hornsby's behalf by encouraging record labels to sign the band. Windham Hill Records offered to sign Hornsby after he sent them a four-song demo tape that included "The Way It Is". The tape then leaked to other record labels, who then also expressed interest in signing the artist. Hornsby's lawyer encouraged him to submit the tape to a few other labels, although Hornsby was initially hesitant as he was tired of being rejected. Hornsby ultimately declined to sign with Windham Hill Records over his belief that they were not interested in the rock music that The Range's offered. He
```

### Album 111, chunk 2

```text
instead going with RCA Records, saying that "with RCA, I was able to make the total record I wanted to make. They were interested in all of me, not just one side." Some of the material written for The Way It Is related to Hornsby's home state of Virginia. The 'roadside shack' referenced in "Down the Road Tonight" related to a location near Williamsburg, Virginia. "The Wild Frontier" relates to Hornsby's desire to escape from Los Angeles and return to Virginia. He explained that "L.A. is okay but not great. I just have an overall feeling of 'Well, this place really isn't for me...I don't think anybody out there really likes breathing the air or dealing with the traffic. That's where I live, but Virginia is my home." Hornsby found the recording process for The Way It Is to be a departure from the session work he had previously done in Los Angeles based on the additional responsibilities associated with making a solo album, including decisions relating to mixing and mastering. The original release of the album featured an impressionistic photograph on the cover of Bruce Hornsby playing an accordion. It was initially aimed at the New Age music market and included slightly different versions of the songs "Down the Road Tonight" and "The River Runs Low." As the album's tracks began to receive regular airplay on pop music stations in late 1986, it was remixed and subsequently re-released on December 20, 1986, with a new sepia-toned cover featuring a
```

### Album 111, chunk 3

```text
photograph of the band superimposed over an image of the Chesapeake Bay Bridge–Tunnel in Virginia. In their review of The Way It Is, Billboard said that its songs "recall the melodic flow and western imagery that reached a peak with the Eagles", adding that the music "laces these elements with a canny mix of acoustic and electric accents." Bruce Hornsby – vocals, grand piano, synthesizer, hammered dulcimer, accordion David Mansfield – guitar, mandolin, violin George Marinelli – acoustic guitar, electric guitar, backing vocals Joe Puerta – bass, backing vocals John Molo – drums, percussion Huey Lewis – harmonica, backing vocals on "Down the Road Tonight" John Gilutin and Sean Hopper – synthesizer consultants Jeff Gerson – enforcement Paul Atkinson – executive producer Bruce Hornsby – producer (1–3, 5, 7, 9) Elliot Scheiner (for Trackman, Inc.) – producer (1–3, 5, 7, 9) Huey Lewis – producer (4, 6, 8) Ivy Skoff – production assistant Marge Meoli – A&R coordinator Kathy Hornsby – art consultant Tim Neece – management Stephen Marcussen – mastering at Precision Lacquer (Hollywood, California) Bob Harlan – digital editing Elliot Scheiner – tracking engineer (1–3, 5, 7, 9), mixing Jim Gaines – tracking engineer (4, 6, 8) Eddie King – mixing, additional engineer David Luke – mixing Don Smith – mixing
```

## Album 112: Mail on Sunday — Flo Rida

- **album_id:** `e527eea8-efd0-42e2-8694-bd249cf006d3`
- **Tags (identification only):** hip hop, pop rap, contemporary r and b, dance pop, southern hip hop, thug rap, rap and hip hop
- **Chunks:** 3 (702 words)

### Album 112, chunk 1

```text
Mail on Sunday is the debut studio album by American rapper Flo Rida, and was released on March 18, 2008 under Atlantic, and Poe Boy Entertainment, serving as Flo Rida's follow-up to his 2007 mixtape Mr Birthday Man. It spawned three singles; the first, "Low" was number one on the U.S. Billboard Hot 100 for 10 weeks. The second, and third singles, "Elevator", and "In the Ayer", were successful as well, being top 20 hits. "Roll" featuring Sean Kingston was not an official single, but it managed to peak at number 59 on the US Billboard Hot 100, and number 43 on the Canadian Hot 100 due to digital sales in both countries. T-Pain, who laced the first single, is only one of the many featured guests throughout the album. Timbaland, who produced the second single "Elevator", is also featured on the track. Rick Ross, and Trey Songz made appearances as well. Lil Wayne has also been added to the list with assistance by young Memphian, Jamil Smith, while Sean Kingston appears on the J. R. Rotem-produced "Roll" the concept was created, and co-written by Compton rapper Spitfiya, from The Bullets Production Team, Various other guests include Birdman, Brisco. The third single is "In the Ayer" featuring will.i.am. The fourth single was scheduled to be "Money Right" featuring Brisco, and Rick Ross, but was canceled due to the release of his upcoming second studio album R.O.O.T.S. His second collaboration with T-Pain, "I Bet", his collaboration with Trina, named "Bout It"
```

### Album 112, chunk 2

```text
and as well as his second collaboration with Sean Kingston named "OG", all three didn't make the final track list, but were recorded. As for production, J. R. Rotem, DJ Montay, and Timbaland all provided tracks for Mail on Sunday, among others. Mail on Sunday garnered mixed reviews from music critics. At Metacritic, which assigns a normalized rating out of 100 to reviews from mainstream critics, the album received an average score of 54, based on 12 reviews. Steve 'Flash' Juon of RapReviews praised the album for containing great production and tracks that are potential singles but found the artist on said album lacking in identity, concluding with, "When you try to come up with positive comparisons to other artists, you realize just how derivative Flo Rida is. He's a little bit Twista, a little bit Trick Daddy, and a whole lot Nelly. None of those things are negative, but the fact he can't distinguish himself from any of them isn't a positive. I'd like to see Flo Rida convince me why he's special with his next album - until then he's just another MC with a well produced album who came out of a cookie cutter hitmaking mold." Joseph Barracato of Entertainment Weekly also praised the production for having "ferocious beats" and "infectious hooks," and gave credit to Flo Rida for delivering female anatomy metaphors in a creative way. Billboard writer Jeff Vrabel said that, "Flo Rida's flow is an engaging/ringy-dingy/he-sounds-like-Nelly thing. But his hooks can be rock-solid ("Ack
```

### Album 112, chunk 3

```text
Like You Know") and his interest in gleaming synthesizerism (opener "American Superstar" comes into "Tubular Bells" territory, really) helps set him off from the legions of rappers clawing over each other to break out of the South." AllMusic's Andy Kellman said that, "Though Flo Rida has his own identity – for all the tough talk and the automotives fixation, he does come off as big-hearted, and he could just as easily make an R&B album – and covers more bases than what is typical from other mainstream-yet-street rap albums of 2007 and 2008, he's not nearly as distinctive as any of his predecessors." Robert Christgau graded the album as a "dud", indicating "a bad record whose details rarely merit further thought." Rolling Stone's Christian Hoard found the album trying hard to replicate the success of "Low" but found the tracks to be "generic pop rap" and both the production and vocal delivery "standard-issue." Wilson McBee of Slant Magazine criticized the record's tired use of party tracks, phoned in contributions, and misogynistic lyrical content, concluding that "unless he can once again catch the coattails of T-Pain or some other hit-magnet, odds are that he’ll be beginning his descent back into anonymity very soon."
```

## Album 113: Home From Home — Millencolin

- **album_id:** `c81fb83e-e503-4c38-b150-47b1ce05d4be`
- **Tags (identification only):** alternative rock, pop punk, hard rock, punk, punk rock, rock, sweden, swedish
- **Chunks:** 2 (493 words)

### Album 113, chunk 1

```text
Home from Home is the fifth album by Swedish punk band Millencolin, released on 12 March 2002 by Epitaph Records. The songs "Kemp", "Man or Mouse", and "Battery Check" were each released as singles with accompanying music videos. In April 2001, Millencolin were reportedly writing and rehearsing new material in their hometown Örebro, Sweden, in anticipation of recording their next album with Mark Trombino. Home from Home was instead recorded with producer Lou Giordano at Little Big Room Studios in Haninge, Sweden between 15 September and 17 October 2001. Giordano also acted as engineer, with assistance from Mats Lindfors, Fredrik Andersson, and Ernie. Giordano mixed the recordings over the course of two weeks, before they were mastered by Peter In de Betou at Cutting Room. On 5 December 2001, Home from Home was announced for released in early 2002. Six days later, the album's track listing was revealed. "Man or Mouse" was posted on the band's website on 4 January 2002. "Kemp" was released as a single on 23 January 2001. On 2 February 2001, "Fingers Crossed" was made available for download after playing a game on the band's website. In February and March 2002, the band toured across Australia and New Zealand. On 7 March 2002, the music video for "Kemp" was posted online; it was animated by Kalle Haglund, the former vocalist of Voice of a Generation. Home from Home was released on 11 March 2002 in Europe through Burning Heart, and the following day in the US
```

### Album 113, chunk 2

```text
through Epitaph. While on tour in the US, drummer Fredrik Larzon injured his elbow, which required him to fly back to Sweden for surgery; he was temporarily replaced by Thomas Falk of Bombshell Rocks. In April and May 2002, the band toured across Europe with the Donots and Anti-Flag. Their substitute drummer Kjell Ramstedt of No Fun at All became ill, resulting in the cancellation a show; the show prior to that, Ramstedt had fainted, which caused the band's set to be shorted. Larzon's injury had healed, with him returning to the band in time for an appearance at Ozzfest. Millencolin was due tour the UK in December, with Brand New; however, the tour was cancelled. In April and May 2003, the group embarked on a west coast and then east coast treks of the US. The former was supported by Rufio and River City High (who left partway through the tour and were replaced by Ten Foot Pole), while the latter was planned to be supported by American Hi-Fi and the Unseen. Prior to the start of the east coast leg, the tour was cancelled due to family issues. It was revealed shortly afterwards that the cancellation was a result of frontman Nikola Šarčević's brother having gone missing. The band subsequently rescheduled the east coast shows to November 2003, which were supported by Senses Fail; Wakefield was also due to support, but because of recording conflicts they were replaced by Matchbook Romance.
```

## Album 114: Deadline — Leftöver Crack

- **album_id:** `c0ea6930-a28a-4e1b-9069-c29f217ec55d`
- **Tags (identification only):** punk, punk rock, anarcho punk, crack rock steady, pop punk, rock, ska, ska punk
- **Chunks:** 1 (270 words)

### Album 114, chunk 1

```text
Deadline is a split album released in 2007 on Alternative Tentacles Records and Fat Wreck Chords. The album features 15 songs from the 2 bands, Leftöver Crack and Citizen Fish. Each band covers two songs. Citizen Fish covers "Money" by Choking Victim, and "Clear Channel (Fuck Off!)" by Leftöver Crack. Leftöver Crack covers "Supermarket Song" by Citizen Fish, and "Reasons for Existence" by The Subhumans. This album has cameos from Dave Dictor from MDC on the Intro song for the Leftöver Crack portion of the record, and vocals from Jello Biafra on Leftöver Crack's "Baby-Punchers". Allmusic writer Corey Apar gave the album four stars, stating "The bleeding urgency that both bands discharge with such directed force and street-level ferocity is truly refreshing...Deadline is surprisingly still incredibly accessible and even poppy." Chris Moran of Punknews.org gave it three and a half stars, calling it "a pleasant piece of punk history". Ty Trumbull, writing foe Exclaim!, viewed it as "a good example of what a split record should be: two bands that, while not completely dissimilar, each bring something different to the table." Andrew Miller for Alternative Press, awarded it three stars, stating that the album "confirms the genre's continued vitality and vigilance". Naren Rauch Atomic – Engineer, Assistant Jello Biafra – Vocals on Baby-Punchers Alec Crack "Shit Boat" – Bass Ara Crack "Slacka" – Drums Scott Sturgeon "Stza" – Guitar, Keyboards, Vocals, Producer, Mixing Dave "Knucklehead" Dictor – Vocals on L.Ö.C Intro (B.D.C) Kristen Ferrell – Logo Jasper – Bass, Vocals, Artwork Ezra Kire "Way Way" – Guitar, Keyboards, Vocals Brad Logan – Guitar, Vocals Jamie McMann – Producer, Engineer, Mixing
```

## Album 115: Everything Was Beautiful — Spiritualized

- **album_id:** `bc16c7b2-cb95-4d15-b828-d30d4c61cd63`
- **Tags (identification only):** rock, space rock, 1–4 wochen, english, laut.de, offizielle charts, ph temp checken, plattentests.de
- **Chunks:** 3 (645 words)

### Album 115, chunk 1

```text
Everything Was Beautiful is the ninth studio album by Spiritualized, released under Fat Possum Records on April 22, 2022. The album contains influences from psychedelic music, gospel music, and classic rock. The content of Everything Was Beautiful was taken from the same demo sessions as and serves as a companion piece to the band's previous album, And Nothing Hurt. Put together, both album titles form the quote "Everything Was Beautiful and Nothing Hurt", taken from the 1969 novel Slaughterhouse-Five by Kurt Vonnegut. The album's lead vocalist, Jason Pierce, played 16 different instruments during the album. The album's first single and music video, "Always Together with You", was released on 2 November 2021; the album's second single and music video, "Crazy", was released on 10 January 2022; the album's third and final single and music video, "The Mainline Song", was released on 7 March 2022. On the review aggregate site Metacritic, Everything Was Beautiful earned a rating of 83 out of 100, based on 23 reviews, indicating "universal acclaim". Aggregator AnyDecentMusic? gave it 8.2 out of 10, based on their assessment of the critical consensus and ranked it the 18th best album of 2022. The album received 4/5 stars from the Observer and 4/5 from the NME. Ben Cardew of Pitchfork gave the album a 7.8/10 and described the album "like meeting an old friend and finding new shared memories." Caleb Campbell writing for Under the Radar gave the album a 9/10 while claiming that there is "immensely evident craftsmanship that
```

### Album 115, chunk 2

```text
runs through the album". AllMusic reviewer Fred Thomas described the album as a "delirious and exciting, a perfect distilment of the best parts of the band's various phases that feels reinvigorated and new" and gave the album a 4.5/5. Writing for The Line of Best Fit, John Amen gave the album 9/10 and concluded, "Everything Was Beautiful shows Spiritualized accessing yet another artistic plateau, forging an exemplary hybridization of unshakeable songs and sublimely assembled music." In Relix, Justin Jacobs notes that Spaceman relies on "many of his old tricks, but the music still comes out sounding fresh and colorful" and writes that "his heady sound feels more vital than ever". J Spaceman – Fender Thinline guitar, Fender Jazzmaster guitar, Gibson L-00 acoustic guitar, Fender Bass VI, Burns Sonic bass, Gibson Firebird III guitar, Farfisa Compact organ, Vox Continental guitar, Roland Juno-60 keyboard, Moog, Radio Shack 100, harmonica and bass harmonica, glockenspiel, melodica, piano Tony Foster – Gibson Black Beauty guitar, Fender Jazzmaster guitar, harmonica, Rickenbacker lap steel, Epiphone Batwing guitar James Stelfox – Fender Precision bass, Fender Jazz bass, Fender Bass VI, Burns Sonic bass, Epiphone violin bass John Coxon – Gibson Firebird guitar, Vicente Sanchis Spanish guitar, Fender Telecaster guitar Tom Edwards – percussion, timpani, vibraphone, glockenspiel, marimba, orchestral bass drum Lee Horsley – Hammond organ, piano, Vox Continental guitar, Fender Rhodes electric piano, Farfisa Compact organ Kevin Bales – Gretsch Round Badge drums and percussion Kid Millions (John Colpitts) – drums on original recording of "Best Thing You
```

### Album 115, chunk 3

```text
Never Had (The D Song)" Brad Truax – bass on original recording of "Best Thing You Never Had (The D Song)" Alan Wilkinson – tenor and baritone saxophones Alex Ward – clarinet, alto saxophone Kevin Brown – soprano and alto saxophones Kevin Cunningham – trumpet Stuart Haugh – trombone Jim Walker – violin Diamond White – violin James Cocker – viola Arnold Parks – cello Melvyn Duffy - pedal steel Jason Hart – pedal steel David Wrench – Moog One 16 Voice analog synthesizer Nikki Lane – vocals on "Crazy" Dex Chilcott – backing vocals on "Crazy" Daniel Thomas, Lena Wright, Wendi Rose, Travis Cole – singers Alex Lamay, Adam Langston – strings and horns Iris Mathieson – ukulele Poppy Spaceman – vocals on "Always Together With You" David Wrench and J Spaceman – mixing Dan Cox and J Spaceman – additional production and editing
```

## Album 116: Construct — Dark Tranquillity

- **album_id:** `8050cf50-332b-4d2a-9602-5882043f3fd7`
- **Tags (identification only):** melodic death metal
- **Chunks:** 5 (1065 words)

### Album 116, chunk 1

```text
Construct is the tenth studio album by Swedish melodic death metal band Dark Tranquillity. It was released on 27 May 2013 through Century Media Records. A music video for "Uniformity", directed by Patric Ullaeus, was released on 10 May 2013. The album was written during what the band described as their "darkest period" and drew critical praise for its melodrama and darkness. Construct would be the band's last studio album with founding member guitarist Martin Henriksson as he left the band in early 2016 due to loss of passion for playing music. At 42 minutes, Construct is Dark Tranquillity's shortest studio album to date. Prior to recording the music for Construct, bassist Daniel Antonsson departed on amicable terms and guitarist Martin Henriksson (who originally played bass for Dark Tranquillity before switching to guitars beginning with Projector in 1999) filled in for the recording session. Mikael Stanne described Antonsson as "a great guy and an awesome musician" but acknowledged that he was not "on the same page" as the rest of the band due to his desire to be "like a band leader. He wants to be the one in charge, but there's no way to be in charge in our band [as] we're all democratic and close to each other after playing together for so long". Two songs, "Sorrow's Architect" and "A Memory Construct", were recorded during the making of this album, but were instead released on the "A Memory Construct" limited tour single. Stanne noted from where both the
```

### Album 116, chunk 2

```text
lyrical themes and the album title originated: [T]he stuff that angers me the most[, which is] the narrow-mindedness and biased will to not see things as they are...I wish we could be more honest with ourselves and see things more clearly and be more rational...Over the years I've gotten more upset about this and that got me thinking about what motivates and drives us to believe the things we believe. The big theme is the ultimate construct of religion and faith. The title is Construct in a most negative way: this shield or excuse we have to do the things we do. In another interview, Stanne said "I want people to be sceptical and be able to think for themselves. The herd type of behaviour of many I find quite disturbing...I like people to be pure and unbiased and free any preconceptions when they encounter other people. The utter ignorance and bigotry of some people really gets to me". Niklas Sundin elaborated that "Our brains have evolved to find patterns and connections where there are none, but – as they say – extraordinary claims require extraordinary evidence. I rarely want to talk about non-musical stuff in interviews, but as a science buff and skeptic I have to take the opportunity to recommend every UFO or conspiracy theorist to read Carl Sagan's The Demon Haunted World". The songwriting process departed from Dark Tranquillity's typical method. Henriksson reduced his role in arranging the songs, while keyboardist Martin Brandstrom, guitarist Niklas Sundin, and
```

### Album 116, chunk 3

```text
drummer Anders Jivarp served as the principal songwriting team. Stanne commented about this method: [It] was totally different from what we normally do...It was an experiment at first, but then it turned into this really creative thing. We were all really excited. We could talk and be more objective about the songs and what they needed and what the album should be like. It was so liberating. Finally, we could make music and not argue about it too much. It was a very positive experience. Stanne attributed the album's sharp departure from previous albums to the band's struggle with "writer's block" and the alternate songwriting configuration that eventually enabled the band to create the new album: "The material we had was pretty emotional. It was written during this period where we were struggling...Most of the material was emotional and sad and heavy. That's what the album became. The stuff we wrote during our darkest period was put together in the most creative way we had done in many years." Their previous album, We Are the Void had not been as positively received as their previous albums, and the group had experienced troubles in the creation of the album, such as in-fighting. The band commented on the style of the album, saying, "While still bearing the unmistakable mark of the Dark Tranquillity, the record is probably our most different and diverse offering since 1999's Projector". Mikael Stanne described the album as being both "melody driven" and a "reaction" to the band's
```

### Album 116, chunk 4

```text
recent work. Chad Bowar of About.com noted "the darkness and sadness in the composition of many of the songs", which he attributed to the more collaborative songwriting approach. However, Sundin stated in an interview that "Most likely, the upcoming 500 years will be a patchwork of great tragedy and suffering as well as major advance and improvement, just like the past 500 years have been. But metal lyrics are often about polarizing. You don't sing about being mildly skeptical of a certain amount of people behaving in a slightly disagreeable way and that you would prefer if they please could consider changing their behavior. You sing about throwing the whole of humanity in a sea of fire and brimstone and laughing while doing it". Describing the band as "legendary", Chad Bowar of About.com remarked, "it's no surprise that Dark Tranquillity has delivered another quality album with Construct. It's one of their most creative and diverse releases in quite a few years." James Christopher Monger of Allmusic noted that the album pulled back on the intensity in favour of an approach that "retains the chilly elegance of the band's best work while dialing back on the more punishing aspects, resulting in an expansive, world-weary, and windswept racket". Kyle Ward of Sputnikmusic compared Construct with the band's 1999 album Projector, due to the character of the experimentation, and praised the album's atmosphere as "the most palpable and poignant of their entire discography, due in large part to its focus on dark, melodramatic
```

### Album 116, chunk 5

```text
tones in the synths and the swift, tight melodies that make up the guitar leads". On 15 June 2013 the album entered the US Billboard 200 chart at number 171. Mikael Stanne – vocals Niklas Sundin – lead guitar; album artwork Martin Henriksson – rhythm guitar; bass guitar, music composition (2, & 4) Martin Brändström – keyboard Anders Jivarp – drums Jens Bogren – mixing
```

## Album 117: X — INXS

- **album_id:** `d2d5128c-fe66-4e9a-8c8f-f3d5892d3e69`
- **Tags (identification only):** pop rock, rock, electronic, pop, alt rock, college rock, dance rock
- **Chunks:** 7 (1751 words)

### Album 117, chunk 1

```text
X is the seventh studio album by Australian rock band INXS, released on 25 September 1990 through WEA in Australia, Mercury Records in Europe, and Atlantic Records in the United States and Canada. The follow-up to the massive seller Kick, X scored hits with "Suicide Blonde" and "Disappear" (both Top 10 in the US). Both singles were later used in the soundtrack to the 1991 American teen comedy Mystery Date. Two other singles from X were "Bitter Tears" and "By My Side" but they had less chart success. A fifth single, "The Stairs", was only issued in the Netherlands to coincide with the release of the Live Baby Live album. X was the third consecutive INXS album produced by Chris Thomas. The title, the Roman numeral for "10", represents the band's tenth year since their debut album was released in 1980. X features a sample of blues-harp player Charlie Musselwhite on "Suicide Blonde", and Musselwhite himself playing on "Who Pays the Price" and "On My Way". In 2002, a remastered version of the album was released, which included five previously unreleased tracks. INXS gained great success with the release of their previous studio album, Kick. The multimillion-selling album received critical acclaim and proved to be the band's biggest selling album by far, having gone platinum multiple times. In 1987 and 1988, INXS toured heavily in support of Kick. During 1989, the band took a break to work on side projects. Vocalist and primary songwriter Michael Hutchence collaborated with Ian 'Ollie'
```

### Album 117, chunk 2

```text
Olsen in the band Max Q, the two having previously worked together on Richard Lowenstein's film Dogs in Space. The remaining members of INXS also got involved in other musical projects, including songwriter and multi-instrumentalist Andrew Farriss, who joined singer-songwriter Jenny Morris in the studio to produce her second solo album, Shiver. Bass guitarist Gary Garry Beers collaborated with ARIA award-winning Sydney band Absent Friends during 1989. Beers first toured with the group, and later recorded tracks for their debut album, Here's Looking Up Your Address. Drummer Jon Farriss joined the recording sessions, contributing percussion on one track. Guitarist and saxophonist Kirk Pengilly, along with lead guitarist Tim Farriss, both paired up to help produce an album for local Sydney band, Crash Politics. Upon entering the 1990s, INXS wanted to follow up on Kick, their multimillion-selling international success. In a radio interview shortly after the release of X, Hutchence said, "We had to follow-up (on Kick) otherwise we'd disappear". The band worked again with producer Chris Thomas at the new Rhinoceros studio in Sydney, Australia. Regarding the new studio, Thomas felt that it imposed a different feeling on the band's sound, which reflected in the album's material. In a 2002 interview, Thomas commented, "We worked at the new Rhinoceros studio, which was ridiculously enormous. To some degree, it forced isolation on everything, including the control room. To get a vibe on playback, you had to turn everything up really loud because the room was so big". Most of the material
```

### Album 117, chunk 3

```text
for X was written by the songwriting duo of Andrew Farriss and Michael Hutchence with the exception of "Disappear", "Faith in Each Other" and "Deepest Red" (excluded from the album), which were written by Hutchence and Jon Farriss, whereas "By My Side" was a collaboration between Andrew and Kirk Pengilly. According to the album's liner notes, Thomas assisted in arranging the song's composition, specifically the chorus; the song's original demo, under the title "Dark of Night", with alternate lyrics was released on the album's 2002 remaster. Some songs that appear on the album were in fact written years prior, including "Lately" and "Disappear" - the lyrics for "Lately" were originally written by Andrew during the recording sessions of the group's fifth studio album, Listen Like Thieves, while Hutchence and Jon wrote the lyrics for "Disappear" when they were living in Hong Kong in 1989. An idea that Andrew suggested to Hutchence and the rest of the band was the sound of a Blues harp. After discovering Blues musician Charlie Musselwhite had been touring Australia, the band met with him and decided to use his harmonica playing talent on the album. For "Suicide Blonde", the band used samples of Musslewhite's playing rather than recording with the band in the studio; he does play traditional harmonica on "Who Pays the Price" and "On My Way". Like the band's two previous studio albums produced by Thomas, X features a slickness and polish in its production, a quality that was removed during production of
```

### Album 117, chunk 4

```text
subsequent albums. It was also the group's last studio album produced by Thomas. Their next collaboration was four years later on the recording of both "The Strangest Party (These Are the Times)" and "Deliver Me", which were two new songs that appeared on the band's Greatest Hits compilation released in 1994. Sticking to the formula that was built on Kick, Thomas urged primary songwriters Andrew Farriss and Hutchence to condense their song writing strengths on X. According to the liner notes on the album's 2002 remaster, Thomas stated, "Everything about INXS this time around was grandiose, and this was reflected in the material". He added, "The album got away from the funky stuff and was moving towards the epic on tracks like "Lately" and "The Stairs". Paul Evans of Rolling Stone summed up the changes with "[INXS] focus their strengths, coming up not only with tough, state-of-the-art pop but with the casual confidence of a mature collective personality". Regarding the recorded material, Evans observed that "the record blends R&B; and rock as INXS always has done – but this time the grooves are more solid, the energy and moods less disparate". Similar to the themes that were explored on Kick, X continues to reflect on the band's personal experiences about relationships and daily life, while touching on social topics such as media, fame and society. The title and lyrics to "Suicide Blonde" came from a phrase that Hutchence first heard used by his then-girlfriend Kylie Minogue, while "Disappear" describes how
```

### Album 117, chunk 5

```text
[Hutchence] is flushed with anxiety when he sees what's going on in the world, but all those problems and fears are cast aside when he's with the one he loves. Hutchence asserted that "The Stairs", a song about singular city life, was the most ambitious song he had ever written; the song describes how tens of millions lead daily lives separated by walls mere inches apart yet never meet. Andrew was inspired to write "By My Side" for his wife, Shelly, and said that the song is about "missing family and people while being on the road". Regarding the lyrics to "Hear That Sound", Hutchence commented, "it is about the power of people, more particularly in large crowds or in marches for the purpose of peaceful protest or celebration". While reviews for X were generally favourable, with some critics commenting that INXS had stepped up their game, others felt that the album followed too much in the same formula as Kick. AllMusic's Steven McDonald mentions this in the beginning of his review, stating "The seventh album from Australia's INXS basically sticks to the formula set up on Kick, mixing solid remixable dance floor beats with slightly quirky production tricks, Michael Hutchence's rough-edged, bluesy vocals, and some good solid song hooks". In his 1990 review for Rolling Stone, music critic Paul Evans rated the album four stars out of five and called X the band's "best and most cohesive album". He added, "X is greater than the sum of its parts.
```

### Album 117, chunk 6

```text
It defines the band and clarifies the fullness of its appeal". Double J (radio station) Their 50 Best Australian albums of the 90's, they included X at #45." Q (magazine) "Wrote" - 3 Stars - Good - listed X in their 50 best albums of 1990." Record Mirror's Robin Smith initiated that the album, isnt't all raunchy rock - not by a long chalk. 'Disappear' and 'The Stairs' shimmer into view, both trim tunes with understated yet memorable choruses and mellow ideas, the disc was given a 5 out of 5 "Perfect Rating" Radio X (United Kingdom) Placed X at #19, on their list of the 25 best indie albums of 1990." Smash Hits Marc Andrews, called the album "Pretty Good" giving it a 7 out of 10 on the rating scale." Spin (magazine)'s Al Shipley also Put X in his list of the 30 Great Albums of 1990, That Deserve Their Own 30th Anniversary Pieces." Even though the album and its singles did not exceed the success of Kick, it did perform well worldwide, particularly in Europe; In the United Kingdom, the album peaked at number 2 on the UK Albums Chart. In total, it remained in the UK charts for an impressive 44 weeks. The album was certified platinum in January 1991 by the British Phonographic Industry (BPI) for sales in excess of 300,000 copies. X proved successful across Europe, reaching number 5 in Switzerland, number 7 in France, number 9 in (Germany), number 10 in Sweden and
```

### Album 117, chunk 7

```text
number 13 in Norway. The album quickly received gold accreditations in all these regions, subsequently attaining platinum status in both France and Switzerland. In the band's native Australia, X entered at number 1 on the Australian Albums Chart on 21 October 1990, remaining at the top spot for two weeks. It was present for a total of 34 weeks on the chart. In New Zealand, the album peaked at number 2 on the RIANZ Chart, staying on the chart for 23 weeks. X was certified double platinum by the Australian Recording Industry Association (ARIA) and platinum by the Recording Industry Association of New Zealand (RIANZ) for shipments of 140,000 and 15,000 units respectively. In the United States, X peaked at number 5 on the Billboard Top 200 on 20 October 1990. Similar to the United Kingdom, the album spent a total of 43 weeks in the charts. Less than two months after its release, X was certified gold by the Recording Industry Association of America (RIAA) on 13 November 1990 for shipments of 500,000 units. The album became double platinum on 16 December 1997 for sales of two million copies in the United States. X was also certified double platinum in Canada in February 1991 for shipments of 200,000 units. Michael Hutchence – vocals Andrew Farriss – keyboards, guitars Tim Farriss – guitars Garry Gary Beers – bass Jon Farriss – drums, keyboards, programming Kirk Pengilly – guitars, saxophone, vocals, programming Charlie Musselwhite – harmonica (7, 10) Chris Thomas – producer
```

## Album 118: 10 000 Hz Legend — Air

- **album_id:** `367e620b-3d3d-4fe5-aef8-07b527a4270e`
- **Tags (identification only):** electronic, downtempo, leftfield, ambient pop, electronica, alternative/indie rock, club, experimental
- **Chunks:** 1 (213 words)

### Album 118, chunk 1

```text
10 000 Hz Legend is the second studio album by French electronic music duo Air, released in France on 28 May 2001 by Virgin Records and in the United States on 29 May 2001 by Astralwerks. On this album, tracks are longer and more electronic-oriented than on their previous records. These experimentations find the duo expanding their capacities and working with other artists including Beck and suGar Yoshinaga of Buffalo Daughter. The album artwork was produced by Ito Morabito. It features Monument Valley, located on the Arizona–Utah border. 10 000 Hz Legend received generally less favourable reviews from critics than had their previous albums; however, Q listed 10 000 Hz Legend as one of the 50 best albums of 2001. Most reviewers were dissatisfied on the group's departure from the sound of 1998's Moon Safari, although the soundtrack album The Virgin Suicides (2000) had a similar mood and sound. The American music website Stereogum takes its name from the lyrics of the song "Radio #1". Air – recording, production Pascal Garnon – drum recording Bruce Keen – sound engineering, editing Tony Hoffer – additional production, editing, mixing Julien Delfaud – mixing assistance Stéphane Elfassi – executive production Marc Teissier du Cros – executive production Abake – Air logo, layout Ora-Ïto – concept, design
```

## Album 119: Antidotes — Foals

- **album_id:** `35a2d9b4-ecfb-4adf-add3-6e5b75226b67`
- **Tags (identification only):** indie rock, math rock, rock, dance punk, post punk
- **Chunks:** 2 (372 words)

### Album 119, chunk 1

```text
Antidotes is the debut studio album by British indie rock band Foals. It was released on 24 March 2008 in the United Kingdom on Transgressive Records, and on 8 April 2008 in the United States through Sub Pop. The album's themes are varied and cryptic, but are generally melancholic and focused on relationships. They are exemplified by the four singles: "Balloons", "Cassius", "Red Socks Pugie", and "Olympic Airways". The album was recorded in Stay Gold Studios Brooklyn in summer 2007, and was produced by TV on the Radio's Dave Sitek. However, Foals remixed Antidotes in London, complaining that he made it sound like it was "recorded in the Grand Canyon." However, in an interview with MusFlashTV, Foals' drummer Jack Bevan said, "Our producer, David Sitek was great because he didn't interfere in the actual recording progress. We kind of engineered it so that we would get the tracks down, get all of the sort of essential parts down and then, halfway through the recording he kind of came in, and when we were doing overdubs and that kind of thing, he sort of started to assist us with making it sort of fill out." Yannis added "All the sounds were there, and he added a depth. He messed with the spaces around the sounds so there's this weird ambience on all the tracks." The tracking of the parts was unorthodox in many ways ranging from drums recorded in alleyways on cassette tape recorders and then reprocessed through outboard gear to
```

### Album 119, chunk 2

```text
vocals being sung while moving round the room and brass performed by members of Antibalas Afrobeat Orchestra directed to not play directly into the microphones. It peaked at number three in the UK Albums Chart. In the US, it reached a high of number 28 on the Top Heatseekers chart, but failed to chart on the Billboard 200. According to Metacritic, the album received "generally favourable reviews" from critics. Yannis Philippakis – vocals, guitar, drums Jack Bevan – drums Jimmy Smith – guitar Walter Gervers – bass, backing vocals Edwin Congreave – keyboard, backing vocals Stuart Bogie – saxophone Aaron Johnson – trombone Eric Biondo – trumpet Mike Crossey – mixing David Andrew Sitek – producer L. Hris Moore – recording assistant
```

## Album 120: The Christmas Spirit — Johnny Cash

- **album_id:** `a30d541f-f431-4104-86bc-cbc1397d1bdf`
- **Tags (identification only):** ballad, christmas music, country, holiday, americana, christmas, rock and roll, rockabilly
- **Chunks:** 1 (109 words)

### Album 120, chunk 1

```text
The Christmas Spirit is the first Christmas album and tenth album by country singer Johnny Cash, released on Columbia Records in November 1963. It contains four original Christmas songs written by Cash and eight tracks originally written by other artists, including "Blue Christmas" (at this point best known through the version recorded by Cash's former Sun Records labelmate Elvis Presley), "Silent Night" and "Little Drummer Boy". Johnny Cash - vocals, guitar Luther Perkins, Grady Martin, Jack Clement - guitar Marshall Grant - bass W.S. Holland, Buddy Harman - drums Hargus "Pig" Robbins, Bill Pursell - organ, piano Maybelle Carter - autoharp Anita Kerr - organ Bob Johnson - flute
```

## Album 121: Dream Theater — Dream Theater

- **album_id:** `49bcd249-c807-4747-b594-f9b19d134770`
- **Tags (identification only):** progressive metal, rock, 10s, heavy metal
- **Chunks:** 7 (1578 words)

### Album 121, chunk 1

```text
Dream Theater is the twelfth studio album by American progressive metal band Dream Theater, released worldwide in September 2013, through Roadrunner Records. The album was written, recorded, mixed, and mastered between January and May 2013 at Cove City Sound Studios in Long Island, New York, the same studio as the band's previous album, A Dramatic Turn of Events (2011). It is the first Dream Theater album to include drummer Mike Mangini in the songwriting process. The band made the album Dream Theater to emphasize that they were moving forward in their career and to make it a reference point for fans. The album's songs are shorter on average than most Dream Theater songs, with the exception of the 22-minute closer, "Illumination Theory". Some songs utilize organic strings, which were arranged by Eren Başbuğ, a Berklee College of Music student. The album features two instrumentals, "False Awakening Suite" and "Enigma Machine", which were the first instrumentals that the band had written for a studio album since Train of Thought (2003). Many of the album's lyrics were motivated by real-life events, such as the Boston Marathon bombings. Dream Theater moved 34,000 units in the United States during its debut week, charting at number seven and becoming the band's second highest-charting album behind 2009's Black Clouds & Silver Linings. For its lead single, "The Enemy Inside", the band received their second consecutive Grammy nomination in the Best Hard Rock/Metal Performance category. In early 2014, Dream Theater toured Europe and America in support of
```

### Album 121, chunk 2

```text
the album, and recorded their performance at the Boston Opera House for a live release. Preliminary writing for Dream Theater's twelfth album commenced on the A Dramatic Turn of Events Tour in April 2012. During soundchecks, the band would jam and record their ideas, and guitarist John Petrucci would try out independently composed material. They did not enter the recording studio until January 2013, returning to Cove City Sound Studios in Glen Cove, New York, where they recorded their previous album, A Dramatic Turn of Events (2011). The first song that the band wrote was "Surrender to Reason", which bassist John Myung credited with setting the pace for the remainder of writing. From the start of the creative process, drummer Mike Mangini contributed as a writer, unlike for A Dramatic Turn of Events, where Petrucci programmed the main drum parts during writing and Mangini recorded his own interpretations of them later. Commenting on Mangini's work, Petrucci said, "When people hear the drumming on this album, they’re gonna be pretty freaked out ... I feel like now he’s just Mike Mangini unleashed. It's all him. It's all his creativity, all his decisions and ideas - and man, the guy's an animal." During the studio sessions, every band member's instrument was miked and captured as they were writing so that they could simulate ahead of time exactly how the music would sound when it was formally recorded. Reflecting on his guitar tone, Petrucci joked, "I describe it as a piece of chocolate
```

### Album 121, chunk 3

```text
cake and that was my goal in the studio. It's like I had a nice picture of a layered chocolate cake. Why chocolate cake? Well, chocolate cake is rich, creamy and it has layers." Recording concluded in May, and mixing was performed by Richard Chycki, who was hired based on Dream Theater's past experiences with him and his history with Rush. In calling the album Dream Theater, the band tried to define who they were and emphasize that they were moving forward. Reflecting on the decision for Guitar World, Petrucci said, "We wanted to make this album a reference point for [fans] as far as what Dream Theater is all about. That was the goal and the mission, and it set the tone for the entire project." In an article for Grantland, Steven Hyden noted the album's stylistic similarities to Rush, writing, "There are songs on Dream Theater that are just straight-up Rush imitations, most notably 'The Looking Glass,' which crossbreeds 'Limelight' with 'Freewill' while leaving out Neil Peart's misanthropic individualism." The songs on Dream Theater are shorter and more compact on average than on other Dream Theater albums, a conscious decision made by the band during writing that Petrucci later admitted was a challenge for them. Two songs on the album made use of a string ensemble conducted by Berklee College of Music student Eren Başbuğ, including the 20-minute closer "Illumination Theory", which keyboardist Jordan Rudess called the band's opportunity to go "crazy" after writing so many concise songs.
```

### Album 121, chunk 4

```text
Split into five sections, the track goes through many style and time signature changes, with Loudwire observing, "Jam-packed with a head-spinning mix of quiet interludes, face melting jams and, courtesy of bassist Myung and Mangini, forests full of rhythmic majesty, this suite plays like a mini album in itself." Dream Theater features two instrumentals, "False Awakening Suite" and "Enigma Machine", the former of which was written specifically to open the band's live shows. They were the first instrumentals that the band had written for a studio album since "Stream of Consciousness" on 2003's Train of Thought. Many of the album's lyrics are based on real events; for example, "The Enemy Inside", which deals with post-traumatic stress disorder (PTSD), was written in response to the Boston Marathon bombings, and "Behind the Veil" references the Elizabeth Smart kidnapping. In June 2013, Dream Theater announced that their upcoming studio album would be self-titled and released in September. The album's first single, "The Enemy Inside", was made available for streaming by USA Today on August 5, and its second single, "Along for the Ride", was made available for streaming the following month. The album was premiered by Rolling Stone on September 16 via a free online stream, and was officially released one week later, on September 23. In its debut week, Dream Theater sold over 34,000 copies in the United States to land at number seven on the Billboard 200 chart, making it the band's third-consecutive top ten debut and second-highest-charting album ever behind
```

### Album 121, chunk 5

```text
2009's Black Clouds & Silver Linings, which debuted at number six. During the album's release week, the band released a music video for "The Enemy Inside", which drove awareness for Save a Warrior, a foundation dedicated to helping veterans heal from the effects of combat. Dream Theater remained on the charts until November 9, and as of January 2016, it has sold 87,000 copies total in the United States. In February 2014, the album's second and final music video was released, this time for "The Looking Glass". Dream Theater received generally positive reviews from music publications. AllMusic felt that it was one of the band's best albums, concluding, "it holds inside it everything a fan could want, yet also expands the reach of American prog metal." Many critics were particularly complimentary of "Illumination Theory", which Revolver described as "stunningly ambitious". Grantland's Steven Hyden, whose introduction to the band was through the self-titled album, wrote, "I drank this cocktail, and I’m glad. Dream Theater is a blast." For "The Enemy Inside", Dream Theater received their second consecutive Grammy nomination in the Best Hard Rock/Metal Performance category. Critics reacted favorably to Dream Theater's attempt at writing more concise songs. In their review, Loudwire commented, "The band also seems to be expanding their appeal beyond the faithful with some punchy, stylish and tuneful songs that seduce immediately. Good thing, too. Because the more people that can hear an album like this, the more faithful there will be." RTÉ.ie had a similar reaction, writing,
```

### Album 121, chunk 6

```text
"Sure, the did-they-really-just-play-that? double takes arrive by the half-minute on their latest magnum opus (self-titled for extra definitiveness), but chances are you will come away from Dream Theater singing a chorus rather than throwing air guitar/bass/drums/keyboards/violin/conductor's baton shapes." Some critics noted that the album was too similar to previous Dream Theater albums. PopMatters felt that the band was no longer offering anything new, observing, "For quite awhile, the sky was the limit for Dream Theater; now that they’ve ascended, however, the creative air is running thin." Sputnikmusic also wrote that the album sounded familiar, but ultimately gave it an overall positive review, saying that it did "a bit better than recent efforts in the band's formulaic approach to anti-formulaic music." In promotion of the album, Dream Theater toured Europe and North America in early 2014. The tour's setlist featured both old and new material, including nine songs off of Awake (1994) and Metropolis Pt. 2: Scenes from a Memory (1999), which were celebrating anniversaries. On March 25, the band performed at the Boston Opera House with the Berklee Concert Choir and Berklee World Strings in an event that was dubbed their "homecoming". The concert was recorded and eventually released on September 30 as part of the Breaking the Fourth Wall live collection. It debuted at number one on various music video charts, and the band donated part of the proceeds to the Dream Theater Scholarship Fund at Berklee. James LaBrie – lead vocals John Petrucci – guitar, backing vocals, producer
```

### Album 121, chunk 7

```text
Jordan Rudess – keyboards, GeoSynth iPad app, Seaboard John Myung – bass, Moog Taurus pedals Mike Mangini – drums, percussion Misha Gutenberg – violin Larisa Vollis – violin Yelena Khaimova – violin Yevgeniy Mansurov – violin Aleksandr Anisimov – viola Noah Wallace – viola Anastasia Golenisheva – cello Valeriya Sholokhova – cello Len Sluetsky – double bass Richard Chycki – engineering, mixing Kevin Matela – assistive mixing Dave Rowland – assistive mixing Eren Başbuğ – orchestral arrangement, conducting
```

## Album 122: Delta Kream — The Black Keys

- **album_id:** `03f8a044-5d79-4294-a73e-3f36707e1a8b`
- **Tags (identification only):** blues rock, blues, delta blues, electric blues, hill country blues, longing, raw
- **Chunks:** 2 (453 words)

### Album 122, chunk 1

```text
Delta Kream is the tenth studio album by American rock duo the Black Keys, released through Easy Eye Sound and Nonesuch Records on May 14, 2021. It is a cover album of hill country blues songs. It was preceded by the April 15 release of a cover of "Crawling Kingsnake", based on Junior Kimbrough's rendition. The album was recorded "in about 10 hours" over two afternoons at Dan Auerbach's Easy Eye Sound studio in Nashville at the end of the Let's Rock tour, with little planning and no advance rehearsals. It includes contributions from R. L. Burnside's guitarist Kenny Brown as well as Junior Kimbrough's bassist Eric Deaton; the Black Keys had previously covered Burnside's "Skinny Woman" (titled "Busted") and Kimbrough's "Do the Romp" (titled "Do the Rump") on their 2002 debut album The Big Come Up, and released the Kimbrough tribute album Chulahoma: The Songs of Junior Kimbrough in 2006. Brown and Deaton had been recording at Easy Eye Sound studio concurrently along with Auerbach for the album Sharecropper's Son by Robert Finley, which lead to their availability for the Delta Kream sessions. In a statement, Auerbach said: "We made this record to honor the Mississippi hill country blues tradition that influenced us starting out. These songs are still as important to us today as they were the first day Pat and I started playing together and picked up our instruments." The album cover features a 1970s photograph by William Eggleston of the Delta Kream shop in Tunica, Mississippi,
```

### Album 122, chunk 2

```text
with an Oldsmobile Cutlass parked outside – the shop no longer exists. The Black Keys announced Delta Kream on April 13, 2021, exclusively through their Lonely Boys and Girls fan club. Through the fan club, on the same day, they also released the album's lead single, a cover of Junior Kimbrough's version of "Crawling Kingsnake". It was released to digital music platforms two days later. Additionally, a music video for the song was released. Directed by Tim Hardiman, it features a performance of the song by the band at the Blue Front Cafe, owned by blues musician Jimmy "Duck" Holmes. Delta Kream was released on May 14, 2021, through Easy Eye Sound and Nonesuch Records on digital music platforms and physical media. The album's digital release includes a shortened edit of "Crawling Kingsnake" as a bonus track. Physically, the album was made available to purchase as both a CD and double 12-inch vinyl record, with standard black, limited edition "purple haze", and Spotify user-exclusive pink options available for the vinyl release. Dan Auerbach – lead vocals, electric guitar, production Patrick Carney – drums, percussion, production Eric Deaton – bass Kenny Brown – electric guitar Sam Bacco – additional percussion Tchad Blake – mixing
```

## Album 123: Bringing Down the Horse — The Wallflowers

- **album_id:** `fc2cd4b4-68ad-4424-a7b9-4a3ef01d614e`
- **Tags (identification only):** rock, alternative rock, adult alternative pop/rock, alternative/indie rock, american trad rock, americana, country rock, pop/rock
- **Chunks:** 5 (1115 words)

### Album 123, chunk 1

```text
Bringing Down the Horse is the second album by American rock band the Wallflowers. It was released worldwide on May 21, 1996. The album was produced by T Bone Burnett and includes four singles: "6th Avenue Heartache", "One Headlight", "The Difference", and "Three Marlenas". Bringing Down the Horse reached number four on the Billboard 200 and went quadruple platinum, becoming the Wallflowers' highest-selling album to date. Three songs from the album were nominated for Grammy Awards; in 1997 the Wallflowers received two nominations, both for "6th Avenue Heartache". In 1998 the band received three additional nominations; two for "One Headlight" and one for "The Difference". "One Headlight" won in both categories it was nominated in. The song was the band's most popular single, reaching number one on the Billboard Mainstream Rock, Modern Rock, and Adult top 40 charts. "One Headlight" is also listed at number 58 in Rolling Stone's list of the 100 Greatest Pop Songs. Bringing Down the Horse was issued on vinyl for the first time as a double LP set for the album's 20th anniversary, released by Interscope/Universal Music Group, on May 13, 2016. The Wallflowers released their debut album in 1992 on Virgin Records and subsequently parted ways with the label shortly after the album's release. The band went back to playing clubs in Los Angeles in hopes of securing another record deal. In the year it took to get another deal, the Wallflowers went through a number of personnel changes; the band's bass player Barrie
```

### Album 123, chunk 2

```text
Maguire and drummer Peter Yanowitz both left the band in 1993. Maguire was quickly replaced by Greg Richling, but the drummer position remained open. Soon after Yanowitz's departure, the Wallflowers were noticed by Jimmy Iovine and Tom Whalley of Interscope Records and the band was signed to the label in 1994. After multiple years away from the studio, the Wallflowers were ready to record. However, they encountered some difficulty in finding a producer willing to work with them. The band sent demo tapes to many producers and one ended up in the hands of T Bone Burnett. Burnett was impressed with what he heard and agreed to produce the band. The Wallflowers entered the studio to begin recording in 1994. Much of the album was recorded in the Los Angeles area. The band's lineup heading into the studio consisted of lead singer-songwriter/rhythm guitarist Jakob Dylan, bassist Greg Richling, keyboard player Rami Jaffee and lead guitarist Tobi Miller. Early in the sessions, however, Miller quit the band for undisclosed reasons, though he remained on good terms with the band. This left the band without a permanent lead guitarist or drummer. Those positions were temporarily filled by drummer Matt Chamberlain and a number of guitarists including Mike Campbell of Tom Petty and the Heartbreakers, Fred Tackett, Jay Joyce and Michael Ward, who would go on to become a permanent member of the group. Bringing Down the Horse further explores roots sounds heard on the band's previous self-titled album but used a more
```

### Album 123, chunk 3

```text
refined approach. This album features an array of instruments normally associated with roots music including banjos, dobros and pedal steel guitars. Dylan commented on the sound of the record: You can counter different sounds and different things. We were in a certain channel already, and I do remember thinking if we mixed it organically, and we kept chasing that [Americana sound], it probably would sound dated. I wasn't interested in making a throwback record from the 60's or 70's. I didn't have any interest in doing that. And that was one of the reasons we had Tom Lord-Alge, who was a very current mixer at the time. We thought that he could counter a lot of these acoustic sounds with something that sounded really fresh and up to date. Upon entering the studio, Dylan, who wrote all the songs for Bringing Down the Horse, had written some songs that were ready to record but needed more to complete the album. Due to the delay between the band's first album and this album, the songwriting process was staggered. Songs for Bringing Down the Horse were written in a span of roughly 5 years. One of the earliest songs, "6th Avenue Heartache", was written before the band's first album; likely around 1990. Several other songs, such as "God Don't Make Lonely Girls", were written when the band was in between labels. During recording sessions, Dylan wrote seven additional songs for the album including "One Headlight", "Bleeders", "Three Marlenas", "The Difference", "Josephine", "Invisible
```

### Album 123, chunk 4

```text
City", and "I Wish I Felt Nothing". On the lyrical content, Dylan stated, "Every song, fortunately or unfortunately is about feeling massively defeated, because that's what I was living." Dylan later said he wrote "I Wish I Felt Nothing" with the band's pedal steel guitarist Leo LeBlanc in mind, who was battling cancer at the time. LeBlanc had been playing with the Wallflowers for several years and was prominently featured on several songs on Bringing Down the Horse, including "Invisible City" and "I Wish I Felt Nothing". He died shortly after completing the album in 1995. Upon the album's release, the Wallflowers dedicated Bringing Down the Horse to LeBlanc. In a 2023 review, Madison Bloom of Pitchfork rated Bringing Down the Horse a 7.3 out of 10, declaring that a "stale sense of dissatisfaction" with the recording industry is present in the lyrics and highlighted several tracks that make up minor musical suites that made the album a commercial powerhouse. Review by James Chrispell points out that only two members remain from the original band. However, he says the music is still assured and contemporary with enough of the past showing through. He feels the album is, "A fine effort indeed." Jakob Dylan – vocals, rhythm guitar Rami Jaffee – piano, Hammond B-3 organ, Vox Continental, upright piano Greg Richling – bass guitar Michael Ward – lead guitar Mario Calire – drums (credited as the band's drummer, but also noted as not performing on the record) Matt Chamberlain – drums
```

### Album 123, chunk 5

```text
Jon Brion – lead guitar on "One Headlight" Stephen Bruton – background vocals on "I Wish I Felt Nothing" Mike Campbell – slide guitar on "6th Avenue Heartache" Adam Duritz – background vocals on "6th Avenue Heartache" Leo LeBlanc – pedal steel guitar on "I Wish I Felt Nothing", "God Don't Make Lonely Girls" and "Invisible City"; Dobro on "One Headlight" Gary Louris – background vocals on "One Headlight" and "The Difference" Michael Penn – background vocals on "Angel on my Bike" Sam Phillips – background vocals on "One Headlight" and "Laughing Out Loud" Tom Lord-Alge – engineering, mixing T Bone Burnett – production Stephen Marcussen - mastering at Precision Mastering in Los Angeles, CA
```

## Album 124: Big Sexy Land — Revolting Cocks

- **album_id:** `40554776-c2fe-493c-bc20-85376a152e47`
- **Tags (identification only):** industrial, electronic, rock, alternative pop/rock, alternative/indie rock, heavy metal, industrial dance, pop/rock
- **Chunks:** 2 (326 words)

### Album 124, chunk 1

```text
Big Sexy Land is the debut studio album by industrial rock band Revolting Cocks, released through Wax Trax! Records in 1986. This is the only album to feature the group's founding lineup of Luc van Acker, Richard 23 and Alain Jourgensen. The album's title is a reference to a strip club in West Berlin. Jourgensen said that the club's large, neon sign was "the biggest capitalistic tease" for citizens in East Germany. The album was recorded in 1985 at ICP Studios in Brussels. Van Acker attributed the album's mixing to Jourgensen's sessions with Adrian Sherwood on Twitch. Van Acker said Jourgensen surreptitiously took notes on Sherwood's settings, but, without any context for the numbers, they had to later guess at what the settings were for, such as reverb and delay time. According to Van Acker, Jourgensen did not appear as a musician on the album because he was still under contract by Sire. After Jourgensen released a dub remix of "You Often Forget" without the band's input, Richard 23 quit. The track "We Shall Cleanse the World" includes a sample of the title phrase taken from the film The Omega Man starring Charlton Heston. The title of the track "Attack Ships on Fire" is taken from dialog in the film Blade Runner. "38" is a reference to the victims of the Heysel Stadium disaster which occurred on May 29, 1985, although the final death toll in the disaster was actually 39. The Rough Guide to Rock described the album as
```

### Album 124, chunk 2

```text
a "more fluid Nitzer Ebb" evocative of current trends in electronic music. AllMusic wrote that it is "a distinguished debut from a 'side project' that occasionally surpasses the day-job work that its members became famous for". No Devotion (1985) "No Devotion" "Attack Ships..." "...On Fire" Luc van Acker – vocals, guitars Richard 23 – vocals, programming Alain Jourgensen – production, engineering Bill Rieflin – drums ("You Often Forget") Patrick Codenys – additional keyboards (2, 4, 6)
```

## Album 125: Kasabian — Kasabian

- **album_id:** `affb3dc9-d9ec-4961-b439-43ada18ffdec`
- **Tags (identification only):** indie rock, alternative dance, electronic, alternative rock, neo psychedelia, post punk revival, baggy, cccd
- **Chunks:** 4 (960 words)

### Album 125, chunk 1

```text
Kasabian is the debut studio album by British rock band Kasabian, released on 6 September 2004. The album's highest chart position on the UK Albums Chart was number 4, making it the band's only studio album not to reach number one. Five singles were released from Kasabian. This is the only full album to feature the lead guitarist and lead songwriter Christopher Karloff, who left the band during the recording sessions of their next album, Empire. The album features a rotating cast of drummers, with full-time drummer Ian Matthews joining the band after the release of the album. Different geographical regions had different colours for their album cover. The British version is black and white, the European import is black and red, and the American version is black and blue. The Japanese "Ultimate Version" is silver and white. The UK limited-edition version is a double-sided DualDisc and has a glow-in-the-dark cover. The DVD element contains a making-of documentary and several music videos. This album has been released with the Copy Control protection system in some regions. In the United States and Canada it uses the MediaMax CD-3 system. The Canadian version of the album does not contain the songs "Orange", "Pinch Roller" and "Ovary Stripe", with the exception of digital releases. The opening track "Club Foot" features a signature distorted bass riff, played by Christopher Karloff and features "a quilt of relentless beats, hissing electronic noises, buzzing guitar and Tom Meighan's breathless, menacing vocals", and lyrics inspired by the Iraq
```

### Album 125, chunk 2

```text
War. "Processed Beats", one of eventual drummer Ian Matthews' two contributions to the album has been compared to The Stone Roses with its "shambolic beat" and unison chorus from Meighan and Pizzorno. "Reason is Treason" was branded as an "indie rock seducer", with a sound resembling "Stereolab backing Ian Brown". "L.S.F (Lost Souls Forever)" features prominent use of the electronic instrument Omnichord, played by Karloff and was described as featuring "massive backswells of low-end punch overlaid with Tom Meighan's monotonic snarl and Sergio Pizzorno's swirling guitars and electronics." "Test Transmission", the first of two songs to feature Pizzorno on lead vocals was branded as "prog rock danced in baggy jeans" and "Chemical Brothers-esque psychedelic electronica". Noted for its opening lyric 'John was a scientist, he was hooked on LSD', the fifth and final single "Cutt Off" "pitches space-age synths to the sort of psycho-babble only usually risked by Orb". "Butcher Blues" was described as "cinematic" and featuring "hazy dissolves, tube station announcement vocals, and head-nodding electronic percussion". After the instrumental track "Ovary Stripe", "U Boat" closes out the album, featuring Pizzorno's vocals over "layered organic and electronic bliss", resulting in "space rock meeting angst rock". After a long gap, a hidden track plays, the Jacknife Lee remix of "Reason is Treason". Kasabian received generally favourable reviews but music critics were mixed on the band's mixture of alternative rock and electronica. At Metacritic, which assigns a normalised rating out of 100 to reviews from mainstream critics, the album received an average
```

### Album 125, chunk 3

```text
score of 65, based on 21 reviews. AllMusic's David Jeffries praised the album for its take on different rock genres and compared them favourably to The Stone Roses and Tangerine Dream, saying that "Painting them as rock's saviors just makes the overly ambitious moments of the album look all that much bigger." Paul Moody of NME praised the album for its aggressive instrumentals and space rock sound resembling that of The Libertines. He singled out "Test Transmission" as the standout track, calling it "an indication that once they've purged the violent tendencies, a future as space-rockers in the Spiritualized mould awaits." Betty Clarke of The Guardian praised the album's overall sound for resembling baggy music, saying that it "sums up Kasabian's affection for experimentation of every description." Johnny Loftus, writing for Pitchfork, commended the album's high-energy tracks for containing production that will grab listeners' attention but felt that it loses steam in places and will send said listeners away to better records that inspired it, concluding that "Kasabian is brash, loutish, and seems liable at times to cut you; the consistent kick drum beat throughout it is like a great party's heartbeat. But like the roustabout in the corner, drinking all the lager and scratching up your old records, it can be more loudmouthed than substantial." Tom Edwards of Drowned in Sound criticized the album's songs for lacking any hooks and nuances to grab the listener's attention concluding with, "Sure this album may well sound awesome if you've just snorted
```

### Album 125, chunk 4

```text
a metre of charlie or recently breakfasted from a menu of 'shrooms and LSD, but for sober ears it's enough to drive anyone to drugs." Barry Walters of Rolling Stone criticized the band for filling the album with half-baked ideas based on influences from Happy Mondays and Primal Scream, saying that "Kasabian make the mistake of trying to be revolutionary by quoting revolutionaries." Tom Meighan – lead vocals (tracks 1–4, 6, 7, 10, 11), backing vocals (tracks 8, 13) Sergio Pizzorno – rhythm guitar (tracks 1–4, 6–8, 10–13), synths (all tracks), lead vocals (tracks 8, 13), vocals (track 3), backing vocals (tracks 1, 2, 4, 6, 7, 10–12) Christopher Karloff – lead guitar (tracks 1–4, 6–8, 10–13), synths (all tracks), omnichord (tracks 2–4, 6, 10–12), bass (tracks 1, 3, 8) Chris Edwards – bass (tracks 2, 4, 6-7, 10–13) Ian Matthews – drums (tracks 2, 11) Ryan Glover – drums (tracks 3, 8) Martin Hall-Adams - drums (track 6) Daniel Ralph Martin – drums (track 10) Mitch Glover – drums (track 12) Kasabian – production Jim Abbiss – additional production and mixing (tracks 1–4, 6–8, 10–13) Barny – mixing and engineering (tracks 5, 9), mix engineer (tracks 1–4, 7, 8, 10, 12, 13) Damian Taylor – programming (tracks 6, 11)
```
