# Embedding text relevance, batch 11 of 12 (albums 251–275 of 300)

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

This batch: **25 albums, 108 chunks**.

## Album 251: You Have No Idea What You’re Getting Yourself Into — Does It Offend You, Yeah?

- **album_id:** `dbe29a31-fa41-401c-afe1-4bf478d8322b`
- **Tags (identification only):** britannique, dance punk, 2008, british, disco punk, electro, electronic, indie rock
- **Chunks:** 1 (78 words)

### Album 251, chunk 1

```text
You Have No Idea What You're Getting Yourself Into is the debut album from Does It Offend You, Yeah?. It was released on 24 March 2008. James Rushent – lead vocals, bass, guitar, synth, vocoder Rob Bloomfield – drums, bass, guitar, synth, backing vocals Dan Coop – synth Sebastien Grainger – vocals on "Let's Make Out" Elliot James – guitar Morgan Quaintance – guitar on "Doomed Now" Producers: Does It Offend You, Yeah?, Eliot James Mix: Rich Costey
```

## Album 252: Plux Quba — Nuno Canavarro

- **album_id:** `bb61888d-3ca6-4b1e-8b8c-dbb5efb703fb`
- **Tags (identification only):** electronic, experimental, ambient, abstract, avant garde, electroacoustic, glitch
- **Chunks:** 5 (1103 words)

### Album 252, chunk 1

```text
Plux Quba: Música Para 70 Serpentes (Music for 70 Serpents), frequently shortened to Plux Quba, is the sole studio album by Portuguese musician Nuno Canavarro. Originally released on the private press label Ama Romanta in 1988, it was expanded and reissued in 1998. Plux Quba consists of pieces based around sparse, electronically processed tones and heavily treated spoken word samples. It was released to very little initial reception, and would not see distribution outside of Portugal until it was reissued in 1998 by the record label Moikai. Following the re-release, it gradually gained a following for its innovative sound, and has been considered a precursor to the development of the IDM and glitch music styles. Musicians such as Jim O'Rourke, Mouse on Mars, Prefuse 73, and Oval have cited the album as an influence on their work. Nuno Canavarro was raised in Lisbon, Portugal where he played keyboards in several local bands as a teenager. He composed the music for Plux Quba after studying composition at Institute of Sonology in the Netherlands for two years. Speaking about his time there, Canavarro noted that "There existed an incredible movement in terms of concerts, exhibitions, electro-acoustic music. I did not have the calmness, the concentration to do anything there. When I arrived, I wanted to work quickly." Upon returning to Lisbon, Canavarro recorded the album in his home studio, with the aid of a Fostex 8-track tape recorder and an Ensoniq Mirage, a then state-of-the-art 8-bit digital sampling keyboard that he filled
```

### Album 252, chunk 2

```text
with pre-recorded, highly modified samples of television programs, radio voices, ethnic music tapes, and a melodica. Canavarro remarked on how the equipment affected the recording process: "With an eight-track recorder, and that system that lets a person turn anything into an instrument, I started to create a structure from it. Record yourself on a track, and then, later, start to add other things. You can, for example, record one track, and then another six or seven around it, and then finally erase the first one, these kinds of tricks. Or you could put stuff in reverse and record at different speeds. At the time, that was it." Around this period, Canavarro previewed Plux Quba at a concert held at Instituto Franco-Português. This caught the attention of musician João Peste, who offered to release the album through his private press record label Ama Remanta. The vinyl master was cut directly from Canavarro's original tape, with no post-production work, although three songs had to be left off due to lack of cutting space. 500 copies of Plux Quba were pressed onto vinyl, though Canavarro was unsure how many actually sold, and that costs of production or the signature of a contract "did not exist". Canavarro contributed liner notes to the album, instructing listeners to play the record through speakers which are separated from each as far as possible at a low volume, starting from the track "Wask" onwards. The album's "enigmatic" title was chosen to "make it even weirder". Despite Plux Quba
```

### Album 252, chunk 3

```text
being received positively by the local Lisbon music scene, its small circulation meant that it quickly fell into obscurity. Canavarro would go on to record one further album, a collaboration with Carlos Maria Trindade entitled Mr. Wollogallu, in 1991, before pursuing a career composing film soundtracks. In 1991, Plux Quba was introduced by Christoph Heemann to several musicians, including Jim O'Rourke and Jan St. Werner of Mouse on Mars, during an informal listening party in Cologne, Germany. O'Rourke in particular grew to become a fan of the album, and a few years later met up with Rafael Toral, a musician and mutual friend of Canavarro, to track down the album's master tapes. O'Rourke eventually contacted Canavarro, and learned that he made the album whilst largely unaware of the developments happening elsewhere in electronic music, such as the ambient work of Brian Eno. With Canavarro's permission, Plux Quba was digitally remastered by Toral and released through O'Rourke's Moikai label in 1998, reinstating the three tracks that were left off the original pressing. The album would later be reissued again in 2015 through Drag City. The reissue of Plux Quba helped to bring the album a much wider audience outside of Portugal, and was met with an enthusiastic response from critics. In 2018, Andy Beta of Pitchfork placed Plux Quba at 181 on the site's Top 200 Best Albums of The 1980s article, stating that: Thirty years on, Portuguese composer Nuno Canavarro's lone solo work remains as enigmatic and inscrutable as the
```

### Album 252, chunk 4

```text
day it was first released. Plux Quba was discovered by wily experimenters like Jim O'Rourke, Mouse on Mars, and Oval in the '90s; from there, it became an influence on early ’00s clicks-and-cuts aesthetes, adventurous producers like Jan Jelinek and Fennesz, and present-day shapeshifters like Oneohtrix Point Never and Yves Tumor. As such a heady list of admirers suggests, Canavarro's music eludes easy classification. Made up of chiming electronics, processed cries and whispers, electroacoustic études, smeared noise, and scrambled lullabies, Plux Quba skips and glitches between one sound world and the next. At first, it can feel jarring and cracked, yet such shards slowly assemble into an exquisite whole. Plux Quba plays like some long-lost memory, conjuring evocative emotions before fragmenting and falling back out of reach again. In 2001, fellow Pitchfork columnist Mark Richardson referenced the album in his article "Fuck Words of Wisdom", citing it as an example of how speech is deconstructed in music, saying that "Plux Quba is filled with haunting manipulated vocals, where words are stripped of specific meaning but not emotional content." Richardson compared the album to Robert Ashley's Automatic Writing which he cited as a possible influence. Musician Sam Prekop of the Sea and Cake praised the album, declaring to be "the high-water mark, in my opinion, of electronic music. It's a really delicate, beautiful, and really weird record." In 2001, producer Prefuse 73 recorded the track "Nuno", which predominantly samples "Wask", for his album Vocal Studies + Uprock Narratives. Reflecting on Plux
```

### Album 252, chunk 5

```text
Quba years after its release, Canavarro described it as a "totally isolated" work and that he could "hardly believe" how he managed to make it, though remarked that "on the other hand, the very limitation of my technical means, in this case, I think worked in my favor, because it led to my creativity. I got to use its own defects, at the level of the software of the sampler. It was a very unstable apparatus, there were some beastly things that, when forcing it to work hard, responded somewhat unpredictably. It was beastly for the kind of music I wanted to do."
```

## Album 253: The Lost Boy — YBN Cordae

- **album_id:** `692936c2-96c0-4b91-8f75-79bb206adec9`
- **Tags (identification only):** hip hop, conscious hip hop, dmv rap, jazz rap, neo soul, pop rap, rap, southern hip hop
- **Chunks:** 2 (540 words)

### Album 253, chunk 1

```text
The Lost Boy is the debut studio album by American rapper Cordae (then known as YBN Cordae). The album was released on July 26, 2019, by Atlantic Records and Art@War, and contains features from Chance the Rapper, Anderson .Paak, Ty Dolla Sign, Pusha T, Arin Ray, and Meek Mill. The album has received widespread acclaim from music critics. The album was later nominated for Best Rap Album at the 2020 Grammy Awards, while the album track "Bad Idea" was nominated a Grammy Award for Best Rap Song. The Lost Boy was supported by three singles, "Have Mercy", "Bad Idea", and "RNP". The album's lead single, "Have Mercy", was released on March 8, 2019. Two music videos for "Have Mercy" were released on April 16, 2019, with the first one being directed by Cole Bennett and the other being directed by Aplus. The single was produced by Flippa, Kid Culture, and Nils. The album's second single, "Bad Idea", was released on June 17, 2019, along with an accompanied music video and features vocals from American rapper Chance the Rapper. The single was produced by Bongo ByTheWay with co-production by Kid Culture. The album's third single, "RNP", was released on July 23, 2019, and features vocals from American singer Anderson .Paak. The single was produced by J. Cole. The music video was released on October 14. The music video for "Broke as Fuck", was released on August 15, 2019. The Lost Boy received widespread acclaim from critics. At Metacritic, which assigns a
```

### Album 253, chunk 2

```text
normalized rating out of 100 to reviews from mainstream publications, the album received an average score of 81, based on five reviews. Fred Thomas of AllMusic said, "The rapper's skills aren't in question on The Lost Boy, but the album sometimes overshoots in its ambition, aiming for too many styles to hit them all with excellence. It's still a strong collection, and when Cordae strikes a perfect balance of mellow production and lyrical power on standout tracks like "We Gon Make It," it points to even more fully formed work ahead from a strong talent just getting started." Nicolas Tyrell of Clash stated "Both bold and filled with bravado, yet layered and emotional, YBN Cordae is able to convey his desires, hopes, and fears in an ambitious and well-thought out format. A strong debut from an artist who knows that he is capable of long-term success." Jacob Carey of Exclaim! said, "If The Lost Boy was the new wave rapper's most substantial test of talent and longevity, YBN Cordae passed with flying colours." Scott Glaysher of HipHopDX stated "Encapsulates everything a Gen Z rapper should be aiming for; young gun energy mixed with traditional skill." Will Schube of Pitchfork said, "Despite the glossy guestlist, The Lost Boy remains Cordae’s show. At 15 songs, it could have used an edit, another voice in the room telling him to tone it down. But still, it’s an assured debut." Tom Hull ranked it 52nd on his list of the best non-jazz albums from 2019. The Lost Boy debuted at number 13 on the Billboard 200, with 25,000 copies moved in its first week for the chart dated August 10, 2019. The album also debuted on the Top R&B/Hip-Hop Albums chart at number eight.
```

## Album 254: The Rising Tide of Oblivion — Neaera

- **album_id:** `d6ddf0e2-aa23-4c14-8a50-9b837fd071a8`
- **Tags (identification only):** death metal, heavy metal, melodic death metal, hardcore, melodic metalcore, rock
- **Chunks:** 1 (94 words)

### Album 254, chunk 1

```text
The Rising Tide of Oblivion is the first full-length album released by Neaera. It was released on 21 March 2005 by Metal Blade Records. Benjamin Hilleke – vocals Stefan Keller – guitar Tobias Buck – guitar Benjamin Donath – bass guitar Sebastian Heldt – drums Claus Ulka (ex-Misery Speaks) – vocals on "Save the Drowning Child" Magdalena Gerritsen – violin on "From Grief..." and "The Last Silence" Sören Krefis – cello on "From Grief..." and "The Last Silence" Andy Classen – production, mastering Reiner Wyen – production of "From Grief..." and "The Last Silence"
```

## Album 255: Friction, Baby — Better Than Ezra

- **album_id:** `cd605b6e-9cb2-4fd4-ad44-fba1b3bfd248`
- **Tags (identification only):** alternative rock, rock, electronic, jangle pop, post grunge, pregaptrack
- **Chunks:** 1 (193 words)

### Album 255, chunk 1

```text
Friction, Baby is the third studio album by Better Than Ezra, released in 1996. The album's title comes from a television interview with Keith Richards of the Rolling Stones. When asked how he and Mick Jagger stayed together for so long, Richards took a long drag from his cigarette and said "friction, baby." This may also be a reference to the fact that the band had replaced its original drummer, Cary Bonnecaze, between the recording of their previous album and this one. The album produced two hits on the Billboard modern rock charts: "King of New Orleans" and "Desperately Wanting." "Desperately Wanting" also narrowly missed the Billboard Top 40, peaking at #48. The third and fourth singles, "Long Lost" and "Normal Town," failed to chart. In its review, The A.V. Club called Friction, Baby "a batch of low-impact pop cheese that's too mindlessly catchy not to be likable." Kevin Griffin – Guitar, Vocals Tom Drummond – Bass Travis McNabb – Drums Joan Wasser – Violin Peter Holsapple – Piano, Organ, Mandolin Anthony Dagrade – Saxophone, Clarinet, Flute Jamil Sharie – Trumpet Mark Mullins – Trombone Matthew Perrine – Tuba Lawrence Sieberth – Piano
```

## Album 256: Colors II — Between the Buried and Me

- **album_id:** `8a0847f2-6d95-4fb2-bf3b-9eb71d33a181`
- **Tags (identification only):** metalcore, progressive metalcore, 1–4 wochen, heavy metal, metal, offizielle charts, progressive metal, rock
- **Chunks:** 3 (795 words)

### Album 256, chunk 1

```text
Colors II is the tenth studio album by the American progressive metal band Between the Buried and Me. It was released on August 20, 2021 through Sumerian Records, their second and final release with the label, after the two-part album Automata I and II. It serves as a direct follow-up to their 2007 album Colors. It is also the band's last album to feature rhythm guitarist Dustie Waring after his dismissal from the band in 2023. In regards of the conception of the album, vocalist Tommy Giles Rogers Jr. explained: Especially with 2020, we really wanted to give it all we could and show the world we’re still here. That’s part of the reason we named it Colors II. We were in a similar spot when we did the first Colors. Back then, we had just gotten done with Ozzfest. We were wondering, 'Where do we belong in this music scene?' We still struggle with that. At both of these moments in our career, we decided to just be ourselves and write the best album we can. We came out guns blazing, and I feel like it’s some of our most creative material in a long time. Guitarist Paul Waggoner added: Colors was very much our attempt at a do-or-die statement. We had to establish our identity and be who we really wanted to be in order to have a career. This time around, our industry was shut down for a year. Once tours were canceled due to the pandemic,
```

### Album 256, chunk 2

```text
we were like, 'We've got to write a record, and it's got to be good'. We had to do something next level. About the concept, Rogers commented: Musically, it flows like a sequel to Colors, but it wasn’t just another version of that album. On the original, I was analyzing myself and analyzing humanity. With last year, I was in a perfect position to do that. I wrote lyrics in the same way, but they felt new. It was more of a real-world concept by virtue of making a continuation. Music’s purpose is to help. That's a big theme of this album. Once our songs are done, they belong to our listeners. Maybe this will help them move forward creatively or in life. And about the track "Fix the Error", he shared: The intention was to write a metal song with a big gospel vibe. It turned into this monster. It's a small story on the record about this guy who lives in a big apocalyptic city. He retires from his job, but he wants to take down this huge corporation. The song is a celebration of taking down corruption and saying, 'Fuck you', to the man. It's about as punk as we’ll ever get. The first single "Fix the Error" was released on June 25, 2021. An animated music video was released for the song on July 7, 2021, animated by Tony Celano. The second single "Revolution in Limbo" was released on July 23, 2021. A music video for
```

### Album 256, chunk 3

```text
"The Future Is Behind Us" was released on August 20, 2021, the same date as the album release. The album received generally positive reviews from music critics upon its release. On review aggregator Metacritic, the album holds a score of 68 out of 100 based on four reviews. Kerrang! gave the album 4 out of 5 with writer James Hickie stating: "Unsurprisingly, at 80 minutes long, and with exhaustive closing track 'Human Is Hell (Another One with Love)' taking up 15 of those, it's entirely too much music to wrestle with on cursory listens, and requires serious dedication, though that's no bad thing in an age when streaming has fundamentally altered the attention span. As a result, the uninitiated are likely to be overwhelmed by such a glut of material, particularly when it takes so many stylistic detours and about-turns. It's worth the endeavour, though, because there's some sublime music here, deep and diverse, which has plenty to offer nerds and newbies alike." Metal Hammer gave the album a positive review, stating: "In being so loyal to the structure of what's come before, Colors II doesn't reinvent progressive metal like its predecessor, but by all other metrics, it lives up to its lineage. It's the only album to ever recapture Colors' brand of restlessness, reaffirming that BTBAM are once-in-a-lifetime masterminds." Tommy Giles Rogers Jr. – vocals, keyboards Paul Waggoner – lead guitar Dustie Waring – rhythm guitar Dan Briggs – bass, keyboards Blake Richardson – drums, harsh vocals on "Revolution in Limbo" Mike Portnoy – first drum solo on "Fix the Error" Navene Koperweis – second drum solo on "Fix the Error" Ken Schalk – third drum solo on "Fix the Error" Jamie King – production, engineering Jens Bogren – mixing Richardo Borges – mixing
```

## Album 257: Fountain Baby — Amaarae

- **album_id:** `1307e31f-086f-4ea2-891c-d500b8f5eb76`
- **Tags (identification only):** alternative r and b, alté, afrobeat, afrobeats, contemporary r and b, dance music, dance pop, electronic
- **Chunks:** 2 (513 words)

### Album 257, chunk 1

