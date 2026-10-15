# Embedding text relevance, batch 8 of 12 (albums 176–200 of 300)

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

This batch: **25 albums, 76 chunks**.

## Album 176: Self Portrait — Bob Dylan

- **album_id:** `1d7891fe-def7-4dc6-b9fa-2b3f7623312c`
- **Tags (identification only):** folk rock, rock, country rock, should be public domain
- **Chunks:** 8 (1886 words)

### Album 176, chunk 1

```text
Self Portrait is the tenth studio album by American singer-songwriter Bob Dylan. It was released on June 8, 1970, through Columbia Records. The album was produced by Bob Johnston and was Dylan's second double album, after Blonde on Blonde (1966). The record is compiled of cover songs, live recordings, and new originals, while the arrangements and vocal performances continue in the country vein of the preceding Nashville Skyline (1969). Self Portrait was released to negative reviews and confusion from critics and fans alike. Criticism was directed at the album's production, performances, and the lack of new material. Dylan himself has since referred to the album as having been released with the purpose of confounding the public's expectations of him, and to counter the "spokesman of a generation" tag which had been placed on him throughout the 1960s. Despite the critical reception, the album was a commercial success, reaching number four in the US and topping the chart in the UK. In 2013, Dylan released The Bootleg Series Vol. 10: Another Self Portrait (1969–1971), which resulted in further positive critical revaluation. The motives behind Self Portrait have been subject to wild speculation and great debate. Critic Robert Shelton was under the impression that Self Portrait was intended as a serious release. "I told Dylan that Self Portrait confused me," Shelton wrote in 1986. "Why had he recorded 'Blue Moon'? He wouldn't be drawn out, although obviously he had been stung by the criticism. 'It was an expression,' he said. He indicated
```

### Album 176, chunk 2

```text
that if the album had come from Presley or the Everly Brothers, who veered toward the middle of the road, it wouldn't have shocked so many." However, in a Rolling Stone interview, in 1984, Dylan gave a different reason for the album's release: At the time, I was in Woodstock, and I was getting a great degree of notoriety for doing nothing. Then I had that motorcycle accident [in 1966], which put me outta commission. Then, when I woke up and caught my senses, I realized that I was just workin' for all these leeches. And I didn't wanna do that. Plus, I had a family, and I just wanted to see my kids. I'd also seen that I was representing all these things that I didn't know anything about. [. . .] This was just about the time of that Woodstock festival, which was the sum total of all this bullshit. And it seemed to have something to do with me, this Woodstock Nation, and everything it represented. So we couldn't breathe. I couldn't get any space for myself and my family, and there was no help, nowhere. I got very resentful about the whole thing, and we got outta there. We moved to New York. [. . . ] There'd be crowds outside my house. And I said, “Well, fuck it. I wish these people would just forget about me. I wanna do something they can't possibly like, they can't relate to. They'll see it, and they'll listen,
```

### Album 176, chunk 3

```text
and they'll say, 'Well, let's go on to the next person. He ain't sayin' it no more. He ain't givin' us what we want,' you know? They'll go on to somebody else," But the whole idea backfired because the album went out there, and the people said, "This ain't what we want," and they got more resentful. And then I did this portrait for the cover. I mean, there was no title for that album. I knew somebody who had some paints and a square canvas, and I did the cover up in about five minutes. And I said, "Well, I'm gonna call this album Self Portrait." [Rolling Stone:] Which was duly interpreted by the press as: This is what he is... Yeah, exactly. And to me, it was a joke. As to why he chose to release a double album, Dylan replied, "Well, it wouldn't have held up as a single album–then it really would've been bad, you know. I mean, if you're gonna put a lot of crap on it, you might as well load it up!" Later, Cameron Crowe interviewed Dylan for his liner notes to 1985's Biograph, a boxed-set retrospective of Dylan's career. When asked about Self Portrait, Dylan added more details to the story: Self Portrait was a bunch of tracks that we'd done all the time I'd gone to Nashville. We did that stuff to get a [studio] sound. To open up we'd do two or three songs, just to get things right and
```

### Album 176, chunk 4

```text
then we'd go on and do what we were going to do. And then there was a lot of other stuff that was just on the shelf. But I was being bootlegged at the time and a lot of stuff that was worse was appearing on bootleg records. So I just figured I'd put all this stuff together and put it out, my own bootleg record, so to speak. You know, if it actually had been a bootleg record, people probably would have sneaked around to buy it and played it for each other secretly. Also, I wasn't going to be anybody's puppet and I figured this record would put an end to that...I was just so fed up with all that 'who people thought I was' nonsense. Later interviews only echoed the sentiments expressed to Crowe. Certain tracks have drawn praise over the years. One of them is written by Alfred Frank Beddoe (who was "discovered" by Pete Seeger after applying for work at People's Songs, Inc. in 1946), "Copper Kettle" captures an idyllic backwoods existence, where moonshine is equated not only with pleasure but with tax resistance. Appalachian farmers who struggled to make their living off the land would routinely siphon off a percentage of their corn in order to distill whiskey. Everything produced would then be hidden from the government in order to avoid the whiskey tax of 1791. Clinton Heylin writes, "'Copper Kettle'...strike[s] all the right chords...being one of the most affecting performances in Dylan's entire
```

### Album 176, chunk 5

```text
official canon." Music critic Tim Riley called it "an ingenious Appalachian zygote for rock attitudes, the hidden source of John Wesley Harding's shadows." "Copper Kettle" was popularised by Joan Baez and appeared on her best-selling 1962 LP Joan Baez in Concert. Among the original songs written for the album, the instrumental "Wigwam" later achieved recognition for its use in the 2001 Wes Anderson film The Royal Tenenbaums. "Living the Blues" was later covered by Leon Redbone. "Living the Blues" was also covered by the Jamie Saft Trio with Anohni on the album Trouble: The Jamie Saft Trio Plays Bob Dylan, in 2006. "All the Tired Horses" only features two lines, and is sung by Hilda Harris, Albertine Robinson, and Maeretha Stewart. The song featured in the 2001 film Blow. One of the live songs on the album is the party-friendly romp "The Mighty Quinn (Quinn the Eskimo)", originally recorded at the 1967 Basement Tapes sessions and covered to great success by Manfred Mann in 1968. For live venues, the Grateful Dead and Phish made the song an iconic favorite. The version on Self Portrait, however, is a soundboard-sourced live performance from Dylan and the Band's Isle of Wight Festival concert (as are three other tracks on the album). Self Portrait received negative reviews by critics and consumers alike. Critical disdain seemed universal. At best, a number of journalists, including Robert Christgau, felt there was a concept behind Self Portrait that had some merit. "Conceptually, this is a brilliant album," wrote
```

### Album 176, chunk 6

```text
Christgau, "which is organized, I think, by two central ideas. First, that 'self' is most accurately defined (and depicted) in terms of the artifacts—in this case, pop tunes and folk songs claimed as personal property and semispontaneous renderings of past creations frozen for posterity on a piece of tape and (perhaps) even a couple of songs one has written oneself—to which one responds. Second, that the people's music is the music people like, Mantovani strings and all." However, few critics expressed any interest in the music itself. "[I]n order for a concept to work it has to be supported musically—that is, you have to listen," Christgau admitted. "I don't know anyone, even vociferous supporters of this album, who plays more than one side at a time. I don't listen to it at all. The singing is not consistently good, though it has its moments, and the production—for which I blame Bob Johnston, though Dylan has to be listed as a coconspirator—ranges from indifferent to awful. It is possible to use strings and soprano choruses well, but Johnston has never demonstrated the knack. Other points: it's overpriced, the cover art is lousy, and it sounds good on WMCA." In his Rolling Stone review Greil Marcus used a memorably vitriolic opening line: "What is this shit?" Additionally, Marcus wrote, "Unless [Dylan] returns to the marketplace, with a sense of vocation and the ambition to keep up with his own gifts, the music of [the mid-sixties] will continue to dominate his records, whether
```

### Album 176, chunk 7

```text
he releases them or not." He also commented, "I once said I'd buy an album of Dylan breathing heavily. I still would. But not an album of Dylan breathing softly." In a 1971 telephone interview with journalist A.J. Weberman, Dylan can be heard responding angrily to the Marcus review, while attempting to defend larger accusations of perceived non-committal politics. A rare dissenting positive voice about the album was English musician Marc Bolan. Appalled at the negative reviews directed at the album, Bolan wrote a letter in its defence to the 11 July 1970 edition of Melody Maker: I've just listened to Dylan's new album, and in particular "Belle Isle", and I feel deeply moved that such a man is making music in my time. Dylan's songs are now mainly love ballads, the writing of which is one of the most poetic art forms since the dawn of man. "Belle Isle" brought to my memory all the moments of tenderness I've ever felt for another human being, and that, within the superficial landscape of pop music, is a great thing indeed. Please, all the people who write bitterly of a lost star, remember that with maturity comes change, as surely as death follows life. Rock critics Jimmy Guterman and Owen O'Donnell, in their 1991 book The Worst Rock and Roll Records of All Time, listed Self-Portrait as the third worst rock album ever, with only Lou Reed's experimental Metal Machine Music and Elvis Presley's concert byplay album Having Fun with Elvis
```

### Album 176, chunk 8

```text
on Stage faring worse. "The breakup of the Beatles shortly before this album's release," they wrote, "signaled the end of the sixties; Self-Portrait suggested the end of Bob Dylan." In 1973, Knopf published Dylan's song lyrics, sketches, and album notes as Writings and Drawings, with updated versions called Lyrics appearing in 1985 and 2000. In all three editions, the original lyrics from Self Portrait are never acknowledged, suggesting Dylan's disavowal of the whole album to that time. However, the lyrics to "Living the Blues" and "Minstrel Boy" are included, listed as extra songs from the Nashville Skyline sessions; the 2004 edition includes them under their own entry and Dylan's current website includes the release together with lyrics and download links. Dylan revisited Self Portrait on The Bootleg Series Vol. 10: Another Self Portrait (1969–1971) in 2013.
```

## Album 177: Phrenology — The Roots

- **album_id:** `b357f9f3-0018-41b2-a6d6-e729e49b6c1c`
- **Tags (identification only):** hip hop, alternative hip hop, conscious hip hop, jazz rap, alternative rap, band, east coast hip hop, hardcore hip hop
- **Chunks:** 4 (869 words)

### Album 177, chunk 1

```text
Phrenology is the fifth studio album by American hip-hop band the Roots, released on November 26, 2002, by MCA Records. Recording sessions for the album took place during June 2000 to September 2002 at Electric Lady Studios in New York. It was primarily produced by members of the band and features contributions from hip-hop and neo soul artists such as Cody ChesnuTT, Musiq Soulchild, Talib Kweli, and Jill Scott. Although it did not parallel the commercial success of the band's previous album, Things Fall Apart, the album reached number 28 on the US Billboard 200 chart and sold steadily, remaining on the chart for 38 weeks. On June 3, 2003, it was certified gold by the Recording Industry Association of America, for shipments of 500,000 copies in the United States. Upon its release, Phrenology received universal acclaim from music critics, who praised its musical direction and lyrical themes, and it was included in numerous publications' year-end lists of the year's best albums. Following the breakthrough success of Things Fall Apart (1999), its release was highly anticipated and delayed, as recording took two years. The album is named after the discredited pseudoscience of phrenology, the study of head shapes to determine intelligence and character, which was used to rationalize racism during the 19th century in the United States. Its cover art was created by artist/printmaker Tom Huck. Primarily a hip-hop album, Phrenology features lyrical themes of hip-hop culture and its commodification, with musical elements of rock, jazz, techno, hardcore punk, and
```

### Album 177, chunk 2

```text
soul music. According to music critic Greg Kot, the Roots forge a connection between hip-hop and neo soul on the album, while Treble writer says it can "best be described" as progressive rap, and Entertainment Weekly's Raymond Fiore calls it the band's "left-field rock-rap opus". A production of the Soulquarians collective, the album features contributions by Cody ChesnuTT, Musiq Soulchild, Talib Kweli, and Jill Scott. On "Something in the Way of Things (In Town)", Amiri Baraka performs a poem about how the spirit of death and decay permeates African-American urban experiences. Set to a fusion of several African-American music influences, his poem observes "something in the way of our selves" and uses unusual imagery such as death "riding on top of the car peering through the windshield" and a "Negro squinting at us through the cage" with a smile "that ain't a smile but teeth flying against our necks". Phrenology received widespread acclaim from critics. At Metacritic, which assigns a normalized rating out of 100 to reviews from mainstream publications, the album received an average score of 87, based on 23 reviews. Mojo magazine hailed it as a "masterpiece", while Rolling Stone writer Pat Blashill said it has "a startling array of hip-hop reinventions". Dave Heaton from PopMatters called Phrenology "an impressive, ambitious work" that shows the Roots "filling their sound out and pushing it in a variety of directions", with a form of "tight soul/funk" that "sounds even more exact, funkier and edgier" than on Things Fall Apart. In
```

