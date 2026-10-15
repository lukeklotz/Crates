# Embedding text relevance, batch 6 of 12 (albums 126–150 of 300)

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

This batch: **25 albums, 132 chunks**.

## Album 126: Unleashed in the East: Live in Japan — Judas Priest

- **album_id:** `b2703557-3d52-4e33-8ecb-cae85b3dd580`
- **Tags (identification only):** heavy metal, album rock, british metal, hard rock, new wave of british heavy metal, live, rock
- **Chunks:** 3 (753 words)

### Album 126, chunk 1

```text
Unleashed in the East is the first live album by the English heavy metal band Judas Priest, released in September 1979 on Columbia Records. It was recorded live over two nights in Tokyo during their Hell Bent for Leather Tour in February 1979. Upon release Unleashed became the band's best-selling album up to that point, reaching the US Top 100 and the UK Top Ten, eventually the album became one of the five Judas Priest albums to gain a RIAA platinum certification. It is the first Priest album to be produced by Tom Allom who would remain at the helm for the next decade for the band, and the last release to feature drummer Les Binks. To what extent the album was really live remains a matter of contention, with the album being nicknamed Unleashed in the Studio by some listeners. Years later, after he had left Priest, Rob Halford noted in various interviews that the music was indeed live, but that his vocals had been ruined in the original recording and were later dubbed in a concert-like studio setting. The 2001 CD reissue featured four "bonus tracks", "Rock Forever," "Delivering the Goods," "Hell Bent for Leather" and "Starbreaker", which had been issued on the 7-inch bonus disc that came with the original 1979 Japanese vinyl release. Three of these were from their then-current album Killing Machine (released in the US as Hell Bent for Leather), which was not well represented on the original release. "Delivering the Goods" and "Starbreaker"
```

### Album 126, chunk 2

```text
had been exclusive to the Japanese release, although the former would be one of the B-side tracks to the "Living After Midnight" 12-inch, released in March 1980. These four tracks were previously available on the Japanese pressing of the album (titled Priest in the East and having the same track-list as the remaster), and were recorded at the same time as the original nine tracks. Additionally, two more songs were recorded from the same concerts but were only available as B-sides on various singles: "Evil Fantasies" was on the "Living After Midnight" 12-inch, along with "Delivering the Goods." This live version of "Evil Fantasies" had an official CD release on Single Cuts (2011), albeit with a 6-second edit to the start, which trims Halford's chat slightly. "Beyond the Realms of Death" was pressed with "Rock Forever" and "Hell Bent for Leather" on a special 3 track live EP that came with initial UK pressings of "Unleashed in the East". There is also a 1979 UK cassette version with 12 songs: "Rock Forever", "Hell Bent for Leather" and "Beyond the Realms of Death" in addition to the original 9 tracks. To date, this version of 'Beyond the Realms of Death' has not been released on CD. All the extra songs are fully produced, and are of the same quality as the original nine tracks. Certain bootlegs have turned up with all fifteen tracks in the original setlist order, to better reflect the actual concerts of the 1979 tour. (For the record,
```

### Album 126, chunk 3

```text
all the Unleashed in the East recordings were taken from shows on 10 February 1979 at Kosei Nenkin Kaikan Tokyo, and 15 February 1979 at Nakano Sunplaza Tokyo. Additionally, there were two shows on 10 February: an afternoon and an evening show. The two 10 February shows can be found as a bootleg under the title "Tyranny Unleashed in the East.") Two more songs, "White Heat, Red Hot" and "Take on the World" were performed but never officially recorded. However, the "Take on the World" 12-inch single, released in late 1978, included a live version of "White Heat, Red Hot" recorded at The Agora in Cleveland, Ohio on 9 May 1978 (on the Stained Class Tour). Live versions of "Beyond the Realms of Death" and "Starbreaker" recorded from the same 1978 Cleveland show were released as b-sides to the "Evening Star" 7-inch single and "Take on the World" 12-inch single, respectively. These tracks are available on the Priest, Live and Rare CD. They are not the same versions as on Unleashed in the East. The band was possibly trying to avoid repetition by not including songs on the official full-length live album that were already available as live versions on singles. The Globe and Mail noted that "this absurd piece of bombast was recorded live in Japan and you can pick up every nuance of 120-decibel rock bounding off the audiences' skulls." Rob Halford – vocals K. K. Downing – guitars Glenn Tipton – guitars Ian Hill – bass Les Binks – drums
```

## Album 127: Supermodified — Amon Tobin

- **album_id:** `4bb32d40-91ee-4a0e-88c7-7a35c49cde36`
- **Tags (identification only):** electronic, leftfield, breaks, downtempo, electronica, breakbeat, drum and bass, future jazz
- **Chunks:** 2 (496 words)

### Album 127, chunk 1

```text
Supermodified is the fourth studio album by Brazilian electronic music producer Amon Tobin. It was released on 16 May 2000 by Ninja Tune. Tobin's official website defined the title of the album as: modification: the act of modifying, state of being modified; change made in vowel by mutation, graphic representation of this super: on the top (of); over; beyond; besides; in addition; exceeding; going beyond; more Supermodified was released by the Ninja Tune label on 16 May 2000 in the United States and on 22 May 2000 in the United Kingdom. Two singles were issued from the album: "Slowly" on 1 May 2000 and "Four Ton Mantis" on 4 September 2000. Music videos were produced for both "Slowly" (directed by Ben Rivers and Jeremy Butler) and "Four Ton Mantis" (directed by Floria Sigismondi). In 2012, Supermodified was awarded a double silver certification by the Independent Music Companies Association, signifying sales of at least 40,000 copies in Europe. At Metacritic, which assigns a normalised rating out of 100 to reviews from professional publications, Supermodified received an average score of 85 based on eight reviews, indicating "universal acclaim". Pitchfork critic Taylor M. Clark found it more accessible than Tobin's previous albums, as well as more cohesive: "Everything just fits together so well, like Lego blocks making a castle." John Bush of AllMusic wrote that Tobin had "again made great strides in his production skills, and the range and greatness of this material serves as proof positive." "Natureland", "Slowly" and "Get Your Snack
```

### Album 127, chunk 2

```text
On" were used in the movie coverage of the 2003 Gumball 3000 Rally. "Saboteur" was used in the 2003 remake of The Italian Job. "Slowly" was used in the 2006 film Candy, as well as ES footwear's film, "Menikmati". "Four Ton Mantis" was used in a commercial for "Death Note" on Adult Swim, Paul Rodriguez's "Forecast" skateboarding video for Mike Mo Capaldi's segment, a Molson M commercial. and a commercial for the Nissan Qashqai. "Chocolate Lovely" has been used on Adult Swim's commercial bumps. "Deo" was used in a Coca-Cola commercial. "Get Your Snack On" and "Deo" were used in the 2005 anime "IGPX". "Get Your Snack On" was used in season 8, episode 13 of American Dad!. "Get Your Snack On" and "Four Ton Mantis" have been used in various Toonami bumps. "Rhino Jockey" was used in the movie Project X. "Natureland" was used on Channel 4's TV promotional spot for its Stanley Kubrick season. In a 2017 Facebook post, Amon Tobin confirmed fan speculation that “for reasons beyond my control a number of my albums tracks listings [sic] have been altered on mainstream digital platforms” and that “a small number of my most well known [sic] tracks have also been removed” from streaming services. This is possibly due to sample clearance issues, and includes “Easy Muffin” from Bricolage (1997), and "Four Ton Mantis" from Supermodified. Amon Tobin – production Quadraceptor – beatboxing on "Precursor" She 1 – typography Haig Vartzbedian – recording on "Precursor"
```

## Album 128: Born Again — Black Sabbath

- **album_id:** `836d657d-990e-41aa-a928-5fc51a419768`
- **Tags (identification only):** heavy metal, hard rock, metal, rock, blues rock, classic rock
- **Chunks:** 14 (3311 words)

### Album 128, chunk 1

```text
Born Again is the eleventh studio album by the English heavy metal band Black Sabbath, released on 12 September 1983 in the United Kingdom. It is the only album the group recorded with lead vocalist Ian Gillan, their last with bassist Geezer Butler for nine years, and their final album with drummer Bill Ward. The album has received mixed reviews from critics, but was a commercial success upon its 1983 release, reaching No. 4 in the UK charts. The album also hit the top 40 in the United States. In July 2021, guitarist and founding member Tony Iommi confirmed that the long-lost original master tapes of the album had finally been located, and that he was considering remixing the album for a future re-release. Following the departure of vocalist Ronnie James Dio and drummer Vinny Appice in 1982, Sabbath's future was in doubt. The band switched management to Don Arden, father of Sharon Osbourne who was married to the band's founding singer Ozzy Osbourne. Arden suggested Ian Gillan of Deep Purple as the new vocalist. The band had considered vocalists such as Robert Plant and David Coverdale before settling on Gillan. With Whitesnake on the verge of breaking up, Iommi was eager to form a new group with Coverdale and drummer Cozy Powell joining him and Butler, but Coverdale and Powell decided at the last minute to continue with Whitesnake (the latter would eventually join Black Sabbath in 1988). Iommi has claimed the band received an audition tape from Michael
```

### Album 128, chunk 2

```text
Bolton who was then working in hard rock before finding success as a pop-ballad singer. However, Butler claims no such thing happened and said Iommi concocted the Bolton story as "a joke". This claim has also been refuted by Bolton himself, who clarified that it was "only a rumor" which might have originated from his band Blackjack once opening a concert for Ozzy. Iommi told Hit Parader magazine in late 1983 that Gillan was the best candidate, saying "His shriek is legendary." Gillan was at first reluctant, but his manager convinced him to meet with Iommi and Butler at The Bear, a pub in Oxford. After a night of heavy drinking, Gillan officially committed to the project in February 1983. The following morning Gillan had no memory of joining the band and claimed he didn't even like Black Sabbath's music, but the deal had already been struck. The project was originally intended to be a new supergroup, and the members of the group had no intention of billing themselves as Black Sabbath. At some point after recording had been completed, Arden insisted they use the recognizable Sabbath name, and the members were overruled. Butler reported how Arden had secured a sizable advance from the record company with the proviso that Gillan be involved, and the album issued under the Black Sabbath name. With Cozy Powell electing to remain with Coverdale in Whitesnake, Black Sabbath's longtime drummer Bill Ward was persuaded to return to the band. Ward claimed to be newly
```

### Album 128, chunk 3

```text
sober after leaving the band in 1980 to treat his alcoholism and he assured Iommi and Butler that he was up to recording and touring once again. Ward began drinking at some point during the sessions and returned to Los Angeles for additional addiction treatment once the album was completed, and has remained sober ever since. Ward said he enjoyed making the album, which remains his final studio album with the band. Sabbath began recording in May 1983 at Richard Branson's Manor Studio, in the Oxfordshire countryside. Engineer Robin Black had worked with the band in the mid-1970s on Sabotage and received a co-producer credit on Born Again. During recording, the band members lived at Manor Studio while Gillan chose to live outside the house, alone, in a marquee tent on the studio grounds: "I thought he was joking, but when I arrived at the Manor I saw this marquee outside and I thought, fucking hell, he's serious. Ian had put up this big, huge tent. It had a cooking area and a bedroom and whatever else", said Iommi. Butler said that the tent situation and Gillan's refusal to live with his new bandmates, in hindsight, likely indicated how the vocalist didn't view himself as a member of the band. "Ian's lyrics were about sexual things or true facts, even about stuff that happened at The Manor there and then," Iommi said. "They were good, but quite a departure from Geezer's and Ronnie's lyrics." For example, Gillan returned from a
```

### Album 128, chunk 4

```text
local pub one evening, took a car belonging to drummer Ward, and commenced racing around a go-cart track on the Manor Studio property. He crashed the car, which burst into flames after he escaped uninjured. He wrote the album's opening "Trashed" about the experience. Butler felt that Gillan's lyrics on tracks such as "Digital Bitch" and "Keep It Warm" were good, but much better suited to the musical style of Deep Purple than Black Sabbath. "Disturbing the Priest" was written after a rehearsal space – set up by Iommi in a small building near a local church – received noise complaints from the resident priests. "We wanted this effect on 'Disturbing the Priest'," recalled the guitarist, "and Bill got this big bucket of water and he got this anvil. It was really heavy, and he'd got it hanging on a piece of rope and lower it in to get this effect: hit it and lower it in, and then lift it out again. It was a great effect, but it took hours to do." The band got along well, but it became apparent to all involved that Gillan's style did not quite mesh with the Sabbath sound. In 1992, Gillan told director Martin Baker he was "the worst singer Black Sabbath ever had. It was totally, totally incompatible with any music they'd ever done [and] I think the fans probably were in a total state of confusion." In 1992, Iommi was quoted in Guitar World saying "Ian is a great
```

### Album 128, chunk 5

```text
singer" but generally not well suited for Black Sabbath's material. To the contrary, Ward recalled Gillian worked well in the studio and "delicately put lyrics together. It made sense. I thought he did an excellent job." "I did some of the best drum work on that album…" Bill Ward recalled. "On 'Disturbing the Priest', there were some polyrhythms and some counterpoint things that I was doing, and I was using at least twenty different pieces of percussion towards the end of that song… I was real proud of a lot of the work that I did. Some of it invariably got lost in the mix, but I know that it's printed on those tracks." Butler said that Ward began acting quite strangely during recording and was angrier than he had ever seen him. At one point the drummer began hallucinating and had to be hospitalized, and while he was there the band discovered his secret stash of vodka that he'd been consuming in secret at night. After being released from the hospital, Ward quit the band again and returned to America to sort out his issues, with his drum parts already recorded. When the band heard the final product, they were horrified at the muffled mix. In his autobiography, Iommi explains that Gillan inadvertently blew a couple of tweeters in the studio speakers by playing the backing tracks too loud and nobody noticed. "We just thought it was a bit of a funny sound, but it went very wrong somewhere
```

### Album 128, chunk 6

```text
between the mix and the mastering and the pressing of that album...the sound was really dull and muffly. I didn't know about it, because we were already out on tour in Europe. By the time we heard the album, it was out and in the charts, but the sound was awful." Butler recalled listening to the tapes in his hotel room and being alarmed at how "muffled and unclear" the tracks were, but Iommi and Black assured him that the issue would be corrected during mixing. Ultimately, the issue never was corrected, with Butler lamenting years later that "that's what happens when you don't hire a bona fide producer, like Martin Birch, to handle things." For all his misgivings, Gillan remembers the period fondly, stating in the Black Sabbath: 1978–1992 documentary: "[W]e had a good year...And the songs, I think, were quite good." After Bill Ward had left the band for rehab, drummer Bev Bevan was hired for the subsequent tour. Bevan was a friend of Iommi's who knew Don Arden well, but he was ultimately not a heavy metal drummer and struggled to fit with their musical style. Gillan refused to learn the lyrics to much of the band's earlier material, and this version of Black Sabbath fell apart with Gillan and Bevan quitting. The tour was also a breaking point for Butler, who admits in the Black Sabbath: 1978–1992 documentary, "I just got totally disillusioned with the whole thing and I left some time in 1984 after the
```

### Album 128, chunk 7

```text
Born Again tour. I just had enough of it." In 2015, Butler clarified to Dave Everley of Classic Rock how he wanted to spend more time with his family and young children, but there was no acrimony in his departure. Butler felt Gillan was preoccupied with an upcoming Deep Purple reunion and said Iommi was unhappy when Gillan announced his departure from Black Sabbath, as Iommi thought it had been a long-term arrangement. Disagreements with management also contributed to the band's dissolution. The Born Again album cover – depicting what Martin Popoff described as a "garish red devil-baby" – is by Steve 'Krusher' Joule, a Kerrang! designer who also worked on Ozzy Osbourne's album Speak of the Devil. It is based on a black-and-white photocopy of a photograph published in a 1968 magazine. Joule was said to have deliberately delivered a sub-par cover due to his involvement with and loyalty to the band's former vocalist Osbourne. Butler called the cover "a bit sick, but (Arden) loved it, so that was that." Gillan told the press that he vomited when he first saw the picture. However, Iommi approved the cover, which has long been regarded as one of the worst in rock music history. Ben Mitchell of Blender called the cover "awful". The British magazine, Kerrang!, ranked the cover in second place, behind only the Scorpions' Lovedrive, on their list of "10 Worst Album Sleeves in Metal/Hard Rock". The list was based on votes from the magazine's readers. NME included the
```

### Album 128, chunk 8

```text
sleeve on their list of the "29 sickest album covers ever" and Metal Hammer included it on their list of "50 most hilariously ugly rock and metal album covers ever". Sabbath's manager Don Arden was quite hostile towards the band's ex-vocalist Ozzy Osbourne, who had recently married Arden's daughter Sharon, and was fond of telling Osbourne that his children resembled the Born Again cover. Born Again was released in September 1983 and was a commercial success. It was the highest charting Black Sabbath album in the United Kingdom since Sabbath Bloody Sabbath (1973), and became an American Top 40 hit. Despite this, it was the first Black Sabbath album to fall short of RIAA certification. The album received mixed reviews upon its release. AllMusic's Eduardo Rivadavia wrote that the album has "gone down as one of heavy metal's all-time greatest disappointments" and described "Zero the Hero", "Hot Line", and "Keep It Warm" as "embarrassing". Blender contributor Ben Mitchell gave the album one out of five stars and claimed that the music on Born Again was worse than its cover. Martin Charles Strong, the author of The Essential Rock Discography, wrote that it was "an exercise in heavy-metal cliché". However, PopMatters contributor Adrien Begrand has noted the album as "overlooked". The British magazine Metal Forces defined it "a very good album" even if "Gillan may not be the perfect frontman for the Sabs". Despite the overall negative reception with critics, the album remains a fan favorite. Author Martin Popoff has written
```

### Album 128, chunk 9

```text
that "if any album in the history of Black Sabbath is getting a new set of horns up from metalheads here deep into the new century, it's Born Again." Industrial metal band Godflesh and death metal band Cannibal Corpse both have covered "Zero the Hero", the former appears on the Masters Of Misery - Black Sabbath: The Earache Tribute album while the latter is featured on the Hammer Smashed Face EP. Cannibal Corpse's former singer, Chris Barnes, has called Born Again his favourite Black Sabbath album. "Zero the Hero" has also been cited as the inspiration for the Guns N' Roses hit "Paradise City", and in his autobiography Iommi also suggests the Beastie Boys may have borrowed the riff from "Hot Line" for their hit "(You Gotta) Fight For Your Right (To Party!)". Metallica drummer Lars Ulrich has called Born Again "one of the best Black Sabbath albums". Bill Stevenson, former drummer of Black Flag, stated the band was listening to the album around the time of My War, defining songs like "Trashed" and "Disturbing the Priest" as "ideal". Iron Maiden vocalist Bruce Dickinson has also defended the album, saying "'Born Again' — great album. Everybody goes, 'Oh, forget that one.' No, it's a great album." In 1984, Ozzy Osbourne stated that the album was the "best thing I've heard from Sabbath since the original group broke up". Butler has pointed to "Zero the Hero" and "Disturbing the Priest" as his favorites on the album. Butler has said that while
```

### Album 128, chunk 10

```text
he initially felt that the poor production had spoiled Born Again, upon re-listening to it decades later "it was a lot better than I remembered", saying "If the songs are good enough, you can get away with iffy production." He points to Iommi's riffs and says "Ian's singing is great". In 1992, Iommi confessed to Guitar World, "To be honest, I didn't like some of the songs on that album, and the production was awful. We never had time to test the pressings after it was recorded, and something happened to it by the time it got released." Ian Gillan expressed disappointment in the final production mix of the album, saying that although he did not break his first copy of it, "I threw it out the window of my car. [Laughs]" He also reflected on the touring activity with the band, "I was with Black Sabbath for a year and I sang Ozzy Osbourne songs as well as the songs from Born Again. And I never felt right doing that. It was great — I could sing them okay — but I didn't sound like Ozzy. There was something not quite right." A re-mastered 'Deluxe Expanded Edition' of Born Again was released in May 2011 by Sanctuary Records. It included several live tracks from the 1983 Reading Festival originally featured on BBC Radio 1's Friday Rock Show. Though the release was remastered, it was not remixed due to the inability to locate the original master tapes, as well as
```

### Album 128, chunk 11

