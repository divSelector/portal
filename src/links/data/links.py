from links.helpers import alphabetical_section

search_engines = alphabetical_section(
    (
        "Wiby",
        "https://wiby.me/",
        "Emphasis on collecting websites with simple HTML without a lot of bloated scripts."
    ),
    (
        "Marginalia",
        "https://marginalia-search.com/",
        "\"Nothing you do to try to make the web a better place matters if nobody can find what you did. There are a lot of precious websites out there that deserve an audience, but instead are languishing in obscurity.\""

    ),
    description="Search engines are essentially link directories built by web crawlers that can be queried. Here are some small ones."
)

link_directories = alphabetical_section(
    (
        "Open Directory Project (ODP)",
        "https://web.archive.org/web/20250924190251/http://odp.org/",
        "Based on DMOZ (directory mozilla) RDF, which was owned by AOL, it was maintained by volunteer editors for decades, and this site is an archive of that directory created when AOL closed the project. The links here will be very old."
    ),
    (
        "Peelopaalu",
        "https://peelopaalu.neocities.org/",
        "Unsorted collection. There are sites here from the 90's and sites that were made last week. Maintained from 2019-2024."
    ),
    (
        "Free Media Heck Yeah",
        "https://fmhy.net",
        "Starting as a primer and harm reduction guide on piracy, it's now an exhaustive wiki of free resources and Internet services."
    ),
    description="There is some temptation to build on top of other link directory sites, but as I want the portal to go hard in its own way, I will simply direct you to these other sites.",
    include={"Search Engines": search_engines}
)

