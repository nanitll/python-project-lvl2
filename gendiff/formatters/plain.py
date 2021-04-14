def formatting(element):
    if isinstance(element, dict):
        return "[complex value]"
    elif element is None:
        return 'null'
    elif isinstance(element, bool):
        return 'true' if element else 'false'
    
    return "'{}'".format(element) if isinstance(element, str) else element

def generate_string(diff, path):
    lines = []

    for item_key, item_value in diff.items():
        type_, current_value = item_value
        current_path = path + item_key

        if type_ == "removed":
            lines.append("Property '{}' was removed".format(current_path))
        elif type_ == "added":
            lines.append(
                "Property '{}' was added with value: {}".format(
                    current_path,
                    formatting(current_value),
                )
            )

        elif type_ == "changed":
            lines.append(
                "Property '{}' was updated. From {} to {}".format(
                    current_path,
                    formatting(current_value[0]),
                    formatting(current_value[1]),
                )
            )
        
        elif type_ == "nested":
            lines.append(
                generate_string(
                    current_value,
                    "{}.".format(current_path),
                )
            )
        return "\n".join(lines)


def render(diff):
    return generate_string(diff, "")