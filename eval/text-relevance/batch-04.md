# Embedding text relevance, batch 4 of 12 (albums 76–100 of 300)

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

This batch: **25 albums, 81 chunks**.

## Album 76: Raw Like Sushi — Neneh Cherry

- **album_id:** `bee5a7d3-4519-4405-8c14-c2b59c7f2609`
- **Tags (identification only):** pop, urban, 80s, alternative rap, dance, dance pop, electronic, hip hop
- **Chunks:** 3 (594 words)

### Album 76, chunk 1

```text
Raw Like Sushi is the debut studio album by Swedish musician Neneh Cherry, released 5 June 1989 by Virgin Records. The album includes the commercially successful single "Buffalo Stance". An early version of "Buffalo Stance" appeared on the B-side of the 1986 Stock Aitken Waterman-produced Morgan-McVey single, "Looking Good Diving", titled "Looking Good Diving with the Wild Bunch". The single was not successful; however, the B-side was re-recorded with Tim Simenon of Bomb the Bass, and became the version of "Buffalo Stance" that was a worldwide hit, reaching No. 3 in the UK Singles Chart, No. 3 on the Billboard Hot 100 and No. 1 in the Netherlands and Sweden. The album also contains the No. 8 US (and No. 20 UK) hit "Kisses on the Wind", and the No. 5 UK hit "Manchild". All musicians and programmers are credited in the album sleeve, however Cameron McVey, Cherry's husband, is credited as "Booga Bear". Massive Attack's Robert Del Naja co-wrote "Manchild", and fellow member Andrew Vowles aka DJ Mushroom performs on "Kisses on the Wind", "The Next Generation" and "So Here I Come". "My Bitch" is a vocal duet with Gilly G. The cover and inner photos were shot by fashion photographer Jean-Baptiste Mondino. Raw Like Sushi is distinctive for its eclectic mix of genres, incorporating influences from across the trends of 1980s pop music. Cherry sings and raps accompanied by a diverse set of sounds, including pianos, synthesizers, brass instruments, guitars, and go-go percussion. The album's lyrical themes are
```

### Album 76, chunk 2

```text
influenced by Cherry's experiences of motherhood, and her education and upbringing. When it was released, the album was favorably compared to Madonna and Prince, though it did not reach similar popularity. NME critic David Quantick praised Raw Like Sushi as "the sort of record you can rarely buy – immediate, commercial pop that only someone with a rather individual worldview could have made", highlighting its unconventional song structures and Cherry's "wit, intelligence and even maturity." Selina Webb of British music newspaper Music Week called it "eclectic, wholesome, a subtly teasing collection of provoking yet pouting songs", "a confident manifesto from refreshing new pop diva." Pete Clark of Hi-Fi News & Record Review said that Cherry's music "is illuminated by a jazzy delight in non-conformity" and singled out "effortlessly memorable" "Buffalo Stance" and "Manchild". As per Chris Murray of RPM "this package contains something for any contemporary dance music fan." Raw Like Sushi is included in the book 1001 Albums You Must Hear Before You Die. Neneh Cherry – lead vocals, programming Sandy McLelland – backing vocals on "Inna City Mamma", "Love Ghetto" and "Phoney Ladies" Chandra Armstead – backing vocals on "Outré Risqué Locomotive" Eagle-Eye Cherry – toasting on "Heart" Sarah Erde – Hispanic vocals on "Kisses on the Wind" Cameron "Booga Bear" McVey – backing vocals, executive producer, mixing, beats on "Manchild" Phil Chill – programming, beats, backing vocals on "The Next Generation" Claudia Fontaine – backing vocals on "Kisses on the Wind" Nellee Hooper – vibraphone Jerod Minnies
```

### Album 76, chunk 3

```text
– guitar on "Love Ghetto" Alvin Moody – beats and programming on "Outré Risqué Locomotive" Nick Plytas – programming Jeff Scantlebury – congas on "Kisses on the Wind" John Sharp – programming on "Manchild" Tim Simenon – beats and turntables on "Buffalo Stance" and "Heart" Dynamik Duo – beats Mark Saunders – multi-instruments, beats on "Buffalo Stance" Wil Malone – conductor, programming, string arrangements on "Manchild", backing vocals Gordon Dukes – backing vocals on "Outré Risqué Locomotive" Mushroom – programming, turntables on "Kisses on the Wind", "The Next Generation" and "So Here I Come"
```

## Album 77: To Hell With the Devil — Stryper

- **album_id:** `a1fe00d1-7ef8-43df-aa5f-5ea4852ae049`
- **Tags (identification only):** christian metal, christian rock, contemporary christian, glam metal, hard rock, heavy metal, glam, gospel
- **Chunks:** 3 (586 words)

### Album 77, chunk 1

```text
To Hell with the Devil is the third studio album by the Christian metal band Stryper, released in 1986. It was the first Christian metal album to achieve platinum status, selling over one million copies. It remained the best-selling Christian metal album until P.O.D.'s Satellite in 2001. Within nine weeks of its October 1986 release, the album had entered the national Top 40 and was approaching gold certification, making it the best-selling album in the Enigma Records' catalogue to date. Robert Sweet attributed the album's ambition to the success of their first album, Soldiers Under Command: "This one was easier in a sense because we had more money to do it. But it was harder in one sense because we worked with a co-producer Stephan Galfas, who was always sending us back to do it again, to do whatever we could to make it perfect." The album was listed at No. 88 in the 2001 book, CCM Presents: The 100 Greatest Albums in Christian Music. The album was the only heavy metal album on the list. Ian Christe, author of the heavy metal history book Sound of the Beast: The Complete Headbanging History of Heavy Metal (2003), mentions To Hell with the Devil in his book as one of the landmarks of the glam metal movement. Throughout 1987, both music videos for "Free" and "Honestly" ranked No. 1 on Dial MTV, the daily MTV list of most requested videos. The first single/video for "Calling on You" also reached No. 2
```

### Album 77, chunk 2

```text
on the show. "Honestly" was the biggest single from the record, peaking at #23 on Billboard's Hot 100 Singles Chart. The original artwork depicted four long-haired angels (closely resembling the band members) throwing the devil into a fiery pit. The cover was then changed on later pressings to a basic black cover with the Stryper logo and the album title in the center. According to Michael Sweet's autobiography, as the band started to record the album, Michael felt Tim Gaines wasn't the right bassist for the record. He was replaced by bassist Matt Hurich, who ultimately didn't work out. So session bassist Brad Cobb took Gaines' place while recording the album. However, before the tour began, Sweet asked Gaines to rejoin, as he felt it wasn't right to perform as "Stryper" without him. In 2010, HM Magazine listed To Hell with the Devil No. 3 on its Top 100 Christian Rock Albums of All Time list, stating that "when this album broke, it went multi-platinum, forever raising the ceiling of what heavy Christian music could do." Heaven's Metal fanzine ranked it No. 6 on its Top 100 Christian metal albums of all-time list. Michael Sweet – lead vocals, backing vocals, lead guitars, acoustic guitar, arrangements Oz Fox – guitars, backing vocals Robert Sweet – drums John Van Tongeren – keyboards Brad Cobb – bass guitar Oz Fox – producer Michael Sweet – producer Robert Sweet – producer, cover concept Stephan Galfas – producer, arrangements, engineer Dan Nebanzal – engineer Gary
```

### Album 77, chunk 3

```text
Myerberg – technical assistant Eddy Schreyer – mastering at Capitol Mastering (Hollywood, California) Brian Ayuso – art direction, design Ray Brown – costume design Annamaria DiSanto – photography Anna Revenge – photography Neil Zlozower – photography Suzan Carson – photography assistant Kyle Rae Sweet – make-up artist Janice Sweet – management "Free"/"Calling on You" - released February 10, 1987 (Enigma Records 75001) "Honestly"/"Sing-Along Song" - released August 10, 1987 (Enigma 75009) "Calling On You" "Free" "Honestly" "All of Me" (on the documentary Stryper: In the Beginning)
```

## Album 78: The Shepherd's Dog — Iron & Wine

- **album_id:** `a3fbd83d-5cd6-473e-8823-82c9d5bfbba2`
- **Tags (identification only):** folk, folk rock, indie rock, alternative and punk, country, indie, rock, singer songwriter
- **Chunks:** 1 (272 words)

### Album 78, chunk 1

```text
The Shepherd's Dog is the third full-length studio album by Iron & Wine, released on September 25, 2007. If bought at select retailers or if pre-ordered through Sub Pop, the album comes with a bonus disc featuring two unreleased tracks. "Boy with a Coin" is the first single and was released on July 10, 2007 via Sub Pop, including the single edit of the song along with two other tracks. The album debuted at number 24 on the U.S. Billboard 200 chart, selling about 32,000 copies in its first week. In 2008, "Flightless Bird, American Mouth" was used in the movie Twilight. The song was specifically chosen for the film's prom scene by Kristen Stewart, the female lead, and appears on the movie's soundtrack. On its release The Shepherd's Dog received widespread critical acclaim. At Metacritic, which assigns a normalized rating out of 100 to reviews from mainstream critics, the album received an average score of 84, based on 34 reviews, which indicates "universal acclaim". The album was ranked at #10 in Paste's list of top albums of 2007. "Pagan Angel and a Borrowed Car" was #86 on Rolling Stone's list of the 100 Best Songs of 2007. Pitchfork included the album in their Top 50 Albums of 2007 ranking it at number 36. "Flightless Bird, American Mouth" was a key track used in the 2008 film Twilight, part of the Twilight Saga. The song is closely associated to the successful movie franchise and an acoustic version of the song was also used in The Twilight Saga: Breaking Dawn - Part 1. "Arms of a Thief" - 3:41 "Serpent Charmer" - 2:40
```

## Album 79: Here You Come Again — Dolly Parton

- **album_id:** `803e326c-a164-4053-8612-8831e0a449f9`
- **Tags (identification only):** country rock, country, ballad, countrypolitan, pop, rock
- **Chunks:** 3 (625 words)

### Album 79, chunk 1

```text
Here You Come Again is the nineteenth solo studio album by American entertainer Dolly Parton. It was released on October 3, 1977, by RCA Victor. The album was a commercial success, peaking at number 20 on the US Billboard 200, placing at number 2 on the Hot Country Albums year-end chart, and also being nominated for Favourite Country Album at the American Music Awards. It became Parton's first album to be certified platinum by the Recording Industry Association of America for shipping a million copies. The lead single and title track was also a success, entering the top five of the US Billboard Hot 100 and being nominated for Favourite Country Single at the American Music Awards. Billboard published a review of the album in the October 17, 1977, issue, which said, "This is by far Parton's most accessible pop crossover attempt. The material she chooses to work with, some by noted authors, others self penned, is delivered in Parton's little girl-sounding vocals. Her sweet-flowing voice becomes more and more likeable on each cut, emitting a warm innocence. The delicate string and horn accompaniment adds to the breezy, more subtle country effect. And the strong guitar work, pedal steel included, doesn't distract from Parton's vocals. Parton's title track single, which she sang on the Rock Awards television broadcast, is a sure bet to crack the Hot 100." In the October 22, 1977, issue, Cashbox published a review saying, "Dolly's winning ways have convinced more than a few former non-believers that
```

### Album 79, chunk 2

```text
country and western audiences have no right to a monopoly on this songbird's talents. With this album, Dolly takes a giant step into the pop mainstream with a spicy repertoire that features only an occasional banjo or pedal steel lick. But even those who have seen her perform will have to be at least mildly surprised at how naturally proficient Dolly is at jumping into a completely new bag." The album peaked at No. 1 on the US Billboard Hot Country LPs chart and No. 20 on the US Billboard 200 chart. In Canada, the album peaked at No. 12 on the RPM Canadian Albums chart. The album's first single, "Here You Come Again", was released in October 1977 and peaked at No. 1 on the US Billboard Hot Country Singles chart, No. 3 on the US Billboard Hot 100 and No. 2 on the US Billboard Easy Listening chart. In Canada, the single peaked at No. 1 on the RPM Canadian Country Singles chart, No. 7 on the RPM Canadian Singles chart and No. 1 on the RPM Canadian Easy Listening chart. In Australia, the single peaked at No. 10 on the ARIA Top 100 Singles chart. The single also peaked a No. 75 on the OCC UK Singles Chart. In February 1978, "Two Doors Down" and "It's All Wrong, But It's All Right" were issued as a double A-side single, aimed at the pop and country charts respectively. The version of "Two Doors Down" issued on the single
```

### Album 79, chunk 3

```text
was recorded by Parton in January 1978 and features a more pop sound than the album version. It would replace the original album version on all subsequent pressings of the album. "Two Doors Down" peaked at No. 19 on the US Billboard Hot 100 and No. 12 on the US Billboard Easy Listening chart. In Canada, the single peaked at No. 26 on the RPM Canadian Singles chart and No. 7 on the RPM Canadian Easy Listening chart. "It's All Wrong, But It's All Right" peaked at No. 1 on both the US Billboard Hot Country Singles chart and the RPM Canadian Country Singles chart. In April 1980, "Me and Little Andy" was released as a single in the UK and it did not chart.
```

