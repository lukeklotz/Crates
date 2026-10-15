# Sound-filtered Wikipedia text: results and LLM grading task (2026-10-15)

This file has two parts. **Part 1** records what the experiment changed and what was measured without grades; read it for context only. **Part 2** is the grading task: do it exactly as instructed there. Your grades decide whether the change is kept.

## Part 1: experiment results

### Background

Crate recommends albums. The embedding recommender represents each album as two vectors made by the sentence encoder `BAAI/bge-small-en-v1.5`:

- a **tag vector**, from the album's top 20 genre/tag terms written as one line;
- a **text vector**, the average of the vectors of its cleaned English Wikipedia article, split into 250-word chunks.

When both albums have text, similarity = 0.6 × tag cosine + 0.4 × text cosine. Otherwise it's the tag cosine alone. Cosine similarity is 1.0 for vectors pointing the same way and lower for less similar ones.

### Problem found

Of the 25,000 catalog albums, 12,799 (51%) have article text. Most of that text is not about how the album sounds:

- **What it's made of:** release dates and labels, chart positions, tours, band biography, recording studios, and personnel lists. Sections that describe the sound (composition, music, musical style) are under 10% of article words.
- **Same artist:** text-only nearest neighbours were by the seed's own artist 23.6% of the time. With Teeth's text neighbours were five other Nine Inch Nails albums.
- **Famous rock albums cluster together:** The Stone Roses' text neighbours were three Rolling Stones albums, Oasis and the Beatles, all at cosine about 0.91.
- **Short articles give noisy neighbours:** Misguided Roses (folk rock) matched Chicago 18 and Lara Fabian.

### Change tested: variant `embed-tags+sound`

Before chunking, each article is split into sentences, and only sentences that describe the sound are kept:

- **Credit lines** ("Name – bass guitar") are dropped outright.
- **Every other sentence** is embedded with the same encoder and compared with 16 hand-written "describes sound" examples (e.g. "jangly guitars over a loose, danceable groove") and 15 "not about sound" examples (e.g. "it peaked at number three on the Billboard 200").
- **Keep rule:** the sentence is kept when its mean similarity to its 3 closest sound examples is higher than its mean similarity to its 3 closest not-sound examples.

Everything else is unchanged from `embed-tags+text`, including tag vectors and α = 0.6. An album that keeps no sentences gets no text vector and is compared on tags alone.

### Build statistics

| Measure | Value |
|---|---|
| Sentences kept | 124,943 of 565,178 (22%) |
| Albums with a text vector | 11,087 (was 12,799) |
| Albums whose text was all filtered out | 1,712 |
| Hand check on 300 sampled articles | about 2 in 3 kept sentences describe the sound; nearly all dropped sentences don't |

### Proxy measurements (no grades yet)

Text-only nearest neighbours, top 10, for 1,500 random albums that have both tags and text:

| Measure | Old text (`embed-tags+text`) | Sound-filtered (`embed-tags+sound`) |
|---|---|---|
| Neighbours by the same artist | 23.6% | 9.4% |
| Neighbours sharing the seed's top genre/tag, same-artist neighbours excluded | 12.3% | 9.8% |
| Mean cosine between two random albums (lower = more spread out) | 0.646 | 0.605 |

Text-only neighbour examples, old → sound-filtered:

- **The Stone Roses:** Black and Blue, Hackney Diamonds, Definitely Maybe, The Beatles, Some Girls → Chinese Democracy, A Northern Soul (The Verve), (What's the Story) Morning Glory?, The Beatles, Queens of the Stone Age.
- **With Teeth (Nine Inch Nails):** five Nine Inch Nails albums → The Fragile, Siamese Dream, …And Justice for All, Chinese Democracy, The Downward Spiral.
- **Chaosphere (Meshuggah):** Nothing (Meshuggah), Follow the Reaper, Burn My Eyes, RE-ANIMATOR (Everything Everything), Stormblåst → HEX (Earth), War Master (Bolt Thrower), Start a War (Static-X), The End of All Things to Come (Mudvayne), Chaos A.D. (Sepultura).

**What this says:** the filter clearly cut same-artist matches. Genre agreement fell slightly, but genre-tag agreement is a crude stand-in for recommendation quality. Graded relevance (Part 2) is the real test.

### Previous graded results, for reference (human grades, 2026-10-09, 10 seeds)

| Variant | NDCG@5 | Recall@5 | Judged@5 |
|---|---|---|---|
| tfidf-tags | 0.717 | 0.578 | 1.00 |
| embed-tags | 0.314 | 0.242 | 0.46 |
| embed-tags+text | 0.252 | 0.200 | 0.48 |

How to read this table:
- **NDCG@5** is a 0-to-1 ranking-quality score over each variant's top 5 picks: higher is better, and good picks near the top count more.
- **Judged@5** is the share of those top-5 picks that have a grade.
- The embedding rows were only about half graded, so their scores are not yet trustworthy. Part 2 grades every remaining top-5 pick of `embed-tags`, `embed-tags+text` and `embed-tags+sound` so all three can be compared fairly.

## Part 2: grading task for an LLM

You are grading album recommendations for Crate, an album recommender. For each **seed** album below, grade every **candidate** album on how good a recommendation it is for someone who loves the seed. Use your own knowledge of the music; the tags and Wikipedia sentence are there to identify the album, not as the only evidence.

### Rubric (identical to the human grader's)

| Grade | Meaning |
|---|---|
| 2 | I'd recommend it to someone who loves the seed. |
| 1 | Clearly related and plausible. |
| 0 | Not relevant. |

Rules:
- Grade same-artist albums on their merits, neither bonus nor penalty for sharing the artist.
- Grade each candidate independently against its seed. Don't rank candidates against each other, and don't spread grades out on purpose: all 2s or all 0s is fine.
- You don't know which recommender produced a candidate. Candidates are shuffled and duplicates removed.
- If you don't recognize an album, grade from its tags and Wikipedia sentence, and say so in `note`.

### Output format

Reply with **one fenced `jsonl` block** with exactly one line per candidate, in any order, and nothing else inside the block. Copy `seed_id` and `candidate_id` exactly from the `ids` lines. `note` is a short reason (at most 15 words).

```jsonl
{"seed_id": "<seed id>", "candidate_id": "<candidate id>", "grade": 2, "note": "same dream pop sound, ethereal vocals"}
```

Total to grade: **48 candidates across 10 seeds**.

### Seed: Not Too Late — Norah Jones

- **Seed id:** `c554909b-935f-4b53-b784-1e209ad2036c`
- **Album:** Not Too Late — Norah Jones (2006)
- **Top tags:** jazz, contemporary jazz, jazz blues, vocal jazz, adult alternative pop/rock, alternative rock, alternative/indie rock, contemporary, contemporary jazz vocals, indie rock, jazz and blues, pop/rock
- **Wikipedia first sentence:** Not Too Late is the third studio album by American singer-songwriter Norah Jones, released on January 30, 2007, through Blue Note Records.

Candidates (7):

#### Candidate 1
- **ids:** seed_id `c554909b-935f-4b53-b784-1e209ad2036c`, candidate_id `d27a3964-9f40-4234-84b2-35dd1211d69d`
- **Album:** Both Sides Now — Joni Mitchell (2000)
- **Top tags:** adult contemporary, contemporary jazz, folk, folk rock, vocal jazz, jazz, singer songwriter, standards
- **Wikipedia first sentence:** Both Sides Now is a concept album and the seventeenth studio album by Canadian singer-songwriter Joni Mitchell that was released in 2000.

#### Candidate 2
- **ids:** seed_id `c554909b-935f-4b53-b784-1e209ad2036c`, candidate_id `34e5ec6a-f6c7-4b25-8f87-a4b9860ff471`
- **Album:** 20th Jun Togawa — 戸川純 (2000)
- **Top tags:** alternative rock, avant garde jazz, contemporary jazz, electronic, experimental, j pop, jazz, pop

#### Candidate 3
- **ids:** seed_id `c554909b-935f-4b53-b784-1e209ad2036c`, candidate_id `7598ed1b-62c5-465c-875a-4e8dee9663df`
- **Album:** Painted From Memory — Elvis Costello (1998)
- **Top tags:** adult contemporary, ballad, easy listening, jazz, adult alternative pop/rock, alternative/indie rock, baroque pop, contemporary pop/rock
- **Wikipedia first sentence:** Painted from Memory is a collaboration album by Elvis Costello and Burt Bacharach, released on 29 September 1998 through Mercury Records, a division of Universal Music Group.

#### Candidate 4
- **ids:** seed_id `c554909b-935f-4b53-b784-1e209ad2036c`, candidate_id `9c8fed90-7c49-44cd-9c62-d9d6301b26fa`
- **Album:** Mecca for Moderns — The Manhattan Transfer (1981)
- **Top tags:** jazz, adult contemporary, bop, contemporary jazz, harmony vocal group, mainstream jazz, pop/rock, rock
- **Wikipedia first sentence:** Mecca for Moderns is the sixth studio album by the Manhattan Transfer.

#### Candidate 5
- **ids:** seed_id `c554909b-935f-4b53-b784-1e209ad2036c`, candidate_id `79e00cee-582f-4160-8af4-92e57a45d4ab`
- **Album:** Chimera — Ardecore (2007)
- **Top tags:** alternative rock, ballad, blues, blues rock, contemporary jazz, experimental, folk rock, jazz

#### Candidate 6
- **ids:** seed_id `c554909b-935f-4b53-b784-1e209ad2036c`, candidate_id `174337a4-981a-40b3-8bcd-c66591f569c4`
- **Album:** Brasil — The Manhattan Transfer (1987)
- **Top tags:** contemporary jazz, jazz, adult contemporary, bop, harmony vocal group, latin jazz, mainstream jazz, pop

#### Candidate 7
- **ids:** seed_id `c554909b-935f-4b53-b784-1e209ad2036c`, candidate_id `2bbcd314-022d-42ee-9ff3-a7bf0b34d9e8`
- **Album:** Unforgettable: With Love — Natalie Cole (1991)
- **Top tags:** jazz, adult contemporary, pop/rock, r and b, rock, soul, vocal
- **Wikipedia first sentence:** Unforgettable ...

### Seed: Heaven or Las Vegas — Cocteau Twins

- **Seed id:** `6b7cb74a-df56-4da9-bc11-0f086b779201`
- **Album:** Heaven or Las Vegas — Cocteau Twins (1990)
- **Top tags:** dream pop, downtempo, ethereal wave, rock, shoegaze, alternative rock, ambient, ambient pop, electronic
- **Wikipedia first sentence:** Heaven or Las Vegas is the sixth studio album by the Scottish band Cocteau Twins, released on 17 September 1990 by 4AD.

Candidates (5):

#### Candidate 8
- **ids:** seed_id `6b7cb74a-df56-4da9-bc11-0f086b779201`, candidate_id `60fb03ec-4b56-4b6f-b3ae-646c6d394388`
- **Album:** Chances — Acopia (2022)
- **Top tags:** ambient, electronica, trip hop, downtempo, dream pop, electronic, pop, shoegaze

#### Candidate 9
- **ids:** seed_id `6b7cb74a-df56-4da9-bc11-0f086b779201`, candidate_id `9a7e4a83-84ea-4e6e-98ff-db2e2fe85206`
- **Album:** BBC Sessions — Cocteau Twins (1999)
- **Top tags:** downtempo, dream pop, electronic, rock, ethereal, ethereal wave, indie, post punk
- **Wikipedia first sentence:** BBC Sessions is an album of BBC studio recordings by the band Cocteau Twins released in 1999 by Bella Union in the UK and Rykodisc in the US.

#### Candidate 10
- **ids:** seed_id `6b7cb74a-df56-4da9-bc11-0f086b779201`, candidate_id `6173180a-8781-4121-834b-08ecd5affd1c`
- **Album:** Euphoric Recall — MØAA (2021)
- **Top tags:** ambient, dark wave, dream pop, ethereal wave, indie, indie rock, noise pop, pop

#### Candidate 11
- **ids:** seed_id `6b7cb74a-df56-4da9-bc11-0f086b779201`, candidate_id `a491328f-0fc8-4119-b432-e698ce75d9ac`
- **Album:** Blood — This Mortal Coil (1991)
- **Top tags:** rock, ambient, dream pop, electronic, ethereal wave, experimental, alternative, ambient pop
- **Wikipedia first sentence:** Blood is the third and final album released by 4AD collective This Mortal Coil, an umbrella title for a loose grouping of guest musicians and vocalists brought together by label co-founder Ivo Watts-Russell.

#### Candidate 12
- **ids:** seed_id `6b7cb74a-df56-4da9-bc11-0f086b779201`, candidate_id `3fb421ba-ba30-48dc-9e74-1fec34e5bd27`
- **Album:** Milk & Kisses — Cocteau Twins (1996)
- **Top tags:** rock, dream pop, electronic, ambient, ambient dream pop, ethereal, ethereal wave, pop
- **Wikipedia first sentence:** Milk & Kisses is the eighth and final studio album by Scottish rock band Cocteau Twins, released on 15 April 1996 in the United Kingdom by Fontana Records and on 14 May 1996 in the United States by Capitol Records.

### Seed: Until the Quiet Comes — Flying Lotus

- **Seed id:** `c76e2269-3608-474e-84f3-b4d859ea945f`
- **Album:** Until the Quiet Comes — Flying Lotus (2012)
- **Top tags:** electronic, award/qobuz/qobuzissime, experimental, hip hop, jazz
- **Wikipedia first sentence:** Until the Quiet Comes is the fourth studio album by American electronic music producer Flying Lotus, released on September 26, 2012 by Warp Records.

Candidates (8):

#### Candidate 13
- **ids:** seed_id `c76e2269-3608-474e-84f3-b4d859ea945f`, candidate_id `efe838ee-c5a9-4310-9525-759c38ef0c77`
- **Album:** Huge Samurai Radish — Raoul Sinier (2007)
- **Top tags:** electronic, experimental, glitch, electro, hip hop

#### Candidate 14
- **ids:** seed_id `c76e2269-3608-474e-84f3-b4d859ea945f`, candidate_id `e4ac4ec1-53b9-4910-94db-75b27026e0c6`
- **Album:** If You Wait — London Grammar (2013)
- **Top tags:** indie rock, indie pop, rock, art pop, award/qobuz/qobuzissime, dream pop, electronic, pop
- **Wikipedia first sentence:** If You Wait is the debut studio album by English indie pop band London Grammar, released on 6 September 2013 by Metal & Dust Recordings and Ministry of Sound.

#### Candidate 15
- **ids:** seed_id `c76e2269-3608-474e-84f3-b4d859ea945f`, candidate_id `8be5930b-b05a-46ea-9b24-c7a04c2b320a`
- **Album:** Athena — Sudan Archives (2019)
- **Top tags:** alternative r and b, ambient pop, art pop, award/qobuz/qobuzissime, folktronica, hip hop, neo soul, r and b
- **Wikipedia first sentence:** Athena is the debut studio album by American musician Sudan Archives.

#### Candidate 16
- **ids:** seed_id `c76e2269-3608-474e-84f3-b4d859ea945f`, candidate_id `6e33b764-6b84-4121-adf1-37ec1b8d5d58`
- **Album:** Des lumières sous la pluie — Psykick Lyrikah (2004)
- **Top tags:** electronic, experimental, hip hop, instrumental

#### Candidate 17
- **ids:** seed_id `c76e2269-3608-474e-84f3-b4d859ea945f`, candidate_id `687f9246-ea3b-4cc6-a37b-6ff537c08ff9`
- **Album:** Ectopia — Steroid Maximus (2002)
- **Top tags:** jazz, electronic, experimental, free jazz, industrial, electronica

#### Candidate 18
- **ids:** seed_id `c76e2269-3608-474e-84f3-b4d859ea945f`, candidate_id `147655fa-3718-4708-a1ed-ed454f66875f`
- **Album:** Дикие — EU (2006)
- **Top tags:** electronic, experimental, idm, abstract, hip hop

#### Candidate 19
- **ids:** seed_id `c76e2269-3608-474e-84f3-b4d859ea945f`, candidate_id `432d7e19-a28e-4047-bd23-13880b8ca4f7`
- **Album:** With a Hammer — Yaeji (2023)
- **Top tags:** electronic, alternative r and b, art pop, award/qobuz/qobuzissime, dance pop, glitch pop, house, jungle
- **Wikipedia first sentence:** With a Hammer is the debut studio album by American musician Yaeji.

#### Candidate 20
- **ids:** seed_id `c76e2269-3608-474e-84f3-b4d859ea945f`, candidate_id `939f746e-d153-4f5a-bd86-094d5e033acd`
- **Album:** Butter for the Fat — Tacteel (2002)
- **Top tags:** electronic, hip hop, instrumental, abstract

### Seed: Monkey Business — The Black Eyed Peas

- **Seed id:** `1c31e4ba-97d6-4a01-bb7c-6373c7f4f1db`
- **Album:** Monkey Business — The Black Eyed Peas (2005)
- **Top tags:** hip hop, pop rap, dance pop, conscious, pop, conscious hip hop, club, dance, electronic, funk, hip hop rap
- **Wikipedia first sentence:** Monkey Business is the fourth studio album by American group the Black Eyed Peas.

Candidates (6):

#### Candidate 21
- **ids:** seed_id `1c31e4ba-97d6-4a01-bb7c-6373c7f4f1db`, candidate_id `bced9663-dc60-4591-9699-dbc29f41625f`
- **Album:** 3615 TTC — TTC (2006)
- **Top tags:** electro, electronic, pop, hip hop, pop rap

#### Candidate 22
- **ids:** seed_id `1c31e4ba-97d6-4a01-bb7c-6373c7f4f1db`, candidate_id `16726d4c-2526-4a19-ac09-b764558b93ac`
- **Album:** Music for the People — Marky Mark and the Funky Bunch (1991)
- **Top tags:** club/dance, dance pop, electronic, electronic/trance/hiphop/jazz, hip hop, hip house, party rap, pop
- **Wikipedia first sentence:** Music for the People is the debut studio album by American hip hop group Marky Mark and the Funky Bunch, released on July 23, 1991.

#### Candidate 23
- **ids:** seed_id `1c31e4ba-97d6-4a01-bb7c-6373c7f4f1db`, candidate_id `43b81eee-3102-4051-a77d-3c788e73dd8a`
- **Album:** Vom selben Stern — Ich + Ich (2007)
- **Top tags:** pop, ballad, general hip hop rap, pop rock, rock, dance pop, electronic, soul

#### Candidate 24
- **ids:** seed_id `1c31e4ba-97d6-4a01-bb7c-6373c7f4f1db`, candidate_id `bee5a7d3-4519-4405-8c14-c2b59c7f2609`
- **Album:** Raw Like Sushi — Neneh Cherry (1989)
- **Top tags:** pop, urban, 80s, alternative rap, dance, dance pop, electronic, hip hop
- **Wikipedia first sentence:** Raw Like Sushi is the debut studio album by Swedish musician Neneh Cherry, released 5 June 1989 by Virgin Records.

#### Candidate 25
- **ids:** seed_id `1c31e4ba-97d6-4a01-bb7c-6373c7f4f1db`, candidate_id `b0fbcd16-2eee-4618-a1d3-06118b440105`
- **Album:** How Bizarre — OMC (1996)
- **Top tags:** dance pop, hip hop, pop, pop rap, pop/rock, rap, rock
- **Wikipedia first sentence:** How Bizarre is the debut and sole studio album by the New Zealand musical group OMC, released in 1996.

#### Candidate 26
- **ids:** seed_id `1c31e4ba-97d6-4a01-bb7c-6373c7f4f1db`, candidate_id `a1674d16-dc46-49d5-9f3e-681540dc362c`
- **Album:** The Beginning — The Black Eyed Peas (2010)
- **Top tags:** pop rap, dance pop, electro house, rock, electropop, hip hop, electro hop, electronic
- **Wikipedia first sentence:** The Beginning is the sixth studio album by American group the Black Eyed Peas.

### Seed: Kiko — Los Lobos

- **Seed id:** `b8a80fb0-401b-440d-865f-3cf80f1a1c42`
- **Album:** Kiko — Los Lobos (1992)
- **Top tags:** latin, rock, rock and roll, 90s, blues rock, country, experimental, jazz, roots rock, soft rock, tex mex
- **Wikipedia first sentence:** Kiko is the sixth album by the Mexican American rock group Los Lobos.

Candidates (2):

#### Candidate 27
- **ids:** seed_id `b8a80fb0-401b-440d-865f-3cf80f1a1c42`, candidate_id `c7bd3c17-a5dd-4134-9799-75f09edb830d`
- **Album:** 1+1+1=4 — Sir Douglas Quintet (1970)
- **Top tags:** rock, blues rock, country, country rock, folk rock, funk, oldies, southern rock

#### Candidate 28
- **ids:** seed_id `b8a80fb0-401b-440d-865f-3cf80f1a1c42`, candidate_id `516d05e4-5f71-4982-953c-e82d29280b30`
- **Album:** Good Morning Aztlán — Los Lobos (2002)
- **Top tags:** 00s, blues, folk, latin, mexico, rock, rock pop, soft rock
- **Wikipedia first sentence:** Good Morning Aztlán is a studio album by the American band Los Lobos, released in 2002.

### Seed: Killing Time — Massacre

- **Seed id:** `084c35e9-3cd5-4fbb-8117-2ae4340303f7`
- **Album:** Killing Time — Massacre (1981)
- **Top tags:** jazz, avant garde, classic pop and rock, experimental rock, free improvisation, no wave, noise rock, rock
- **Wikipedia first sentence:** Killing Time is the debut album by American experimental rock trio Massacre.

Candidates (4):

#### Candidate 29
- **ids:** seed_id `084c35e9-3cd5-4fbb-8117-2ae4340303f7`, candidate_id `d99f7212-9e4e-40b1-bea5-b477644c088b`
- **Album:** Concerts — Henry Cow (1976)
- **Top tags:** jazz, rock, abstract, art rock, classic pop and rock, experimental, free improvisation, prog rock
- **Wikipedia first sentence:** Concerts is a live double album by English avant-rock group Henry Cow, recorded at concerts in London, Italy, the Netherlands and Norway between September 1974 and October 1975.

#### Candidate 30
- **ids:** seed_id `084c35e9-3cd5-4fbb-8117-2ae4340303f7`, candidate_id `4264798b-def8-49e8-ba24-1acd0cc10f9e`
- **Album:** Lux Aeterna — William Sheller (1972)
- **Top tags:** rock, avant garde, classical, experimental, free improvisation, instrumental, jazz, non music

#### Candidate 31
- **ids:** seed_id `084c35e9-3cd5-4fbb-8117-2ae4340303f7`, candidate_id `a50cd869-af8e-44ee-9f81-010682dfdd6a`
- **Album:** Free Alchemy Vol. 1 — Enloom (2014)
- **Top tags:** avant garde, experimental, experimental rock, free improvisation, free jazz, instrumental, jazz rock, noise

#### Candidate 32
- **ids:** seed_id `084c35e9-3cd5-4fbb-8117-2ae4340303f7`, candidate_id `d6747784-2484-42e5-9f94-dffe10754291`
- **Album:** Clean — Cloroform (2007)
- **Top tags:** electronic, experimental, free improvisation, jazz, pop, rhythmic noise, rock, jazz rock

### Seed: Louder Than Words — Lionel Richie

- **Seed id:** `705979bf-c857-409d-8014-4228ddc09812`
- **Album:** Louder Than Words — Lionel Richie (1996)
- **Top tags:** pop, contemporary r and b, easy listening, electronic, funk, pop rock, rock, soul
- **Wikipedia first sentence:** Louder Than Words is the fourth studio album by American singer Lionel Richie.

Candidates (8):

#### Candidate 33
- **ids:** seed_id `705979bf-c857-409d-8014-4228ddc09812`, candidate_id `4b0348b1-d617-404e-b209-122960ca4a5b`
- **Album:** Ready for the World — Ready for the World (1985)
- **Top tags:** electro, contemporary r and b, dance pop, electronic, funk, pop, funk soul, r and b

#### Candidate 34
- **ids:** seed_id `705979bf-c857-409d-8014-4228ddc09812`, candidate_id `df55e0f5-3732-4ee6-b7d8-02e7fdb121d8`
- **Album:** Here at the Mayflower — Barry Manilow (2001)
- **Top tags:** pop, adult contemporary, contemporary pop/rock, easy listening, electronic, pop/rock, rock, soft rock
- **Wikipedia first sentence:** Here at the Mayflower is the nineteenth studio album by Barry Manilow, released in 2001.

#### Candidate 35
- **ids:** seed_id `705979bf-c857-409d-8014-4228ddc09812`, candidate_id `7a2e2e62-e4b2-475e-89ed-dbe53100f54e`
- **Album:** Still Waters — Bee Gees (1997)
- **Top tags:** pop, contemporary r and b, disco, pop rock, r and b, soul
- **Wikipedia first sentence:** Still Waters is the twenty-first and penultimate studio album by the Bee Gees, released on 10 March 1997 in the UK by Polydor Records, and on 6 May the same year in the US by A&M Records.

#### Candidate 36
- **ids:** seed_id `705979bf-c857-409d-8014-4228ddc09812`, candidate_id `5532ddfe-cd2b-4dd9-85f6-c60b0eb1fadf`
- **Album:** Based on a True Story — Kimberley Locke (2007)
- **Top tags:** pop, pop rock, rock, contemporary r and b, funk soul, rhythm blues
- **Wikipedia first sentence:** Based on a True Story is the second studio album by American Idol finalist Kimberley Locke.

#### Candidate 37
- **ids:** seed_id `705979bf-c857-409d-8014-4228ddc09812`, candidate_id `7f2fde02-f88a-431d-9e27-f69fbce57a48`
- **Album:** Young Hearts Run Free — Candi Staton (1976)
- **Top tags:** disco, pop, electronic, funk, r and b, soul

#### Candidate 38
- **ids:** seed_id `705979bf-c857-409d-8014-4228ddc09812`, candidate_id `e0fa6d1e-734d-4df0-a451-ccf15b9692ed`
- **Album:** Triumph — The Jacksons (1980)
- **Top tags:** disco, electronic, soul, contemporary r and b, funk, pop, pop soul
- **Wikipedia first sentence:** Triumph is the fourteenth studio album by the Jacksons, released on September 26, 1980, by Epic Records.

#### Candidate 39
- **ids:** seed_id `705979bf-c857-409d-8014-4228ddc09812`, candidate_id `bc6c6a35-5c1a-44fe-b946-93e100efb3da`
- **Album:** Millennium — Earth, Wind & Fire (1993)
- **Top tags:** pop, contemporary r and b, disco, electronic, funk, old school, r and b, soul
- **Wikipedia first sentence:** Millennium is the sixteenth studio album by American band Earth, Wind & Fire released in September 1993 on Warner Bros.

#### Candidate 40
- **ids:** seed_id `705979bf-c857-409d-8014-4228ddc09812`, candidate_id `8f3a9260-0aaf-49d9-a107-148d69aff451`
- **Album:** Niteflyte — Niteflyte (1979)
- **Top tags:** disco, electronic, jazz, funk soul, pop, rock

### Seed: Welcome Home — Osibisa

- **Seed id:** `101ce734-57d4-4309-810c-b3644a9ac2e6`
- **Album:** Welcome Home — Osibisa (1975)
- **Top tags:** funk, fusion, jazz, jazz funk soul funk, funk soul, rock
- **Wikipedia first sentence:** Welcome Home is the seventh studio album by British Afro rock band Osibisa released in 1975 by Island Records ILPS 9355.

Candidates (4):

#### Candidate 41
- **ids:** seed_id `101ce734-57d4-4309-810c-b3644a9ac2e6`, candidate_id `7618330b-3097-44b5-ad7c-8608e1eaaee3`
- **Album:** After the Storm — Norman Brown (1994)
- **Top tags:** jazz funk, blues, jazz, funk / soul, fusion

#### Candidate 42
- **ids:** seed_id `101ce734-57d4-4309-810c-b3644a9ac2e6`, candidate_id `0b967dbe-cf31-4f72-89d6-d0bd6ee7426e`
- **Album:** Flying Start — The Blackbyrds (1974)
- **Top tags:** jazz funk, disco, funk, funk soul, jazz
- **Wikipedia first sentence:** Flying Start is the second album by the American band the Blackbyrds.

#### Candidate 43
- **ids:** seed_id `101ce734-57d4-4309-810c-b3644a9ac2e6`, candidate_id `2e0f7b0b-02b9-4472-9a65-1f5612342f36`
- **Album:** Sweet Soul — Dizzy Gillespie (1977)
- **Top tags:** funk, jazz, jazz funk, funk soul, soul jazz

#### Candidate 44
- **ids:** seed_id `101ce734-57d4-4309-810c-b3644a9ac2e6`, candidate_id `a90fc624-819f-4219-9057-e91fbc6e5900`
- **Album:** From Me to You — George Duke (1977)
- **Top tags:** funk, jazz funk, jazz, jazz rock, rhythm and blues, soul
- **Wikipedia first sentence:** From Me to You is the tenth studio album by American keyboardist and record producer George Duke.

### Seed: Live in Barcelona ’25 — King Gizzard & the Lizard Wizard

- **Seed id:** `599b795d-9bbf-4367-8f90-7627dbb2dfbe`
- **Album:** Live in Barcelona ’25 — King Gizzard & the Lizard Wizard (2025)
- **Top tags:** alternative rock, anatolian rock, boogie rock, garage rock, heavy psych, indie rock, jam band, livetronica, psychedelic rock, rock, stoner metal, thrash metal

Candidates (1):

#### Candidate 45
- **ids:** seed_id `599b795d-9bbf-4367-8f90-7627dbb2dfbe`, candidate_id `22e82361-e1f4-40e4-9e35-40739a965999`
- **Album:** Live in Vancouver ’24 — King Gizzard & the Lizard Wizard (2024)
- **Top tags:** alternative rock, anatolian rock, boogie rock, indie rock, jam band, livetronica, progressive electronic, progressive metal

### Seed: ESCAPISM — Neko Milkshake

- **Seed id:** `4f4a5430-b152-4579-86be-d12af89ae6bd`
- **Album:** ESCAPISM — Neko Milkshake (2023)
- **Top tags:** electro, electronic, french house, future funk, house

Candidates (3):

#### Candidate 46
- **ids:** seed_id `4f4a5430-b152-4579-86be-d12af89ae6bd`, candidate_id `0fca31af-c488-4166-8ab4-2b023eda925c`
- **Album:** Reverse Psychology — Bomfunk MC’s (2004)
- **Top tags:** electro, electronic, funky house, hip hop

#### Candidate 47
- **ids:** seed_id `4f4a5430-b152-4579-86be-d12af89ae6bd`, candidate_id `9fb193d8-a6dc-45ad-8b52-16928d080f07`
- **Album:** Romborama — The Bloody Beetroots (2009)
- **Top tags:** house, disco, electronic, downtempo, electro, electro house, fidget house, french electro
- **Wikipedia first sentence:** Romborama is the debut studio album by Italian electronic duo The Bloody Beetroots.

#### Candidate 48
- **ids:** seed_id `4f4a5430-b152-4579-86be-d12af89ae6bd`, candidate_id `440f7416-639b-45d6-a529-396da49462af`
- **Album:** Just a Little More Love — David Guetta (2002)
- **Top tags:** house, electronic, electro, electro house, euro house, french house, funky house, rhythmic
- **Wikipedia first sentence:** Just a Little More Love is the debut studio album by David Guetta, released on 10 June 2002 (2002-06-10) by Virgin and Gum Prod.