### Album 177, chunk 3

```text
the Chicago Sun-Times, critic Jim DeRogatis gave the record four out of four stars and called it "a near-classic right out of the gate, an urgent, raucous and thought-provoking 70 minutes that mine the musical territory between hard hip-hop and smoother Philly soul". Blender's RJ Smith called it "a celebration of self-determination, a nonstop joyride through some very complicated brains". Jeremy Gladstone from Kludge felt the Roots had combined "complicated beats" with "complex lyrics" to produce a "shockingly honest sound". In The Guardian, Alexis Petridis found the group "exclusively capable of absorbing other genres", while the "more straightforward hip-hop" is "idiosyncratic and hugely enjoyable". Slant Magazine's Sal Cinquemani called the album "subtly progressive" and felt the lyrics "challenge the commodification and subsequent destruction of hip-hop culture". In a less enthusiastic review, Uncut magazine said Phrenology shows the Roots' "willingness to push the envelope of their organic jazz-rap" that is unparalleled but sometimes musically pretentious or indulgent, particularly on "Something in the Way of Things" and the coda to "Water". AllMusic editor Steve Huey felt it is "a challenging, hugely ambitious opus that's by turns brilliant and bewildering, as it strains to push the very sound of hip-hop into the future." He also called it the band's "hardest-hitting" album because they successfully "re-create their concert punch in the studio." In his column for The Village Voice, Robert Christgau believed the Roots have finally discovered how to write tuneful and structured music on Phrenology, as they "humanize their formal commitment with injections
```

### Album 177, chunk 4

```text
of singing and guitar". At the end of 2002, Phrenology was named one of the year's best albums. It was voted the seventh best album of 2002 in The Village Voice's Pazz & Jop, an annual poll of American critics. The Rolling Stone Album Guide (2004) later gave it four-and-a-half stars and cited "Water" as a highlight, "that begins with the age-old Bo Diddley beat and ends as an extended musique concrète-style instrumental fantasia". Phrenology was included in the 2010 reference book 1001 Albums You Must Hear Before You Die and in Tom Moon's 1000 Recordings to Hear Before You Die (2008). Slant Magazine listed the album at number 231 on its "Top 250 Albums of the 2000s" (2010).
```

## Album 178: Blue’s — Zucchero Sugar Fornaciari

- **album_id:** `5378eb59-3d04-4880-9b08-93605b4f308d`
- **Tags (identification only):** blues, gospel, italian pop, jazz, piano blues, pop rock, rock, soul
- **Chunks:** 1 (202 words)

### Album 178, chunk 1

```text
Blue's is the fourth studio album by Italian singer-songwriter Zucchero Fornaciari. It was released on 15 June 1987, with Fornaciari credited as "Zucchero Sugar Fornaciari". The album sold over 1.3 million copies. The success that Zucchero had experienced at music festivals in the early 1980s, including several appearances at the Sanremo Music Festival, eventually attracted the attention of foreign musicians. After travelling to the United States in the mid-1980s, he returned with a new band including some American musicians and a focus on the blues. Among them was keyboardist David Sancious. The tour following the release of the album included performances featuring Joe Cocker, Miles Davis, Eric Clapton, and B. B. King. The album elevated Zucchero's reputation internationally It became the best-selling album internationally by an Italian musician, until it was overtaken by Zucchero's subsequent studio album Oro Incenso & Birra in 1989. Zucchero – vocals, piano Giorgio Francis – drums Rosario Jermano – percussion Polo Jones – bass Corrado Rustici – guitar David Sancious – keyboards Wayne Jackson – trombone, trumpet Andrew Love – saxophone Clarence Clemons – saxophone Eric Daniel – saxophone James Thompson, Aida Cooper, Arthur Miles, Simona Pirone, Coro di Voci Maschili della Chiesa Avventista – backing vocals
```

## Album 179: For Alto — Anthony Braxton

- **album_id:** `09f847a0-6b9e-4b20-8439-86baad47090c`
- **Tags (identification only):** jazz, acoustic, atmospheric, atonal, avant garde, chaotic, complex, dissonant
- **Chunks:** 3 (773 words)

### Album 179, chunk 1

```text
For Alto is a studio album by American composer and saxophonist Anthony Braxton, recorded in 1969 and released on Delmark Records in 1971. Braxton performs the pieces on this album entirely on alto saxophone, with no additional musicians or overdubbing. Although other jazz musicians, such as Coleman Hawkins, Sonny Rollins, and Eric Dolphy, had recorded unaccompanied saxophone solos, For Alto was the first jazz album composed solely of solo saxophone music. According to Braxton, For Alto came about as a result of his fascination with the solo piano music of Arnold Schoenberg, Fats Waller, and Karlheinz Stockhausen. However, feeling that his skills on the piano were inadequate, he decided to create "a particular language for the saxophone." He also cited the experience of a 1967 improvised solo saxophone concert during which he ran out of ideas. He recalled: "I imagined I was just going to get up there and play for one hour from pure invention, but after ten minutes I'd run through all my ideas and started to repeat myself. I felt like, 'Oh my God, and there's still fifty minutes to go!'" This led to a project in which he catalogued specific, easily identifiable musical elements (for example, long sounds, trills, multiphonics, short attacks) which could then be used as "starting points or springboards to musical activity." Braxton would term this concept "Language Music," of which For Alto is an early example. Braxton later stated that he recorded the music himself in the basement of the Parkway Community
```

### Album 179, chunk 2

```text
Center in Chicago, and that he "basically gave it to Delmark Records." Although the published liner notes consist only of a series of diagrams, he had originally intended to include a lengthy essay in which he stated: "If this record doesn't sell a million copies I will be very disappointed. Already I am making room on my mantle for a gold record and I am going to have parties and I am preparing an acceptance speech." Braxton would go on to record several more solo alto saxophone albums, such as Saxophone Improvisations Series F (1972) and Alto Saxophone Improvisations 1979, and For Alto would inspire other saxophonists, such as Joe McPhee, Evan Parker, and Steve Lacy, to record their own solo albums. Initial reaction to the album was mixed. In a June 1971 DownBeat review, Joe H. Klee called the album "revolutionary" and awarded it five stars. In the same issue of DownBeat, saxophonist Harold Land commented on the track "To Artist Murry DePillars" for the magazine's "Blindfold Test" column: "I think that he's a very good saxophonist... I have great respect for his technique and his control of the instrument." Four months later, the magazine published a second Blindfold Test, this time with saxophonist Phil Woods, in which he stated of the same track: "That was terrible, I can't imagine the ego of a person thinking they can sustain a whole performance by themselves... It's not jazzy, it's not classical... it's dull... this is such an ego trip..." Subsequent
```

### Album 179, chunk 3

```text
reactions have been more uniformly positive, and the album is now recognized as a landmark. The AllMusic review by Thom Jurek stated: "For Alto is one of the greatest solo saxophone records ever made, and maybe one of the greatest recordings ever issued, period". The Penguin Guide to Jazz gives For Alto a four-star rating (of a possible four) along with its "crown" token of merit, and describes it as "one of the genuinely important American recordings. While some landmark performances retain only a mystical aura of their original significance, [For Alto] remains powerfully listenable and endlessly fascinating." In All About Jazz, Derek Taylor observed: "This is a recording and artistic statement that completely changed the rules. Braxton's gall seemed audacious to some, but revolutionary to far more and the hindsight of history has proven this latter camp correct." In Jazzwise, Kevin Le Gendre stated: "Braxton's alto saxophone is like the sound of acid dripped from the beating wings of hummingbirds, a charmingly corrosive caress. Through brilliant dynamics, lyricism, harmonic invention and pure sound trickery, Braxton showed a single horn could be a complete orchestra." Nate Wooley, writing for Sound American, interpreted For Alto as "a fascinating document" of Braxton’s concept of language types, as well as "an enjoyably rigorous example of his mastery of the alto saxophone." Author Tom Moon included the album in his book 1,000 Recordings to Hear Before You Die, writing: "For Alto is dizzying and maddening, dense and challenging, inventive and offputting. It's also among a handful of great solo saxophone recordings in jazz, alongside the unaccompanied tunes on Eric Dolphy's Far Cry." Anthony Braxton – alto saxophone
```

## Album 180: m² — Marcus Miller

- **album_id:** `db51d51f-227f-4e67-9e5f-e05a8cc6f0a4`
- **Tags (identification only):** jazz, smooth jazz, contemporary jazz, funk, jazz funk, soul jazz
- **Chunks:** 3 (626 words)

### Album 180, chunk 1

```text
M2 is a studio album by Jazz fusion musician Marcus Miller, released in 2001 on Telarc Records. This album won the 2002 Grammy Award for Best Contemporary Jazz Album. Sonia Murray of the Atlanta Journal Constitution, in a B review declared, "on occasion, the past bandmate of Miles Davis, Steely Dan's Donald Fagen, George Benson and others steps out front and graces us with a solo project. And his first such effort in seven years -- even in its funk tendencies -- evokes the kind of ease and beauty that makes the word "grace" appropriate." Rob Theakston of Allmusic in a 4/5 star review commented, "Marcus Miller continues to display his multi-instrument virtuosity with M², and while the order of the day is still smooth jazz, there's more of a soulful R&B edge than the majority of his previous work. It also features an all-star cast that includes Herbie Hancock, Branford Marsalis, Raphael Saadiq, Paul Jackson, Jr., and Lenny White among others." Marcus Miller – Wurlitzer electric piano (1), synthesizers (1–8, 10–15), vocoder (1, 4), bass guitars (1, 8, 12, 14), drum programming (1–6, 10, 13, 14), scratches (1, 6, 10, 12–13), organ (2, 11), guitars (2, 11), bass guitar (2–4, 7, 9, 11, 15), tenor saxophone (2, 6, 10, 12–14), bass clarinet (2, 5, 7, 9, 10, 13–15), lead vocals (3), acoustic bass (3), vocals (4), Fender Rhodes (4, 7–9, 12), synth bass (4, 15), alto saxophone (4), fretless basses (5), B♭ clarinet (5, 9), fretless bass (6, 10,
```

### Album 180, chunk 2

```text
13), rhythm guitar (7), Roland TR-808 (7), backing vocals (8), clavinet (9), ambient synthesizer (9), talking synth bass (9), electric guitar (10, 13), radio (11), guitar effects (12), percussion programming (12, 14, 15), vibraphone (12), acoustic guitar (13), soprano saxophone (14) Bernard Wright – Fender Rhodes (1, 7), organ (4) Herbie Hancock – acoustic piano (3), acoustic piano solo (5) Paul Jackson, Jr. – acoustic guitar (3, 8), guitars (4), dobro (9) Hiram Bullock – lead guitar (7), guitars (12, 15) Leroy Taylor – synth bass (2, 7, 12), Fender Rhodes (15) Poogie Bell – drums (7, 9, 11–12, 15) David Isaac – water effects (1), hi-string note (1), tom overdubs (7), cowbell (7), triangle (7), percussion programming (11) Mino Cinelu – percussion (6, 8–10, 13) Kenny Garrett – alto saxophone (2, 12), alto sax solo (7, 15) Branford Marsalis – soprano sax solo (2, 8) Hubert Laws – flute solo (2), flute (9) Wayne Shorter – soprano saxophone (9), soprano sax solo (13) Fred Wesley – trombone (7), trombone solo (12) Michael "Patches" Stewart – trumpet (2–3, 7) Larry Corbett – cello (1–3, 7, 9, 13–14) Matt Funes – viola (1, 3, 7, 9, 12, 14) Joel Derouin – violin (1, 3, 12, 14) Lenny White – brush fills (2) Raphael Saadiq – lead vocals (3) Nikki Miller – vocals (4) Vinnie Colaiuta – drums (8) Djavan – scat vocals (8) James Carter – tenor sax solo (11) Maceo Parker – alto sax solo (12) Chaka Khan – vocals
```

### Album 180, chunk 3

```text
(14) Harold Goode – executive producer Harry Martin – executive producer Marcus Miller – executive producer, producer, recording David Isaac – co-producer, recording, mixing (3, 11, 14, 15) Khaliq-O-Vision – recording, mixing (3, 11, 14), vocal recording (15), assistant engineer Ray Bardani – mixing (1, 2, 4–10, 12, 13) Paul Mitchell – recording Malcolm Pollack – recording Enrico DePaoli – vocal recording (8) David Hampton – piano recording (3, 5) Danny Romero – vocal recording (3) Michelle Forbes – assistant engineer Richard Furch – assistant engineer Takamasa Honda – assistant engineer Alexandre Reis – assistant engineer Charles Harrison – string copyist, string transcription Bibi Green – production coordination Jack Frisch – art direction, design Kumiko Higo – photography Jack Leitenberg – management David Passick – management
```