## Album 80: Telephone Free Landslide Victory — Camper Van Beethoven

- **album_id:** `bf89dd34-d5a5-41fc-9043-d979a493ca86`
- **Tags (identification only):** country rock, folk rock, garage rock, pop, psychedelic rock, rock, acoustic, alternative rock
- **Chunks:** 1 (250 words)

### Album 80, chunk 1

```text
Telephone Free Landslide Victory is an album by musical group Camper Van Beethoven, released on Independent Project Records in June 1985. It featured the band's best known song, "Take the Skinheads Bowling". The album has sold over 60,000 copies. The band's lineup at the time of recording was David Lowery (lead vocals, rhythm guitar), Jonathan Segel (violin, keyboards, guitar, backing vocals), Chris Molla (guitar, backing vocals), Victor Krummenacher (bass, backing vocals), and Anthony Guess (drums). The album is the only Camper Van Beethoven record not to feature guitarist Greg Lisher. Lisher is actually listed in the album credits as a band member, but he did not join the band until after the album was recorded. The reunited Camper Van Beethoven frequently features several of the album's songs in their set lists, including "Take the Skinheads Bowling", the countrified Black Flag cover "Wasted", the hardcore send-up "Club Med Sucks", "The Day That Lassie Went to the Moon", "Ambiguity Song", and several of the instrumentals. The band originally intended the album to be titled Telephone Tree Landslide Victory, but a friend who was producing advance copies of the LP on cassette mistakenly replaced "Tree" with "Free". Michael Stipe named Telephone Free Landslide Victory one of his ten favorite albums of 1985 in a list he wrote for Rolling Stone. David Lowery – lead vocals, guitars, drums Jonathan Segel – violin, backing vocals, keyboards, mandolin, noises Chris Molla – guitars, backing vocals, drums Victor Krummenacher – bass, backing vocals Anthony Guess – drums
```

## Album 81: Get the Knack — The Knack

- **album_id:** `0ad004b2-f430-4a23-8c6f-d41266846b07`
- **Tags (identification only):** power pop, rock, new wave, pop rock
- **Chunks:** 5 (1068 words)

### Album 81, chunk 1

```text
Get the Knack is the debut studio album by American power pop band The Knack, released in June 1979. At the time, the album was one of the most successful debuts in history, selling over 1,000,000 copies in less than 2 months and spending 5 weeks at #1 on the Billboard 200 album chart. The lead single from the album, "My Sharona", was number one on the Billboard Hot 100 for 6 weeks and #1 on Billboard's Top Pop Singles of 1979 year-end chart. The follow-up single, "Good Girls Don't", reached #11 on the Hot 100 and followed "My Sharona" to number one on the Canadian Singles Chart. In Billboard magazine's year-end charts, Get the Knack ranked at #16 for 1979, and #72 for 1980. The Knack formed in L.A. in May 1978, and after shopping their demo tape to various record labels without success, the band began playing the local club circuit beginning in June, playing over 50 gigs in the next six months. The band quickly gained a following as word of mouth spread about their energetic shows, and musicians such as Ray Manzarek, Tom Petty, and Bruce Springsteen came to their shows and joined the group on stage. By December, 13 record labels, including some that previously rejected them, were offering recording contracts, and the group signed with Capitol Records in January 1979. Get the Knack was recorded in just two weeks at a cost of only $18,000, an extremely quick and inexpensive recording at a time
```

### Album 81, chunk 2

```text
when many established artists were spending months and several hundred thousand dollars to record an album. The album was produced by Mike Chapman, who had written hits for Sweet in the early 1970s and most recently produced Blondie's breakout album Parallel Lines. Get the Knack was released in June 1979 and became an immediate success, thanks in part to an intense promotional campaign by Capitol Records. The Knack's image was largely influenced by the Beatles. The album cover imitates the Beatles' first Capitol LP, Meet the Beatles!, and the back cover photo depicts a scene from the Beatles' film A Hard Day's Night. To complete the Beatles' imagery, the 1960s Capitol rainbow label adorned the LP, a detail the band had written into its contract. The album obtained a gold certification from the RIAA in just 13 days, becoming Capitol Records' fastest-selling debut LP since Meet the Beatles! in 1964. In August, the album reached #1 on the Billboard 200, where it remained for 5 weeks, and was certified platinum by the RIAA for 1,000,000 copies sold. The lead single, "My Sharona", also met with immediate success, becoming Capitol's fastest-selling debut single since the Beatles' "I Want to Hold Your Hand" and staying at #1 on the Billboard Hot 100 for 6 weeks. A backlash against the Knack's overnight success formed among critics who found the band's image too contrived and their attitude too brash. San Francisco conceptual artist Hugh Brown, who had designed the Clash's Give 'Em Enough Rope
```

### Album 81, chunk 3

```text
album cover, started a "Knuke the Knack" campaign complete with T-shirts, buttons, and bumper stickers. Some music writers began to criticize the band for what they perceived as arrogance, hype, and a misogynist attitude expressed in their songs. The band's refusal to do interviews was also viewed negatively by the music press. One entertainment weekly, Scene magazine, refused to publish a review of the Knack's concert in Cleveland due to what it called "attempts at censorship" by the band's management. Robert Christgau of The Village Voice was critical of the album's misogynistic themes and remarked that if the Knack "felt this way about girls when they were unknowns, I shudder to think how they're reacting to groupies." However, Christgau countered critics who had dismissed the band on "purely technical terms", arguing that "if they're less engaging musically than, say, the Scruffs, they have a lot more pop and power going for them than, say, the Real Kids." Billboard critic Dick Nusser was particularly complimentary of tracks such as "Let Me Out", "Maybe Tonight" and "That's What the Little Girls Do", while noting that the pleading song "Oh Tara" indicates that the Knack "aren't strict girl haters." In a retrospective review, AllMusic critic Chris Woodstra wrote that the Knack's attempt to "update the Beatles sound for the new wave era" was "a good idea that was well executed", describing Get the Knack as "at once sleazy, sexist, hook-filled, and endlessly catchy – above all, it's a guilty pleasure and an exercise
```

### Album 81, chunk 4

```text
in simple fun." Trouser Press noted the negative portrayal of the female protagonists of certain songs and singled out "Maybe Tonight" as "bottom-of-the-barrel sap", but praised "My Sharona", "Let Me Out" and "Frustrated" as "tight guitar pop." In 2016, Paste ranked Get the Knack at number 39 on its list of the 50 best new wave albums. Nirvana frontman Kurt Cobain listed Get the Knack as one of his 50 favorite recordings. When the album was initially released on CD in 1989, the song "(She's So) Selfish" had vocals different from the original release, with lyrics like "coming from the quaalude scene" changed to "...lame'o scene". Capitol Records used a censored, alternate version of the track which was requested in certain countries. The album was re-issued on CD in 2002 as a remastered version true to the original vinyl release. This version included bonus demos of "My Sharona" and "That's What the Little Girls Do", as well as a rehearsal take of "Maybe Tonight". It also included a cover of Bruce Springsteen's Darkness on the Edge of Town outtake "Don't Look Back", which the Knack recorded in 1979 but was left off the Get the Knack LP, and a cover of Nick Lowe's "I Knew the Bride". A subsequent CD re-issue was remastered by Iconoclassic Records in 2011. Unlike the previous remaster, the 2011 release contains no dynamic range compression. In April 2017, Mobile Fidelity Sound Lab released an audiophile version of the album on hybrid SACD. This release, like
```

### Album 81, chunk 5

```text
the 2002 Capitol and 2011 Iconoclassic versions, utilizes the original, un-censored mixes. Doug Fieger – lead and backing vocals, rhythm guitar, harmonica on "Good Girls Don't" Berton Averre – lead guitar, backing vocals Prescott Niles – bass, backing vocals on "My Sharona" Bruce Gary – drums, backing vocals on "My Sharona" Mike Chapman – production David Tickle – recording, backing vocals on "My Sharona" Peter Coleman – recording
```

## Album 82: There Be Squabbles Ahead — Stolen Babies

- **album_id:** `9c520a04-12b7-477c-96f8-4d7dbc67fdd1`
- **Tags (identification only):** avant garde metal, alternative metal, electronic, experimental rock, dark cabaret, post hardcore, rock
- **Chunks:** 1 (96 words)

### Album 82, chunk 1

```text
There Be Squabbles Ahead is the first full-length album from Stolen Babies. The album has received almost unanimously positive reviews, and has helped to expand their fanbase massively. Additional background vocals on tracks 3, 7 and 12 performed by Dan Rathbun Additional tuba on track 7 performed by Dan Rathbun Violin on tracks 7 and 11 performed by Carla Kihlstedt Trumpet on tracks 3, 7 and 12 performed by Michael Iago Mellender Acoustic guitar on track 11 performed by Davin Givhan Recorded and mixed by Dan Rathbun Album artwork by Dominique Lenore Persi and Crab Scrambly
```

## Album 83: Leaving Through the Window — Something Corporate

- **album_id:** `4f84a992-b8ce-40d8-b68f-44ae80c72f65`
- **Tags (identification only):** alternative rock, pop rock, punk, rock, emo, pop punk
- **Chunks:** 11 (2638 words)

### Album 83, chunk 1

```text
Leaving Through the Window is the second studio album and major-label debut by American rock band Something Corporate. Following the success of the Drive-Thru Records-released Audioboxer (2001) EP, the band signed to their label distributor MCA Records in late 2001 after the EP caught their attention. The three-month recording process for Leaving Through the Window took place in studios across California and Florida, with Jim Wirt acting as producer. A few songs from previous releases were re-recorded for inclusion on the album; the material was anywhere from three months to three years old. A music video was made for "If You C Jordan" in early 2002; the group then embarked on a three-month long US tour. After the tour, Leaving Through the Window was released jointly by Drive-Thru and MCA Records on May 21. The band performed on the Warped Tour in 2002 and supported New Found Glory once on a European trek and again on a US tour through to the end of the year. A DVD single that featured music videos for "I Woke Up in a Car" and "If You C Jordan" was released during the US leg. They co-headlined a three-month US tour with the Juliana Theory, which coincided with the release of a music video for "Punk Rock Princess". It was released as a UK single in early March and was promoted with a tour there; at the end of the month, "If You C Jordan" was released as a single. Leaving Through the Window
```

### Album 83, chunk 2

```text
sold 12,000 copies in its first week, charting at number 101 on the Billboard 200 chart in the process. It appeared on another Billboard chart, Heatseekers Albums, where it reached number one. "Punk Rock Princess" and "If You C Jordan" had some success: "If You C Jordan" charted at number 29 on Billboard's Alternative Songs chart and number 68 in the UK; "Punk Rock Princess" charted only in the UK at number 33. As of mid-2005, the album's sales stood at 291,000 copies. The record received a mixed reception from critics, with negative comments on its length and frontman Andrew McMahon's vocals, and positive comments about his musicianship. Something Corporate's debut album Ready... Break was released through a local concert venue in November 2000. Before vocalist/pianist Andrew McMahon's final year of high school, guitarists Josh Partington and Reuben Hernandez left for college. Eventually, the two flew back to play gigs. The group met to discuss their commitment to the band; a portion of their day-job wages was being used to help fund the group. Hernandez left the group to continue his studies and was replaced by William Tell. After finalizing their line-up, the group began performing at local venues, eventually gaining support slots for bands like Better Than Ezra and Sugar Ray. Shortly afterwards, a number of record labels showed an interest in signing the group. House of Blues representative Sean Striegel suggested to independent label Drive-Thru Records that they check out the band while they were in the process
```

### Album 83, chunk 3

```text
of recording the Audioboxer EP in June 2001. Representatives from the label, who saw the group's crossover potential, visited McMahon's home for a performance in his garage. They stayed for over an hour and a half as the group performed a full set, compared to the 20-minute sets that other labels wanted them to play. The following month, the band signed to Drive-Thru Records, partially because the label liked their ballads. Drive-Thru wanted a minor release to introduce the band, leading to the release of Audioboxer in October. KROQ came across the EP and began playing the track "If You C Jordan" later that month. The EP soon caught the attention of major label MCA Records, which had a distribution deal with Drive-Thru that allowed MCA to upstream bands from them. In November and December, the group toured across the US with the likes of Reel Big Fish, Sugarcult and River City High. Pre-production began for Leaving Through the Window on Boxing Day 2001 and wrapped up in early January 2002. Main recording took place between January and March at various studios across the US: Cello Studios in Hollywood, California; 4th Street Recording in Santa Monica, California; South Beach Studios in Miami Beach, Florida; and Jungle Room Studios in Glendale, California. Jim Wirt produced and engineered all the sessions, with additional engineering by Mike Fraser. "Globes & Maps" was engineered by Brian Reeves. PJ Smith, Alan Sanderson and Joel Ausbrooks served as additional engineers. CJ Eiriksson and Patrick Shevelin acted
```

### Album 83, chunk 4