```text
Sanctuary not wanting delay the release in an effort to locate said tapes for a remix. In 2021, Tony Iommi confirmed that the original master tapes, long thought lost, had been found and that he was considering remixing them for an eventual release. According to Iommi's autobiography, Ward began drinking again near the end of the Born Again recording sessions and returned to Los Angeles for treatment. The band recruited Bev Bevan, who had played with The Move and ELO, for the upcoming tour in support of the new album. Gillan had all the lyrics to the Sabbath songs written out and plastered all over the stage, explaining to Martin Baker in 1992, "I couldn't get into my brain any of these lyrics...I cannot soak in these words. There's no storyline. I can't relate to what they mean." Gillan attempted to overcome the problem by having a cue book with plastic pages on stage, which he would turn with his foot during the show. However, Gillan did not anticipate the "six buckets" of dry ice that engulfed the stage, making it impossible for the singer to see the lyric sheets. "Ian wasn't very sure-footed either," Iommi writes in his memoir. "He once fell over my pedal board. He was waving at the people, stepped back and, bang!, he went arse over head big time." Gillan also told Birch that it was Don Arden's idea to open the show with a crying baby blaring over the speakers and a dwarf made
```

### Album 128, chunk 12

```text
to look exactly like the demonic baby depicted on the Born Again album cover miming to the screaming. "We noticed a dwarf walking around the day before the opening show...And we're saying to Don, 'We think this is in the worst possible taste, this dwarf, you know?' And Don's going, 'Nah, the kids will love it, it'll be great.'" The tour is most infamous, however, for the gigantic Stonehenge props the band used. Iommi recalls in his autobiography that it was Butler's idea but the designers took his measurements the wrong way and thought it was meant to be life-size. Months later, while rehearsing for the tour at the Birmingham NEC, the stage set arrived. "We were in shock," writes Iommi. "This stuff was coming in and in and in. It had all these huge columns in the back that were as wide as your average bedroom, the columns in front were about 13 feet high, and we had all the monitors and the side fills as well as all this rock. It was made of fiberglass and wood, and bloody heavy." Although it is said that the set is copied in Rob Reiner's 1984 rock music mockumentary This Is Spinal Tap, with the band having the opposite problem of having to use miniature Stonehenge stage props, this is untrue as the movie was filmed in late 1982 and a 20 minute demo of the film also including the Stonehenge scene being made even earlier that same year. In an
```

### Album 128, chunk 13

```text
interview for the documentary Black Sabbath: 1978–1992, Gillan claims Don Arden had the dwarf walk across the top of the Stonehenge props at the start of the show and, as the tape of the screaming baby faded away, fall back "from about thirty-five feet in the air on this big pile of mattresses. And then, 'Dong!' The bells start and the monks come out, the whole thing. Pure Spinal Tap." The band toured Europe first, playing the Reading Festival (a performance that is included on the 2011 deluxe edition of Born Again) and also playing in a bullring in Barcelona in September. Sabbath performed Gillan's hit with Deep Purple, "Smoke on the Water", on the tour, with Iommi explaining in his memoir, "it seemed like a bum deal for him not to do any of his stuff while he was doing all of ours. I don't know if we played it properly but the audience loved it. The critics moaned; it was something out of the bag and they didn't want to know then." In October, the band took the Stonehenge set to America but could only use a portion of it at most gigs because the columns were too high. The set was eventually abandoned. A music video for "Zero the Hero" was also released, featuring performance footage of the band onstage interspersed with scenes involving several grotesque characters performing experiments on a witless young man in a haunted house filled with rats, roosters and a roaming horse. Ian
```

### Album 128, chunk 14

```text
Gillan – vocals Tony Iommi – guitars, guitar effects, flute Geezer Butler – bass, bass effects Bill Ward – drums, percussion Geoff Nicholls – keyboards Bev Bevan – drums (on 2011 Deluxe Edition – disc two, tracks 3–11) Steve Barrett – art assistant Black Sabbath – producer Robin Black – producer, engineer Paul Clark – co-ordination Peter Restey – equipment technician
```

## Album 129: Son of a Son of a Sailor — Jimmy Buffett

- **album_id:** `a6ff40ff-6d9b-4789-9ebf-f3167d3fd3d1`
- **Tags (identification only):** adult contemporary, contemporary pop/rock, reggae, country rock, gulf and western, pop/rock, rock, tropical rock
- **Chunks:** 3 (714 words)

### Album 129, chunk 1

```text
Son of a Son of a Sailor is the eighth studio album by American singer-songwriter Jimmy Buffett. It was initially released in March 1978 as ABC Dunhill AA-1046 and later re-released on its successor label, MCA. Son of a Son of a Sailor reached #10 on the Billboard 200 album chart and #6 on the Billboard Top Country Albums chart. The album was also certified Platinum by the RIAA. Three singles from the album charted including "Cheeseburger in Paradise" (#32 on the Billboard Hot 100), "Livingston Saturday Night" (#52 Hot 100; #91 on the Billboard Hot Country Singles chart), and "Mañana" (#84 Country). Two of the songs on Son of a Son of a Sailor are written by Keith Sykes and the remainder are written by Buffett. "Cheeseburger in Paradise" from the album appears on all of Buffett's major greatest hits collections and is a perennial concert favorite, one of "The Big 8" songs that he has played at almost every concert and which is the namesake of the Cheeseburger in Paradise restaurant chain. Buffett had recorded a significantly different version of "Livingston Saturday Night" for the 1975 Rancho Deluxe soundtrack. The Son of a Son of a Sailor version of the song also appeared on the soundtrack to the 1978 movie FM that featured a cameo appearance by Buffett. Record World said that "Livingston Saturday Night" is "a piece of his usual down home rock beat and good-time lyrics." Record World said that "Mañana" shows Buffett's "sly way with
```

### Album 129, chunk 2

```text
a lyric" and that "Like 'Margaritaville', the mood is easy with a touch of Latin." The New York Times noted that "it may not be desperately important music, but it's very, very pleasant." Jimmy Buffett – vocals, acoustic guitar Steve Goodman – guitar Tim Krekel – guitar Harry Dailey – bass Mike Utley – keyboards Kenneth Buttrey – drums, percussion Greg "Fingers" Taylor – harmonica Norbert Putnam – bass, kalimba, producer Jay Spell – keyboards Harvey Thompson – saxophone Farrell Morris – percussion Billy Puett – recorder, bass flute The Sid Sharp Strings – strings Deborah McColl, Ginger Holladay, Janie Fricke, Larry Lee, Lea Jane Berinati, Penny Nichols – background vocals 1978 saw Buffett begin his own tour with the Coral Reefer Band to support the album, called the Cheeseburger in Paradise Tour, spending March and April playing along the east coast and then the mid-west. June brought California dates which included a few shows opening for Jackson Browne in San Jose and Angels Camp, California. August brought a Florida stadium tour with the Little River Band and the Steve Miller Band along with three shows in Atlanta and Miami which were recorded for the live album You Had To Be There. Jimmy Buffett: Vocals and guitar Barry Chance: Guitar Harry Dailey: Bass and background Vocals Deborah McColl: Background vocals Greg "Fingers" Taylor – Harmonica and background Vocals Jay Spell – Piano Michael Utley – Organ Kenneth Buttrey – Drums The set list changed nightly, mainly with an acoustic set
```

### Album 129, chunk 3

```text
between "Margaritaville" and "Why Don't We Get Drunk"—however, You Had to Be There chronicles some unusual inclusions, such as: "Miss You So Badly" replaces "Mañana"; a new song "Perrier Blues" emerges later in the tour; a rare performance of "The Captain and the Kid" appeared during the acoustic set; and "Cheeseburger in Paradise" was missing. The shows opened with "Son of a Son of a Sailor" and closed with "Tampico Trauma" every night; and the encore typically consisted of "Morris' Nightmare", "Dixie Diner" (Larry Raspberry and the Highsteppers cover) and "Last Line" (Keith Sykes cover) respectively, with "Morris' Nightmare" closing the show only when it debuted in Boston. An average set list: "Son of a Son of a Sailor" "Pencil Thin Mustache" "Wonder Why We Ever Go Home" "Landfall" "Mañana" "Livingston Saturday Night" "Margaritaville" "Grapefruit—Juicy Fruit" (acoustic) "Banana Republics" (Steve Goodman cover) (acoustic) "He Went to Paris" (acoustic) "God's Own Drunk" (Richard Buckley cover) (acoustic) "Why Don't We Get Drunk" (mostly performed with the Coral Reefer Band, but occasionally performed acoustically) "Coast of Marseilles" (Keith Sykes cover) "Cheeseburger in Paradise" "Changes in Latitudes, Changes in Attitudes" "A Pirate Looks at Forty" "Come Monday" "Tampico Trauma" Encore: "Morris' Nightmare" "Dixie Diner" (Larry Raspberry And The Highsteppers cover) Encore 2: "The Last Line" (Keith Skyes cover)
```

## Album 130: C′mon You Know — Liam Gallagher

- **album_id:** `706544ee-b126-4c02-bab7-e5f350f80663`
- **Tags (identification only):** alternative rock, rock, 1–4 wochen, alternative dance, art pop, baggy, britpop, chamber pop
- **Chunks:** 2 (439 words)

### Album 130, chunk 1

```text
C'mon You Know is the third studio album by English musician Liam Gallagher, released on 27 May 2022 through Warner Records. Andrew Wyatt served as the album's primary producer and co-writer. It was preceded by lead single "Everything's Electric", co-written by Dave Grohl, which charted at #18 on the UK Singles Chart, becoming Gallagher's first solo single to reach the UK Top 20. "C'mon You Know", "Better Days","Diamond in the Dark", "Too Good for Giving Up" and "More Power" were also subsequently released as singles. The album was released the same day as Gallagher's second live album Down by the River Thames. Gallagher toured Europe, Oceania and Latin America in support of the album. C'mon You Know received generally positive reviews from critics and became Gallagher's fourth solo album to debut at #1 on the UK Albums Chart, attaining silver certification in its first week, and subsequently being certified gold in 2022. Gallagher announced the album in October 2021, whereupon he stated the song "More Power" was dedicated to his brother Noel, calling it "a naughty little tune" but "lovely". The cover is a photograph of "fans in the pit" at one of Gallagher's shows that was taken at Reading Festival 2021. C'mon You Know received generally positive reviews from critics, with many positive reviews praising its new direction and increased depth. At review aggregator Metacritic, the album received a score from 74 out of 100 based on twelve critics' reviews, indicating "generally favorable" reception. Robin Murray of Clash called
```

### Album 130, chunk 2

```text
it "the broadest of Liam Gallagher's three solo albums, and also the deepest. It's the one in which he learns to bare his soul a little, and accept different influences." Jordan Bassett of NME found it to be Gallagher's "best and most experimental solo album yet", writing that he does not "overthink this third record, which is packed with Summer of Love anthems". Writing for The Independent, Helen Brown opined that "There's so much sheer, on-one attitude in Gallagher's parka pastichery that's hard to resist. His band are on fire with it. Riffs skirling from the guitars. Drums constantly a-quiver. [...] Fans will only need to give this album a couple of spins before they'll be set to sing along in the festival fields." Reviewing the album for Classic Rock, Ian Fortnam called the album "a bit of a cracker, finding a 'repentant' Liam [...] gleefully infuriating his usual detractors (with 'Diamonds In The Dark''s 'Now I know how many holes it takes to...' hook), delivering catnip ballads ('Too Good For Giving Up'), hitting all the right Liam Gallagher buttons ('Don't Go Halfway') and occasionally kicking hand-me-down Stonesy arse".
```

## Album 131: Vespertine — Björk

- **album_id:** `bbeda91f-3bdf-46f5-a332-fce8e22f5b9c`
- **Tags (identification only):** electronic, art pop, abstract, ambient, glitch pop, idm, downtempo, experimental
- **Chunks:** 18 (4435 words)

### Album 131, chunk 1

```text
Vespertine is the fourth studio album by Icelandic recording artist Björk. It was first released on 18 August 2001 in Japan by One Little Indian Records and 27 August 2001 in the United States by Elektra Entertainment. Björk aspired to create an album with minimal and intricate electronic music to evoke an intimate and domestic feeling, in contrast with the louder styles of her previous studio album Homogenic (1997). She enlisted producers such as Opiate, Console and the duo Matmos, and also worked with harpist Zeena Parkins. Production on the album began while filming her role in Dancer in the Dark. Björk composed arrangements with thin-sounding instruments, including the harp, the celesta, clavichord, strings and custom music boxes. Assisted by Matmos, Björk created "microbeats" from various commonplace sounds, such as that of shuffling cards and ice being cracked. Lyrically, the album drew inspiration from Björk's new relationship with Matthew Barney, exploring themes related to sex, intimacy, eroticism, and love. Other lyrical sources include the poetry of E. E. Cummings and British playwright Sarah Kane's Crave. Three singles were released from Vespertine: "Hidden Place", "Pagan Poetry", and "Cocoon". The music videos of the latter two were banned on MTV for their depictions of sexuality. Björk embarked on the Vespertine world tour with Parkins, Matmos, and a choir of Inuit women, where they performed at theatres and small venues in favor of acoustics. The album peaked at number 19 on the US Billboard 200 selling 75,000 copies in its first week and
```

### Album 131, chunk 2

```text
at number 8 on the UK Albums Chart. It was certified gold in Canada, France, and the United Kingdom. Noted for its erotic, intimate mood and sonic experimentation, Vespertine received universal acclaim from music critics, with some considering it Björk's best album to date. The album appeared on several publications' lists of the best albums of 2001 and of the decade, and has been evaluated by many critics to be one of the best albums of all time. Björk had released her previous studio album, Homogenic, in 1997. The album's style differed from her previous two releases, described by her as "very emotionally confrontational and [...] very dramatic". She also described "All Is Full of Love"—Homogenic's closing track—as the first song on Vespertine, as it opposed the rest of the album's "aggressive, macho" aesthetic. Writer and critic Mark Pytlik writes, "Her appetite for thumping techno had been, temporarily at least, subsumed by a desire for stark melodies and minimalist production". In 2000, she starred in Lars von Trier's Dancer in the Dark, and composed its soundtrack, Selmasongs. While she worked on the film, she also began producing her next album, writing new music, and teaming with new collaborators. She has said "Selmasongs was the day job and Vespertine was the hobby". During this time, she also began to use her new laptop to write music, and Vespertine has been retrospectively referred to as "her laptop album". She initially set about making a record with a domestic mood featuring "everyday moods
```

### Album 131, chunk 3

```text
and everyday noises translating into melodies and beats", hence its working title Domestika. Marius de Vries told Sound on Sound that the project was driven by an "overriding aesthetic of being homely and comfortable", which had "all to do with Björk wanting to make a record as a reaction to the wanderings and the pain she experienced making Dancer in the Dark… [and coming back] after you've wandered." Björk's initial idea was also to "celebrat[e] the banalities of everyday life." For example, the title track "Domestica", originally titled "Lost Keys", was meant to be a "gentle, humorous snapshot" of Björk looking for her keys. Her new relationship with artist Matthew Barney, and the stress she experienced while filming Dancer in the Dark, have been referred to as the two major forces that shaped what would become Vespertine. Her relationship with Barney influenced her lyrics, which became more intimate, detailed, and revealing in contrast to her past works. As Björk had to be extroverted during the filming process, the music she wrote for Vespertine also became hushed and tranquil as a way for her to escape. The eventual title change of the record reveals its changing nature. Writer and critic Mark Pytlik notes that, "where [Domestika] signified a focus of extracting magic from the platitudes of everyday life, [Vespertine] [...] suggested a creation of magic through much more powerful forces. In fine style, Björk had set out to write an album about making sandwiches. She'd ended up with an album about
```

### Album 131, chunk 4

```text
making love". A stylistic antecedent was her poem "Techno Prayer", published in Details magazine in July 1996, which would later be used as part of the lyrics of "All Neon Like". It featured thematic ideas such as cocooning and thread-weaving that she would later explore on Vespertine. The earliest sessions took place in Spain with programmer Jake Davies. Björk commissioned Valgeir Sigurðsson to relocate some of his studio equipment from Iceland to Denmark where Dancer in the Dark was being filmed. While living in Copenhagen, she also contacted the electronic musician Thomas Knak (also known as Opiate), after having enjoyed his 1999 album Objects for an Ideal Home. In Iceland, programmers Jake Davies and Marius de Vries joined Björk for a writing session, laying down more tracks, in addition to nine already mixed. Then, she "set up camp [...] during summer" in a New York City loft, and began to work with harpist Zeena Parkins. Much of Vespertine was "composed, crafted and edited" in that loft, in what has been called the "Domestika sessions". Some tracks were recorded as an overdub "on top of a slave mixdown" of the Spanish sessions. "Undo" was written during a two-week session with Knak that January in Reykjavík. Björk recorded her vocals on top of Knak's minimalist rhythmic backbone, and months later she had added a full choir and string section. "Cocoon", also produced by Knak, was one of the last songs to be written for the album; its melody suddenly came to Björk
```

### Album 131, chunk 5

```text
and she contacted him. Knak took it as a chance to make a more minimal track, similar to his own releases. "Heirloom" was based on an existing instrumental track from electronic musician Console's album Rocket in the Pocket (1998), titled "Crabcraft" (which itself samples Orchestral Manoeuvres in the Dark's "Sacred Heart"). Björk contacted Console in early 2000 and they met in London; she then added her vocals on top. During this period, Björk also worked with Bogdan Raczynski on the song "Who Is It", but it did not make the final cut and was subsequently re-recorded for the album Medúlla. Björk said that she worked on Vespertine for three years. As she wanted to write her own songs on music boxes, Björk contacted a music box company requesting transparent acrylic boxes because she wanted the sound to be "as hard as possible, like it was frozen". Björk decided to use sounds that would not be compromised when downloaded from sites such as Napster, such as "microbeat[s]", whispered vocals, the harp, music box, celeste, clavichord, and strings which "ended up being more panoramic textures in the background." For the string and music box arrangements, she used Sibelius scorewriter software. For Vespertine, Björk wanted to make a "microcosmos of thirty or forty beats interacting". To do this, she recorded noises around her house to make beats out of them. Once the songs were almost finished, Björk contacted the duo Matmos, who she considered "virtuosos" in the field, and sent them various songs
```

### Album 131, chunk 6

```text
to work with. They added beats made from the noise of crushing ice and shuffling cards, among others. In her documentary Minuscule, Björk explained that this process consisted of "taking something very tiny and magnifying it up to big", intending to convey the "sensation that you've been told a secret", that is also present in micrographs. Marius de Vries and Björk did much of the sound design on Vespertine with a text-based synthesizer called SuperCollider. De Vries said that typing in commands as opposed to using knobs, "take[s] you in surprising directions." Additionally, Knak used an Ensoniq ASR-10, for "Cocoon". Björk has stated that she wanted the album to sound like "modern chamber music", referring to the times where "the most ideal music situation was in the home, where people would play harps for each other". She also considers Vespertine to be the opposite of her previous studio album Homogenic, the former being an introverted, quiet, winter record; the latter a loud, dramatic, summer record. Björk has also described the album as "more electronic folk music". Critics have classified Vespertine as electronica, art pop, psychedelia, ambient, folktronica, and glitch pop. Music journalists have also noted the experimental nature of the record. The Orlando Weekly wrote that with the album, Björk "[took] her modernist art-pop further into the abstract". According to Joseph Hale of Tiny Mix Tapes, described Vespertine's music as a combination of "psychedelic techno, chamber music, and chorale together into modal constructions that swelled and receded like emotions (or
```

### Album 131, chunk 7

```text
psilocybin)". David Fricke of Rolling Stone wrote "Vespertine is the closest any pop-vocal album has come to the luxuriant Zen of the new minimalist techno". Björk's performance on Vespertine has been described as that of an "art-rock torch singer". Stylistically, Vespertine incorporates elements of both art and dance music. For example, the instrumentation of choir, strings, and harp is suggestive of Romantic art music, while the "synthesised keyboard sonorities, filtering effects and complex percussive sounds" are elements characteristic of dance-based pop. Academic Nicola Dibben wrote that its "classical and dance-based elements" combine "the spiritual and the sensual" allusions of the album. Vespertine is also characterised by "the obsession with sonic traces of analog technology – that is, the pervasive use of loops, static and white noise". Unlike previous albums like Debut and Post, "electronic sounds are the norm, and the acoustic sounds become the interjections." Influenced by the 1999 album New Ancient Strings, a recording of kora duets by Toumani Diabaté with Ballaké Sissoko, Björk said she "messed up the sound of too angelic instruments, like the harp or the glockenspiel" on Vespertine. Björk's voice is used as a supplement to "the complex electronic textures". Her vocals often appear to be recorded close to the microphone and with little treatment, and sung in a sometimes "unstable whisper", conveying a sense of close proximity and reduced space suitable for the intimate lyrics. The album opens with "Hidden Place", which features a soprano section and strings, "over the top of a warm,
```

### Album 131, chunk 8