## Album 181: Dead Winter Dead — Savatage

- **album_id:** `16cec9be-5d66-46ab-9172-6baaecbba6eb`
- **Tags (identification only):** heavy metal, rock, 1–4 wochen, 90s, english, offizielle charts, progressive metal, rock opera
- **Chunks:** 6 (1516 words)

### Album 181, chunk 1

```text
Dead Winter Dead is the ninth studio album by the American heavy metal band Savatage, released in 1995. It is a concept album, that tells a story from the perspectives of a Serb boy, a Bosniak girl and an old man. The story of the album is set during the Bosnian War, which was ongoing at the time. Dead Winter Dead marked the first Savatage album to feature guitarist Chris Caffery, who had been an occasional and touring member of the band since 1987, but had become an official permanent member by the time the album was recorded. Alex Skolnick, who had played guitars on Savatage's previous album Handful of Rain, opted not to stay around for the next album in order to concentrate on his solo band. Singer Jon Oliva took drummer Jeff Plate from the Handful of Rain tour, and brought in his old friend Caffery, former member and Doctor Butcher member to join the band. Atlantic Records also felt that the band needed a second, more well-known guitarist to complete the line-up. Al Pitrelli, formerly a member of Alice Cooper's touring band, became the co-lead guitarist for the band. This record gave the band an unexpected radio hit in "Christmas Eve (Sarajevo 12/24)", and the band decided they wanted to explore this kind of music in a different way. Around this time, Paul O'Neill, along with Robert Kinkel, was interested in starting up what became the Trans-Siberian Orchestra (TSO). It was later re-released by TSO as "Christmas
```

### Album 181, chunk 2

```text
Eve/Sarajevo 1994" on their first release, Christmas Eve and Other Stories. The track "Mozart and Madness" quotes directly from the opening theme of Mozart's Symphony No. 25, and was re-recorded as "Mozart and Memories" as released on the later TSO album "Night Castle"; whilst "Memory" quotes directly from the fourth movement of Beethoven's 9th symphony ("Ode to Joy"). In the Bosnian capital of Sarajevo, there is a town square surrounded by buildings that were constructed during the Middle Ages. The square has a beautiful stone fountain at its center and at one corner there is a thousand year old church with a gargoyle carved into its belfry. This gargoyle, for the last thousand years, has spent all his time trying to comprehend the human emotions of laughter and sorrow, but even after a millennium of contemplation, these most curious of human attributes remain a total mystery to him. Our story begins in the year of 1990; the Berlin Wall has just fallen, communism has collapsed and for the first time since the Roman Empire, Yugoslavia finds itself a free nation. Serdjan cannot believe his good fortune to be alive and young at such a moment. The future and the happiness of all seem assured in what must surely be "the best of times" ("Sarajevo", "This Is the Time"). However, even as Serdjan celebrates with his fellow countrymen, there are little men with little minds who are already busy sowing the seeds of hate between neighbors. Young and impressionable Serdjan joins
```

### Album 181, chunk 3

```text
some of his friends in a Serbian Militia Unit and eventually finds himself in the hills outside of Sarajevo firing mortar shells nightly in the city ("I Am"). Meanwhile, in Sarajevo itself, Katrina Brasic, a young Muslim girl, finds herself buying weapons from a group of arms merchants and then joining her comrades firing in the hills around the city ("Starlight", "Doesn't Matter Anyway"). The years pass by and it is now late November 1994. An old man who had left Yugoslavia many decades before, has now returned to the city of his birth, only to find it in ruins. As the season's first snowfall begins, he stands in the town square, looks toward the heavens and explains that when the Yugoslavians prayed for change, this is not what they intended ("This Isn't What We Meant"). As the old man finishes his prayer, the sun begins to set and the first shells of the evening's artillery barrage are starting to arc overhead. But instead of heading for the shelters with the rest of the civilians, he climbs atop the rubble that used to be the fountain and taking out his cello, starts to play Mozart as the shells explode around him. From this night forward he would repeat this ritual every evening. And every evening Serdjan and Katrina each find themselves listening to the thoughts of Mozart and Beethoven as they drift between the explosions across no man's land ("Mozart and Madness", "Memory"). Though the winter does its best to
```

### Album 181, chunk 4

```text
cover the landscape with a blanket of temporary innocence, the war only escalates in violence and brutality ("Dead Winter Dead"). One day in late December, Serdjan on a patrol in Sarajevo, comes across a schoolyard where a recent exploding shell has left the ground littered with the bodies of young children. It is one thing to drop shells into a mortar and quite another to see where they land. Long after Serdjan returns to his own lines, he cannot get the faces of the children out of his mind. Realizing that what he has been participating in is not the glorious nation building that their leaders had described, but rather a path to mutual oblivion, he decides right then and there that he can no longer be a part of this, that you cannot build a future on the bodies of others. At the first opportunity, he resolves that he will desert ("One Child"). Sitting in his bunker on December 24, he listens to the sounds of Christmas carols from the old cello player mingling with the sounds of war. Katrina, on the other side of the battlefield, is also listening. It had just stopped snowing and the clouds had given way to reveal a beautiful star-filled sky when suddenly the cellos player's music abruptly ceases. Fearing the worst, Serdjan and Katrina both do something quite foolish and from their respectives sides, start to make their ways across no man's land toward the town square. Arriving at exactly the same
```

### Album 181, chunk 5

```text
moment, they see one another. Instinctively realizing that they are both there for the same reason, they do not start to fight, but instead, together walk slowly to the fountain. There they find the old man lying dead in the snow, his face covered with blood, his cello lying smashed and broken at his side ("Christmas Eve (Sarajevo 12/24)"). Then without warning, a single drop of liquid falls from the cloudless sky, wiping some of the blood off the old man's cheek. Serdjan looks up, but he can see nothing except the stone gargoyle high up on the church belfry. Overcome by what he has seen this night, he decides that he must leave this war immediately. Turning to the Muslim girl he asks her to come with him, but now all she sees is his Serbian uniform. Pouring out his feelings, he explains that he is not what she thinks that he is. Eventually winning her to his side, they leave the night together ("Not What You See"). In a contemporary review, Matthias Breusch of Rock Hard magazine remarked how the album is the band's "most significant move so far in the direction of classical-symphonic bombast compositions" with "piano and string arrangements (...) omnipresent", even if "dedicated fans" would miss the "fine line between genius and madness, on which the interaction of the two Oliva brothers up to and including Edge of Thorns has driven every Savatage album." He judged "the instrumentals 'Overture: Sarajevo', 'Mozart and Madness' and 'Christmas
```

### Album 181, chunk 6

```text
Eve'" and the quieter numbers, "like the exquisite 'This Is Not What We Meant', 'Now What You See', 'This Is the Time' or 'One Child'", the true highlights of the album, while he considered the title track "somewhat lethargic" and the uptempo songs "mediocre". Modern reviews are positive. AllMusic reviewer wrote that "Savatage have built upon the musical ground of Handful of Rain with grand but heavy arrangements of theatrical and complex pieces", resulting in "something that could appear in many a Broadway show" and with the music nicely capturing "the wide range of emotion that the narrative calls for." In fact, Sputnikmusic reviewer declared that "Dead Winter Dead really feels like a sort of heavier, more vocally-driven first Trans-Siberian Orchestra album", but also "true to metal form with plenty of aggressive vocals and fast, heavy riffs" establishing "war as the predominant atmosphere." Martin Popoff in his review for The Collector's Guide to Heavy Metal wrote that Dead Winter Dead is simply "a great piece of theatre, elegant, expressive, guitar-driven storytelling of the highest order", making "one of the most forceful concept records going, not so much sad as it might have been, but imposing." Zachary Stevens – lead vocals Jon Oliva – keyboards, lead vocals on "I Am" and "Doesn't Matter Anyway", backing vocals on "Starlight", co–producer Al Pitrelli – guitar, backing vocals Chris Caffery – guitar, backing vocals Johnny Lee Middleton – bass guitar, backing vocals Jeff Plate – drums Bob Kinkel – additional keyboards, engineer Mary Wooten – solo cello Paul O'Neill – producer Dave Whittman – mixing Ben Arrindell – mixing assistant
```

## Album 182: Hints Allegations and Things Left Unsaid — Collective Soul

- **album_id:** `1a8206a9-e2b2-4e83-8b6a-c4efc388ce2f`
- **Tags (identification only):** alternative rock, alternative and punk, rock, 90s, alternative, american trad rock, hard rock, pop/rock
- **Chunks:** 4 (840 words)

### Album 182, chunk 1

```text
Hints Allegations and Things Left Unsaid is the debut studio album by American rock band Collective Soul. It was originally released on the band's self-owned label called Rising Storm Records in 1993. Collective Soul later signed on with Atlantic Records, and the album was re-released in 1994 under the Atlantic label. The track "Shine" gained the band attention thanks to college radio. The cover art is a modified version of an advertising image from the 19th century, with the text on the sign changed. Hints Allegations and Things Left Unsaid was recorded in a basement in 1992 as a promotional demo. Frontman Ed Roland hoped to simply sell the songs to a publishing company rather than form a band. He gave the demo to a small college radio station in Atlanta that began playing "Shine". The track quickly became their most requested song and the band was asked to perform some concerts for the station. Favoring an opportunity to perform a few shows with his brother, Roland agreed and regathered the demo's guitarist (Ross Childress) and drummer (Shane Evans) as well as his brother Dean. On the original Rising Storm pressing of the album, David Neal is credited as bassist. He would eventually be replaced by Will Turpin. Prior to Collective Soul, Ed Roland had performed in the band Marching Two-Step alongside Evans. In order to make Hints Allegations and Things Left Unsaid feel more like a "band effort", three songs that were conceived during the Marching Two-Step era were
```

### Album 182, chunk 2

```text
included on the album: "Goodnight Good Guy", "Love Lifted Me", and "Scream". The album was essentially self-released by the band, as Rising Storm Records was simply a moniker used by the band and their manager Bill Richardson. The attention gained by "Shine" allowed it to chart and catapulted the band to national stardom. They were soon picked up by Atlantic Records who wished to release the demo as the debut studio album of Collective Soul. In a 1995 interview, Roland elaborated on his mixed feelings regarding the situation: "It wasn't even remixed. It was the same demo. Before we got signed we'd already charted with 'Shine.' Once we got signed I said, 'We want to re-record. This is not a band recording.' But they said, 'You're gonna lose momentum. You're looking at a three to five month process. So let's go with it and you can get your next record out quick.' We thought it would be great to sell 10-20,000 units. [When it went gold], we were sitting there with our eyes wide open." Consequently, Collective Soul would regard their self-titled 1995 studio album under Atlantic as the band's official debut. Roland told Metal Edge, "It's so funny for people to compare the two. It's like comparing one band to another band. [Collective Soul] is our first record, flat out." The album was produced by Matt Serletic, becoming his first production success, and who would then subsequently go on to much wider fame producing all of Matchbox 20's releases
```

### Album 182, chunk 3

```text
as well as those by their frontman Rob Thomas, including his Santana collaboration "Smooth". Hints Allegations and Things Left Unsaid featured three singles, the most successful of which was "Shine". Aside from radio popularity, the song also had a music video which received heavy airplay on MTV. The follow-up single, "Breathe", moderately charted in the US as well. Collective Soul performed at Woodstock 1994 and opened for Aerosmith during their Get a Grip Tour. The album gained overall positive reception from critics. It was given credit for its strong melodies but a less savory response regarding its apparent lack of originality. Also of note was Collective Soul's more upbeat sound amidst their more angst, grunge-influenced contemporaries. Chuck Eddy of Entertainment Weekly gave a somewhat sarcastic review, describing the album as "bubble-gum grunge: an idea whose time has come." In The Village Voice, Robert Christgau was even more negative, singling it out in Consumers Guide "Turkey Shoot" feature as a "Must to Avoid", an example of "...mediocre pseudoalternatives from every corner of this embittered, all too grateful land of ours." Ed Roland – lead vocals, guitar Dean Roland – rhythm guitar Ross Childress – lead guitar, backing vocals Will Turpin – bass, backing vocals (credited on the Atlantic pressing, but he doesn't play bass); percussion on "Heaven's Already Here" (Rising Storm pressing) Shane Evans – drums David Neal – bass (credited only on the Rising Storm pressing) Matt Serletic – keyboards, trombones and string arrangements on "Sister Don't Cry", "Pretty Donna",
```

### Album 182, chunk 4