```text
as Pro-Tools engineers. Smith provided background vocals on "Punk Rock Princess", "I Woke Up in a Car", "The Astronaut", "Hurricane", "Straw Dog", "Drunk Girl" and "Not What It Seems". Strings were engineered by Steve Churchyard with assistance from Robert Read. Session musician Patrick Warren contributed chamberlin and organ to "Globes & Maps". "Punk Rock Princess" and "Hurricane", both of which featured on the Audioboxer EP, were re-recorded for the album as the group wanted to be "happier with their execution", according to McMahon. Three tracks—"Cavanaugh Park", "Straw Dog" and "Drunk Girl"—from Ready... Break were also re-recorded for the album. On two separate occasions, the piano was tracked in half-time to give it a different sound. Mixing was done by Tom Lord-Alge in April, before being mastered by Stephen Marcussen at Marcussen Mastering in Hollywood. All of the songs on Leaving Through the Window were written by McMahon, with the exception of "Hurricane", "Fall" and "You're Gone" which were written by Josh Partington. McMahon found it easier coming up with arrangements on the piano, rather than a guitar, as it seemed a better instrument to expand song structures. The band spent the time required to get the right sound balance between McMahon's piano, and Partington and Tell's guitars. McMahon reasoned that instruments needed to be at the right place in a song's arrangement so they could be "both felt and heard." "Punk Rock Princess", "Cavanaugh Park", "Straw Dog" and "Globes & Maps" feature string arrangements written by Paul Buckmaster who conducted
```

### Album 83, chunk 5

```text
the 26-piece orchestra that performed them. Partington described the album as a "conglomeration of songs that were anywhere from three months to three years old ... like a greatest hits of our early stuff." Discussing the album's title, McMahon said they wanted a name that was connected to some of the tracks, namely, to two lines in "I Want to Save You". He added that they lines "kind of reference the kind of getting in and out without being detected so that's how we came out with that". Musically, the album has been classified as alternative rock, pop punk and power pop. It has been compared to works by bands like Jimmy Eat World, Cheap Trick, Lit, and New Found Glory. Austin Saalman of Under the Radar wrote that the album was a "a warm concoction of guitar-heavy pop-punk and emotive piano rock, charmingly complemented by [...] McMahon’s naive boy-next-door lyrical sensitivity". "I Want to Save You" is a character sketch of a girl who was mistreated by her partner. Discussing "Punk Rock Princess", McMahon said he was interested in a girl who liked punk rock music while he was in high school. The song served as a metaphor for what was a frequent discrepancy between the pair, which McMahon described: "She was cooler than I was and she liked punk and I was this, like, squirrely kid in, like, a piano band." The song had initially began as a ballad. "I Woke Up in a Car" was written after
```

### Album 83, chunk 6

```text
the first Something Corporate tour. A day or two after it ended, McMahon sat in his parents' garage, where his piano was situated and wrote the song around his memories of the tour. They almost named it "I Woke Up in a Van", but felt that it did not fit as well as car did. The song references a show the band played in Poughkeepsie, New York at The Chance venue, as well as to Rockford, Illinois. "If You C Jordan" was written during McMahon's last year in high school, after a guy named Jordan wanted to fight with him over a girl. It is about being bullied and using words to fight back. The track was not initially planned for release on the album and was meant to appear solely on the Audioboxer EP. "If You C Jordan" and "If I Were a Terrorist, I'd Bomb the Graduation" were written during the same period in 68 time. The band wanted both tracks to on the EP as an introduction to their music. However, "Terrorist" was left off the release because of the September 11 attacks; the group thought it would be in bad taste to use it. They had been playing the track live for up to six months before the event occurred. "The Astronaut" was written in the midst of the album's recording sessions while Tom Petty was working in the next room. It lyrics reference space travel, which would continue to be an occasional theme in McMahon's
```

### Album 83, chunk 7

```text
songwriting. "Hurricane" is credited to Partington, with McMahon contributing three words. When Partington played the track for the band at practice, McMahon was enthusiastic about it. Sean Richardson of The Boston Phoenix said Partington's lyrical form was "more introspective and harder-hitting than McMahon’s". McMahon wrote "Cavanaugh Park" while he was 16 or 17; it was named after a recreational area in Lake Forest, California. The park serves as a benchmark for incidents while growing up, like hanging out with friends and getting into trouble. The pop punk track "Fall" is followed by two indie pop songs, "Straw Dog" and "Good News"; the latter two, plus closer "Globes & Maps", showcased a sound that McMahon would later explore with his solo project Jack's Mannequin a few years later. While recording was nearly completed, "If You C Jordan" was gaining traction at popular alternative radio stations. In early February 2002, a music video was filmed for the track at El Segundo High School. It was directed by Richard Reines, who co-founded Drive-Thru Records and filmed over two 14-hour days. It opens with Chris Owen, who acts as Jordan the bully showing up to high school in a Porsche. The band takes musical equipment from the choir room and starts performing in the hallway. It concludes with them hanging out with Summer Altice. On February 25, the group performed the track on The Late Late Show with Craig Ferguson. On March 15, the album's title Leaving Through the Window was announced; later that
```

### Album 83, chunk 8

```text
day, the group worked on images for the album with photographer Justin Stephens. Between March and May, the group toured across the US. Following this, the group filmed a music video for "I Woke Up in a Car" in Toronto, Canada during an off day in between tours. Leaving Through the Window was released on May 21, 2002 as a joint release by Drive-Thru and MCA Records. The UK edition, which was released on September 9, included "Little" and "Walking By" (both from Audioboxer) as bonus tracks. The artwork stars Sara Pohlman, a 15 year-old model from Tennessee. Between late June and mid-August, the group went on the Warped Tour (2002). Following this, the group toured across Europe supporting New Found Glory in August and September, before headlining two shows in the UK and four in Japan. "I Woke Up in a Car" was released to Hot AC radio on September 27. In October and November, the band toured across the US alongside New Found Glory, Finch and Further Seems Forever. A DVD single was released on November 5, featuring music videos for "I Woke Up in a Car" and "If You C Jordan". Following two European shows, the band went on a co-headlining tour of the US with the Juliana Theory between January and March 2003, supported by Vendetta Red, Red West and Fiction Plane. On January 17, a music video was released for "Punk Rock Princess"; it was filmed the previous December in Toronto, Canada. The track was
```

### Album 83, chunk 9

```text
released as a CD single in the UK on March 17 with "Forget December" and "Konstantine" as the B-sides. The latter track was initially planned for inclusion on the album, but was let off as the band thought it did not fit with album's flow. In March, the group went on a UK tour with Home Grown and Steel Train. On March 31, "If You C Jordan" was released as a single. Leaving Through the Window received mixed response from music critics. AllMusic reviewer Alex Henderson wrote the group's style was "punky yet vulnerable and introspective", with McMahon "anchoring" many of the songs around his piano. He felt it was "among the more memorable and promising alterna-rock efforts of 2002." CMJ Music Monthly writer Michelle Kleinsak said McMahon's musicianship on the piano disconnects the group from their emo/punk peers, and helps make their album "such an elegant and confident debut." Melodic reviewer Kaj Roth wrote that the "real nice" record was filled with "loads of catchy tunes" that are "perfect for the radio this hot summer." Richard Abowitz of Rolling Stone noted the band crafted "suburban ennui and high school angst into slick, hummable punk." He mentioned that McMahon's song writing was "the secret weapon," calling it "derivative, but not boring." Sputnikmusic emeritus Andrew H. viewed the album as "pretty average", though he found the lyrics/vocals "really personal", adding that some listeners would dislike McMahon's voice. The staff at Modern Fix noted that the keyboard would struggle to compete with
```

### Album 83, chunk 10

```text
the loudness of the guitars and McMahon's vocals, while praising their "excellent grasp on constructing songs that have defined parts and movements, flows and sways". Punknews.org's Scott Heisel opened his review complaining of the record's length: "This CD is too fucking long", before adding that it was "way too long overall. There are too many songs, and each song seems to enjoy sauntering in at around the 4 minute mark". In spite of this, he said the group seemed "pretty proficient at writing a good pop song" and praised McMahon's vocals. Steve Servos of Chart Attack claimed the band tried "so hard to be punk ... but fall so far short that when they look around they can’t even see where punk went." He criticized the album's length, wishing the band had left "at least a minute from each song on the studio’s floor, where they belong." Ink 19 reviewer Kiran Aditham found McMahon's singing "less annoying" compared to the band's labelmates New Found Glory. He lambasted the release as being "standard fare" which Weezer had done "much better and more creatively almost a decade ago." Drowned in Sound's Peter White dismissed the album as an "XFM playlist without the edge" that "makes a mockery of all things beautiful about the joy of discovery and the fun of breathing." Leaving Through the Window charted at number 101 on the Billboard 200 chart, selling 12,000 copies in its first week. It also charted at number one on the Heatseekers Albums chart.
```

### Album 83, chunk 11

```text
"Punk Rock Princess" charted at number 33 in the UK. "If You C Jordan" charted at number 29 on the Alternative Songs chart and number 68 in the UK. By June 2005, album sales stood at 291,000 copies. The album has appeared on best-of pop punk album lists by BuzzFeed, Houston Press and i-D. Additionally, Rock Sound ranked it at number 227 on the list of best albums in their lifetime. Cleveland.com ranked "Punk Rock Princess" at number 52 on their list of the top 100 pop-punk songs. Alternative Press ranked "Punk Rock Princess" at number 92 on their list of the best 100 singles from the 2000s. In his retrospective piece, Saalman wrote that the album, "remains a significant act within its genre’s canon, its songs forming a collective portrait of late-’90s and early-’00s American youth culture".
```

## Album 84: The Genius Hits the Road — Ray Charles

- **album_id:** `f2f8be78-7a47-4aa7-974f-9cec22ca953b`
- **Tags (identification only):** jazz, rhythm and blues, soul, blues, jazz blues, piano blues, standards, vocal jazz
- **Chunks:** 1 (263 words)

### Album 84, chunk 1

```text
The Genius Hits the Road is a 1960 album by Ray Charles. The concept album focuses on songs written about various parts of the United States. It peaked at number nine on the pop album charts and produced a US No. 1 single, "Georgia on My Mind". Ray Charles – vocals, piano Edgar Willis – bass Milt Turner – drums David "Fathead" Newman – tenor saxophone Hank Crawford – alto saxophone Leroy Cooper – baritone saxophone John Hunt – trumpet Marcus Belgrave – trumpet Ralph Burns – arranger, conductor Sid Feller – producer Ray Charles – piano, vocals Edgar Willis – bass (tracks 14, 17, 18) Roosevelt Sheffield – bass (track 19) Mel Lewis – drums (track 14) Teagle Fleming – drums (tracks 17) William Peeples – drums (tracks 18, 19) David "Fathead" Newman – tenor saxophone (tracks 14, 17 to 19), alto saxophone (tracks 18, 19) Hank Crawford – alto saxophone (tracks 14, 17), baritone saxophone (track 17) Leroy Cooper – baritone saxophone (track 14) Emmet Dennis – baritone saxophone (tracks 18, 19) John Hunt – trumpet (tracks 14, 17, 19) Marcus Belgrave – trumpet (track 17) Joe Bridgewater – trumpet (tracks: 18, 19) The Raelettes – vocals (tracks 15, 17, 19) The Jack Halloran singers – vocals (track 15) The Cookies – vocals (track 19) Frank Rosolino – trombone (track 14) Harry Betts – trombone (track 14) Kenny Shroyer – trombone (track 14) Richard Nash – trombone (track 14) Bruno Carr – percussion (track 14) Ahmet Ertegün – producer (tracks 17, 18 19) Jerry Wexler – producer (tracks 17, 18 19)
```

## Album 85: Young Modern — Silverchair

- **album_id:** `83676020-877a-4dc1-bfe0-a1a80273a5ae`
- **Tags (identification only):** pop, rock, alternative rock, art rock, australian, experimental, mellow, orchestral
- **Chunks:** 4 (1024 words)

### Album 85, chunk 1

```text
Young Modern is the fifth and final studio album by Australian rock band Silverchair, released in Australia on 31 March 2007 and in the United States on 24 July 2007 and co-produced by Daniel Johns and Nick Launay. The title comes from a nickname given to Daniel Johns by composer Van Dyke Parks. The tracks "Straight Lines", "Reflections of a Sound", "If You Keep Losing Sleep" and "Mind Reader" were released as singles. Young Modern entered the Australian albums chart at No. 1 on 15 April 2007, their fifth consecutive album to do this, making Silverchair the first band to accomplish this feat in Australia. The album was certified Triple Platinum by the ARIA, peaked at No. 70 on the US Billboard 200 chart and opened at No. 8 on the New Zealand albums chart. Young Modern won six ARIA Awards in 2007, including Best Group, Best Rock Album, Single of the Year (for "Straight Lines") and Album of the Year. At the J Awards of 2007, the album was nominated for Australian Album of the Year. Silverchair spent five weeks in the Australian Hunter Region in late 2005 to practise and sharpen material that Daniel Johns had previously written. Following this, the band recorded intermediate full band demo versions of the songs. To record the final versions of these songs, the band travelled to Los Angeles to record with record producer Nick Launay at Seedy Underbelly Studios. Johns co-produced the album alongside Launay. During the L.A. sessions, additional songs
```

