#!usr/bin/env python3
import argparse
import json
import yaml


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


def generate_diff(file_path1, file_path2):
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


def main():
    parser = argparse.ArgumentParser(description="Compares two cnfiguration files and shows a diference")
    parser.add_argument("first_file", type=str)
    parser.add_argument("second_file", type=str)
    parser.add_argument("-f", "--format", help="set format of output")
    args = parser.parse_args()
    first_file = args.first_file
    second_file = args.second_file

    print(generate_diff(first_file, second_file))
    return 0


if __name__ == '__main__':
    main()
