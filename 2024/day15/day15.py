#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Author: Mateusz O.
#Date:05 January 2025
#Time:21:30
#{{{import and argument parser
#based on Advent Of Code template from github.com/matauto/templates

import argparse
import sys
import os
import re
from pathlib import Path
import aoclib as aoc

parser = argparse.ArgumentParser(
        prog = 'day15.py',
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
def makeMove(robot,actValues,move):
    outDict=actValues
    moveDir={"^":[-1,0],"v":[1,0],">":[0,1],"<":[0,-1]}
    actPos=(robot.actPos[0],robot.actPos[1])
    nextPos=(robot.actPos[0]+moveDir[move][0],robot.actPos[1]+moveDir[move][1])
    if '.' in actValues.values():
        if actValues[nextPos]=='.':
            outDict[actPos]='.'
            outDict[nextPos]='@'
            robot.setPos(nextPos)
        elif actValues[nextPos]=='O':
            outDict[actPos]='.'
            outDict[nextPos]='@'
            #robot.setPos(nextPos)
            nextActPos=nextPos
            while True:
                nextPos=(nextPos[0]+moveDir[move][0],nextPos[1]+moveDir[move][1])
                if actValues[nextPos]=='.':
                    robot.setPos(nextActPos)
                    outDict[nextPos]='O'
                    break
                elif actValues[nextPos]=='#':
                    robot.setPos(actPos)
                    return dict({})
                    break
    return outDict
#}}}
#{{{solve Part One
def solvePartOne(fileName):
    #solution for first part of puzzle
    print("PART ONE")
    result=0
    map2D=list([])
    moveList=list([])
    actPos=[0,0]
    with open(fileName, 'r', encoding="utf-8") as inputFile:
        rowI=0
        for line in inputFile:
            #process the input file
            row=list(line.strip())
            if row:
                #map part of file
                if row[0]=='#':
                    map2D.append(row)
                    if '@' in row:
                        actPos[0]=rowI
                        actPos[1]=row.index('@')
                    else:
                        rowI+=1
                #directions part of file
                elif row[0] in {'<','>','^','v'}:
                    moveList+=row

    robot=aoc.map2D.CPlayer(map2D,actPos)
    print("Initial map")
    robot.mapPrint()
    #print(robot.getViewRow(robot.actPos[0]))
    #print(robot.getViewCol(robot.actPos[1]))
    #print(map2D)
    #print(moveList)
    for movI,move in enumerate(moveList):
        actValues=dict({})
        changedValues=dict({})
        if move=='<':
            actValues={key:value for key,value in robot.getViewRow(robot.actPos[0]).items() if key[1]<=robot.actPos[1]}
        elif move=='>':
            actValues={key:value for key,value in robot.getViewRow(robot.actPos[0]).items() if key[1]>=robot.actPos[1]}
        elif move=='^':
            actValues={key:value for key,value in robot.getViewCol(robot.actPos[1]).items() if key[0]<=robot.actPos[0]}
        elif move=='v':
            actValues={key:value for key,value in robot.getViewCol(robot.actPos[1]).items() if key[0]>=robot.actPos[0]}
        #print("For: ",move," : ",actValues)
        if '.' in actValues.values():
            #function to shift values in ditionary according to rules
            changedValues=makeMove(robot,actValues,move)
            if changedValues:
                print(changedValues[tuple(robot.actPos)])
#               if changedValues[robot.actPos]!='@':
                robot.setMapValues(changedValues)
                #robot.makeMove(move)
        print("Move number: ", movI+1," : ",move)
        robot.mapPrint()
    #calulate a sum of boxes GPS coordinaes
    map2D=robot.map2D
    for row in range(robot.maxRow):
        for col in range(robot.maxCol):
            if robot.getValueMap((row,col))=='O':
                result+=100*row+col
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