```text
Fountain Baby is the second studio album by the Ghanaian-American singer Amaarae. It was released on June 9, 2023, via Golden Child Entertainment and Interscope Records. The album, released to widespread critical acclaim, was supported by four singles, "Reckless & Sweet", "Co-Star", "Wasted Eyes", and "Angels in Tibet". The album went on to earn spots on multiple year-end best-of lists. In 2024, Amaarae expanded the project with Roses Are Red, Tears Are Blue – A Fountain Baby extended play, which was released on June 28, 2024 and introduced seven new tracks. Around the same time, she also featured alongside Jorja Smith on Childish Gambino's single "In the Night". On her 2020 debut album The Angel You Don't Know, Amaarae embraced themes of desire and self-assuredness, presenting her "zaddy" persona with a genre-blurring mix of R&B, pop, and alté that highlighted her creative fearlessness. Following her global breakthrough with "Sad Girlz Luv Money" featuring Moliy—and its remix with Kali Uchis—Amaarae continued to develop her sound by blending diverse global influences into her signature Afrobeats-inspired style. Pitchfork described the lead single "Reckless & Sweet" as a subtler, more introspective take on Amaarae's signature style, blending soft drums and guitar with lyrics that explore emotional vulnerability and material tension. The review highlighted the track's biblical imagery and understated production as a contrast to her usual confidence. Following the lead single "Reckless & Sweet", Amaarae released the second single "Co-Star", accompanied by a star sign–themed music video directed by Lauren Dunn. Amaarae released a
```

### Album 257, chunk 2

```text
music video for the third single, "Wasted Eyes". Directed by Lauren Dunn, the video is set in a nightclub featuring a wall-to-wall fish tank. She later followed it with a vibrant visual for the fourth single "Angels in Tibet", directed by Yavez Anthonio, which features performances on stage and in ornate settings alongside dancers Hamly and Beaulexx. Fountain Baby was released to overwhelmingly positive reception. Metacritic, a review aggregator, awarded a score of 95/100 based on eight critic reviews, indicating "universal acclaim". Pitchfork named the record "Best New Music" with Julianne Escobedo Shepherd writing, "The Ghanaian American singer's dazzling second album is a confident and unconventional record that flows, saunters, and boasts its way to one of the best pop albums of the year." Tarisai Ngangura for NPR enjoyed the variety between songs and was impressed by the cohesive fusion of various genres. Robert Christgau, reviewing in his "Consumer Guide" column, appreciated Amaarae's grounded gratitude for the same-sex obsession "she can afford" to have as a successful artist: Her portion of fame proud and earned, her voice simultaneously fragile and self-possessed, her star-time comforts and advantages acknowledged without vanity or apology, she doesn't so much boast about her crushes, trysts, and conquests as lay them out lubriciously or matter-of-factly as the cherished rewards of a lifestyle I wouldn't be surprised to learn she's exaggerating ... she appreciates what she's got without taking it for granted, and without assuming there are no more chapters to her story. In September, Rolling Stone listed the album as one of the best albums of 2023 so far.
```

## Album 258: Bryter Layter — Nick Drake

- **album_id:** `f0aec274-a79f-45c8-a1b1-af56d373bf87`
- **Tags (identification only):** folk, baroque pop, chamber folk, contemporary folk, singer songwriter, british, british folk rock, english
- **Chunks:** 4 (802 words)

### Album 258, chunk 1

```text
Bryter Layter is the second studio album by the English folk singer-songwriter Nick Drake. Released on March 5, 1971 by Island Records, it was his last album to feature other musicians, as his next and final studio album, Pink Moon, had him perform unaccompanied. Like Five Leaves Left, the album contains no unaccompanied songs; Nick Drake was accompanied by musicians including members of Fairport Convention and John Cale of the Velvet Underground, as well as Beach Boys session musicians Mike Kowalski and Ed Carter. According to arranger Robert Kirby, Drake had intended for the arrangements to evoke the Beach Boys' Pet Sounds. Initially scheduled for release in November 1970, with UK promotional copies being sent out at the time, dissatisfaction with the artwork meant that the album was held over until the following March. Contemporary reviews were mostly positive. In Sounds, Jerry Gilbert called the album "superb" and said, "On their own merits, the songs of Nick Drake are not particularly strong, but Nick has always been a consistent if introverted performer, and placed in the cauldron that [producer] Joe Boyd has prepared for him, then things start to effervesce." Gilbert praised the "splendid arrangements" of Robert Kirby and said that the songs "take time to work through to the listener, with help from the beautiful backing which every track receives". Lon Goddard of Record Mirror was also impressed by Drake's guitar technique and Kirby's arrangements, and stated that "Nick isn't the world's top singer, but he's written fantastic numbers
```

### Album 258, chunk 2

```text
that suit strings marvellously. Definitely one of the prettiest (and that counts!) and most impressive albums I've heard ... Happy, sad, very moving." "The Disc Panel" in Disc and Music Echo stated that Drake "sings his own very personal songs in a strange, deep vaseline voice, probably more suited to crooning, accompanied at times by really funky backing" and called the record "an extraordinarily good hefty folk album". However, Andrew Means of Melody Maker described the album as "late-night coffee'n'chat music" where "the 10 tracks are all very similar – quiet, gentle and relaxing." Retrospectively, Mojo called the album "certainly the most polished of his catalogue". Alternative Press called it "[one] of the most beautiful and melancholy albums ever recorded". In his 2016 book Never a Dull Moment: 1971 – The Year That Rock Exploded, David Hepworth described "At the Chime of a City Clock" as "the perfect soundtrack for the dispensing of a cup of tea in a polystyrene cup, marrying sound and image in a way that made me unsure whether I was watching a commercial or actually in a commercial". In 2000, Q placed Bryter Layter at number 23 in its list of the 100 Greatest British Albums Ever. It ranked at number 14 in NME's list of the Greatest Albums of the '70s. It was voted number 306 in the third edition of Colin Larkin's All Time Top 1000 Albums (2000). In 2003, the album was ranked number 245 on Rolling Stone magazine's list of the
```

### Album 258, chunk 3

```text
500 Greatest Albums of All Time. The guitar Drake holds on the album cover is owned by Nick Laird-Clowes of the Dream Academy, whose "Life in a Northern Town" was written as an elegy to Drake. The cover of the North American version of the 2003 album Akuma no Uta by Japanese metal band Boris pays tribute to Bryter Layter. The song "Fly" was featured in Wes Anderson's 2001 film The Royal Tenenbaums and appeared on its soundtrack. The song "One of These Things First" was featured in the 2004 film Garden State and on the Grammy Award-winning soundtrack, compiled by Zach Braff. The song was also used in the 2008 film Seven Pounds. The song "Northern Sky" was featured in the 2001 film Serendipity, was frequently featured in the NBC series This Is Us, and was chosen as a track by Sue Perkins whilst on BBC Radio 4 programme Desert Island Discs. Bryter Layter features prominently in the 2020 novel Summer by the Scottish author Ali Smith, when the character Grace hears the album ("pretty flute, very 1970s") being played on a cassette machine in a church, leading to a conversation about Drake. Nick Drake – vocals (2–5, 7–9); acoustic guitar; electric guitar (8) Dave Pegg – bass (1–3, 5–10) Dave Mattacks – drums (1, 2, 5, 6, 10) Robert Kirby – string arrangement (1, 3, 5, 10); brass arrangement (2) Richard Thompson – electric guitar (2) Ray Warleigh – alto saxophone (3, 8); flute (10) Paul Harris –
```

### Album 258, chunk 4

```text
piano (4) Ed Carter – bass (4) Mike Kowalski – drums (3, 4, 8, 9) Lyn Dobson – flute (5, 6) John Cale – viola, harpsichord (7); celeste, piano, organ (9) Chris McGregor – piano (8) Pat Arnold – backing vocals (8) Doris Troy – backing vocals (8) Joe Boyd – producer
```

## Album 259: Lovehatetragedy — Papa Roach

- **album_id:** `6200e3c5-f389-4b1f-a92d-062672c62ef6`
- **Tags (identification only):** alternative metal, nu metal, hard rock, heavy metal, rock
- **Chunks:** 2 (368 words)

### Album 259, chunk 1

```text
Lovehatetragedy is the third overall and second major label studio album by the American rock band Papa Roach. It was released on June 18, 2002. A re-recorded version of the song "M-80 (Explosive Energy Movement)" was featured in the game Amplitude. The song "She Loves Me Not" was featured in the game NHL 2003. The songs "She Loves Me Not" and "Walking Thru Barbed Wire" were recorded in 1999, with the former appearing on the band's 1999 demo and the latter on the ...Let 'Em Know! EP. In comparison to their prior album, Infest, the band aimed to incorporate less rapping, and more singing in Lovehatetragedy. Lovehatetragedy is Papa Roach's last album under DreamWorks Records, before signing to Geffen in 2003. Alongside with Infest, a debut vinyl edition of the album was released on September 8, 2017. According to the review aggregator Metacritic, Lovehatetragedy received "generally favorable reviews" based on a weighted average score of 75 out of 100 from 12 critic scores. The album debuted at number two on the Billboard 200 by selling approximatively 136,000 copies in its first week, behind Eminem's The Eminem Show. Lovehatetragedy was mostly well received by music critics, gaining an average score of 75 on Metacritic. Papa Roach toured on the second edition of the Anger Management Tour during the summer of 2002. They co-headlined with Eminem, who was also supported by Ludacris, Xzibit, X-Ecutioners, Bionic Jive during the tour. It was the last edition of Anger Management that had rock music being
```

### Album 259, chunk 2

```text
prominently featured, with Papa Roach's set occurring between Eminem and Ludacris's while Bionic Jive opened the concerts during the first half of the tour. It achieved a gold certification in the U.S for exceeding 500,000 copies sold in the first two months. Despite peaking at higher positions on most international charts, "Lovehatetragedy" failed to catch the success of Infest both in lifetime sales and chartrun (15 weeks within the Billboard 200). It was also certified Gold in Canada, Switzerland and in the UK Jacoby Shaddix – lead vocals Jerry Horton – guitar, backing vocals Tobin Esperance – bass, backing vocals Dave Buckner – drums Brendan O'Brien – producer, mixing Adam Ayan – digital editing Ron Handler – A&R
```

## Album 260: In the Heat of the Night — Imagination

- **album_id:** `2891bc68-92a9-484b-986f-11a4d634c8c0`
- **Tags (identification only):** disco, boogie, contemporary r and b, electronic, funk, pop soul, r and b, soul
- **Chunks:** 1 (161 words)

### Album 260, chunk 1

```text
In the Heat of the Night is the second album by British soul/dance group Imagination, produced by Steve Jolley and Tony Swain and released in 1982. In the Heat of the Night was Imagination's most successful album, reaching No. 7 in the United Kingdom. "Just an Illusion" was the group's highest charting single, peaking at No. 2 (kept off the top spot by the Goombay Dance Band's "Seven Tears"), and also making the top 10 in several other countries in Western Europe and Scandinavia. It was covered by Destiny's Child on its self-titled album and Mariah Carey sampled this song as part of her hit "Get Your Number" on her 2005 album The Emancipation of Mimi. "Music and Lights" was another UK top 5 hit, and "In the Heat of the Night" and "Changes" also charted. Tony Swain – Roland SH-1000 synthesizer (track 5, 8) Tony Swain – engineer, producer, arrangement Steve Jolley – engineer, producer, arrangement Howard Saunders – typography
```

## Album 261: Jacksonville City Nights — Ryan Adams & the Cardinals

- **album_id:** `4484f110-6a8a-46ae-89a5-bebc1d3e687e`
- **Tags (identification only):** country, alternative country, alternative rock, americana, blues, country blues, country rock, rock
- **Chunks:** 3 (635 words)

### Album 261, chunk 1

```text
Jacksonville City Nights is the seventh studio album by American alternative country singer-songwriter Ryan Adams, released on September 26, 2005, and released in the US on September 27, 2005 on Lost Highway. The album is Adams' second with The Cardinals, and the second in a trilogy of albums released in a seven-month timespan during 2005. By 2007, the album had sold 100,000 copies in the United States and 158,000 worldwide. The album was recorded live in the studio, without overdubs. The title is a reference to Adams' hometown of Jacksonville, North Carolina, which has been referenced throughout his career. Several limited American releases contained a DVD titled September (originally intended to be the title of the album), which featured a 20-minute documentary about the band on the road and in the studio. Bassist Catherine Popper is featured in the photograph on the album cover. In August 2005, two fans of Adams prematurely uploaded four tracks from Jacksonville City Nights to a fansite of Adams. In March 2006, Robert Thomas of Milwaukee and Jared Bowser of Jacksonville, Florida, two moderators of the fansite, were indicted by US federal court after the two had pled guilty to federal copyright violations. They had violated the Family Entertainment and Copyright Act (FECA), which establishes a federal crime for pirating music and movies before their official release to the public. If they had been convicted on all counts, they could have faced up to 11 years in prison. The case ended after Thomas and Bowser
```

### Album 261, chunk 2

```text
accepted a plea deal; they were able to bring down the felony counts to misdemeanors. Instead of the 11 years, they received two months of house arrest and two years of probation. Thomas was able to be removed from house arrest and probation early because of good behavior. Due to there being no proof of monetary loss to the record label, Thomas and Bowser did not have to pay the record label. While the case was ongoing, Thomas shut the fansite down but relaunched it after the case ended, missing the community. The album so far has a score of 72 out of 100 from Metacritic based on "generally favorable reviews". Spin gave it a B+ and said the album "reminds you why Adams was once a big deal." NME gave it a score of seven out of ten and said, "Adams could clearly make use of an editor here--but you can't possibly hate an album that uses pedal-steel on every track." Tiny Mix Tapes gave it a score of three-and-a-half stars out of five and said, "As with most Adams records, the fact that some of the songs made the cut is perplexing." However, Blender gave it three stars out of five and said, "It's the sound of a New Yorker coming home for a breath of country air." Prefix Magazine gave it an average review and said, "Perhaps Adams is just earning cheap sympathy with his strained, tour-weary voice, or maybe it's just too thrilling to hear him
```

### Album 261, chunk 3

```text
revisit Gram, but Jacksonville City Lights [sic] does seem to come by its sound honestly." Ryan Adams - vocals, acoustic guitar, piano J.P. Bowersock - electric guitars Catherine Popper - bass, piano, background vocals Brad Pemberton - drums, percussion Jon Graboff - pedal steel, background vocals Claudia Chopek: Violin. David Gold: Violin & Viola. Bob Hoffnar: Pedal steel. Byron Isaacs: Background vocals. Norah Jones: Piano & vocals. Julia Kent: Cello. Joe McGinty: Piano. Michael Panes: Violin. Johnny T: Drums. Glenn Patscha: Piano & background vocals. The Nashville String Machine perform on the song "My Heart Is Broken" and are: Bergen White: Arranger and conductor. Violins: Carl Gorodetsky, Pamela Sixfin, Conni Ellisor, Allan Umstead, David Angell, Cathy Umstead & Mary Kathryn Vanosdale. Violas: Kris Wilkinson, Gary Vanosdale & Jim Grosjean. Cellos: Carole Rabinowitz & Bob Mason.
```

## Album 262: Lateralus — Tool

- **album_id:** `0f038ae6-5e6e-4817-b8eb-70bad7789bf8`
- **Tags (identification only):** alternative metal, progressive metal, progressive rock, rock, heavy metal, alternative rock, art rock, dense
- **Chunks:** 8 (1959 words)

### Album 262, chunk 1

```text
Lateralus () is the third studio album by the American rock band Tool. It was released on May 15, 2001, through Volcano Entertainment. The album was recorded at Cello Studios in Hollywood and The Hook, Big Empty Space, and The Lodge, in North Hollywood, between October 2000 and January 2001. David Bottrill, who had produced the band's previous release Ænima, produced the album along with the band, and it became the last Tool album produced by Bottrill to date. On August 23, 2005, Lateralus was released as a limited edition two-picture-disc vinyl LP in a holographic gatefold package. The album debuted at No. 1 on the Billboard 200 chart, selling more than 555,200 copies in its first week of release. It was certified triple platinum by the RIAA on April 15, 2021. On February 13, 2015, the album was certified Gold by the BPI. It was also certified double platinum in both Australia and Canada. The band won the Grammy Award for Best Metal Performance for the song "Schism" in 2002. Lateralus was ranked No. 123 on the Rock and Roll Hall of Fame's "Definitive 200" list. Lateralus emerged after a four-year legal dispute with Tool's label, Volcano Entertainment. During those years, the band avoided writing new material. In January 2001, the band announced that their new album's title would be Systema Encéphale and provided a 12-song track list with titles such as "Riverchrist", "Numbereft", "Encephatalis", "Musick", and "Coeliacus". File sharing networks such as Napster were flooded with bogus files
```

### Album 262, chunk 2

```text
bearing the titles' names. At the time, Tool's members were outspokenly critical of file-sharing networks in general due to the negative effect on artists that are dependent on success in record sales to continue their career. During an interview with NY Rock in 2000, lead singer Maynard James Keenan stated: I think there are a lot of other industries out there that might deserve being destroyed. The ones who get hurt by MP3s are not so much companies or the business, but the artists, people who are trying to write songs. A month later, the band revealed that the new album was actually titled Lateralus (supposedly a portmanteau of the leg muscle Vastus lateralis and the term lateral thinking) and that the name Systema Encéphale and the track list had been a ruse. Lateralus and the corresponding tours would take Tool a step further toward art rock, and progressive rock territory, in contrast to the band's earlier material, which has often been labeled as alternative metal. The album has also been described as progressive metal. Rolling Stone wrote in an attempt to summarize the album that "Drums, bass and guitars move in jarring cycles of hyperhowl and near-silent death march ... The prolonged running times of most of Lateralus thirteen tracks are misleading; the entire album rolls and stomps with suitelike purpose." Joshua Klein of The A.V. Club in turn expressed his opinion that Lateralus, with its 79-minute running time and relatively complex and long songs—topped by the ten-and-a-half minute
```

