# Embedding text relevance, batch 10 of 12 (albums 226–250 of 300)

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

This batch: **25 albums, 54 chunks**.

## Album 226: A Night on the Town — Rod Stewart

- **album_id:** `8bc276c4-27b1-4d68-9b9f-3376067fd2a4`
- **Tags (identification only):** rock, soft rock, adult contemporary, hard rock, pop, pop rock, album rock, classic rock
- **Chunks:** 1 (266 words)

### Album 226, chunk 1

```text
A Night on the Town is Rod Stewart's seventh album, released on June 18th, 1976. The cover art is based on Pierre-Auguste Renoir's painting Bal du moulin de la Galette, with Stewart inserted in the centre in period costume. On 30 June 2009, Rhino reissued the album as a two-disc CD with bonus tracks. A Night on the Town was Stewart's last UK number-one studio album until Time in 2013. The album is regarded as one of Stewart's finest. "The Killing of Georgie" is one of Stewart's most hard-hitting sets of lyrics, a melancholic tale of a gay friend who is cast out by his family and becomes a sensation in the New York nightlife, only to be murdered by a New Jersey gang during an attempted robbery. Controversial "Tonight's the Night" was a No. 1 hit but was banned by some radio stations due to the very obvious lyrics about sex and loss of virginity. A cover of Cat Stevens' "The First Cut Is the Deepest" was also a success and has since become one of Stewart's signature songs. Rod Stewart – vocals Donald Dunn, Bob Glaub, David Hood, Lee Sklar, Willie Weeks – bass guitar Pete Carr, Steve Cropper, Jesse Ed Davis, David Lindley, Billy Peek, Fred Tackett, Joe Walsh – guitar Barry Beckett, David Foster, John Barlow Jarvis, J. Smith – keyboards Roger Hawkins, Al Jackson Jr., Andy Newmark, Rick Shlosser – drums Joe Lala, Tommy Vig – percussion Jimmy Horowitz, Mel Lewis, Arif Mardin – string arrangements Tower of Power horn section – French horn Plas Johnson, Jerry Jumonville – tenor saxophone
```

## Album 227: Places Like This — Architecture in Helsinki

- **album_id:** `068100aa-bc79-4217-877c-8c4157810ad1`
- **Tags (identification only):** indie pop, indie rock, abstract pop, pop, rock, alternative, aussie, australian
- **Chunks:** 1 (275 words)

### Album 227, chunk 1

```text
Places Like This is the third studio album by Architecture in Helsinki, which was released in Australia on 27 July 2007 at the launch of their Australian tour. It was also released in Japan on 18 July, Europe on 8 August, and in the United States on 21 August. It debuted at No. 31 on the ARIA Albums Chart, and dropped to No. 49 in its second week. At the J Awards of 2007, the album was nominated for Australian Album of the Year. Australian group, Architecture in Helsinki issued their third studio album, Places Like This on 28 July 2007 on Polyvinyl Record Co. In September of the previous year, Laura Pearson of Pitchfork Media reported that the group were working on tracks with Cameron Bird (lead singer) in Brooklyn, United States while the other members were in Melbourne. It was recorded at Dave Sitek's (from TV on the Radio) studio in Williamsburg, Brooklyn and in Sydney's Big Jesus Burger Studios between October 2006 and January 2007. It was engineered and mixed by Chris Coady, who has previously worked with TV on the Radio, Yeah Yeah Yeahs and Grizzly Bear. The first single from the album, "Heart It Races", was released ahead of the album in May and peaked into the top 50 on the ARIA Singles Chart. Places Like This reached the top 30 on the related albums chart. In the US, the album reached the top 10 on two of Billboard magazine's component charts: Top Electronic Albums and Heatseekers Albums in September. According to review aggregator Metacritic, Places Like This has a score of 66 out of 100, indicating "generally favorable reviews".
```

## Album 228: Get Lost — The Magnetic Fields

- **album_id:** `494e61bc-0052-4160-bdb4-4c11ad3f3cc5`
- **Tags (identification only):** electronic, indie pop, synth pop, folk, indie, lo fi, pop
- **Chunks:** 1 (172 words)

### Album 228, chunk 1

```text
Get Lost is the fifth studio album by American indie pop band the Magnetic Fields, released on October 24, 1995. The Divine Comedy have recorded covers of three songs from this album. "Love Is Lighter Than Air" appears as the B-side of their 1996 single "Something for the Weekend". "Famous" appears as the B-side of their 1999 single "National Express". Their version of "With Whom to Dance" appears as the B-side of their 1999 single "The Pop Singer's Fear of the Pollen Count". Tracey Thorn has recorded covers of several Magnetic Fields songs. "Smoke and Mirrors" from Get Lost appears as the B-side of her 2007 single "Raise the Roof", together with her version of "The Book of Love" from 69 Love Songs. Advance Base recorded a version of "You and Me and the Moon" for the 2018 album Animal Companionship. Stephin Merritt – vocals, instrumentation Claudia Gonson – drums, vocals, ukulele Sam Davol – cello, flute John Woo – guitar, banjo Julie Cooper – bass guitar Natalie Lithwick – French vocals
```

## Album 229: True Brew — Millencolin

- **album_id:** `05aa0f62-768c-4c99-a3f1-74df9bfc0477`
- **Tags (identification only):** pop punk, punk, punk rock, rock, skate punk, sweden, swedish
- **Chunks:** 1 (110 words)

### Album 229, chunk 1

```text
True Brew is the eighth studio album by Swedish punk rock band Millencolin. It was first released on 22 April 2015. Stylistically, True Brew returns to the faster punk rock sound of Millencolin's '90s releases and marks a departure from the more alternative rock-driven sound that dominated their albums since Pennybridge Pioneers. Unlike past releases, the album is more political in tone, evident in songs such as "Sense & Sensibility", which condemns the rise of right-wing populist parties in many countries of Europe. Nikola Šarčević – lead vocals, bass Erik Ohlsson – guitar, keyboards, album artwork Mathias Färm – guitar, percussion, keyboards, assistant engineer, editing Fredrik Larzon – drums, percussion
```

## Album 230: Days of the New — Days of the New

- **album_id:** `816668cc-3bc8-48b4-8921-e93094d04ae6`
- **Tags (identification only):** alternative rock, alternative pop/rock, post grunge, rock, acoustic rock, alternative metal, alternative/indie rock, country rock
- **Chunks:** 3 (631 words)

### Album 230, chunk 1

```text
Days of the New (also known as the Orange or Yellow album) is the debut studio album by American alternative rock band Days of the New, and the first of their three self-titled albums. The album was released on June 3, 1997, through Outpost Records. In 2025, Lauryn Schaffner of Loudwire named the album the best post-grunge release of 1997. That same year, she said it was the band's best album. The band recorded its debut album in late October and early November 1996 at Woodland Studios in Nashville, Tennessee. Drummer Matt Taul was called away from the studio during the sessions for the birth of his daughter, so session drummer Adam Turgeon filled in on some tracks. Travis Meeks named Dead Can Dance as an inspiration while working on the album. The last song on the album, "Cling," is a home demo that Meeks recorded on a four-track machine. The entire album is acoustic, with emphasis on guitar, and features dark melodies such as "Face of the Earth" and "Freak" as well as more up-tempo songs like "The Down Town" and "Where I Stand." Days of the New was a success, selling 1.5 million copies worldwide. Three songs from the album were hits: "Touch, Peel and Stand," "The Down Town," and "Shelf in the Room." "Touch, Peel and Stand" was number one on Billboard's Rock Chart for 16 weeks; "The Down Town" and "Shelf in the Room" were each top 40 hits. Music videos produced for the three singles
```

### Album 230, chunk 2

```text
also found rotation. Shortly after releasing the album, the band went on tour with Metallica and Jerry Cantrell in 1998. Internal problems became publicly evident, however, and soon after concluding the tour, the band split up. Todd Whitener, Matt Taul and Jesse Vest would go on to form Tantric while Meeks formed a new band under the Days of the New name. Reviewing for The Village Voice in December 1997, Robert Christgau was unenthusiastic about the album: "As marketing, pure genius. Looks like alt-country, no electric guitars even, yet is actually America's answer to Silverchair. And hey, it's sincere—17-year-old heartland frontman Travis Meeks really is depressed, really has immersed in Soundgarden, really does think it's deep to hook your single to the all-purpose trope 'abuse.' This is why grownups need Hanson. It's also why they need Radish." Stephen Thomas Earliwine was more complimentary, giving the album three out of five stars. He said Meeks's vocals and lyrics were occasionally disappointing, but the album's stronger moments "prove that teenagers can rock as hard, and with as much purpose, as adults." Mike Peake of Kerrang!, who gave the album four stars out of five, stated that "the sheer songwriting class, production and the obvious musical savvy of the band makes [Days of the New] one of the most appealing and powerful debut albums for some time." "Independent Slaves" - Appears on the Touch, Peel and Stand single and on the Crow: Salvation soundtrack "Got to Be You" - Appears on the Touch,
```

### Album 230, chunk 3

