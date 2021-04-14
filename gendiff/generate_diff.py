from gendiff.difference import build
from gendiff.formatters import mapping_for_choose_formatter
from gendiff.io import read_data
from gendiff.error_constants import FORMAT_ERROR

def output_diff(key1, key2, operand=' '):
    return " {} {}: {}\n".format(operand, key1, key2)


def pars_files(file_path1, file_path2):
    print(file_path1[-1:-3:-1])
    if file_path1[-4::] == 'yaml' and file_path2[-4::] == 'yaml':
        file_1 = yaml.safe_load(open(file_path1))
        file_2 = yaml.safe_load(open(file_path2))
    else:
        file_1 = json.load(open(file_path1))
        file_2 = json.load(open(file_path2))
    return file_1, file_2


def generate_diff(file_path1, file_path2, output_format="stylish"):
    file_1, file_2 = pars_files(file_path1, file_path2)
    diff = []

    for i in file_1.keys():
        if i not in file_2.keys():
            diff.append(output_diff(i, file_1[i], '-'))
        elif file_1[i] == file_2[i]:
            diff.append(output_diff(i, file_1[i], ' '))
        else:
            diff.append(output_diff(i, file_1[i], '-'))
            diff.append(output_diff(i, file_2[i], '+'))

    for i in file_2.keys():
        if i not in file_1.keys():
            diff.append(output_diff(i, file_2[i], '+'))

    diff_str = ''.join(sorted(diff, key=lambda x: x[3]))
    return diff_str
