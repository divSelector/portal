from links.helpers import alphabetical_section

gamedev = alphabetical_section(
    (
        "nothings.org",
        "https://nothings.org",
        "Home page of Sean Barrett, \"dysfunctional programmer.\" He worked on Thief and System Shock games/engines among other things."
    ),
    (
        "Roguebasin",
        "https://roguebasin.com/",
        "Roguelike information resource that you can edit."
    ),
    (
        "Jonathon Blow",
        "http://number-none.com/blow/blog/",
        "Controversial and iconic video game programmer who made Braid and the Witness",
        {
            "oldBlog": "http://number-none.com",
            "theWitness": "http://the-witness.net/news/",
            "souljaBoy": "https://www.youtube.com/watch?v=xSXofLK5hFQ",
            "lololol": "https://www.youtube.com/watch?v=gWqnz-7iQbY"
        }
    ),
    (
        "Lode's Computer Graphics Tutorials",
        "https://lodev.org/cgtutor",
        "Holds a soft spot in my heart as the raycasting guide here was the first gamedev tutorial I ever did."
    ),
    (
        "The Book of Shaders",
        "https://thebookofshaders.com/",
        "This is a gentle step-by-step guide through the abstract and complex universe of Fragment Shaders."
    ),
    (
        "Shadertoy",
        "https://www.shadertoy.com/",
        "Platform for building and sharing shaders."
    )

)

technology = alphabetical_section(
    (
        "Eric S. Raymond's Home Page",
        "http://www.catb.org/~esr/",
        "Personal site of software developer and open-source advocate of 1990s best known for writing The Cathedral and the Bazaar.",
        {
            "jargon": "http://www.catb.org/~esr/jargon/"
        }
    ),
    (
        "Defensive Computing Checklist",
        "https://defensivecomputingchecklist.com/",
        "\"There are many websites devoted to privacy and many devoted to security. But each is only a piece of the Defensive Computing puzzle.\""
    ),
    (
        "Don't Ask to Ask, Just Ask",
        "https://dontasktoask.com",
        "\"Any Java experts around who are willing to commit into looking into my problem?\""
    ),
    include={"Gamedev": gamedev}
)