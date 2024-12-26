#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Author: Mateusz O.
#Date:26 December 2024
#Time:01:34
#{{{import and argument parser
#based on Advent Of Code template from github.com/matauto/templates

import argparse
import sys
import os
import re
from pathlib import Path

parser = argparse.ArgumentParser(
        prog = 'day11.py',
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
#}}}
#{{{functions
def digitsCount(stoneValue):
    return len(str(stoneValue))

def divideStone(stoneValue, numOfDigits):
    stoneStr=str(stoneValue)
    halfPoint=numOfDigits // 2
    stoneValue1=int(stoneStr[0:halfPoint])
    stoneValue2=int(stoneStr[halfPoint:])
    #print("stonStr: ", stoneStr, " halfPoint: ", halfPoint, " str1: ", stoneStr[0:halfPoint]," str2: ", stoneStr[halfPoint:])
    return (stoneValue1,stoneValue2)
#}}}
#{{{solve Part One
def solvePartOne(fileName):
    #solution for first part of puzzle
    print("PART ONE")
    result=0
    with open(fileName, 'r', encoding="utf-8") as inputFile:
        stoneList=[int(x) for x in inputFile.read().split()]

    print("Initial stones: ", stoneList)
    #give a number of blinks
    noBlinks=input("Number of blinks: ")

    addedElement=False
    for blink in range(int(noBlinks)):
        for ind,stone in enumerate(stoneList):
            if addedElement:
                addedElement=False
            else:
                numOfDigits=digitsCount(stone)

                if stone==0:
                    stoneList[ind]=1
                elif not(numOfDigits % 2):
                    twoStones=divideStone(stone, numOfDigits)
                    stoneList[ind]=twoStones[0]
                    stoneList.insert(ind+1,twoStones[1])
                    addedElement=True
                else:
                    stoneList[ind]=stone*2024
        print("Blink number: ", blink+1)    
        #print(stoneList)

    result=len(stoneList)
    print("Part one answear: ", result)

#}}}
#{{{solve Part Two
def solvePartTwo(fileName):
    #solution for second part of puzzle
    print("PART TWO")
    result=0

    print("Part two answear: ", result)
#}}}
#{{{main
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
#}}}
