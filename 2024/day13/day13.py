#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Author: Mateusz O.
#Date:03 January 2025
#Time:19:45
#{{{import and argument parser
#based on Advent Of Code template from github.com/matauto/templates

import argparse
import sys
import os
import re
from pathlib import Path

parser = argparse.ArgumentParser(
        prog = 'day13.py',
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
#return all combinations (x,y) to solve equation A*x+B*y=C
#where is integer and x<=100 and y<=100
def solveEquation(A,B,C):
    result=set({})
    y=0
    #A*x+B*y=C ==> y=(C-A*x)\B
    for x in range(0,101):
        try:
            y=(C-A*x)/B
            if y<0:
                break
            if int(y)==y and y<=100:
                result.add((x,int(y)))
        except TypeError:
            continue
    return result

#function for calculate number of button A and B presses to move arm over prize
#return tuple (buttonApressed,buttonBpressed)
def calculateSteps(butAval,butBval,prizeDist):
    resX=solveEquation(butAval[0],butBval[0],prizeDist[0])
    if resX:
        resY=solveEquation(butAval[1],butBval[1],prizeDist[1])
        resXY = resX & resY 
        if resXY:
            #print("resXY: ",resXY)
            #here we should write the special function for this: min(3*resXY[0]+1*resXY[1])
            return min(resXY)
    return (0,0)
#}}}
#{{{solve Part One
def solvePartOne(fileName):
    #solution for first part of puzzle
    print("PART ONE")
    result=0
    butAcost=3
    butBcost=1
    buttonAregex=re.compile("Button A: X\+(\d+), Y\+(\d+)")
    buttonBregex=re.compile("Button B: X\+(\d+), Y\+(\d+)")
    prizeRegex=re.compile("Prize: X=(\d+), Y=(\d+)")
    butAval=[0,0]
    butBval=[0,0]
    prizeDist=[0,0]
    with open(fileName, 'r', encoding="utf-8") as inputFile:
        #process the input file
        for line in inputFile:
            butAsearch=re.search(buttonAregex, line)
            butBsearch=re.search(buttonBregex, line)
            prizeSearch=re.search(prizeRegex, line)
            if butAsearch:
                butAval[0]=int(butAsearch.group(1))
                butAval[1]=int(butAsearch.group(2))
            elif butBsearch:
                butBval[0]=int(butBsearch.group(1))
                butBval[1]=int(butBsearch.group(2))
            elif prizeSearch:
                prizeDist[0]=int(prizeSearch.group(1))
                prizeDist[1]=int(prizeSearch.group(2))

                print("butAval=",butAval," butBval= ",butBval," prizeDist= ",prizeDist)
                #function for calculate number of button A and B presses to move arm over prize
                prizeSteps=calculateSteps(butAval,butBval,prizeDist)
                if not(prizeSteps==(0,0)):
                    tokenNum= butAcost*prizeSteps[0] + butBcost*prizeSteps[1]
                    result += tokenNum
                    print("button A presses: ",prizeSteps[0]," button B presses: ",prizeSteps[1]," total cost= ", tokenNum)
                else:
                    print("Impossible to win")

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
