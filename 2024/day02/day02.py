#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Author: Mateusz O.
#based on Advent Of Code template from github.com/matauto/templates

import argparse
import sys
import os
import re
from pathlib import Path

parser = argparse.ArgumentParser(
        prog = 'day02.py',
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
        #calculate result
        result=0
        for line in inputFile:
            numLine = list(map(int, line.split()))
            #print(numLine)
            #determin order for good result
            orderUP = False
            if numLine[1] > numLine[0]:
                #ascending order
                orderUP = True
            #test each element for conditions
            #assume line is good toggle to false if error occur
            goodLine = True
            for i in range(1, len(numLine)):
                if orderUP and (not(abs(numLine[i]-numLine[i-1]) in range(1,4)) or numLine[i]<numLine[i-1]):
                    goodLine = False
                    break
                if not orderUP and (not(abs(numLine[i]-numLine[i-1]) in range(1,4)) or numLine[i]>numLine[i-1]):
                    goodLine = False
                    break
            if goodLine:
                print("Good line: ", line, end="")
                result=result+1
            else:
                print("Bad line: ", line, end="")
        print("\n\n=================================")
        print("Part one answear: ", result)
        #exit()
        #############################################################################
        print("\nPART TWO")
        #solution for second part of puzzle 
        inputFile = open(fileName, 'r', encoding="utf-8")
        #calculate result
        result2=0
        for line in inputFile:
            tempLine = list(map(int, line.split()))
            #print(numLine)
            for i in range(0, len(tempLine)):
                numLine = list(tempLine)
                del numLine[i]
                orderUP = False
                if numLine[1] > numLine[0]:
                    #ascending order
                    orderUP = True
                #test each element for conditions
                #assume line is good toggle to false if error occur
                goodLine = True
                for i in range(1, len(numLine)):
                    if orderUP and (not(abs(numLine[i]-numLine[i-1]) in range(1,4)) or numLine[i]<numLine[i-1]):
                        goodLine = False
                        break
                    if not orderUP and (not(abs(numLine[i]-numLine[i-1]) in range(1,4)) or numLine[i]>numLine[i-1]):
                        goodLine = False
                        break
                if goodLine:
                    print("Good line: ", tempLine)
                    result2=result2+1
                    break
                #else:
                 #   print("Bad line: ", tempLine)
        print("\n\n=================================")
        print("Part two answear: ", result2)
    else:
        print("it is not file")

if __name__ == "__main__":
    main()
