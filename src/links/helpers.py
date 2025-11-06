def make_link(url, description, **extra):
    """Return a standard link/description dict with optional extra fields."""
    return {"link": url, "description": description, **extra}


def simple_alphabetical_section(*entries, description=None, include=None):
    """
    Build a dict from tuples or lists like:
        simple_alphabetical_section(
            ("Name", "https://example.com", "Description here"),
            ...
        )
    Sorted alphabetically by name.
    Optionally include:
      - 'description': text placed at the top
      - 'include': dict of nested sections (added at the top, alphabetized)
    """
    section_entries = dict(sorted(
        ((name, make_link(link, desc)) for name, link, desc in entries),
        key=lambda x: x[0].lower()
    ))

    nested_sections = dict(sorted(include.items(), key=lambda x: x[0].lower())) if include else {}

    section = {}
    if description:
        section["description"] = description
    section.update(nested_sections)
    section.update(section_entries)

    return section
