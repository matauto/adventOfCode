#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import sys
import os
import re
from pathlib import Path

parser = argparse.ArgumentParser(
        prog = 'day01.py',
        description = 'advent of code day 01',
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

        leftCol=[]
        rightCol=[]
        #ingest data
        for line in inputFile:
            x, y = map(int, line.split())
            leftCol.append(x)
            #print(x, end=", ")
            rightCol.append(y)
            #print(y)

        #sort data
        leftCol.sort()
        rightCol.sort()

        #calculate result
        result=0
        for i in range(len(leftCol)):
            result = result + abs(leftCol[i]-rightCol[i])

        print("Total distance: ", result)

        print("PART TWO")
        #solution for second part of puzzle 
        result2=0
        for i in range(len(leftCol)):
            leftX = leftCol[i]
            n = rightCol.count(leftX)
            result2 = result2 + leftX*n

        print("Similarity score: ", result2)
    else:
        print("it is not file")

if __name__ == "__main__":
    main()
