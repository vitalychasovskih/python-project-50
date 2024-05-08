import json
import yaml


def read_json_file(path):
    return json.load(open(path))


def read_yaml_file(path):
    return yaml.safe_load(open(path))
