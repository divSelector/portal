from links.helpers import alphabetical_section

emo_music_blogs = alphabetical_section(
    (
        "Open Mind / Saturated Brain",
        "https://openmindsaturatedbrain.blogspot.com/",
        "Blog cataloging real emo and hardcore albums since 2013",
    ),
    (
        "Sophie's Floorboard",
        "https://sophiesfloorboard.blogspot.com/",
        "Blog cataloging real emo and hardcore albums since 2012",
    ),
    (
        "What the heck *is* emo, anyway?",
        "https://fourfa.com/",
        "Primer on the Gen X era of Emo. This site has been around for years and is a window into what emo was like before MySpace.",
    ),
)

vaporwave_music_blogs = alphabetical_section(
    (
        "Utopia District",
        "https://utopiadistrict.com",
        "A site that gives me a bit of nostalgia for quarantine-era livestream events. I was paying a lot of attention to the vaporwave scene because of this community at the time.",
    ),
    (
        "Nightwave Plaza",
        "https://plaza.one/",
        "Online vaporwave and future funk radio station with aesthetic backgrounds and network streams."
    ),
    (
        "Arcology Online",
        "https://www.arcology.online/",
        "Articles and interviews in vaporwave space with a very good sized collection of links and resources to external sites."
    )
)

music = alphabetical_section(
    (
        "America's Decline",
        "https://americasdecline.neocities.org",
        "The vibe is like: You're out shopping in the early 2000s and coming up to the checkout, you pass those stands of magazines with Britney Spears and Katy Perry on the front cover. A variety of stuff but the bulk of content is pop music related.",
    ),
    (
        "World Playground Deceit",
        "https://world-playground-deceit.net/",
        "Posts about music, film, programming, and other subjects, but the music reviews featuring dark music and extreme metal are my favorite sections."
    ),
    (
        "OverClocked Remix",
        "https://ocremix.org/",
        "Before Spotify, Bandcamp, YouTube, Soulseek, Limewire, or Napster, there was this weird site of people remixing video game music. At the time VGM wasn't respected as real music, so hearing people render it as classical or dance music, it was extremely novel and moreover one of the earliest places I know of that you could download free music.",
        {
            "string": "Hello World",
            "number": 123,
            "float": 123.45,
            "null": None,
            "bool": False
        }
    ),
    include={
        "Emo": emo_music_blogs,
        "Vaporwave": vaporwave_music_blogs
    }
)