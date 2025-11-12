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

web_design = alphabetical_section(
    (
        "CSS Garden",
        "https://csszengarden.com/",
        "You can get some pretty cool ideas for web design here.",
        {"favorite": "https://csszengarden.com/219/"}
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
    (
        "Software That Sucks Less",
        "https://suckless.org",
        "If you don't specifically use any software they maintain, their philsophy is still interesting and their people section leads to a variety of hacker personal pages.",
        {
            "philosophy": "https://suckless.org/philosophy/",
            "people": "https://suckless.org/people/"
        }
    ),
    (
        "/g/ \"InstallGentoo\" Wiki",
        "https://igwiki.lyci.de",
        "I never spent much time on /g/ but they made a decent wiki. Most of the activity was closer to 2014.",
        {
            "cyberpunkMovies": "https://igwiki.lyci.de/wiki/Movies"
        }
    ),
    (
        "MDN Web Documentaion",
        "https://developer.mozilla.org/",
        "The best documentation for HTML, CS, JS, and other webdev technologies on the Internet probably."
    ),
    include={
        "Gamedev": gamedev,
        "Webdev": web_design
    }
)