```text
Peel and Stand single and on 2 Guitars, Bass & Drums: Songs For Survival "Special Guide" - Appears on the Shelf In The Room single "The Character/The Threat" - Appears on the Days of the New: Live VHS "Break You" - Played during the Fall 1997 tour "I Tried" Unreleased song On December 1, 1998, Outpost released Days of the New: Live, a VHS featuring concert footage and two music videos. The video includes numerous songs that would be released on future Days of the New albums. Fighting with Clay Freak Best in Life Shelf in the Room The Character/The Threat Face of the Earth Special Guide How Do You Know You? Touch, Peel and Stand Bring Yourself The Down Town Touch, Peel and Stand (video) Shelf in the Room (video)
```

## Album 231: Dariacore — leroy

- **album_id:** `2ec235b6-f0ab-4b6a-a832-789ac2dc2843`
- **Tags (identification only):** dariacore, digicore, edm, hyperpop, mashcore, plunderphonics, pop
- **Chunks:** 3 (561 words)

### Album 231, chunk 1

```text
Dariacore is the debut studio album by Leroy, a side project of the American musician Jane Remover. It was self-released on May 14, 2021. Described as a mashup album, Remover was inspired by the musician Vektroid and SoundClown music. Its name is taken from the Daria TV series, as the series also served for the visual aesthetic of the album. Dariacore was responsible for the creation of a genre of the same name, which inspired a wave of SoundCloud artists, and was considered one of the best albums of 2021 by The Fader. It received two sequels. Dariacore was a result of Remover "messing around" in the digital audio workstation FL Studio after being inspired by the production livestreams of the electronic artist Vektroid. They were also inspired by Vektroid's "glitchy" track "Sick & Panic" and SoundClown music. Remover began uploading untitled songs under the pseudonym Leroy, using screenshots taken from the television show Daria as covers. Dariacore is a mashup album. Jordan Darville of The Fader wrote, "Thanks to its liberal use of frenzied breakbeats, Dariacore could be described as a grandson of drum and bass, with a heart that pumps Frosted Flakes milk." In a review for Sputnikmusic, staff member Kirk Bowman deemed the album "equal parts Girl Talk, brostep, and Vine compilation". He thought it drew inspiration from many sources, like hyperpop, drum and bass, memes, and especially pop music. The album was self-released on May 14, 2021. In his 4.3/5 review for Sputnikmusic, Bowman said that
```

### Album 231, chunk 2

```text
"Leroy [...] has proven their worth several times this year alone, but for my money, this is their high point". He said that "this is the sound of someone who adores music [...] and has enormous talent pairing that with a sense of humor, a short attention span, and, above all, brilliant musicality". Bowman was positive of the album's flow and, even though it contained "crazy ideas", "to one extent or another, all these ideas somehow work. This is the epitome of taking risks and having it pay off." He declared that "Go White Enby Go" could be his favorite song of the year. Dariacore was listed as the 40th best album of 2021 by The Fader's staff. Darville wrote that "perhaps every generation needs a musical Frankenstein, and if that's the case, I'm glad Gen Z has Leroy". Remover is credited with creating the dariacore microgenre—named after the album itself—which inspired a wave of SoundCloud artists. They referred to the microgenre's name as "a joke that's been going on for too long." In a review of their album Frailty released under Jane Remover, Mano Sundaresan wrote to Pitchfork that "[Remover's] defining moment of the year may be inventing a glorious microgenre of shitposty Jersey club mashups called dariacore". With the popularity of the album, they stated: "I guess people just caught on and wanted to join me and that's how it came to be. I like how much fun everyone's having with it. I want to keep it separate
```

### Album 231, chunk 3

```text
from [Jane Remover], but I also don't really have a direction that I want to take Leroy in. I just do whatever I want on there and all the songs just happened to sound the same." Remover released two sequels: Dariacore 2: Enter Here, Hell to the Left (2021) and Dariacore 3... At Least I Think That's What It's Called? (2022).
```

## Album 232: Hey, Love — The New Rotary Connection

- **album_id:** `0af635c1-bf8a-4123-9717-236640b514a7`
- **Tags (identification only):** funk, jazz, psychedelic, soul, soul jazz, psychedelic soul, rare groove a to z, rhythm and blues
- **Chunks:** 1 (211 words)

### Album 232, chunk 1

```text
Hey, Love is a 1971 studio album by American psychedelic soul group Rotary Connection released by Cadet Records. Editors at AllMusic rated this album 4 out of 5 stars, with critic Andy Kellman writing that this is "one of Rotary Connection's best records" and recommends to listeners that this is as vital to the band's discography as their debut album, furthermore stating that "I Am the Black Gold of the Sun" "is the apex, the brightest moment in the group's discography". In The Rough Guide to the Best Music You've Never Heard, Nigel Williamson credits this track with resurrecting the band's career. In a review for retailers, Billboard called the group a "sweeping soul combo" and highlighted the vocals as well as Charles Stepney's work as particularly strong. In Psychedelia and Other Colours, Rob Chapman states that this album is stronger than predecessor Dinner Music and credits Stepney for being "at the top of his game". Pat Ferreri – guitar Henry Gibson – congas Kitty Haywood – alto and soprano vocals Dave Scott – tenor vocals Donny Simmons – percussion Sydney Simms – bass guitar Charles Stepney – piano, harpsichord, organ, electric piano, horn arrangement, vocal arrangement Minnie Riperton – soprano vocals Phil Upchurch – guitar Shirley Wahls – contralto vocals
```

## Album 233: Theology — Sinéad O’Connor

- **album_id:** `ea37a7fa-3c93-4074-be23-4f3d80974e17`
- **Tags (identification only):** rock, acoustic, alternative rock, ballad, blues, classical, experimental, pop
- **Chunks:** 1 (220 words)

### Album 233, chunk 1

```text
Theology is the eighth full-length album by Irish singer Sinéad O'Connor. It was released in 2007 on Rubyworks (and Koch Records in the US). The album consists of two discs, the acoustic "Dublin Sessions" and the full-band "London Sessions". The first single from Theology is "I Don't Know How to Love Him" (an Andrew Lloyd Webber and Tim Rice song from Jesus Christ Superstar). In the issue dated 14 July 2007, the album entered the US Billboard 200 chart at number 168. The album also debuted in the top 20 of Billboard's Independent Albums list at number 15. First-week sales of the album in the US amounted to 4,700 units, while the record also charted in Ireland, France and Italy. Sinéad O'Connor – vocals, guitar Steve Cooney, Hawi Gondwe, Ron Tom (Ron Tomlinson), Sam Cloth Shop – guitar Mark Gilmour, Andrew Smith – guitar, bass guitar Robbie Shakespeare – bass guitar Donald "Don-E" McLean – guitar, bass guitar, piano Toby Baker – piano Camilla – harp Julian Saxi, Neil Williams, Jonah O'Leary – violin Diana Tice, Natalie Azario – cello Richard Baylis – French horn Nathan Tice - flute Bev, Chris Brown, Val Staccato – backing vocals Tommy "Specs" White, Matthew Phillips – drums, percussion John Reynolds – drums and production assistance on "I Don't Know How To Love Him"
```

## Album 234: Bare Trees — Fleetwood Mac

- **album_id:** `32e551fc-8fb7-46e9-992e-7152d34a0afa`
- **Tags (identification only):** rock, blues rock, pop rock, classic rock, should be public domain, soft rock
- **Chunks:** 6 (1333 words)

### Album 234, chunk 1

```text
Bare Trees is the sixth studio album by British-American rock band Fleetwood Mac, released in March 1972. It was their last album to feature Danny Kirwan, who was fired during the album's supporting tour. The album peaked at number 70 on the US Billboard 200 chart dated 3 June 1972. In the wake of the band's later success with the Buckingham/Nicks line-up in the mid-1970s, Bare Trees returned to the US Billboard 200 chart at number 182 dated 6 September 1975. The album was certified platinum by the Recording Industry Association of America (RIAA) on 9 February 1988. Mick Fleetwood was particularly impressed with Kirwan's contributions to the album, saying that "Danny had the chops with layering techniques, and the ability to know what's right and wrong in the studio". "Child of Mine" alludes to Kirwan's biological father not having been part of his life (Kirwan was his stepfather's surname). "The Ghost" was later re-recorded by Bob Welch for His Fleetwood Mac Years and Beyond, Vol. 2 in 2006, but this version was only available on the digital edition. The flute noises on "The Ghost" were triggered from a mellotron played by Christine McVie. "Homeward Bound" alludes to Christine McVie's road weariness and desire "for a proper night's rest in her own bed", according to Fleetwood. "Sunny Side of Heaven" is an instrumental, which was later performed with Lindsey Buckingham on guitar for some shows in the mid-1970s. "Bare Trees" shares a theme with both the album's cover photography by
```

### Album 234, chunk 2

