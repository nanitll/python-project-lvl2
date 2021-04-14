def convert(element):
    if element is None:
        return "null"
    elif isinstance(element, bool):
        return "true" if element else "false"
    return element

def line(some_key, some_value, type_, depth):
    sign = {
        "removed": "-",
        "added": "+",
        "unchanged": " ",
        "nested": " ",
    }

    if isinstance(some_value, dist):
        normalize_value = generate_string(some_value, depth + 1)
    else:
        normalize_value = convert(some_value)
    
    return " {} {}: {}".format(sign, some_key, normalize_value)

def generate_string(diff, depth):
    lines = []

    for item_key, item_value in diff.items():

        if isinstance(item_value, tuple):
            type_ = item_value[0]
            current_value = item_value[1]
        
        else:
            type_ = "unchanged"
            current_value = item_value
        
        if type_ == "nested":
            nested_diff = generate_string(current_value, depth + 1)
            lines.append(line(item_key, nested_diff, type_, depth))
        elif type_ == "changed":
            lines.append(line(item_key, current_value[0], "removed", depth))
            lines.append(line(item_key, current_value[1], "added", depth))
        else:
            lines.append(line(item_key, current_value, type_, depth))
            
    ident = "{}{}".format("\n", "    " * depth)
    return "{{{0}{1}{2}}}".format(indent, indent.join(lines), indent)


def render(diff):
    return generate_string(diff, 0)