### Album 262, chunk 3

```text
music video for "Parabola"—posed a challenge to fans and music programming alike. Drummer Danny Carey said, "The manufacturer would only guarantee us up to 79 minutes ... We thought we'd give them two seconds of breathing room." Carey aspired to create longer songs like those by artists he grew up listening to. The band had segues to place between songs, but had to cut out a lot during the mastering phase. The CD itself was mastered using HDCD technology. Just as Salival was initially released with several errors on the track listing, early pressings of Lateralus had the ninth track incorrectly spelled as "Lateralis". The original title of "Reflection" was "Resolution" before being changed three months prior to the album's release. The track listing is altered on the vinyl edition, with "Disposition" appearing at track 8. Because of the long running time, the double vinyl edition could not be released like the disc since the songs would not fit on each disc side in that order. By moving "Disposition" to an earlier point, the sides were balanced and could fit the material. This edit breaks the segue that occurs between "Disposition" and "Reflection", however, which, along with "Triad", are linked together on the tracklist. Two of the singles from the album, "Parabola" and "Schism", are featured in the video game Guitar Hero World Tour. The insert is translucent and flips open to reveal the different layers of the human body. Disguised in the brain matter on the final layer is
```

### Album 262, chunk 4

```text
the word "God". The artwork was done by artist Alex Grey, who would later design the 3D edition cover for the followup to Lateralus, 10,000 Days and a major part of the artwork for Tool's fifth studio album Fear Inoculum. Drummer Danny Carey sampled himself breathing through a tube to simulate the chanting of Buddhist monks for "Parabol", and banged piano strings for samples on "Reflection". "Faaip de Oiad" samples a recording of a 1997 call on Art Bell's radio program Coast to Coast AM. "Faaip de Oiad" is Enochian for The Voice of God. "Disposition", "Reflection", and "Triad" form a sequence that has been performed in succession live with occasional help from various tourmates such as Mike Patton, Dave Lombardo, Buzz Osborne, Tricky, and members of Isis, Meshuggah, and King Crimson. The title track, "Lateralus", incorporates the Fibonacci sequence. The theme of the song describes the desire of humans to explore and to expand for more knowledge and a deeper understanding of everything. The lyrics "spiral out" refer to this desire and also to the Fibonacci spiral, which is formed by creating and arranging squares for each number in the sequence's 1,1,2,3,5,8,... pattern, and drawing a curve that connects to two corners of each square. This would, allowed to continue onwards, theoretically create a never-ending and infinitely expanding spiral. Related to this, the song's main theme features successive time signatures 9/8, 8/8, and 7/8. The number 987 is the sixteenth integer of the Fibonacci sequence. "Eon Blue Apocalypse" is
```

### Album 262, chunk 5

```text
an instrumental piece in-between "The Grudge" and "The Patient". The track "Mantra" is the slowed-down sound of Maynard James Keenan gently squeezing one of his cats. In an interview with producer David Bottrill, he revealed that the lyrics for "Schism" were changed last minute because of Adam Jones thinking they were too close to home. The first version of the lyrics were, according to Bottrill, very explicitly about the building tensions between Maynard and Adam, and the band as a whole. Maynard changed them after a lengthy band meeting, to be more broadly applicable to relationships falling apart. Overall, Lateralus was met with generally favorable reviews by mainstream music critics upon its initial release. At Metacritic, which assigns a normalized rating out of 100 to reviews from critics, the album received an average score of 75, which indicates "generally favorable reviews", based on 15 reviews. Many of their responses mentioned the album's ambition and ability to confound listeners, such as Spin's Ryan Rayhil's summarization of it as a "monolithic puzzlebox". Rob Theakston reviewed the record for AllMusic, where he claimed that "Lateralus demands close listening from the first piece onward, as it becomes quickly apparent that this is not going to be an album one can listen to and accept at face value. Complex rhythm changes, haunting vocals, and an onslaught of changes in dynamics make this an album other so-called metal groups could learn from." Terry Bezer praised Lateralus in a review for Drowned in Sound by comparing it
```

### Album 262, chunk 6

```text
to the band's previous album, Ænima, calling it "a more focused and cunning record than its predecessors that in many ways puts everything the band have formerly produced into perspective." David Fricke of Rolling Stone also measured the album up to earlier works from the band's oeuvre; "Tool have everything it takes to beat you senseless; they proved it on 1993's Undertow and their 1996 Grammy-winning beast, Ænima. Here, Tool go to extravagant lengths to drown you in sensation." In a review for Kerrang!, Dave Everly claimed "It's the most perfectly played, perfectly produced record you're likely to hear this or any other year" and that it was "one of the greatest albums you'll hear in your lifetime." Writing for NME, Andy Capper also approved of it; "Lateralus has added a little more colour to their palette of chanting, drumming and high drama. Singer Maynard James Keenan has been unaffected by the comparative tunefulness of his side project A Perfect Circle, while the stripped-down nature of the instrumentation means that Tool's innate heaviness shines out in a world of production tricks and dodges. There's no trickery—Tool's progressiveness is all their own work." By contrast, in a review for Pitchfork, Brent DiCrescenzo claimed that, "With the early new century demanding 'opuses', Tool follows suit. The problem is, Tool defines 'opus' as taking their 'defining element' (wanking sludge) and stretching it out to the maximum digital capacity of a compact disc." In the Village Voice, Robert Christgau lambasted the album, calling it
```

### Album 262, chunk 7

```text
"meaning-mongering for the fantasy fiction set." The review published in Blender described the album as sounding like "Black Sabbath jamming with Genesis at the bottom of a coal shaft." The album was a commercial success in the United States, debuting at No. 1 on the U.S. Billboard 200 albums chart with over 555,200 copies sold in its first week of release, just ahead of Missy Elliott's Miss E... So Addictive and dethroning Destiny's Child's Survivor. On August 5, 2003, the album was certified double platinum by the RIAA. On April 30, 2010, the album was certified gold by the BPI for sales of 100,000 in the U.K. In addition, Lateralus was certified double platinum by the ARIA and MC. Tool received the 2002 Grammy Award for Best Metal Performance for the song "Schism". During the band's acceptance speech, drummer Danny Carey stated that he would like to thank his parents "for putting up with [him]", and bassist Justin Chancellor concluded, "I want to thank my dad for doing my mum." Kludge ranked Lateralus at No. 2 on their list of top 10 albums of 2001. Kerrang! placed the album at No. 1 on their 2001 "Albums Of The Year" list. Q listed Lateralus as one of the best 50 albums of 2001. The album continued to gain accolades in the years following its release. In 2016, Loudwire named Lateralus the No. 1 hard rock/metal album of the 21st century. The magazine also ranked it No. 6 on their "Top 25
```

### Album 262, chunk 8

```text
Progressive Metal Albums of All Time." The album was ranked at No. 32 on Rolling Stone's 50 Greatest Prog Rock Albums of All Time list. Louder Sound placed the album at No. 33 on their Top 100 Prog Albums of All Time list. Publications have also continued to praise the performances by the band members on the album. NutSie.com ranked the drumming performance by Danny Carey on the song "Ticks & Leeches" at No. 3 on their list of Top 100 Rock Drum Performances. A vinyl edition and two DVD singles from the album were released later. The "double vinyl four-picture disc" edition of Lateralus was first released as a limited autographed edition exclusively available to fan club members and publicly released on August 23, 2005. Two music videos were produced; one for "Schism" (with the short ambient segue "Mantra" at the beginning) and one for "Parabol/Parabola". These were subsequently released as two separate DVD singles on December 20, 2005, featuring remixes of the tracks by Lustmord. Maynard James Keenan – vocals Adam Jones – guitars, art direction Justin Chancellor – bass Danny Carey – drums, percussion, samples Statik (Collide) – machines on "Triad" Tool – production David Bottrill – production, engineering, mixing Vince DeFranco (Synesthesia) – neurocistance, engineering
```

## Album 263: hopeless fountain kingdom — Halsey

- **album_id:** `645cff12-dcda-4080-aa09-2faa1a4ab810`
- **Tags (identification only):** pop, indie pop, synth pop, alternative, alternative pop, concept album, electronic, electropop
- **Chunks:** 12 (2867 words)

### Album 263, chunk 1

```text
Hopeless Fountain Kingdom (stylized in all lowercase) is the second studio album by American singer-songwriter Halsey. It was released on June 2, 2017, through Astralwerks. Conceived as a concept album, it serves as a companion to her debut studio album, Badlands (2015), and follows a narrative inspired by William Shakespeare's Romeo and Juliet. Halsey served as an executive producer and collaborated with producers including Greg Kurstin, Benny Blanco, Ricky Reed, and Cashmere Cat. Hopeless Fountain Kingdom is a pop, R&B, electropop, and synth-pop album, with elements of hip hop, soul, EDM, and alternative music. Its lyrics explore themes of love, heartbreak, desire, and identity through the story of two lovers from opposing worlds. The album features guest appearances from Quavo and Lauren Jauregui, while Sia and the Weeknd contributed as songwriters. It was supported by three singles—"Now or Never", "Bad at Love" and "Alone", as well as two promotional singles—"Eyes Closed" and "Strangers"; "Now or Never" charted within top 20 on the US Billboard Hot 100, while "Bad at Love" peaked at number 5 on the chart. Halsey further promoted the record with the Hopeless Fountain Kingdom Tour, which visited North America, Europe, Asia, Latin America, and Australia between 2017 and 2018. Hopeless Fountain Kingdom received generally favorable reviews from music critics, who often praised its ambition and conceptual scope, as well as Halsey's artistic development, although some criticized its stylistic influences and execution. The album charted at number one in the United States and Canada while reaching the top
```

### Album 263, chunk 2

```text
ten in Australia, Ireland, and New Zealand and peaking within the top 20 in multiple European countries. Hopeless Fountain Kingdom was certified double platinum in the United States and New Zealand, as well as platinum in Australia and Canada. Halsey said that she had not intended her debut studio album to target mainstream radio. While she described Hopeless Fountain Kingdom as having a more radio-friendly sound, she still considered herself an alternative artist, adding that she was "more than capable of writing radio music". For this album, Halsey worked with various producers like Greg Kurstin, Benny Blanco, and Ricky Reed. She was an executive producer and oversaw the album's concept, songwriting, visual direction, and accompanying fan experiences. Recording for Hopeless Fountain Kingdom primarily took place at studios in Los Angeles, with additional sessions held in Van Nuys and London. Halsey drew inspiration for Hopeless Fountain Kingdom from her experience in a toxic relationship. A concept album, it connects with her previous studio album, Badlands (2015); whereas Badlands used an apocalyptic setting as a metaphor for depression, Hopeless Fountain Kingdom follows two lovers from different worlds whose desire to be together leads them to sacrifice parts of themselves, drawing inspiration from William Shakespeare's play Romeo and Juliet. The opening track "The Prologue" features the play's prologue spoken by Halsey, while the music video for "Alone" was heavily influenced by Baz Luhrmann's 1996 film adaptation of the play, Romeo + Juliet. Halsey explained various parallels between lyrics in songs from both albums;
```

### Album 263, chunk 3

```text
each track contains connections to the album's wider narrative and to songs from Badlands through recurring lyrical references and themes. Speaking with Paper, Halsey revealed that Hopeless Fountain Kingdom is set in a purgatory-like world where two lovers from different backgrounds attempt to "beat the odds" and make their relationship work, unlike Badlands. Billboard author Colin Stutz pointed out that the album might be named after a real fountain built by Halsey's ex-boyfriend near the L train's Halsey Street station in Brooklyn. Halsey said that Hopeless Fountain Kingdom would incorporate more urban and R&B influences, while also featuring some stripped-down and vulnerable songs. Featuring collaborations with various artists including the Weeknd, Sia, Quavo, and Lauren Jauregui, the album is mainly rooted in pop, R&B, electropop, and synth-pop, with elements of trap-pop, alternative, hip-hop, soul, and EDM. Jon Caramanica of The New York Times noted that Halsey's adaptable vocal style allows her to move between different musical approaches, incorporating influences from other singers. Thematically, Hopeless Fountain Kingdom is noted for swapping the genders of Romeo and Juliet and including same-sex relationships. The main character is a bisexual female named Luna Aureum, and her main love interest is a male character Solis Angelus. There are references to female love interests in the songs "Bad at Love" and "Strangers"; the latter features Jauregui, who is also bisexual. "100 Letters" incorporates hand drum-driven instrumentation and a restrained chorus as well as atmospheric percussion loops and distant guitar textures. Featuring goth-leaning production, "Eyes Closed" combines
```

### Album 263, chunk 4

```text
layered backing vocals with melancholic melodies. Multiple critics compared it to the style of co-writer the Weeknd; Variety's Jem Aswad felt that the song adopted the Weeknd's signature "wistful" and "hazy" sound, arguing that the departure from Halsey's earlier style worked to her advantage. On "Alone", Deborah Krieger of PopMatters and Caramanica observed a lyrical and musical resemblance to Alessia Cara's "Here" and Ed Sheeran's "Dive", respectively. The alt-pop and soul song combines brass and cello instrumentation with the sounds of 1990s music. "Now or Never" is an R&B, dark pop, and mid-tempo song that adopts a more summer-influenced sound than much of Halsey's earlier works. "Sorry" is a classical piano ballad; Krieger highlighted the song for its stripped-back arrangement, which pairs Halsey's vocals with a somber piano accompaniment and largely avoids the vocal effects and electronic production found elsewhere on the album. "Good Mourning" is a one-minute interlude featuring spoken-word vocals by a child. An urban hip-hop and R&B song, "Lie" features guest vocals from Quavo, which adds a collaborative element to the album's midsection. According to Halsey, the mid-tempo pop ballad "Bad at Love" was intended to evoke the sounds of "Leonardo DiCaprio in a Hawaiian T-shirt in a droptop yellow convertible". "Walls Could Talk" is built around a violin riff and a stuttering chorus, drawing comparisons to late 1990s pop and R&B. Halsey co-wrote "Devil in Me" with Sia, which appears as part of the album's closing trio; it is paired with "Angel on Fire" and was
```

### Album 263, chunk 5

```text
noted for maintaining its emotional intensity without becoming excessive. The final track "Hopeless" is an electro song that features Cashmere Cat and incorporates elements of alternative music. The opening track "The Prologue" quotes Romeo and Juliet, which reinforces its conceptual framework. "100 Letters" depicts a deteriorating relationship through imagery of discarded love notes and emotional manipulation. The Observer journalist Kitty Empire observed that it balances expressions of "righteousness" and "self-excoriation". "Alone" portrays a narrator navigating parties, drinking, and social interactions while grappling with anxiety. Inspired by Halsey's breakup with co-writer Lido, "Lie" was described by Halsey as the most difficult song on the album to write. It depicts "both sides of a strange relationship gone off the rails" as she sings the lines "Are you misled? / I gave you the messiest head", according to Rolling Stone's Rob Sheffield. "Bad at Love" reflects on a series of Halsey's past relationships with both men and women, while acknowledging repeated mistakes in love. "Don't Play" concentrates on nightlife, partying, and substance use. "Strangers" depicts a same-sex relationship between two women, reflecting Halsey's intention to write a female–female love song. Alongside "Bad at Love", it is identified as one of the tracks in which Halsey explicitly references loving women. Krieger considered the lyrics of "Angel on Fire" as "the most teenager-y line", with Halsey singing "nobody seems to ask about me anymore / And nobody seems to care 'bout anything I think". Halsey referenced Hopeless Fountain Kingdom as early as 2014, posting "the
```

### Album 263, chunk 6

```text
Kingdom" via her Twitter. It prompted speculation among fans about its connection to the fictional settings established in her earlier works. When playing at Madison Square Garden in 2016, Halsey displayed the words "you can find me in the Kingdom" on a screen. In February 2017, she invited 100 fans in London to a church to hear four new songs from the album. In March, four Twitter accounts connected to Halsey began hinting at a storyline present in the album, involving two characters named Luna and Solis belonging to two different houses called the House of Aureum and the House of Angelus. Soon after the tweets were released, Halsey began mailing out quotes from Romeo and Juliet to her fans. Hopeless Fountain Kingdom was announced on March 7, 2017, along with a photograph of her holding a rose. On March 23, she announced the release date of June 2. To reveal the album's cover art, she had a global scavenger hunt, where miniature gun-shaped USB flash drives were hidden in nine cities around the world with pieces of the cover. To promote Hopeless Fountain Kingdom's narrative, Halsey and her team developed an extensive interactive campaign that included mailed clues, scavenger hunts, and character profiles designed to expand the storyline beyond the music itself. On May 4, "Eyes Closed" premiered at Apple Music's Beats 1 during an interview with Zane Lowe and Luhrman. On the same day, Halsey performed "Now or Never" at The Tonight Show Starring Jimmy Fallon, later at
```

### Album 263, chunk 7

```text
the Billboard Music Awards on May 21. Via Astralwerks, various editions of Hopeless Fountain Kingdom were released simultaneously on June 2, 2017. The 13-track standard edition was released on compact disc (CD), vinyl, digital download, and streaming services. The deluxe edition contains a remixed version of "Alone" which features the rappers Big Sean and Stefflon Don, while Target and Deluxe Plus editions include three additional tracks—"Heaven in Hiding", "Don't Play", and "Angel on Fire". Three singles supported Hopeless Fountain Kingdom. The lead single, "Now or Never", was released on April 4, 2017, with the accompanying six remixes. Co-directed with Sing J Lee and shot in Mexico City, its music video premiered on the same day. According to Halsey, the video—her directorial debut—forms part of a broader narrative telling the story of "two people in love despite the forces trying to keep them apart". "Now or Never" debuted at number 50 and peaked at number 17 on the US Billboard Hot 100, becoming her first single as a lead artist to reach the top 40 and her first since a collaboration with the Chainsmokers, "Closer" (2016). Two promotional singles, "Eyes Closed" and "Strangers" that features Jauregui, were released on May 4 and May 26, respectively. The former was supported by the accompanying music video. "Strangers" peaked at number 100 on the Hot 100, being Halsey's sixth entry and Jauregui's first as a solo artist. The second single, "Bad at Love", followed on August 22. It was recorded in Los Angeles alongside
```

