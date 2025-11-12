from links.helpers import alphabetical_section

my_sites_goeshard_org = alphabetical_section(
    (
        "blog",
        "https://goeshard.org",
        "This was a pseudo-professional E/N blog with articles on various topics from gamedev to the alt web. It accepted guest posts in its time but it's been on hiatus for a while.",
        {"onHiatus": True},
    ),
    (
        "imageboard",
        "https://board.goeshard.org",
        "A static archive of Nobo's imageboard. You can't post on it anymore but you can browse the threads. It was taken offline for reasons you could discover by lurking.",
        {
            "postingEnabled": False,
            "bonus": "https://tylenol.goeshard.org"
        },
    ),
)

my_sites = alphabetical_section(
    (
        "ᚾᚩᛒᚩ",
        "https://nobo.bearblog.dev/",
        "A personal blog where Nobo posts hot takes and generally tells you how he really feels"
    ),
    (
        "¥†mñÐ",
        "https://goeshard.neocities.org/",
        "You're The Man Now Dawg-inspired shitposts that I dump on neocities"
    ),
    include={"goeshard.org": my_sites_goeshard_org},
    description="I am the maintainer of this page BTW. Some of my sites:"
)