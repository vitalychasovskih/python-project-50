import argparse
import pathlib
from .parse_file import read_json_file, read_yaml_file

# 1. получаем путь из командной строки get_paths()
# 2. определяем расширение файла get_extension()
# 3. выбираем какой функцией читать в словарь choice_
# 4. читаем содержимое файла в словарь read_'extension'_file()
# 5. сравниваем словари и получаем результат сравнения find_difference()
# 6. выводим результат сравнения print()

YML =['.yml', '.yaml']
def get_paths_from_commandline():
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
    path_file1 = args.first_file
    path_file2 = args.second_file
    return path_file1, path_file2


def get_extension(path):
    return pathlib.Path(path).suffix


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
        if key in dict1 and key in dict2 and dict1[key] == value:
            result += f'\n    {key}: {get_formatted_value(value)}'
        if key in dict1 and key in dict2 and dict1[key] != value:
            result += f'\n  - {key}: {get_formatted_value(dict1[key])}'
            result += f'\n  + {key}: {get_formatted_value(value)}'
        if key in dict1 and key not in dict2:
            result += f'\n  - {key}: {get_formatted_value(dict1[key])}'
        if key not in dict1 and key in dict2:
            result += f'\n  + {key}: {get_formatted_value(value)}'
    return '{' + result + '\n}'


def generate_diff(path1=None, path2=None):
    if not path1 or not path2:
        path1, path2 = get_paths_from_commandline()
    if get_extension(path1) == '.json' and get_extension(path2) == '.json':
        a = read_json_file(path1)
        b = read_json_file(path2)
        return find_difference(a, b)
    if get_extension(path1) in YML and get_extension(path2) in YML:
        a = read_yaml_file(path1)
        b = read_yaml_file(path2)
        return find_difference(a, b)
    else:
        print('Недоступный формат расширения файлов')
