import json
import yaml
from os.path import splitext
from gendiff.error_constants import VALUE_ERROR

def load(file_descriprtor, extension):
    if extension == ".json":
        return json.load(file_descriprtor)
    if extension in {".yaml", ".yaml"}:
        return yaml.safe_load(file_descriprtor)

    raise ValueError(VALUE_ERROR.format(extension))

def read_data(filepath):
    _, extension = splitext(filepath)
    with open(filepath) as file_descriprtor:
        return load(file_descriprtor, extension)