```text
John McVie and the closing poem "Thoughts On a Grey Day." "Sentimental Lady" was released as a single, and was later re-recorded by Welch (with Mick Fleetwood, Christine McVie, and Buckingham backing him) for his solo album French Kiss. Welch recorded the song again for His Fleetwood Mac Years & Beyond in 2003. "Danny's Chant" features the use of wah-wah guitars. The track is largely an instrumental, although it does feature rhythmic, wordless vocals from Kirwan. "Spare Me a Little of Your Love" became a staple of the band's live act through the mid 1970s, including tours with the Rumours era lineup. The song was also covered by Johnny Rivers on his studio album New Lovers and Old Friends in 1975. Jackie DeShannon recorded a version for her 1972 album Jackie although this did not make the final cut and was not released on her All the Love: The Lost Atlantic Recordings album. In his first memoir, Fleetwood identified "Spare Me a Little of Your Love" as one of his favourite songs of McVie's, saying that "the great thing about her songs is that she always finds such novel ways to say 'I love you'". The lyrics for "Dust" were taken from the first two verses of a poem of the same title, written by Rupert Brooke in 1910. Unlike W. H. Davies, who received a credit for the words to "Dragonfly", Brooke was not credited. The final track on the album, "Thoughts on a Grey Day", is not a
```

### Album 234, chunk 3

```text
Fleetwood Mac song but a monaural recorded poem written and read by an elderly woman, Mrs. Scarrott, who lived near the band's communal home, 'Benifold', in southern England. Bob Welch gave differing accounts on who recorded the poem. In a 1999 Q&A with The Penguin, he said that "the spoken thing Mick does about 'Trees so bare' was written, I think, by this sweet old lady that lived near Benifold ... Mick did an affectionate 'schtick' on her to close the album." In a different Q&A with The Penguin in 2003, Welch said that Mrs. Scarrott lived within walking distance of their communal home. According to Welch, Fleetwood suggested the idea of bringing a cassette tape recorder to her house so that she could recite one of her poems. Five of the ten tracks, comprising the majority of the music featured on the album, were written by Kirwan. "Trinity", another Kirwan song recorded at the sessions, was subsequently released in 1992 on the 25 Years – The Chain box set in stereo. The 2020 remastered edition of Bare Trees from the 1969 to 1974 CD box set features the track in an alternate mono mix, alongside the US single mix of "Sentimental Lady", and a live recording of "Homeward Bound". Once the album was completed, the master recordings were brought to New York but were summarily demagnetized and erased as they passed through an x-ray machine at the airport. The band then travelled to the Record Plant where they spent
```

### Album 234, chunk 4

```text
"a horrible and hectic few days" remixing the album. In their review of Bare Trees, Record World called the album a "worthwhile package" that improved on the band's "brand of rock and roll". Cashbox said that the album was another stunning example of tight rock and roll playing" and concluded that the album's final track "Thoughts on a Grey Day" would make listeners smile "even on an orange day.". Billboard said that Kirwan's vocals were "full of delightful little flourishes" and also thought that the rest of the band were "accomplished" players in their own right. The publication also labelled Kirwans's "Child of Mine", "Bare Trees", and "Danny's Chant" as "outstanding" tracks. In his review for New Musical Express, Tony Stewart wrote that the album "retained much of the initial Mac appeal", which he attributed to the rhythm section from the band's earliest albums remaining intact. He also highlighted the musicianship of the band and the prevalence of the guitar, saying that the instrument was used in a tasteful manner rather than a showcase for "instrumental ego trips." With the exception of "Dust", he was generally complimentary of Kirwan's compositions; he singled out "Sunny Side of Heaven" as "a beauty in itself" and thought that the song was reminiscent of The Shadows. He also praised McVie's songwriting on the album and wished that her keyboards were more present in the mix. In a retrospective review, AllMusic called Bare Trees "the "first consistently strong album Fleetwood Mac ever recorded". Bare Trees
```

### Album 234, chunk 5

```text
debuted at number 175 on US Billboard 200 chart dated 22 April 1972. The album reached its peak at number 70 on the chart dated 3 June 1972, after being on the chart for seven weeks. The album ultimately spent a total of 27 weeks on the chart. On 9 February 1988, the album was certified platinum by the Recording Industry Association of America (RIAA) for sales of over a million copies in the United States. Following the release of Bare Trees, Fleetwood Mac embarked on a tour to promote the album. In an interview on 5 August 1972 with Disc magazine, McVie said that the band planned to promote the album in Europe following their summer tour in North America. She also expressed her opinion that the band were "happier than we've ever been before." By the end of the summer, Kirwan had left the group. At the time of his departure, New Musical Express were told by the band's publicist that Kirwan "was happy to leave, because he wanted to do a solo album for some time." However, Fleetwood later stated that Kirwan was fired after his refusal to join the band on stage after a disagreement with Welch over guitar tunings. During the argument, Kirwan destroyed his Gibson Les Paul and several items in the dressing room. The band then performed the set without Kirwan, who observed their performance from offstage. Fleetwood mentioned that the band became more incensed after Kirwan offered critiques of the band's performance.
```

### Album 234, chunk 6

```text
When discussing the incident, Welch recalled that "the set seemed to drag on for ever. To do a whole set without Danny was tough, because all the band arrangements depended on him being there for a guitar part or a vocal part...I think we told the audience Danny was sick, which I guess he was in a way." Danny Kirwan – guitar, vocals Bob Welch – guitar, vocals Christine McVie – keyboards, vocals John McVie – bass guitar Mick Fleetwood – drums, percussion
```

## Album 235: Rat Saw God — Wednesday

- **album_id:** `90b2a531-4c85-4137-b2d0-c0698bb56b58`
- **Tags (identification only):** indie rock, alternative country, alt country, noise pop, noise rock, shoegaze, slacker rock
- **Chunks:** 4 (991 words)

### Album 235, chunk 1

```text
Rat Saw God is the fifth studio album by American rock band Wednesday, released by Dead Oceans on April 7, 2023. It was preceded by the singles "Bull Believer" and "Chosen to Deserve". The album received high praise from critics, praising it as "stunningly powerful" and "riveting". It was noted by critics for its depiction of life in the American South. It was the band's final album with bass guitarist Margo Schultz, who painted the album's artwork. She was replaced by Ethan Baechtold ahead of the album's tour. The album was named after the Veronica Mars episode "Rat Saw God". Wednesday released their cover album, Mowing the Leaves Instead of Piling 'Em Up, through Ordinal Records in March 2022. It received positive reviews from Pitchfork and Under the Radar. The album's sound ranged from country, to Americana, to alternative rock. The band recorded the album after getting an opportunity to record in a studio in Durham, North Carolina with Alli Rogers; the band's singer and guitarist Karly Hartzman said the band recorded a cover album because "Wednesday owes so much to [their] musical influences" and the members' favorite music "is a big part of what brought [them] together". Mark Moody from Under the Radar called it a "one-off placeholder until Wednesday's next full-length of original material comes out". Hartzman felt that blending influences of emo, shoegaze, and country made the record have an "original sound […] that hasn't been done [much before]". She was inspired by country musicians and bands
```

### Album 235, chunk 2

```text
such as Lucinda Williams, Tom T. Hall, Outlaw Country, Vic Chesnutt, and Drive-By Truckers. The album presents a Wall of Sound achieved by Xandy Chelmis on the lap steel guitar, the noisy slide sections, and the pedal steel guitar, as well as MJ Lenderman on the album's lead guitar sections. Hartzman stated that the positive reception toward their third album, Twin Plagues (2021), made her more confident in singing on Rat Saw God; she felt that the confidence can be heard in the album itself. Throughout the recording process, the band utilized overdubbing. In contrast to Twin Plagues, the band were unable to play the songs live before recording them. The band was affected by time constraints and limited time in the studio; Alan Miller said they were getting studio time "as a favor, because [the band was not] on a big label yet". In the studio, Hartzman typically wrote the lyrics and guitar passages, while the rest of the band work out their respective contributions. Hartzman expressed that the album sees the band heading into a heavier sound; she enjoyed the idea of showcasing a heavy song mixed with country aspects. Wednesday signed with Dead Oceans the last day they were in the studio recording the album. On September 8, 2022, the band announced that they left Orindal Records and signed to Dead Oceans, releasing the single "Bull Believer". On January 18, 2023, the band released the single "Chosen to Deserve" and announced their fifth album, Rat Saw God,
```

### Album 235, chunk 3

```text
which was released on April 7, 2023. The album cover art is a 6' x 6' oil painting made by former bassist Margo Schultz. Rat Saw God received universal acclaim from music critics. At Metacritic, which assigns a normalized rating out of 100 to reviews from professional publications, the album received an average score of 89, based on 16 reviews. Reviewing the album for AllMusic, Mark Deming concluded, "Some albums sound like the artists were trying with all their might to make an epic statement in words and music; Rat Saw God sounds like Wednesday had no such lofty aims, but their commitment to the people they write about and their instincts about crafting music to match make this a stunningly powerful work that may well turn out to be a masterpiece." In Beats per Minute, Tim Sentz claimed that the album is an example of, "a band operating at their highest most infectious potency, and the end result is riveting." Craig Howwieson at Clash described it as, "Finding magic in the mire - Rat Saw God is an emphatic, uplifting reminder of the privilege of being alive." Writing for DIY, Sam Thirwell stated that, "While some of the stylistic variation here can feel disjointed at times, there's plenty on offer to suggest a band on the rise, capable of rising even higher." In Exclaim, Dylan Barbabe claimed that, "Rat Saw God is wildly ambitious and easily lives up to the industry hype — Wednesday have succeeded once again in
```