### Album 85, chunk 2

```text
were written and recorded. Van Dyke Parks was hired to compose orchestral arrangements for three songs: "If You Keep Losing Sleep", "All Across the World" and the three part epic "Those Thieving Birds/Strange Behaviour". Johns and Parks travelled to Prague to have the orchestral arrangements recorded by the City of Prague Philharmonic Orchestra. Unlike previous Silverchair albums, Young Modern was funded independently by the band rather than by a record label. This was done to "remove the added label pressures", according to Billboard. The name Young Modern comes from a nickname given to Silverchair's lead singer, Johns, by Van Dyke Parks during their time working together on Diorama in 2002. The album features various guest appearances from Australian and international musicians such as Luke Steele, Julian Hamilton and Paul Mac, the latter of whom performed with Johns as the Dissociatives. Young Modern was released on 31 March 2007 in Australia, and 24 July 2007 in the United States of America. The album was released in several versions—the original contained 11 songs, while the iTunes version contained an extra song, "English Garden" which featured Judith Durham. A limited edition DVD was also released, which contained a documentary entitled "The making of Young Modern", as well as the "Straight Lines" music video. The album's artwork (as well as the music video for "Reflections of a Sound") is a three-dimensional homage to Mondrian art; specifically, it is a direct reference to Composition with Red Blue and Yellow and its variants. The first single
```

### Album 85, chunk 3

```text
from Young Modern, "Straight Lines", was released on 10 March 2007, a week before the album's release. "Straight Lines" entered the ARIA Charts at No. 1 on 25 March 2007, and held that rank for four weeks. It also peaked at No. 11 on the RMNZ charts. "Straight Lines" was certified double platinum by the Australian Recording Industry Association. On 28 October 2007, "Straight Lines" won Best Selling Australian Single at the ARIA Music Awards of 2007, as well as Single of the Year. The second single, "Reflections of a Sound", was released on 14 July 2007 as a digital single. The music video for "Reflections of a Sound" was first screened on 8 June 2007, and was produced by Damon Escott and Stephen Lance of Head Pictures. The third single from Young Modern was "If You Keep Losing Sleep", released on 9 October 2007. The song spent one week on the ARIA charts at No. 16, before dropping out of the charts. The music video for "If You Keep Losing Sleep" was orchestrated by Van Dyke Parks, and was produced by Damon Escott and Stephen Lance, who also created the "Reflections of a Sound" video. The video was described by Molly Meldrum as "the best video I've seen from Australia ever". Young Modern's fourth single, "Mind Reader", was released as an internet-only single on 23 February 2008. It had first appeared on radio in January that year. Young Modern was received with high acclaim from reviewers. AllMusic's review said
```

### Album 85, chunk 4

```text
the album contained "catchy melodic hooks, inspired lyrical themes, and stunning string arrangements", and called it the "pinnacle of the band's fascinating development". Reviewer Clayton Bolger heaped praise on most of the songs on the album, calling "Straight Lines" an "instant rock classic". Rolling Stone reviewer David Fricke called Silverchair's members "young (in their late twenties)...[and] aggressively modern", and Entertainment Weekly called the album a "polished glam-rock suite". Sputnikmusic reviewer Tyler Fisher also approved of the album, although he did not think it was as good as it was made out to be, commenting "It is not as good as the ARIA awards will undoubtedly make it out to be but still one of the better mainstream listens of the year." During his weekly entertainment segment on the popular Australian breakfast show Sunrise, Australian music personality Molly Meldrum made a sincere comparison of the album to the classic Beatles album Sgt. Pepper's Lonely Hearts Club Band. Nick Pearson of PopMatters, meanwhile, was critical of the album. He began his review with the statement "Once you reach the level of intellectual maturity where you can tell the difference between cryptic but poetic lyrics and nonsensical crap, you have outgrown Silverchair", and continued in the same fashion throughout. Pearson unfavourably likened Johns to Kurt Cobain, saying Johns shared a common inability: "[an] inability to write lyrics". His only praise was for the third single released from the album, "If You Keep Losing Sleep", stating "'If You Keep Losing Sleep' is proof that Silverchair are capable of recording interesting music". The song "Straight Lines" was featured as downloadable content for the video game Rock Band in 2010.
```

## Album 86: World’s Gone Wrong — Lucinda Williams

- **album_id:** `86617188-0df9-486f-9783-359226063561`
- **Tags (identification only):** 1–4 wochen, alternative country, americana, blues rock, me 26–02 [4.5/6], musikexpress.de [4.5/6], ph 3 stars, plattentests.de [7/10]
- **Chunks:** 2 (318 words)

### Album 86, chunk 1

```text
World's Gone Wrong is the sixteenth studio album by the American singer-songwriter Lucinda Williams. It was released on January 23, 2026, under Williams' own label Highway 20 Records with distribution by Thirty Tigers. World's Gone Wrong features nine original songs composed by Williams and a cover of Bob Marley and the Wailers' "So Much Trouble in the World", heard here as a duet with Mavis Staples. The album also features additional guest appearances from Brittney Spencer ("The World's Gone Wrong" and "Something's Gotta Give") and Norah Jones ("We've Come Too Far to Turn Around"). The album was produced by Tom Overby and Ray Kennedy and recorded at the Room & Board Studio in Nashville, Tennessee. The album's lead single, "The World's Gone Wrong", was released on October 30, 2025, simultaneously with the album's announcement. A performance video coincided with the song's release. The second single, "So Much Trouble in the World", was released on December 12, 2025. In an article published by the Oxford American, writer Jim Beaugez commented, "World’s Gone Wrong articulates the anger, hope, and inspiration she’s carried since the protests of her youth, with songs that explore the struggles of race, poverty, and trauma that continue to shadow America today." The article also references parallels with the 2017 Jesmyn Ward novel Sing, Unburied, Sing, which inspired the song "Sing Unburied Sing": "In the same way Ward uses song as a medium for the marginalized, Williams recognizes the act of singing as protest and affirmation." John Amen of
```

### Album 86, chunk 2

```text
Beats Per Minute wrote, "Williams examines the 'dark age' we’re currently traversing but refuses to surrender to despair". He concluded, "World’s Gone Wrong extends Williams’ fertile run, infused with the aesthetic adventurousness and undiluted honesty that have characterized her work for over four decades". As of August 2nd, 2026 World Gone Wrong has an aggregate score of 82 on Metacritic placing it in the Universal Acclaim category. https://www.metacritic.com/music/worlds-gone-wrong/lucinda-williams
```

## Album 87: Shrines of Paralysis — Ulcerate

- **album_id:** `d8ab1982-36af-4b98-8e02-b8c67a6de7c4`
- **Tags (identification only):** technical death metal, atmospheric sludge metal, dissonant death metal, post metal, sludge metal
- **Chunks:** 3 (781 words)

### Album 87, chunk 1

```text
Shrines of Paralysis is the fifth studio album by New Zealand technical death metal band Ulcerate. The album was released on October 28, 2016, through Relapse Records. The album was officially announced on June 27, 2016, with the band confirming that they would be touring North America in support of the album in late 2016 with Phobocosm and Zhrine, including a show at the Saint Vitus bar in New York City. On August 23, 2016, the release date for the album was confirmed for October 28, 2016 and the band began streaming the album's first single, 'Extinguished Light'. On its release, the album received positive reviews from music critics, and later featured on a number of end-of-year lists. Jamie Saint Merat has explained that the album title represents and represents the species’ apathy and inabilities in dealing with self-imposed catastrophe until it’s beyond the point of reconciliation. In general, the lyrics speak of mankind’s arrogance and narcissism, and failure to respect our irrelevance in the broadest possible sense. The artwork ties in with this inextricably and provides a visual metaphor of the sonic content of the album." The band altered their approach to songwriting, recording and production in comparison to previous albums, with Merat explaining that "In terms of melody, it feels like now is the time for us to pull back from dissonance twenty-four-seven and really start making more melodic music". In his review of the album, music critic John D. Buchanan noted that the album's style was broadly
```

### Album 87, chunk 2

```text
in line with the band's 2008 album Everything Is Fire, but with slight variations, nuances and improvements. He described the album's style as "Sheets and shards of incredibly abrasive, harsh, dissonant guitar work pile up over a pummeling onslaught of drums and grinding bass, and vocalist/lyricist Paul Kelland roars like a wounded animal. Creating a palpable aura of fear, dread, and despair, it's like a black hole that sucks all the light out of the room." He also noted that "This is not just noise, by any means: there is both melody and harmony here, and, while dissonant, the music has, at times, its own strange beauty. There are hints of both classical and jazz influence, and the gloomy, gothic pall of classic doom metal." In an interview, Jamie Saint Merat said the following about the recording process:We split the tracking of instruments over 2 studios, both for convenience and tonal reasons. Drums were tracked at MCA studios here in Auckland over 2 days – nothing too exciting to report, I just track as efficiently as possible, I like to do full takes for the most part with minimal punch-ins to keep the energy of the performance intact. I’m also staunch about zero editing and quantisation after the fact too. We tracked guitars and bass in Auckland also at Depot Studios over a 5 day period, which went smoothly, but was extremely fatiguing in terms of the sheer amount of tracks we needed to lay down (4 channels of rhythm
```

### Album 87, chunk 3

```text
guitars, 2 of bass, between 3 and 4 of additional lead/overlay guitars). Vox were tracked in a day or 2 also at MCA, and I worked on the mix and master over a 2 week period after tracking was done and dusted. Shrines of Paralysis has received very positive reviews from music critics. Sputnik Music described the album as a "masterpiece of musicianship, composition and imagery", writing that "In keeping with Ulcerate opuses of the past, Shrines of Paralysis hides all of its nuances from plain view, uncovering them only for the most devout. Return with regularity and the mosaic begins to piece itself together." Invisible Oranges also praised the album, writing that "A lot of technical death metal gets described as knotty, but Ulcerate are much better at untangling the strands", and that "This decentralized and evasive approach to brutality captures the essence of death metal at its onset – a sense of unease and terrifying otherness – without ever falling prey to the genre’s tropes." Metal Hammer's Dom Lawson described the album as "intensely internal music, wrung from the darkest depths of the New Zealanders’ collective consciousness and spewed out with flailing abandon like Cthulhu bursting through the earth’s surface. It speaks of unimaginable horrors, as barbarous and excruciating maelstroms of dissonance and rhythmic ebb and flow like the opening Abrogation and the unnervingly bleak There Are No Saviours unfold." He concluded that the album is "another evolutionary jump for these shadowy Kiwis, but not one that caters to the easily bewildered." AllMusic's John D. Buchanan praised the album, writing that "this is death metal like she should be wrote." Paul Kelland – vocals, bass Michael Hoggard – guitar
```

## Album 88: Life Goes On — Sash!

- **album_id:** `3770faf0-0fad-4450-b35c-7c55fa9e6a86`
- **Tags (identification only):** electronic, trance, euro house, eurodance, house, progressive house
- **Chunks:** 1 (54 words)

### Album 88, chunk 1

```text
Life Goes On is the second album by the German DJ Sash! released on 17 August 1998 via Mighty label. It contains the hit singles "La Primavera" and "Mysterious Times". Overall, the record includes four singles: "La Primavera", "Mysterious Times", "Move Mania", and "Colour the World". The album was certified gold in the UK.
```

## Album 89: Noël — Josh Groban

- **album_id:** `77749aa0-d168-456f-b549-b81dbe891174`
- **Tags (identification only):** christmas, christmas music, modern classical, classical, easy listening soundtracks and musicals, pop
- **Chunks:** 3 (686 words)

### Album 89, chunk 1

```text
Noël is a Christmas album and the fourth studio album by Josh Groban that was released on October 9, 2007. In the United States, the album is available as a single CD release in most retail stores. However, Target stores released a limited-edition version of the album with a bonus DVD that features a "making of" documentary entitled The Making of Noël. According to Nielsen SoundScan, the album sold 3,699,000 copies in 2007 after its release, making it the overall best-selling album in the US for all of 2007. It was also the best-selling holiday album in 2008, with sales of 915,000 copies. As of October 2015, the album has sold 5.8 million copies in the United States according to SoundScan, making it the second best-selling holiday album in the US in the Nielsen SoundScan era (March 1991–present) behind Kenny G's 1994 holiday set Miracles: The Holiday Album. According to Billboard, Noël is the second best-selling classical album of the 2000s decade in the US, behind Groban's own Closer. On August 14, 2017, Noël was certified Sextuple Platinum by the Recording Industry Association of America, recognizing shipment of six million copies in the United States. On October 12, 2017, Groban announced a tenth-anniversary deluxe edition, released on November 3. It includes six songs not featured in the initial release, including four new recordings. AllMusic editor Matt Collar found that the album "features more of Groban's dewy, supple vocals set to David Foster's cinematic orchestrations [...] While most of the productions
```

### Album 89, chunk 2

