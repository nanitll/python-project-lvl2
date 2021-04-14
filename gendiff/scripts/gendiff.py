#!usr/bin/env python3
from gendiff.cli import parse_args
from gendiff import generate_diff


def main():
    args = parse_args()
    print(generate_diff(args.first_file, args.second_file, args.format))
    return 0


if __name__ == '__main__':
    main()
