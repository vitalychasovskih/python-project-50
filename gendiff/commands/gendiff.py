import argparse
import json


def read_json_file(path):
    return json.load(open(path))


def get_formatted_value(value):
    if isinstance(value, bool):
        formatted_value = str(value).lower()
    else:
        formatted_value = value
    return formatted_value


def find_difference(dict1, dict2):
    merged_dictionary = {**dict1, **dict2}
    result = ''
    for key, value in sorted(merged_dictionary.items()):
        if key in dict1 and key in dict2:
            if dict1[key] == value:
                result += f'\n    {key}: {get_formatted_value(value)}'
            if dict1[key] != value:
                result += f'\n  - {key}: {get_formatted_value(dict1[key])}'
                result += f'\n  + {key}: {get_formatted_value(value)}'
        if key in dict1 and key not in dict2:
            result += f'\n  - {key}: {get_formatted_value(dict1[key])}'
        if key not in dict1 and key in dict2:
            result += f'\n  + {key}: {get_formatted_value(value)}'
    return '{' + result + '\n}'


def generate_diff():
    parser = argparse.ArgumentParser(description='Compares two '
                                                 'configuration files '
                                                 'and shows a difference.')
    parser.add_argument("-f",
                        "--format",
                        type=str,
                        help="set format of output")
    parser.add_argument("first_file", type=str)
    parser.add_argument("second_file", type=str)
    args = parser.parse_args()
    first_file = args.first_file
    second_file = args.second_file
    a = read_json_file(first_file)
    b = read_json_file(second_file)
    print(find_difference(a, b))