```text
intimate melody". Michael Hubbard of musicOMH felt the track was reminiscent of Homogenic's "Hunter", but less focused on the beats. NME called it progressive folk, while Drowned in Sound wrote it was electro. Björk sings about "how two people can create a paradise just by uniting", as she intones: "I'm so close to tears/And so close to/Simply calling you up/And simply suggesting/We go to that hidden place". "Cocoon" is "based around an exploratory bassline and beats that sound like fingertips on skin". Discussing the glitch nature of the track, Björk said, "when you take technology and use the areas where it breaks, where it's faulty, you're entering a mystery zone where you can't control it". Lyrically revolving around making love, the song alternates between metaphors like "Who would have known/That a boy like him/Would have entered me lightly/Restoring my blisses", and explicit lines such as "He slides inside/Half awake, half asleep" and "Gorgeousness/He's still inside me". Björk sings a breathy, "whispered, near-cracking falsetto" on the track. "It's Not Up to You" has been described as a "dizzying ballad" and a song that lifts the album upward. Michael Paoletta of Billboard described the track as "melancholy". Its lyrics are about "love for the unknown devices that culminate in 'perfect days'", and "pleas to find beauty in unlikely places". The "caressing lyrics" of "Undo" assure that: "It's not meant to be a strife/It's not meant to be a struggle uphill". Biographer Mark Pytlik wrote that "Undo" is "a reassuring reminder that anything
```

### Album 131, chunk 9

```text
can happen once you let it. If you are in pain, undo it, Björk suggests, no hint of disingenuousness in her voice, over climbing strings and a rising choir". "Pagan Poetry" is a "harp-splashed" song that concerns unrequited love. The track builds slowly, "with Björk wailing over swelling keyboard crescendos", until, at the four-minute mark, "all the music drops away, leaving Björk utterly exposed" as she sings "I love him, I love him/I love him, I love him/I love him, I love him". The song also features "a flotilla of music boxes with an Asian-teahouse touch". The instrumental interlude "Frosti" has been described as "metallic tundra". Its sound stems from a music box, creating an intimate, fairy tale-like effect. "Frosti" fades into "Aurora", while "a warm, faintly crunchy sound" is heard. These are samples of footsteps in the snow—the work of Matmos—re-appropriated as the song's "subtly shifting beat". "Aurora" has been described as "something that appeals to a child-like imagination", and having a "magical and airy quality". In the lyrics, she addresses a Nature goddess, and sings about "literally dissolving with pleasure" as she "prays to become one with… the northern lights". One of Björk's broodiest compositions, "An Echo, a Stain" is underpinned by a creeping choir line and nibbling clicks, and features an "unresolved, ominous tension" that is atypical of her writing style. Most of the song's lyrics speak directly to incidents in Sarah Kane's 1998 dark-themed play Crave, so much so that it was titled "Crave" up to
```

### Album 131, chunk 10

```text
the last minute. "Sun in My Mouth" is an adaptation of E. E. Cummings' poem "I will wade out/Till my thighs are steeped in burning flowers", with an emphasis on the vocal and accompaniment provided by a string orchestra, a harp, and soft electronica. The track's lyrics have been considered a "startling allusion to masturbation", positioned "within the fantasy-like imagery of burning flowers, sea-girls, darkness and the sun". "Heirloom" alters "between what sounds like a samba preset on a vintage Wurlitzer organ and skittering breakbeats, and is decorated with inverted synthtones and analog keyboards". The song's lyrics tell a "fuzzy story" about a recurring dream, while "[likening] the art of singing to swallowing and exhaling 'glowing lights'" as Björk sings: "During the night/They do a trapeze walk/Until they're in the sky/Right above my bed". Film director Harmony Korine wrote "Harm of Will"'s lyrics. The Slate album review noted the minimalist nature of the track, pointing out a lack of hook, beat and melody. It is a slow song, as is the closing track, "Unison". The latter "[contains] a refrain directly inspired by [Björk's] experience in Dancer in the Dark and a healthy dollop of self-effacing humor evoked to counter the balance". It "brings beats and strings together in a final crescendo that also manages to incorporate a little jungle". The cover art, shot by Inez van Lamsweerde and Vinoodh Matadin in Los Angeles, California, is a black and white photograph of Björk lying down on the patterned ground next to
```

### Album 131, chunk 11

```text
a swimming pool, covering her eyes from the sun and wearing the Marjan Pejoski swan dress that she wore at the 73rd Academy Awards in 2001, which caused a media frenzy and was widely criticised. The duo M/M (Paris), known for applying and integrating their work on photographs (so called dessin dans l'image, or "drawings in the picture"), illustrated the cover, featuring a swan and the album's title with feathers. Björk thought swans embodied Vespertine's music, describing them as "a white, sort of winter bird" and "very romantic". Vespertine came with a booklet of M/M (Paris) artwork. Michael Hubbard of musicOMH commented, "the spine of the CD is entirely white, while the rest of the sleeve features innovative photography and artwork". Academic Nicola Dibben has likened Vespertine's artwork and promotion to representations of the Greek myth of Leda and the Swan, emphazising the erotic overtones of both. Vespertine was released later than One Little Indian Records had intended. Originally, the album's release was scheduled for May, but by March it had been put back to August, so as to enable Björk to work on the album's promotion. On 22 May 2001, Björk premiered six songs off the new album in an intimate concert at the Riverside Church in New York City, accompanied by Matmos and Zeena Parkins. Vespertine was released on 27 August, as a double 12" record, CD and compact cassette. To coincide with the release of the album, Björk also released an eponymously titled coffee table book, created
```

### Album 131, chunk 12

```text
by her and edited and designed by M/M (Paris). A second single, Towards the end of 2001, Vespertine was released as a DVD-Audio. The music videos for "Hidden Place", "Pagan Poetry" and "Cocoon" were included in the DVDs Volumen Plus (2002) and Greatest Hits – Volumen 1993–2003 (2002). Together, Elektra, and New York-based independent marketing firm Drill Team, created the Björk Vespertine Syndicate (BVS), a group of 30-plus websites that had exclusive access to non-album tracks, music videos, and concert/rehearsal footage. To promote the album, Björk appeared in various magazines in mid-2001, including: The Fader, Q, Pulse, URB, USA Today, InStyle, Vibe, Us, Nylon, Index, CMJ New Music Monthly and, Spin. Magazines Dazed & Confused and Les Inrockuptibles featured a special issue with texts, photographs, and different CDs issued randomly, each with a different song from the album. The Times issued a Björk special, featuring videos, music, photographs, and a competition to see Björk perform. She also appeared on several TV shows, including: The Rosie O'Donnell Show, The Tonight Show with Jay Leno, Space Ghost Coast to Coast, The David Letterman Show and, Charlie Rose, among others. On 6 August 2001, "Hidden Place" was released as the album's lead single, its music video having premiered in July. It was released as two CDs and a DVD, featuring B-sides "Generous Palmstroke", "Foot Soldier", "Mother Heroic" and "Verandi". The music video for "Hidden Place" was directed by Inez van Lamsweerde and Vinoodh Matadin and co-directed by M/M (Paris). It was shot in
```

### Album 131, chunk 13

```text
London over four days in February 2001. It was originally planned for a song from Selmasongs, but Björk felt the project was more appropriate for Vespertine. The video consists of close-up shots panning around Björk's face, as fluids flow in and out of her facial orifices. M/M (Paris) said that they "wanted to get as close to her as we could, as we all felt she had never been portrayed as the 'real' and beautiful woman she is.", and that the fluids in the video "visualiz[e] all possible emotions pulsating and circulating in her very busy brain. "Pagan Poetry", was released on 5 November 2001 as two CDs and a DVD, featuring a remix by Matthew Herbert, "Domestica", "Batabid", an Opiate remix of "Aurora", and the music video for "Pagan Poetry". Nick Knight, who had previously shot the cover art for Homogenic, directed the music video for "Pagan Poetry". It is about a woman preparing herself for marriage and for her lover, as she sews a wedding dress onto her skin. As she had asked him to make a video about her love life, Knight gave Björk a camcorder and asked her to shoot her own private scenes. Shots of skin being pierced were also recorded with this camera; the people being pierced were five women who "were into subculture and piercings" and Björk herself, who only pierced her ear. This first two-thirds of the video contains a great deal of post-production by Peter Marin, who gave the image its
```

### Album 131, chunk 14

```text
abstract watercolor-like effect. The shots of Björk with her Alexander McQueen topless wedding dress were filmed in super 35 format. The main idea behind the music video was: "to do something with the moving image that was a mirror of what was happening musically". Although the music video has been well received by critics, it was highly controversial and banned from MTV in 2001. "Cocoon", the album's third single, was released on 11 March 2002. Its music video had premiered in February. Once again, the single was released as two separate CDs and a DVD, with "Pagan Poetry", "Sun in My Mouth" and "Amphibian" as B-sides. The music video for "Cocoon" was directed by Eiko Ishioka and was shot in April 2001 in New York City. One of Björk's most avant-garde music videos, it: "plays with minimalist white for both costume and bleached eyebrows, treating Björk as a geisha whose makeup extends over her entire nude body". Red threads emerge from her nipples and circulate between her breasts and nose, finally enveloping her in a cocoon. Björk actually wore a very close-fitting body suit. Although not as controversial as the "Pagan Poetry" music video, it was still banned from MTV. In early August 2001, Björk confirmed the first set of dates for the Vespertine world tour which would take place at opera houses, theatres, and small venues, with favourable acoustics for the concerts. She enlisted Matmos, Zeena Parkins, a choir of Inuit girls from Greenland, and conductor Simon Lee; Visually,
```

### Album 131, chunk 15

```text
fauna illustrations by Ernst Haeckel were used as a backdrop during the tour. The tour opened at the Grand Rex in Paris on 18 August. While in Paris, she held a press conference to discuss the album but gave no individual interviews saying that: "she'd rather do music than talk about it." While in France she also received the National Order of Merit at the Ministry of National Education in Paris. Another press conference was held in Barcelona on 3 November 2001 while touring in Spain. A 16 December 2001 performance at the Royal Opera House in London was released as the DVD Live at Royal Opera House in 2002. A DVD release featuring a behind-the-scenes look at the tour, titled Minuscule, was released at the end of 2003. Vespertine Live, a live album consisting of songs recorded during the Vespertine world tour, was included in the 2003 box set Live Box; it also includes a live version of "All Is Full of Love", a song from Homogenic and "Overture" from Selmasongs. Vespertine debuted at #19 on the Billboard 200 chart, selling 75,000 units in its first week, becoming her career peak in sales. It also debuted upon the top spot on the Top Electronic Albums chart, staying there for 3 weeks. One Little Indian head Derek Birket declaring that the album had sold over 1.2 million copies in Europe alone. That month, the album also became number one on the album charts in Iceland, Sweden, Denmark, France, Norway, and
```

### Album 131, chunk 16

```text
the European Top 100 Albums chart. In addition, Vespertine charted in the top 10 of Canada, Italy, Germany, Japan, the United Kingdom, Finland, Belgium, Switzerland, Sweden, Austria and Australia. The album has been certified Gold in Canada, France, Switzerland, and the United Kingdom. Lead single "Hidden Place" reached the top spot of the singles charts in Spain, also charting in the top 40 in the United Kingdom, Canada, Italy, Denmark, Norway, Finland, Belgium and France. Following release "Pagan Poetry" also performed well in Spain, while entering the French chart at number 49 and the UK chart at number 38. "Cocoon" performed more poorly, charting at number 61 in France and number 35 in the United Kingdom. Upon release, Vespertine received universal acclaim from music critics. At Metacritic, which assigns a normalised rating out of 100 to reviews from mainstream critics, the album received an average score of 88, based on 28 reviews. Various writers including David Fricke and Simon Reynolds named Vespertine Björk's best album to date. The album received some praise for its themes of intimacy and introversion, with Anthony Carew from About.com writing: "What makes Vespertine even more intriguing is the way that it marries its musical ambitions to its thematic emotions… And what makes it great… is the purity and intimacy of its feelings." Fricke and musicOMH's Michael Hubbard have both noted that the singer had shown a more mature side of her. The A.V. Club's Keith Phipps found it to be: "an album both timeless and
```

### Album 131, chunk 17

```text
of the moment, an avant-garde electronic-pop exploration of classic themes". In a later review for The New Rolling Stone Album Guide, Douglas Wolk described the album as "a banquet in the hall of Björk's personal erotics" and stated that "it's not the stuff of radio hits, but the music is spectacular". An enthusiastic review came from The Wire, which felt that: "In the end, Vespertine commits its magic by daring to go places more obvious and more human than one would have ever expected." Calling it "one of the most impressive and cohesive" albums of the year, Tiny Mix Tapes found Vespertine to be Björk's most effective use of the studio as an instrument. Chris Smith of Stylus Magazine praised the album for its nuance and delicacy, describing its sonic palette as "a breath of fresh air." Additionally, Vespertine was thought to have challenged gender roles in rock music and in sexuality. Q also praised the album, stating that it "quietly proves that cutting-edge production and human contact aren't mutually exclusive." American music journalist Robert Christgau enjoyed the album's central theme of sex and wrote: "when she gets all soprano on your ass you could accuse her of spirituality". A more lukewarm review came from Pitchfork's Ryan Schreiber, who felt that: "while undeniably beautiful, Vespertine fails to give electronic music the forward push it received on Björk's preceding albums". David Browne of Entertainment Weekly said "her lyrics occasionally dive into the deep end" and "her voice is at times stiff",
```

### Album 131, chunk 18

```text
although he also wrote "when it all comes together, [...] Björk and her electronica collaborators create moving interplanetary chorals". Almost Cool wrote: "if there's one question to be raised with the album, it's that it's all simply so lush and nice that on some levels it fails to excite". In a 2015 interview with The Pitchfork Review, Björk said that her work on Vespertine was not fully acknowledged by press, she further added, "Matmos came in the last two weeks and added percussion on top of the songs, but they didn't do any of the main parts, and they are credited everywhere as having done the whole album.". In 2002, Vespertine was nominated for the Shortlist Music Prize, though the award went to In Search of... by N.E.R.D. The same year, the album received a Grammy Award nomination for Best Alternative Album, losing to Coldplay's Parachutes. In addition, Björk was nominated for Best International Female Solo Artist at the Brit Awards, and Best International Female Artist at the Italian Music Awards, while Vespertine was nominated for Album of the Year at the Icelandic Music Awards.
```

## Album 132: Pulse Demon — Merzbow

- **album_id:** `731c0727-603a-4450-9a05-b6ffa1afcfc9`
- **Tags (identification only):** noise, harsh noise, electronic, japanoise, private tag 1
- **Chunks:** 2 (351 words)

### Album 132, chunk 1

```text
Pulse Demon is a studio album by the Japanese noise musician Merzbow, released 28 May 1996. The album was reissued on vinyl in May 2018 by Bludhoney Records, and again in November 2019 by Relapse, with a bonus track. The holographic, shiny silver artwork is a homage to the 1970s Prospective 21e Siècle imprint of Philips Records, in particular the albums of Ivo Malec. However, the art is most similar to the work of Bridget Riley, "Fall" and "Current" in particular. Basically, this shiny silver is the color of Heavy Metal. I mean it the way William Burroughs said it. My basic idea is I think this idea has been approached in the past by Heldon and King Crimson. The title was inspired by the 1970s afro-rock band Demon Fuzz and Akita's use of a fuzz box as a pulse generator. Some song titles were inspired by Jon Appleton's Appleton Syntonic Menagerie LP. Critical reaction to Pulse Demon was mixed. Pitchfork gave the album's 2003 re-release a score of 8.7/10, their highest rating out of their eight reviews of Merzbow albums. Calling it an "incomparable classic", the reviewer describes the album as "simply pure sound, viciously unadulterated static", going on to state that "music cannot get much more extreme than this. Maybe John Cage's 4′33″, and that's so far to the limit, it's probably cheating. This is the edge of music, of sound in general." Also praised was the album's packaging, being called "more valuable than some people's lives." However,
```

### Album 132, chunk 2

```text
AllMusic's dismissive two-line review from Jason Ankeny simply said "Merzbow's second American release offers more of the deafening white noise that is his trademark, mastered for maximum loudness. Not for the faint of heart, but ideally suited for the hard of hearing." Being given only 2.5/5 stars, Pulse Demon is one of the four lowest rated of AllMusic's 31 (solo) Merzbow reviews. The A.V. Club, in their review, described the album as "genuinely extreme, downright torturous sounds that are strangely compelling in their shredding intensity." Masami Akita – metals, EMS, audio generator, shortwave, noise electronics, tape, voice Colour Climax – visual
```

## Album 133: Dirty Work — All Time Low

- **album_id:** `957c555d-13a9-4d5e-955c-cda16709e6ab`
- **Tags (identification only):** rock, pop punk, pop rock, alternative rock, alternative/indie rock, emo pop, pop
- **Chunks:** 17 (4212 words)

### Album 133, chunk 1

```text
Dirty Work is the fourth studio album by American rock band All Time Low. Following the success of Nothing Personal, the band signed to major label Interscope Records in late 2009. After spending sometime writing material in Los Angeles, the band started recording with Mike Green in March 2010. Over the following months the band recorded songs with John Fields, Butch Walker, Matt Squire, David Kahne and U4L. In between sessions, the band embarked on the Bamboozle Roadshow tour. Neal Avron mixed the majority of the album's recordings while Green, Mark Trombino and Chris Lord-Alge each mixed a song. Vocalist/guitarist Alex Gaskarth co-wrote the album's songs with a variety of people, including those who produced a few of the songs. While recording, the album was planned for release in 2010. It was delayed to January 2011, and then to spring. Further recording sessions then took place in November 2010, as well as in January 2011. Following these extra sessions, the album was then slated for release in March 2011. Between March and May, the band went on tours of the UK and the US. While on the tour, "I Feel Like Dancin'" was released as a single, and the album was reportedly going to be released in June. Dirty Work was eventually released on June 7. In July, the band appeared at the Sonisphere and Oxegen UK festivals and embarked on a North America tour, which lasted into August. During the tour, "Forget About It" was released as a single.
```

### Album 133, chunk 2

```text
The band went on a US tour in October and November, as well as appearing on Conan. After the tour's conclusion, music videos were released for "Time-Bomb" and "Merry Christmas, Kiss My Ass" in November and December, respectively. "Time-Bomb" was released as a single in January 2012, before the band went on a UK tour, which ran into February. A Canadian tour followed shortly afterwards and "Guts" was released as a single. Dirty Work received a mixed-to-positive reception from critics. It was projected to sell 50–55,000 copies in its first week and chart within the top 10 of the Billboard 200, before eventually selling 43,000 copies and reaching number six. The album charted highly on a number of Billboard charts, even reaching number one on both the Alternative Albums and Top Rock Albums charts. It also charted at various positions in Australia, Canada, UK, Ireland, Japan, the Netherlands and Belgium. "I Feel Like Dancin'" and "Time-Bomb" both reached the top 40 on several Billboard charts. In February 2009, it was reported that All Time Low had signed to major label Interscope Records. However, the following month, vocalist/guitarist Alex Gaskarth denied this. The band released their third album, Nothing Personal in July of that year through independent label Hopeless Records, which sold 63,000 copies in its first week of release, debuting at number four on the Billboard 200. The band later confirmed they signed to Interscope Records in November. Guitarist Jack Barakat said signing to the label gave the band "a
```

### Album 133, chunk 3

```text
bunch of new resources", such as being able to "write with people that we could never write with before, recording with people, getting certain mixers/producers and everything." Gaskarth found the transition "[not] too difficult", but noting that it "definitely different though". Gaskarth mentioned how they went from being one of the biggest groups on a label who had a small amount staff and could provide their complete attention, to a major label "and we're definitely not the biggest fish in that pond. There's a lot going on, it takes a little bit longer to get things done and get things moving." He added that the band thought they "hit a ceiling" with Hopeless Records since "trying to tackle things like getting radio [airplay] and things like that was sort of becoming harder and harder based on the fact that the label hadn’t really done it before." In December, the band began writing for their next album. The band demoed around 20 songs for inclusion on their next album before whittling the number down, with the aim of recording 15 or 16 of them. After touring in Australia as part of the Soundwave festival in February and March 2010, Gaskarth spent time writing new material in Los Angeles. On March 24, 2010, All Time Low began recording their next album with Mike Green. A studio update video was posted on April 1, showing the band recording new material. Further video updates were posted on April 18 and May 13. Following this,
```

### Album 133, chunk 4

```text
the band toured throughout the remainder of May and most of June as part of the Bamboozle Roadshow 2010. Another video update was posted on June 16. On June 27, Gaskarth revealed that eight songs had been recorded and that they would record a few more with Matt Squire, after the conclusion of Bamboozle Roadshow tour in July. On July 13, the band said 10–12 tracks would be on the album. On July 29, Gaskarth announced via Twitter that they had finished recording the album, having recorded 14 songs. Mixing took place in August, with the majority of the album's recordings being mixed by Neal Avron. In addition, Mark Trombino mixed "No Idea". Following this, the band sent the finished album to the label in September. SonicScoop reported in November 2010 that the band were doing overdubs with Green, who was producing and engineering, in Studio A at Sear Sound in New York. The band previously made a demo of "Merry Christmas, Kiss My Ass" with Dan Book. Scott Stallone of U4L added electronic drums, rock samples and synthesizers to it. While working with Green, the band remade the track: re-doing guitars, replacing the old drums with new live drums, as well as new vocals, but retained a number of sounds that Stallone had added. SonicScoop also reported that in January 2011 that the band had recently recorded in Studio C at Avatar Studios with producer David Kahne and engineer Roy Hendrickson with assistance from Aki Nishimura. Ted Jensen mastered
```