```text
here should appeal to longtime fans of Groban's particular classical-crossover sound, some cuts like soft rock inflected "It Came Upon a Midnight Clear" and the Celtic folk leaning "Little Drummer Boy" do expand upon the Groban/Foster palette in a pleasing way". BBC Music critic Michael Quinn felt that Noël was "as perfect a yuletide present as Groban could have given his fans". Seven weeks after its release, Noël reached No. 1 on the U.S. Billboard 200 on the chart dated December 8, 2007. The album sold about 405,000 copies in the week it reached number one, rising from the number two position with an 81% sales increase. The week's sales corresponded to an appearance by Groban on The Oprah Winfrey Show during the highly anticipated annual Oprah's Favorite Things feature. In the next week, the album stayed at No. 1 on the Billboard 200 and its sales increased further, by 33%, with 539,000 copies being sold that week. In its 9th week, the album held the top spot with another 8% increase in sales, moving 581,000 copies, and increased yet again in its tenth week selling 669,000 copies, and again holding the number one spot. The album has set numerous Billboard 200 records, starting with being the first Christmas album to spend four consecutive weeks at No. 1 in the chart's 51-year history, as well as being only the second Christmas album to ever spend four weeks at No. 1, tying with Elvis Presley's Elvis' Christmas Album. It is also
```

### Album 89, chunk 3

```text
the first album to spend four consecutive weeks at No. 1 and experience a sales increase each of those weeks since No Doubt's Tragic Kingdom album did so in December 1996. The 669,000 copies the album sold in its tenth week was the biggest single week tally for a Christmas album since Kenny G's Miracles: The Holiday Album sold 819,000 copies in the Christmas week of 1994. By its tenth week the album had already become the best selling album of 2007, scanning 2.8 million copies in only a little over two months of release, a rarity in the fast declining physical album market of the past few years. In its 11th week it became the first album of 2007 to hold No. 1 for 5 weeks, and the first Christmas album ever to hold No. 1 on the Billboard 200 for 5 weeks in a row. In that fifth week at No. 1 it outsold Mary J. Blige's Growing Pains, selling about 757,000 copies. As of December 2022, Noël has sold a total of 6.32 million copies in the United States, according to Nielsen Music.
```

## Album 90: Evolution — Boyz II Men

- **album_id:** `b28d3715-c106-4a46-9614-948347516a87`
- **Tags (identification only):** pop, r and b, contemporary r and b, hip hop soul, soul
- **Chunks:** 3 (703 words)

### Album 90, chunk 1

```text
Evolution is the fourth studio album by American R&B quartet Boyz II Men, released on September 23, 1997. It is their final album released on Motown Records. A Spanish language version, Evolución, was also issued. The Spanish edition won the Billboard Latin Music Award for Pop Album of the Year by a New Artist. On August 20, 1997, Boyz II Men held a press conference to talk about their first album since 1994's II. They were under pressure with their last two albums cumulatively selling almost 30 million copies worldwide. With Evolution, they worked with their regular collaborators, including Jimmy Jam and Terry Lewis and Babyface. They appeared on many talk shows including The Rosie O'Donnell Show, The Oprah Winfrey Show, The Tonight Show with Jay Leno, The Vibe Show, The Keenen Ivory Wayans Show and MTV Live. The album was released on September 23, and that night, Boyz II Men signed copies of the album at the Virgin Megastore in New York City. In October 1998, Boyz II Men went to Japan and Europe to promote the album, and during that year they embarked on the Evolution Tour. The first single released from the album, "4 Seasons of Loneliness", was released on September 8, 1997. The song was Boyz II Men's highest debut on the Billboard Hot 100 Singles. It debuted at number two, behind Mariah Carey's "Honey". The following week, the single went to number one, became their fifth (and to date, last) chart-topper. 4 Seasons of Loneliness
```

### Album 90, chunk 2

```text
became Boyz II Men's sixth platinum single. Later that year, the second single, "A Song for Mama", was released, a track which already appeared in film Soul Food and its soundtrack. The single reached number seven on the Billboard Hot 100 and number one on the R&B Singles Chart, making Boyz II Men the only group in history to have seven platinum singles in the United States. AllMusic editor Stephen Thomas Erlewine editor Stephen Thomas Erlewine observed that Evolution "is supposed to capture Boyz II Men in full maturity," but "sounds surprisingly similar to their blockbuster II." He noted that the group focused on "smooth ballads" delivered with "typical grace," yet argued that their "signature sound [was] beginning to sound like a formula" and that they "fail to offer any new twists." Entertainment Weekly's Jeremy Helligar agreed that while Boyz II Men's style remains technically strong, it felt repetitive and uninspired. He remarked that their "harmonies glide ever so smoothly," but dismissed this as "old news," adding that their focus on love and romance makes the album feel like "a quiet storm we've weathered before." Helligar concluded that true artistic growth would require them to "actually entertain us," calling such a shift "evolution." Jon Pareles of The New York Times noted that while Boyz II Men lean on their "image as an old-fashioned vocal group," on Evolution they attempt to be "less wimpy," with songs addressing cheating and denying an ex a second chance. He highlighted their expansion into "electronic
```

### Album 90, chunk 3

```text
soundscapes," but found their efforts to sound lascivious or modern "awkward." Despite some experimentation, Pareles concluded that Evolution remains "nearly as unctuous as the group’s previous multimillion-sellers." Connie Johnson of The Los Angeles Times observed that the group had largely shed their boyishness, with the album showing a move to "put childish things aside," though some tracks were "low on energy." She concluded that Boyz II Men maintained their dignity without begging for love, suggesting that "to go forth and beg no more seems to be Boyz II Men’s first step" toward true evolution. Rolling Stone critic Ernest Hardy argued that despite Evolution’s claims of maturity, Boyz II Men "still sound like boys." He wrote that they "haven't tampered with an iota of their formula," relying on "sappy, sound-alike ballads" and clichéd lyrics. Evolution debuted and peaked at number one on the US Billboard 200 with first week sales of 211,000 copies. It also reached the top of Billboard's Top R&B/Hip-Hop Albums chart, becoming the band's third album to do so. However, the album spent only one week at the number-one spot and quickly fell down the charts. Evolution sold two million copies in the United States and over four million copies worldwide.
```

## Album 91: [The Black Album] — Prince

- **album_id:** `e510665e-1790-411d-a0fa-191cecaebf23`
- **Tags (identification only):** funk, dance rock, minneapolis sound, new jack swing, p funk, pop rap, pop rock, rock
- **Chunks:** 7 (1740 words)

### Album 91, chunk 1

```text
The untitled sixteenth studio album by American recording artist Prince, referred to as The Black Album, was scheduled for release in December 1987 but was canceled at Prince's request after promotional copies had been issued. The follow-up to Sign o' the Times, the album was to appear in an entirely black sleeve with no title or even a credit to Prince; hence it being referred to as The Black Album. Dubbed The Funk Bible by preceding press releases, and in a hidden message within the album itself, the work seemed to be a reaction to criticism that Prince had become too pop-oriented. The album was his attempt to regain his black audience. The 1987 promotional release had no printed title, artist name, production credits or photography printed; a simple black sleeve accompanied the disc. On promotional copies, only a song listing and catalog number 25677 were printed on the disc itself. The commercial version was to only have the catalog number printed in pink on the spine. The original compact disc pressing was made by Sony DADC rather than WEA Manufacturing. After Prince became convinced that the album was "evil", he ordered it to be withdrawn a week before its release date. It was replaced with the album Lovesexy, a brighter pop-oriented album with elements of religious affirmation. The album was officially released on November 22, 1994, by Warner Bros. Records. Prince invoked Camille, the alter-ego behind his unreleased 1986 album Camille, as the guiding force responsible for The Black
```

### Album 91, chunk 2

```text
Album. The opening track also mentioned the title of the album as being The Funk Bible, which was a consideration during work on this project. The title refers both to the album's all-black cover design and to Prince's attempt to earn back his credibility among the black pop audience. The album features one of the most atypical Prince songs: "Bob George", in which he assumes the identity of a profane man who suspects his girlfriend to have had an affair with a man named Bob. He asks her what the man does for a living and learns that Bob manages Prince, whom he dismisses as "that skinny motherfucker with the high voice". The gun-wielding alter ego then fires a multitude of gunshots, and ends up being raided by the police. During live performances of the song during the Lovesexy Tour, he ends up being shot. The name for the track was a combination of Bob Cavallo (former manager), and Nelson George, a critic who was felt to have become very critical of Prince. "Bob George" features a growling monologue that is pitched down (using a Publison) to the point of being almost unrecognizable as Prince. The voice at the end of the song that says "bizarre" is actually a stock sound from the Fairlight CMI IIx library, with its pitch raised, the sample being lifted from the spoken-word track “Our Bizarre Relationship” on The Mothers of Invention's 1969 Uncle Meat album. The Black Album features songs such as the hip
```

### Album 91, chunk 3

```text
hop parody "Dead on It", which playfully makes the accusation that all rappers are tone-deaf and unable to sing, and the playful "Cindy C.", which refers to supermodel Cindy Crawford. The rhyme at the end of the song was originally written by Steve "Silk" Hurley and was included on a song titled "Music Is the Key", which was previously released by Chicago house-music group JM Silk, of which Hurley was the founder. Hurley would later go on to remix two of the songs from the "Gett Off" maxi-single, the Housestyle and Flutestramental versions. The album contains several instances of the portrayal of characters, using either a sped-up or slowed-down vocal track by Prince (as on "If I Was Your Girlfriend", "U Got the Look", "Strange Relationship", and "Housequake", all from the Sign o' the Times album). The instrumental jazz-funk jam "2 Nigs United 4 West Compton" was revisited as a live song on the One Nite Alone... Live! album, but it was hardly the same track. "Rockhard in a Funky Place" was originally considered for inclusion on the Camille project and then the planned Crystal Ball album. After the album's fade out, dissonant feedback fades in, followed by Prince saying "What kind of fuck ending was that?" before fading out again. "When 2 R in Love" is the only ballad on the album, and reappeared on Lovesexy, which was released the next year. Prince performed "Bob George", parts of "When 2 R in Love", and "Superfunkycalifragisexy" on his Lovesexy Tour.
```

### Album 91, chunk 4

```text
"When 2 R in Love" was usually part of the piano medley in Act II, whereas the other two songs were part of the Act I segment, where Prince's evil side showed through (coinciding with the idea that The Black Album was evil). Act II was his "born-again" segment, with more upbeat spiritual songs, highlighting most of the Lovesexy songs, and top 40 hits. Samples of "Bob George" would later show up on the "Dub Beats" official promo mix of Madonna's 1989 single "Like a Prayer". Days before its intended December 1987 release, Prince contacted Warner Bros. chairman Mo Ostin and requested the album's withdrawal. Prince attributed his decision to a "spiritual epiphany" that convinced him the record represented the "anger" and "licentiousness" that the singer had to leave behind. He later blamed the album on an entity named Spooky Electric, described as a demonic, low-voiced alter-ego induced by Camille. The withdrawal decision is rumored to have been influenced by Prince's having a bad experience on MDMA. The record company had to destroy about 500,000 copies of the album which were already on loading docks, ready for shipment to stores. However, a small number of those copies escaped destruction, which made the album available on the bootleg market following its cancellation. Prince would later reference the withdrawal in the music video for the lead single from Lovesexy, "Alphabet St.", where a message quickly scrolls down the screen that reads: "Don't buy The Black Album, I'm sorry." In April 2016, an
```

### Album 91, chunk 5

```text
original promo copy from 1987 was sold on Discogs' marketplace for a then-record of US$15,000.00. In 2017, five copies were discovered in the United States, with one of those selling for US$42,298. In June 2018, another copy of the original album was found in Canada—this copy later sold on the Discogs marketplace for $25,000. The Black Album was finally released by Warner Bros. Records on November 22, 1994—again, containing only a track listing and the new catalog number 45793 printed onto the disc itself, and a copyright date of 1994 (with the exception of "When 2 R in Love", which was released in 1988 on Lovesexy). The sole explicit identifier was a sticker placed on the front case. Although it was released in a strictly limited edition and was deleted on January 27, 1995, the album was re-released exclusively to Tidal in 2016. In the week of the album's official release, Warner ran an ad at the back of the November 26, 1994, issue of Billboard that offered owners of counterfeit copies a free copy of the legal release, provided they mail their bootleg copy to the label in exchange. This offer was given only to the first 1,000 individuals who sent in their copies. Reactions to the 1987 promo release were largely positive. Several celebrities, including U2's The Edge and Bono, cited it as one of their favorite albums of 1988 in a Rolling Stone magazine poll. Robert Christgau, writing in The Village Voice, compared Prince's approach to George
```

### Album 91, chunk 6

