"""A small scenes.toml shared by the scene tests.

Scenes a (1994–2006), b (2005–), c (1965–1982) and d (1978–2010) sit on
two paths: a → b → c and d → a.
"""

from crate_backend.scenes.config import parse_scene_config

MINIMAL = """
[settings]
live_share = 0.05
connector_share = 0.15
deep_cut_share = 0.15
broad_weight = 0.3
artist_free_albums = 3
artist_decay = 0.75
deprioritized_factor = 0.4
deep_cut_max_votes = 6
deep_cut_min_terms = 4
deep_cut_min_scene_terms = 2
nondescriptive_terms = ["Seen Live"]
deprioritized_terms = ["Indie Rock"]
cut_terms = ["Black Metal", "free jazz"]

[[scene]]
id = "a"
name = "A"
tier = "center"
years = [1994, 2006]
share = 2
terms = ["Shibuya-kei"]

[[scene]]
id = "b"
name = "B"
tier = "echoes"
years = [2005]
share = 1
terms = ["hauntology"]

[[scene]]
id = "c"
name = "C"
tier = "roots"
years = [1965, 1982]
share = 1
terms = ["krautrock"]

[[scene]]
id = "d"
name = "D"
tier = "wider"
years = [1978, 2010]
share = 1
terms = ["shoegaze", "dream pop"]
broad_terms = ["rock"]
exclude_terms = ["post punk revival"]

[[scene]]
id = "e"
name = "E"
tier = "wider"
years = [1978, 2010]
share = 1
terms = ["ambient", "idm"]
needs_company = ["ambient"]

[[path]]
name = "a to c"
scenes = ["a", "b", "c"]

[[path]]
name = "d to a"
scenes = ["d", "a"]
"""


def minimal_config(text: str = MINIMAL):
    return parse_scene_config(text)
