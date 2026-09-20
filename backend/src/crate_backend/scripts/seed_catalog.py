"""Seed a small, hand-picked album catalog for local development and Phase 1
search testing. Superseded by the MusicBrainz import pipeline in Phase 2.

Run with: uv run python -m crate_backend.scripts.seed_catalog
"""

import asyncio

from sqlalchemy import select

from crate_backend.db.session import async_session_factory
from crate_backend.models.catalog import Album

# (title, artist, release_year)
SEED_ALBUMS: list[tuple[str, str, int]] = [
    ("Illinois", "Sufjan Stevens", 2005),
    ("The Age of Adz", "Sufjan Stevens", 2010),
    ("Kid A", "Radiohead", 2000),
    ("OK Computer", "Radiohead", 1997),
    ("In Rainbows", "Radiohead", 2007),
    ("A Moon Shaped Pool", "Radiohead", 2016),
    ("To Pimp a Butterfly", "Kendrick Lamar", 2015),
    ("good kid, m.A.A.d city", "Kendrick Lamar", 2012),
    ("DAMN.", "Kendrick Lamar", 2017),
    ("Mr. Morale & the Big Steppers", "Kendrick Lamar", 2022),
    ("My Beautiful Dark Twisted Fantasy", "Kanye West", 2010),
    ("The College Dropout", "Kanye West", 2004),
    ("Yeezus", "Kanye West", 2013),
    ("Blonde", "Frank Ocean", 2016),
    ("Channel Orange", "Frank Ocean", 2012),
    ("Discovery", "Daft Punk", 2001),
    ("Random Access Memories", "Daft Punk", 2013),
    ("Homework", "Daft Punk", 1997),
    ("Currents", "Tame Impala", 2015),
    ("Lonerism", "Tame Impala", 2012),
    ("The Slow Rush", "Tame Impala", 2020),
    ("Rumours", "Fleetwood Mac", 1977),
    ("Tusk", "Fleetwood Mac", 1979),
    ("Abbey Road", "The Beatles", 1969),
    ("Revolver", "The Beatles", 1966),
    ("Sgt. Pepper's Lonely Hearts Club Band", "The Beatles", 1967),
    ("The Dark Side of the Moon", "Pink Floyd", 1973),
    ("Wish You Were Here", "Pink Floyd", 1975),
    ("The Wall", "Pink Floyd", 1979),
    ("Nevermind", "Nirvana", 1991),
    ("In Utero", "Nirvana", 1993),
    ("Bleach", "Nirvana", 1989),
    ("Ten", "Pearl Jam", 1991),
    ("Vs.", "Pearl Jam", 1993),
    ("Loveless", "My Bloody Valentine", 1991),
    ("Souvlaki", "Slowdive", 1993),
    ("Spiderland", "Slint", 1991),
    ("Funeral", "Arcade Fire", 2004),
    ("The Suburbs", "Arcade Fire", 2010),
    ("Merriweather Post Pavilion", "Animal Collective", 2009),
    ("Person Pitch", "Panda Bear", 2007),
    ("For Emma, Forever Ago", "Bon Iver", 2007),
    ("Bon Iver, Bon Iver", "Bon Iver", 2011),
    ("22, A Million", "Bon Iver", 2016),
    ("Boys for Pele", "Tori Amos", 1996),
    ("Little Earthquakes", "Tori Amos", 1992),
    ("Homogenic", "Björk", 1997),
    ("Vespertine", "Björk", 2001),
    ("Post", "Björk", 1995),
    ("Hounds of Love", "Kate Bush", 1985),
    ("The Kick Inside", "Kate Bush", 1978),
    ("Blue", "Joni Mitchell", 1971),
    ("Court and Spark", "Joni Mitchell", 1974),
    ("Songs in the Key of Life", "Stevie Wonder", 1976),
    ("Innervisions", "Stevie Wonder", 1973),
    ("What's Going On", "Marvin Gaye", 1971),
    ("Voodoo", "D'Angelo", 2000),
    ("Black Messiah", "D'Angelo", 2014),
    ("Baduizm", "Erykah Badu", 1997),
    ("Mama's Gun", "Erykah Badu", 2000),
    ("The Miseducation of Lauryn Hill", "Lauryn Hill", 1998),
    ("Ready to Die", "The Notorious B.I.G.", 1994),
    ("Illmatic", "Nas", 1994),
    ("Enter the Wu-Tang (36 Chambers)", "Wu-Tang Clan", 1993),
    ("The Chronic", "Dr. Dre", 1992),
    ("2001", "Dr. Dre", 1999),
    ("Aquemini", "Outkast", 1998),
    ("Stankonia", "Outkast", 2000),
    ("Madvillainy", "Madvillain", 2004),
    ("Since I Left You", "The Avalanches", 2000),
    ("Endtroducing.....", "DJ Shadow", 1996),
    ("Selected Ambient Works 85-92", "Aphex Twin", 1992),
    ("Music Has the Right to Children", "Boards of Canada", 1998),
    ("Untrue", "Burial", 2007),
    ("Blue Lines", "Massive Attack", 1991),
    ("Mezzanine", "Massive Attack", 1998),
    ("Dummy", "Portishead", 1994),
    ("Portishead", "Portishead", 1997),
    ("Third", "Portishead", 2008),
    ("Disintegration", "The Cure", 1989),
    ("Pornography", "The Cure", 1982),
    ("Closer", "Joy Division", 1980),
    ("Unknown Pleasures", "Joy Division", 1979),
    ("Substance", "New Order", 1987),
    ("Power, Corruption & Lies", "New Order", 1983),
    ("Talking Heads: 77", "Talking Heads", 1977),
    ("Remain in Light", "Talking Heads", 1980),
    ("Fear of Music", "Talking Heads", 1979),
    ("London Calling", "The Clash", 1979),
    ("The Clash", "The Clash", 1977),
    ("Never Mind the Bollocks Here's the Sex Pistols", "Sex Pistols", 1977),
    ("Marquee Moon", "Television", 1977),
    ("Horses", "Patti Smith", 1975),
    ("Blood on the Tracks", "Bob Dylan", 1975),
    ("Highway 61 Revisited", "Bob Dylan", 1965),
    ("The Freewheelin' Bob Dylan", "Bob Dylan", 1963),
    ("Astral Weeks", "Van Morrison", 1968),
    ("Moondance", "Van Morrison", 1970),
    ("Pet Sounds", "The Beach Boys", 1966),
    ("Exile on Main St.", "The Rolling Stones", 1972),
    ("Let It Bleed", "The Rolling Stones", 1969),
    ("Led Zeppelin IV", "Led Zeppelin", 1971),
    ("Physical Graffiti", "Led Zeppelin", 1975),
    ("Hotel California", "Eagles", 1976),
    ("Harvest", "Neil Young", 1972),
    ("After the Gold Rush", "Neil Young", 1970),
    ("Music from Big Pink", "The Band", 1968),
    ("Sign o' the Times", "Prince", 1987),
    ("Purple Rain", "Prince", 1984),
    ("1999", "Prince", 1982),
    ("Thriller", "Michael Jackson", 1982),
    ("Off the Wall", "Michael Jackson", 1979),
    ("Like a Prayer", "Madonna", 1989),
    ("Ray of Light", "Madonna", 1998),
    ("Back to Black", "Amy Winehouse", 2006),
    ("Frank", "Amy Winehouse", 2003),
    ("21", "Adele", 2011),
    ("25", "Adele", 2015),
    ("Lemonade", "Beyoncé", 2016),
    ("Renaissance", "Beyoncé", 2022),
    ("Dangerously in Love", "Beyoncé", 2003),
    ("Norman Fucking Rockwell!", "Lana Del Rey", 2019),
    ("Born to Die", "Lana Del Rey", 2012),
    ("Melodrama", "Lorde", 2017),
    ("Pure Heroine", "Lorde", 2013),
    ("Blackstar", "David Bowie", 2016),
    ("The Rise and Fall of Ziggy Stardust", "David Bowie", 1972),
    ("Low", "David Bowie", 1977),
    ("Heroes", "David Bowie", 1977),
    ("Station to Station", "David Bowie", 1976),
    ("A Love Supreme", "John Coltrane", 1965),
    ("Giant Steps", "John Coltrane", 1960),
    ("Blue Train", "John Coltrane", 1957),
    ("Kind of Blue", "Miles Davis", 1959),
    ("Bitches Brew", "Miles Davis", 1970),
    ("Head Hunters", "Herbie Hancock", 1973),
    ("Maiden Voyage", "Herbie Hancock", 1965),
    ("The Köln Concert", "Keith Jarrett", 1975),
    ("Time Out", "The Dave Brubeck Quartet", 1959),
    ("Mingus Ah Um", "Charles Mingus", 1959),
    ("Moanin'", "Art Blakey", 1959),
]


async def seed() -> None:
    async with async_session_factory() as session:
        for index, (title, artist, year) in enumerate(SEED_ALBUMS):
            external_id = f"seed-{index:04d}"
            existing = await session.scalar(
                select(Album).where(
                    Album.external_source == "seed", Album.external_id == external_id
                )
            )
            if existing:
                existing.title = title
                existing.artist_name = artist
                existing.release_year = year
            else:
                session.add(
                    Album(
                        title=title,
                        artist_name=artist,
                        release_year=year,
                        external_source="seed",
                        external_id=external_id,
                    )
                )
        await session.commit()
    print(f"Seeded {len(SEED_ALBUMS)} albums.")


if __name__ == "__main__":
    asyncio.run(seed())