```text
Clinton's "sonic wallop and communal craziness", adding that "the bassy murk never lets up, and at its weirdest [...] it's as dark as Cosmic Slop." Commenting on the scarcity of advance-release copies, he recommended that "those who pine for heavy funk should nag their local dealers". The New York Times' Jon Pareles remarked that both The Black Album and Lovesexy "show a musician experimenting like mad with every musical parameter, and so prolific that he has to cut back his output so he won't be competing with himself". He observed that The Black Album "answers the Beatles' eclectic White Album with Prince's own tour of black music styles (from a skeletal, synthesized blues to a rap, with extended stops at James Brown, Sly and the Family Stone and Parliament-Funkadelic); it has black humor and nasty fantasies." Retrospective reviews since the album's limited official release have been more mixed. In one of the few unambiguously negative appraisals, Select's Matt Hall panned the album as "the sound of someone losing step with the times", and was particularly critical of Prince's "embarrassing, bitter rant against hip hop" on "Dead on It". David Browne of Entertainment Weekly believed that The Black Album had not aged well by 1994, writing that "[i]n the pre-gangsta days of 1987, The Black Album was jarring, but now that our ears have become jaded — at times liberated — it sounds downright average", but offered praise for the "spooky, scary, and funny, sometimes all at once" "Bob George". More
```

### Album 91, chunk 7

```text
sympathetically, Stephen Thomas Erlewine of AllMusic opined that the album "isn't a lost masterwork — it's fun, but not much more". He criticized "When 2 R in Love" as "nondescript" and "Dead on It" as "one of the lamest things he ever waxed", but declared that "[t]he rest of the eight-song album is brilliant, pure funk" and "a terrific little record that still delights, even after its mystique has faded". Prince – lead vocals (tracks 1–4, 6, 8), rapping (track 6), spoken word (tracks 2, 5, 7), backing vocals (tracks 1–4, 6, 8), electric guitar (tracks 1–3, 5–6, 8), bass (tracks 1–3, 6–8), Fairlight CMI (tracks 1–3, 5–6, 8), synthesizers (all tracks), E-mu Emax (track 4), Ensoniq Mirage (track 5), Sequential Prophet VS (tracks 5, 8), Yamaha DX7 (tracks 4, 5), Publison IM90 Infernal Machine (track 5), Hammond organ (track 7), drums (tracks 1–2, 5–6, 8), percussion (tracks 2, 6, 8), claps (tracks 2, 8), programming (tracks 1–6) Atlanta Bliss – trumpet (tracks 1–2, 7–8) Boni Boyer – backing vocals (tracks 1–2), claps (track 2) Sheila E. – backing vocals (tracks 1–2), percussion (track 2), claps (track 2), sampled line from "Holly Rock" (track 3) Jill Jones – backing vocals (tracks 1–2), claps (track 2) Eric Leeds – saxophone (tracks 1–2, 7–8), flute (track 8) Susannah Melvoin – backing vocals (tracks 1–2, 8), claps (tracks 2, 8) Cat Glover – rap (track 2), spoken vocals (track 7) Prince – producer
```

## Album 92: Presto — Rush

- **album_id:** `fdffc781-1e3b-4923-a888-6eccc42ec537`
- **Tags (identification only):** progressive rock, hard rock, pop rock, rock, aor, arena rock, symphonic rock
- **Chunks:** 7 (1646 words)

### Album 92, chunk 1

```text
Presto is the thirteenth studio album by Canadian rock band Rush. It was released on November 17, 1989 by Anthem Records and was the band's first album released internationally by Atlantic Records, following the group's departure from Mercury. After the Hold Your Fire (1987) tour ended in 1988, the group members reconvened in December to decide their next step and agreed to take six months off before starting on a new album. Presto marked another change in Rush's sound, with a reduction in synthesizers and a return towards more guitar-driven arrangements. Presto reached No. 7 in Canada and No. 16 in the United States. "Show Don't Tell," "The Pass" and "Superconductor" were released as singles from Presto; the former charted at No. 1 on the U.S. Album Rock Tracks chart. Rush supported the album with the Presto Tour from February to June 1990. Presto reached gold certification by the Recording Industry Association of America for selling 500,000 copies. The album was remastered in 2004 and 2013, the latter as part of the 2013 box set The Studio Albums 1989–2007. In 2015, it was reissued after being remastered by Sean Magee at Abbey Road Studios, following a direct approach by Rush to remaster their entire back catalogue. In May 1988, Rush wrapped up touring the band's previous album, Hold Your Fire (1987), which was followed by the band's third live release, A Show of Hands, in early 1989. The group then decided not to renew contracts with international distributor Mercury Records;
```

### Album 92, chunk 2

```text
Lifeson said they departed because the relationship had become stale by this point. Peart later wrote that with the band now "free of deadlines and obligations" for the first time in 15 years, they chose to take advantage by taking a six-month break. In December 1988, the group gathered at Peart's house to discuss the next step and agreed to start a new studio album after the break. Work on Presto began with Rush renting a studio in the country to write and rehearse new material. They adopted their usual method of Lifeson and Lee working on music while Peart worked alone on lyrics. Peart wrote: "At the end of the day I might wander into the studio, ice cubes clinking, and listen to what they'd been up to, and if I'd been lucky, show them something new." Rush worked at the studio during the week and returned home on weekends. Presto marks the beginning of Rush's return to a more guitar-driven sound from what's known to many as the band's "synthesizer period" of the previous four releases. When Lifeson and Lee discussed what musical direction to take, they agreed that the core of the band's sound, emotion, and energy had come from the guitar, something that they wanted to return to for Presto. This resulted in a much more satisfying album for Lifeson. Lifeson had felt constricted in his guitar playing since synthesizers began playing a more dominant role in the songwriting and performance on Signals (1982), which had
```

### Album 92, chunk 3

```text
continued through the 1980s. Lee explained that Rush wanted Presto to be "more of a singer's album, and I think you'll notice that the arrangements musically support the vocal. [...] Neil's lyrics to me are a lot more heartfelt. [...] This album was a real reaction against technology in a sense. I was getting sick and tired of working with computers and synthesizers. [...] We made a pact to stay away from strings, pianos, and organs—to stay away from digital technology. In the end, we couldn't resist using them for colour." In a contrast to previous albums Grace Under Pressure (1984), Power Windows (1985) and Hold Your Fire, the album does not contain an overall running lyrical theme, or what Peart described as "heavy" lyrical messages, instead adopting a more loose approach with each track making its own statement. Peart used the word "response" to describe the lyrical content as a whole. "The idea that you don't go through life just looking at things. It doesn't matter if you've been all around the world - you may have seen it, but if you haven't felt it, you haven't been there." Peart added: "There are many threads and a strong motif of looking at life today and trying to act inside it." The album's title was an idea that Rush had considered using for A Show of Hands, but when Peart started writing a song entitled "Presto", it was then used as the title of the album. After several songs had
```

### Album 92, chunk 4

```text
been worked out, the band felt it was the right time to present what they had to a co-producer. However, their initial choice, Peter Collins, who'd worked on Power Windows and Hold Your Fire, reluctantly declined the offer to work on Presto, as he wished to produce other bands. Though Rush felt confident enough to undertake production duties themselves, they still wanted someone they could trust and to provide an objective point of view to their ideas. Among the various candidates was English producer, songwriter, and keyboardist Rupert Hine, whose experience with a variety of artists attracted the group. Peart recalled the time when they presented their ideas to Hine: "We were a little bemused [...] at the end of some of them he actually seemed to be laughing! We looked at each other, eyebrows raised as if to say: 'He thinks our songs are funny?' But evidently it was a laugh of pleasure; he stayed 'til the end". At Hine's suggestion, the group brought in Stephen W. Tayler as the recording and mixing engineer. The sessions with Rush and Hine together were productive; initially, 10 days were assigned for pre-production work with one track for each day, but it was complete after just one-and-a-half days. Presto was recorded from June to August 1989. As part of their deal with Hine, the band agreed to record parts of the album in London. Presto was finished around four weeks ahead of schedule. When the album was complete, Rush sought a new
```

### Album 92, chunk 5

```text
record deal and signed to Atlantic Records after executive Doug Morris, who had wanted to sign the group for a number of years, made an attractive offer. Presto continues the treble-heavy, light progressive rock of Rush's previous two studio albums. "The Pass" concerns a friend of Peart's who joined him on a cycle ride and once discussed juvenile suicide, which inspired the lyrics for the song. Peart named it the song he had worked the hardest on, due to the delicate nature of the subject. The song became a group favorite; Peart cited the track as the reason they would re-record the Presto album, if they could. "Scars" features a complex drum pattern in which both acoustic and electronic drums are utilized. The pattern was derived from a tribal rhythm Peart heard while on a bicycle tour of Africa (later chronicled in his first book, The Masked Rider: Cycling in West Africa). He went on to incorporate this pattern into his live drum solos. The song also features the use of a sequencer in place of, and often mistaken for, a bass guitar. Lifeson said the title track is about "feeling more active in your heart than in your head, not having the answers to problems." "Superconductor" deals with the superficiality of mainstream music. That topic also appears in other songs such as "Grand Designs" from the Power Windows album. In "Anagram (for Mongo)", every line contains one or more words that are formed by using letters in another word
```

### Album 92, chunk 6

```text
from that same line (e.g. "There is no safe seat at the feast"), and certain lines contain anagrammed words (e.g. "Miracles will have their claimers"). Its title was inspired by the character Mongo from the 1974 film Blazing Saddles. Lifeson spoke about the lyrics: "It doesn't mean anything, it was just a fun thing, but there are some great twists in there." "Hand over Fist" was originally an instrumental that Rush had intended to include on Presto, but Peart continued to submit lyrical ideas to Lifeson and Lee; one in particular fit the music well enough and the plan for an instrumental was scrapped. In the album's tour book, Peart used the symbolism that the hand game "rock, paper, scissors" represents, which was made into a nursery rhyme and used as a lyrical chant in "Hand over Fist." The album's sleeve was designed by Rush's longtime collaborator Hugh Syme: a black-and-white design depicting a levitating magician's hat on a hill with a rabbit emerging from it. The field in the foreground has many rabbits. Rush had devised its concept and presented it to Syme, who then produced several ideas depicting what they suggested. Lifeson recalled the moment when they saw the design they went with: "We all started laughing hysterically, 'This is great, it's perfect!'" Rush produced three music videos for Presto: "Show Don't Tell", "The Pass" and "Superconductor". Presto received mixed reviews from critics. Gregory Heaney of AllMusic described the album as "workmanlike" and removed from the creativity of
```

### Album 92, chunk 7

```text
their earlier works. However, he asserted that the songs weren't terrible, just that something was not quite clicking, perhaps due to the length of time it had been since the band wrote more-traditional, guitar-based songs. However, before Heaney's review was posted, the site had listed a favorable 4.5 star (out of a possible 5) review of the album by Mackenzie Wilson, who described the album as one that "intelligently leads Rush into the '90s without musical bleakness". Geddy Lee – bass guitar, vocals, synthesizers Alex Lifeson – electric and acoustic guitars Neil Peart – drums, electronic percussion Rupert Hine – additional keyboards and backing vocals Jason Sniderman – additional keyboards Rush – production, arrangements Rupert Hine – production, arrangements Stephen W. Tayler – recording engineer, mixing Andrew MacNaughtan – portraits Ray Danniels, SRO Productions – management Moon Records (Val Azzoli and Liam Birt) – executive production
```

## Album 93: Frampton Comes Alive! — Peter Frampton

- **album_id:** `dbc7e329-59b9-4d37-9f6d-db104fa622aa`
- **Tags (identification only):** rock, album rock, pop rock, pop, aor, hard rock
- **Chunks:** 3 (797 words)

### Album 93, chunk 1

```text
Frampton Comes Alive! is a double live album by the English musician and songwriter Peter Frampton, released in 1976 by A&M Records. Following four studio albums with little success and sales, Frampton Comes Alive! was a breakthrough for Frampton and is one of the best-selling live albums ever. "Show Me the Way", "Baby, I Love Your Way", and "Do You Feel Like We Do" were released as singles; all three reached the top 10 in Canada and the top 15 on the US Billboard Hot 100, and frequently receive airplay on classic rock radio stations. Released on 15 January 1976, Frampton Comes Alive! debuted on the charts at No. 191. It reached No. 1 on the Billboard 200 the week ending 10 April 1976, spending 10 non-consecutive weeks in the top spot through October. It was the best-selling album of 1976 and has sold over 8 million copies in the United States. Frampton Comes Alive! was voted "Album of the Year" in a 1976 Rolling Stone readers' poll. It stayed on the chart for 97 weeks and was still No. 14 on Billboard's 1977 year-end album chart. It was ranked No. 41 on Rolling Stone's "50 Greatest Live Albums of All Time" list. Readers of Rolling Stone ranked it No. 3 in a 2012 poll of all-time favourite live albums. In 2020, Frampton Comes Alive! was inducted into the Grammy Hall of Fame. The album Frampton Comes Alive! was recorded between June and November 1975, primarily at the Winterland Ballroom
```

### Album 93, chunk 2

