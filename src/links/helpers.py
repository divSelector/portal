def make_link(url, description, **extra):
    """Return a standard link/description dict with optional extra fields."""
    return {"link": url, "description": description, **extra}


def simple_alphabetical_section(*entries):
    """
    Build a dict from tuples or lists like:
    make_simple_section(
        ("Name", "https://example.com", "Description here"),
        ...
    )
    Sorted alphabetically by name.
    """
    section = dict(sorted(
        ((name, make_link(link, desc)) for name, link, desc in entries),
        key=lambda x: x[0].lower()
    ))
    # section["count"] = len(entries)
    return section