```text
and "Beautiful World" Joe Randolph – guitar on "Goodnight, Good Guy", "Love Lifted Me", and "Scream" Brian Howell – bass on "Scream" Melissa Ortega – solo violin on "Wasting Time" Jun-Ching Lin – leader, violin I David Braitberg – violin II Paul Murphy – viola Daniel Laufer – cello Ed Roland – producer, mixer, and engineer (all tracks) Matthew Serletic – producer, mixer, and engineer (tracks 4, 8, 10, 14); mastering Joe Randolph – producer (tracks 5, 11) Bill Richardson – executive producer Mike Childers – digital editing, artwork, DTP
```

## Album 183: Hourglass — Dave Gahan

- **album_id:** `0552b6bb-3dc1-4612-b87b-501711485326`
- **Tags (identification only):** electronic, pop rock, rock, alternative dance, alternative rock, rock and indie, synth pop
- **Chunks:** 3 (745 words)

### Album 183, chunk 1

```text
Hourglass is the second solo studio album by English singer Dave Gahan, released on 17 October 2007 by Mute Records. It received generally favourable reviews; most critics complimented its electronica sound, while some criticised it for sounding too similar to Gahan's group Depeche Mode. At Metacritic, which assigns a normalised rating out of 100 to reviews from mainstream critics, the album received an average score of 64, based on 18 critical reviews, which indicates "generally favorable reviews". Ben Hogwood of musicOMH wrote, "Gahan, it seems, is progressing into a well-rounded, mature songwriter who plays to all his strengths, and in particular the cracked voice, and its ability to move from a confidential whisper to a rabble-rousing bellow. These songs show him in a newly redemptive prime and will satisfy both short and long term devotees". David Jeffries of Allmusic praised the album and felt it was "a more electronic, better built, and altogether better deal than Monsters, thanks mostly to the singer and-don't-you-forget-to-mention songwriter's better sense of self." "Hourglass doesn't have any overly urgent need to shake off Depeche Mode comparisons. Instead, it surrounds Gahan's serviceable writing skills with the dark electronic soundscapes he's obviously comfortable with." only criticising "Cringe-worthy couplets like "Miracle's "I don't believe in Jesus/But I'm praying anyway." find Gahan writing in the style of Gore and coming up short." Marc Hawthorne of The A.V Club observed "Dave Gahan's second solo disc should find love from anyone who can recite from memory the albums after Songs Of
```

### Album 183, chunk 2

```text
Faith And Devotion. Everyone else will be indifferent. That doesn't mean it deserves to be ignored—two decades removed from his band's creative peak, Gahan has actually made one of the year's best-sounding electronic releases," concluding, "But when all is said and done, Hourglass simply lacks the exciting moments that got him here. A major exception is "A Little Lie," whose hook is like a mechanized version of the sax in The Psychedelic Furs' "Dumb Waiters." But trapped down at track nine, it feels like an anomaly." Al Spicer of BBC praised Gahan's vocals saying, "Covering the emotional gamut from tearful regret to sated melancholy - at times with more reverb than strictly necessary - Dave’s voice is the album’s strongest, most memorable facet; the perfect vehicle with which to acknowledge one’s sins, invoke divine protection and beseech forgiveness. Gahan’s control and masterful delivery show that years of the rock star lifestyle left no lasting damage: if anything, the slight rasp of maturity lends an air of authentic experience that his work with Depeche Mode only hinted at." Caroline Sullivan of The Guardian gave a 4 star rating saying "Dave Gahan's second solo outing is reliably bleak, probing the murk of his post-heroin-addiction mind as you'd expect, but achieving a kind of magnificence, too. A return from Paper Monsters' grungy guitars to uncompromising electronica works very well, elevating Gahan's morose thoughts into frigid symphonies. His remarkable voice fills in occasional gaps in the songwriting (the most nagging being a lack of
```

### Album 183, chunk 3

```text
hooks that contrasts unfavourably with the chorus-laden tunes of Depeche Mode's Martin Gore) and induces goosebumps, too." Benjamin Boles of Now was more negative in his review saying "Depeche Mode frontman David Gahan's second solo disc is closer to the electro-pop vibe of his better known project than that of his first solo outing, for which DM fans will likely be grateful. Unfortunately, he's not as good a songwriter as Martin Gore, and this has a shortage of decent hooks." calling it "a bit of a mopefest" and saying "Some songs start out peppy and intriguing, but his moaning over top sucks all the life out of the groove."concluding, "Hardcore Depeche Mode fans will likely find more to like, but it's hard to imagine any but the most rabid really loving it." Dave Gahan – vocals John Frusciante – guitar solo (track 1) Graham Finn – bass (track 2); guitar (track 4) Tony Hoffer – guitar (track 9) Niko Stoessl – additional guitar (tracks 2, 6); backing vocals (track 6) Kevin Murphy – cello on "Saw Something" (track 1) Jenni Muldaur – backing vocals (track 10) Karl Ritter – Dobro (track 10) Dave Gahan – production Christian Eigner – production Andrew Phillpott – production Tony Hoffer – mixing (all tracks); engineering (track 9) Andy Marcinkowski – mixing assistance (all tracks); engineering (track 9) Ryan Hewitt – recording (track 1) Niko Stoessl – additional editing (tracks 2, 6) Kurt Uenala (K10K) – additional editing, additional engineering
```

## Album 184: The Good the Bad and the Funky — Tom Tom Club

- **album_id:** `93863b02-6f8f-453e-b7ec-8df08a5373aa`
- **Tags (identification only):** downtempo, electronic, pop, awesome name, dance pop, dancehall, disco, dub
- **Chunks:** 1 (111 words)

### Album 184, chunk 1

```text
The Good, The Bad, and the Funky is the fifth studio album of the Tom Tom Club. A remix of the album's second track, "Who Feelin' It?", was featured in the 2000 dark comedy American Psycho as the "Philip's Psycho Mix". Bernie Worrell – organ, clavinet Chris Frantz – drums, percussion, keyboards, loops, vocals Toots Hibbert – vocals Abdou M'Boup – percussion, kora Doug McKean – mixing, sample arrangements Steve Scales – mixing, conga Tina Weymouth – organ, synthesizer, synthesizer bass, piano, acoustic guitar, bass, vocals Bruce Martin – keyboards Charles Pettigrew – vocals Robby Aceto – electric guitar, guitar effects Sergio Rotman – electric guitar, saxophone Mystic Bowie – toasting
```

## Album 185: The Pod — Ween

- **album_id:** `04b157fa-a56b-40a7-af4c-240b0bf39972`
- **Tags (identification only):** lo fi, rock, alternative rock, avant garde, experimental rock, noise rock, psychedelic rock, comedy rock
- **Chunks:** 4 (818 words)

### Album 185, chunk 1

```text
The Pod is the second studio album by American rock band Ween. It was released on September 20, 1991, by Shimmy-Disc. The album was recorded from January to October 1990, at the Pod on Van Sant Road in Solebury Township, Pennsylvania. Recording concluded one month prior to the release of their debut on November 16. The album was derived from two tapes titled the Bilboa tape and the Big Timmy Wasserman tape. Both tapes contain not only demo versions of songs on the album, but many outtakes not used on any album or tracks used on future albums. All of the songs have a muddy quality to them, due to being recorded on a Tascam four-track cassette recorder, and many of the vocals are manipulated in strange ways. The album contains bizarre lyrical content, often attributed to the fact that Dean and Gene both came down with cases of mononucleosis during the recording of the album, as well as their alleged relationship with huffing Scotchgard. However, when their fans began huffing Scotchgard, it was refuted by Gene Ween and Dean Ween themselves as being "the most slime-bag thing we could think of." Robyn Hitchcock is credited with "musical inspiration" for the track "Alone", which borrows elements from his song "Bones in the Ground". The track "Pollo Asado" is a comedic skit with a man ordering Mexican food over music. The song was inspired by Gene Ween's time briefly working at a Mexican restaurant in New Hope, Pennsylvania. The album takes
```

### Album 185, chunk 2

```text
its name from the band's apartment where the album was recorded, which the band nicknamed "The Pod". The album's cover art is a takeoff of the 1975 The Best of Leonard Cohen cover; Ween simply positioned a photo of part-time bassist Mean Ween's head wearing a Scotchgard powered bong (known as a “Jammy Pac”) over Cohen's cover art, and altered the title text and other graphics. The copy of the Leonard Cohen record that Ween used had purportedly belonged to Deaner's mother. From the Shimmy-Disc CD: "Recorded by Dean and Gene Ween on a Tascam four-track cassette recorder between January and October 1990. All songs recorded at the Pod, where we lived for a year and 10 months (with our cat Mandee). The Pod was scenically located on Van Sant Road in Solebury Township, Pennsylvania. Our apartment was a haven for flies because it sits in the middle of a horse farm. In the time this album was completed, we filled up 3,600 hours of tape, and inhaled 5 cans of Scotchgard. This album was then produced and mixed by Andrew Weiss (our pal) at the Zion House of Flesh, Hopewell, New Jersey. Straight to DAT Mang. Mean Ween played the bass on "Alone" and that's him on the cover doin' up some Scotchguard powered bongs. We got evicted on October 1, 1991. But Dave Ayers says he's gonna help us out. Cover and art designs by Logarithms." The Pod produced three music videos. "Pollo Asado", "Captain Fantasy", and "Pork
```

### Album 185, chunk 3

```text
Roll Egg and Cheese" were included on a VHS music video compilation titled Shimmy-Disc Video Volume 3. Shimmy-Disc Video was a series of VHS tapes created by Shimmy Disc containing music videos from artists who were signed to the label. These tapes were never remastered or re-released, nor were the music videos. Shimmy-Disc released a vinyl version of The Pod in 1991. It was also remastered and reissued by Elektra Records in 1995, after the relative success of Ween albums such as Pure Guava (1992) and Chocolate and Cheese (1994). In 1993, the album was named one of the 20 best albums of 1992 by Spin. Trouser Press wrote: "Less inflamed and inspired than the first album (blame, perhaps, the five cans of Scotchguard the band claims to have inhaled), The Pod lurches, howls, fuzzes and strums through sloppy creations that are mostly one hit short of a high." In a 1999 review of the album, The Stranger called it "excellent" and wrote that "someday, classical music students will write dissertations on The Pod." Kerrang! wrote that "the electrified production on tracks like 'Dr. Rock' and 'Sketches of Winkle' is utterly unhinged, while the barking, aimless pace of 'The Stallion' (either part, really) feels like the sweaty blatherings of the most poisonous of drunks." In a September 1992 Spin interview, Faith No More singer Mike Patton mentioned it as one of his favorite albums, and around this time his band also did live covers of the Pure Guava track "The
```

### Album 185, chunk 4

```text
Goin' Gets Tough From the Getgo". In later years, Aphex Twin named it one of his 10 favorite albums of all time (making it one of two Ween albums on the list, the other being Pure Guava). Dean Ween – vocals, acoustic & electric guitar, bass guitar, keyboards, drum machine Gene Ween – vocals, acoustic guitar Mean Ween - bass guitar on “Alone” Andrew Weiss – producer, mixing
```

## Album 186: Let It Loose — Gloria Estefan

- **album_id:** `f669aff1-e2ab-457a-b88a-48c139a61e9e`
- **Tags (identification only):** adult contemporary, dance pop, electronic, female vocal, latin, latin pop, pop, ballad
- **Chunks:** 1 (134 words)

### Album 186, chunk 1

```text
Let It Loose (also released as Anything For You) is the tenth studio album by Gloria Estefan and Miami Sound Machine, released in 1987. It is the first studio album to feature a specific credit for Estefan, but is her 10th album overall including her work with Miami Sound Machine. It is Miami Sound Machine's most commercially successful album, being certified triple-platinum by the RIAA and peaking at number six on the Billboard 200. The album includes the top 5 Billboard Hot 100 singles "Rhythm Is Gonna Get You", "Anything for You", and "1-2-3", in addition to "Betcha Say That" and "Can't Stay Away from You". Following the success of the single "Anything for You", the album was reissued with new artwork as Anything For You across Europe, South Africa, Australia, and New Zealand.
```

## Album 187: Tomahawk Technique — Sean Paul

- **album_id:** `f6d02d54-e9cd-4a3a-8238-37829887968c`
- **Tags (identification only):** dancehall, dance pop, electro house, pop, pop rap, ragga, reggae
- **Chunks:** 3 (695 words)

### Album 187, chunk 1