### Album 133, chunk 5

```text
the album at Sterling Sound in New York City. Green produced "Do You Want Me (Dead?)", "I Feel Like Dancin'", "Guts", "Under a Paper Moon", "Return the Favor", "No Idea", "A Daydream Away", "Heroes" and "Get Down on Your Knees and Tell Me You Love Me". John Fields produced "Forget About It". Squire produced "Time-Bomb" and "My Only One". Butch Walker produced "Just the Way I'm Not". Kahne produced "That Girl", to which Green provided additional production and was mixed by Chris Lord-Alge. U4L produced "Merry Christmas, Kiss My Ass", which was mixed by Green. Asked about the choice of using several producers, Barakat said "We're all about using multiple producers on our records. ... I'm not 100% into the one producer/one record thing because you get a lot of the same sounding songs. It's cool to have a bunch of variety." Gaskarth added "working with a lot of different producers is good, because it pulls you in all kinds of new directions." He added that, similar to Nothing Personal, they "kinda split up the [recording] with different producers that we wanted to work with in the past, but for scheduling or monetary reasons, we couldn’t lock them in for the whole record." Barakat said the writing process consisted of Gaskarth "writing songs and us going into the studio to put in our two cents and changing a couple things around." In an interview with Just So You Know, Gaskarth said the album title "summarizes the theme of the songs,
```

### Album 133, chunk 6

```text
most of which centralize around escapism; running from my problems, burning bridges because of those problems; and the realization that its hard work to rebuild after those problems have torn people apart." In an interview with MTV, Gaskarth said that the title was inspired "by the subject matter on the record, where it's this toss-up of being wrapped up in what we do, and having the fun and the good times, and kind of pulling that blindfold down in order to ignore the fact that other problems are crumbling around you". Gaskarth also said "one of the big things that came along with this album ... [was] a lot of anxiety. About where were we going to go". Gaskarth said the band purposely sought to "step outside of the box and do some things that were a bit scary." He mentioned that "there's one [track] that starts with classical guitar playing something that sounds like it could be out of vaudeville and it's that kind of thing that we really decided to go for on this record." The album's sound has been described as emo pop, pop, pop rock, and power pop. Gaskarth felt the album was "more of a pop-rock/alt-rock album for us. There are definitely elements of pop punk—where we came from. But this album was an effort to develop our sound and hone in on [sic] great songwriting rather than conform to the boundaries of a certain genre." Gaskarth mentioned that they "took influence from our older
```

### Album 133, chunk 7

```text
stuff in some of the songs, but in others we went in a new direction, whether that was poppier or more rock or just weird." Gaskarth added that "We stripped a lot of the bells and whistles out this time and I think the songs are better off for it." Barakat said the album was "a good mix of faster type typical ATL songs and also some slow ballad type songs." He added "there are a lot of pop songs, as well as a lot rock songs. There isn’t a mix of the two. I think they are a lot more distinguished this time around." The band's manager suggested they write a song with Green early on in the writing process. Gaskarth ended up writing "Do You Want Me (Dead?)", "Guts", "Under a Paper Moon", "A Daydream Away" and "Get Down on Your Knees and Tell Me You Love Me" with Green within three days. Barakat said the pair had "an amazing chemistry together. He added this sweet dynamic to the band we never had before. He made us think in ways we never would have thought before." "Forget About It" was written by Gaskarth and Fields. "Time-Bomb" was written by Gaskarth, Bouvier, Comeau and Squire. "Just the Way I'm Not" was written by Gaskarth and Butch Walker. "Return the Favor" was written by Gaskarth, Jacob Lutrell and Daniel Lutrell. "No Idea" was written by Gaskarth, Christopher "Tricky" Stewart and Terrius Nash. "That Girl" and "My Only One" were written
```

### Album 133, chunk 8

```text
by Gaskarth and Squire. Barakat said Gaskarth and Squire "are great writers ... They just have an amazing chemistry together." "Heroes" was written by Gaskarth and John Feldmann. "Merry Christmas, Kiss My Ass" was written by Gaskarth, Book and Alexei Misoul. According to Gaskarth, "Do You Want Me (Dead?)" is a up-tempo track that begins the album with "a great guitar hook and lots of energy." He said the song talks about "feeling like you're being stretched to your limits by somebody. Gaskarth visited Weezer frontman Rivers Cuomo at his house and ended up co-writing "I Feel Like Dancin'". He called Cuomo "such a cool guy to work with." Gaskarth said the track was "an ode to having a good time and not taking yourself too seriously." Barakat called the track "a great song ... It has a cool Weezer/All Time Low/party hybrid-vibe to it." Gaskarth said "Forget About It" details "that place in a relationship where people have been together for a really long time and they're afraid to let go." Despite this, he said it was "a totally fun song." Gaskarth said "Guts" was "about finding within yourself the ability to say and do what you want no matter what the repercussions might be." Maja Ivarsson from The Sounds provides guest vocals on the track. Gaskarth said Ivarsson was "someone I’ve always respected vocally". He added that the pair "both sound really similar ... she definitely sounds like a girl and I sorta sound like a girl so
```

### Album 133, chunk 9

```text
there’s a weird mix that happens but trust me it works for the song." He called the track "a departure for us as it's more universal and timeless than we've ever been." "Time-Bomb" was originally written by Gaskarth along with Squire, Bouvier and Comeau for a Simple Plan song. However, during the writing process they deemed it more of an All Time Low song. Gaskarth was then featured on the Simple Plan song "Freaking Me Out" from Simple Plan's Get Your Heart On! album. Gaskarth said the track "paints a picture of a relationship in trouble, symbolised by a bomb that's about to go off." According to Barakat, the track was "the perfect song to bridge the gap" between Nothing Personal and Dirty Work. Gaskarth said "Just the Way I'm Not" was an ode to Def Leppard, going as far to include a snare sample from one of their songs on the track. It talks about how "relationships don't always work out as perfectly as a Top 40 hit would have us believe." He called it "a fun song, but a very personal one" with a "huge, anthemic chant-along chorus." According to Gaskarth, "Under a Paper Moon" was inspired by Ella Fitzgerald's "It's Only a Paper Moon" where she "talks about how when this person she wants around isn't with her everything feels fake ... I wanted to adopt and modernise [that concept]." With "Return the Favor", Gaskarth was "thinking way outside of the box", mentioning that it was inspired
```

### Album 133, chunk 10

```text
by vaudeville and Queen. The track was initially composed on piano and then the band "built the rock on top." It talks about "wanting someone to return the feelings you have for them, but to no avail." "No Idea" is based upon the film Inception (2010), specifically the scene where the character Dom Cobb has a dream relationship with his wife. Gaskarth said it was "actually something I can relate to, as there is someone from my past I'm distanced with now and the only at I can revisit that time is in my dreams. It made for a cool song." Gaskarth called "A Daydream Away" the "kind of front porch, snare brushes and acoustic guitar slow jam I always wanted to write." He added the lyrics were "very personal" and said it is a "good song to put on when you miss somebody and just want to relax." Gaskarth called "Heroes" the "no-so-find farewell closer" that is also the "most pop-punk song" on the record, in tribute to their roots. He classed it as an ironic song since it mocks the concept of "people idolising bands and all the drama that goes along with that when those bands try to evolve their sound as they grow up." He said it was an "important final song and point to make for this album specifically as we've really taken some risks and stretched ourselves." The title of "Merry Christmas, Kiss My Ass" comes from the film National Lampoon's Christmas Vacation (1989).
```

### Album 133, chunk 11

```text
Early in the recording process, Kerrang! reported that the band's new album would be released sometime in 2010. Towards the end of the recording process, Gaskarth said the album would be released in January 2011. On August 17, a demo was posted online of the track "Actors". Gaskarth said he posted it because he "thought people should hear it." He said that the song wouldn't fit on Dirty Work since it "didn't represent the theme of the new album closely enough." After appearing at Reading and Leeds Festivals in August, the band returned to the studio to finalise the album's track listing in September. In October and November, the band went on a headlining club tour in the US with support from A Rocket to the Moon and City (Comma) State. The band held a contest where five fans could hear the new album at each stop on the tour. On October 18, the album's title as revealed: Dirty Work. In November, Barakat revealed that the album's release date had been pushed back to early spring and that the majority of the album's songs were mixed. In December, "Merry Christmas, Kiss My Ass" was made available for streaming. In January 2011, Gaskarth said the group were sorting out the track order and working on the album's artwork. He also said that the album was originally going to be released in the same month, "but now it looks like we’re going to have to push it back" and were aiming for
```

### Album 133, chunk 12

```text
its release between January and March. During an interview in early February, Gaskarth stated that the band were currently approving artwork. He went on to say: "the record is slated to be released in late March so I would expect people to start hearing something in the next few weeks." Gaskarth stated in another interview: "We never actually gave an official release date; it's all been left to speculation and stretching of the facts. At this point, its looking more like the record will come out a bit later than March, but I think folks can still expect to hear some new material in the coming weeks." On February 9, 2011, Gaskarth posted a new song, titled "Art of the State", on his Twitter. Gaskarth said that "people are chomping at the bit for something new. ... I just tossed a little fuel on the flames." Despite speculation that it would be the intro to the album, Gaskarth clarified that it was "more of an ending to the story. We pulled a [Quentin] Tarantino." On February 14, while on tour, the band played a new song entitled "Time-Bomb". On February 16, Gaskarth stated that the "record's definitely not coming out in March" due to the "restructuring" of Interscope Records and a number of records have been pushed back, Dirty Work being one of them. In a later interview, Gaskarth presumed "a bunch of people got fired. We just wanted to make sure we didn't get caught up in that shit
```

### Album 133, chunk 13

```text
storm essentially, so we decided to hold off on putting the record out." "Time-Bomb" was made available for streaming on February 26. In March, the band went on a UK tour alongside Yellowcard and Young Guns. In mid-March, Barakat stated in an interview with AbsolutePunk that All Time Low will "hopefully be releasing the track-listing shortly, maybe even clips of every song." He went on to say that a single hadn't been picked, though mentioned that "I Feel Like Dancin" was "in the running and will most likely be released as a single at some point, we're just not sure if it will be the first one." On March 22, 2011, All Time Low exclusively unveiled the artwork for Dirty Work through Alternative Press. From late March to early May, the band went on the Dirty Work Tour with support from Yellowcard, Hey Monday, and the Summer Set. While on the tour, the band performed a new track titled "Under the Paper Moon". On March 23, NME reported that the album would be released in May. Two days later, the band revealed the album's track listing. On April 1, AbsolutePunk reported that Dirty Work would be released in June. "I Feel Like Dancin'" was made available for streaming on April 4, before released as single a day later. In mid-April, a music video was filmed for "I Feel Like Dancin'". The video was later released on May 23, directed by Matt Stawski. Gaskarth explained the video was "taking a stab
```

### Album 133, chunk 14

```text
at the music industry, how it works and the sort of things and extents people go to become successful." Dirty Work was released on June 7 through Interscope Records. "I Feel Like Dancin'" was released to mainstream radio on June 14. On June 17, the band appeared on Hoppus on Music, performing "Do You Want Me (Dead?)" and "I Feel Like Dancin'". In early July, the band appeared at the Sonisphere and Oxegen festivals in the UK. On July 12, a music video was released for "Forget About It", directed by Jonathan Bregel. The video consists of behind-the-scenes footage of the band at backstage and radio appearances, among other things. In July and August 2011, the band toured across North America on the Gimme Summer Ya Love tour. The band were supported by Mayday Parade and We Are the In Crowd for the majority of the tour, while the Starting Line, Cartel, the Cab and Brighter appeared on select dates. On August 15, the song "Forget About It", was released as a single. In late August, the band appeared at the Reading and Leeds Festivals. In early September, a music video was filmed for "Time-Bomb". In late September and early October, the band toured Australia as part of the Soundwave Counter-Revolution festival. In October and November, the band went on the Rise and Fall of My Pants tour in the US with support from the Ready Set, He Is We and Paradise Fears. On October 19, the band performed "Time-Bomb"
```

### Album 133, chunk 15

```text
on Conan. In mid-November, the band revealed they were working on music video for "Merry Christmas, Kiss My Ass". Also in mid-November, it was reported that Big Time Rush had stolen the chorus to "No Idea" for their song of the same name. All Time Low and their management initially stated that permission was not granted for the use of the chorus. However, shortly afterwards Gaskarth clarified that representatives of Big Time Rush asked if they could do their own version of "No Idea", to which Gaskarth said "we were totally cool with". On November 30, the music video for "Time-Bomb" was released, directed by Asher Levin. The music video for "Merry Christmas, Kiss My Ass" was released on December 8, directed by Jon Danovic. On January 6, 2012, "Time-Bomb" was released as a single. In January and February, the band went on a UK tour with support from the Maine and We Are the In Crowd. This was followed by a tour of Canada with Simple Plan. "Guts" was released as a radio single on May 14. Dirty Work received mixed to positive reviews from music critics. At Metacritic, which assigns a normalized rating out of 100 to reviews from mainstream critics, the album received an average score of 67, indicating "generally favorable reviews", based on 8 reviews. Entertainment Weekly gave this album a positive review, saying "Dirty Work proves you can grow up and still act like a kid, just as long as your songs are this head-rushingly
```

### Album 133, chunk 16

```text
catchy". AllMusic was also positive, saying "Consider Dirty Work the band's ultimate bid for mainstream acceptance, and one of their strongest pop albums to date". Alternative Press gave the album an average review, stating "Guts, featuring The Sounds' Maja Ivarsson is a synth-assisted 6/8 number loaded with urgency and lyrical poignancy" yet also notes "Other tracks feel homogenized and lifeless, as if they were focus group to death. Time-Bomb is a Metro Station-aping electro-dance number that does nothing to actually make the listener dance." Luuux gave the album an overall average review, stating "Fast beat with electric guitar songs like "That Girl" and "I Feel Like Dancin'" (a satire song about the radio/music industry) don't have me as a fan either, but the rest of the album is worthwhile." Sputnikmusic was more negative, stating that "Similarly, there was a time when All Time Low were a genuinely exciting young pop punk band; when the songs were dynamic and Alex Fucking Gaskarth's vocals were merely double-tracked rather than layered and autotuned to fuck." idobi Radio also gave a negative review stating, "The band lost their way... This experiment went wildly out of control. The album lacks overall direction and cohesiveness." Review Rinse Repeat's review was mixed, noting that the record "Overproduced and emotionally flat, there just isn't much good to say about this album. Strange enough, All Time Low seem to be in a completely different world this time around, as tracks like "Forget About It", "Under a Paper Moon" and
```

### Album 133, chunk 17

```text
"I Feel Like Dancin'" show with unneeded slickness, out-of-body songwriting (not in a good way) and underachieving vocals." Dirty Work was projected to sell 50–55,000 copies and chart within the top 10 of the Billboard 200. It eventually debuted at number 6 on the Billboard 200 with 43,000 first week sales. Dirty Work has sold 107,000 copies in the US to date October 2012. Dirty Work also charted on a number of Billboard charts: number 1 on both the Alternative Albums and Top Rock Albums charts, number 3 on the Digital Albums chart and number 19 on the Tastemaker Albums chart. In addition, the album reached number 13 in both Australia and Canada, number 20 in the UK, number 31 in Ireland, number 41 in Japan, number 67 in the Netherlands and number 83 in Belgium. "I Feel Like Dancin'" reached number nine on the Rock Digital Song Sales chart number 23 on the Heatseekers Songs chart and number 39 on the Pop Songs chart. It also reached number 85 in the UK. "Time-Bomb" reached number 13 on the Rock Digital Song Sales chart and number 24 on the Heatseekers Songs chart. Alternative Press included "Under a Paper Moon", "That Girl" and "Heroes" on their list of the band's best non-single songs.
```

## Album 134: Life — KRS‐One

- **album_id:** `586e1eac-1949-4fde-bbd5-744a7445d956`
- **Tags (identification only):** hip hop, east coast rap, hardcore rap, political rap, east coast hip hop, hardcore hip hop, rap
- **Chunks:** 1 (132 words)

### Album 134, chunk 1

```text
Life is the eighth solo studio album by American rapper KRS-One. It was released on June 13, 2006 via Antagonist Records. Produced by the Resistance, it features guest appearance from the Footsoldiers. The album received generally positive reviews from music critics. Lawrence "KRS-One" Parker – main artist Theresa Jones – additional vocals (track 2) Orlando "Triune" Solano Jr. – featured artist (track 4), additional vocals (track 6) Ishmeal "Ishues" Cuthbertson – featured artist (track 6) Dax Reynosa – additional vocals (track 6), producer, executive producer Nazareth "DJ Rhettmatic" Nirza – scratches (track 7) Raphael "Raphi" Henley – featured artist (track 8) DJ Wize – scratches (track 9) Jason "Propaganda" Petty – featured artist (track 10) Donald "Dert" Baker – producer, design, layout Habit – co-producer (track 3) Justin "Dubb" Taylor – mixing
```

## Album 135: A Tiny House, In Secret Speeches, Polar Equals — Sweet Trip

- **album_id:** `d6afb3f0-b9a2-4468-864b-2be3b0153623`
- **Tags (identification only):** dream pop, electronic, idm, indietronica, glitch pop, rock, shoegaze, synth pop
- **Chunks:** 2 (331 words)

### Album 135, chunk 1

```text
A Tiny House, In Secret Speeches, Polar Equals is the fourth and final studio album by American experimental pop act Sweet Trip, released through Darla Records on May 28, 2021. The album was released 12 years after Sweet Trip's previous studio album, You Will Never Know Why. The song "Walkers Beware! We Drive into the Sun" was released in January 2021 along with the announcement of the album. Sweet Trip describes the album as being heavily influenced by the shoegaze and electronic pop sounds of their previous albums. Roberto Burgos and Valerie Cooper, the duo behind Sweet Trip, announced the band was taking a break in 2013. Their last full album, You Will Never Know Why, was released in 2009, 12 years before the release of A Tiny House, In Secret Speeches, Polar Equals. In May 2020, Sweet Trip released the song "In Sound, We Found Each Other". In January 2021, the duo released the single "Walkers Beware! We Drive into the Sun" and announced the release of A Tiny House, In Secret Speeches, Polar Equals as well as a reissuing of You Will Never Know Why. Before the release of A Tiny House, In Secret Speeches, Polar Equals, two of the band's previous albums, Velocity : Design : Comfort and You Will Never Know Why, were reissued. On January 7, 2022, two bonus tracks were added to the album on streaming, originally being exclusive to a 7" vinyl which came as a bonus in some purchases of the album
```

### Album 135, chunk 2

```text
on vinyl. According to Sweet Trip's description of the album, it was "created out of the blue; nothing planned, not even a sense of direction" out of "strong emotions and pure love". The group says that the album was influenced heavily by their previous albums Halica: Bliss Out v.11, Velocity : Design : Comfort, and You Will Never Know Why in terms of technique and style. Sputnikmusic named A Tiny House, In Secret Speeches, Polar Equals the 8th-best album of 2021.
```

## Album 136: Get Rid! — Robots in Disguise

- **album_id:** `b258c48e-b04c-4ac6-a03b-294cba69fb4a`
- **Tags (identification only):** electronic, rock, electro, electroclash, electropunk, punk, synth pop
- **Chunks:** 1 (33 words)

### Album 136, chunk 1

```text
Get RID! is the second album by Robots in Disguise. Tracks include the single "Turn It Up", a song composed mainly of references to other songs and, "La Nuit", sung entirely in French.
```

## Album 137: The Ascension — Otep

- **album_id:** `c5ecee4a-fd19-4350-ae9d-c46b4c6b99cf`
- **Tags (identification only):** nu metal, rock, alternative/indie rock, goth metal, goth rock, heavy metal, industrial metal, pop/rock
- **Chunks:** 2 (451 words)

### Album 137, chunk 1

