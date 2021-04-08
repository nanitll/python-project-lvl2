#!usr/bin/env python3
import argparse

parser = argparse.ArgumentParser(description="Generate difff")
parser.add_argument("first_file")
parser.add_argument("second_file")
parser.add_argument("-f", "--format", help="set format of output")
args = parser.parse_args()

def main():
    return 0