### Album 235, chunk 4

```text
twisting nostalgia and existential dread into a braid of bruising, life-affirming rock music." At Paste, Samantha described Karly Hartzman's, "Lyrical precision is what makes the record shine, the fact that Hartzman can recall the exact video game, in this case, Mortal Kombat, that someone was playing when her nose started bleeding at a New Year's Eve party she didn't even want to be at." Sam Sodomsky of Pitchfork wrote, "Wednesday's noisy, rangy sound finds a home in the quiet, lonely corners of America. Their outstanding new album is why they're one of the best indie rock bands around." In Rolling Stone, Jon Dolan proclaimed that, "There's a Flannery O'Connor story collection worth of Southern fucked-up-ness going on here. But Wednesday are just as interested in sucking you in with a walloping guitar banger as they are in freaking you out with their snapshots from the ruralburban coming-of-age abyss. These songs are so catchy you almost don't notice the body count." Jeremy Winograd praised the album in the review for Slant: "All of the wobbling between tempos and styles might sound haphazard, but it's executed with precision. And Hartzman's snatches of Americana imagery—rain-rotted houses, parking lots, "piss-colored bright yellow Fanta"—ultimately cohere into an evocative portrait of the fringes of American life." Karly Hartzman – guitar, vocals MJ Lenderman – guitar, backing vocals Xandy Chelmis – lap steel Margo Schultz – bass, painting Alan Miller – drums Alex Farrar – production, mixing, engineering
```

## Album 236: What Went Down — Foals

- **album_id:** `e58f6793-aada-40e2-9f0f-5eb73d62431b`
- **Tags (identification only):** indie rock, rock, pop, alternative rock
- **Chunks:** 3 (558 words)

### Album 236, chunk 1

```text
What Went Down is the fourth studio album by British rock band Foals, released on 28 August 2015 via Transgressive Records in the United Kingdom. The album is produced by James Ford, known for his work with Simian Mobile Disco, the Last Shadow Puppets and Arctic Monkeys amongst others. Frontman Yannis Philippakis called it their loudest and heaviest record to date. What Went Down debuted at number 3 on the UK Albums Chart and at number 58 on the Billboard 200, making it their highest charting album in the United States to date. On 9 June 2015, a 12-second clip teaser of the band performing aggressively in an empty warehouse entitled "FOALS // 2015" was released through their social media. Two days later, it was announced that What Went Down was to be released 28 August 2015 via Transgressive Records with a slightly longer trailer in lieu. On 16 June, the album's self-titled debut single was debuted on DJ Annie Mac's BBC Radio 1 show, along with the premiere of the music video (directed by Niall O'Brien) via YouTube. What Went Down received largely positive reviews from contemporary music critics. At Metacritic, which assigns a normalised rating out of 100 to reviews from mainstream critics, the album received an average score of 77, based on 23 reviews, which indicates "generally favorable reviews". Mark Beaumont of NME praised the album, saying, "For ‘What Went Down’, written in their Oxford “stinkbox”, they have found their fulcrum. Riffs. Massive, fucking heavy cavern rock
```

### Album 236, chunk 2

```text
riffs, the size of cathedrals and the weight of God's balls. They slammed into your eardrums like wrecking balls the first time you heard the compulsive title-track, aghast that these desert rock goliaths could be the same band that sounded like frivolous disco pixies just two years ago. Opening their fourth album, Yannis roaring “When I see a man I see a lion!” over its Stooges-meets-Queens fuzz throttle, it sounds like a defining statement, an arrival. They've mastered math rock, destroyed disco and flattened funk, now they measure hard rock in their hands like a medicine ball, and find it a comfortable weight." Ian Cohen of Pitchfork gave the album a generally positive review noting that, "What Went Down is the latest example of Foals’ uncanny ability to make records whose basic musical trajectory and quality are nearly equal regardless of the band's intentions going in. And What Went Down is their most consistent, steady-handed work yet—the distance between their purest pop moments ("Miami", "My Number") and their opulent ballads ("Spanish Sahara") has virtually disappeared. It's also significantly less exciting than Total Life Forever and Holy Fire, dynamic records because of their unevenness and ambitious strain—while Foals have realized a sound that's truly their own, they sound far too comfortable in it." Yannis Philippakis – vocals, guitar, art direction Jack Bevan – drums Jimmy Smith – guitar, keyboards Walter Gervers – bass, backing vocals Edwin Congreave – keyboards, backing vocals James Ford – producer, additional keyboards, guitar & percussion Damien
```

### Album 236, chunk 3

```text
Arlot – studio assistant Alan Moulder – mixing at Assault & Battery Studios, London Caesar Edmunds – mix assistant John Davis – mastering at Metropolis Studios, London Kit Monteith and Foals – filming and editing of "Crème anglaise" and the Poolside Sessions Niall O'Brien – director of "What Went Down" Liz Kessler – producer of "What Went Down"
```

## Album 237: Land Speed Record — Hüsker Dü

- **album_id:** `a46f5014-fda5-4a0a-9a3e-d163849d885e`
- **Tags (identification only):** hardcore, hardcore punk, rock, alternative rock, noise rock, punk
- **Chunks:** 2 (332 words)

### Album 237, chunk 1

```text
Land Speed Record is a live album (and first full-length release) by American punk rock band Hüsker Dü, released in January 1982 by New Alliance Records. It was recorded live on August 15, 1981, at the 7th Street Entry, a venue in Minneapolis, Minnesota. The album is a straight-forward hardcore record compared to the melodic post-hardcore that the band pioneered and performed towards the end of their career. Hüsker Dü's August 1981 concert was recorded straight to 4-track soundboard tape on a three hundred dollar budget. Mould said, "We played really really fast and kept it together; and we did it live with no overdubs." Once the band had taped it they realized they lacked the financial means to release the album. Friend of the band and member of Minutemen, Mike Watt, offered to put out the album on his label, New Alliance. The original LP release on New Alliance contained an insert with lyrics and upcoming tour dates. The album got a European release on Alternative Tentacles in the UK. The album was reissued in 1987 on SST Records on compact disc and LP. Like Hüsker Dü's other releases, Land Speed Record has not been remastered to alter the LP's sound for the compact disc release. The band's ongoing royalty disputes with SST have been given as the cause for not having a unique CD edition issued. Ken Shipley of The Numero Group has noted that the original tape was stolen from the band's van. The SST CD contains
```

### Album 237, chunk 2

```text
only two tracks, one for each side of the original LP. The Numero Group's 2017 box set Savage Young Dü includes an alternate version of the same set, recorded at a Twin/Tone Records showcase two weeks later. Bob Mould – guitar, vocals Greg Norton – bass, vocals Grant Hart – drums, vocals Hüsker Dü – producer, mixdown Steve Fjelstad – remote mix, mixdown Terry Katzman – remote mix assistant Doug Remley – remote mix assistant Wayne B. Case – remote mix assistant
```

## Album 238: Late for the Sky — Jackson Browne

- **album_id:** `dd0067f6-f38d-4651-94dd-50cda002396f`
- **Tags (identification only):** rock, 1974, classic rock
- **Chunks:** 4 (1023 words)

### Album 238, chunk 1

```text
Late for the Sky is the third studio album by American singer–songwriter Jackson Browne, released by Asylum Records on September 13, 1974. It peaked at number 14 on Billboard's Pop Albums chart. In 2020, the album was deemed "culturally, historically, or aesthetically significant" by the Library of Congress and selected for preservation in the National Recording Registry. Browne was still living in his childhood home, Abbey San Encino, where he began writing the songs for his third album. Because of the high costs of recording his previous album, Asylum Records founder David Geffen required him to complete this next album quicker and at less cost. Browne decided to use his touring band of David Lindley, Doug Haywood, Jai Winding, and Larry Zack. It was also decided that Al Schmitt, an engineer on For Everyman, would co-produce to aid in the album being completed on time. The album was completed in six weeks and at half the cost ($50,000) of For Everyman. Numerous friends of Browne, including Dan Fogelberg, Don Henley, and JD Souther contributed harmony vocals. There were only eight songs on the album, five of them longer than five minutes. Browne has publicly acknowledged that the cover art for Late for the Sky was inspired by the 1954 painting L'Empire des Lumieres ("Empire of Light"), by Belgian surrealist René Magritte. The album itself contains the credit, "cover concept Jackson Browne if it's all reet with Magritte". The original photograph was shot on South Lucerne Avenue just south of West
```

### Album 238, chunk 2