### Album 263, chunk 8

```text
Reed and accompanied by its music video—also co-directed with Lee—picking up where the "Now or Never" video left off. The song was accompanied by five remixes. "Bad at Love" peaked at number five on the Hot 100 and entered various Billboard charts such as Streaming Songs, Pop Songs, and Radio Songs, reaching number one on the Dance Club Songs and Dance/Mix Show Airplay charts. After a music video for the track "Sorry" was released on February 2, 2018, a remixed version of "Alone" featuring Sean and Don served as the album's third single on March 15. Hannah Lux Davis co-directed the music video, and it was unveiled on April 6. "Alone" peaked at number 66 on the Hot 100. On May 3, 2017, Halsey announced the Hopeless Fountain Kingdom Tour in support of the album. PartyNextDoor and Charli XCX joined the tour as opening acts, and ticket pre-sales became available on May 8. Starting from Uncasville, Connecticut, on September 29, the tour concluded at Cleveland, Ohio, on November 22. In November, Halsey cancelled the remaining Canadian dates of the tour after stopping a concert in Alberta mid-performance. The following scheduled show in Edmonton was also cancelled, with promoters citing a "personal emergency". On March 26, 2018, Halsey announced an exclusive UK tour, set to take place at Eventim Apollo in London. Additional opening acts were Kehlani, Lauren Jauregui, and Niki, who performed in Australia, Latin America, and Asia, respectively. Jessie Reyez performed on the North American dates as a special
```

### Album 263, chunk 9

```text
guest. Alma and Raye served as opening acts for the final dates in London. On release, Hopeless Fountain Kingdom received generally positive reviews from music critics. At Metacritic, which assigns a normalized rating out of 100 to reviews from mainstream critics, the album has an average score of 66 out of 100, based on ten reviews. Critics frequently commented on the album's ambition and conceptual scope. Rob Sheffield of Rolling Stone wrote that Halsey "shows off all her wild musical ambitions" on her "bold" second album, describing it as a "sprawling science-fiction breakup tale" that indulges her penchant for "wide-screen melodrama". Jem Aswad of Variety wrote that Hopeless Fountain Kingdom largely succeeds, noting that it represents a "big step forward" both musically and conceptually from the more "monochromatic" sound of Halsey's debut, even though she is surrounded by "heavy company". Madelyn Tait of The Music wrote that Hopeless Fountain Kingdom shows Halsey's ability to create music that achieves radio appeal while retaining "creativity and originality", and praised it as a "complete body of work" that rewards listening from start to finish. Writing for NME, Rhian Daly likewise considered the album "ambitious" yet "cohesive", arguing that its numerous collaborators and guest appearances never distracted from Halsey's artistic vision. Reviewers also highlighted Hopeless Fountain Kingdom's expanded musical palette and Halsey's artistic development. Stephen Thomas Erlewine of AllMusic wrote that it broadened the EDM-pop foundation of Badlands with influences from singer-songwriter music, hip hop, and soul, arguing that its expanded stylistic range helped
```

### Album 263, chunk 10

```text
make its songs more distinctive, and Sheffield similarly characterized its sound as "adult dystopian synth-pop realness". In The Line of Best Fit, Grant Rindner felt that Halsey displayed greater versatility than on her previous releases, finding that the album suggested artistic growth even if it did not yet establish a definitive new sound for her career. Reviewing for Consequence, Dan Weiss noted the contributions of numerous collaborators but nevertheless viewed Halsey as an "album artist first", arguing that the record stands out most when Halsey draws on her experiences and insights regarding relationships with both men and women. Other critics questioned the album's originality and stylistic identity. Writing for The Observer, Kitty Empire argued that the album "succumbs to post-hit syndrome", citing Halsey's appearance on "Closer" as an early "omen". Although she considered the record "not remotely bad" and representative of the kind of "hotly awaited pop" album expected in 2017, she felt that the influence of the music industry was evident throughout. Jon Caramanica of The New York Times commended Halsey's lyrical perspective and delivery, noting that her narratives possess "rough edges and ellipsis endings". However, he felt that the album lacked a comparable "musical edge", arguing that it instead reflected "a belief in the crowdsourcing of ideas". In a mixed review, USA Today's Maeve McDermott felt that the album drew heavily from the "magpie-like" sounds of other artists, though she considered some of those influences "better" than others. Spin editor Jordan Sargent similarly described the record as a
```

### Album 263, chunk 11

```text
"deeply imperfect and too-often derivative" effort, while Deborah Kreiger of PopMatters criticized both its lyrical specificity and concept, arguing that its Romeo and Juliet-inspired narrative added little to the listening experience. Conversely, Spectrum Culture's Daniel Bromfield described it as "one of the most songwriting-focused pop records of the year". Although he considered the record "full of the trappings of an auteur project", he felt that Halsey's direct and personal writing prevented it from becoming overwrought. More critical of the album's execution, Katherine St. Asaph of Pitchfork argued that although its concept was ambitious, the album often relied on familiar pop conventions. While she praised songs such as "100 Letters", "Walls Could Talk" and "Alone", she felt that various stylistic experiments were less successful and concluded that the album's musical style did not always match its thematic ambitions. Hopeless Fountain Kingdom debuted at number one on the US Billboard 200 with 106,000 album-equivalent units, of which 76,000 were pure album sales. It made Halsey the first female act in 2017 to open atop the chart. In Canada, the album peaked at number one, while in Australia, it debuted at number two with first-week sales of 4,300 copies. The album debuted at number 12 on the UK Albums Chart, selling 7,123 copies in its first week. Across Europe and Oceania, it reached the top ten in Ireland and New Zealand, peaking at number seven and six, respectively. Elsewhere, it charted within the top 20 in Belgium's Flanders region, the Netherlands, Italy, Portugal,
```

### Album 263, chunk 12

```text
Spain, Norway, Finland, Austria, and the Czech Republic, while also reaching the top 30 in Germany, Denmark, Greece, Poland, Sweden, and Switzerland. The album attained lower peak positions in Belgium's Wallonia region, France, Latvia, and Slovakia. On the 2017 year-end charts, Hopeless Fountain Kingdom reached numbers 81, 194, and 61 in Australia, Flanders, and the United States, respectively. It further peaked at numbers 51 and 165 on the 2018 and 2019 year-end charts in the United States, respectively. Hopeless Fountain Kingdom has received certifications in multiple markets, including double platinum in Brazil, New Zealand, and the United States, platinum in Australia, Canada, and Norway, and gold certifications in Denmark, Mexico, Poland, Singapore, Sweden, and the United Kingdom.
```

## Album 264: Bravery, Repetition, and Noise — The Brian Jonestown Massacre

- **album_id:** `16dab716-a78d-42dc-8d66-9387cbe6f9c5`
- **Tags (identification only):** indie rock, experimental, psychedelic, psychedelic rock, rock, drone, folk rock, lo fi
- **Chunks:** 1 (175 words)

### Album 264, chunk 1

```text
Bravery Repetition and Noise is the eighth studio album by American psychedelic rock band The Brian Jonestown Massacre. The album was released in October 16, 2001. All the songs were written by Anton Newcombe, except the track "Sailor," originally by The Cryan' Shames. The album was produced by Anton Newcombe and Rob Campanella with additional mixing by Courtney Taylor. The front cover features American independent film director Jim Jarmusch. Incidentally, The Brian Jonestown Massacre's song "Not if You Were the Last Dandy on Earth" appears on the soundtrack to his film Broken Flowers. Anton Newcombe – vocals, guitar, bass, mini moog, mellotron, organ, drums, horns Jeffrey Davies – guitar, organ, fuzz, vocals Rob Campanella – Hammond organ, Mellotron, acoustic guitar, classical guitar, 12-string electric guitar, vox fuzz repeater Frankie Emerson – guitar Hunter Crowley – drums David Koenig – bass Bobby Hecksher – guitar James Ambrose – vocals, guitar Raymond Richards – pedal steel guitar Jeff Levitz (credited as Jeff Levitts) – guitar Mara Keagle – vocals Raugust – flute Courtney Taylor-Taylor – additional mixing
```

## Album 265: Crisis? What Crisis? — Supertramp

- **album_id:** `1881fe91-34e7-48de-a6d0-5fffe102393b`
- **Tags (identification only):** rock, art rock, progressive rock, album rock, pop, classic rock, pop rock, progressive pop
- **Chunks:** 3 (574 words)

### Album 265, chunk 1

```text
Crisis? What Crisis? is the fourth studio album by the British rock band Supertramp, released on 28 November 1975, by A&M Records. It was recorded in both London and Los Angeles, marking the group's first use of American recording studios. A remastered CD edition was issued on 11 June 2002, featuring the original artwork and credits as well as printed lyrics, which were absent from the initial release. Record Mirror listed Crisis? What Crisis? among the best albums of 1975 in its year-end survey. Following the commercial breakthrough of Crime of the Century (1974), Supertramp's record label pressed the band to deliver a follow-up quickly. While touring North America in early 1975, guitarist and vocalist Roger Hodgson injured his hand, forcing the cancellation of remaining dates. The downtime was used to begin work on the next album. Despite the additional time, the band entered the studio with little new material, relying heavily on leftover compositions from Crime of the Century and earlier. The shortage of songs forced a temporary halt in production while Hodgson and keyboardist Rick Davies wrote additional tracks, including "Ain't Nobody But Me". Four songs—"Sister Moonshine", "Another Man's Woman", "Lady", and "Just a Normal Day"—had already been performed live and were later issued on the 2001 concert release Is Everybody Listening?. Contemporary accounts suggest mixed feelings among the band. Hodgson described the album as hastily assembled and lacking the conceptual unity of Crime of the Century. Bassist Dougie Thomson echoed this view, calling it disjointed. In contrast,
```

### Album 265, chunk 2

```text
Hodgson later remarked in the mid-1980s that it was his personal favourite of the group's albums. Music writers have noted elements of continuity with Supertramp's later work. For example, Ultimate Classic Rock observed that the melody of "Sister Moonshine" anticipates the group's later hit "Give a Little Bit". The album's title and cover concept were devised by Davies. The sleeve depicts a man relaxing in a deckchair under an umbrella amid an industrial wasteland, photographed by Paul Wakefield. The background was shot in the Welsh mining valleys and later composited with the studio model. The imagery was partly inspired by Yves Robert's 1968 film Alexandre le bienheureux. The phrase "Crisis? What crisis?" also appeared in Fred Zinnemann's 1973 film The Day of the Jackal and was later used by the British press during the Winter of Discontent. Contemporary reviews were mixed. Rolling Stone offered a largely negative assessment, criticising the lyrics in particular. Retrospective appraisals have been more favourable. AllMusic highlighted Rick Davies' keyboard playing, Hodgson's vocals, and John Helliwell's saxophone contributions, describing the record as warm and subtly engaging. Rick Davies – lead and backing vocals, acoustic piano (tracks 3, 5, 7, 8), Wurlitzer piano (track 7), harmonica (track 2), organ (tracks 2, 3, 6, 10), harpsichord (tracks 4, 6, 10), synthesizers (tracks 1, 2, 4, 6, 8, 9) Roger Hodgson – lead and backing vocals, electric guitar (tracks 1, 2, 3, 5, 6, 7, 9) 12-string guitar (tracks 1, 2, 9, 10), acoustic piano (track 4), Wurlitzer piano
```

### Album 265, chunk 3

```text
(track 6), flageolet (track 2), cello (track 7), pump organ (track 10), marimba (track 6), electric sitar (tracks 1, 2) John Anthony Helliwell – saxophones, clarinet and bass clarinet (tracks 7, 10), backing vocals (tracks 3, 6, 7, 10) Dougie Thomson – bass guitar Bob Siebenberg (credited as Bob C. Benberg) – drums, percussion Ken Scott - producer Supertramp - producers John Jansen - assistant Ed Thacker - assistant Richard Anthony Hewson - arranger
```

## Album 266: Kiln House — Fleetwood Mac

- **album_id:** `65b3fbb5-8787-43a3-959a-177669a28f09`
- **Tags (identification only):** rock, blues rock, blues, classic rock, pop rock, soft rock
- **Chunks:** 7 (1702 words)

### Album 266, chunk 1

```text
Kiln House is the fourth studio album by British blues rock band Fleetwood Mac, released on 18 September 1970 by Reprise Records. This is the first album after the departure of founder Peter Green, and their last album to feature guitarist Jeremy Spencer. Christine McVie was present at the recording sessions and contributed backing vocals, keyboards and cover art, although she was not a full member of the band until shortly after the album's completion, when she was to join the band for the album's accompanying tour. The album peaked number 39 in the UK, becoming their last album to reach the top 40 in that country until their 1975 self-titled album. It also reached number 67 and number 69 in Canada and the United States, which up to that point was band's highest charting album in those respective countries. Kiln House was recorded after the departure of Peter Green, a founding member of Fleetwood Mac. Around the time of Green's final performance with the band on 28 May 1970, the remaining members regrouped by moving to the English countryside with their wives, children, and road managers. John McVie commented that "The legs went out from under us, and we were faced with a future without Peter." The album title is taken from the name of two converted oast houses, known as Kiln House, in Truncheaunts Lane in East Worldham, near Alton, Hampshire. The oast houses had previously been used for drying hops for beer brewing and were later combined
```

### Album 266, chunk 2

```text
into one building. In 1977, the property became a listed building. The band leased Kiln House and lived there communally with their families for a six-month period in 1970. Mick Fleetwood married Jenny Boyd at the house on 20 June 1970. McVie recalled that they spent some of their time smoking hashish and making tie-dye shirts at the property. The band converted one of the spaces within the facility into a music room. Boyd described the space as a converted barn and said that the band used the room to rehearse material. She recalled occasionally overhearing Kirwan singing wordless vocals over the music as they practiced. Spencer later recounted his memories recording the album in a Q&A. I remember sitting with Mick, Danny and Christine in a small side room off the practice studio that occupied what decades ago used to be the oast-drying place for the making of beer and mulling over our future. All we knew, Danny and I, was that we had some material to record. The band spent two weeks recording Kiln House at De Lane Lea Studios. Christine McVie, who at the time was still known as Christine Perfect, lived in Kiln House with the band and participated in the album's recording sessions. She was signed to Blue Horizon as a solo artist and could not be credited as a musician in the liner notes of Kiln House due to contractual reasons. Clifford Davis, the band's manager, provided McVie with session money for her contributions.
```

### Album 266, chunk 3

```text
Spencer, who played on one track during the recording of the previous album, Then Play On, played a much more active role during the Kiln House sessions. His retro 1950s homages and parodies dominate the album and Danny Kirwan's songs are almost equally prominent. Spencer was particularly influenced by rockabilly and music from the Sun Records record label. He recorded several of his demos on Revox machines and overdubbed multi-track vocal harmonies onto the demos. The band would later incorporate some vocal harmonies onto final versions that appeared on Kiln House. During the recording process, microphones were positioned close to the drums to achieve a sound that Fleetwood described as "very closed down" and "tight". Fleetwood also placed towels on his drums to create a muted tone. "Buddy's Song" is derivative of "Peggy Sue Got Married" with new lyrics listing a number of Buddy Holly song titles with a writing credit given to Buddy's mother. Fleetwood Mac's cover of "Hi Ho Silver" was based on a recording titled "Honey Hush" from Johnny Burnette's Rock and Roll Trio. Johnny Burnette's nephew, Billy Burnette, later joined Fleetwood Mac in 1987. Fleetwood Mac performed "Buddy's Song" and "Honey Hush" on BBC Radio 1 for a broadcast on Top Gear; these recordings later appeared on Live at the BBC in 1995. "Jewel Eyed Judy" was written about the band's secretary Judy Wong. McVie wrote the lyrics with Boyd, who at the time was four months pregnant with her first child. The song was also
```

### Album 266, chunk 4

```text
released as a single in certain markets, including the United States and the Netherlands. Spencer's "Blood on the Floor" was a style parody of country and western dirges. An early version of Kirwan's instrumental "Earl Gray", entitled "Farewell", was later released on the compilation The Vaudeville Years. Demos of the song were recorded in the middle of April 1970 at De Lane Lea Studio when Green was still a member of the band. Spencer originally wanted to drop "One Together" from the album, but the band convinced him otherwise. "Tell Me All the Things You Do" was included in Fleetwood Mac's live setlists through 1977 and again in 2018–2019 during the band's An Evening with Fleetwood Mac Tour. "Mission Bell" was a cover of a 1960s ballad originally performed by Donnie Brooks. In a Q&A, Spencer said that their cover of "Mission Bell" was not universally accepted by the public; he recalled hearing people express their displeasure with the rendition included on Kiln House. Five days before they were set to depart for their American tour, the band asked Christine Perfect to join Fleetwood Mac. Following five days of rehearsals, the band left for America on 26 July 1970. The band's first performance was in New Orleans on the first of August. One week after her first performance with the band, the British press announced that she had joined the group and would be known as Christine McVie from then on. McVie said that the band was met with apprehension
```

### Album 266, chunk 5