```text
The Ascension (stylized as the_Ascension) is the third studio album by Otep. The original release date was set for March 20, 2007 through Capitol Records, however, the album was delayed indefinitely due to the merger with Virgin Records. The album debuted at number 81 on the Billboard 200 with 10,200 copies sold. The album was partly recorded in New Orleans, Louisiana, where producer Dave Fortman was living. New Orleans, especially the 9th Ward was still affected by the effects of Hurricane Katrina. Otep said that while the songs were not influenced by the area, the mood of the album was. The band began recording the album in late July 2006, and it was completed by the end of the year. Several songs were written with Mudvayne guitarist Greg Tribbett, who Fortman had worked with in the past. Otep explained the song to KNAC.com: "It was about writing a protest anthem to stand up, speak out and strike back. To celebrate the unique opportunity that we have here in America. You can do anything to have your voice be heard in this country, that’s the beauty of this country. There’s no one stopping anyone in America from getting out on the street and saying something or writing a letter or e-mailing and text messaging now that everything is now, now, now." Otep compared the song to "Warhead" from House Of Secrets. "Breed" is a cover of a Nirvana song of the same name. It is Otep's first cover song. "We'd never
```

### Album 137, chunk 2

```text
done a cover song before but I just love the song. I listen to music before we play on tour and that song just kind of grabbed me. I couldn't get enough of it. I'd listen to it 60, 70 times, just over and over in the back of the bus before the show,” she explained to Campus Circle. “For me, it's just this amazing song that touched me in a certain way that made me miss Nirvana a lot and Kurt Cobain's touch on musical culture and his philosophy on music and art. I just wanted to do something to inspire and to, in a way, connect our energies.” The Ascension received mixed reviews from critics. Otep Shamaya – vocals Karma Singh Cheema – guitars Holly Knight – mellotron, piano, programming on "Perfectly Flawed" Jason "eViL J" McGuire – bass guitar, backing vocals Brian Wolff – drums Art direction, design – Otep Shamaya, P.R. Brown Photography – P.R. Brown, Sam Throne Engineer – Jeremy Parker Assistant engineers – David Troia, Drew Vonderhaar, Wesley Fontenot Executive producer – Jonathan Cohen, Otep Shamaya Mastering – Ted Jensen Recording, producer, mixing – Dave Fortman Drum technician – Rory Facianne Co-producer – Holly Knight
```

## Album 138: Balloonerism — Mac Miller

- **album_id:** `eddcaf71-bfa8-4ec9-b0fd-b06bc3a310cd`
- **Tags (identification only):** abstract hip hop, jazz rap, neo psychedelia, 1–4 wochen, cloud rap, english, experimental hip hop, hip hop
- **Chunks:** 15 (3720 words)

### Album 138, chunk 1

```text
Balloonerism is the seventh studio album by American rapper Mac Miller, and his second posthumous album following his death in 2018. The album was released by Warner Records on January 17, 2025, under license to Warner Records, exactly five years from the release of his first posthumous album Circles, and features guest appearances by SZA and Miller's alter ego Delusional Thomas. Initially, Balloonerism was constructed between 2013 and 2016, mostly amidst the production of Miller's studio album Watching Movies with the Sound Off (2013) and Faces (2014) but was scrapped in favor of other projects for years. A neo soul, experimental hip-hop, and jazz-influenced album, Balloonerism showcases Miller's themes and lyrics on drug use, depression, death, and a longing for childhood innocence, in which he uses metaphoric lyrics and vague storytelling throughout the album. The album's style emphasizes a contrast between its bright tone and dark themes, in which the production gradually becomes darker near the album's conclusion. It is described as a transitional project in Miller's career, distancing from his earlier frat rap style and moving towards a more introspective approach with singing. Much of Balloonerism was finished within a week through jam sessions with musician Thundercat's involvement. After it was scrapped, some of the album's tracks were leaked in 2020 by a Reddit user, which led various Miller fans to construct their versions of Balloonerism. In 2022, Miller's brother Miller McCormick began discussing with recording engineer Josh Berg and mixer E. Dan about the album's commercial release. In
```

### Album 138, chunk 2

```text
November 2024, Balloonerism was announced with a visual trailer screened at Camp Flog Gnaw. In promotion of the album, "5 Dollar Pony Rides" was released as its lead single, and an animated short film based on the album was released on the same day of the album's release. Balloonerism was met with generally positive reviews from music critics, praising the album for Miller's introspective lyrics, emotional depth, experimental production, and its approach as a posthumous album. Commercially, the album debuted at number three on the US Billboard 200, earning 81,000 album-equivalent units. In addition, the album topped multiple Billboard album charts and peaked at number two on the US Top R&B/Hip-Hop Albums chart. Outside of the US, the album appeared in multiple album charts internationally. Balloonerism later received a nomination for Best Recording Package at the 68th Annual Grammy Awards. In 2012, following the commercial success of his debut studio album Blue Slide Park (2011), Miller moved to Los Angeles. At the time, he had been criticized by hip-hop purists as a "wholesome white frat-rapper", and had done more than 250 shows from the age of eighteen to twenty-one. He decided to move to Los Angeles following a personal fondness for the city while shooting an episode of Punk'd. His residence in Studio City was later noted as a music studio for up-and-coming rappers at the time, including Schoolboy Q, Ab-Soul, Tyler, the Creator, Vince Staples, and Earl Sweatshirt. After shooting two seasons of his MTV reality series Mac Miller
```

### Album 138, chunk 3

```text
and the Most Dope Family and leaving his contrast with Rostrum Records, Miller found himself in a reflective state according to record engineer Josh Berg. On June 18, 2013, Miller released his second studio album Watching Movies with the Sound Off, marking a drastic shift from his frat rap days. He remained productive during the whole year, releasing Stolen Youth, a collaborative mixtape with Vince Staples; Delusional Thomas, a horrorcore mixtape based on his alter ego of the same name; and Live from Space, a live album from his tour. In 2014, Miller released the mixtape Faces, recorded not long after Balloonerism's initial sessions, and was critically acclaimed for its themes of psychosis, addition, and mortality, similar to the latter. Following the initial scrapping of the album, Miller added more singing elements to his work on The Divine Feminine (2016), continuing the approach on Swimming (2018) and the posthumous album Circles (2020). In September 2018, Miller died of an accidental drug overdose at the age of 26, leaving behind various unreleased projects including Balloonerism. The period when Balloonerism was recorded is disputed. Some publications claimed it was recorded between 2013 and 2014, conceived amidst the production of Watching Movies with the Sound Off. Rolling Stone writer Maya Georgi stated that the album was recorded in the spring of 2014, while its liner notes list the recording dates as between 2014 and 2016 and was recorded at The Sanctuary in Los Angeles. Much of the Balloonerism sessions came from Miller's friendship
```

### Album 138, chunk 4

```text
with Thundercat, who shared similar tastes in humor and collaborated in a freewheeling, improvisational approach. Usually, a track from the album was finished within a day with little revision. In the production of Balloonerism, Miller provided the tambourine on four tracks, drums on three tracks, and served as a recording engineer in two tracks. Thundercat worked on the majority of the album, providing bass in eight tracks and additional vocals on "DJ's Chord Organ". SZA provided additional vocals on "DJ's Chord Organ" and "Friendly Hallucinations". Jameel and Ronald Bruner provided keyboards and drums, respectively, on "5 Dollar Pony Rides". "Mrs. Deborah Downer" features additional vocals from Ashley All Day, and "Manakins" and "Rick's Piano" features additional vocals from Dylan Reynolds, with the latter involving guitar. Balloonerism was mixed by E. Dan and mastered by Mike Bozzi. The album cover was painted by artist Alim Smith, which depicts an abstract portrait of Miller. Smith posted it in September 2018 following Miller's death. A month prior, she posted a similar painting, with Miller's response being "need this". Upon the album's release, Smith revealed that she was unaware that her painting was being used by fans on their own revisions of Balloonerism until after Miller's estate reached out to her in 2024. By the summer of 2014, Miller was struggling with severe depression and substance abuse, which led him to collaborate with producer and record label founder Rick Rubin for help. Rubin later revealed that Miller called him while drunk on his way
```

### Album 138, chunk 5

```text
to a European tour, saying "Rick, dude, I'm fucked up, will you help me?". Miller went into sobriety during his time of making music at Rubin's personal studio. Two tracks that Miller worked on with Rubin appeared on the official release of Balloonerism. "Shangri-La" was likely recorded approximately during the summer of 2014 at Rubin's studio of the same name, while "Rick's Piano" was initially titled "Rick Rubin's Piano". E. Dan of ID Labs revealed his thoughts about the project in a now-deleted post, where he revealed that Miller made a track list and that the majority of the tracks from Balloonerism were made within a week consisting of jam sessions. Dan claimed that Miller took a few tracks for Faces and moved on from the project. He later addressed his fans that the artwork and track lists from online versions of Balloonerism were fan-made, adding that Miller made a few iTunes playlists consisting of the project and was left unfinished. Quentin Cuff, who was Miller's best friend and former tour manager, briefly mentioned Balloonerism in the book The Book of Mac: Remembering Mac Miller (2021), and revealed that it was conceptualized before Faces. With Miller and recording engineer Josh Berg recording the project at The Sanctuary in Los Angeles, Cuff described their process as "cooking up very zany, otherworldly, weird creations" during a Passion of the Weiss interview. Following the album's production, Miller regularly gave discussions about the release of Balloonerism, though his other projects including GO:OD AM (2015)
```

### Album 138, chunk 6

```text
took precedence. In 2020, a Reddit user leaked tracks from the Balloonerism sessions, including "Do You Have a Destination", "Uber", and "He Finally Sleeps", and created a detailed timeline of the album's leaks. The user also discovered that the album artwork was commissioned from Alim Smith and that the domain name Balloonerism.com was registered in 2014. Many Miller fans made their own iterations of the album, including other tracks such as "Colors and Shapes", "Stoned", and "Tambourine Dream". In 2022, Miller's brother Miller McCormick, who helps manage the former's music following his death, began seriously discussion a commercial release of Balloonerism with Berg and E. Dan. Balloonerism is a neo soul and experimental hip-hop album with jazz, psychedelia, and funk influences. Thematically, the album centers on Miller's drug use, depression, lost love, a longing for childhood innocence, and existential angst throughout the album. Using his philosophy about life and death while finding answers about it, the album's contrasts are used throughout by tapping into dark themes while presenting the concept in a "preachy and bright" tone. Themes about drugs remain common throughout Balloonerism, where Miller uses metaphoric lyrics such as "Even pills turn the power, the world wanna crush you down", to parts where his delivery becomes more slurred and downbeat. He emphasizes vague storytelling, rhetorical questions, and metaphors that come off as blunt when relating to his personal struggles and death. Whynow writer Aaron Edwards metaphorically described the album's title to represent Miller's "euphoric state before his balloon is
```

### Album 138, chunk 7

```text
burst and he falls back down to earth." Matthew Strauss of Pitchfork reflected that the album still expressed a duality of happier themes from Miller's frat rap period while adding a more "lurid and dangerous" style with sadness. Rolling Stone writer Maya Georgi described Balloonerism as sounding like outtakes from Watching Movies with the Sound Off and Faces. AllMusic considered it to represent a series of ideas that feel "both carefree and on the brink of implosion." Compositionally, the album's instrumentation features "heavenly hard samples and wistfully beautiful piano loops." "Woozy, electric guitar" and bass lines commonly appear in tracks including "Stoned", "Friendly Hallucinations", and "Mrs. Deborah Drowner". Georgi's consider the album's style as a precursor to Miller's funk-based album The Divine Feminine and the instrumentation of Swimming (2018). "Tambourine Dream" opens as a half-minute instrumental that features a mix of tambourines, maracas, and "distant skimming of drum skins". Progressing to "DJ's Chord Organ", the song begins with a sound collage in its first few minutes, which combines distant vocal harmonies with soft organ chords and building drums. In the middle of the song, SZA appears with a "strutting verse over a circusy organ riff". Featuring additional vocals from Thundercat instead of Miller's, the latter composed by using the chord organ of singer-songwriter Daniel Johnston, initially under the title "The Song That Changed Everything". On "Do You Have a Destination?", Miller brags about having "supermodels in his swimming pool" before admitting that he feels disconnected despite his success. The song
```

### Album 138, chunk 8

```text
shows a "daydreamy" approach with various additions such as ad-libs, background singing, vocal distortion, boom bap-esque production, and piano riffs revolving around the song. The next track, "5 Dollar Pony Rides", is a boom bap-esque song and a "groovy jam about a girl". Being introspective and emotive, Miller sings about "fleeting pleasures and loneliness" to a lover while yearning for a vacation. Rather than materialistic items, he wants to fill the woman's soul with "what she needs." The song concludes with "funky" basslines, soft vocals and soul intonations. "Friendly Hallucinations" features a smooth baseline from Thundercat and a "catchy hook", with the song described as sounding like a "soul-infused haunted house with soft loving vocals" that evolve into a "trance-like chant". Lyrically, Miller reflects on his relationship with drugs and how much it impacted some of his friendships. Continuing the weight of his drug addiction, "Mrs. Deborah Downer" shows his self-confrontation on "where he would be without drugs" as crashing cymbals persist throughout the song, Being self-reflexive and corrective at the same time, it serves in a way that is described as "distorted yet optimistic" with slowly played bass from Thundercat. A similar-sounding song with an anthemic tone, "Stoned" narrates a story about a woman whose preference for "isolation and self-serving deception is curable" in a way Miller knows how. Featuring a smooth guitar riff, Miller sings to the woman about getting high, which he "compares to heaven, with her." "Shangri-La" marks a departure from Thundercat's jazz-based sound, where Balloonerism
```

### Album 138, chunk 9

```text
evolves to a more "sultry-toned-rap" sound. In a pitched down voice with a lack of drums and bright synths, Miller raps about death, in which he says, "If I'm dying young, promise you'll smile at my funeral". On the opening of "Funny Papers", Miller opens the song with "Did no one ever teach you how to dance?" in a "silly, old Hollywood voice". Based on a simple beat and bittersweet piano tune, the song features continues Miller's contemplative lyrics about death and the loss of innocence, using themes of childhood to compliment it as a "pensive, nostalgic" tone. On one of the song's verses, he tells a story about a baby boy who later questions why his loving mother would subject him to a cruel world. "Excelsior", described as an interlude, shows Miller's experimental style by merging real-life sounds with trip hop beats, including the sounds of screaming children that reminds him of his imaginative childhood. He reveals on the song that he wanted to be a magician growing up, hence closing it with "abracadabra". "Transformations" features Miller's pitch-shifted horrorcore alter ego Delusional Thomas, which explores darker themes and lyrics based on his own psychosis. The Line of Best Fit writer Lana Marshall described the song as a conversation between Miller and Thomas. Over a harp-infused instrumental and psychedelic influences, Miller adds a stronger emotional weight to Balloonerism on "Manakins", as he speaks about dying while drifting sonically. Shifting to another track, which opens with a Rick Rubin-centered knock knock
```

### Album 138, chunk 10

```text
joke, "Rick's Piano" refers to Miller's experience with using a keyboard at Rubin's studio, with topics based on death, searching for happiness, and hope. He questions what death feels like and why it "steals life", as well as the existence of Heaven by promising that "the best is yet to come." The concluding track, "Tomorrow Will Never Know", expands to nearly twelve minutes, which features muffled sounds of children playing while a telephone rings in the distance, as well as lyrical ruminations over death, suicide, and pressure. Capturing a "dubious and dark" mood, Miller wonders if God would give him a break before deciding that it wouldn't matter. An automated voicemail plays throughout the track, as he becomes unable to answer his phone calls by its conclusion. On November 16, 2024, a visual trailer for Balloonerism was screened at Camp Flog Gnaw, between Sampha and the Alchemist's sets. An animated trailer that runs for nearly three minutes, it shows two kids playing on a playground until an object falls from the sky and "impacts the ground in the distance." Following this, multiple rodents are seen "going on an epic journey with trippy visuals", before concluding with the word "soon" and the album's artwork as the music is set to the then-leaked song "5 Dollar Pony Rides". A few days after the album's announcement, Miller's family released a statement on their intention to release Balloonerism, which was to showcase "both the breadth of his musical talents and fearlessness as an artist"
```

### Album 138, chunk 11

```text
and serve as a response to unofficial versions of the album that circulated for years. Subsequently, they announced the release date to be January 17, 2025. On January 7, the track list was revealed. On January 9, 2025, "5 Dollar Pony Rides" was released as the lead single for Balloonerism. On January 13, it was announced that an animated short film based on the album would be previewed in advanced theatre screenings. It was later made available on Amazon Prime Video on the day of the album's release. On January 17, 2025, Balloonerism was released to streaming services and digital download, through Warner Records. Physically, the album was released on LP, CD, and cassette, along with a limited edition deluxe LP version that includes a white splattered cloud cover, poster, a 32-page booklet featuring photos and lyrics, and a 3D pop-up centerfold. In addition, unisex T-shirts and sweatshirts were made available. On the day of its release, Balloonerism received praise from fans, with one stating that it sounded like "he came back from the dead and recorded this last year", while another complimented the album's vulnerability and existential themes. SZA gave a tribute to Miller on X, stating that she was grateful "he saw something in me before most and treated me w love from day 1", and also revealed that "DJ's Chord Organ" was entirely unchanged from its original recording. Balloonerism was met with generally positive reviews from music critics. According to the review aggregator Metacritic, Balloonerism received "generally
```

### Album 138, chunk 12

```text
favorable reviews" based on a weighted average score of 77 out of 100 from 10 critic scores. The Independent's Helen Brown praised the album, in which she said that it gives a "complete and cohesive" structure compared to other posthumous albums, and that the significant aspect of the album comes from its percussion. Lana Marshall of The Line of Best Fit considered it to be an "emotive and plaintive testament" to Miller's legacy and impact on hip-hop. Robin Murray of Clash praised Balloonerism, noting it for its cohesive structure and high quality as a posthumous work. Sean Fennell of Flood Magazine praised the album's psychedelic influence and its emotionally resonant songs, while he considered its posthumous nature to complicate its interpretation, remaining in uncertainty whether Miller intended to release Balloonerism in its present form. Gavyn Green of Paste characterized it as a laid-back and introspective album that shows Miller's "musical soul-searching" while retaining the lyricism of his earlier work. He highlighted one of its tracks, "Funny Pagers", as an example of the album's ambiguity and stated that its quieter details help make Balloonerism more comforting to revisit. HotNewHipHop writer Gabriel Bras Nevares noted that the album was an example of Miller's experimentation and vulnerability that was developing "behind the scenes of his mainstream mid-2010s output", seeing it as "nothing less than idiosyncratic." Matthew Strauss of Pitchfork highlighted the intimate and melancholic aspects in Balloonerism's production, including Miller's melodic vocals, reminiscent songwriting, and the use of comforting music from dark emotions.
```

### Album 138, chunk 13

```text
He eventually characterized the album as a sweet and sedate "mood piece". Maddy Mussen of The Standard viewed Balloonerism as a bridge between his earlier frat-based hip-hop style and his more genre-fluid style of his later career, describing it as an introspective, emotionally difficult, and less accessible album compared to his other albums. New Wave Magazine writer Awan Magumbe saw it as a posthumous album that gives listeners insight into Miller's personal reflections and artistic development, in which he regarded as a substantial addition to his discography. Wonderland reviewer Ben Tibbits stated that Balloonerism represents an "imperfect odyssey into the mind of a searching soul", praising Miller's emotional depth and melancholic elements throughout the album. AllMusic stated that while Balloonerism may not be Miller's greatest, consistent, or most experimental work, he saw it as an unseen chapter in his artistic evolution. Though Rolling Stone writer Maya Georgi gave a mixed reception to the album, she considered Balloonerism to reflect the darker side of Miller's thoughts, stating that the album's songs "hold a different weight" than when he was alive. In the United States, Balloonerism debuted at number three on the US Billboard 200, behind Bad Bunny's Debí Tirar Más Fotos and SZA's SOS, earning 81,000 album-equivalent units (including 41,000 copies in traditional album sales) during its first week. This became Miller's eighth US top-ten album. The album marked the highest debut of the week and was the best-selling album of the week with 41,000 units sold. With 32,000 on vinyl,
```

### Album 138, chunk 14

```text
it served as Miller's his best sales week on vinyl and Balloonerism topped multiple Billboard album charts, including Top Album Sales, Top Rap Albums, Vinyl Albums and Indie Store Album Sales. It also peaked at number two on the US Top R&B/Hip-Hop Albums chart and was ranked number 78 on its year-end chart by the end of 2025. The album later received a nomination for Best Recording Package at the 68th Annual Grammy Awards, with credits to Bráulio Amado and Alim Smith. In the United Kingdom, Balloonerism peaked at number sixteen on the UK Albums chart and topped the UK R&B Albums chart. In Australia, it peaked at number twelve on its albums chart and number two on its hip-hop albums chart. Elsewhere, the album topped the Belgium Albums (Flanders) chart; peaked at the top five in Canada, the Netherlands, New Zealand, and Poland; peaked at the top ten in Austria, Denmark, Germany, Sweden, and Switzerland; and also appeared in Belgium (Wallonia), Croatia, Finland, France, Hungary, Iceland, Ireland, Italy, Lithuania, Norway, Scotland, and Spain. A short film based on Balloonerism was first announced on January 13, 2025. It received advance theatre screenings nationally from New York to Pittsburgh (Miller's home city) on January 15, and internationally the following day before its release on Amazon Prime Video on January 17. The short film was directed by Samuel Jerome Mason, who also directed Miller's "Colors and Shapes" (2014) music video. It was written by Sam Mason and Roland Kennedy, produced by Heather
```