```text
2nd Street in Windsor Square, about 10 miles southwest of Browne's childhood home, the Abbey San Encino, in Highland Park, California. Designer and front cover photographer Bob Seidemann said, "I spoke to Jackson in 1980 and he told me he thought it was his favorite cover. Lest the jacket appear too funereal, a mood-defusing photo of a relaxed Jackson, almost smiling and looking as though he has a surprise to share, occupies a small square of the back cover." Reviewing for Rolling Stone in 1974, Stephen Holden highly praised the album, calling it Browne's "most mature, conceptually unified work to date" and saying that the "...open-ended poetry achieves power from the nearly religious intensity that accumulates around the central motifs; its fervor is underscored by the sparest and hardest production to be found on any Browne album yet... as well as by his impassioned, oracular singing style." In a retrospective review for AllMusic, William Ruhlmann describes the themes of the album as "love, loss, identity, apocalypse", similar to Browne's debut album, feeling that Browne "delved even deeper into them...Yet his seeming uncertainty and self-doubt reflected the size and complexity of the problems he was addressing in these songs, and few had ever explored such territory, much less mapped it so well." According to The Rolling Stone Album Guide, Late for the Sky "strengthens and solidifies Browne’s approach; it’s the quintessential Browne album. The metaphorical complexity of 'Fountain of Sorrow' and the clear-eyed poignancy of 'For a Dancer' would be a
```

### Album 238, chunk 3

```text
tough act to follow...when his songwriting is sharp, the mellowing trend in his music dulls the impact." A 1999 Rolling Stone review of For Everyman called Late for the Sky Browne's "masterpiece". MusicHound Rock: The Essential Album Guide calls it "a bit mopey, but it hangs together as Jackson Browne's strongest and most melodious album, with a couple of rockers thrown in to perk up the listeners." Robert Christgau was more critical in Christgau's Record Guide: Rock Albums of the Seventies (1981), saying that Browne's "linguistic gentility is inappropriate, his millenarianism is self-indulgent." Ultimate Classic Rock critic Michael Gallucci rated two songs from the album, "Before the Deluge" and "Late for the Sky", as being among Browne's top 10 songs. Gallucci stated that "Before the Deluge" "piles on the apocalyptic dread" and "could be heralding the end of a relationship ... or maybe something much, much bigger" Gallucci felt that "it foreshadows themes of growing up and out of youthful idealism found on The Pretender, and Running on Empty, but with more widespread and cataclysmic results." In his speech inducting Browne into the Rock and Roll Hall of Fame, Bruce Springsteen called Late for the Sky Browne's "masterpiece" and referred to the car doors slamming at the end of "The Late Show". In 2000 it was voted number 594 in Colin Larkin's All Time Top 1000 Albums. In 2003, the album was ranked number 372 on Rolling Stone magazine's list of the 500 greatest albums of all time, Browne's highest
```

### Album 238, chunk 4

```text
ranking. In a 2012 update it ranked at 377. The album was certified as a Gold record in 1974 and Platinum in 1989 by the Recording Industry Association of America (RIAA). "For a Dancer" has a unique connection to Saturday Night Live. The song was played at memorial services for both John Belushi and Phil Hartman (by Browne at the Hartman service). The title track was used in the 1976 Martin Scorsese film Taxi Driver. "Fountain of Sorrow" was covered by Joan Baez on her 1975 album Diamonds & Rust; "Before the Deluge" was covered by Joan Baez on her 1979 album Honest Lullaby; Baez and Browne performed the song together on her 1989 PBS concert special. It was also covered in 1981 by Irish group Moving Hearts on their eponymous debut album;"Walking Slow" and "Fountain of Sorrow" were released as singles but both failed to chart. The title track is included as essay twenty in Songbook (published in the United Kingdom as 31 Songs) by Nick Hornby. Jackson Browne – vocals, acoustic guitar, piano, slide guitar (on "The Road and The Sky") David Lindley – electric guitar, lap steel guitar, fiddle; harmony vocals (as Perry Lindley) David Campbell – string arrangement on "The Late Show" Jai Winding – piano, Hammond organ Doug Haywood – bass guitar, harmony vocals Larry Zack – drums, percussion Joyce Everson and Beth Fitchet – women harmony vocals Dan Fogelberg, Terry Reid and Don Henley – harmony vocals Fritz Richmond – jug on "Walking Slow" JD Souther – harmony vocals H. Driver, Henry Thome, Michael Condello – handclaps Jackson Browne – producer, cover concept Al Schmitt – producer
```

## Album 239: The Ghosts That Haunt Me — Crash Test Dummies

- **album_id:** `8a2b5262-5d23-40cc-b11e-93892a8c15e0`
- **Tags (identification only):** folk rock, rock, pop rock, alternative and punk
- **Chunks:** 1 (226 words)

### Album 239, chunk 1

```text
The Ghosts That Haunt Me is the 1991 debut album by the Canadian folk rock group Crash Test Dummies. It featured their hit "Superman's Song". The artwork featured on the cover, and throughout the liner notes, is by 19th-century illustrator Gustav Doré and is from The Rime of the Ancient Mariner by Samuel Taylor Coleridge. The same painting would later be used for black metal band Judas Iscariot's final album To Embrace the Corpses Bleeding, in 2002. Art is also taken from the French novelist Nicolas Restif de la Bretonne's The Discovery of the Austral Continent by a Flying Man, 1781. The Ghosts That Haunt Me was successful, selling 400,000 copies in Canada and 200,000 copies in the United States by November, 1993. AllMusic writer Stephen Thomas Erlewine called The Ghosts That Haunt Me "a fine debut album by the ever-smug, collegiate, folk-pop humorists." Brad Roberts – lead vocals, acoustic and electric guitars Ellen Reid – piano, keyboards, accordion, tin whistle, backing vocals Benjamin Darvill – mandolin, harmonica Dan Roberts – bass guitar Vince Lambert – drums Steve Berlin – percussion Bob Doige – recorder on "At My Funeral" Greg Leisz – pedal steel on "The Voyage" Garth Reid – banjo on "Comin' Back Soon" Lynn Selwood – cello on "Superman's Song" Bill Zulak – violin on "Winter Song", "The Country Life" and "At My Funeral".
```

## Album 240: Moment of Truth — Gang Starr

- **album_id:** `b14d4b13-15d9-431d-9354-4d86c5170f1a`
- **Tags (identification only):** hip hop, east coast hip hop, jazz rap, east coast rap, east coast rap;jazz rap;rap
- **Chunks:** 2 (443 words)

### Album 240, chunk 1

```text
Moment of Truth is the fifth studio album by American hip-hop duo Gang Starr, released on March 31, 1998, by Noo Trybe Records and Virgin Records. Gang Starr recorded Moment of Truth in sessions at D&D Studios. It is widely regarded as Gang Starr's magnum opus, and one of the greatest hip-hop albums of all time. Moment of Truth marked Gang Starr's fifth studio album, released in 1998 following a four-year hiatus. Prior to the album, both artists were pursuing solo work; with DJ Premier prolifically collaborating with artists such as Jay-Z, Nas, and Biggie during this period, while Guru had released his second instalment of his Jazzmatazz series. This contributed to a refined sound for the album, while maintaining the group's signature hardcore style. Guru faced serious legal issues, including a gun charge that could have resulted in a five-year prison sentence. The weight of this potential outcome influenced much of the album's thematic direction, particularly in tracks such as "Moment of Truth," which reflected the group's real-life struggles. Tension over Guru's drinking habits also briefly led to DJ Premier stepping away from the group during the album's production. However, the two reconciled and completed the album together. The album is the group's most commercially successful album to date. Moment of Truth debuted at #1 on the Top R&B/Hip Hop Albums chart. The album sold 97,000 copies in its first week. It went on to sell over 500,000 copies and was certified Gold by the RIAA on May 7,
```

### Album 240, chunk 2

```text
1998. The lead single, "You Know My Steez", became the duo's second Billboard Hot 100 appearance in 1997, peaking at #76. Spin magazine ranked it as the #16 album of 1998. Pitchfork also ranked it as the 16th best album of 1998. Writer Marcus J. Moore wrote: "Moment of Truth is an all-in effort that found the duo at their creative apex. Not only did Guru and Premier step up their respective talents, the album also featured standout verses from rappers Inspectah Deck, Freddie Foxxx, G-Dep, and Scarface. For a group teetering on the edge, Moment of Truth is Gang Starr’s shining moment." The album's title track was featured in the 2011 Matthew McConaughey film The Lincoln Lawyer. The title track also appeared in the soundtrack of the 2001 video game Dave Mirra Freestyle BMX 2 as well as an episode during the third season of the television show Mr. Robot. The song Work appears on ESPN promos for SC6 with Michael/Jemele. Work also appeared in the 1998 movie Caught Up starring Bokeem Woodbine and was included on the soundtrack. Work was again sampled in 2019 for a Bank of Melbourne television commercial.
```

## Album 241: Rancid — Rancid

- **album_id:** `4785f854-95c1-4ea4-a53f-873d9ae891ff`
- **Tags (identification only):** punk rock, punk, rock, alternative pop/rock, alternative/indie rock, hardcore punk, melodic hardcore, oi
- **Chunks:** 3 (705 words)

### Album 241, chunk 1