```text
for some of their performances, particularly amongst those who missed Peter Green. "I think the audience are wondering what we are going to be like. Before Peter ran the band. Now there is no leader, we just take turns. Obviously, some of the people miss Peter's guitar playing. But then, the sound is different now and other people have said that they don't even notice he's missing." McVie said that she was a "nervous wreck" during the tour and remembered that the shows incorporated some improvisation with extensive soloing. She credited this tour as being "a time of learning" for improving her keyboard playing. "Let's Dance" by Chris Montez and "Mission Bell" were among the songs included in the band's setlist. Spencer did not participate during certain portions of the set and would join the band later on to perform covers, particularly tracks from Elmore James. Spencer recalled that the album and ensuing tour were met with hostility in the UK. However, Kiln House was received much more favorably in North America, where it peaked at No. 69 on the Billboard 200 album chart on 7 November 1970 and No. 67 in Canada's RPM Magazine, 19 December 1970. At the time, Kiln House was Fleetwood Mac's best-selling album in the US. In 1971, the band travelled to Los Angeles for their next performance, where they were slated to play at the Whisky a Go Go. After they arrived at the hotel, Spencer informed Fleetwood that he was going out to
```

### Album 266, chunk 6

```text
visit a bookstore. The performance was cancelled when Spencer did not return; Davis contacted the local police and a local radio station to determine Spencer's whereabouts. Davis was later informed that Spencer had joined The Children of God, a religious cult, and travelled to their headquarters to meet with Spencer. During their discussion, Spencer maintained his preference to remain with The Children of God and confirmed that he would not be returning to Fleetwood Mac. Rather than cancel the tour, the band asked Green to fulfill the remaining dates. In his review of Kiln House, J.R. Young wrote in Rolling Stone that the album was "carefully conceived and prepared" and marked a shift from the Fleetwood Mac's earlier work with Green, saying that "Danny Kirwan and Jeremy Spencer took up the slack and built a new engine" for the band. He felt that Kirwan was successful in reining in Spencer's retro-pastiches such as "Blood on the Floor" and also found Spencer's material on Kiln House to be more tasteful than the songs found on his self-titled album released earlier in 1970. Billboard characterised the album as a foray into "the roots of contemporary rock." Record World noted the band's pivot away from blues music in favor of "straightaway rock entertainment" and believed that fans of the band would find the material pleasing. Cashbox thought that Kiln House demonstrated the band's ability to create "new and exciting material". Robert Christgau rated the album higher than Then Play On even with the
```

### Album 266, chunk 7

```text
absence of the "miraculously fluent [Peter] Green." Regarding one aspect of the band’s then bifurcated style, he claimed "the mansions in their jazzy blues/rock and roll guitar heaven are spacier than ever." In reference to the album’s rockabilly parodies, he admitted that Spencer's "Blood on the Floor” was "less charitable than one would hope", but was more complimentary toward "This is the Rock". Beat Instrumental described the band as a "mighty fine unit" without Green and highlighted the "nostalgia for the fading 'fifties" that permeated through Spencer's compositions. They also thought that "Station Man" and "Tell Me All the Things You Do" exemplified the band's "multi-guitar work". In a retrospective review, Bruce Eder of AllMusic wrote that the album lacked the intensity found on some of their previous work with Green, but said that the album instead "broaden[ed] the band's use of blues into other contexts, and add[ed] new influences in the absence of Green's laser-like focus." Danny Kirwan – guitar, vocals Jeremy Spencer – guitar, slide guitar, vocals, piano John McVie – bass guitar Mick Fleetwood – drums, percussion Christine McVie – Wurlitzer 200A, piano, backing vocals (uncredited) Producer – Fleetwood Mac Engineer – Martin Birch Cover drawing – Christine McVie
```

## Album 267: Troubled Paradise — Slayyyter

- **album_id:** `61b96c7f-4834-4da1-a998-d3308d827f03`
- **Tags (identification only):** electronic, bubblegum bass, dance pop, electropop, hip hop, house, hyperpop, indie pop
- **Chunks:** 5 (1180 words)

### Album 267, chunk 1

```text
Troubled Paradise is the debut studio album by American singer Slayyyter. It was released on June 11, 2021, by Fader Label. It received generally positive reviews from music critics, who praised the updated production, lyricism and maturity in songwriting. Some critics deemed this album an improvement from her debut mixtape. In September 2019, after releasing a string of singles and having achieved a moderate success with tracks on TikTok, as well as ascending in social media as an emerging star in niches such as hyperpop and the Stan Twitter community, Slayyyter released her eponymous debut mixtape. A month before its release, the artist answered some online questions regarding the mixtape. In response to a fan asking if rock would be present on the mixtape, she replied that she would be "saving this style for S2", presumably referring to her then-upcoming debut studio album. Later, Slayyyter did indeed work with the genre in some of the Troubled Paradise tracks. Slayyyter stated that she named the album after the title track, "Troubled Paradise," as a condensed version of the phrase "trouble in paradise." The album’s visuals and sound were partly inspired by Gwen Stefani's Love. Angel. Music. Baby. (2004). The multi-genre nature of the album was intentional, a bid to show fans her diverse potential as an artist and to break away from her past Y2K and bimbo aesthetics. In September 2019, a few days before the release of Slayyyter, the singer was questioned on Twitter about a popular unreleased track among
```

### Album 267, chunk 2

```text
fans she had mentioned and played before, "Doghouse" (later, "Dog House"). The answer was "yes :} will be finished for s1 deluxe edition". Months after that, she continued to tease fans with a taste of what was coming, having teased "Doghouse" almost in full while livestreaming on Instagram. Some other rumors also started spreading about what songs would be included in Slayyyter's next record. Known tracks at the time (late 2019 and early 2020) were "Talk to Me", "ID", "Dangerous", "Villain" and "Heaven". None of those tracks, with the exception of "Villain" and "Dog House", were added to the final tracklist of Troubled Paradise. It is also worth noting that since the release of her first demos on SoundCloud, around 2018, the release of her debut mixtape and Mini Tour in 2019, until the release of Troubled Paradise in 2021, Slayyyter gained enough popularity to obtain a loyal fanbase. "Serial Killer" was one of the first songs Slayyyter ever wrote, which she brought back for this album. The production of Troubled Paradise has its roots back in Slayyyter's Mini Tour (2019), when she teased fans saying the album would be "much better" than her debut mixtape and that they would love it. In early 2020, the singer traveled to L.A. to work on the record. She ended up staying there, while many recording studios shuttered and halted music production. "A lot of people were, like 'I can't make songs right now 'cause I can't get to the studio [...] And
```

### Album 267, chunk 3

```text
I was like, '[That] sucks. I'm fine. I know how to do it.'", she says. Regarding the production of Troubled Paradise, she stated in interviews that its sound would be cleaner than her previous record, as she realized many fans were criticizing the mixing of Slayyyter. "It isn't bedroom pop", says the artist. Slayyyter said that the album was divided into a rap-centered first half and a pop-centered second half. Slayyyter described her sound during this era as experimental pop. She also said that the album’s lyrics were supposed to be "vulgar" and "ridiculous" in order to play with taboos and humor, comparing her humor to Cardi B's. Slayyyter later described the album's visuals as a "disaster". Slayyyter described "Venom" as an "club track," and the most "insane" song on the album. Throatzillaaa was inspired by a comment Slayyyter's friend made about a porn star. Slayyyter cited “Clouds” as the best song she had ever made, in June 2021. Clouds was inspired by the imposter syndrome she felt as an unsuccessful artist during the COVID-19 quarantine. "Cowboys" and "Serial Killer" are narratively driven, and saw Slayyyter pushing herself to write stronger lyrics. She said that "Letters" is her first love ballad, a stark contrast from the explicit nature of her other work. On October 21, 2020, "Self Destruct" was released as the album's lead single, accompanied by the release of its music video hours later. The music video was directed by Brent McKeever. "Throatzillaaa" was released as the first promotional
```

### Album 267, chunk 4

```text
single on November 13, 2020. A lyric video was made available on November 9 before the official announcement on November 11. In December, the title track "Troubled Paradise" was registered on Slayyyter's ASCAP. before being officially announced on January 19, 2021. "Troubled Paradise" and its music video, directed by Munachi Osegbu and produced by Collin Druz, were released on January 22. The song was leaked in full the day before, as well as the album's final tracklist, cover art and the "Troubled Paradise" music video. On January 21, 2021, one day before planned, Slayyyter announced the official album title as Troubled Paradise on social media, along with its official art cover and release date of June 11, 2021. The day after, the tracklist and pre-sale were made available. "Clouds" was released as the next single on February 26, 2021, followed by "Cowboys" on April 9 and "Over This!" on May 7. Critics including Nick Malone of PopMatters and Stereogum's Chris DeVille noted Slayyyter's departure from her previous Britney Spears-influenced sound on Troubled Paradise. The record's sound recalled the "pure pop" era of the early 2010s, and was compared to veteran pop acts like Kesha, No Doubt, Robyn, Robin S., Lady Gaga, and Paramore as well as Slayyyter's contemporaries like Ashnikko, Rina Sawayama, Charli XCX, and Kim Petras. DeVille criticized Troubled Paradise for adopting the hyperpop sound without pushing the genre's sonic boundaries meaningfully. The album drew on the sex-positive club, techno, and electropop sounds of the era, while remaining surface-level
```

### Album 267, chunk 5

```text
in its exploration of them, according to him. Abigail Firth of Dork magazine called the album "fun and tacky," and noted Slayyyter's embrace of pop-punk on "Over This!" and "Cowboys". According to Firth, Slayyyter solidified her presence in the music industry with this album. Beyond the Stage magazine lauded the three-song run from "Troubled Paradise" to "Cowboys" as the arc of the album, reinforcing Slayyyter's "rambunctious" image. They also pointed to Slayyyter's references to The Wizard of Oz throughout the album, both lyrically and aesthetically, as a means to explore her identity as an artist. Wuki – mixing, recording (1) Rob Kinelski – mixing (2, 5–12) Ike Schultz – mixing (3, 4) Robokid – recording (2, 4–6) Gupi – recording (3) John Hill – recording (6) Jordan Palmer – recording (6) Schmarx – recording (7) Nicopop – recording (7) Dave Burris – recording (8) Micah Jasper – recording (8) Lauren D'Elia – recording (9) Pilotpriest – recording (9) Chris Greatti – recording (10, 11) Zakk Cervini – recording (10, 11) Kyle Shearer – recording (12) Nate Campany – recording (12)
```

## Album 268: A Private Heaven — Sheena Easton

- **album_id:** `f31183c8-81b2-450c-836b-2fd8cd98a93e`
- **Tags (identification only):** adult contemporary, dance pop, contemporary pop/rock, electro, electronic, pop/rock, soft rock, synth pop
- **Chunks:** 3 (683 words)

### Album 268, chunk 1

```text
A Private Heaven is the fifth studio album by Scottish singer Sheena Easton, released on 21 September 1984 by EMI America Records. The album featured two Billboard Hot 100 Top 10 singles – the lead single "Strut" and the controversial "Sugar Walls", whilst "Swear", a third single, peaked at No. 80. Recognised as Easton's most successful studio album in the United States where it peaked at No. 15 on the US Billboard 200, it sold over one million copies in the United States, earning a gold and platinum certification from the RIAA. In Canada, the album also went platinum. The tour that year featured Bruce Hornsby on keyboards in the live band. The album marked a conscious effort by Easton to change her image to that of a sexy pop singer after cultivating a "sweet and innocent" image since the launch of her career five years earlier. The sexually charged "Strut" - co-written by Charlie Dore - became Easton's biggest solo hit in the US since 1981's "For Your Eyes Only". Easton collaborated with Prince on the controversial track "Sugar Walls", written by Prince under the pseudonym Alexander Nevermind. The track and its accompanying video were banned in some regions due to its sexually risqué lyrics and was one of several songs cited by Tipper Gore on her Filthy Fifteen list in her efforts to introduce mandatory warning labeling of explicit musical albums. Easton's musical association with Prince continued for the next few years, with him writing "Eternity" for her
```

### Album 268, chunk 2

```text
eighth studio album, No Sound But a Heart (1987) and Easton later featuring on Prince's singles "U Got the Look" in 1987 and "The Arms of Orion" in 1989. The album also includes cover versions of Tim Scott's new wave track "Swear" and Joan Armatrading's 1976 classic "Love and Affection". Converse to the album's success in America, in the UK, it was her first studio album not to chart, and none of the singles released made the official Top 75. In 2000, One Way Records released a remastered version of A Private Heaven with bonus tracks and B-sides. On 23 February 2013, Edsel Records (UK) reissued Easton's A Private Heaven and its follow-up studio album Do You (1985) on two CDs remastered with bonus tracks. On 24 November 2014, the album was included in a box set in the UK with all of her first five albums with EMI through Warner Music Group. A 2CD deluxe edition of A Private Heaven, remastered from the original master tapes for the first time with 21 bonus tracks, including 12 previously unreleased tracks, along with 12" mixes and B-sides, was released on 25 February 2022 by Cherry Pop/RT Industries. On 31 May 2024 RT Industries and Cherry Pop Records released a 40th Anniversary Edition of the album featuring 12" mixes and three previously unreleased tracks on a red vinyl double LP set. In 2025 RT Industries released "A Private Heaven" in (Ultimate Edition) format for streaming services. Cashbox magazine reviewed the album in
```

### Album 268, chunk 3

```text
October 1984, writing that with "Virtually unlimited talent, Sheena Easton is at her absolute best", describing the album as "dazzling" and featuring "solid, punchy, techno-pop production with dramatic ballads". The album spent 35 weeks on the US Billboard album charts and reached its peak position of No. 15 in early February 1985. Sheena Easton – lead vocals, backing vocals Michael Boddicker – keyboards Greg Mathieson – keyboards Michael Landau – guitars Lee Ritenour – guitars Steve Lukather – all guitars (9) Abraham Laboriel – bass Carlos Vega – drums Lenny Castro – percussion, bongos Gary Herbig – saxophones Larry Williams – saxophones Bill Reichenbach Jr. – trombone Gary Grant – trumpet Jerry Hey – trumpet, horn arrangements Trevor Veitch – music contractor Steve George – backing vocals Tom Kelly – backing vocals Richard Page – backing vocals Devo – backing vocals Prince – synthesizers (2), electric guitar (2), Linn LM-1 (2) Greg Mathieson – producer, arrangements David Leonard – recording, mixing Wally Traugott – mastering at Capitol Mastering (Hollywood, California) Sue Mann – make-up Barron Matalon – hair stylist Harriet Wasserman – management
```

## Album 269: To Leave or Die in Long Island — Bomb the Music Industry!

- **album_id:** `32575b28-d8da-40b5-bbf9-ffb8ad3296f6`
- **Tags (identification only):** rock, ska punk, acoustic rock, alternative emo, alternative punk, ambient, anarcho punk, electropunk
- **Chunks:** 1 (212 words)

### Album 269, chunk 1

```text
To Leave or Die in Long Island is the second release by the DIY collective Bomb the Music Industry!. It is considered a "mini-album" by the band members, being too long to be an EP but not long enough to be a full-length. The album was released by Asbestos Records on vinyl in December 2006, after a delay due to a manufacturing error. The first pressing consists of three versions on vinyl, and a limited edition picture disc. "Congratulations, John, On Joining Every Time I Die" is about BtMI! guitarist/bass player John DeDomenici, who singer/guitarist Jeff Rosenstock thought was going to quit BtMI! to join metalcore band Every Time I Die. He did not. The line "1, 2, 3, 1, 2, 3, Pick it up, 1, 2, 3" in the bridge is an homage to the Every Time I Die song "Off Broadway", but the actual lyric in the song is "keep it up", not pick it up. The sample at the beginning of "Showerbeers" is from the movie Can't Hardly Wait. "Bomb the Music Industry! (and Action Action) (and Refused) (and Born Against) Are Fucking Dead" contains a sample from the British sitcom The Office. "Brian Wilson Says SMiLE! (a.k.a. Beard of Defiance)" uses a sample from The SpongeBob SquarePants Movie.
```

## Album 270: Insomniac Doze — envy

- **album_id:** `b8287878-0559-441f-bee6-a5168e74b64c`
- **Tags (identification only):** rock, alternative, emo, envy, experimental, hardcore, post hardcore, post metal
- **Chunks:** 1 (105 words)

### Album 270, chunk 1

```text
Insomniac Doze is the fourth album from Envy. The album was released in September 2006 by Temporary Residence Limited in the United States, by Rock Action Records in the United Kingdom, and by Sonzai Records in Japan. The sound of Insomniac Doze is characterized as being more epic and atmospheric than what is noted in Envy's previous albums. The album also displays Envy's ability to create a cohesive conglomeration of hardcore punk and screamo alongside melodic post-rock elements. Dairoku Seki - drums Tetsuya Fukagawa - sequencer, vocals Nobukata Kawai - guitar Masahiro Tobita - guitar Manabu Nakagawa - bass guitar Takashi Kitaguchi - recording, mixing
```

## Album 271: Stain — Living Colour

- **album_id:** `52588560-d63e-4a82-b068-87de71b10752`
- **Tags (identification only):** funk metal, alternative metal, rock, 1993, alt metal, hard rock
- **Chunks:** 3 (652 words)

### Album 271, chunk 1