### Album 138, chunk 15

```text
Hardin and Stephanie Demeautis, edited by Minseok Kim, and executively produced by Michael Feder, Greg Bedard, and Hana Shimizu. Balloonerism was directly influenced from the album's lyrics and visualized Miller's interest in themes of "youthful wonderment". Its plot follows a group of school friends, led by Timmy, who are "transfigured by the music of a chord organ" and moved into a "shadow world", where they go through the "underbelly of adulthood." Stylized in "texturally realistic" 3D computer graphics, the short film was produced by Hornet Studios with distribution from Miller's independent label Remember Music and Warner Records. The short film's characters were inspired from the song "Excelsior", and its only dialogue consist of Miller's vocals from the album. Malcolm McCormick – lead vocals (all tracks), percussion (track 1), drums (track 6, 9, 11), recording (tracks 11, 13) Thundercat – bass (tracks 2, 4–6, 9, 11, 13, 14), additional vocals (track 2) Taylor Graves – keyboards (tracks 3, 5, 6, 9, 11), drums (track 5), background vocals (track 8) Jameel Bruner – keyboards (track 4) Ronald Bruner – drums (track 4) SZA – additional vocals (tracks 2, 5) Ashley All Day – additional vocals (track 6) Dylan Reynolds – additional vocals (tracks 12, 13), guitar (track 13) Josh Berg – recording, photography E. Dan – mixing Bráulio Amado – design, packaging
```

## Album 139: One Life Stand — Hot Chip

- **album_id:** `01b4876f-c1c7-4ded-9839-734f34542f0e`
- **Tags (identification only):** electronic, alternative dance, electropop, alt dance, dance pop, electro, indie, indietronica
- **Chunks:** 14 (3364 words)

### Album 139, chunk 1

```text
One Life Stand is the fourth studio album by English synth-pop band Hot Chip, released digitally on 1 February 2010. The physical album was released in the United Kingdom on 1 February 2010 by Parlophone and in the United States the following week on 9 February 2010 by Astralwerks. The album's lead single from the album, "One Life Stand", was released on 30 November 2009. Vocalist Alexis Taylor described the album as "the most warm and soulful sounding record we've made" and expressed hope that people would also say it was "a soulful quality that ties [the album] together". One Life Stand was recorded in a different manner than the group's previous albums. Alexis Taylor stated that the album was not "made in short bursts" but was "made with time". The first song created was "Alley Cats", which was written near the end of the band's 2008 tour, the only song to be written and performed whilst on tour. From performing it live, the band formulated a structure for the song that they felt would work and added a number of new features, such as new melodics, new hooks and a new bass line. The band partly returned to the creative process used in the creation of The Warning in that some parts of songs were written and recorded in Joe Goddard's bedroom, with Taylor also writing from his house and recording in the room he designated as a "music room". These parts were then built upon in a studio
```

### Album 139, chunk 2

```text
where the band had more space, enabling them to "expand on things". Goddard used Cubase to record at his house whilst Logic Pro was used in the studio as well as GarageBand to create parts of songs. Of the latter Taylor said, "that's what I use for recording, and that's like half of the record is going through that program". In regards to the creation of the music, Taylor stated that everyone had involvement in aspects of all of the tracks. Taylor stated that the group felt as though they had exhausted their home studio sound and the possibilities of the instruments they could use at home. Despite this, Taylor explained that he and Joe have a similar work aesthetic and that ideas would "come [...] any time of the day or night"; working on material at home would enable them to "record at home whenever ideas come". However Taylor stated, "even the studio we worked in, it's not like a professional studio that is like, top of the range. It's just a big basement with a desk and various synthesisers and a drum kit." Goddard said that although the album came together easily, the band had difficulty creating "Hand Me Down Your Love" because "it was just a matter of months and months of adding synthesizers, [and] adding drum parts", which resulted in "something like 160 tracks or pieces of music". As well as this, the band needed to edit out sections that they felt were unnecessary. Goddard discussed
```

### Album 139, chunk 3

```text
the element of time and stated that because the band had more time to create the album, they "tried things out differently" which was ultimately "a little bit unhelpful" due to the number of recorded parts that were never used. Goddard said the band wanted to move away from synths and minimised their presence by making them more subtle. Although the band wanted the album to be a pop record and present "a unified front", Al Doyle stated that the band did not want to lose the "experimental element that [they] had before". To achieve this the band used a broader range of instruments, including a flugelhorn and steelpans in combination with synths and drum machines, as well as a guitar, a drum kit and a piano. Doyle said it was "quite exciting for [the band] to work with that palette of instruments". Whilst the band wanted to create an album that was more cohesive, Taylor said that they did not "try to make it all sound like [the songs are] from the same record". The cohesiveness and unity of the album was a by-product of the way the band spent their time crafting it: I think naturally we must have been in a slightly more focused state of mind, because we weren't touring. We just had this time to make the record where usually, we've never really taken a break from touring. We've never had much time specifically for recording. So by having it, maybe that gives you greater
```

### Album 139, chunk 4

```text
clarity, your mind is just kinda all in one place, rather than feeling like you're juggling a lot of things and try to make a great album at the same time. When the album was completed and handed over to the label, their response was positive: "Cool, we really like it". Unlike Made in the Dark, the song writing approach to One Life Stand was less of a collaborative effort. Only three or four songs were written as a group whilst the rest were written by Goddard and Taylor, though Doyle said "we did have input in the way it was produced". Doyle described the writing process for the album as "a bit like writing a poem" because there was "a certain structure" that the band needed to work to whilst exercising "as much freedom" as they could. Goddard described the band's approach to song-writing as a "mix of things [with] a lot of very careful thinking about rhythms, and interlaying a lot of different ideas and influences" though, at certain points, there would be the sense that something needed to occur and these elements in songs were created spontaneously from the interaction between himself and Taylor: "this melody will somehow suddenly explode in your mind. It's never planned, it just seems to happen; almost like it has to." "Hand Me Down Your Love" and "Slush" were written by Taylor whilst Goddard wrote "Brothers". Doyle stated that "One Life Stand" and "I Feel Better" were put together "in a slightly
```

### Album 139, chunk 5

```text
more piecemeal way". The album was penned in the summer, with Doyle stating that the band were trying to make an "upbeat, optimistic, summertime record". Goddard said that in previous work, the band were "nervous about being open or emotionally honest" and would sometimes "have a jokiness or guarded sense to some of the words" whereas the new album is more open lyrically. In response to a description of the album as the band's most serious yet, Taylor said, "there was no decision to be more or less comic. I don't feel more or less humorous in my day-to-day" but stated that he could hear melancholy, of which he said was in "almost everything" he writes. He explained that he did not know why this was the case and said, "I can't ever write a song that just sounds completely saccharin. Even if I'm singing about someone being my complete love life, I'm singing about my own inabilities to be as bright as that person." Like Taylor, Doyle said he felt that there was "a certain vein of disquiet and melancholy that runs through the record". Another emotion that the band felt was present in One Life Stand was love. Goddard stated that the band did not set out to write an album about love but due to them feeling "quite settled and happy", he admitted that it had come through in their song writing. In particular, Taylor wrote some of the songs whilst holding his newborn daughter. Taylor felt
```

### Album 139, chunk 6

```text
that due to their growth as songwriters and producers the band had progressed over time, resulting in improved "clarity, melodic simplicity and strength" in their song writing. Fimber Bravo and Charles Hayward were asked to collaborate on the album and Taylor said they immediately created unexpected material. Taylor described Hayward as "very capable of coming up with his own stuff" and stated that he was responsible for the drumming in the background of the final chorus of "Hand Me Down Your Love", which Taylor labelled as "explosive". He stated that it was not something the band would have thought to do and that it worked "tremendously well". The recordings Hayward did only lasted for a few hours and Taylor stated, "we were kind of just left to our own devices to see if we could make use of it". Bravo wanted to use the steel pans, featured in the title track "One Life Stand", "in a way that [they are] not really known for". In an interview with Pitchfork, Taylor said, "I feel like the melodies on the new album are much more in-your-face, and it's more coherent." Compared with Made in the Dark, where Taylor stated he was interested in embracing the idea of "a messy double album" where each song sounds different sonically, Taylor said One Life Stand "hangs together better and doesn't feel the need to be lots of different things stylistically". Goddard stated that he felt Made in the Dark "was trying to be more futuristic,
```

### Album 139, chunk 7

```text
more crazy, 21st century, synthy and weird" whereas One Life Stand goes "back to basics". Taylor described the album as being "a less cluttered, less busy sounding record than ever before". Taylor felt that the backing vocals of the song "Slush" sounded like a vocal exercise, using "the same cadence as many very famous melodies" and likened it to "Crazy" by Willie Nelson. Taylor liked the simplicity of "Slush" and stated that "one of the most special things about the album" for him was that Charles Hayward, drummer of This Heat, plays and sings in it. Unlike the previous albums where the band felt their lyrics were obtuse they wanted to be direct with the song meaning and based the song's lyrics on love and their relationships. Taylor described "Alley Cats" as one of Goddard's more private songs and speculated that the song seemed "to partly be about his mother and wishing that she was alive to hear this song that he's singing". Taylor stated that the words of the chorus "relate to when you're feeling something that you really love is coming to an end, and saying that's not really possible". The song "I Feel Better" was described by Taylor as a song "trying to reach a kind of positive conclusion and positive state of mind whilst also trying to think about the terrible state the world is in". Doyle explained that the lyrics were about "the malaise of living in a world where there's climate change and finding
```

### Album 139, chunk 8

```text
solace in the arms of your partner". The album was influenced by a variety of different people. Taylor stated that "I Feel Better" was based on Joe Goddard "listening to Susan Boyle on TV and [he] thought of [the] string melody [...] by kind of misremembering [the] Les Misérables song". Following this, Taylor wrote the chorus, which he described as sounding like "La Isla Bonita" by Madonna. This was not the only song to be influenced by Boyle; "Keep Quiet" was written by Goddard immediately after seeing Boyle perform "I Dreamed a Dream" on Britain's Got Talent. Goddard said he "found it quite incredible" and listening to it made him want to write a song, which he sent to Taylor, who wrote the words and sent it back." Taylor stated that though the song "Alley Cats" was influenced by the song "That's Us/Wild Combination" by Arthur Russell, which he and Goddard both like, the sound of the finished version was "something a bit more Fleetwood Mac-y". Taylor said that a new bass line, which gave the song a different feel, was responsible for the transformation. Taylor said "We Have Love" had a similar feel to Donna Summer's "I Feel Love" "in terms of the euphoria of the chorus", which he described as being "reminiscent of that". Darren Wall (Wallzo), who previously designed the artwork for The Warning and Made in the Dark, was responsible for the album artwork for One Life Stand. As with previous Hot Chip album designs, Wall
```

### Album 139, chunk 9

```text
worked closely with Owen Clarke on the initial idea to reach "a core aesthetic" to experiment with. Wall expressed that over time the taste and influences of the band and himself "are always a little bit different", which results in differing artwork. However, Wall stated that he and Clarke have "hugely overlapping tastes" and tend to "gravitate towards 'mysterious objects' that invite interpretation" such as the blocks featured on the cover of The Warning and "The Artifact" used for Made in the Dark. The design the duo settled on was of a suspended marble head, which was inspired by photographs of statues being lowered into place using coloured canvas slings. Wall felt this created an interesting theme due to the idea of a classical form being "intersected with bright stripes of colour" and the idea appealed to the band. Wall described the cover as being "essentially quite an over-the-top image" and stated that there was "plenty of Giorgio de Chirico and Hipgnosis reference" in it. The name of the album was chosen because the band could not agree upon any other names. Taylor described the album title as being "a very dumb pun in a way" and felt it was "quite an ugly sounding phrase" but despite this, he felt the sentiment behind made it "quite a nice thing to say" because, as in the title song, it refers to "turning a one night stand into someone's whole life". Taylor stated that he liked "that kind of way of expressing
```

### Album 139, chunk 10

```text
love towards someone" and the idea of using a "simple but quite clumsy turn on [the] cliché" to do so. Taylor discussed the idea of applying the album title as a metaphor for how it could be read. He felt the title suggested longevity and stated that although it was not the band's intention to create an album "that'll be around for a long time", there was a "kind of [an] underlying guide to make songs worthwhile for a long time, and not just temporary". General manager of marketing for Astralwerks, Glenn Mendlinger, stated that the first single of the album, "One Life Stand", had not been "officially serviced" but was given to some "key tastemakers", reaching number five at KCRW, a Los Angeles public radio station. He said, "This is also the first time we're taking the band wider at radio, not just to college and speciality stations, but to commercial alternative". To promote One Life Stand, Hot Chip toured a variety of places, including the UK in February 2010 as well as Europe with ten dates in Belgium, France, Germany, Italy and the Netherlands in March 2010 and embarked on a US tour with The xx for six dates at large venues as of 19 April 2010. Rehearsals were set to begin in January 2010 with Goddard stating, "I can't really remember how to play any of the new songs at this point". As well as touring, Hot Chip promoted the album by performing their then-current single "I
```

### Album 139, chunk 11

```text
Feel Better" on Later... with Jools Holland on 13 April 2010, as well as previous single "One Life Stand". The album was released on two CD formats: a standard album, which contains ten tracks; and a deluxe edition, which includes the album and a bonus DVD with a "making of" documentary and three live tracks recorded in Brixton in 2008. The album was also released on 12-inch vinyl in two editions: a standard album and a special edition gatefold designed by Wallzo. The special-edition vinyl release was limited to 1,000 hand-numbered copies worldwide and consisted of two 200-gram records, pressed on the EMI 1400 in Hayes, Hillingdon. It was released by The Vinyl Factory and contained a number of special features such as an exclusive art print. It was claimed that the format would become "an instant collectors item". One Life Stand received generally positive reviews from music critics. At Metacritic, which assigns a normalised rating out of 100 to reviews from mainstream publications, the album received an average score of 79, based on 34 reviews. The Observer's Gareth Grundy wrote that the album "not only sees [the band] back on track, it's also their best work, paring down those past excesses and unifying them into an extraordinarily lovely whole." Huw Jones of Slant Magazine described it as "a smooth, sleek, and splendid pop record" where "[e]ach individual track sticks to its own tone and theme, while the group gracefully sashays through several shifts in tone and tempo." Heather Phares
```

### Album 139, chunk 12

```text
of AllMusic noted that "their sensitive side dominates One Life Stand—they don't sound ready for the floor, they sound ready to settle down. Even the most energetic songs feel tempered compared to the neon energy of Made in the Dark and The Warning's hits." She added that "[t]hough this emotional nakedness is an unusual move after Made in the Dark pushed Hot Chip to a new level of attention and acclaim, it also shows they're in it for the long haul." Nick Annan from Clash deemed it "different to Made In The Dark but a more cohesive and more heartfelt effort too. One Life Stand sees Hot Chip let us into their hearts as well as their thoughts." Benjamin Boles of Now commented that "[i]t's not that they've completely reinvented their sound as much as they've simply focused and polished it up. The real shift is in their attitude, which allows them to embrace earnestness and write some straightforward love songs. It's a strategy that could have backfired, but instead it has inspired their strongest and most consistent album so far." Uncut's Andrew Mueller believed that the album "contains little trace of the discordant outings or rather rigidly utilitarian dance grooves they seemed to feel obliged to deploy on previous albums. This is an album that sees Hot Chip freeing themselves of the surly bonds of their more orthodox dance and electronic influences and settling comfortably into the orbit of New Order and Pet Shop Boys." The A.V. Club reviewer
```

### Album 139, chunk 13

```text
Michaelangelo Matos opined that "while One Life Stand's mindset is Hot Chip's most overtly serious, the album is also its most musically accomplished. The melodies are Alexis Taylor and Joe Goddard's longest-lined, and the melodies often unfurl beautifully." Ian Mathers of PopMatters viewed it as "Hot Chip's most kinetic album" and stated that "One Life Stand may be less pleasingly idiosyncratic than Hot Chip's previous work, but it pays off in their most consistently winning set of songs to date. It's still not quite as raucous as their incredible live show, [...] but those who felt that Made in the Dark never built up enough momentum ought to find this one's straightforward drive more satisfying." Scott Plagenhoef of Pitchfork named One Life Stand the band's "most consistent and most complete record", but remarked that "it's missing an A-list single on par with 'Boy From School', 'Over and Over', or 'Ready for the Floor'. It's also missing dance songs in the mode of the latter two, focusing instead on Hot Chip at their most lush and romantic." Drowned in Sound's Hayden Woolley wrote that the album "sees their familiar pick'n'mix genre-shopping combined with unprecedented levels of Mills & Boon sentimentality. It's a heady cocktail, but when mixed in the right proportions the results are stunning." Jamie Fullerton of NME concluded that the album "does have some of the best songs of the year on it. But, again, waiting for Hot Chip to make that classic album is a bit like waiting
```

### Album 139, chunk 14

```text
for an alcoholic parent to arrive at your birthday party. There's a kind of unconditional love that'll keep you hoping every time one comes around, but there may be a point where you have to accept that it's just never going to happen." Chris Beanland of BBC Music felt that "[t]his is an imbalanced record, and one that leaves you frustrated rather than elated. But despite the blips, they have dished up at least two cerebral bangers here." Andy Gill of The Independent characterised it as "an album full of earnest endeavour, but lacking verve and creative zest." Pitchfork placed it at number 24 on its list of "The Top 50 Albums of 2010".
```

## Album 140: Balkan Beat Box — Balkan Beat Box

- **album_id:** `7d2d4ee6-502d-4df8-b73b-379d115b2960`
- **Tags (identification only):** electronic, gypsy jazz, jazz, country, downtempo, folk, future jazz, tribal
- **Chunks:** 1 (17 words)

### Album 140, chunk 1

```text
Balkan Beat Box is the self-titled debut album from the Israeli electronica-world fusion trio Balkan Beat Box.
```

## Album 141: Spend the Night — The Donnas

- **album_id:** `f1dba592-0fdc-4651-b38d-a747c5438baf`
- **Tags (identification only):** alternative/indie rock, blues, punk pop, rock pop, alternative, pop rock, pop/rock, punk
- **Chunks:** 2 (346 words)

### Album 141, chunk 1

```text
Spend the Night is the fifth studio album and major label debut by the American hard rock band the Donnas, released in 2002 on Atlantic Records. It was the band's first charting record on the Billboard 200, peaking at number 62, and features their most successful single, "Take It Off", which peaked at No. 17 on the Billboard Modern Rock Tracks chart and the top 40 of the UK Singles Chart. In November 2016, Cherry Red Records re-released the album to feature six bonus tracks, which consists of B-sides and songs from previous albums. As of 2005, it has sold 450,000 units in United States according to Nielsen SoundScan. Brett Anderson – lead vocals Allison Robertson – guitars, backing vocals Maya Ford – bass Torry Castellano – drums, percussion, backing vocals The Hellacopters – backing vocals Producer: Jason Carmer, Robert Shimp (Record) Producer: David Anthony, Gloria Gabriel (DVD) Engineers: Sean Beresford, Jason Carmer, Dime Assistant, Clint Roth, Robert Shimp Assistant engineers: Jesse Nichols, Michael Rosen Mixing: Chris Lord-Alge Mastering: Emily Lazar Assistant mastering engineer: Sarah Register Audio supervisor: Scott Smith A&R: Nick Casinelli, Mary Gormley Drum technician: Paul Revelli Art direction: Christina Dittmar Cover art concept: The Donnas Artwork: Stephen Stickler Photography: Stephen Stickler Cover photo: Stephen Stickler Direction: Popglory Art Camera operators: The Donnas, Tim Baker, Jackie Kelso Animation: Chris Becker Interviewer: Andy Dick Interviewee: The Donnas Model: Davy Newkirk The song "Take It Off" has been featured in the films Dodgeball: A True Underdog Story, The Hangover, and
```

### Album 141, chunk 2

```text
Guitar Hero (as a cover version by Wave Group Sound), and as a part of a 3-song downloadable pack via Xbox Live for the Xbox 360 version of Guitar Hero II. It appeared one more time in Guitar Hero Smash Hits. It was also featured in the Birds of Prey episode, "Gladiatrix". It was later released as DLC for Rock Band. "Who Invited You" was featured in EA Sports' MVP Baseball 2003, Splashdown: Rides Gone Wild, and True Crime: Streets of LA. "Who Invited You" was featured in the 2025 film Five Nights at Freddy's 2.
```