```text
Rancid (also known as Rancid 5 or Rancid 2000 to avoid confusion with their debut album) is the fifth studio album by the American punk rock band Rancid, released on August 1, 2000. It is the second eponymous album and the first to be released through frontman Tim Armstrong's label, Hellcat Records. It also features the return of producer Brett Gurewitz, who has produced every subsequent album by the band. Recording concluded in April 2000. It is Rancid's most hardcore offering to date, which was released as a follow-up to the more ska and reggae oriented Life Won't Wait. It spans 22 tracks in under 40 minutes, owing to over 3/4 of the songs clocking at under 2 minutes. "Maggots" was recorded, but that ended up being a song on Lars Frederiksen & the Bastards record. The Japanese version includes one bonus track, "Sick Sick World". Songs on the album make reference to famous gangster Al Capone, as well as the Norse god Loki, John Brown, Ulysses S. Grant, Nelson Mandela, Charles Van Doren, Geoffrey Chaucer's Canterbury Tales and Don Giovanni. Brett Gurewitz (Bad Religion) reunited with Rancid and became their producer for this album. It was 6 years since he co-produced the band's second album Let's Go (1994), although he engineered the band's third album, ...And Out Come the Wolves (1995). Rancid and Gurewitz would continue their collaboration for their next five albums, Indestructible, Let the Dominoes Fall, Honor Is All We Know, Trouble Maker, and Tomorrow Never Comes.
```

### Album 241, chunk 2

```text
On the record released to the public, there was a mastering error on the track "Poison" on the first run of CDs pressed, but was fixed in subsequent pressings and is not present on the vinyl copies of the record. "Disgruntled" was posted on the band's website on June 3, 2000. A joint music video for "Don Giovanni" and "Disgruntled" was directed by Tim Armstrong. Shortly after this, a demo version of "Poison" was released on Punk-O-Rama 5. "Let Me Go" was released as the album's lone official single while "Radio Havana" was released as a promotional single. Music videos for "Let Me Go", "GGF (Golden Gate Fields)", "Young Al Capone", "I Am Forever", "Dead Bodies", "Rwanda", "Blackhawk Down", "Black Derby Jacket", "Rattlesnake", "Poison" and "Loki" were also released. After being planned for release in May 2000, Rancid was eventually released on August 1, 2000. In November, the band embarked on tour of the US, with support from AFI and the Distillers. Between June and August 2001, the group performed on the Warped Tour. Following this, the band appeared at the Reading and Leeds Festivals. The album received mostly positive reviews, though it failed to meet the success of Rancid's three previous albums. Rick Anderson of AllMusic noted "After several fine, if rather derivative, albums of ska-inflected punk rock, and after years of being criticized for relying unduly on gestures lifted from the Clash, Rancid has come roaring out with the harshest and most consistent album of their career. It
```

### Album 241, chunk 3

```text
wouldn't be entirely accurate to say that they've left their influences behind; rather, they've integrated them more completely and created a sound that is completely satisfying without having to prove anything about its own originality. That sound ends up being something like a cross between the Clash circa 1978 and the hardcore punk of the early-'80s Los Angeles scene. "Rwanda" is a stutter-step anthem of sympathy for a devastated country; "Corruption" has an atonal power-chord progression and headlong tempo that Minor Threat would have killed for; and "Blackhawk Down" is built on a ridiculously catchy descending bassline and a distinctly Oi!-flavored singalong chorus. No ska, no reggae, no dub, just 22 tracks in 38 minutes with barely a pause between songs and high tempos all the way. If you're looking for artistic subtlety, go back to the catalog; if all you need is a half-hour of undiluted adrenaline, you've come to the right place." Select gave the album a rating of three out of five, referring to the album as "infectious as they are insufferable". Tim Armstrong – vocals, guitar Lars Frederiksen – guitar, vocals Matt Freeman – bass, vocals Brett Reed – drums Brett Gurewitz – producer, mixing Thomas "TJ" Johnson – engineer, mixing
```

## Album 242: Praise & Blame — Tom Jones

- **album_id:** `cd487b92-f0e3-4789-aa9d-48d6ab184ca9`
- **Tags (identification only):** adult contemporary, blues, blues rock, gospel, ale jaja, american trad rock, best of 2010, dylan cover
- **Chunks:** 3 (566 words)

### Album 242, chunk 1

```text
Praise & Blame is the 38th studio album by Welsh musician Tom Jones, released on 26 July 2010. The album was Jones' first release with Island Records and was recorded in 2009 at the Real World Studios in Wiltshire, England. Produced by Ethan Johns, Praise & Blame is made up of largely little known devotional and gospel covers, marking a departure from the pop-orientated style that had dominated Jones' recent recordings. Upon its release, Praise & Blame received generally positive reviews from most critics. Giving the album four stars, Andrew Perry in The Daily Telegraph claimed that the album was "by far Jones' best album in two decades" and stated that "with its loose, spontaneous sound, and the all-pervasive sense of artistic rebirth…it’s a revelation." Similarly, Andy Gill in The Independent stated: "Overall, it's an extraordinary achievement: Praise & Blame represents the kind of reconnection with his core creative fire that was hinted on a few tracks of his last album, 24 Hours, but is here left naked and bleeding raw, bereft of showbiz blandishments". Giving the album five stars, Gill labelled the album one of the best in Jones' six decade long career. The album's stripped-down production and focus upon spiritual songs gained numerous comparisons to Johnny Cash's American series and Elvis Presley's 1968 comeback. Writing in American Songwriter, Rick Moore applauded the song selection and stated that "on this excellent collection of songs examining the human condition, Jones confronts the issues of heaven and hell in a way
```

### Album 242, chunk 2

```text
that Cash did for much of his life, especially toward the end of it… [Tom] Jones and [Ethan] Johns have made a real statement in the same way that Rubin, and of course T Bone Burnett, do almost every time they produce an album." Writing in The New York Times, Stephen Holden states that Jones' vocal delivery "conveys the contrition of a sinner as he delivers a mixture of traditional spirituals and contemporary gospel songs tautly arranged for a small band. It is a respectful, expressively focused exploration of a genre beloved by Mr. Jones’s American counterpart, Elvis Presley." The change of musical direction, together with stripped down, live production – much at odds with Jones' traditional style – led Michael Hann in The Guardian to state "at last Jones the artist is the match of Jones the entertainer." Allison Stewart, writing in The Washington Post, stated that Praise & Blame is "Jones's "O Brother," "Raising Sand" and "Ain't No Grave" all rolled into one, a mixed bag of roots-related styles – blues, gospel-lite, country-folk, rockabilly, soul – stripped of all fat and reduced to the barest elements of voice and spartan, if often electrified, instrumentation. The song choices are impeccable, from a thunderous cover of Bob Dylan's "Oh Mercy" standout "What Good Am I?" to a holy roller redo of John Lee Hooker's "Burning Hell," all propelled by Jones's remarkable voice, still a marvel of quaveriness and bluster and sinew after all these years." "Tom has made, in my
```

### Album 242, chunk 3

```text
opinion, a really great record. [...] It's the church of Tom Jones [...]" – remembering that Tom Jones already thought it was "positive" to have a real church in your honor (in 2006); in 2007, the ministry (founded by actor and pastor Jack J. Stahl) nicknamed "Church of Tom Jones", was being a considered a success story among 35 remarkable companies according to an award-winning book.
```

## Album 243: All the Little Lights — Passenger

- **album_id:** `e257763e-c7f4-4f48-b089-a501e5526e53`
- **Tags (identification only):** indie pop, alternative rock, indie folk, pop, indie rock, 5+ wochen, alternative/indie rock, english
- **Chunks:** 2 (323 words)

### Album 243, chunk 1

```text
All the Little Lights is the fourth studio album by English singer-songwriter Passenger and was released by Black Crow Records and Nettwerk on 24 February 2012. The album contains 12 tracks, comprising 11 studio tracks recorded at Sydney's Linear Recording, and one song recorded live at The Borderline in London. The album originally contains no guest appearances, but the re-recording version, released on 10 November 2023, features Ed Sheeran, Gabrielle Aplin, Foy Vance, and Nina Nesbitt. A limited edition features a second disc containing acoustic versions of eight songs from the album. All the Little Lights received positive reviews from music critics. John Walshe of Hot Press called it "a truly gorgeous record". Hilary Saunders of Paste said, "Luckily, Passenger serves as a very real, welcome alternative to reality TV talent shows, proving original songwriters do still exist". Jordan Blum of PopMatters called it "a masterful work of art, plain and simple". Mike Rosenberg – lead vocals, acoustic guitar, omnichord (tracks 1, 3, 5) Stu Larsen – backing vocals Georgia Mooney – backing vocals Stuart Hunter – piano, keys, synths Cameron Undy – upright bass, electric bass Kerry Martin (violin), Madeleine Boud (violin), Shelley Soerensen (viola), Janine Boubbov (cello) – strings (tracks 1, 2, 3, 6) James Steendam – string arrangements (tracks 1, 2, 3, 6) Glenn Wilson – drums (tracks 1, 2, 3, 9, 10) Declan Kelly – drums (track 5) Tim Hart – drums (tracks 4, 7, 8), banjo (tracks 3, 6, 9), mandolin (track 6) Jess Ciampa
```