```text
Tomahawk Technique is the fifth studio album by the Jamaican rapper and singer Sean Paul. It was released by his label Dutty Rock Productions, VP Records, and Atlantic Records in several countries beginning on 24 January 2012, with a US release in September 2012. Tomahawk Technique was nominated for Best Reggae Album at the 55th Annual Grammy Awards, earning Paul his second nomination in that category after Imperial Blaze (2009). Sean said to the music blog Rap-Up that Akon, Stargate, DJ Ammo, Benny Blanco, and Kelly Rowland, would appear on the album. "There's a broadening of my artistry, I’m working with other producers and artists I’ve never worked with," the Jamaican DJ told Reuters at the recent KIIS FM Jingle Bell Ball in Los Angeles. Tomahawk Technique follows the success of the singer's 2009's record Imperial Blaze. For the new CD, he has teamed up with producers Rico Love, Benny Blanco and Stargate, who have been behind artists such as Katy Perry, Rihanna and Natasha Bedingfield, to work on his new album. "What’s going to surprise fans is that there’s a lot more singing, more high notes that I never used to do before," said Paul, adding "it’s a mixture of pop music into dance music." "I’m trying to bridge the gap, broaden my artistry," Sean told Rap-Up TV. "I’m asking [the producers] to try and make dancehall from their perspective. So it’s sounding more international than dancehall." The album's Japanese version features an upcoming Jamaican singer/songwriter, Zia Benjamin, as
```

### Album 187, chunk 2

```text
well as a remix of the song "Dream Girl" featuring Japanese artiste, Lecca. The first single "Got 2 Luv U" features vocals from American singer Alexis Jordan. It was released on 19 July 2011 by Atlantic Records. The song was written by Sean Paul, Ryan Tedder and Stargate, and Stargate produced it. It reached number 1 in Switzerland and the Top 10 in several countries worldwide. "She Doesn't Mind" was released as the second single taken from Tomahawk Technique. It was written by Sean Paul, Shellback and Benny Blanco and was produced by Shellback and Benny Blanco. It was released on 29 September 2011 on NRJ & Skyrock (French radios), and to iTunes on 31 October. Like its predecessor, "She Doesn't Mind" topped the Swiss Singles Chart as well as the Austrian Singles chart and reached top-ten in many other European territories. "Hold On" was released as the third single in February 2012. It reached number 1 in Belgium and number 35 in France. "Dream Girl (remix)" featuring Lecca was released as a single in Japan on 28 March 2012 while in the United States, "How Deep Is Your Love" featuring Kelly Rowland was released as the fifth single on 24 July 2012. The single has so far reached number seventy-two in Switzerland. The Guardian editor Paul MacInnes described Tomahawk Technique as a "clash of powerful forces: the irrepressible charm of Sean Paul against the intolerable global pop sound. Who will win: the Jamaican star whose 2003 Dutty Rock album
```

### Album 187, chunk 3

```text
brought dancehall to the charts, or the squealing, amped-up trance that is ubiquitous in 2012, from Rihanna to LMFAO? The head says the latter." AllMusic critic David Jeffries wroe that Tomahawk Technique "feels like a play for the world with its Black Eyed Peas and Flo Rida-styled club tracks, the best of which has to be the slow-stepping "Got 2 Luv U." [...] A couple more true dancehall tracks would have made this feel more natural. Straying far from home, Tomahawk Technique isn't an awful Sean Paul album, but it is an odd one." NME's Rebecca Schiller found that "sadly, his creative decline continues on his fifth studio album, Tomahawk Technique, which is – trance'n'b-meddling album lowlight "Touch The Sky" aside – a lacklustre collection of what sounds like pallid versions of previous hits. Missile launch failed." Anupa Mistry, writing for Now, felt that "it's been sad to see Sean Paul ditch that sexed-up specificity for shameless, sanitized synth pop in the key of, like, everyone else. Past the dancehall signifiers (Paul's increasingly strained lilt and tepid syncopated pulse), the new record is brazenly mediocre. When you’re finished pretending to care, put on Popcaan instead."
```

## Album 188: Reborn — Living Sacrifice

- **album_id:** `5c1feb28-de66-4218-ae20-271e078fb3b8`
- **Tags (identification only):** alternative metal, christian metal, heavy metal, pop/rock, punk/new wave, hardcore punk
- **Chunks:** 2 (306 words)

### Album 188, chunk 1

```text
Reborn is the fourth album by the Christian metal band Living Sacrifice. The album was released in 1997, and later re-released and remastered in 2004. In 2020, the band announce a vinyl re-release of Reborn, which sold out quickly. Reborn saw a drastic separation from their previous style, dropping most of the death metal sound of Nonexistent and Inhabit, in favor of more of a metalcore and hardcore punk sound. The album was well-received by the metalcore and hardcore scene, whereas the death metal scene predominantly disregarded it. The album is widely considered as Living Sacrifice's biggest album. Stephen Thomas Erwine of AllMusic wrote "...the average metal fan will find much here of interest, particularly the pummeling riffs and shredding solos." Fred Keel of Jesus Freak Hideout stated "Reborn is a Christian metal masterpiece recommended for fans of Demon Hunter and Becoming the Archetype." Alex Figgis of Cross Rhythms, for the review of the original Reborn album, gave 10/10 and reported "They leave the listener in no doubt as to their heartfelt desire to share the gospel with those who have ears to hear; tacking the wisdom of the world head on with the seemingly foolishness "I God in Christ, with us much subtlety as a sledge hammer." Tony Cummings, also of Cross Rhythms reviewing the reissue, also gave the album 10/10. "For more enlightened hard rock lovers, here's a chance to hear again a Christian hard music classic in all its brutal glory and catch that master guitarist, Jason
```

### Album 188, chunk 2

```text
Truby, in pre-P.O.D. days, in the process." There were also several reviews from Cornerstone Magazine, Garlic Press, HM Magazine, 7Ball, and YouthWorker. Bruce Fitzhugh - vocals, rhythm guitar Jason Truby - lead guitar, backing vocals Chris Truby - bass guitar Lance Garvin - drums, percussion Barry Poynter - recording, engineer, mixing Brandon Ebel - executive producer
```

## Album 189: Common One — Van Morrison

- **album_id:** `514b3936-ed20-488d-b4c2-33a8293c07c3`
- **Tags (identification only):** r and b, blues rock, rock, adult contemporary, album rock, blue eyed soul, contemporary pop/rock, folk rock
- **Chunks:** 4 (917 words)

### Album 189, chunk 1

```text
Common One is the twelfth studio album by Northern Irish singer-songwriter Van Morrison, released in 1980. The album was recorded over a nine-day period at Super Bear Studios, near Nice, on the French Riviera. Its title is in the lyrics of the song "Summertime in England": "Oh, my common one with the coat so old and the light in her head". The 2008 re-issued and re-mastered version of the album contains alternate takes of "Haunts of Ancient Peace" and "When Heart Is Open". Apart from polarising critics on its initial release, Common One has been cited by Morrison himself as his favourite of his own albums. According to Mick Cox the early stages of the album were rehearsed during November and December 1979. The songs "Summertime in England" and "Haunts of Ancient Peace" were rehearsed by Morrison and the band during small gigs in January 1980. Cox thought that "some of these performances at the rehearsals were far better than the final recordings." Speaking of the recording sessions at Super Bear, Cox said: "We were all ensconced in a very, very intense, highly charged situation for those eleven days, but it did bring out that album." Jef Labes recalled about his arrangements on the album: "... but what I always tried to do with string arrangements for him was to just try to mimic what he was singing, 'cause he was such a song instrument." In contrast to many of his previous albums, Common One ventures more into the realms
```

### Album 189, chunk 2

```text
of free jazz than the usual Van Morrison R&B, with the sax playing of Pee Wee Ellis coming to the fore. The songs are also somewhat longer than on his previous albums. Morrison said that the original concept was even more esoteric and was heavily influenced by his reading of nature poets. The opening track, "Haunts of Ancient Peace" was named from a (1902) book by Alfred Austin (Poet Laureate 1896–1912), and features the twin brothers of Morrison's voice against the answering saxophone of Pee Wee Ellis, with the trumpet of Mark Isham. "Summertime in England" was the longest track and proved to be a successful live performance for some time to come. Morrison said it "was actually a part of a poem I was writing and the poem and the song sort of merged." The lyrics include images of Wordsworth and Coleridge "smokin' up in Kendal" (Brian Hinton says they are "smokin' with poetry not spliffs"). It ends with the music being brought down to nothing and the words, "Can you feel the silence?" "Spirit" played with sudden tempo changes and the ending fifteen-minute track, "When Heart Is Open", was experimental in form with elements of melody from Miles Davis's In A Silent Way. It is free tempo (presaging the era of New-age music). Critical response to Common One was divided. Graham Locke reviewed it in NME calling it "colossally smug and cosmically dull; an interminable, vacuous and drearily egotistical stab at spirituality". Dave McCullough wrote in Sounds: "For
```

### Album 189, chunk 3

```text
the fan, as I am myself, it's not even possible to romanticize and say that Morrison has lost his way temporarily, so stern and so acute is his departure." Rolling Stone critic Tom Carson named "Satisfied" as the record's only "masterpiece", in which "the simplicity that Morrison is striving for arrive as something natural and effortless, as a gift of grace". Clinton Heylin contends that Morrison was bruised by the reaction and "would not attempt anything quite so ambitious again." In 1982, Lester Bangs argued for a reassessment, saying, "Van was making holy music even though he thought he was, and us rock critics had made our usual mistake of paying too much attention to the lyrics." Also in 1982, The Boston Phoenix's John Piccarella wrote that "Common One was probably Morrison’s richest record (rich like haute cuisine), brighter and sunnier than predecessors Astral Weeks and Veedon Fleece, lusher and elevated far above most people’s tolerance for elated sentiment. American critics voted it the 27th best album of 1980 in The Village Voice's annual Pazz & Jop poll. In an accompanying essay, poll supervisor Robert Christgau wrote, "As somebody who considers Moondance an apotheosis and has never gotten Astral Weeks, I think this is his worst since Hard Nose the Highway – sententious, torpid, abandoned by God. I know lots of Astral Weeks fans who agree. But Morrison has a direct line to certain souls, and they still hear him talkin'." In retrospect, he deemed "Satisfied" and "Summertime in England"
```

### Album 189, chunk 4

```text
to be the record's highlights. In 2009, Erik Hage said "the dominant critical reaction represented it as prohibitive, sententious, and inaccessible, when in fact it is filled with much melody and beauty." AllMusic later wrote, "No wonder the rock critics of the time didn't get it; this is music outside the pop mainstream, and even Morrison's own earlier musical territory. But it retains its trancelike power to this day." In a 2014 list by Stereogum, ranking all the thirty-two solo Van Morrison albums from worst to best, Common One was placed in the sixteenth position. Van Morrison – vocals, guitar, harmonica Mick Cox – lead guitar Herbie Armstrong – guitar, backing vocals David Hayes – bass guitar, backing vocals John Allair – Hammond organ, piano, Fender Rhodes, backing vocals Pee Wee Ellis – tenor saxophone, alto saxophone, flute Mark Isham – trumpet, flugelhorn Pete Brewis – backing vocals on "Satisfied" with the band Peter Van Hooke – drums Toni Marcus – sitar, violin Mark Jordan – keyboards
```

## Album 190: All My Demons Greeting Me as a Friend — AURORA

- **album_id:** `58370778-4473-45d9-b59e-e8d992b4bb53`
- **Tags (identification only):** art pop, indie pop, chamber pop, indietronica, pop, synthpop, alternative dance, ambient pop
- **Chunks:** 7 (1719 words)

### Album 190, chunk 1

```text
All My Demons Greeting Me as a Friend is the debut studio album by Norwegian singer-songwriter Aurora. It was released on 11 March 2016 by Decca and Glassnote Records. The album followed the release of her debut extended play (EP) Running with the Wolves (2015), which contained two songs that were later included on the album. Aurora collaborated with several producers, including Odd Martin Skålnes, Magnus Skylstad, Nicolas Rebscher, Alf Lund Godbolt, and Electric during its recording. All My Demons Greeting Me as a Friend has been described predominantly as an electropop album, along with folk, electronic, synth-pop, Nordic-folk, and alternative pop that explores fantasy, heartache, life, and death through its lyrics. The album was met with positive reviews from music critics. At the 2017 Spellemannprisen, All My Demons Greeting Me as a Friend won Pop Soloist and was nominated for Album of the Year; the music video of the song "I Went Too Far" won Music Video of the Year. Commercially, the album topped the Norwegian albums chart in its first two-week, while also reaching the top 50 in various North American and European countries, in addition to attaining modest positions on several European charts. The album was certified platinum in Norway and has sold more than 500,000 copies worldwide. Seven singles supported the album, and 6 of which were supplemented by accompanying music videos. "Runaway" became a sleeper hit six years later and peaked at number one on the Billboard Bubbling Under Hot 100 in the United States.
```