```text
Stain is the third studio album by American rock band Living Colour. It was released on March 2, 1993, by Epic Records. It is the first album to feature bassist Doug Wimbish. Stain features a generally heavier sound with more pessimistic themes, the songs representing a range of genres. It peaked at #26 on the Billboard 200. The song "Leave It Alone" was nominated for Best Hard Rock Performance at the 36th Annual Grammy Awards in 1994, but lost to "Plush" by Stone Temple Pilots. From the mid-1990s through the early 2010s, the album was out of print due to rights issues after a lawsuit from Jon Stainbrook of the band The Stain forced Sony to cease production of the album. In November 2013, the album was reissued by Music On CD and is also available as an MP3 download. In June 2018, the album was reissued on limited edition green vinyl. The album has retrospectively been considered a "dark horse" in the alternative rock, hard rock, and heavy metal genres. In 2015, Corey Glover explained, "Stain was a darker turn for us. Muzz was out of the band at that point, and Doug had taken over, and we kind of got really dark. I think about songs like 'Postman,' and just how menacing and dark that song is. It had some very interesting things about it, and I think it was a turn. And part of that I think was about how far we had gotten to that point...I
```

### Album 271, chunk 2

```text
don't know if 'jaded' is the word, but we were sort of worn out by the world that we lived in. And just reflecting how worn out we were getting. I think it holds up. If you want to hear some really good hard rock - closer to the metal parts of our existence - I think Stain is the record that has the most of that." The sample "Fifty-six times in eighty-one seconds. Something like this," at the start of "This Little Pig" is taken from Bill Bradley discussing the blows of the four officers beating Rodney King. The cover art features a woman, the model Mouri Mbonika, wearing a scold's bridle. At the time of the album's release, reviews were mixed, including David Browne in Entertainment Weekly giving it a C− rating, and saying "What happened to the lively, spunky, and essentially good-humored band of Living Colour's debut, Vivid? Stain doesn't flow; it clots." That year, the album did not even make the top-25 'albums of the year list' in Kerrang!, whereas both Vivid and Time's Up had in previous years. But there were also positive reviews, including renowned music critic Robert Christgau giving it an A− rating in Consumer Guide Album, and saying "The best thing about this excellent record is how hard it crunches." And in an interview with Vernon Reid in Rolling Stone that year, journalist David Breskin praised Stain as "by far their best record." Stain was included in the 2014 book Overlooked/Underappreciated: 354
```

### Album 271, chunk 3

```text
Recordings That Demand Your Attention. In 2018, Loudwire said "But twenty-five years later, the album seems more relevant than it ever was in its day." In 2023, Stain came in at #423 of a "Best 1,000 Albums Ever" list on the PopThruster site. In a retrospective album review, AllMusic said that "The tracks were more focused and streamlined when compared to the all-encompassing compositions on 1990's Time's Up, but were just as hard-hitting and thought provoking." In 2022, the Metal Injection site reported the band may be re-recording the album, after a post on Instagram that showed Vernon Reid recording guitar parts for a new rendition of the song "Nothingness". Corey Glover – vocals Vernon Reid – guitars, guitar synthesizer Doug Wimbish – bass, ambiance Will Calhoun – drums Andrew Fairley – vocals on "Hemp" Bernard Fowler – backing vocals Ron Saint Germain – production, recording, mixing Andre Betts – additional production
```

## Album 272: Peter Criss — Peter Criss

- **album_id:** `29f77101-a250-494a-a226-09a7af66e4f4`
- **Tags (identification only):** hard rock, album rock, heavy metal, rock, arena rock, classic rock, glam, glam rock
- **Chunks:** 4 (831 words)

### Album 272, chunk 1

```text
Peter Criss is the debut solo studio album by Peter Criss, the drummer of American rock band Kiss. It was one of four solo albums released by the members of Kiss on September 18, 1978, but yet under the Kiss label, coming out alongside Ace Frehley, Gene Simmons and Paul Stanley. The album was produced by Vini Poncia, who went on to produce Dynasty (1979) and Unmasked (1980) for Kiss. Peter Criss, in contrast to the anthemic hard rock of Kiss, was described as "pop rock, sung in the style of Rod Stewart," by Daly Andrew of MusicRadar. "My album reflected my musical taste," Criss explained in his 2012 autobiography Makeup to Breakup. "Motown-inspired R&B with horns and backup singers." Producer Vini Poncia aimed for emotional and relatable songs to Criss, recalling "he was able to do some white R&B, and bluesy kind of things that he grew up with. He was able to show the world a different side to him." Four of the tracks ("I'm Gonna Love You", "Don't You Let Me Down", "That's the Kind of Sugar Papa Likes" & "Hooked on Rock 'n' Roll") were originally written in 1971 for Criss's pre-Kiss band, Lips. Criss also covers "Tossin' and Turnin'", which was a No. 1 hit for Bobby Lewis in the U.S. during the summer of 1961. The song was subsequently covered by Kiss on their 1979 tour. Reviews for Peter Criss were mostly negative. In a retrospective assessment AllMusic called it "the most undistinguished of
```

### Album 272, chunk 2

```text
the bunch, lacking hooks on either the pop-metal rockers or the power ballads, as well as personality throughout." The album was the lowest charting of all the Kiss solo albums of 1978, reaching No. 43 on the US Billboard album chart. Of the four solo albums, Peter Criss was the only album to have two singles released from it: "Don't You Let Me Down" and "You Matter to Me", neither of which charted. In an interview in Goldmine magazine, Stanley and Simmons dismissed the record as being completely opposite of the aims of what Kiss music was about. In rankings of Kiss' albums, Peter Criss was named the worst Kiss record by Eduardo Rivadavia of Loudwire, Paul Elliott of Classic Rock, and Matthew Wilkening of Ultimate Classic Rock. Rivadavia interpreted it as "a cry for help, after years trapped in the relentlessly charging Kiss machine, but it was nothing like the chorused cries of 'HELP!' issued by all the fans who bought this sub-yacht-rock debacle." He added that while the 1978 Kiss solo albums were meant as spaces for each member to "just be himself", Criss "clearly misread the memo and decided to 'just be Barry Manilow' instead." Wilkening commented that Criss was "clearly running as far from the band's hard rock sound as possible", instead creating an album that "leans heavily on ballads and the R&B sound of his previous groups. Even considering that, he simply doesn't have the songwriting talent or charisma to front an entire album." Elliott
```

### Album 272, chunk 3

```text
wrote that Criss, a fan of pop and soul music, "turned MOR crooner on lightweight toe-tapping tunes" such as "Don't You Let Me Down" and "That's the Kind of Sugar Papa Likes"; he deemed the ballad "I Can't Stop the Rain" the best song for how it suits Criss' raspy voice, but dismissively added that, overall, Peter Criss contained music that Kiss fans' parents would like. Nonetheless, he wrote that the title of "worst solo album made by a drummer" belonged to Keith Moon's Two Sides of the Moon (1975). Harvey Milk covered "Easy Thing" for their compilation album The Singles. Awaken covered "I'm Gonna Love You" on their double album Party in Lyceum's Toilets. The Slam covered "Hooked on Rock 'n Roll" on their album Hit It!. Peter Criss – lead vocals, drums on all songs except tracks 6–7 and 10, percussion on track 8, backing vocals Allan Schwartzberg – drums on tracks 6–7 and 10 Bill Bodine – bass guitar on tracks 1–5 and 9 Neil Jason – bass guitar on tracks 6–7 and 10 Art Munson – guitars on tracks 1–5 and 9 Stan Penridge – guitars on 1–5 and 8–9, backing vocals Elliot Randall – guitars on "Easy Thing" and "I Can't Stop the Rain" John Tropea – guitars on tracks 6–7 and 10 Brendan Harkin – guitars on "Easy Thing" Steve Lukather – guitar solo on "That's the Kind of Sugar Papa Likes" and "Hooked on Rock and Roll" Bill Cuomo – keyboards 1–5 and
```

### Album 272, chunk 4

```text
9 Richard Gerstein – keyboards on tracks 6–7, and 10 Davey Faragher, Tommy Faragher, Danny Faragher, Jimmy Faragher, Maxine Dixon, Maxine Willard, Julia Tillman, Vini Poncia, Annie Sutton, Gordon Grody – backing vocals Tom Saviano – Horns arranged Michael Carnahan – saxophone solo on "Tossin' and Turnin'", baritone sax on "Hooked on Rock 'n' Roll" Lenny Castro – percussion on "Tossin' and Turnin'" and "Don't You Let Me Down" Mike D. Stone – engineer at the Record Plant, New York City
```

## Album 273: I Am a Bird Now — Antony and the Johnsons

- **album_id:** `029abcc8-a31e-4d1f-887e-c3100a20e60a`
- **Tags (identification only):** art pop, chamber pop, art rock, avantgarde, indie, vocal jazz
- **Chunks:** 3 (552 words)

### Album 273, chunk 1

```text
I Am a Bird Now is the second studio album by Anohni's band Antony and the Johnsons, released on February 1, 2005, by Secretly Canadian. After it won the 2005 Mercury Prize, the record shot up the UK albums chart from No. 135 to No. 16 in one week, the biggest jump in the history of the prize. As of September 2011, UK sales stood at 220,000 copies. I Am a Bird Now features guest appearances by Rufus Wainwright, Devendra Banhart, Boy George and Lou Reed. The cover is a photograph by Peter Hujar of Warhol superstar Candy Darling on her deathbed. I Am a Bird Now received very positive reviews. On the review aggregate site Metacritic, the album has a score of 88 out of 100, indicating "universal acclaim". Drowned in Sound's Anthony Gibbons gave the album a score of 10/10, writing "It's not an exaggeration. This isn't hype. I Am A Bird Now is a beautiful, emotive, glorious, and sometimes sinister album that will top many a critic's list come the end-of-year polls, and justifiably so." Tiny Mix Tapes also gave the album a perfect score, writing "This music grabs a hold of you and doesn't let go. It feels timeless and gorgeous and bigger than life. It may not be 'soul' in the strict, music appreciation 101 sense, but it could make even the most jaded atheist approach a metaphysical regard... I'd put on my critic's cap and dive into scrutiny, but I am too enraptured by
```

### Album 273, chunk 2

```text
this artist's music." Pitchfork's Brandon Stosuy praised the vocals, writing "The ultimate draw is [Anohni's] voice, and within the first two seconds of the album, it should be very clear to even the most unaware newbies that [Anohni] has an amazing Nina Simone/Brian Ferry [sic]/Jimmy Scott vibrato, a multi-octave siren that would sound painfully lovely no matter what [she] was saying." The album has appeared on several end of year lists. Mojo named I Am a Bird Now the best album of 2005. Pitchfork ranked the album No. 5 on its list of the top 50 albums of 2005. On the same website, the track "Hope There's Someone" was ranked No. 28 on their list of the Top 500 Songs of the 2000s and was selected as 2005's best single. In 2019, the album was ranked 40th on The Guardian's 100 Best Albums of the 21st Century list. The song "For Today I Am a Boy" is the namesake for the book For Today I Am a Boy, by Kim Fu. The song's lyrics are quoted in the novel's epigraph. Anohni Hegarty – organ, piano, vocals Tahrah Cohen – drums Julia Kent – cello Parker Kindred – drums (track 7) Jeff Langston – bass Maxim Moston – violin Joan Wasser – viola Doug Wieselman – saxophone Devendra Banhart – guitar (track 5), vocals (track 8) Steve Bernstein – horn John Bollinger – drums (track 5) Keith Bonner – flute Boy George – vocals (track 5) Danielle Farina – viola (tracks
```

### Album 273, chunk 3

```text
2, 9) Jason Hart – piano (track 6) Rainy Orteca – bass (track 7) Lou Reed – guitar and vocals (track 7) Paul Shapiro – horn Rufus Wainwright – vocals (track 6) Julia Yasuda – Morse code, vocals (track 9) Emery Dobyns – engineer and mixer Doug Henderson – mixer and mastering
```

## Album 274: Sticky Fingers — The Rolling Stones

- **album_id:** `b6e1176b-161b-44e2-acdf-0dc493e0d805`
- **Tags (identification only):** rock, blues rock, hard rock, country rock, album rock, blues, rock and roll, drugs
- **Chunks:** 11 (2588 words)

### Album 274, chunk 1

```text
Sticky Fingers is the ninth studio album by the English rock band the Rolling Stones. It was released on 23 April 1971 on the Rolling Stones' new label, Rolling Stones Records. The Rolling Stones had been contracted by Decca Records and London Records in the UK and the US since 1963. On this album, Mick Taylor made his second full-length appearance on a Rolling Stones album (after the live album Get Yer Ya-Ya's Out!). It was the first studio album without Brian Jones, who had died two years earlier. The original Grammy-nominated cover artwork, conceived and photographed by Andy Warhol, showed a picture of a man in tight jeans, and had a working zip that opened to reveal underwear fabric. The cover was expensive to produce and damaged the vinyl record, so the size of the zipper adjustment was made by John Kosh at ABKCO Records. Later re-issues featured just the outer photograph of the jeans. The album featured a return to basics for the Rolling Stones. The unusual instrumentation introduced several albums prior was absent, with most songs featuring drums, guitar, bass, and percussion as provided by the key members: Mick Jagger (lead vocals, various percussion and rhythm guitar), Keith Richards (guitar and backing vocals), Mick Taylor (guitar), Bill Wyman (bass guitar), and Charlie Watts (drums). Additional contributions were made by long-time Stones collaborators including saxophonist Bobby Keys and keyboardists Billy Preston, Jack Nitzsche, Ian Stewart, and Nicky Hopkins. As with the other albums of the Rolling Stones late
```

### Album 274, chunk 2

```text
1960s/early 1970s period, it was produced by Jimmy Miller. Sticky Fingers is widely regarded as one of the Rolling Stones' best albums. It was the band's first album to reach number one on both the UK albums and US albums charts, and has since achieved triple platinum certification in the US. "Brown Sugar" topped the Billboard Hot 100 in 1971. Sticky Fingers was voted the second best album of the year in The Village Voice's annual Pazz & Jop critics poll for 1971, based on American critics' votes. The album was inducted into the Grammy Hall of Fame and included in Rolling Stone magazine's "The 500 Greatest Albums of All Time" list. With the end of their Decca/London association at hand, the Rolling Stones were finally free to release their albums (including cover art) as they pleased. However, their departing manager Allen Klein dealt the group a major blow when they discovered that they had inadvertently signed over their entire 1960s American copyrights to Klein and his company ABKCO, which is how all of their material from 1963's "Come On" to Get Yer Ya-Ya's Out! The Rolling Stones in Concert has since been released solely in America by ABKCO Records. The band later sued for their return but without success, settling in 1984. The band would remain incensed with Klein for decades for that act. Klein died in 2009. When Decca informed the Rolling Stones that they were owed one more single, the band submitted a track called "Cocksucker Blues",
```

### Album 274, chunk 3

```text
correctly assuming that this would be refused. Instead, Decca released the two-year-old Beggars Banquet track "Street Fighting Man" while Klein retained dual copyright ownership in conjunction with the Rolling Stones of "Brown Sugar" and "Wild Horses". Although sessions for Sticky Fingers began in earnest in March 1970, the Rolling Stones had been recording at Muscle Shoals Sound Studio in Alabama in December 1969, where they cut "You Gotta Move", "Brown Sugar" and "Wild Horses". "Sister Morphine", cut during Let It Bleed's sessions earlier in March of that year, had been held over from that release. Much of the recording for Sticky Fingers was made with the Rolling Stones' mobile studio in Stargroves during the summer and autumn of 1970. Early versions of songs that would eventually appear on Exile on Main St. were also rehearsed during these sessions. Sticky Fingers originally included 10 tracks. The music has been characterised by commentators as hard rock, roots rock and rock and roll. According to Rolling Stone magazine, it is "the Stones' most downbeat, druggy album, with new guitarist Mick Taylor stretching into jazz and country". The artwork emphasized the innuendo of the Sticky Fingers title, showing a close-up of a jeans-clad male crotch with the visible outline of a penis. The cover of the original vinyl LP featured a working zipper and perforations around the belt buckle that opened to reveal a sub-cover image of white briefs. The vinyl release displayed the band's name and album title along the belt; behind the
```

### Album 274, chunk 4

```text
zipper, the underpants were seemingly rubber stamped in gold with the stylized name of American pop artist Andy Warhol, below which read "THIS PHOTOGRAPH MAY NOT BE—ETC." The artwork was conceived and photographed by Warhol, and the design by Craig Braun. Billy Name is sometimes accredited as the photographer, however, Braun believes Warhol shot the Polaroid photos for the album, and the Factory associates who were involved in the photo shoot have claimed that Warhol took the photos. Braun and his team suggested wrapping the album in rolling paper – a concept later used by Cheech & Chong in Big Bambu – but Jagger was enthused by Warhol's concept. Warhol duly sent Braun Polaroid pictures of a model in tight jeans. We manufactured those kind of one-off packages, because a lot of conventional record suppliers were a bit baffled as to how to make them. I'd already done a few of them for bands like The Temptations, The Supremes, Joe Cocker and a teen idol named Bobby Sherman, where a band would be selling in sufficient quantities – maybe a million-plus – to have a custom-made sleeve. So when there was a big act like the Stones, you knew the initial release would be a million-plus, and a custom package could be made without costing the label too much of a premium. So the Stones' managers came to me and asked what I could do. Fans assumed the cover photo of the crotch to be Jagger, but he revealed that
```

### Album 274, chunk 5