### Album 243, chunk 2

```text
– percussion (tracks 3, 6, 8, 11) Lucian McGuiness, Simon Ferenci, Sam Golding – brass (tracks 3, 7, 9, 10, 11) Alan Davey – trumpet (track 5) A re-recorded version of the album was released on 10 November 2023, entitled All the Little Lights (Anniversary Edition). The album features song duets with Ed Sheeran ("Let Her Go"), Gabrielle Aplin ("Circles"), Foy Vance ("Life's for the Living") and Nina Nesbitt ("Feather on the Clyde").
```

## Album 244: Family Scriptures — Mo Thugs

- **album_id:** `a7dabe52-6fb7-452e-9f79-c7d117b8dd1f`
- **Tags (identification only):** gangsta rap, contemporary r and b, g funk, r and b, hip hop, pop rap, urban, west coast hip hop
- **Chunks:** 1 (234 words)

### Album 244, chunk 1

```text
Family Scriptures is the debut studio album by American hip hop collective Mo Thugs. It was released on November 5, 1996, via Mo Thugs/Relativity Records. The recording sessions took place at Private Island Trax in Los Angeles. It was produced by Krayzie Bone, who also served as executive producer together with Layzie Bone, Archie Blaine, Bobby Jones and Paul "Tombstone" O'Neil, with co-producers Gates and Sin. It features contributions from Flesh-n-Bone, II Tru, Ken Dawg, Krayzie Bone, Layzie Bone, Poetic Hustla'z, Souljah Boy, the Graveyard Shift, and Tré. The album peaked at number two on the Billboard 200 and the Top R&B/Hip-Hop Albums in the United States selling 219,000 copies. On January 3, 1997, it received Platinum certification status by the Recording Industry Association of America for selling 1,000,000 copies. Its sequel, Mo Thugs Family Scriptures Chapter II: Family Reunion, was released on May 26, 1998. On April 28, 2011, former Bone Thugs-n-Harmony/Mo Thugs associate Roland Brown filed the lawsuit in the Cuyahoga County Court of Common Pleas in Cuyahoga County, Ohio, for breach of contract over unpaid royalties, claiming he wrote “Take Your Time” and “Here With Me” by Tré. Naming Mo Thugs Records, Loud Records, Relativity Records, Ruthless Records, Sony Music and Warner Music Group as defendants, Brown was seeking for $27 million ($24 million in damages and $3 million in mechanical royalties for the single, music video, and Family Scriptures album).
```

## Album 245: Retired from Sad, New Career in Business — Mitski

- **album_id:** `92a5b5ce-2d1a-4561-9e60-50fe8743c8bf`
- **Tags (identification only):** rock, alternative rock, indie pop, pop, art pop, baroque pop, chamber pop, indie rock
- **Chunks:** 1 (177 words)

### Album 245, chunk 1

```text
Retired from Sad, New Career in Business is the second studio album by American musician Mitski. Mitski recorded the project in 2013 while studying music at State University of New York at Purchase. The album was her senior project and featured a 60-piece student orchestra. Every song on the album was accompanied by a music video, each video playing a part in an ongoing story, making it a visual album. In summer 2020, the track "Strawberry Blond" gained popularity on the social media app TikTok, specifically in the cottagecore community. Retired from Sad, New Career in Business received praise for its blend of "out-of-the-norm orchestral sounds with electronics and 'found' sounds". In a career retrospective following Mitski's 2018 studio album Be the Cowboy, Jesse Herb of Atwood Magazine said that the album "completely highlights Mitski's writing growth in just one year, and also her impeccable composition" and that the album "could be in an off-broadway musical." Herb singled out "Shame", "Circle", and "Strawberry Blond" in particular, saying that the latter "feels like a lost Dar Williams record".
```

## Album 246: Today’s Empires, Tomorrow’s Ashes — Propagandhi

- **album_id:** `48954e02-25ef-4b77-bae8-1974e4c096bf`
- **Tags (identification only):** punk rock, punk, alternative pop/rock, alternative/indie rock, hardcore punk, melodic hardcore, pop/rock, punk revival
- **Chunks:** 2 (499 words)

### Album 246, chunk 1

```text
Today's Empires, Tomorrow's Ashes is the third studio album by Canadian punk rock band Propagandhi, released February 6, 2001. It was released on the band's own G7 Welcoming Committee Records label in Canada and Fat Wreck Chords elsewhere. It is the first Propagandhi release of new material on their own label. Recording sessions were delayed due to various issues, one of which was the band's practice space being flooded, and another being that drummer Jord Samolesky broke his foot playing hockey. Prior to recording in May 2000, the band announced that it would have 14 songs, and would be titled Today's Empires, Tomorrow's Ashes. Samolesky broke his foot again in June 2000 while riding motocross; recording continued into August. One of the album's tracks, "Back to the Motor League", indirectly refers to two songs by the Dead Kennedys, "Triumph of the Swill" and "Chickenshit Conformist", as well the year of their release on the 1986 album Bedtime for Democracy. The "Back to the Motor League" lyrics state: "fifteen years later it still reeks of swill and chickenshit conformists". Both the Dead Kennedys songs and the Propagandhi track concern the co-opting of punk ideology by the corporate record industry. "Purina Hall of Fame" is a reference to the Nestlé owned pet food company, The Ralston Purina Company. The title is a cynical take on the Purina Animal Hall of Fame, a site that celebrates animals who have saved human lives. The lyrics of "Purina Hall of Fame" obliquely outline Propagandhi's concerns
```

### Album 246, chunk 2

```text
about animal cruelty. The album art features the painting The Unfinished Flag of the United States by American poet Lawrence Ferlinghetti. Propagandhi continued this motif of using established artists to provide their cover artwork on their next two albums, Potemkin City Limits, using a piece by anarchist artist Eric Drooker, and Supporting Caste, which featured a painting entitled "The Triumph of Mischief" by Kent Monkman. After initially being planned for released in October 2000, and then delayed to November due to bassist/vocalist Todd Kowalski and guitarist/vocalist Chris Hannah both losing their voices. The album was again delayed to early 2001, with the label citing "something to do with hockey and ice-fishing." "Back to the Motor League" was posted on G7 Welcoming Committee Records' website on November 10, 2000. Today's Empires, Tomorrow's Ashes was eventually released on February 6, 2001; G7 Welcoming Committee released it in Canada, and Fat Wreck Chords released it in the US. A release show was held at the University of Manitoba in Manitoba, Canada, on February 23, 2001. The band toured eastern Canada in April and May 2001, with Sixty Stories. In June and July, the band toured across Australia. In August and September, the band went on a tour of North America with Randy. Following the September 11 attacks, the remaining tour dates were cancelled. The album was shortlisted for the Polaris Heritage Prize at the 2025 Polaris Music Prize. Chris Hannah – guitar, vocals Jord Samolesky – drums Todd Kowalski – bass, vocals
```

## Album 247: Fast Life — Paul Wall

- **album_id:** `aa7e97ed-7d40-44e2-aee3-4c0451a50aff`
- **Tags (identification only):** dirty south, gangsta rap, hip hop, southern rap, crunk, pop rap, rap, southern hip hop
- **Chunks:** 2 (536 words)

### Album 247, chunk 1

```text
Fast Life is the fourth studio album by American rapper Paul Wall. It was released on May 12, 2009, by Swishahouse and Asylum Records. Production on the album was handled by Beanz-N-Kornbread, Travis Barker, X-Fyle, Antwan "Amadeus" Thompson, Gennessee Lewis, Happy Perez, I.N.F.O., NOVA, Mouse, and Yung Chill, with G-Dash and Michael "5000" Watts serving as executive producers. The album features guest appearances from Z-Ro, Baby Bash, Gorilla Zoe, Kobe, Krizz Kaliko, Lil' Keke, Marty James, Mouse, Tech N9ne, the Federation, Too Short, Trae, Webbie, Yung Chill, Yung Joc, and Yung Redd. Skinhead Rob also provides guest vocals; he and Barker performed with Wall as Expensive Taste. Paul Wall described Fast Life as the project was underway: I really stepped it up a lot lyrically because I wanted this record to show real strength and emotion... We worked with a lot of new producers... so they'll get to see a lot of different vibes that they might have not seen with me with past albums. Subject matter we went a little more in-depth, talked about a lot of different things that I never really spoke on—I might have mentioned it here and there but never really made whole songs about. I had a lot of fun working on the album. "You're going to hear in-depth topics," he says, adding that he's been recording nonstop for the album for the last two years, a feat that has given him more than 50 songs to choose from. "You'll hear some stuff that
```

### Album 247, chunk 2

