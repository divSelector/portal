from django import template
register = template.Library()


@register.filter
def items(obj):
    """Return dict items if dict, else empty list."""
    return obj.items() if isinstance(obj, dict) else []

@register.filter
def is_list(obj):
    """True if value is list or tuple."""
    return isinstance(obj, (list, tuple))

@register.filter
def is_bool(obj):
    """True if value is a boolean."""
    return isinstance(obj, bool)

@register.filter
def is_number(obj):
    """True if value is a number but not boolean."""
    return isinstance(obj, (int, float)) and not isinstance(obj, bool)

@register.filter
def is_none(obj):
    """True if value is None."""
    return obj is None

@register.filter
def is_last_folder(node):
    if not isinstance(node, dict):
        return False
    # True if all children are primitives
    return all(
        not isinstance(v, (dict, list))
        for v in node.values()
    )