### Album 190, chunk 2

```text
The second single, "Running with the Wolves" reached number 72 in Germany, becoming her first song to chart in that country. An acoustic version of "Murder Song (5, 4, 3, 2, 1)" was released in August 2015 while its studio version was released a month later. Her cover of the song "Half the World Away" by Oasis was released for the 2015 John Lewis Christmas advert and included in the album's deluxe edition. The singles "Conqueror" and "I Went Too Far" were released throughout 2016. After receiving attention for its appearance in a closing scene from Netflix's TV series Adolescence, "Through the Eyes of a Child" was released as the album's seventh single in 2025, nine years after its release. Aurora began playing piano at the age of six, but it wasn't until she became nine that she decided to compose her own songs. When a live performance at her high school's leaving ceremony and a recording of her song "Puppet" were uploaded online, it was quickly discovered by a representative of the Norwegian management agency of Artists Made Management. Even though she initially denied the proposal, she accepted it since her mother advised her that "maybe there's someone out there who desperately needs [her music]." In a few hours, both songs received thousands of visits in Norway, which earned Aurora some recognition in her country, in addition to a fan base on Facebook. After releasing a series of non-album singles, she followed with the release of her debut EP
```

### Album 190, chunk 3

```text
Running with the Wolves in May 2015, which received positive reviews from online music blogs and national press. Aurora embarked on a short tour in cities of the United States and the United Kingdom to promote it. Like in Running with the Wolves, most of the album was recorded at Lydriket Studios, located in her native Bergen, while additional recording was taken at The Engine Room and Angel Recording Studios in London. Band members from her live band, Magnus Skylstad and Odd Martin Skålnes produced most of the songs from the album. The songs from the album were written from Aurora's childhood to March 2015, when the album was finished. In early 2016, Aurora featured in British band Icarus' song "Home" and released a cover of David Bowie's "Life on Mars" for the HBO Girls television series. All My Demons Greeting Me as a Friend is mainly an electropop, folk, electronic, synth-pop, Nordic-folk, and alternative pop record, featuring elements of art pop, new age, disco, and trip hop. The album is mostly a collection of experiences that Aurora wrote about while growing up in her native Norway. According to her, the record is mainly "about bad experiences from the past that can be good memories, [and about] come to peace with everything that happened." Lyrical nature themes throughout the record present vivid lyricisms about fantasy, heartache, life, and death. The productions of the record has been characterised as "minimalist" with spacy electronics, pulsating beats, yearning modalities, and synth-driven sounds. Critics
```

### Album 190, chunk 4

```text
compared the record to the music of artists like Björk, Lorde, Lykke Li, Florence Welch, Goldfrapp, and Enya. All My Demons Greeting Me as a Friend opens with the folktronica and synth-pop number "Runaway". The song featured echoing water droplet effects, screeches, and transitions. Aurora has stated that the song takes an influence from Nordic folk music and is about "a girl begging to go home – the only place where she belongs, or just the only place left to go". The second track, "Conqueror", is a synth-pop and electropop song that features "clattering drum beats building towards a euphoric chorus". The track has been described to be "poppy" and "playful", musically upbeat with a catchy percussive beat, sparkling synths, and a battle-ready chorus. The Scandipop song, "Running with the Wolves" serves as the third track. Its lyrics is about "the dawning realisation that the answer is to be found in this world, however damaged it might be". The fourth track, "Lucky", is a piano and organ-led ballad with lyricisms about "someone striving against their inner voice telling them to give in". "Winter Bird" is the fifth track which has been described as a new age-tinged folk, Nordic folk, and "Enya-ambient-folk dream" with nature themed lyrics. The sixth track, "I Went Too Far" is a disco-inflected pop and synth-pop ballad. The ballad has been described as "solemn" with a synth-swirling chorus and dance-insistent beat. "Through the Eyes of a Child" is the seventh track which is also the seventh single
```

### Album 190, chunk 5

```text
from the album. It has been described as an "icily atmospheric" ballad that "showcases [a] lovely piano and voice". The eighth track, "Warrior" has an upbeat uptempo sound that showcases the brighter side of the record with a vulnerable and authentic self-love inspired message. The lyrics are about someone "struggling to let love back into their life". Ninth track, "Murder Song (5, 4, 3, 2, 1)" is a solemn and shimmering ballad with a "creeping" title that has a smooth and synthy minor. Lyrically, the ballad speaks about a mercy killing of a protagonist "recounting the story of her own death". The tenth track, "Home" has been described as a "chilly, almost robotic" song. Eleventh track "Under the Water" and twelfth track "Black Water Lillies", share the same subject about drowning and death within the lyrics. On "Under the Water", the ballad talks about the romanticisation of drowning. The closing track of the standard edition, "Black Water Lilies" follows the same theme as "Under The Water". "Black Water Lilies" features extended notes, reverberating piano, and simple beats, about "overcoming forces both in the natural and mental realms". Aurora initially announced that her debut studio album was expected for release in September 2015, but was later postponed. During that time, she revealed that some of the songs were "less dreamy" and "more happy" in comparison to previous ones and concluded that "it's not just a sad and dark record, there is some hope in it [...] which is nice!" Months later,
```

### Album 190, chunk 6

```text
Aurora announced in January 2016 that the album would be released on 11 March of the same year. The album in its standard and deluxe editions was issued on 11 March 2016, by Decca and Glassnote Records. An international deluxe edition was released digitally for several countries on 26 August 2016. To promote the album, Aurora performed at the 2015 Nobel Peace Prize Concert, saying that she and her family "have been following it from the living room at home for many years", and "it is an incredibly beautiful thing to be a part of." Her presentation was praised by the concert's host Jay Leno. She has played a sold-out headline show in London and supported Of Monsters and Men at Brixton Academy in November 2015. On 14 March 2016, Aurora made her American television debut on The Tonight Show Starring Jimmy Fallon, performing "Conqueror", which was later performed on Conan. She also starred in her own short documentaries: "Into the Light" and "Nothing is Eternal", directed by Isaac Ravishankara and produced by The Fader. She also partnered with YouTube for a creative content distribution program, becoming the first in a series of emerging artists. In September 2026, Aurora announced the re-release of All My Demons Greeting Me as a Friend under the subtitle The Moth Tapes, which released on 25 September in celebration of its tenth anniversary. The unreleased title track was released on 2 September, and the reissue includes demo versions of "The Silent Twins", "Running with the
```

### Album 190, chunk 7

```text
Wolves", and "Let Me Heal You". All My Demons Greeting Me as a Friend received further promotion from her second headlining concert tour, the All My Demons Tour, which began on 1 February 2016 in Manchester, United Kingdom. All My Demons Greeting Me as a Friend received generally positive reviews from music critics. At Metacritic, which assigns a normalised rating out of 100 to reviews from mainstream critics, the album received an average score of 80, which indicates "generally favorable reviews", based on 10 reviews. Writing for Entertainment Weekly, Madison Vain commended Aurora's vocals and production and added that the record "channels a similar magical vibe as the art-pop superstar [Björk]". The song "Conqueror" received particular praise as being "simply a cut above the rest of the songs. It’s a glorious mix of synths, powerful drumbeats, and a chorus that is as memorable as it is fun to listen to." All My Demons Greeting Me as a Friend debuted at number one on the Norwegian VG-lista Topp 40 Album with first-week sales of 4,800 units, topping the chart for two consecutive weeks. In the United States, the album debuted at number No. 150 on the Billboard 200 with 5,000 album-equivalent units. All My Demons Greeting Me as a Friend has sold 500,000 units worldwide as of September 28, 2018.
```

## Album 191: Dynamite — Jamiroquai

- **album_id:** `22f58a46-c372-474e-9662-c8c95594639c`
- **Tags (identification only):** funk, electro disco, electronic, acid jazz, conscious, funk soul, melodic, nu disco
- **Chunks:** 3 (606 words)

### Album 191, chunk 1

```text
Dynamite is the sixth studio album by English funk and acid jazz band Jamiroquai. It was released on 15 June 2005 in Japan, 20 June 2005 in the United Kingdom, 21 July 2005 in Australia, and 20 September 2005 in the United States. It is the band's first album to feature keyboardist Matt Johnson, who joined the band in 2002. This is also Jamiroquai's only album without an official bassist, as Nick Fyffe left the band prior to the recording sessions, while Paul Turner joined the band following the album's completion and release. The album was released after the 2004 film Napoleon Dynamite featured the Jamiroquai song "Canned Heat" in its climactic dance scene. "Feels Just Like It Should" was the first single, reaching No. 8 in its first week on the UK charts. It has since become a No. 1 hit on the Billboard dance charts in the United States. The single was also certified Gold in Japan for selling 100,000 copies. The second single, "Seven Days in Sunny June", was released in the UK in August 2005, peaking at No. 14 on the UK Singles Chart. The song also features in the film The Devil Wears Prada. On 7 November 2005, "(Don't) Give Hate A Chance" was released as the third single from the album. The politically driven video for the track was Jamiroquai's first animated clip; it features a Buffalo Man, complete with buffalo-horned hat, sunglasses, and tracksuit. The clip helped the track score Top 20 showings
```

### Album 191, chunk 2

```text
in UK charts such as the Smash Hits and Hit40UK charts, both of which take in radio and video airplay as well as sales. The track reached No. 27 on the official UK Singles Chart. The album was recorded in many locations, including singer Jay Kay's personal Chillington Studios. The album peaked at No. 3 in the United Kingdom, becoming the first Jamiroquai album to chart outside the top two spots. Uncut gave the album 3 out of 5 stars, claiming "Jay Kay returns with another blast of super-slick soul". Vibe wrote that "The space cowboys return with a vengeance, sounding funky as ever." Jay Kay – lead vocals (all tracks), backing vocals (tracks 1–3, 6, 10–11), synthetic bass vocals (1), backing vocal arrangements (2, 4–8, 12) Rob Harris – guitar (tracks 1–8, 10–12) Matt Johnson – keyboards (1–6, 8, 10–12), piano (tracks 5, 8–9, 12), synthesizer bass (6), Fender Rhodes piano (7) Derrick McKenzie – drums (tracks 1, 3, 5–6, 8, 10–12), additional hi-hat percussion (2) Sola Akingbola – percussion (tracks 1, 3, 5, 10, 12) Alex Meadows – bass (tracks 2, 10) Derrick McIntyre – bass (tracks 3, 5, 8, 12) additional bass (11) Randy Hope-Taylor – bass (track 7), additional bass (8) Miaer Lloyd aka DJ Snare – scratch DJ (track 6) Nathan Haines – flute, saxophone (track 7) Benjamin Wright – string section leader (tracks 5, 7–9, 12), string arrangements (5, 7–9, 12), brass section leader (12), brass arrangements (12) Mike Spencer – music programming (tracks
```

### Album 191, chunk 3

```text
1–8, 10–12) Bridgette Blades – backing vocals (tracks 2, 5, 11–12) Alexandra Brown – backing vocals (tracks 2, 5, 11–12) Vann Johnson – backing vocals (tracks 2, 5, 11–12) Samantha Smith – backing vocals (track 4) Valerie Etienne – backing vocals (tracks 5, 7, 10) Hazel Fernandez – backing vocals (tracks 5, 7, 10) Audrey Martells – backing vocals (tracks 8) Mike Spencer – producer (all tracks), engineer (tracks 1, 3, 5, 7–10, 12), audio mixing (all tracks) Jay Kay – producer (2, 6, 8), artwork Rick Pope – recording engineer (tracks 1, 3, 5, 8, 10, 12) Reginald Dozier – recording engineer (tracks 7, 9)
```

## Album 192: Put On Your Rosy Red Glasses — The Number Twelve Looks Like You

- **album_id:** `cb718694-7146-4c2b-ad33-11058e4dff3c`
- **Tags (identification only):** mathcore, aggressive, anxious, avant garde, blast beats, chaotic, complex, concept album
- **Chunks:** 1 (260 words)

### Album 192, chunk 1

```text
Put on Your Rosy Red Glasses is the debut studio album by American mathcore group the Number Twelve Looks Like You. It has been reissued twice since its original release by Brutal Records, and once by Silent Pendulum Records as a 20th anniversary celebration. It has been regarded as the band’s heaviest release. On June 12, 2015 the album was re-released on limited edition, hand numbered cassettes. The lyrics of Put on Your Rosy Red Glasses are almost completely written in-perspective of well-known convicted murderer Albert Fish, although songs such as "If These Bullets Could Talk" and "Empty Calm" have no connection to the story of Fish. The track "Document: Grace Budd" is a spoken excerpt of a letter written by Fish, detailing his murder of Grace Budd in 1934. The track "Civeta Dei" translates in English to "City of God". The music on this release is much heavier than the band's later releases. The vocals on this album were done by using the fry scream technique among both Korman and Pedrick. There were neither edits nor enhancements on either of their voices. Following the end of the final track "Civeta Dei", the album ends with 12 minutes of silence broken up into four hidden tracks that spell out the word "Die", with a small composition at the very end. Jesse Korman - vocals Justin Pedrick - vocals Alexis Pareja - guitar Jamie Mcilroy - guitar Michael Smagula - bass guitar Christopher Conger - drums Kurt Ballou - engineering, mastering, mixing, production The Number Twelve Looks Like You - production
```

