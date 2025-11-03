from .helpers import simple_alphabetical_section, make_link


art = simple_alphabetical_section(
    (
        "Public Domain Treasures",
        "https://publicdomaintreasures.neocities.org/",
        "Collection of public domain art organized into categories with an aesthetic book design."
    ),
)

esoteric = simple_alphabetical_section(
    (
        "Checkwave",
        "https://lab.hakim.se/checkwave/",
        "Click a checkbox in a grid of checkboxes and see it create waves of checking adjacent boxes."
    ),
)

emo_music_blogs = simple_alphabetical_section(
    (
        "Open Mind / Saturated Brain",
        "https://openmindsaturatedbrain.blogspot.com/",
        "Cataloging real emo and hardcore albums since 2013",
    ),
    (
        "Sophie's Floorboard",
        "https://sophiesfloorboard.blogspot.com/",
        "Cataloging real emo and hardcore albums since 2012",
    ),
    (
        "What the heck *is* emo, anyway?",
        "https://fourfa.com/",
        "Not a blog but a primer on the Gen X era of Emo. This site has been around for years and is a window into what emo was like before MySpace.",
    ),
)

vaporwave_music_blogs = simple_alphabetical_section(
    (
        "Utopia District",
        "https://utopiadistrict.com",
        "A site that gives me a bit of nostalgia for quarantine-era livestream events. I was paying a lot of attention to the vaporwave scene because of this community at the time.",
    ),
)

pop_music_blogs = simple_alphabetical_section(
    (
        "America's Decline",
        "https://americasdecline.neocities.org",
        "The vibe is like: You're out shopping in the early 2000s and coming up to the checkout, you pass those stands of magazines with Britney Spears and Katy Perry on the front cover. A variety of stuff but the bulk of content is pop music related.",
    ),
)

forums = simple_alphabetical_section(
    (
        "Something Awful",
        "https://forums.somethingawful.com",
        "Y2K era forum known for its significant influence on Internet culture. Well past its prime; it's a retirement home for people that remember it.",
    ),
    (
        "Agora Road",
        "https://forum.agoraroad.com",
        "A vaporwave and nostalgia forum with an undeserved reputation for harboring schizoids. Practically it's a refuge from highly moderated spaces for people all over the world whose values tend towards reactionary.",
    ),
    (
        "Blue Dwarf",
        "https://bluedwarf.top",
        "Cozy board that reminds me of Hacker News for people trying to escape the modern Internet. Its most notable feature is that it supports unencrypted use, making it appealing to users with ancient devices who aren't worried about the encryption.",
    ),
    (
        "Basement Community",
        "https://basementcommunity.com",
        "Small forum with custom software and just enough modern polish. It imitates Something Awful in ways: public sanctions on users, similar new user avatar. Although I don't get the impression that most users are aware of the homage.",
    ),
    (
        "Black Hat World",
        "https://www.blackhatworld.com",
        "This is a shady Internet marketing forum. You can learn a lot here but be aware that everyone will scam you if you let them. The entire forum is built on scamming ignorant people. You can learn a lot but you can't take everything said at face value. Don't give anyone your money unless you know what you're doing. Just lurk and be skeptical.",
    ),
    (
        "Trouble Free Pool",
        "https://www.troublefreepool.com",
        "This is the best place on the Internet to get mostly unbiased information about home pool maintenance. Something you figure out when you get a pool is that the products are expensive and almost all knowledge that is out there is designed to take advantage of your ignorance and push you towards products that make you dependent on spending more. This is required reading for anyone who is going to maintain a pool.",
    ),
    (
        "Bladerunners",
        "https://forum.bladerunners.net/",
        "'For people to chat about tech related things, document their journey in exploring fun stuff etc. Don't take it too seriously' - chxshire22",
    ),
)

tools = simple_alphabetical_section(
    (
        "ColorKit",
        "https://colorkit.co/color/8133b2/",
        "Good for building color palettes. Enter a color, pivot to darker, brighter, more saturated, or complementary colors.",
    ),
)

my_sites = {
    "description": "He is the maintainer of this page BTW",
    "goeshard.org": {
        "blog": make_link(
            "https://goeshard.org",
            "This was a pseudo-professional E/N blog with articles on various topics from gamedev to the alt web. It accepted guest posts in its time but it's been on hiatus for a while.",
            onHiatus=True,
        ),
        "imageboard": make_link(
            "https://board.goeshard.org",
            "A static archive of Nobo's imageboard. You can't post on it anymore but you can browse the threads. It was taken offline for reasons you could discover by lurking.",
            postingEnabled=False,
        ),
    },
    "ᚾᚩᛒᚩ": make_link(
        "https://nobo.bearblog.dev/",
        "A personal blog where Nobo posts hot takes and generally tells you how he really feels.",
    ),
}

friend_sites = simple_alphabetical_section(
    (

        "chxshire22",
        "https://chxshire22.com/",
        "Fellow tinkerer, nerd, hackery enthusiast and cyberpunk enjoyer"
    )
)

music_blogs = {
    "Emo": emo_music_blogs,
    "Vaporwave": vaporwave_music_blogs,
    "Pop": pop_music_blogs,
}

data = {
    "success": True,
    "status": 200,
    "Art": art,
    "Blogs": {"Music": music_blogs},
    "Forums": forums,
    "Tools": tools,
    "Esoteric": esoteric,
    "Mine": my_sites,
    "Friends": friend_sites,
    "none": None,
}
