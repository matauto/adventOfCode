#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Author: Mateusz O.
#Date:19 December 2024
#Time:20:52
#based on Advent Of Code template from github.com/matauto/templates

import argparse
import sys
import os
import re
from pathlib import Path

parser = argparse.ArgumentParser(
        prog = 'day09.py',
        description = 'advent of code problem solver',
        epilog = 'none')
parser.add_argument("file",
                    default = ".",
                    type = Path,
                    help = "input file for script")
parser.add_argument("part",
                    default = "0",
                    type = int,
                    choices=[0,1,2],
                    help = "input file for script")
args = parser.parse_args()

def solvePartOne(fileName):
    #solution for first part of puzzle
    print("PART ONE")
    result=0
    with open(fileName, 'r', encoding="utf-8") as inputFile:
        diskMap=inputFile.readline()
        dotsEn=False
        diskBlock=list([])
        num = 0
        for char in diskMap:
            if char=='\n':
                break
            i = int(char)
            #process the disk map to generate disk block
            if dotsEn:
                for x in range(i):
                    diskBlock.append('.')
                dotsEn=False
            else:
                for x in range(i):
                    diskBlock.append(num)
                num += 1
                dotsEn=True

    print("diskBlock uncompressed: ", diskBlock)

    #compress disk block 
    numF = 0
    numB = 0
    while numB >= numF:
        firstDot=True
        num = 0
        for i in diskBlock:
            if i == '.':
                if firstDot:
                    numF = num
                    firstDot=False
            else:
                numB = num
            num += 1
        if numB > numF:        
            diskBlock[numF] = diskBlock[numB]
            diskBlock[numB] = '.'

    print("diskBlock before compressed: ", diskBlock)

    #calculate checksum=result
    for i,ele in enumerate(diskBlock):
        if ele == '.':
            break
        else:
            result += int(ele) * i

    print("Part one answear: ", result)


def solvePartTwo(fileName):
    #solution for second part of puzzle
    print("PART TWO")
    result=0

    print("Part two answear: ", result)

def main():
    fileName=Path(args.file)
    partExec=args.part
    if (fileName.exists() and fileName.is_file()):
        if partExec==0 or partExec==1:
            #solution for first part of puzzle
            solvePartOne(fileName)
        if partExec==0 or partExec==2:
            #solution for second part of puzzle 
            solvePartTwo(fileName)
    else:
        print("it is not file")

if __name__ == "__main__":
    main()
