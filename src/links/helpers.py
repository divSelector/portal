def _make_link(url, description, **extra):
    """Return a standard link/description dict with optional extra fields."""
    return {"link": url, "description": description, **extra}


def _build_section_entry(entry):
    if len(entry) == 3:
        name, link, desc = entry
        return name, _make_link(link, desc)
    elif len(entry) == 4:
        name, link, desc, extra = entry
        return name, _make_link(link, desc, **extra)
    else:
        raise ValueError(f"Invalid entry: {entry}")


def alphabetical_section(*entries, description=None, include=None):
    """
    Build a dict from tuples or lists like:
        alphabetical_section(
            ("Name", "https://example.com", "Description here"),
            ("Another", "https://another.com", "Desc", {"key": "value"}),
            ...
        )
    Sorted alphabetically by name.
    Optionally include:
      - 'description': text placed at the top
      - 'include': dict of nested sections (added at the top, alphabetized)
    """


    section_entries = dict(sorted(
        (_build_section_entry(e) for e in entries),
        key=lambda x: x[0].lower()
    ))

    nested_sections = dict(sorted(include.items(), key=lambda x: x[0].lower())) if include else {}

    section = {}
    if description:
        section["description"] = description
    section.update(nested_sections)
    section.update(section_entries)

    return section