```text
in San Francisco as well as Marin Veterans' Memorial Auditorium in San Rafael, California, Long Island Arena in Commack, New York, and a concert on the SUNY Plattsburgh campus in Plattsburgh, New York. The Winterland songs were recorded on a 24-track recorder. Other concerts were captured on 16-track recorders. Recordings from four shows were used for the original album. Master tapes were recorded at 15 inches per second using professional Dolby "A" noise reduction. The live album had been intended to be a single LP disc, but at the suggestion of A&M Records, additional shows were recorded, and the album expanded to two LPs for release. On the special features for the Live in Detroit concert DVD, Frampton commented that some difficulties were encountered in mixing after the cable to the bass drum microphone was inadvertently pulled, causing the microphone to face at a 90-degree angle from the drumhead. During the concerts, Frampton principally used a distinctive modified black 1954 Gibson Les Paul Custom electric guitar (with three Humbucker pick-ups as opposed to the usual P90 and AlNiCo Staple pickups). On the radio program In the Studio with Redbeard, Frampton said, "The album is mostly live except for the first verse of "Something's Happening", the electric rhythm guitar on "Show Me the Way" (the talk-box came out but the engineer forgot to move the mic) and the intro piano on "I Wanna Go to the Sun" were fixed in the studio but the rest was all live (all the guitar
```

### Album 93, chunk 3

```text
solos, acoustic guitars, electric keyboards, drums, bass guitar and rest of vocals)". The double album was released in the U.S. at a reduced list price of $7.98, only $1.00 more than the standard $6.98 of most single-disc albums in 1976. It was pressed in "automatic sequence", with sides one and four on one record and sides two and three on the other. This arrangement facilitated sequential listening on automatic record changers. The album produced three hit singles: "Baby, I Love Your Way", "Do You Feel Like We Do", and "Show Me the Way". The talk box guitar effect became closely associated with Frampton due to its use in the latter two singles. The single version of "Do You Feel Like We Do" was edited to 7:19 from the original 14:15 album version, making it one of the longest singles to reach the top 40, surpassing The Beatles' "Hey Jude" at 7:11. The B-side of "Do You Feel Like We Do", the acoustic instrumental "Penny for Your Thoughts", was the shortest track on Frampton Comes Alive, at 1:23. In January 2001, a 25th Anniversary Deluxe Edition of the album was released. It featured four additional tracks not present in the original version, one recorded in a radio studio and not part of the main concert program. The track sequence was revised to more accurately reflect the original concert set list. Frampton produced the remixed and extended album and performed live with the original band at Tower Records in Los Angeles to promote the release. Peter Frampton – lead vocals, lead guitar, talk box on "Do You Feel Like We Do" and "Show Me The Way" Bob Mayo – rhythm guitar, piano, Fender Rhodes electric piano, Hammond organ, vocals Stanley Sheldon – bass, vocals John Siomos – drums, percussion
```

## Album 94: Phanerozoic II: Mesozoic | Cenozoic — The Ocean Collective

- **album_id:** `f0f08b65-c428-4c28-a815-85edf61cdb86`
- **Tags (identification only):** progressive metal, atmospheric sludge metal, post metal, rock, sludge metal
- **Chunks:** 3 (570 words)

### Album 94, chunk 1

```text
Phanerozoic II: Mesozoic / Cenozoic is the eighth studio album by German post-metal band the Ocean. It was released on 25 September 2020 and is the second part of a concept album series exploring the Phanerozoic geological eon, the first part being Phanerozoic I: Palaeozoic, which was released in 2018. The first two track titles each reference a period of the Mesozoic era, whereas the remaining six each reference a period of the Cenozoic era. Two songs from the album were released in advance; "Jurassic | Cretaceous" which features guest vocals by Katatonia's Jonas Renkse, and "Oligocene" with its own animated music video. The video was partly shot in the Aragats mountains in Armenia during The Ocean's "Siberian Traps" tour in Summer 2019. Founding guitarist Robin Staps said, "We found this place by accident: the dilapidated ruins of a soviet observatory & research station for cosmic radiation. The building itself looked like a spaceship that had crash-landed up high in the mountains, but there were lots of interesting structures scattered across the landscape: concrete cubes, underground tunnels, rusted machinery, fallen power poles and watchtowers. It all looked like taken straight out of Andrej Tarkovsky's 'Stalker' movie." Discussing the album's sound, Staps stated, "Phanerozoic II is more experimental, more eclectic in musical style and direction, and more varied in terms of tempos, beats, guitar work and the use of electronics. This was an intentional choice: We wanted Part I to feel rather streamlined and to have a strong cohesion between the
```

### Album 94, chunk 2

```text
individual songs. We wanted to create a certain vibe to linger from the first until the last note throughout the whole record. We kept the weirder, more daring and more progressive material for Part II." In reference to the album's concept Staps explained, "Though humanity is only a very recent phenomenon in the 541 million years history of the Phanerozoic eon, the lyrics are obviously written from a human perspective. They are following Nietzsche's philosophical idea of amor fati in the light of the larger themes of Eternal Recurrence, and the inevitability of an imaginary impending collision on a planetary scale, which are the two red threads that go through Phanerozoic I and II." Besides Jonas Renkse, another guest in this album is Tomas Hallbom, former vocalist of Swedish post-metal band Breach. Being thrilled about his involvement, Staps said, "Breach were one of the most important bands for me, not only with their milestone album Kollapse, which was basically the invention of what people refer to as post-metal nowadays long before this term was ever coined, but also It's Me God (1997) and especially Venom (1999) - they changed my view on music and guitar playing entirely. Breach were different from everything and everyone else around at that time and it's an honour to have Tomas continue the tradition to guest on our albums for the fourth time now." Staps concluded about the future for The Ocean, "We're always striving to get out as much as we can. And as
```

### Album 94, chunk 3

```text
far away as we can, to bring our music and our lives to the last frontiers which remain in a world where the last square inches of free spaces have been Google-mapped to a frightening high resolution and level of detail." Jonas Renkse's guest vocals on "Jurassic | Cretaceous" were praised specifically by several reviewers among other guests. Metal Hammer named it as the 29th best metal album of 2020.
```

## Album 95: Long Way Down — Tom Odell

- **album_id:** `79f073cd-0d23-4ac1-b79a-0aa7dc7eb02a`
- **Tags (identification only):** folk, pop, indie pop, 5+ wochen, english, indie rock, offizielle charts, piano rock
- **Chunks:** 3 (685 words)

### Album 95, chunk 1

```text
Long Way Down is the debut studio album by British singer-songwriter Tom Odell. It was released on 24 June 2013 and serves as the follow-up to his 2012 extended play, Songs from Another Love. It serves as his first release with a major record label, and was released with Columbia. In early 2012, Odell announced that he had signed to Columbia and began recording his debut album later on in 2012. In November 2012, Tom Odell released his first EP Songs from Another Love for which included famous hit "Another Love", which Odell released an official video on his VEVO. Odell came in to RAK Studios in St Johns Wood with producer Dan Grech-Marguerat to record the album in the summer of 2012. Odell announced that his first single from the album would be "Can't Pretend" which was released worldwide on 6 March 2013. It was later announced the second single to come from the album was "Hold Me". Odell performed "Hold Me" and "Can't Pretend" on both Alan Carr: Chatty Man and The Jonathan Ross Show. In December 2012, Odell announced that the title of his debut album would be Long Way Down. In addition, he also unveiled its artwork and release date of 16 April 2013, however, due to its scheduled U.S. release date it was pushed back until 24 June 2013 to prevent the leak of the album across the rest of the world. He also announced the track listing which included "Another Love", "Can't Pretend" and
```

### Album 95, chunk 2

```text
"Hold Me". To promote the album, Odell went on two tours. The first was a smaller, mini-tour which took place in March 2013, three months before the album's release; the second tour takes place in autumn 2013. In 2012 Odell appeared as an opening act for Jake Bugg on the UK leg of his tour in November 2012. Upon release, Long Way Down received mixed reviews from critics. On Metacritic, which assigns a rating out of 100, the album received an average score of 58 based on 14 reviews by mainstream critics. NME gave the album 0 out of 10, prompting Odell's father to complain to the magazine. In the Spring of 2025, Odell's bonus track song "Heal" from the Long Way Down Deluxe Edition, became revisited in the United States and across the world when American Idol (season 23)/(8 on ABC) contestant and eventual winner Jamal Roberts covered the song during "Iconic Idol Moments" week and during the finale episode. The gospel-soul rendition of Jamal's performance went viral over the internet and social media as the defining moment of the competition for Roberts. Odell expressed in a KTU 103.5 interview while discussing the topic of songwriting, storytelling and remixing, that he had seen the video of John Roberts performance online and was inspired, stating: "It made me cry, he does this version of 'Heal', a song that I wrote when I was 20 years old...and I watched this on YouTube....and for me...that is why I do this!", expressing why
```

### Album 95, chunk 3

```text
he enjoys songwriting. Odell later gave his blessing to Jamal Roberts to release the new cover version of "Heal" as a single, which hit #1 on Apple iTunes top 100 the same week it was released after Roberts' win. Odell's version of "Heal" was featured as the ending credits song on the 2014 film If I Stay and If I Stay (soundtrack). In an audio commentary of the soundtrack with WaterTower Music, filmmaker of the film R.J. Cutler stated they needed a song to: "help the audience transition from the intensity of the final moments of the film, while also resonating lyrically and tonally with the story, for weeks we listened to songs trying to find the right one, we had almost given up...when our music department...came with bunch a new options...we listened, but it didn't work, and then we put on Tom Odell's 'Heal', it was so perfect I couldn't believe it". The song later on, made emotional break appearances on the 2018 film The Miracle Season and television series such as The Vampire Diaries (season 7, episode 17) and 9-1-1 (season 8 finale).
```

## Album 96: Children of the Future — Steve Miller Band

- **album_id:** `1b83a275-2141-4397-89d4-fe552cc72bfa`
- **Tags (identification only):** blues rock, rock, psychedelic rock, pop rock
- **Chunks:** 4 (979 words)

### Album 96, chunk 1

```text
Children of the Future is the debut studio album by the Steve Miller Band, released in April 1968 by Capitol Records. Contributed by several writers, the songs on the album include a mixture of blues and psychedelic rock. The album was produced by British record producer-engineer Glyn Johns. It reached number 134 on the Billboard 200 album chart. Steve Miller Band had formed in November 1966, shortly after Steve Miller moved to San Francisco, and quickly became fixtures on the ballroom scene; they eventually appeared at the Monterey International Pop Festival in June 1967. They attracted the attention of multiple record companies and eventually signed with Capitol Records in November 1967 for a then unprecedented $60,000 advance. The money allowed them to choose where they wanted to record, so Miller picked Olympic Studios in London and asked for engineer Glyn Johns. Before that, the group spent time during November and December 1967 at Columbus Recorders in San Francisco recording preparatory demo tapes where Miller experimented with electronic sounds, combining them with the group's blues-rock base. As keyboardist Jim Peterman recalled, "Steve was already working with pre-recorded sound tapes and electronic music in October/November ’67 and was listening to Stockhausen, John Cage and The Beatles...The rest of the band wasn’t really into it. It just really caught a hold of Steve. His direction then, right before we were getting ready to get that first album’s material together, the change in sound and style that we had, it was developing into the
```

### Album 96, chunk 2

```text
sound that was on the first record - Children of The Future." Some of the songs had been written earlier, when Miller was working as a janitor at a Texas music studio in the summer of 1966. Children of the Future is the first of two Steve Miller Band albums to feature guitarist/vocalist Boz Scaggs before he embarked on a successful solo career. Recording sessions took place at Olympic Studios starting January 29, 1968 after the group had arrived to England by boat on the SS United States. The next four weeks were spent recording with Miller producing, but the sessions were haphazard until Johns threatened to quit unless he could help produce the album himself. Miller conceded and the bulk of the material was recorded smoothly over the final two weeks. Miller would later say of working with Glyn Johns: We had to pretty much keep him off the record. Keep him from playing bass, keep him from playing rhythm guitar, from playing the tambourine. I argued with him all the time. I learned a lot from Glyn about making records. The difference between the English and the Americans was the Americans were all conservative, they didn’t like loud amplifiers or big drums or any of that stuff. They were into making pop records. When you went to London they had a Marshall stack, they wanted you to turn it up, they wanted it to sound like rock ’n’ roll. They had the microphone 15 feet away from the
```

### Album 96, chunk 3

```text
amplifier. There was a crazy guy at the console saying "Let’s see if we can make it sound badder". It was great. We got there and Glyn was all of that. I had a lot of arguments with him about too much echo on the records. I was into Otis Redding and the Stax sound, I liked a lot of dry presence and soul. We argued about the sound of the guitars, the sound of the record. We really argued about electronics. He didn’t like any electronic sound glosses, he thought that was all bullshit. I had to really force him to do that stuff and fight for it. On February 26, 1968 the entire band and their entourage (except Miller himself) were involved in a drug bust at their London home, when a Scotland Yard dog smelled hash in a package addressed to the group. The group were fined and given a one year probation on narcotics charges, but were allowed to finish recording the album. Their work visas, however, were canceled which meant that a series of UK dates the group had planned to play over the next few weeks after recording had to also be canceled. On the same day as the drug bust, Miller's childhood friend Ben Sidran arrived to work on the record. He ended up playing harpsichord on Boz Scaggs' "Baby's Callin' Me Home", a song Scaggs had written about his world travels which was recorded with only himself, Sidran and Johns in the
```

### Album 96, chunk 4

