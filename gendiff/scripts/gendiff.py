#!usr/bin/env python3
import argparse
import json
from collections import OrderedDict

parser = argparse.ArgumentParser(description="Generate diff")
parser.add_argument("first_file", type=str)
parser.add_argument("second_file", type=str)
parser.add_argument("-f", "--format", help="set format of output")
args = parser.parse_args()
first_file = args.first_file
second_file = args.second_file


def generate_diff(file_path1,file_path2):
    file_1 = (json.load(open(file_path1)))
    file_2 = (json.load(open(file_path2)))
    file_1 = OrderedDict(sorted(file_1.items(), key=lambda t: t[0]))
    file_2 = OrderedDict(sorted(file_2.items(), key=lambda t: t[0]))
    diff = ''
    for i in file_1.keys():
        if i not in file_2.keys():
            diff += " - {}: {}\n".format(i, file_1[i])
        elif file_1[i] != file_2[i]:
            diff += " - {}: {}\n".format(i, file_1[i])
            diff += " + {}: {}\n".format(i, file_2[i])
        else:
            diff +="   {}: {}\n".format(i, file_1[i])
    
    for i in file_2.keys():
        if i not in file_1.keys():
            diff += " + {}: {}\n".format(i, file_2[i])
    return diff



def main():
    print(generate_diff(first_file, second_file))
    return 0

if __name__ == '__main__':
    main()