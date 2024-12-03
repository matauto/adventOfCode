#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Author: Mateusz O.
#Date:03 December 2024
#Time:21:39
#based on Advent Of Code template from github.com/matauto/templates

import argparse
import sys
import os
import re
from pathlib import Path

parser = argparse.ArgumentParser(
        prog = 'day03.py',
        description = 'advent of code problem solver',
        epilog = 'none')
parser.add_argument("file",
                    default = ".",
                    type = Path,
                    help = "input file for script")
args = parser.parse_args()

def main():
    fileName=Path(args.file)
    if (fileName.exists() and fileName.is_file()):
        inputFile = open(fileName, 'r', encoding="utf-8")

        print("PART ONE")
        #solution for first part of puzzle
        result=0
        p  = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
        for line in inputFile:
            regSearchList = p.finditer(line)
            for regSearch in regSearchList:
                #print(regSearch)#print object
                print(regSearch.group(0), end=": ")#ex: "mul(2,4)"
                X = int(regSearch.group(1))#ex: 2
                Y = int(regSearch.group(2))#ex: 4
                print(X, "*", Y, end="=")
                print(X*Y)
                result = result + X*Y 
        print("Part one answear: ", result)
        exit()
        print("PART TWO")
        #solution for second part of puzzle 

        #calculate result2
        result2=0

        print("Part two answear: ", result2)
    else:
        print("it is not file")

if __name__ == "__main__":
    main()