```text
it was one of Warhol's "protégés". Jagger said it was Jay Johnson, but the general consensus is that Warhol used his lover Jed Johnson as the model for the cover. It remains uncertain exactly who appears on the cover because Warhol photographed several men and never publicly revealed which photos he used. Braun thought it was Jed Johnson on the cover, but he later said Warhol's business manager Fred Hughes told him it was makeup artist Corey Tippin, with which Tippin concurs, saying "I know my anatomy." Warhol superstar Joe Dallesandro also claimed to be the model on the cover, but Braun is sure it was not him. Former Interview magazine editor Bob Colacello said, "When the album came out, Glenn [O'Brein] was certain that it was he on the inside and Jay Johnson on the outside, but Andy would never say exactly whose crotch he had immortalized." O'Brien, who was an editor for Warhol's Interview magazine, was "100 percent certain" he was the underwear model: "I knew it was me because it was my underwear!" O'Brien initially stated that Jed Johnson was the model for the cover, but he later claimed that it was Tippin. He added that Warhol might not even have known who he selected. "He probably took these Polaroids, put them on the table, and picked ones he liked. I don't think it mattered to him [who it was]," said O'Brien. For the initial vinyl release, the album title and band name is smaller and at
```

### Album 274, chunk 6

```text
the top on the American release. For the UK release, the title and band name are in bigger letters and on the left. Reportedly, when retailers complained that the zipper damaged the vinyl (from stacked shipments), the zipper was "unzipped" slightly to the middle of the record, where damage would be minimized. Sticky Fingers earned a Grammy nomination for Best Album Cover at the 14th Annual Grammy Awards in 1972. The album introduced the tongue and lips logo of Rolling Stones Records, designed by John Pasche in 1970. Jagger suggested to Pasche that he copy the out-stuck tongue of the Hindu goddess Kali. Pasche felt that would date the image to the Indian culture craze of the 1960s, but seeing Kali changed his mind. Before the end of that year, his basic version was faxed to Craig Braun by Marshall Chess. The black and white copy was modified by Braun and his team, resulting in the popular red version: the slim one with the two white stripes on the tongue. Critic Sean Egan wrote: "Without using the Stones' name, it instantly conjures them, or at least Jagger, as well as a certain lasciviousness that is the Stones' own... It quickly and deservedly became the most famous logo in the history of popular music." The tongue and lips design was part of a package that, in 2003, VH1 named the "No. 1 Greatest Album Cover" of all time. In Spain, the original cover was censored by the Franco regime and replaced
```

### Album 274, chunk 7

```text
with a "can of fingers" cover featuring a hand mostly submerged in a can of treacle, which was designed by John Pasche and Phil Jude, and "Sister Morphine" was replaced by a live version of Chuck Berry's "Let It Rock". This track was later included on the CD compilation Rarities 1971–2003 in 2005. In 1992, the LP release of the album in Russia featured a similar treatment as the original cover; but with Cyrillic lettering for the band name and album name, a colourised photograph of blue jeans with a zipper, and a Soviet Army uniform belt buckle that shows a hammer and sickle inscribed in a star. Sticky Fingers was released on 23 April 1971 and reached number one on the UK Albums Chart in May 1971, remaining there for four weeks before returning at number one for a further week in mid June. In the US, the album hit number one within days of release, and stayed there for four weeks. The album spent a total of 69 weeks on the Billboard 200. According to Billboard's Top 200 list, it was one of the albums that topped the German chart that year. In a contemporary review for the Los Angeles Times, music critic Robert Hilburn said that although Sticky Fingers is one of the best rock albums of the year, it is only "modest" by the Rolling Stones' standards and succeeds on the strength of songs such as "Bitch" and "Dead Flowers", which recall the band's previously uninhibited,
```

### Album 274, chunk 8

```text
furious style. Jon Landau, writing in Rolling Stone, felt that it lacks the spirit and spontaneity of the Rolling Stones' previous two albums and, apart from "Moonlight Mile", is full of "forced attempts at style and control" in which the band sounds disinterested, particularly on formally correct songs such as "Brown Sugar". Writing for Rolling Stone in 2015, David Fricke called it "an eclectic affirmation of maturing depth" and the band's "sayonara to a messy 1969". In a positive review, Lynn Van Matre of the Chicago Tribune viewed the album as the band "at their raunchy best" and wrote that, although it is "hardly innovative", it is consistent enough to be one of the year's best albums. Writing for Slate, Jack Hamilton praised the album in a retrospective review, stating that it was "one of the greatest albums in rock 'n' roll history." Sticky Fingers was voted the second best album of the year in The Village Voice's annual Pazz & Jop critics poll for 1971. Lester Bangs voted it number one in the poll and said that it was his most played album of the year. Robert Christgau, the poll's creator, ranked the album 17th on his own year-end list. In a 1975 article for The Village Voice, Christgau suggested that the release was "triffling with decadence", but might be the Rolling Stones' best album, approached only by Exile on Main St. (1972). In Christgau's Record Guide: Rock Albums of the Seventies (1981), he wrote that it reflected how
```

### Album 274, chunk 9

```text
unapologetic the band was after the Altamont Free Concert and that, despite the concession to sincerity with "Wild Horses", songs such as "Can't You Hear Me Knocking" and "I Got the Blues" are as "soulful" as "Good Times", and their cover of "You Gotta Move" is on-par with their previous covers of "Prodigal Son" and "Love in Vain". In 1994, Sticky Fingers was remastered and reissued by Virgin Records. This remaster was initially released in a Collector's Edition CD, which replicated in miniature many elements of the original vinyl album packaging, including the zipper. Sticky Fingers was remastered again in 2009 by Universal Music Enterprises and in 2011 by Universal Music Enterprises in a Japanese-only SHM-SACD version; the latter was also used in 2013 for SHM-CD and Platinum SHM-CD, and then again in 2020 for another Japanese-only (standard) SHM-CD version. In June 2015, the Rolling Stones reissued Sticky Fingers in its 2009 remastering in a variety of formats to coincide with a concert tour, the Zip Code Tour. The Deluxe and Super Deluxe versions of the reissue featured previously unreleased bonus material (depending on the format): alternative takes of some songs, live tracks recorded on 14 March 1971 at the Roundhouse in London and the complete 13 March 1971 show at Leeds University. It re-entered the UK Albums chart at number 7, extending their UK Top 10 album chart span beyond 51 years and 2 months since their self-titled debuted at number 7 on 23 April 1964. It also re-entered
```

### Album 274, chunk 10

```text
the US Albums chart at number 5, extending their US Top 10 album chart span beyond 50 years and 6 months since 12 x 5 on 14 December 1964. Sticky Fingers was ranked number ten in the 1994 first edition of Colin Larkin's All Time Top 1000 Albums. He stated, "Dirty rock like this has still to be bettered, and there is still no rival in sight." In a retrospective review, Q magazine said that the album was "the Stones at their assured, showboating peak ... A magic formula of heavy soul, junkie blues and macho rock." NME wrote that it "captures the Stones bluesy swagger" in a "dark-land where few dare to tread". Record Collector magazine said that it showcases Jagger and Richards as they "delve even further back to the primitive blues that first inspired them and step up their investigations into another great American form, country." In his review for Goldmine magazine, Dave Thompson wrote that the album still is superior to "most of The Rolling Stones' catalog". In a 2018 retrospective review, The Guardian's Alexis Petridis ranked it the best album the band had ever produced, stating "their claim to be The Greatest Rock’n’Roll Band in the World has no more compelling evidence than the flawless 46 minutes of music here." David Hepworth wrote in his 2016 book Never a Dull Moment that the contributions of guest performers such as Keys, Jim Dickinson, and Preston gave the album "more musical range than any other Rolling Stones
```

### Album 274, chunk 11

```text
album", including "Dickinson's honky-tonk piano on 'Wild Horses'" and "Preston's churchy organ solo on 'I Got the Blues'". Hepworth also suggested that Taylor's "Latin-flavored guitar solo" on "Can't You Hear Me Knocking" was influenced by Santana's 1970 album Abraxas. Sticky Fingers was inducted into the Grammy Hall of Fame in 1999. It was listed as No. 63 on Rolling Stone magazine's 2003 list of The 500 Greatest Albums of All Time, No. 64 in a 2012 revised list, and No. 104 in a 2020 reboot of the list.
```

## Album 275: Post — Björk

- **album_id:** `0be84d67-1295-41ad-8fe6-f224279bee6d`
- **Tags (identification only):** electronic, art pop, trip hop, downtempo, idm, leftfield, pop, alternative dance
- **Chunks:** 21 (5221 words)

### Album 275, chunk 1

```text
Post is the second studio album by Icelandic singer Björk. It was released on 12 June 1995 by One Little Indian Records. Continuing the style developed on her first album Debut (1993), Björk conceived of Post as a bolder and more extroverted set of songs than its predecessor, featuring an eclectic mixture of electronic and dance styles such as techno, trip hop, IDM, and house, alongside that of ambient, jazz, industrial, and experimental music. Björk produced Post herself with co-producers including Nellee Hooper, 808 State's Graham Massey, and former Massive Attack member Tricky. She wrote most of the songs after moving to London and intended the album to reflect her new life in the city. The album reached number one in Iceland, number two in the United Kingdom and number 32 in the United States. It was certified gold in New Zealand and Sweden, and platinum in Australia, Canada, the US, and the UK. Six singles were released: "Army of Me", "Isobel", "It's Oh So Quiet", "Hyperballad", "Possibly Maybe", and "I Miss You", with three reaching the UK top 10. Their accompanying music videos were noted for their surrealism, themes of nature and technology, and artistic development of the medium. A remix album titled Telegram was released in 1996. During Post's commercial peak, Björk was affected by promotional touring and media attention. She assaulted a reporter and survived a murder attempt. Björk would relocate to Spain away from the press and produce her next album, Homogenic (1997). Considered an important
```

### Album 275, chunk 2

```text
exponent of art pop, Post has been praised by critics for its ambition and timelessness. It was named one of the greatest albums of 1995 by numerous publications, and has since been named one of the greatest albums of all time by publications including Entertainment Weekly and Rolling Stone. Björk released her previous studio album Debut in 1993. At that time, she had moved to London. The production of Debut was "long and laborious", as Björk sought to fully realise the songs she wrote from the past. After its release, she began to look for new ideas in the present for her next album. She contacted producer Nellee Hooper who had worked with her on Debut. He initially encouraged her to produce the album herself, but agreed when she insisted. Björk agreed to co-produce with other enlisted producers; "to make it stay fresh, she had to think about other people being involved". With Hooper's confirmation, Björk commenced work on the album in late 1994 at the Compass Point Studios in Nassau. The picturesque locale inspired Björk to meld the recording process with the exotic natural environment. For example, Björk waded into the ocean and recorded vocals while the sun set, captured by a digital recorder powered by a generator on the beach. The first version of "Cover Me" was recorded entirely from a cave. Björk incorporated songs she had written in Manchester with 808 State's Graham Massey before the recording of Debut. These included "Army of Me" and "The Modern
```

### Album 275, chunk 3

```text
Things", which she had performed live and did not need to be extensively changed. Björk said she left "Army of Me" off Debut as she felt Debut "was a more gentle energy and Post was more raw, more brutal". Massey said: "With 'Army of Me' we wanted to try something that was quite hard and techno-y. I'm not sure how she wrote those lyrics so fast but I remember that song being almost instantaneous. [...] We kind of knocked that off in one day and then started on 'The Modern Things' the same day and finished that the next." Although the album was supposed to be delivered the day after she returned from the Bahamas, Björk felt it was not yet complete and continued its production in London. She enlisted a new team of engineers and programmers, and spent the next months "tweaking, rearranging, and sometimes completely rerecording her pre-existing tracks". Ultimately, it was the inclusion of more "real" instruments that "resuscitated Post for Björk". Björk continued to compose songs such as "Isobel", which was created while she was visiting Reykjavík for Christmas, before bringing it back to Hooper's studio. The song's lyrics were written in collaboration with Icelandic poet Sjón, which was his first songwriting experience. Sjón would become a frequent collaborator throughout Björk's career. She also enlisted trip hop artist Tricky to assist in producing the album, on the condition that he would work on two tracks on her album and she would contribute two vocals for his
```

### Album 275, chunk 4

```text
album. Their collaboration resulted in the Post songs "Enjoy" and "Headphones"—in addition to "Keep Your Mouth Shut" and "Yoga", which appeared on Tricky's 1996 studio album, Nearly God. The track that underwent the most extensive change was "I Miss You", an old song from the Debut era. Howie Bernstein gave the song its "Latin-tinged [rhythm]". Back in London, Björk contacted "old standby" Talvin Singh to record additional percussion parts for it. Fellow former Sugarcubes member Einar Örn Benediktsson was also contacted to play the trumpet on "Enjoy". English sessionist Gary Barnacle was enlisted to play the saxophone. Brazilian composer Eumir Deodato participated on the album at Björk's request. She contacted him after hearing his arrangements of a Milton Nascimento song called "Travessia". Deodato's presence as composer and conductor "immediately bolstered" the songs "Hyperballad", "You've Been Flirting Again" and "Isobel". This addition of strings, brass and percussion elements gave Post the balance Björk felt her original recordings had lacked. "It's Oh So Quiet" was the last track to be recorded. By the time the album was finished in April 1995, the list of co-producers included Björk, Hooper, Bernstein, Massey, and Tricky. Björk has said: "The people I collaborated with were all people I was hanging out with in clubs in London. I had known them all for a while before we ended up working together." Björk's website described Post as "a bit of a bolder side of [Björk], who now had ventured all the way from Iceland to England, and was
```

### Album 275, chunk 5

```text
exploring the faster pace and big city life that this new country brought. This album became influenced of that and became more adventurous and club-friendly as a contrast to the shy first album, Debut." While IDM and trip hop influences were present on Debut, Post is characterised by Björk's fuller incorporation of these genres. The balance between synthetic and organic elements in Post —generated through the combination of electronic and "real" instruments—is a recurring characteristic of Björk's output. Simon Reynolds wrote in 2011 that "Post tapped into the vortex of multicultural energy that was mid-90s London where she had relocated, and where strange hybrids such as jungle and trip-hop were bubbling". Post has been described as art pop, experimental pop, and avant-pop. With its eclectic nature, Post touches on various musical styles. When asked if this variety of genres was intentional, Björk replied: "Yes, I'm very aware of that. I've got very many sides to me." Björk described Post as "musically promiscuous" and "spastic". In 1996, when asked about the album's musical influences, she stated: "I'm influenced by everything. By books, by the weather, by the water, by my shoes, if they're comfortable or not. Everything." The album opens with "Army of Me", an aggressive song with industrial rock, and trip hop influences. It incorporates a looped drum sample of Led Zeppelin's "When the Levee Breaks". Dedicated to Björk's younger brother, the song's lyrics are, according to Björk herself, "about telling someone who is full of self-pity and doesn't have
```

### Album 275, chunk 6

```text
anything together to get a life and stand up"; as she sings: "And if you complain once more/You'll meet an army of me!" "Hyperballad", is a track that incorporates electronic and orchestral styles, with a sound NME described as being "altered from gentle folktronica to drum and bass-tinted acid house". Its lyrics are about Björk pondering her own suicide, as she throws objects off a cliff as a form of Exorcism before returning to her partner. The track is followed by "The Modern Things", a song that, in a magical realist tone, "playfully posits the theory that technology has always existed, waiting in mountains for humans to catch up". Interview described it in 1995 as a "spooky tune", noting "the odd scratchings at the end" of the track. The big band track "It's Oh So Quiet" covers a German composition made famous by Betty Hutton. It has been described as "a palate-cleanser during the course of the record". Björk included the song "just to make it absolutely certain… that every song would be a shock". The following track, "Enjoy", a song concerning the links between sex and fear, has been considered "decidedly trippy", and "Post's most abrasive track". NME described it in its 1995 review as, "a dark and deranged techno thing". Over military drums and "squalls of noise", Björk sings about "her hedonistic tendencies". The orchestral interlude "You've Been Flirting Again", like the previous track "Enjoy", features "mysterious or open-ended lyrics". They are an attempt to describe the ambiguous
```

### Album 275, chunk 7

```text
nature of flirting. "Isobel" is a string-laden, orchestral trip hop song, Craig McLean of The Face called the track "Broadway on breakbeats". Conceived by Björk as "part autobiography part storytelling", its lyrics concern Isobel, a woman magically born in a forest who finds people in the city "a bit too clever for her", eventually retreating back to nature and sending them a message of instinct through trained moths. "Possibly Maybe" is an ambient dub track that fuses trip-hop and chill-out music and has a slide guitar in the background. Its lyrics document the various stages of Björk's failed relationship with Stéphane Sednaoui. With the track, Marius de Vries (keyboards/programming) "create[d] a vinyl-crackling ambience, full of glissando strings and leaden, muted bass. "I Miss You" was described in 1997 as an "amalgam of styles, with electronic drums melding into African bongos mixed with jazzy horn playing". A house music number, its "horn-infused Afro-Cuban strains [...] reflect the romantic whimsy of [its] lyrics". Björk wrote "Cover Me", one of the quieter moments on the album, to her co-producer Nellee Hooper after he agreed to participate in the making of Post. She has said: "I guess I was trying to make fun of myself, how dangerous I manage sometimes to make album making. And trying to lure him into it. But it is also a admiration thing from me to him". The album ends with the experimental "Headphones", an ambient track. Featuring "just-for-headphones studio tricks", it has been described as "a chiming, somnolent
```

### Album 275, chunk 8

```text
dip into Björk's heavy-lidded pre-dream state". Its lyrics were written as a thank you to Graham Massey, who would make compilation cassettes for Björk. She also stated: "But, of course, it is also a love letter to sound. The sound of sound. Resonances, frequencies, silences and such... a music-worship thing". Björk said the title Post refers to the fact that all the songs were written after her move to England, in contrast to Debut, the songs of which were written while she was still living in Iceland. In a 1996 interview, Björk said: "I always knew it would be two albums and that's why I called them Debut and Post. Before and after." The title also has the meaning of "mail", inspired by Björk's desire to communicate with friends and family in Iceland. Me Company designed the album artwork, while Martin Gardiner modeled the lotus flower in the booklet and packaging. The album depicts Björk in Piccadilly Circus, London, her pale skin and dark hair contrasting with the colours of the Japanese-inspired signs behind her. The photograph was taken on 1 April 1995 by Stéphane Sednaoui. The designer Paul White of Me Company, who had collaborated with Björk since her time with the Sugarcubes, "surrounded her with giant postcards to represent communication with friends and family". Björk said "my musical heart was scattered at the time and I wanted the [cover] to show that". The jacket Björk wears was inspired by Royal Mail airmail envelopes, referencing the album title. It
```