## Album 142: From the Ashes — Pennywise

- **album_id:** `a689042a-8af4-42e4-b13e-7e52a067fa78`
- **Tags (identification only):** punk, 2003, alternative/indie rock, pop punk, pop/rock, punk pop, punk revival, punk rock
- **Chunks:** 7 (1793 words)

### Album 142, chunk 1

```text
From the Ashes is the seventh studio album by the American punk rock band Pennywise. Pennywise released their sixth studio album, Land of the Free?, in June 2001. The band promoted it with a short stint on the Warped Tour, a Midwestern tour of the United States, and shows in Australia and Japan until April 2002. After this, guitarist Fletcher Dragge spent three months writing material for their next album. In November 2002, it was reported that they had spent a few months in a studio, having completed 15 demos. In January 2003, the band began recording their next album; sessions continued into April 2003. Sessions were held at Stall #2 in Redondo Beach, California; Darian Rundall and the band produced the proceedings. Drummer Byron McMackin said 14 songs were recorded from a potential pool of over 30. They took a break from recording to play a benefit show in February 2003. The band took further time out when Dragge's father died; the album was eventually mixed in June 2003. AllMusic reviewer Johnny Loftus described the album's sound as punk rock and said it borrowed a "page from NOFX's War on Errorism, promoting an agenda of awareness amidst its fist-pumping, sun-drenched anthems". Stein Haukland of Ink 19 referred to the album has skate punk with elements of hardcore punk. Lollipop Magazine writer Ewan Wadharmi classified it as hard rock and compared the guitar riffs to the work of Bon Jovi and Thin Lizzy. He wrote that it explores the "political
```

### Album 142, chunk 2

```text
whistle-blowing of Land of the Free?" as the band attempt to "answer what to do in the aftermath". The overall sound of From the Ashes recalled that of Pennywise's third studio album About Time (1995), while one reviewer referred to it as their "most fuming album" since their fourth studio effort Full Circle (1997), with the combination of "[s]ub-grindcore drums; chugging, circle-pit guitar; and Jim Lindberg's distinctive vocals, all velvet and venom". Larry Getlen of CityLink Magazine said the music was a "generation removed from that of the band's hardcore predecessors, with many of the drum fills and guitar licks owing more to metal than punk". Dragge said the lyrics for From the Ashes were written as a reaction to Land of the Free?, which received a minor backlash from some people due to its political nature. He explained that following the September 11 attacks, "people were a little confused as to what Pennywise was about, because we had a lot of anti-government-type songs on that record, and people were feeling like they needed to be behind the government". As a result, they had a meeting and decided that they were going to write about what they "believe is true and what needs to be talked about and what we feel in our hearts". Dragge said the album's title "symbolizes a type of starting over, and learning lessons from major events like 9/11". He attributed some of the "more heartfelt" lyrics to the band's state of mind following the September
```

### Album 142, chunk 3

```text
11 attacks, and mentioned that the death of their former bassist Jason Thirsk was a "pretty profound moment" for them. The album's lyrics also covers the Bush administration's handling of the attacks, in addition to ideology beliefs, such as gun control, news media bias and government abuse. From the Ashes opens with "Now I Know", a skate punk song that deals with self-discovery. "God Save the USA" is critical of the US government and alludes to the work of the Sex Pistols. Lindberg said it dealt with the "government's refusal to protect our greatest natural resources". "Something to Change", another skate punk song, deals with boredom. "Salvation" recalled the work of the band's labelmates Bad Religion. The tempo of "Look Who You Are" evokes the band's earlier material. "Falling Down" sees Lindberg tackle the topic of ageing and hitting middle age. "Holiday in the Sun" was the most reminiscent of the material on Land of the Free?. "This Is Only a Test" is bookended by acoustic intro and outro sections. PopMatters contributor Christine Klunk said the acoustic accompaniment "provides an appropriate beginning to a song that details the tendency of humans to build such walls of 'arrogance' around themselves". "Rise Up" is about being held responsible for one's own actions. "Yesterdays" is the slowest song on the album and incorporates a piano. The album concludes with "Judgement Day", a song that Klunk said warns listeners that the "world is no longer ours, that we've had our fun, and it's time
```

### Album 142, chunk 4

```text
to realize there are consequences for messing with the planet's equilibrium". On June 3, 2003, From the Ashes was announced for release in three months' time; alongside this, the track listing was posted online. In early-to-mid July and late July to early August 2003, the group appeared on the Warped Tour. On August 4, 2003, "God Save the USA" was made available as a free download. "Waiting" was posted on the band's website on August 13, 2003, before being released to radio on August 19, 2003. For the rest of the month, the band toured across Europe, which included appearances at the Reading and Leeds Festivals. From the Ashes was released on September 9, 2003, through Epitaph Records. Sohum Shah of The Cannabist said the album contributed to the "resurgence of politically-charged punk rock recorded during the George W. Bush presidency", alongside The War on Errorism and The Terror State (2003) by Anti-Flag. From the Ashes featured a DVD with studio footage, live performances and a trailer for a forthcoming video album; it was promoted with multiple releases shows across California. On October 3, 2003, the band appeared on Jimmy Kimmel Live!. They took a brief break as Lindberg and his wife had a child. Pennywise appeared at the Smoke Out festival in November 2003, and performed at the KROQ Almost Acoustic Christmas festival the following month. On New Year's Eve 2003 and New Years Day 2004, the band performed at Falls Festival in Australia. In January and February 2004,
```

### Album 142, chunk 5

```text
they went on a tour of the US; the January shows featured Mad Caddies and Stretch Arm Strong, while the February shows included Guttermouth and Stretch Arm Strong. On April 7, 2004, Pennywise performed on The Late Late Show with Craig Kilborn. Shortly afterwards, they played a handful of dates with Authority Zero and Autopilot Off running into May 2004. Pennywise toured Europe as part of the Deconstruction Tour, which lasted until June. They then went on shorts tours of Canada and Japan, and a one-off show in Hawaii. In August 2004, the band performed at the Moto Music Mayhem festival in Canada, followed by an appearance at the Holiday Havoc festival in the US in November 2004. They ended the year with performances in Brazil at the 89FM and Radio Cidede festivals. From the Ashes was met with mixed reviews from music critics. Loftus said it was a "welcome, rocking return to form after some weaker efforts". Haukland said that while "it’s hard not to compare From the Ashes with Land of the Free?, the latter album doesn’t necessarily benefit from such comparison", explaining that the band come across as "more comfortable with their new-found sense of social commentary here". Kerrang!'s James Sherry praised the band for sticking "rigidly to the formula that got them this far" as their "melodic punk formula is still sounding minty fresh and full of life". The Boston Phoenix writer Sean Richardson said the band "play to their strengths", referring to Lindberg's "neurotic howl"
```

### Album 142, chunk 6

```text
their "maximum-impact" punk sound. Vinnie Apicella of In Music We Trust said the album "goes Mach-1 with melody, mindfulness and taut musicianship that are unmistakably Punk yet threateningly offensive to fast talking order takers of the big label, bloated budget variety". Ox-Fanzine's Randy Flame wrote that the band "remain true to themselves and that's a good thing". He added that every track "live up to the criterion of 'catchy' and 'intoxicating'", while Jeff Perlah Revolver said Dragge was "still spewing the kind of chunky, speedy licks that made Pennywise indie-punk heroes a decade ago". Rock Hard reviewer Michael Rensen noted that their last few releases "sound pretty interchangeable", and From the Ashes offers listeners "highly melodic, socially critical Calicore rubble". Mike Verzella of Mxdwn felt that it "brings back memories of cruising with the guys and jumping around at shows". Stuart Green of Exclaim! said the "14 tracks of exactly what we've come to expect. While that may sound like a band stagnating and unable to develop, there's something comforting" in the band being able to "put things in perspective". IGN writer Nick Madsen said that after being a long-term listener, he was "expecting the new album to show some signs of progression and sadly, it doesn't". While complimenting the lyrics for being "matured and seem[ingly] more focused", he criticized the structure of the songs for being the "same, the sound is the same and frankly, the formula is getting a little stale". Punknews.org staff member Jim wrote it "still
```

### Album 142, chunk 7

```text
sounds like Pennywise, but there are little intricacies that set this one apart from their past couple of albums". Aside from the odd track, he mentioned that the remainder of the album was "solid and some of the songs even hold up to the band's older material". He felt that the "political lyrics seem less contrived" compared to those on the album's predecessor. Punk Planet writer Ari Joffe said there was a "few good singalong punk tunes" on the album, but it mainly "stairs up ambivalence [...] it's too rigid for my tastes". Klunk referred to it as a "solid contribution to their catalogue", but acknowledged that it did not have "much variety, not much that breaks out of punk's stereotypical traits". The staff at Modern Fix held a similar view, stating that it features "very little experimentation in sound and formula, and you almost wish that Pennywise would find the motivation to put a new spin on things". Drowned in Sound writer Mat Hocking felt that with repeated listens, the songs seemed weaker than tracks found on About Time, Full Circle or their fifth studio album Straight Ahead (1999), "and as such you start to wish they had experimented a little further". Wadharmi found the tracks to be "very similar, and bear a striking resemblance to previous albums". He added that the "better-than-average lyrics point to matters of significance while rarely touching the dirty things". Nick Catucci of Blender said in the context of Blink-182 and NOFX, "those bands bring humor and warmth into the mix; Pennywise still rely on pro forma antiauthority anthems". From the Ashes reached number 54 on the Billboard 200 and number 4 on the Top Independent Albums chart, marking the highest initial charting album in Pennywise's career.
```

## Album 143: Show No Mercy — Slayer

- **album_id:** `298fe1af-857e-47ee-a391-4fe353b5ffda`
- **Tags (identification only):** thrash metal, metal, speed metal, heavy metal, rock, speed/thrash metal, thrash
- **Chunks:** 7 (1630 words)

### Album 143, chunk 1

```text
Show No Mercy is the debut studio album by American thrash metal band Slayer, released in December 1983 by Metal Blade Records. Brian Slagel signed the band to the label after watching them perform an Iron Maiden cover. The band self-financed their full-length debut, combining the savings of vocalist Tom Araya, who was employed as a respiratory therapist, and money borrowed from guitarist Kerry King's father. Touring extensively promoting the album, the band brought close friends and family members along the trip, who helped backstage with lighting and sound. Although Show No Mercy was criticized for its poor production quality, it became Metal Blade's highest-selling release. It produced the songs "The Antichrist", "Die by the Sword" and "Black Magic", which were played at Slayer's live shows regularly. Slayer was the opening act for Bitch at the Woodstock Club in Los Angeles, performing eight songs—six being covers. While performing an Iron Maiden cover, the band was spotted by Brian Slagel, a former music journalist who had recently founded Metal Blade Records. Slagel met with the band backstage and asked if they would like to be featured on the label's upcoming Metal Massacre III compilation; the band agreed. The band's appearance on the compilation created underground buzz, which led to Slagel signing the band with Metal Blade Records. Recorded in Los Angeles, Show No Mercy was financed by vocalist Tom Araya, who used his earnings as a respiratory therapist, and money borrowed from guitarist Kerry King's father. King says the album is
```

### Album 143, chunk 2

```text
"fuckin' Iron Maiden here and there". Vocalist Araya asserts Venom, Judas Priest, Iron Maiden, and Mercyful Fate were big influences on the record, as guitarist King was into the Satanic image. Lombardo said in 2015 that he was not pleased with how the drums were recorded. The engineer at the time had difficulties getting the right mix between the toms and the cymbals because they were too loud. The solution was to dampen the cymbals with towels and record the toms and cymbals separately. As such, Lombardo called Show No Mercy his least favorite Slayer album, although he emphasized that the songs were great, just not his performance. Gene Hoglan, later known as the drummer for bands like Dark Angel and Death, provided backing vocals on the song "Evil Has No Boundaries". "Back at the time it was Jeff [Hanneman] and Kerry doing the 'Evil!' You know, it didn't sound too heavy and I mentioned to like Tom or Jeff or somebody like, 'You know you guys should consider...maybe consider doing like big gang vocals on that, make it sound evil like demons and stuff,' and they were like 'Good idea.' But how about now, we got about eight dudes sitting around in the studio, and now everybody jumped up and yelled 'EVIL!!!' So I was like 'Cool' because I'm like, 'I wanna sing on this record somehow, that's how I can do it,' totally unplanned you know?! Sure enough they were like, 'Fuck we have the time, let's do
```

### Album 143, chunk 3

```text
it.' So I was like 'Yeah, I got to sing on it!'" On recording the drums, Slagel wanted drummer Dave Lombardo to play without using cymbals due to the amount of noise they made, as he was unsure if he could siphon the noise out, which he eventually did. The band used Satanic themes in both lyrics and live performances to gain notice among the metal community and "to fuck with people". The back cover featured 'side 666' and inverted crosses, with Hanneman playing his guitar. Due to the imagery and lyrical content, Slayer received mail from the Parents Music Resource Center telling the band to stop releasing records. Araya comments, "Back then you had that PMRC, who literally took everything to heart. When in actuality you're trying to create an image. You're trying to scare people on purpose." The album produced the songs "The Antichrist", "Die by the Sword", and "Black Magic", which were played at Slayer's live shows regularly. Jeremy Ulrey of AllMusic characterized the sound on Show No Mercy as "basically amounting to a cleaned-up version of black metal stalwarts Venom." The album's lyrics explore themes including Satanism. Simon Young of Metal Hammer said of the album's cover artwork: "This is what happens when rural metal fans think it'll be a laugh to dress their goat in a cape, black swimming trunks and give them a sword. One minute, it's adorable, the next, your livestock is going fucking mental." After the album's release, the band went on
```

### Album 143, chunk 4

```text
their first US tour. Slagel gave the band a list of venue addresses and contact numbers. Araya was still working at the hospital and called the members, saying, "Today's the day. Are we gonna do this?" The band knew they never would if they did not tour now. So they set out taking Araya's Camaro and U-Haul. During the first leg of the tour, Slayer had no manager; Doug Goodman, who had met the band when he was first in line for their first show in Northern California (opening for Lȧȧz Rockit) took a vacation from his job at a grocery store to help out on the tour, eventually becoming the band's "tour guide". Goodman now tour manages acts such as Green Day and Beck. Kevin Reed, a friend of the band, set up the drums and lighting when touring with the band. Reed's father, Lawrence R. Reed, drew the album cover, which depicts Baphomet with a sword on the album's cover. Araya's younger brother, Johnny Araya, who was 13 or 14 at the time, was a roadie who set up the back line and sound. The band hardly made enough money to sustain themselves, only buying the "essentials" such as food, gas, and beer. Araya asserts, "We basically used whatever money we got to get from point A to point B. When we got back, Brian was like, 'So, where's the money?' And we were like, 'What money?' At that time, we didn't realize that you had to ask
```

### Album 143, chunk 5

```text
for money up front. I think he got a lot of money sent directly to him, and we were supposed to pick up the rest." The band performed in a hotel in Winnipeg, where the basement was the club. Araya comments, "We stayed there for like four or five days, I think. We saw Verbal Abuse play there. Then we played a place in Boston called the Lizard Lounge. In fact, a car had run into the front of the building, and it was all boarded up, but we still played there." When one of the guitarists broke a string Araya would hand them the bass, Hanneman stating, "We'd argue about it, too—like, 'I wanna play bass for a while!'" Although the band did not have enough time to sell any records while touring, the album became Metal Blade Records' highest selling release. Five thousand copies was the label's average. Show No Mercy went on to sell between 15,500 and 20,000 copies in the United States; it also went on to sell more than 15,000 overseas, as Metal Blade had worldwide rights. The success of the album led to Slagel wanting the band to release a new record and an EP. Show No Mercy was met with polarized opinions and reviews, mostly negative when it was issued, but in some recent reviews, it came to be considered a classic album. In 1984, Dave Dickson of Kerrang! crushed the album defining it "pure, unadulterated junk", while Bernard Doe of Metal Forces
```

### Album 143, chunk 6

```text
called the record "one of the heaviest, fastest, most awesome albums of all time!" The German magazine Rock Hard gave Show No Mercy a positive review, which remarked how Slayer were "actually the hardest and fastest" in comparison with their contemporaries Metallica and Exciter, and defined their music as "heavy metal punk." AllMusic reviewer Jeremy Ulrey had mixed feelings towards the album, saying that even though the musicianship and production were "amateurish" compared to Slayer's later releases, the album remains a "solid, if inessential, part of the Slayer legacy". Users voted 4/5 at AllMusic. Sputnikmusic staff member Hernan M. Campbell described the album as "fast, heavy, and mean, inducing an inescapable atmosphere of utter atrocity." He noted that the "lo-fi" production quality gives the album a "classic" feeling. Canadian journalist Martin Popoff praised Show No Mercy for being as "seminal" as Metallica's Kill 'Em All "in defining state-of-the-art speed metal" and for inspiring new bands to "expand the limits of metal." However, he "found the record stiff and one-dimensional", with "its style laid down in stifling arrangements." Fenriz, drummer for Darkthrone, cited Show No Mercy as the inspiration for the band's "current style of fusing NWOBHM with black metal". Terry Butler of Obituary and Death defined the album as "the blueprint for the beginning of death metal" and said: "When I heard Show No Mercy I wanted to play that way....It was a whole new level of mayhem. I wanted to play that way". System of a Down's Daron Malakian
```

### Album 143, chunk 7

```text
has praised Show No Mercy as an influential album that helped shape him as a person and artist. He claimed he introduced heavy metal to the people of Iraq with this album when he lived there at age 14. In 2023, Metal Hammer included the album cover on their list of "50 most hilariously ugly rock and metal album covers ever". Tom Araya – bass, vocals Jeff Hanneman – guitars, backing vocals on "Evil Has No Boundaries" Kerry King – guitars, backing vocals on "Evil Has No Boundaries" Dave Lombardo – drums Gene Hoglan – backing vocals on "Evil Has No Boundaries" Slayer – production Brian Slagel – executive production Bill Metoyer – engineering, mixing Steve Craig – cover concept and design, back cover and sleeve photography, logo and pentagram
```

## Album 144: From Here We Go Sublime — The Field

- **album_id:** `a8d7e225-58e6-4adc-b243-def33bab2d71`
- **Tags (identification only):** electronic, minimal techno, tech house, techno, microhouse
- **Chunks:** 2 (366 words)

### Album 144, chunk 1

```text
From Here We Go Sublime is the debut studio album by Swedish electronic music producer Axel Willner under his alias The Field, released by Kompakt on 26 March 2007. From Here We Go Sublime consists primarily of tracks recorded by Willner as the Field between 2004 and 2006, though the album also includes tracks produced before this period, one of which was originally recorded under a different alias. Willner's production style is sample-based, employing cut-up and resequenced manipulations of snippets of other artists' music, including Kate Bush's "Under Ice" on "Over the Ice", Lionel Richie's "Hello" on "A Paw in My Face", Fleetwood Mac's "Everywhere" on "Everyday", and The Flamingos' "I Only Have Eyes for You" on "From Here We Go Sublime". Despite From Here We Go Sublime being released on the Kompakt label, known primarily for German techno, the album's sound has been described as "less techno than it is trance". Jess Harvell of Pitchfork also noted the style's similarity due to an "anthemic bigness to Willner's little sounds, a certain shameless bombastic quality to the way he deploys his loops and builds his arpeggio" and the "elementary drum tracks, often just a deflated machine thump flecked with hi-hat hiss". The themes of the music on From Here We Go Sublime has been noted for its "unabashed emotionalism" with songs suggesting "bliss", "melancholy" and "loss". From Here We Go Sublime's song titles have been described as vague, and the songs themselves having no intelligible lyrics beyond sampled vocals which
```

### Album 144, chunk 2

```text
have been edited and chopped up. Willner dislikes lyrical content and chose to treat sampled vocals as instruments rather than as voices, as "it gives (the music) a special feeling." From Here We Go Sublime was released on compact disc and vinyl record by Kompakt. The album was released to great critical acclaim from various publications, and, along with Burial's Untrue, was the best-received album of 2007 on the music critic aggregators site Metacritic. It was named the 29th best album of the decade by Resident Advisor. Willner was surprised by the positive reception to the album, stating that "since it is a bit different than (most) other techno, I thought that people wouldn't like it."
```

## Album 145: Breakup Song — Deerhoof

- **album_id:** `fe7cf1cf-9330-4ef0-8393-9a870e85ba20`
- **Tags (identification only):** noise pop, art pop, electronic, experimental, experimental rock, funk rock, indie rock, indietronica
- **Chunks:** 1 (47 words)

### Album 145, chunk 1

```text
Breakup Song is the twelfth studio album by American experimental rock band Deerhoof. It was released on September 4, 2012 on Polyvinyl Records. A music video for the album's title track was released on June 3, 2013. It was directed by Pieter Dirkx. Deerhoof - performance, production
```

