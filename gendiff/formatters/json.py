import json

def render(diff):
    return json.dumps(diff, ensure_ascii=False, ident="    ", sort_keys=True)