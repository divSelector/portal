from .art import art
from .music import music
from .comedy import comedy
from .writing import writing
from .forums import forums
from .games import games
from .tools import tools
from .nostalgia import nostalgia
from .links import link_directories
from .esoteric import esoteric
from .mine import my_sites

data = {
    "success": True,
    "status": 200,
    "Art": art,
    "Music": music,
    "Writing": writing,
    "Forums": forums,
    "Games": games,
    "Comedy": comedy,
    "Tools": tools,
    "Nostalgia": nostalgia,
    "Esoteric": esoteric,
    "Links": link_directories,
    "Mine": my_sites,
    "copyright": None,
    "FYI": [
        "This is just the early version of this site and I'll be adding to it a lot. So please give me your feedback, suggest links to me, and return to see more links.",
        "Sometimes a link doesn't fit neatly into its given category because it's a variety site. In such cases I just pick a spot that feels right in the moment.",
        "If a website is only available via http, I will link to an archive.org backup of the site."
        
    ]
}