## Album 146: Peepshow — Siouxsie and the Banshees

- **album_id:** `b71b01eb-7d92-451e-9e39-4b2db816f595`
- **Tags (identification only):** gothic rock, rock, alternative rock, art pop, electronic, pop, post punk
- **Chunks:** 5 (1202 words)

### Album 146, chunk 1

```text
Peepshow is the ninth studio album by the English rock band Siouxsie and the Banshees, released in the United Kingdom on 5 September 1988 by Polydor Records. It was their first record as a quintet. With the arrival of multi-instrumentalist Martin McCarrick and guitarist Jon Klein, the group recorded a multifaceted album with a variety of influences. Peepshow included three singles "Peek-a-Boo", "The Killing Jar" and "The Last Beat of My Heart". Upon release, the album was critically acclaimed: praise centred around the unpredictability of the orchestrations and new nuances in Siouxsie Sioux's voice. The record was a commercial success, peaking at No. 20 in the UK, and No. 68 on the US Billboard 200 chart in the week of 3 December 1988. It spent a total of 20 weeks on that chart. "Peek-a-Boo" became the band's first American hit and reached number 53 on the Billboard Hot 100 chart. "Peek-a-Boo" also reached number one on the Billboard Alternative Songs chart and "the Killing Jar" got the number two spot. It is the subject of the 2018 book Peepshow by Samantha Bennett, part of the 33⅓ series. Music journalist Parke Puterbaugh described "Peek-a-Boo" as a "collage of sound that incorporates a backward percussion track" with the voice bouncing from channel to channel. "The Killing Jar" opens with "a faint splash of reggae" and then the music dissolves into a trancelike drone in the style of Brian Eno. "Scarecrow" has a "Middle-Eastern feel" and the first side rushes to a climax
```

### Album 146, chunk 2

```text
in "Burn-Up", with cello and drums "simulating a train's mounting momentum". On "Rhapsody", Siouxsie Sioux sang in high register as a soprano. The record was a commercial success, peaking at No. 20 in the UK, and No. 68 on the US Billboard 200 chart in the week of 3 December 1988. It spent a total of 20 weeks on that chart. The lead single "Peek-a-Boo" reached number one on the Billboard Alternative Songs chart and "the Killing Jar" got the number two spot. The album was remastered and reissued on CD with bonus tracks in October 2014. A 180g vinyl reissue, remastered from the original ¼” tapes and cut half-speed at Abbey Road Studios by Miles Showell, was released in December 2018. Upon release, the album was critically acclaimed. Q wrote in its 5 out of 5 star review: "Peepshow takes place in some distorted fairground of the mind where weird and wonderful shapes loom." Reviewer Mark Cooper hailed "Martin McCarrick's accordion that pokes its way into Peek A Boo ... a carny piece of musical imagination". He noted that "the rest of the record bursts with similar acts of imagination", saying: "full honours go to the aforementioned McCarrick for all manner of shrewd decorations and drummer Budgie for endlessly inventive rhythm work that manages to pinpoint the tension inherent in each song without ever lapsing into an obvious beat". Melody Maker highly praised its first single, "Peek-a-Boo", and called it "quite the most astounding British record" of 1988, and
```

### Album 146, chunk 3

```text
"a brightly unexpected mixture of black steel and pop disturbance." The paper also praised the band for the ballad "The Last Beat of My Heart". Chris Roberts said: "The infinite pinnacle is their one joint effort, the bravura hymn "The Last Beat of My Heart"". As Martin McCarrick's accordion and Budgie's directly intelligent rhythms underlie its pathos, this elegy is translated by Sioux with capital beatitude. It's the Banshees' most courageous arabesque in some time." Record Mirror also particularly enjoyed that song when reviewing the album: "The highlight is the restrained 'The Last Beat of My Heart', where Siouxsie's voice explores new ground as she caresses a haunting melody." Reviewer Kevin Murphy concluded by saying: "Brimming with confidence ..., Peepshow is the Banshees' finest hour." NME noted a change of approach in the musical direction: "Peepshow is the best Banshees record since A Kiss in the Dreamhouse because it's the Banshees deciding to be a pop band rather than a rock group". In the US, Spin published a glowing review of the album in their November issue. Discussing "Peek-a-Boo", critic Tony Fletcher said that its "mood fell in perfectly with their beloved London's summer fascination with the sparsity and confusion that call Acid House, Psychedelic and how!" He described the music of "Peek-a-Boo" as "a crazed assortment of fairground accordions, abrupt horns, distant to-and-fro vocals-exotic, erotic, a dancefloor winner for sure and all of three minutes short." Fletcher also hailed the other tracks, noting "an almost lilting reggae feel to
```

### Album 146, chunk 4

```text
the beginning of "Killing Jar", a fragile, waif-like Siouxsie backed only by translucent guitar and a keyboard bass on the brief "Rawhead and Bloodybones", and a delightful, majestic ballad the likes of which it had been a safe assumption was beyond their reach on "The Last Beat of My Heart". [...] As Peepshow ends with the drawn-out "Rhapsody", Siouxsie's operatic flings seem to be a celebration of her reawakened capacity to thrill." Fletcher concluded: "She and the band sound as confident, abandoned and excited as when they started". In Stereo Review, the album was published in the column "Best of the Month". Reviewer Parke Puterbaugh wrote that the record was "a fascinating plunge into the subconscious" and was "Dream-like" and "hypnotic", further emphasizing, "Peepshow brims with nonlinear logic, compulsive rhythms, and icy, crystalline textures." The critic concluded his review, qualifying it as an "utterly unconventional and thoroughly intoxicating album" ... "a transcendent feat: They are not playing music, the music is playing them". Peepshow was listed by Q magazine as one of the top 50 albums of 1988. The readers of Best music magazine rated it the 6th best album of the year. AllMusic published a four-and-a-half -out-of-five-star review writing: "showcasing the band's [...] ability to always provide an accomplished variety of sound and approach while still recognizably maintaining a uniquely Banshees style -- Peepshow is the sound of a band reenergized". The 2004 edition of The Rolling Stone Album Guide gave Peepshow a rating of 2.5 stars out of
```

### Album 146, chunk 5

```text
five, saying that the album mixes "synthesizers and a lighter pop touch with the Banshees' trademark howl", but the combination "lacks spark". In contrast a 2014 review in The Daily Telegraph praised the record, saying that "lush, folk-rock orchestration produced perfect pop". Bloc Party later praised "Peek-a-Boo", which their singer Kele Okereke described: "It sounded like nothing else on this planet. This is just a pop song [...], but to me it sounded like the most current but most futuristic bit of guitar-pop music I've heard." DeVotchKa later covered "The Last Beat of My Heart" at the suggestion of Arcade Fire singer Win Butler. Colin Meloy of The Decemberists also mentioned "The Last Beat of My Heart" as one of his favorite Siouxsie and the Banshees songs. Peepshow was also one of the albums Nic Offer of the band !!! ("Chk Chk Chk"), listened to the most during his formative years. Emel Mathlouthi recorded a rendition of "Rhapsody" as a one-off for French Television, saying that the lyrics were close to her. Siouxsie Sioux – vocals Steven Severin – electric bass Budgie – drums, percussion and harmonica Martin McCarrick – cello, keyboards, accordion Jon Klein – guitar Mike Hedges – producer, engineer
```

## Album 147: Ghosts V: Together — Nine Inch Nails

- **album_id:** `422d0f61-7ccc-40a3-ae10-878f44b6a5e9`
- **Tags (identification only):** ambient, dark ambient, drone, hardnheavy, heavy metal, industrial
- **Chunks:** 3 (636 words)

### Album 147, chunk 1

```text
Ghosts V: Together is the tenth studio album by the American industrial rock band Nine Inch Nails. It was released as a free download on March 26, 2020, as a show of solidarity with the band's fans during the COVID-19 pandemic. It is a follow-up to the 2008 instrumental album Ghosts I–IV, and released simultaneously with their eleventh album, Ghosts VI: Locusts. In 2019, after releasing their eighth soundtrack to the film Bird Box, Trent Reznor and Atticus Ross completed a subsequent score for The Woman in the Window; however, when the production studio decided to re-edit the film after test screenings, Reznor and Ross's score was withdrawn. When discussing the project, Reznor admitted, "It's frustrating when you did that much work and it's gone. And we were proud—and they were proud—of the movie that it was." In March 2020, following two subsequent 2019 soundtracks Watchmen and Waves, Reznor announced two unexpected releases, Ghosts V: Together and Ghosts VI: Locusts, for free download through the official Nine Inch Nails website, YouTube channel, and streaming platforms: "Hours and hours of music. Free. Some of it kind of happy, some not so much." The band's website added, "As the news seems to turn ever more grim by the hour, we've found ourselves vacillating wildly between feeling like there may be hope at times to utter despair—often changing minute to minute. Although each of us define ourselves as antisocial-types who prefer being on our own, this situation has really made us appreciate the
```

### Album 147, chunk 2

```text
power and need for CONNECTION." Two tracks from the album have been featured in the FX comedy-drama television series The Bear: "Hope We Can Again" featured in the season two finale, "The Bear", and "Together" subsequently featured extensively in the season three premiere, "Tomorrow". According to the review aggregator Metacritic, Ghosts V: Together received "universal acclaim" based on a weighted average score of 81 out of 100 from 11 critic scores. James McMahon of NME referred to the album as "more soothing than balm," and "a soundtrack to an edit of 2001: A Space Odyssey where no-one dies." Rolling Stone's Kory Grow thought that Ghosts V and Ghosts VI "felt like distinct artistic statements unlike the first Ghosts collection." Grow also remarked that Ghosts V was "spacious with gentle buzzing, humming, and exhaling drones that slowly evolve, complementing often pretty piano music." Sean T. Collins of Pitchfork considered the record as "solidly the stronger of the two", noting that "throughout, there's a vibe of quiet optimism". For Jon Pareles of The New York Times, "the more approachable of the two albums," Ghosts V is "largely meditative, circling through melodic patterns and touching down in consonance. The music is not entirely soothing [...] but it hints at some possibility of confluence, stability and eventual resolution." The album "has prettier, warmer ingredients [...], serenely elegiac piano melodies, counterpoint in plinking bell tones and choirs of sampled voices." Spin critic John Paul Bullock described both records as "heady, confrontational albums that, like the
```

### Album 147, chunk 3

```text
best art, force consideration and conversation" while noting them to be "definitely not a polite distraction from what's going on in the world outside of your home." Bullock further thought that the tracks on Ghosts V are "big, bold, dynamic, and show a particular mastery of modular synthesis" and various influences on the record do not "overshadow the originality of Reznor and Ross's sound." Sputnikmusic critic Simon regarded Ghosts V as "more organic and acoustic sounding" than Ghosts VI, and remarked that the record "features a calmer, at times relaxed sound, yet you can feel tension slowly mounting around you." Neil Z. Yeung made a similar comparison in the review for AllMusic, claiming the album is "the warm yang to its partner's darker yin, an atmospheric and soothing work that aims to comfort and offer hope."
```

## Album 148: Oriental Beat — Hanoi Rocks

- **album_id:** `89fe0fec-0804-4169-9257-94b8cf5163d5`
- **Tags (identification only):** hard rock, heavy metal, finland, finnish, glam, glam punk, pop metal, rock
- **Chunks:** 3 (581 words)

### Album 148, chunk 1

```text
Oriental Beat is the second studio album by the Finnish glam punk band Hanoi Rocks, recorded in London and released in 1982. Oriental Beat also opened markets in the UK and Japan, where Hanoi eventually became very popular. Recordings for Oriental Beat (then with the working-title, Second Attempt for Suicide) started in late 1981, at the Advision-studio in London. The album was produced, recorded and mixed by Peter Wooliscroft who had worked with Frank Zappa for example. This album also marked the first time McCoy was not the sole songwriter, with Monroe being the second songwriter on the songs "Motorvatin'" and "Teenangels Outsiders". Many of the lyrics deal with typical rock n' roll topics like breaking the law ("No Law or Order) and teenage rebellion ("Teenangels Outsiders"). The album features backing vocals by Katrina Leskanich, the lead singer of Katrina and the Waves. There's also a legend that originally Nasty Suicide sang the song "Devil Woman", but when asked about it Suicide replied: "you know too much". The previous album, Bangkok Shocks, Saigon Shakes, Hanoi Rocks, was only released in Finland and Sweden, but this album opened the doors to an international career. British music magazine Kerrang! released their first article about Hanoi Rocks, when they reviewed Oriental Beat. Kerrang! since covered Hanoi Rocks career in the 80s extensively. The artwork features the band covered in paint behind a glass panel with blue and red paint-pressed hand marks on it. The artwork was originally supposed to feature guitarist Andy McCoy's
```

### Album 148, chunk 2

```text
girlfriend's naked breasts painted blue and red with the legend "Hanoi Roxx" written across it. This was changed due to Castle Records' view that some record shops may refuse to stock the album due to the graphic nature of the cover. The record company was also worried that potential customers may get confused by the alternate spelling of the band's name. The original cover was used as the album's back cover. Over the years, Hanoi Rocks members have stated their dissatisfaction with the mixing of Oriental Beat. The original multitrack recordings of the album were found in 2020 after being lost for over 30 years and a newly mixed version, labeled Oriental Beat - 40th Anniversary Re(al)mix was released on March 17, 2023. The new version peaked at #2 on the Finnish Albums Chart and #1 on the Finnish Physical Albums Chart. Even though Oriental Beat is considered a Hanoi classic, many of the band members have called the album a failure. Michael Monroe has called the album great, but blamed the producer, Pete Wooliscroft, of ruining the album's sound with all-around bad producing and mixing, claiming that Wooliscroft had mixed the album while Hanoi Rocks was on tour, didn't know what Hanoi Rocks was about, and had mixed it without understanding the band's aesthetic. Sami Yaffa called the album "a piece of shit" in a 1985 interview. Even with these comments, the album was voted the 91st best rock album in the "100 Greatest Rock Albums" poll by the
```

### Album 148, chunk 3

```text
Finnish radio station Radio Rock. Oriental Beat beat out such albums as Kiss' Lick It Up and The Doors' Morrison Hotel. The song "Fallen Star" features in the episode titled "Monkey Dory" of the 2022 TV-series Peacemaker. Michael Monroe – vocals, saxophone, harmonica Andy McCoy – guitar, backing vocals Nasty Suicide – guitars, backing vocals Sam Yaffa – bass Gyp Casino – drums Katrina Leskanich – backing vocals on "Don't Follow Me" Producer: Pete Wooliscroft Mixing: Pete Wooliscroft Mastering: Pete Wooliscroft
```

## Album 149: Vagabond Heart — Rod Stewart

- **album_id:** `1249496a-7999-46df-9b78-0109839601b1`
- **Tags (identification only):** adult contemporary, rock, soft rock rock, soft rock, am pop, pop
- **Chunks:** 4 (804 words)

### Album 149, chunk 1

```text
Vagabond Heart is the sixteenth studio album by British recording artist Rod Stewart, released on 25 March 1991 by Warner Bros. Records. The album reached No. 10 in the US, and reached No. 2 in the UK. The album features five singles, among them a cover of Robbie Robertson's song "Broken Arrow" (No. 20 in the US) and Van Morrison's song "Have I Told You Lately", which would become a hit two years later (in a live version), and is Stewart's most recent top five solo hit in the US and the UK. The two biggest hits from the album were "Rhythm of My Heart" (No. 3 in the UK/No. 5 in the US) and "The Motown Song" (No. 10 in the UK and US). The latter song features with Steve Lukather, David Paich, Steve Porcaro and Jeff Porcaro—nearly all of the band Toto. The "Vagabond Heart Tour" was made available on video in 1992, shot during a concert in Los Angeles on Valentine's Day. Overall, the album received positive reviews. According to Rolling Stone, "Vagabond Heart finds Stewart rising to new challenges as both a songwriter and a singer. The strength of the songs and the depth of Stewart's conviction make this his most compelling work since the early 1970s." AllMusic felt the album was "stronger, more diverse album than its predecessor, Out of Order, featuring a more consistent set of songs." Rod Stewart – vocals Richard Cottle – keyboards (1) Kevin Savigar – keyboards (1, 2, 5, 6,
```

### Album 149, chunk 2

```text
9, 13), string arrangements and conductor (1) Mick MacNeil – accordion (1) Gary Maughn – Fairlight programming (1) Chuck Kentis – keyboards (2, 4–6, 8–11), drum programming (5, 9) Patrick Leonard – keyboards (3) David Paich – acoustic piano (7), electric piano (7), basic track arrangements (7) Steve Porcaro – synthesizers (7) Steve Lindsey – synthesizers (7), synth horns (7), horn arrangements (7) Robin Le Mesurier – guitars (1) Steve Lukather – guitars (1, 7) Jeff Golub – guitars (2, 4–6, 8–11), acoustic guitar (13), electric guitar (13) Dann Huff – guitars (2), guitar solo (2) Tim Pierce – guitars (3) Paul Jackson Jr. – guitars (7) Waddy Wachtel – guitars (8), guitar solo (8) Jim Cregan – guitars (9) Neil Stubenhaus – bass guitar (1) Carmine Rojas – bass guitar (2, 5, 9, 11) Jimmy Johnson – bass guitar (3) Bernard Edwards – bass guitar (4–6, 8, 10) Khris Kellow – synth bass (7) John Robinson – drums (1) Rave Calmer – drums (2, 4, 8, 10, 11, 13) Jim Keltner – drums (3) Tony Brock – drums (6) Jeff Porcaro – drums (7) Luis Conte – percussion (3) Chris Trujillo – percussion (7) Paulinho da Costa – percussion (10, 13) Kevin Weed – bagpipes (1) Jimmy Roberts – saxophones (2, 8), sax solo (4, 11) Nick Lane – trombone (2) Rick Braun – trumpet (2) Richard Greene – violin (6) Bruce Miller – string arrangements and conductor (5, 10) Nick Strimple – choir director (1) Joe Turano –
```

### Album 149, chunk 3

```text
choir director (1), backing vocals (1) John Batdorf – backing vocals (1) Lionel Conway – backing vocals (1) Jerry Cook – backing vocals (1) Randy Crenshaw – backing vocals (1) Gary Falcone – backing vocals (1) Roger Freeland – backing vocals (1) Robert Jason – backing vocals (1) Arnold Stiefel – backing vocals (1) Roy Galloway – backing vocals (2) Luther Waters – backing vocals (2) Twinkle Schascle – backing vocals (3) Tina Turner – vocals (4) The Waters – backing vocals (6, 8, 9, 11) The Temptations – backing vocals (7) Angela Winbush – backing vocals (11), additional vocals (11) Malcolm Cullimore – production coordinator (1–6, 8–13) Julie Larson – production coordinator (7) Nancy Poertner – project manager Stephen Marcussen – mastering at Precision Mastering (Hollywood, CA) Steve MacMillan – engineer (1, 2, 4–11, 13), mixing (1, 2, 4–11, 13) Trevor Horn – mixing (1) Bernard Edwards – mixing (2, 4–6, 8–11, 13) Jerry Jordan – engineer (3), mixing (3) Bryant Arnett – assistant engineer (2, 4–6, 8–11, 13) John Karpowich – assistant engineer (2, 4–11, 13) Gil Morales – assistant engineer (2, 4–6, 8–11, 13) "Rhythm of My Heart" copyright WB Music Corp./Jamm Music/Bibo Music Publishers. "Rebel Heart", "When a Man's in Love" and "Moment of Glory" published by Rod Stewart (Intersong Music Admin.)/Cat in the Hat Music/Kentis Music/Malango Bro. "Broken Arrow" published by Medicine Hat Music. "It Takes Two" published by Stone Agate Music Division. "You Are Everything" published by Assorted Music/Bellboy Music/The Mighty Three Group. "The
```

### Album 149, chunk 4

```text
Motown Song" published by Geffen Music/McNally Music Publishing/MCA Music Publishing. "Go Out Dancing" published by Rod Stewart (Intersong Music Admin.)/Cat in the Hat Music/Kentis Music. "No Holding Back" and "If Only" published by Rod Stewart (Intersong Music Admin.)/Almo Music Corp/Kevin Savigar Music/BMG Inc. "Have I Told You Lately" published by PolyGram International Publishing, Inc.
```

## Album 150: Hanoï — Indochine

- **album_id:** `9c92a574-f307-475a-8f90-ebdd84d43812`
- **Tags (identification only):** electronic, new wave, synth pop, 2007, france, francophone, français, french
- **Chunks:** 1 (45 words)

### Album 150, chunk 1

```text
Hanoï is the sixth live album by French new wave band Indochine. It was released in February 2007. It is a recording of a performance that took place on 6 June 2006. The album takes its name from the location of the concert, Hanoi, Vietnam.
```