```text
studio. Although there was concern that the song wouldn't fit in with the rest of the album, Miller allowed it. The album was finished in mid-March, whereupon the group made a brief stopover in France before returning to America. Children of the Future was released in May 1968 with a front cover design by famed San Francisco poster artist Victor Moscoso but underperformed on the charts when it peaked at number 134. Reviews were positive: Rolling Stone described the first side, which plays as a single continuous track (subtitled Children of the Future), as being "constructed like Sgt Pepper, a coherent whole of individual pieces, with a dominant verbal theme (philosophical without pretentiousness)". Writing in Crawdaddy!, Peter Knobler called the album "a triple moment of experience, knowledge, inspiration". San Francisco Chronicle opined that "the album is beautifully recorded and there is a surprising sweetness to it which the Miller band never evidenced prior to its London visit. The tunes and performances are good and there are some interesting electronics employed and the band swings. The blues tracks are smoother than the band usually sounds but the whole thing is quite good, even if it is a little more British than the Miller band ordinarily is." Steve Miller – guitar, vocals Boz Scaggs – guitar, vocals Lonnie Turner – bass guitar Jim Peterman – Hammond organ Tim Davis – drums
```

## Album 97: Revenge — Eurythmics

- **album_id:** `8e09b6bc-9c6f-48a3-8c54-1527bb96b215`
- **Tags (identification only):** contemporary pop/rock, pop, electronic, pop rock, synth pop, dance rock, new wave, rock
- **Chunks:** 2 (352 words)

### Album 97, chunk 1

```text
Revenge is the fifth studio album by the British pop duo Eurythmics, released on 30 June 1986 by RCA Records in the United Kingdom and on 14 July in the United States. Building on the sound of their previous album, Be Yourself Tonight (1985), Revenge saw the duo further embrace a more "rock band" style. The album spawned four singles and was a commercial success. The single "Missionary Man" won the 1987 Grammy Award for Best Rock Performance by a Duo or Group with Vocal. In the band's native UK, at the 1987 Brit Awards, Dave Stewart won the Brit Award for British Producer of the Year (his second of three awards in the category) and the band were nominated (for the third time) for the Brit Award for Best British Group. The album's release was supported by an extensive world tour; a 1987 concert from the Australian leg of the tour was later released on home video as Eurythmics Live. On 14 November 2005, Sony BMG released remastered versions of each of Eurythmics' eight studio albums, containing bonus tracks and remixes. The bonus track "Revenge 2" is a radically different remake of "Revenge", the closing track of the duo's 1981 debut album In the Garden. A line from the song ("She said revenge can be so sweet") is also heard at the end of "A Little of You". Annie Lennox – vocals David A. Stewart – guitar (all tracks); vocals (tracks 4, 5, 9, 10) Patrick Seymour – keyboards
```

### Album 97, chunk 2

```text
Clem Burke – drums Jimmy "Z" Zavala – harmonica (tracks 1, 2, 4, 6); saxophone (tracks 2, 3, 6, 9, 10) Jannick Top – bass guitar (tracks 1, 6) Joniece Jamison – backing vocals (tracks 1, 6, 7, 9) Michael Kamen – orchestra arrangement, conducting (tracks 1, 3, 5, 8, 10) John McKenzie – bass guitar (tracks 2, 3, 5, 7, 8) Bernita Turner – backing vocals (tracks 2, 9) Phil Chen – bass guitar (tracks 4, 10) Jon Bavin – additional keyboards (track 5) Gully – synthesiser guitar noise (track 5) David A. Stewart – production Eric Scott – sleeve paintings
```

## Album 98: In Our Heads — Hot Chip

- **album_id:** `d833250d-1204-4fdb-ae9e-18eab237be59`
- **Tags (identification only):** electropop, synth pop, alternativa, alternative dance, dance pop, indietronica
- **Chunks:** 3 (740 words)

### Album 98, chunk 1

```text
In Our Heads is the fifth studio album by English synth-pop band Hot Chip, released on 6 June 2012. It is the band's first album to be released by Domino. It was recorded in a span of five months at English producer Mark Ralph's Club Ralph studio in London. The promotional single "Flutes", for which a video debuted on 15 March 2012, was made available as a free download when pre-ordering the album through Domino. A limited-edition 12-inch vinyl of the song was eventually released on 2 April 2012. "Night & Day" was released as the album's lead single on 4 June 2012. Prior to that, the Daphni mix of the song was released as a limited-edition 12-inch vinyl on Record Store Day on 21 April 2012. "How Do You Do?" and "Don't Deny Your Heart" were released as the album's second and third singles on 10 September and 26 November 2012, respectively. In Our Heads received generally positive reviews from music critics. At Metacritic, which assigns a normalised rating out of 100 to reviews from mainstream publications, the album received an average score of 79, based on 40 reviews. Heather Phares of AllMusic viewed In Our Heads as one of Hot Chip's "most confident, joyous, and danceable albums yet", as well as the band's "most direct album yet, delivering their quirks and grooves with bigger, broader strokes that don't feel dumbed down". The Guardian journalist Alexis Petridis opined, "No matter where the music on In Our Heads ventures [...]
```

### Album 98, chunk 2

```text
it never feels forced. There's a similar subtlety in the songwriting, which is deeply idiosyncratic without smashing you over the head with its quirkiness." Sean Thomas of Drowned in Sound stated that In Our Heads is "arguably [the band's] consistent record to date", adding that "[t]he over riding result is that Hot Chip now seem infinitely more comfortable and competent in their skins." In a review for PopMatters, Brice Ezell commented that the album "could be the best thing we've heard from [Hot Chip]", concluding that "In Our Heads is proof that Hot Chip are succeeding on their consistently impressive musical journey, and as far as I can see there's still much to be learned from these songwriters." Larry Fitzmaurice of Pitchfork described In Our Heads as Hot Chip's "most playful and colorful record yet, an album-length manifestation of that 'sounds of the studio' game that cut straight through the middle of 'Shake a Fist'." He continued, "The songwriting is as strong and intricate than on 2006's classic The Warning, even if it takes a few listens for the finer points to sink in." The Independent's Simon Price dubbed the album "their most emotional release yet and also their most philosophical—with the complex, seven-minute 'Flutes' and the cascading arpeggios of 'Let Me Be Him' among the finest things Hot Chip have ever achieved musically." Andy Baber of musicOMH referred to it as "the best album start-to-finish from Hot Chip, one that continues to show their deft range—from infectious disco hits
```

### Album 98, chunk 3

```text
to soulful ballads. It's an impressive return from the quirky five-piece, topping their nearly brilliant fourth album in both scale and ambition." Evie Nagy of Rolling Stone wrote, "There's unguarded joy in the British quintet's mix of synthed-up grooves and pop songfulness on tracks like 'Don't Deny Your Heart'. Their communal vocals are always warm and nuanced, with leader Alexis Taylor merging Davy Jones' innocence with the mirror-ball yearning of Erasure's Andy Bell." However, Slant Magazine's Kevin Liedel felt that the album "feels like a cut-and-paste job, with whole parts either lifted from previous Hot Chip tracks [...] or blatant counterfeits of their '80s-era influences", while stating that "[t]he only reliable human standby amid the parade of dreary automation is Alexis Taylor's voice, which remains as pristine and angelic as ever". Thom Gibbs of NME expressed, "From start to finish, it has an educated and intense eye on the dancefloor, and it sounds fantastic", but concluded by saying, "Lively and upbeat, but naggingly sterile. Tasteful and perfectly executed, but workmanlike." Simon Butcher of Clash dismissed In Our Heads as "an '80s-inspired album lacking in pace", citing tracks like "Motion Sickness", "Night & Day" and "Flutes" as "glimmers of liveliness on an otherwise decedent [sic] record". The album was also included in the book 1001 Albums You Must Hear Before You Die. In Our Heads debuted at number 14 on the UK Albums Chart, selling 9,699 copies in its first week.
```

## Album 99: Made in England — Elton John

- **album_id:** `a5289667-cda9-4971-8442-aa63ccbeaa76`
- **Tags (identification only):** adult contemporary, pop, default, pop rock, contemporary pop/rock, electronic, piano rock, pop rock internacional
- **Chunks:** 3 (640 words)

### Album 99, chunk 1

```text
Made in England is the twenty-fourth studio album by British musician Elton John, released in 1995. It was produced by Greg Penny and John, his first album since Leather Jackets without producer Chris Thomas. The album was dedicated to John's boyfriend and future husband David Furnish. It was also dedicated to the memory of Denis Gauthier and Peter Williams. It was the last album to feature regular Elton John Band percussionist Ray Cooper until 2016's Wonderful Crazy Night. With this album, Bob Birch became John's full-time recording and touring bass player until his death in 2012. The song "Please" was covered by bluegrass singer Rhonda Vincent and country singer Dolly Parton for the 2018 tribute album Restoration: Reimagining the Songs of Elton John and Bernie Taupin. While promoting his work for The Lion King soundtrack in September 1994, Elton John debuted "Believe" (five months before its release as a single) during the opening night of a concert tour with Ray Cooper in Phoenix, Arizona. "Believe" reached No. 15 on the UK singles chart and No. 13 on the US Billboard Hot 100, and was the only American hit from the album to reach the top 20. During November, John toured Brazil, Argentina, Chile, Peru, Switzerland, Poland, France, Italy, the UK, Japan, and other countries two months later. Several songs from the album made it to the subsequent Made in England Tour's playlist, including "Believe," "Made in England," "House," "Blessed," "Lies," and "Pain". On "Belfast," the song originally ended simply with
```

### Album 99, chunk 2

```text
John singing the last line, "Belfast." In an interview with fan magazine East End Lights some time later, arranger Paul Buckmaster (in his first project with John since 1978's A Single Man) said he thought the song needed a more uplifting end, and added the outro, making it sound as if it were being played in an Irish pub somewhere up the road. John reportedly was initially wary of the idea, but Buckmaster said he changed his mind upon hearing it and approved the new coda for the final version. George Martin, who owned AIR Studios London where the album was recorded, wrote the horn and string arrangement on "Latitude." John and Guy Babylon are credited as arrangers on "Man," which also included organ by Paul Carrack. There are many outtakes from Made in England. These songs include "Building a Bird", "Leaves", "Hell", "Skin", "Tick-Tock", "Undone", "Red", "Live Like Horses", an alternate version of "Belfast", and an alternate version of "Believe". "Red" was later released on the French compilation Sol En Si and a version of "Live Like Horses" was later released on The Big Picture. "Building a Bird" was recorded by Nigel Olsson for his 2001 Move the Universe album, released only in Japan. "Hell" and the original cut of "Live Like Horses" have circulated on YouTube. The remaining outtakes have yet to circulate. Elton John – vocals, acoustic piano, keyboards, harmonium, backing vocals (8), string arrangements (9) Guy Babylon – keyboards, programming, backing vocals (8), string arrangements (9)
```

### Album 99, chunk 3

```text
Teddy Borowiecki – accordion (6) Paul Carrack – Hammond organ (9) Davey Johnstone – guitars, mandolin, banjo, backing vocals (8) Bob Birch – bass, backing vocals (8) Charlie Morgan – drums Ray Cooper – percussion Paul Brennan – pipes (6), flute (6) Dermont Crehan – violin solo (6) Paul Buckmaster – orchestral arrangements and conductor (1, 3, 4, 6) George Martin – string and French horn arrangements (7), conductor (7) Gavyn Wright – orchestra leader (6), conductor (9) The London Session Orchestra – orchestra (1, 3, 4, 6, 7, 9) Elton John – producer Greg Penny – producer, mixing Jon Ingoldsby – recording, mixing Chris Bellman – mastering at Bernie Grundman Mastering (Hollywood, California) Adrian Collee – studio coordination Steve Brown – album coordination Pete Mills – drum and guitar technician Bill Harrison – percussion technician John Reid – management
```

## Album 100: Songs About Death & Dying, Vol. 3 — OCS

- **album_id:** `22615286-0565-471f-892c-adad25e58e79`
- **Tags (identification only):** indie folk, psychedelic folk, alternative rock, experimental, garage rock, lo fi, neo psychedelia, rock
- **Chunks:** 1 (168 words)

### Album 100, chunk 1

```text
Songs About Death & Dying: Vol. 3 is the third studio album by American garage rock act Osees, released on May 30, 2005, on Narnack Records. Released under the name, OCS, the album was recorded as a duo by John Dwyer and drummer Patrick Mullins, and features experimental freak folk songs. The album was initially released as a double album, alongside the band's fourth studio album, OCS 4: Get Stoved, and was recorded as a side-project to Dwyer's then-primary band, Coachwhips. In a positive review for Allmusic, Alex Henderson wrote: "Dwyer and colleague Patrick Mullins combine that folk-rock influence with bizarre, experimental electro-noise and a very muffled sound. It's a strange mixture, but a strangely appealing one - and most of the time, it works." John Dwyer - vocals, guitar Patrick Mullins - drums (1, 2, 7, 9, 12), electronics (3, 10, 14), bells (14) Mike Donovan - backing vocals (4) Matt Hartman - clarinet (3) John Dwyer - recording David Benzler - skull Kottie Paloma - girl
```
