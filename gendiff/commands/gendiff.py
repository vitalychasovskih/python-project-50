import argparse
import json


def start():
    parser = argparse.ArgumentParser(description='Compares two configuration '
                                                 'files and shows a difference.')
    parser.add_argument("-f",
                        "--format",
                        type=str,
                        help="set format of output")
    parser.add_argument("first_file", type=str)
    parser.add_argument("second_file", type=str)
    args = parser.parse_args()

    first_file = args.first_file
    second_file = args.second_file
    a = json.load(open(first_file))
    b = json.load(open(second_file))
    result = '{'
    for key, value in a.items():
        if key in b and a[key] == b[key]:
            result += f'\n  {str(key)}: {str(value)}'
        elif key not in b:
            result += f'\n  -{str(key)}: {str(value)}'
        elif a[key] != b[key]:
            result += f'\n  -{str(key)}: {str(value)}'
            result += f'\n  +{str(key)}: {str(b[key])}'
    for key, value in sorted(b.items()):
        if key not in a:
            result += f'\n  +{str(key)}: {str(value)}'
    print(result+'\n}')
