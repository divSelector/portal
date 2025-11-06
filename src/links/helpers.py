def make_link(url, description, **extra):
    """Return a standard link/description dict with optional extra fields."""
    return {"link": url, "description": description, **extra}


def simple_alphabetical_section(*entries, description=None):
    """
    Build a dict from tuples or lists like:
        simple_alphabetical_section(
            ("Name", "https://example.com", "Description here"),
            ...
        )
    Sorted alphabetically by name.
    Optionally include a 'description' key at the top.
    """
    section = dict(sorted(
        ((name, make_link(link, desc)) for name, link, desc in entries),
        key=lambda x: x[0].lower()
    ))
    if description:
        section = {"description": description, **section}
    return section