### Album 275, chunk 9

```text
was specially crafted from Tyvek envelope paper by the designer Hussein Chalayan. The jacket is displayed under glass at Hard Rock Reykjavík, and was part of the 2015 Björk exhibition in the Museum of Modern Art, New York City. Vice identified the airmail jacket as one of the "ultimate fashion moments" of Björk's career. A photograph of Björk surrounded by silver balls was planned as the cover, but it was scrapped in favour of something "more poppy". The photo later appeared in a 1995 article for The Face. Post was released on 12 June 1995, as a 12" record, CD, and compact cassette. It was issued on One Little Indian Records in the United Kingdom and Elektra Records in the United States and Canada; Polydor Records issued Post in Australia and Japan, also releasing the European edition of the album. In September 1995, Björk and poet Sjón released Post, a paperback book meant to be a "pictorial and verbal record of the making of that album". It contained interviews with Björk and also focused on the European leg of the tour. The Post tour was her first proper North American tour as a solo artist, with Aphex Twin as her opening act. While in the United States, she also appeared on Late Night with David Letterman; this tour "helped maintain Post's momentum and keep Björk in the public eye", since airings of "Army of Me" and "Isobel" had been relegated primarily to after-hours alternative music shows in MTV. In the
```

### Album 275, chunk 10

```text
United Kingdom, Björk also performed on Top of the Pops on several occasions. In 1996, Björk took part in Arnold Schoenberg's Pierrot lunaire, conducted by Kent Nagano and the Opera orchestra of Lyon. In addition, Björk also appeared in several music magazines. In November 1996, Björk released the "often-delayed" remix project Telegram, which contained reworkings of several songs from Post, with her voice re-recorded. Telegram has been described as "effectively a completely new album". Author Mark Pytlik writes, "Promises of a Post remix album had been circulating since the release of "Army of Me" in April 1995. To compensate, Björk announced the release of a string of 12″ remixes beginning in June, limited to only 1,000 copies each. Producers and musicians featured on Telegram include: Dillinja, Eumir Deodato, LFO, and Graham Massey, among others; Björk only remixed "You've Been Flirting Again" herself. The album also contains a new composition, "My Spine", a collaboration with British percussionist Evelyn Glennie. Telegram spent five weeks on the US Billboard 200 chart, peaking at number 66. In the UK, it peaked at number 59, spending two weeks on the albums chart. In 2005, the UNICEF charity record Army of Me: Remixes and Covers was released; it is a collection of seventeen eclectic remixes of "Army of Me". All profits went directly to the charity, to assist the victims of the 2004 Indian Ocean earthquake and tsunami. Live at Shepherds Bush Empire was released as a VHS in November 1998, containing the last performance of
```

### Album 275, chunk 11

```text
the Post tour, which took place at Shepherd's Bush Empire in February 1997. Post Live, a live album consisting of songs recorded during the Post tour, was included in the 2003 box set Live Box. The 2002 box set Family Tree includes demos and alternate versions of various tracks off the album. Post has been reissued several times, adapting to different formats such as colored records, 180g vinyl, and DualDisc. A remastered version of the album in surround sound was included in the box set Surrounded, which was released in 2006 on Elektra Records. In 2012, Universal Japan issued a limited edition of Debut and Post together as one compilation . All of Post's music videos were included on the 1998 video release Volumen, and its 2002 reissue Volumen Plus. They also appear on Greatest Hits – Volumen 1993–2003, a release that includes the videos featured on Volumen and Volumen Plus. They are also featured on video compilations of its directors, including The Work of Director Michel Gondry and The Work of Director Spike Jonze, all of them from 2003. "Army of Me" was released as the lead single from Post on 24 April 1995, shortly after the album's production concluded. It was released in the United Kingdom as two different CD releases, with "Cover Me", "You've Been Flirting Again", "Sweet Intuition", and various remixes as its B-sides. A commercial success, it peaked atop the Íslenski Listinn Topp 40, as well as at numbers five and ten in Finland and
```

### Album 275, chunk 12

```text
the United Kingdom, respectively. In the United States, it peaked at number 21 on the Alternative Airplay chart. Michel Gondry directed the video for "Army of Me", which takes place in a cyberpunk environment. In the video, Björk is seen driving a massive truck, which has been described as "alternately [looking] like an overgrown SUV and a science fiction tank" as she quests to rescue her loved one from an art museum. "Isobel" was released as the second single on 14 August, with B-sides "Charlene", "I Go Humble", "Venus as a Boy", and several remixes. Although the record company was against the idea of releasing "Isobel", Björk insisted because she "felt intuitively that this was the right choice". However, "Isobel" did not replicate the success of "Army of Me", peaking at number two in Iceland and number 23 in the UK. The music video for "Isobel", directed by Gondry, represents the story of the title character Björk envisioned with Sjón. It tells the story of "a wild child discovering urban culture through installations of toy fighter planes", over lush superimposed imagery. Like in the lyrics, where Björk takes the role of narrator and protagonist, she plays two different parts in the music video: Björk is seen as the Isobel who "weaves and composes this world and this story on her organ", and as the Isobel who inhabits this primal world. "It's Oh So Quiet" was released as the third single on 13 November. Its B-sides included "You've Been Flirting Again",
```

### Album 275, chunk 13

```text
"Hyperballad", "Sweet Sweet Intuition" (a rework of "Sweet Intuition"), and "My Spine". The music video for "It's Oh So Quiet" became one of the most played clips on MTV, and the song became Björk's most successful single, peaking at number one in Iceland and within the top ten in Australia, Finland, Ireland, Scotland and the UK, while peaking at number nine on the US Billboard Hot 100's extension Bubbling Under Hot 100 chart. The single was certified gold by the British Phonographic Industry (BPI) for shipments of 400,000 units in the UK. Spike Jonze directed the music video for "It's Oh So Quiet", a homage to Hollywood's Technicolor musicals that drew inspiration from Busby Berkeley and Jacques Demy's The Umbrellas of Cherbourg. Like Demy, Jonze "mines the magical from the mundane," as he transforms a drab auto shop into the location where Björk dances and sings with a full dance company, an attempt to reflect the "exuberance" of her vocal performance. "Hyperballad" was released as the fourth single on 12 February 1996. The single—consisting of two separate CDs—also included remixes of the song, "Isobel" and "Cover Me". Some regions also included a double A-side single with the song "Enjoy", although it only received a number of promo remixes. It peaked at number eight on the UK Singles Chart and atop the US Dance Club Songs. The music video for "Hyperballad", also directed by Gondry, has been described as "a techno-dream visual story full of flashing lights, buzzing static, and holograms."
```

### Album 275, chunk 14

```text
It shows Björk as "a character running through a landscape that simulates that of a computer game, only to throw herself off a cliff." The clip is an attempt to reflect the song's story, so Gondry depicted Björk lying down as a dead body, with a holographic image of her singing superimposed on her. "Possibly Maybe" was released as the fifth single on 28 October via several 12-inch records and three different CD releases. A limited-edition 12-inch double A-side with remixes of "Possibly Maybe" and "Enjoy" (by Mark Bell and Dom T., respectively) was also released. "Possibly Maybe" peaked at number 13 on the UK Singles Chart. Sednaoui directed the music video for "Possibly Maybe", despite the song being about his failed relationship with Björk. Björk and Sednaoui had previously worked together in the music video for "Big Time Sensuality". In the clip, she appears "as a goddess, floating out from a numinous light-streaked background." Sednaoui is known for having a particularly filmic technique for each of his clips; in "Possibly Maybe", the use of blacklighting "makes Björk glow sensuously and perversely". It was conceived in a theatrical way: nearly all of the scenes were filmed in the same space, which is transformed with changes in the mise-en-scène. The style of "Possibly Maybe"'s scenery and Björk's wardrobe reference East Asian imagery, and a Japanese traditional doll is featured as Björk's only accompaniment; as a silent witness, it is the object on which the protagonist casts reflections on her own identity.
```

### Album 275, chunk 15

```text
Regarding the video, Sednaoui said: "Her song and my video were a way of saying things to each other that we couldn't say otherwise." "I Miss You" was released as the sixth and final single on 17 February 1997. Although it became Björk's third US Dance Club Songs number-one single, it was the least successful single from Post in Europe, as it peaked only at number 36 on the UK Singles Chart. The animation of its music video was produced by John Kricfalusi and directed by Erik Weiss. It was promptly censored on MTV because of its nudity and violence towards the end. Upon its release, Post received universal acclaim from music critics. Lorraine Ali of Rolling Stone praised the album for differentiating from the alternative rock offerings of the early 1990s, and for successfully merging disparate styles. She concluded: "When Post comes to an end, it feels like getting back from a good vacation: the last thing you want to do is re-enter the real world". Writing for Entertainment Weekly, Jim Farber stated that despite Post's "bizarre" combination of diverse genres, the conviction of Björk's delivery and assuring hooks "[made] her most surreal passages as relatable as moon-June standards". He felt that Björk "[reinvented] that tradition, constructing standards for the cyber age". Joy Press, who reviewed the album for The New York Times, praised the album for not being a "play-safe sequel" to Debut, pointing out that Björk, "[had] followed her most wonderfully wayward impulses". Los Angeles Times critic
```

### Album 275, chunk 16

```text
Richard Cromelin felt that Post was "an often heady mix of trendiness and nostalgia" that was capable of transcending Björk's self-consciousness. Greg Kot of the Chicago Tribune found the album's backing tracks to be "even more varied and unusual" than on Debut, describing Björk as "an extra-terrestrial voice rummaging around in a sonic toybox". Spin's Barry Walters felt the album was an improvement over its predecessor, stating its songs were "stronger, more developed, and less reliant on Björk's wide-eyed delivery". He concluded that: "After years of (no) alternative fascist grunge domination, it's heartening that Björk and producer-co-songwriter Nellee Hooper stayed true to themselves and created another highly personal album that has a chance of interrupting the airwave flow of whiny rockers with little imagination". Writing for MTV Online, Lou Stathis wrote that, "[it's mostly] Björk's wacky, mind-altered perspective that makes Post modern pop music at once both baffling and engaging". He believed that the album was a rewarding experience for both the casual consumer, as well as the serious listener, also pointing out that, "it not only sounds good while you're listening to it, but it leaves you feeling good when it's over, too". Robert Christgau, reviewing the album for The Village Voice, was more critical. He found that the album's "eccentric instrumentation" and "electronic timbres" failed to compensate for its lack of "groove" and was unmoved by Björk's lyrics, which he said "might hit home harder if she'd grown up speaking the English she'll die singing, but probably wouldn't".
```

### Album 275, chunk 17

```text
Post reached the top ten of several countries, including Australia, Belgium, Canada, Denmark, the Netherlands, Finland, France, Germany, Ireland, New Zealand, Norway, Portugal, Sweden, Switzerland, and the United Kingdom. Post also peaked at number two on the European Top 100 Albums chart. The album peaked at number 32 in the Billboard 200, almost 30 places higher than the peak position of its predecessor Debut. It also received an enthusiastic reception from college radios. Post also reached top 40 in Hungary and Japan. The album was certified platinum in Australia, Canada, the United Kingdom, the United States, and Europe; and gold in Sweden and New Zealand. In 2007, The Washington Post reported that Post had sold 810,000 units in the United States according to Nielsen SoundScan; it had sold 36,000 additional copies by 2015. The music video for "Army of Me" was removed from MTV's playlist before it aired because its ending depicted Björk bombing an art museum; the Oklahoma City bombing happened at this time. Author Mark Pytlik wrote that this "foreshadowed a string of unlucky events that would further hinder Post's unveiling". Robin Rimbaud filed a lawsuit demanding a co-songwriter credit for "Possibly Maybe", claiming that the song sampled his work. After Rimbaud's label New Electronica refused a sample clearance compensation of £1,000 from One Little Indian founder Derek Birkett, Björk and Birkett resolved to destroy over 100,000 copies of the album to create a new version without the sample. However, at the request of Rimbaud, New Electronica gave
```

### Album 275, chunk 18

```text
Björk permission to use the sample. Musician Simon Fisher sued Hooper and Björk over writing credits in Debut (1993), but these charges were cleared by judge Robin Jacob. According to Pytlik, these events resulted in "the strangest promotional tour anyone could have ever envisioned: in the week since Post had been released, Björk had seen her album deleted, her video banned, and two separate lawsuits brought against her". One Little Indian were also better prepared to promote the album, scheduling a string of European and American tour dates from the beginning of July into late August. During the Post era, the extensive media attention and a world tour of 105 dates began to affect Björk. She repeatedly complained about the intrusiveness of tabloids and reporters. On tour in February 1996, Björk arrived at Bangkok International Airport with her son Sindri after a long flight. While the pair walked through the arrival terminals, reporter Julie Kaufman approached them and said, "Welcome to Bangkok!" Björk charged at Kaufman and wrestled her to the ground. It was later reported Kaufman had been bothering Björk and Sindri for days prior. The incident was reported around the world. On 12 September, an obsessed American fan, Ricardo López, sent a letter bomb rigged with sulfuric acid to Björk's residence in London, returned home and filmed his suicide. Police contacted Scotland Yard, who intercepted the package without incident. To record in privacy away from the unwanted interest of the press, Björk's tour drummer Trevor Morais offered her
```

### Album 275, chunk 19

```text
his studio in Málaga, Spain, to record her next album, Homogenic. Nick Coleman of The Independent considered Post to be an important release of the art pop genre, Retrospectively, Slant Magazine's Eric Henderson argued that Post "will likely always remain the Björk album that most successfully sustains her winning balance of experimental whimsy and solid pop magic", while Heather Phares of AllMusic wrote that the record was "not simply Debut redux" and concluded: "The work of a constantly changing artist, Post proves that as Björk moves toward more ambitious, complex music, she always surpasses herself". Celebrating the album's 20th anniversary, the British magazine NME described it as, "a masterful matching of hard, up-to-the-minute beats with complex, personal lyrics about the rush and rage of being a modern urban woman". The album's influence has been identified as being increasingly palpable on the contemporary music landscape, and later reviews of the album also make note of the timeless aspect of the music. Writing for The Daily Review, James Rose wrote in 2015: "Post is where mainstream music could have gone. While modern chart music hasn't gone there entirely[,] she undoubtedly helped broaden the playing field. [The album] stands today as a body of work that still informs the more marginal artistic fringes of modern music and reminds us how narrow and staid our world would be without outliers like Björk. Also in 2015, Andrew Shaw of Nerdist felt that Post "chose to ignore expectation, market restrictions, and contemporary trends", and that Björk
```

### Album 275, chunk 20

```text
"pushed her vocal performances into new places, where no other vocalists could dare to sing". He compared the album's impact on audiences to that of Jimi Hendrix's 1967 album, Are You Experienced, writing it "set the benchmark for what was possible when you take tradition and set it on fire". Raymond Ang of The Wall Street Journal considered Post to be "Björk's last stab at the pop game… she would dig deeper into her increasingly avant-garde interests and, in the years to come, thrill and challenge her audience". David Longstreth of Dirty Projectors is an admirer of the record, stating he was influenced by Björk's deconstruction of classic melodies. American singer-songwriter Amy Lee has said Post is "one of the biggest records in [her] life". DJ Shadow sampled "Possibly Maybe" in "Mutual Slump", a track off his 1996 album, Endtroducing...... The Vitamin String Quartet—known for its series of tribute albums to rock and pop acts—covered "Army of Me" and "You've Been Flirting Again" in the 2001 album, Ice: The String Tribute to Björk. In 2008, Stereogum released a compilation of cover versions in homage to the album, titled Enjoyed: A Tribute to Björk's Post. It features: Dirty Projectors, Liars, Xiu Xiu, High Places and Atlas Sound, among other artists. Much of Post's six music videos have gone on to become classics—most notably "It's Oh So Quiet" and "Army of Me". At the time of its release, music videos were beginning to be used as an art form, and Björk's visual
```

### Album 275, chunk 21

```text
output during this period—and her career in general—have become a clear example of the medium's artistic legitimation. Spanish writer Estíbaliz Pérez Asperilla has identified recurring motifs and themes through Björk's videography; these include nature and a magnified depiction of Björk. Surrealism and technology have also been identified as recurring features in Björk's visual output of this period. David Ehrlich of Time Out considered her "one of the first artists to meaningfully explore the aesthetic and semiotic value of CG and its relationship to the [videos]." Writing for Paste, Alexa Carrasco felt, "Björk has created some of the most beautiful and weird videos to ever play on MTV." The popularity of the music video for "It's Oh So Quiet" made the song one of Björk's most ubiquitous tracks, and was considered her first breakthrough on MTV. The music videos—and the pink boots Björk wears in "Hyperballad" (the work of Belgian designer Walter Van Beirendonck)—were displayed in the Museum of Modern Art, New York City, as part of the 2015 Björk exhibition. They were also featured in the 2016 exhibition, Björk Digital, which premiered at Carriageworks as part of the Vivid Sydney festival. In 2008, when asked how she felt about the album in retrospect, Björk reflected: "I was kinda surprised how the odd spastic thing of the album had actually aged well."
```