```text
you might not be used to hearing." The album's lead single, called "Bizzy Body", was released on December 2, 2008. The song features a guest appearance from Webbie and Mouse, who produced the track. The music video premiered, via MySpace, on March 27, 2009. The album's second single, "Lemon Drop", was released on the same day as the music video on July 13. The song features a guest appearance from Baby Bash, while the song's production was handled by Gennessee Lewis. The album's third single, "Got to Get It", premiered, along with a music video, on July 23. The song was produced by Beanz-N-Kornbread. The album's fourth and final single, "I Need Mo", was released on the same day as the music video on September 24. The song features Kobe, with Travis Barker producing. Wall shot the video with his iPhone. Alex Thornton of HipHopDX gave praise to Wall for delivering his "usual wit" throughout the tracklist, while also revealing "unexpected musicality" on "I'm Clean". While being mixed on the club tracks, Thornton concluded that "Fast Life is one of the better albums from [Paul] Wall and definitely has a handful of gems." AllMusic's David Jeffries was critical of the record's "B-plus material" lacking the Swishahouse sheen from previous songs, but praised Wall for showing reflective introspection, highlighting "Daddy Wasn't Home" as the standout, concluding that: "Even without the epic single, it is interesting to hear Wall's perspective shifting and his horizons expanding." Jonathan Bonanno of XXL wrote, "What Paul lacks in substance, he makes up for with fun-loving, trunk-poppin' anthems. Although his latest lacks the fuel for a full lap 'round the fast life, big homie can always just pump the brakes and drive slow."
```

## Album 248: You Won’t Go Before You’re Supposed To — Knocked Loose

- **album_id:** `d328dba2-d627-4a9c-8b76-0772e854dbbf`
- **Tags (identification only):** metal, metalcore, hardcore punk, 1–4 wochen, aggressive, angry, antireligious, atmospheric
- **Chunks:** 3 (634 words)

### Album 248, chunk 1

```text
You Won't Go Before You're Supposed To is the third studio album by the American hardcore punk band Knocked Loose. It was released through Pure Noise Records on May 10, 2024, and produced by Drew Fulk. Guitarist Nicko Calderon joined the band in 2021. The band released an EP titled, A Tear in the Fabric of Life that same year. According to vocalist Bryan Garris: "A Tear In The Fabric Of Life' was the first time that we sat down and wrote with strict intention...So coming back around, figuring out what we should be, and then applying that to a full album was very interesting...We knew we wanted to have a bigger album in scale, and with that in mind, we could expect every single type of Knocked Loose song there is." The band announced the album and its release of May 10, 2024. The lead single, "Blinding Faith", was released on February 27, 2024. The second single, "Don't Reach for Me" was released on April 3, 2024. The third single, "Suffocate" featuring Poppy, was released on April 23, 2024. You Won't Go Before You're Supposed To has been described as metalcore and hardcore punk, with elements of nu metal. According to the review aggregator Metacritic, You Won't Go Before You're Supposed To received "universal acclaim" based on a weighted average score of 87 out of 100 from 8 critic scores. AllMusic felt that the album "[upped] the intensity of their relentless metalcore sound". Ellis Heasley of Distorted Sound Magazine
```

### Album 248, chunk 2

```text
compared it to Slipknot's Iowa "in its complete disregard for what a band with this much hype is supposed to do in this situation...and ultimately stands as further irrefutable proof of a truly generational talent." Manus Hopkins writing for Exclaim! stated that "at only 10 songs, with the longest still falling short of five minutes, You Won't Go Before You're Supposed To doesn't wear out its welcome." But they felt that "Slaughterhouse 2", featuring Chris Motionless, was "slightly underwhelming in the shadow of its predecessor", from Motionless in White's album, Scoring the End of the World. Ben Beaumont-Thomas of The Guardian called it "an indulgently rich record that keeps revealing more on double-digit listens." According to Luke Morton of Kerrang!, "the heaviness throughout is unrelenting. No acoustic number, no ballad, no concession... this isn't just their best record yet, it's one of the best albums of the year." Stephen Hill of Metal Hammer of praised Drew Fulk's production stating, [his] production gives the record perfect definition while making it sound as loud as a jet plane taking off inside your cranium." According to Caitlin McMahon of Metal Injection, "Knocked Loose has embraced a melodic direction with this record," and called the album "eerie and unsettling." Mandy Scythe of MetalSucks wrote, "From start to finish, this is a solid, heavy record full of memorable and catchy moments that you'll want to revisit time and time again." According, to Ian Cohen of Pitchfork, "[Knocked Loose have] amplified and concentrated their sound into
```

### Album 248, chunk 3

```text
something so potent that it has its own gravitational pull." Dylan Tuck writing for The Skinny wrote, "You Won't Go Before You're Supposed To takes their staunchly savage sound and dashes it with piercing playfulness and crushing confidence; conjuring a profoundly poisonous record containing some of their most deadly moments to date." Sputnikmusic wrote that "[the] album destroys as much as possible while it's on...[but] it leaves a little to be desired once it's over." Bryan Garris – vocals, lyrics Isaac Hale – lead guitar, vocals Nicko Calderon – rhythm guitar, vocals Kevin Otten – bass Kevin "Pacsun" Kaine – drums Poppy – vocals (3) Chris Motionless – additional vocals (7) Drew Fulk – production, mixing, mastering Zach Tuch – additional production, engineering Jeff Dunne – mixing, mastering Jesse Field – engineering assistance, editing
```

## Album 249: …and the Beat Goes On! — Scooter

- **album_id:** `0955dd3f-01f0-47cc-84b0-cdd57087b3b3`
- **Tags (identification only):** electronic, happy hardcore, trance, euro house, rave
- **Chunks:** 1 (177 words)

### Album 249, chunk 1

```text
...and the Beat Goes On! is the debut studio album by German band Scooter. Four singles were released from it: "Hyper Hyper", "Move Your Ass!", "Friends" and "Endless Summer". After the success of the single "Hyper Hyper", Scooter decided to make their debut album. Released in early 1995, it contains brand new tracks and reworked "The Loop!"-remixes. There are no gaps between the tracks, it sounds like an imaginary Scooter gig (on the LP release, however, all tracks are unmixed and 7 tracks, not released as singles, are even without the crowd noises). The album was re-released in 2013 in the "20 Years of Hardcore Expanded Edition" series. This version contains 3 CDs: the first is the digitally remastered original album; the other two contain the singles, B-sides, live recordings, and remixes related to the album. The album was re-released on LP on 31 January 2020 to coincide with the 25th anniversary of the album's release. It was re-released on yellow LP on 12 June of the following year for Record Store Day, limited to 500 copies.
```

## Album 250: Street Songs — Rick James

- **album_id:** `80bd440f-ecc4-4eac-8631-f6214893b5f0`
- **Tags (identification only):** funk, boogie, contemporary r and b, dance pop, disco, pop, rnb 80 s, rock
- **Chunks:** 2 (438 words)

### Album 250, chunk 1

```text
Street Songs is the fifth studio album by American musician Rick James, released in April 1981 on Gordy Records. It contained three of James' biggest hits: the singles "Give It to Me Baby", "Super Freak", and "Fire and Desire". "Give It to Me Baby", the lead single from the album, became James' second number one single on the R&B chart, spending five weeks at the top spot. The next single, "Super Freak", was an even bigger hit, reaching number 16 on the Billboard Hot 100. A Deluxe Edition was released in 2001 containing an additional 17 mixes and live versions of the album tracks. Although the song "Fire and Desire" (a duet he performed with singer Teena Marie) was not originally released as a single, the song itself received much airplay on R&B radio stations and has since become a classic hit. James and Marie would reunite to perform the song at the 2004 BET Awards five weeks before James' death. The album became an immediate success upon its release, eventually reaching number three on the US Pop chart—James's highest-charting album during his career—and spending twenty weeks at number one on the US R&B chart. The album was certified platinum in the US in July 1981. By 1983, the album had sold nearly four million copies worldwide. At the 24th Annual Grammy Awards (1982), James was nominated for Best Male Rhythm and Blues Vocal Performance for the album while being the first African American male artist to be nominated in
```

### Album 250, chunk 2

```text
the Best Male Rock Vocal Performance category for the song "Super Freak". Rick James – lead vocals Ja'net Dubois – background vocals Melvin Franklin – background vocals ("Give It to Me Baby") Lawrence Hilton-Jacobs – background vocals Teena Marie – lead vocals ("Fire and Desire"), background vocals ("Give It to Me Baby", "Mr. Policeman") Mary Jane Girls – background vocals The Temptations (Dennis Edwards, Melvin Franklin, Glenn Leonard, Richard Street, Otis Williams) – background vocals ("Ghetto Life", "Super Freak") Gerald Albright – tenor flute ("Make Love to Me", "Fire and Desire") Oscar Alston – bass, handclaps, percussion Reggie Andrews – string arranger Rollice Dale – string contractor Clifford J. Ervin – flugelhorn, piccolo, trumpet John Ervin – flute, trombone Fernando Harkless, Roy Poper – trumpet Nathan Hughes, Armando Peraza, Raul Rekow, Bugsy Wilcox – percussion Rick James – arranger, bass guitar, composer, drums, guitar, horns, percussion, producer, timbales, timpani Daniel LeMelle – flute, handclaps, horn arrangements, alto and tenor saxophone, string arrangements Tom McDermott – guitar, percussion Alonzo Miller – producer, composer Narada Michael Walden – drums Stevie Wonder – harmonica soloist ("Mr. Policeman") Levi Ruffin – synthesizers
```