## Album 193: Second Helping — Lynyrd Skynyrd

- **album_id:** `3b1ebb85-8c93-4c58-911a-ed59657d648b`
- **Tags (identification only):** southern rock, rock, classic rock, hard rock, 70s, americana, film scores, films/games
- **Chunks:** 2 (517 words)

### Album 193, chunk 1

```text
Second Helping is the second studio album by Lynyrd Skynyrd, released on April 15, 1974. It features the band's biggest hit single, "Sweet Home Alabama", an answer song to Neil Young's "Alabama" and "Southern Man", which reached No. 8 on the Billboard Hot 100 chart in August 1974. Second Helping reached No. 12 on the Billboard album charts. The RIAA certified it Gold on September 20, 1974, and Double Platinum on July 21, 1987. After the success of their debut album, (Pronounced 'Lĕh-'nérd 'Skin-'nérd), Lynyrd Skynyrd's fan base continued to grow rapidly throughout 1973, largely due to their opening slot on the Who's Quadrophenia tour in the United States. Second Helping features Ed King, Allen Collins, and Gary Rossington all collaborating with Ronnie Van Zant on the songwriting, and cemented the band's breakthrough. Reviewing for Rolling Stone in 1974, Gordon Fletcher said Lynyrd Skynyrd performs a consistent style of Southern music-influenced blues rock similar to the Allman Brothers Band, but lacks their "sophistication and professionalism. If a song doesn't feel right to the Brothers, they work on it until it does; if it isn't right to Lynyrd Skynyrd, they are more likely to crank up their amps and blast their way through the bottleneck." Fletcher concluded Second Helping is distinct from (Pronounced 'Lĕh-'nérd 'Skin-'nérd) "only by a certain mellowing out that indicates they may eventually acquire a level of savoirfaire to realize their many capabilities". Robert Christgau in Creem was also indifferent, saying Lynyrd Skynyrd is "still a substantial, tasteful
```

### Album 193, chunk 2

```text
band, but I have a hunch they blew their best stuff on the first platter." Christgau warmed to the album later, reappraising it in Christgau's Record Guide: Rock Albums of the Seventies (1981). He observed "infectious putdowns of rock businessmen, rock journalists, and heroin", and "great formula" in general: "When it rocks, three guitarists and a keyboard player pile elementary riffs and feedback noises into dense combinations broken by preplanned solos, while at quieter moments the spare vocabulary of the best Southern folk music is evoked or just plain duplicated." In a retrospective review for AllMusic, Stephen Thomas Erlewine stated that Second Helping "replicated all the strengths" of the first album's expert Southern rock "but was a little tighter and a little more professional." Houston Press placed it No. 2 on its list of "Five Essential Boogie-Rock Albums." Ronnie Van Zant – lead vocals Gary Rossington – guitar Allen Collins – guitar Ed King – guitar, backing vocals, bass on "I Need You" and "Don't Ask Me No Questions" Leon Wilkeson – bass (all tracks except "I Need You" and "Don't Ask Me No Questions"), backing vocals Bob Burns – drums, except "I Need You" Billy Powell – keyboards Mike Porter – drums on "I Need You" Merry Clayton, Clydie King, and Sherlie Matthews – background vocals on "Sweet Home Alabama" Bobby Keys, Trevor Lawrence, and Steve Madaio – horns on "Don't Ask Me No Questions" and "Call Me the Breeze" Al Kooper – backing vocals, piano on "Don't Ask Me No Questions" and "The Ballad of Curtis Loew", acoustic guitar on "The Ballad of Curtis Loew"
```

## Album 194: The Music Scene — Blockhead

- **album_id:** `70a3b762-31d0-4156-bcbc-3393a7c7b3fb`
- **Tags (identification only):** electronic, downtempo, trip hop, hip hop, instrumental
- **Chunks:** 1 (198 words)

### Album 194, chunk 1

```text
The Music Scene is the fourth solo studio album by American hip hop producer Blockhead. It was released on Ninja Tune on November 3, 2009. It received generally favorable reviews from critics. At Metacritic, which assigns a weighted average score out of 100 to reviews from mainstream critics, the album received an average score of 75, based on 9 reviews, indicating "generally favorable reviews". Rick Anderson of AllMusic commented that "Everyone makes sample-based music these days, but very few people use found sounds and prefab musical snippets as creatively and thoughtfully as Blockhead does." Sarah Ferguson of Exclaim! said, "The music found on The Music Scene broadcasts a place for explorative musical journeying much greater than one found on pop radio." Ben Hogwood of MusicOMH wrote, "For Blockhead, this album would seem to open up a whole new realm of possibilities, showing as it does an ability to break out of the confines of hip hop, which he had already mastered." Blockhead – production DJ Signify – co-production (11), turntables (1, 12) Damien Paris – guitar (7, 9), bass guitar (3, 7, 8, 10) Wilder Zoby – vocoder (9) Baby Dayliner – mixing Matt Rota – color, design
```

## Album 195: Advaitic Songs — Om

- **album_id:** `5f41f119-4641-416c-bad8-89b9441db757`
- **Tags (identification only):** stoner rock, doom metal, psychedelic rock, raga rock, drone, experimental
- **Chunks:** 1 (188 words)

### Album 195, chunk 1

```text
Advaitic Songs is the fifth studio album by American rock band Om, released on July 24, 2012. The album has received a generally favorable response from both fans and critics, though its reception was more mixed than past works. The album has a 67 on Metacritic, indicating "generally favorable reviews". As with Pilgrimage and God Is Good, Advaitic Songs' album cover again visits Iconography from Christianity. The cover of the album features an image of John the Baptist. Advaitic Songs was released on CD and, for the first time in OM's vinyl-issuing history, a deluxe 2x vinyl audiophile version pressed at 45rpm. In 2013, a cassette version was released, as was a cassette version of the band's 2009 album God Is Good. Al Cisneros – bass, vocals, piano, percussion Emil Amos – drums, guitar, piano, percussion Kate Ramsey – vocals (1) Jory Fankuchen – viola and violin (1, 2, 3, 5) Jackie Perez Gratz – cello (1, 2, 4, 5) Lucas Chen – additional cello (1) Robert Aiki Aubrey Lowe – additional vocals and tamboura (3, 4) Lorraine Rath – flute (5) Hom Nath Upadhyaya – tabla (5)
```

## Album 196: From Mars to Sirius — Gojira

- **album_id:** `1688c0c0-8711-41b7-85d1-38e3bd91e519`
- **Tags (identification only):** death metal, progressive metal, whalecore, alternative metal, heavy metal, metal, rock, technical death metal
- **Chunks:** 4 (1031 words)

### Album 196, chunk 1

```text
From Mars to Sirius is the third studio album by French heavy metal band Gojira. It is a concept album addressing environmental issues and the rebirth of a dead planet through a space travel storyline, with the underlying theme of a transition from war to peace. From Mars to Sirius was released in 2005 to critical acclaim. It has since been ranked amongst the Rolling Stone's 100 Greatest Metal Albums of All Time. The album was largely written by Joe and Mario Duplantier, but Christian Andreu contributed certain parts such as the outro of "Where Dragons Dwell" and the central melody on "World to Come". According to Mario, the album was entirely self-produced by the band. Jean-Michel Labadie was involved in the production, especially on the coherence of his bass in the compositions, and with his work the band sought "to bring a much warmer note into their sound". Gojira had emphasized more interludes and melodies in this album. Joe Duplantier said that From Mars to Sirius represented a journey; saying, "and as in every journey, there are air gaps, variations and moments of calm". After the recording of Terra Incognita made in ten days in a studio in Brussels, the band decided to build their own studio called, Le Studio des Milans, located in their hometown, where From Mars to Sirius would be recorded. The drum recordings were made at Le Florida in Agen. Prior to the album's release date, the band performed two songs at concerts in France,
```

### Album 196, chunk 2

```text
"Backbone" and "The Heaviest Matter of the Universe". The mastering of the album was completed in mid-July 2005. A concept album, From Mars to Sirius relates the resurrection of a dead planet through an interplanetary quest, tackling environmental issues such as climate change and impacts on marine life as well as broader themes of life, death, and rebirth. Explaining the meaning behind the album title, Joe Duplantier said in an interview that "In some cultures, Mars symbolizes war and Sirius peace. I'm simplifying! It is a journey of a state of war, even if in France we are preserved, but it can be a war within us, in our flesh, in our mind, a war with ourselves". The song "Flying Whales" is "a homage" to whales and their intelligence. The concept emerged during the second album's tour and resulted in the imagery and artwork for From Mars to Sirius. The cover art was created by Joe Duplantier. Listenable Records reissued the album on vinyl in September 2012 and in November 2015 in limited quantities. A 10th anniversary box-set was released on 12 February 2016, again through Listenable Records. A video directed by Alain Duplantier was filmed for the song "To Sirius". From Mars to Sirius was received positively by critics. AllMusic's Eduardo Rivadavia noted the influences of bands such as Pantera, Meshuggah, and Neurosis on the album, particularly in the guitar work and emphasis on atmosphere. Heaping praise on the album, Rivadavia wrote that "the fluidity with which utmost heaviness
```

### Album 196, chunk 3

```text
and delicate melodies were made to coexist within the scope of single songs like 'Where Dragons Dwell', 'Flying Whales', and 'World to Come', was truly astonishing—as was the surprisingly seamless flow accomplished by the sequencing of these wildly disparate tracks, and the thematically conjoined esoteric subjects undertaken throughout. The final outcome was still not easy to digest, and admittedly just a tad bit overlong (Gojira's next challenge was definitely to be a little more concise), but compared to most of the impossibly dense (and often exhausting) prog metal available, From Mars to Sirius, struck a close to perfect balance between degree of difficulty and ultimate reward." Blabbermouth.net's Keith Bergman made similar comparisons to Meshuggah and Neurosis, but wrote that "A grocery list of influences does Gojira no justice" and that "This is a masterpiece on par with anything Meshuggah or Mastodon have released." He described their musical style as "dark, churning and hypnotic, massively heavy but varied and surprising, never monotonous"; and their lyrics as "surprisingly positive and life-affirming, their words add humanity to even the most angry, mechanized portions of the album." Bergman concluded his review by praising From Mars to Sirius as an "immense, intense, and very impressive album." Chad Bowar of About.com commented that the album combine "extreme and heavy, but also has a lot of progressive elements", while "some songs are pure death metal, others much more mellow and atmospheric". Noel Murray of The A.V. Club also viewed that it presents Gojira in two style: "between
```

### Album 196, chunk 4

```text
the bouts of sonic violence, Gojira finds time for the spare instrumental". Niki D'Andrea of Phoenix New Times stated, "Quite simply, in a genre that usually sounds crunchy and confined, Gojira sounds huge, like the conscientious monster it is". Rolling Stone named the album No. 97 on their list of the Top 100 Greatest Metal Albums of All Time, and MetalSucks named it no. 9 on their list of the 21 Best Metal Albums of the 21st Century. Loudwire ranked it as the 15th best progressive metal album of all time, and named it the second-best metal album of 2005 in a retrospective list. Metal Hammer named this album No. 15 out of The 100 Greatest Metal Albums of the 21st Century. AllMusic's Eduardo Rivadavia describes the album as marking a turning point for the band, "gaining them access into the exclusive top echelon of the world's progressive metal elite." In 2018, Decibel inducted the album into their hall of fame. Loudwire included "Flying Whales" on their list of the 66 Best Metal Songs of the 21st Century (list sorted by year). Graham Hartmann said it utilized "one of the best riffs and breakdowns of the century", adding that the song "becomes more iconic as the years pass, stretching the limits of what a metal band can achieve without clean vocals or flashy guitar solos". Rolling Stone included the song in their list of the 100 Greatest Heavy Metal Songs, ranking it at number 70. Joe Duplantier – vocals, guitars Christian Andreu – guitars Jean-Michel Labadie – bass guitar Mario Duplantier – drums Gabriel Editions – production Laurent Etchemendy – engineering, mixing Joe Duplantier – mixing, artwork Jean-Michel Labadie – mixing
```

## Album 197: Only Human — Calum Scott

- **album_id:** `355175c4-ed42-4835-9933-96338953f80e`
- **Tags (identification only):** pop, ballad, pop rock, synth pop, electronic
- **Chunks:** 2 (328 words)

### Album 197, chunk 1

```text
Only Human is the debut studio album by English singer-songwriter Calum Scott, released on 9 March 2018 through Capitol Records. The album was re-released in November 2018 as the "special edition" featuring four additional tracks. Only Human received generally positive reviews from music critics. David from auspOp gave the album four of out five, and complimented the "personal" lyrics, writing: "Most of the songs here are a great listen and you can appreciate the effort that's gone into creating such a great debut". Francesca Lamaina of Renowned for Sound gave the album three out of five stars, saying: "Only Human is a decent debut album... Some tracks lack of spirit and suffocates among incessant repetitions. However, Calum Scott's voice is incredibly wonderful." Nick Levine of Gay Times gave the album four of out five and said that "Only Human offers a classy assortment of soulful stompers, gospel-tinged ballads and more reflective downtempo moments", adding: "This is an impressive and affecting debut that proves there’s much more to Calum Scott than a kinda surprising Robyn cover." Chris Gehringer – mastering (tracks 1–14, 16–18) Phil Tan – mixing (tracks 1, 6, 8) Joe Zook – mixing (tracks 2, 4, 5, 9, 12, 13, 18) Serban Ghenea – mixing (tracks 3, 10) John McIntyre – mixing, engineering (tracks 7, 14) Ash Howes – mixing (track 15) Manny Marroquin – mixing (tracks 16, 17) Geoff Swan – mixing (track 19) Manon Grandjean – engineering (tracks 1, 3–5, 8, 9, 11, 13, 17 John Hanes
```

### Album 197, chunk 2

```text
– mix engineering (tracks 3, 10) Chris Galland – mix engineering (tracks 16, 17) Bill Zimmerman – mixing assistance (tracks 1, 4, 6, 8, 11 Dan Ewin – engineering assistance (tracks 1, 3, 5, 8, 11 Ross Newbauer – mixing assistance (tracks 2, 5, 9, 12, 13 Robin Florent – mixing assistance (tracks 16, 17) Scott Desmarais – mixing assistance (tracks 16, 17) Niko Battistini – mixing assistance (track 19) Rob Brinkman – engineering assistance (tracks 4, 9)
```

## Album 198: Live! Live! Live! — Bryan Adams

- **album_id:** `32c35823-5dab-4e54-a64d-b139566730a7`
- **Tags (identification only):** pop, pop rock, rock, hard rock
- **Chunks:** 1 (99 words)

### Album 198, chunk 1

```text
Live! Live! Live! is a live album released by Bryan Adams through A&M Records in 1988. It was recorded live at the Rock Werchter festival on 3 July 1988 in Werchter, Belgium. One track, "Into the Fire", was recorded live in Tokyo. The album sold over 1 million copies. The concert was taped while it "rained in torrents". At the end of It's Only Love, Adams comments to the audience, "I've got to tell you something. For you people to sit out in the rain, means you're one hell of an audience. I mean, to sit out in this..."
```

## Album 199: Fever Ray — Fever Ray

- **album_id:** `53755766-7e00-464b-8aeb-31f49a963c4e`
- **Tags (identification only):** synth pop, art pop, electronic, electro, electropop, ambient pop, future garage, pop
- **Chunks:** 5 (1142 words)

### Album 199, chunk 1

```text
Fever Ray is the debut solo studio album by Fever Ray, the solo musical project of Swedish singer-songwriter Karin Dreijer, known for their work as one half of the electronic duo the Knife. It was released on 12 January 2009 by Rabid Records. The album spawned four singles: "If I Had a Heart", "When I Grow Up", "Triangle Walks" and "Seven". Fever Ray was lauded by music critics. At Metacritic, which assigns a normalised rating out of 100 to reviews from mainstream critics, the album received an average score of 81, based on 27 reviews, which indicates "universal acclaim". Graeme Thomson of The Observer described the album as "an astonishingly stark record" that is "[b]uilt on the barest of electronic bones and brought to life through [Dreijer]'s almost primal vocals, the songs search for a spiritual pulse amid soulless modernity." Ian Mathers of PopMatters stated the album is "not only as good as Silent Shout but [it's also] clearly akin to the sound [they] and [their] brother Olof perfected on that record", concluding, "Nothing that Fever Ray does is as immediate or soaring as a track like 'Marble House' but Fever Ray makes up for the lack of highs by being an even more all-enveloping experience than the last few Knife records." Similarly, John Doran of the NME commented that Fever Ray "has none of the immediacy of albums such as the Knife's Silent Shout, with its playful eclecticism and heavier, dancefloor-leaning beats. Most importantly, it doesn't have a killer
```

### Album 199, chunk 2

```text
hit single in the style of 'Heartbeats'", adding that in order to "fully appreciate this beautiful and understated gem, [...] it's important to relinquish all desires for another 'Heartbeats' and enter fully into the world of Fever Ray." Doran also called the album "magnetic and rewarding" and compared it to the likes of Kate Bush, Underworld and Yellow Magic Orchestra. Pitchfork's argued that, in contrast to the Knife's "plasticky percussions and goofy synth sounds", Fever Ray "brims with fragile, more finely articulated sounds" and "moves at roughly the same pace and with the same general tone, rendering some of the songs indistinguishable at first, but committed listens will reveal this to be as nuanced and as rich of a production as anything either Dreijer has done." The A.V. Club's Chris Martins viewed it as being "countless times more claustrophobic and creepy than Silent Shout" and stated that "[t]he vocal transformer is such a huge part of what [Dreijer] does—androgynizing [their] words to accompany the cold music, mimicking the synth warbles and sustained tones that abound." The Independent critic Rupert Howe expressed, "Even beyond the gothic imagery and glacial electronics, this mesmeric solo project shares much with the Knife's last album Silent Shout", including "surreal lyrics" and "weird vocal treatments which pitch [Dreijer]'s voice down to a baleful masculine groan". Jonathan Keefe of Slant Magazine found that the album is "built upon contrasts. Most notably, [Dreijer]'s Fever Ray persona draws attention to [their] work as half of the Knife [...] Whereas
```

### Album 199, chunk 3

```text
the Knife is ostensibly a dance act, Fever Ray emphasizes tone over rhythm." In a review rated 7.5 out of 10, XLR8R wrote that it "retains real emotional heft" and compared it to the likes of Madonna, Siouxsie and the Banshees and PJ Harvey. Alexander Tudor wrote for Drowned in Sound that "minimal beats on each track prove to have been constructed with incredible attention to detail, as are the smooth synth washes, and electronic simulacra of birdcall or animal noises. The tempo may be nightmarishly unvaried, track after track, but it's composed of glitches [and] bouncing balls", citing "Keep the Streets Empty for Me" as the album's best track. In a review for AllMusic, Heather Phares opined that "Fever Ray's mix of confessional lyrics and chilly, blatantly synthetic and often harsh sounds make this album as successful an electronic singer/songwriter album as Björk's Homogenic." Phares continued, "With almost tangible textures and a striking mood of isolation and singularity, Fever Ray is a truly strange but riveting album." Alexis Petridis of The Guardian felt that the album's "dolorous chords and stately rhythms recall the Cure, circa Faith, the glacial pace makes you think of the Blue Nile", noting that, "as unlikely a step as Fever Ray may seem for one of electronic music's most enigmatic figures, the results are triumphant." BBC Music's Chris Jones called the album "bloody marvellous", while observing "a vague sense of holding pattern here rather than massive innovation. Without brother Olof as a guiding hand on
```

### Album 199, chunk 4

```text
the droning sequencers the tunes fall a bit by the wayside", but wrote that "this very tiny drawback doesn't stop Fever Ray from being the kind of brilliant album that it may not make sense to play if you're prone to nightmares." The Guardian named Fever Ray the second best album of 2009, calling it "[g]lacial, creepy and impish" and commenting, "Between the cavernous synths, the echoes and loops, the polyrhythms and snarling vocal processing, [Dreijer] managed to capture the feeling of being totally alone while also projecting a childlike wonder." It was ranked the second best album of 2009 and twenty-fourth best album of the 2000s decade by Resident Advisor. The Sunday Times named Fever Ray the third best album of 2009 by a new artist and wrote that [Dreijer] "responded to motherhood with an album of glacial sonic architecture, its unforgiving expanses conjuring up sleep-deprived mental churning", dubbing it an "electro classic". NME, Drowned in Sound and Pitchfork all placed the album at number nine on their respective lists of the Top 50 Albums of 2009, with the latter noting that "[w]hat's made [Dreijer]'s work even better is how [their] videos and performances amplify the music's sense of dread and mystery." The album was listed at number sixteen on PopMatters' The Best 60 Albums of 2009, and the website opined, "Alternately chilly and warm, wistful and foreboding, expansive and claustrophobic, Fever Ray's peculiarity and bleak magnificence holds us in its thrall." Online music service Rhapsody included Fever Ray
```

### Album 199, chunk 5

```text
at number twenty-two on its list of The 25 Best Albums of 2009. Slant Magazine named it the twenty-fourth best album of 2009, stating that [Dreijer] "challenges the conventions of dance music with [their] distorted vocals and macabre imagery" the album "emerges as an unsettling, impossible-to-shake record that suggests the aftermath of when 'pop' truly bursts". iTunes US named Fever Ray the best electronic album of 2009 as part of its Rewind 2009 roundup. It was included on AllMusic's Favorite Albums of 2009 and Favorite Electronic Albums of 2009 lists. In 2010, Fever Ray won the P3 Guld award for Dance Artist of the Year, and was nominated for Newcomer of the Year and Pop Artist of the Year. The same year, the singer won a Manifestgalan for Best Live Artist and received a Beatport Music Award nomination for Best Electronica Artist.
```

## Album 200: Piano Man — Billy Joel

- **album_id:** `abc6a82e-c884-4477-be89-14f7fe94f141`
- **Tags (identification only):** rock, pop rock, soft rock, americana, classic rock, folk rock, piano rock, pop
- **Chunks:** 2 (436 words)

### Album 200, chunk 1

```text
Piano Man is the second studio album by American recording artist Billy Joel, released on November 14, 1973, by Columbia Records. The album emerged from legal difficulties with Joel's former label, Family Productions, and ultimately became his breakthrough album. It was initially planned to be released in the UK in May 1974 by Philips but ended up being released there in April 1975 by CBS. The title track, a fictionalized retelling of Joel's experiences with people he met as a lounge singer in Los Angeles, peaked at No. 25 on the US Billboard Hot 100 and No. 4 on the Adult Contemporary singles chart. "Travelin' Prayer" and "Worse Comes to Worst" peaked at No. 77 and 80 on the Hot 100, respectively, while the album itself peaked at No. 27 on the US Billboard 200. The album was certified gold by the RIAA in 1975, but Joel received only $8,000 in royalties (US$47,866 in 2025 dollars). Columbia Records released a two-disc legacy version of Piano Man in November 2011. This edition features a somewhat abbreviated live 1972 broadcast from Philadelphia's Philadelphia 93.3 WMMR FM radio, capturing early performances by Joel recorded at Sigma Sound Studios in Philadelphia. This particular broadcast was instrumental in catalyzing Joel's musical career. Following the recording of the show, the live rendition of "Captain Jack" became a staple on the station, ultimately becoming the most requested song in WMMR's history. The burgeoning popularity of this live recording attracted the attention of Columbia Records executives, who subsequently
```

### Album 200, chunk 2

```text
offered Joel a recording contract. Additionally, the broadcast included three tracks—"Long, Long Time", "Josephine", and "Rosalinda"—which were not featured on any of Joel's studio albums. Rolling Stone mused that Piano Man "represents a new seriousness and flexibility" for Joel, comparing it to the stylings of Elton John. Reviewing the album, Billboard stated that it shows that Joel has a "fine shot at establishing himself as consistent quality AM artist with large scale songs and dynamic performing range". Billy Joel – vocals, acoustic and electric pianos, organ, harmonica Michael Omartian – accordion, arrangements (tracks 1–4, 6–10) Jimmie Haskell – arrangements (track 5) Richard Bennett, Larry Carlton, and Dean Parks – guitars Eric Weissberg – banjo, pedal steel guitar Fred Heilbrun – banjo Wilton Felder, and Emory Gordy Jr. – bass guitar Ron Tutt – drums (tracks 1–9) Rhys Clark – drums (track 10) Billy Armstrong – violin Laura Creamer, Mark Creamer, and Susan Steward – backing vocals Billy Joel – piano, harmonica, vocals Al Hertzberg – acoustic and electric guitars Larry Russell – bass guitar Rhys Clark – drums Dennis Wilen – producer Michael Stewart – producer
```
