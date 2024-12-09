#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Author: Mateusz O.
#Date:07 December 2024
#Time:18:20
#based on Advent Of Code template from github.com/matauto/templates

import argparse
import sys
import os
import re
import time
from pathlib import Path

parser = argparse.ArgumentParser(
        prog = 'day06.py',
        description = 'advent of code problem solver',
        epilog = 'none')
parser.add_argument("file",
                    default = ".",
                    type = Path,
                    help = "input file for script")
parser.add_argument("part",
                    default = "0",
                    type = int,
                    help = "input file for script")
args = parser.parse_args()

def changeDirection(guardDir):
    if guardDir=="^":
        return ">"
    elif guardDir==">":
        return "v"
    elif guardDir=="v":
        return "<"
    elif guardDir=="<":
        return "^"
    else:
        return ""

def nextPosition(guardDir,guardPos):
    row=guardPos[0]
    col=guardPos[1]
    if guardDir=="^":
        return (row-1,col)
    elif guardDir==">":
        return (row,col+1)
    elif guardDir=="v":
        return (row+1,col)
    elif guardDir=="<":
        return (row,col-1)

def replaceStr(someStr, charPos, charReplace):
    s=list(someStr)
    s[charPos]=charReplace
    return "".join(s)

def getNextChar(guardDir, nextChar):
    if nextChar=="." and (guardDir=="^" or guardDir=="v"):
        return "|"
    elif nextChar=="." and (guardDir=="<" or guardDir==">"):
        return "-"
    elif nextChar=="|" and (guardDir=="<" or guardDir==">"):
        return "+"
    elif nextChar=="-" and (guardDir=="^" or guardDir=="v"):
        return "+"
    else:#+, O
        return nextChar

def getLeftChars(labMap, guardDir, guardPos):
    row=guardPos[0]
    col=guardPos[1]
    maxRow=len(labMap)
    maxCol=len(labMap[0])
    
    if guardDir=="^":
        if col+1>maxCol:
            return ""
        return labMap[row][col+1]
    elif guardDir==">":
        if row+1>maxRow:
            return ""
        return labMap[row+1][col]
    elif guardDir=="v":
        if col-1<0:
            return ""
        return labMap[row][col-1]
    elif guardDir=="<":
        if row-1<0:
            return ""
        return labMap[row-1][col]

def loopConditions(labMap, guardDir, guardPos):
    row=guardPos[0]
    col=guardPos[1]
    maxRow=len(labMap)
    maxCol=len(labMap[0])
    nextStep=nextPosition(guardDir,guardPos)
    if nextStep[0]>=maxRow or nextStep[1]>=maxCol or nextStep[0]<0 or nextStep[1]<0:
        return False
    nextChar=labMap[nextStep[0]][nextStep[1]]
    if nextChar=="#" or nextChar=="^":
        return False
    #check right side of guard for loop condition: "+#"
    rightDir=changeDirection(guardDir)
    charBefore=""
    rightPos=nextPosition(rightDir,guardPos)
    #print("rightChars: ")
    while rightPos[0]>=0 and rightPos[1]>=0 and rightPos[0]<maxRow and rightPos[1]<maxCol:
        rightChar=labMap[rightPos[0]][rightPos[1]]
        #print(rightChar,rightPos)
        if (charBefore=="+" or charBefore=="O") and rightChar=="#":
            return True
        charBefore=rightChar
        rightPos=nextPosition(rightDir,rightPos)
    #if found "+#"    
    return False

def main():
    fileName=Path(args.file)
    partExec=args.part
    if (fileName.exists() and fileName.is_file()):
        if partExec==0 or partExec==1:
            #solution for first part of puzzle
            print("PART ONE")
            result=0
            inputFile = open(fileName, 'r', encoding="utf-8")
            #put file to 2D table labMap
            labMap=inputFile.read().splitlines()
            #search guard position
            guardRe = re.compile(r"[<\^v>]")
            #search where guard is posGuard
            for i in range(len(labMap)):
                guardReMatch = guardRe.search(labMap[i])
                #print(row)
                if guardReMatch:
                    #print(labMap[i])
                    guardPos=(i,guardReMatch.span(0)[0])
                    guardDir=guardReMatch.group(0)
                    #print(guardPos)
            #calculate max dimensions of map
            maxRow=len(labMap)
            maxCol=len(labMap[0])
            #print(maxRow,maxCol)
            #move the guard around the map
            endOfMap=False
            while endOfMap==False:
                nextStep=nextPosition(guardDir,guardPos)
                if nextStep[0]>=maxRow or nextStep[1]>=maxCol or nextStep[0]<0 or nextStep[1]<0:
                    endOfMap=True
                    labMap[guardPos[0]]=replaceStr(labMap[guardPos[0]],guardPos[1],"X")
                    result=result+1
                else:
                    nextChar=labMap[nextStep[0]][nextStep[1]]
                    if nextChar=="#":
                        guardDir=changeDirection(guardDir)
                        labMap[guardPos[0]]=replaceStr(labMap[guardPos[0]],guardPos[1],guardDir)
                    elif nextChar=="." or nextChar=="X":
                        labMap[guardPos[0]]=replaceStr(labMap[guardPos[0]],guardPos[1],"X")
                        labMap[nextStep[0]]=replaceStr(labMap[nextStep[0]],nextStep[1],guardDir)
                        guardPos=nextStep
                        if nextChar==".":
                            result=result+1
                print("=========================")
                for line in labMap:
                    print(line)
                #time.sleep(0.1)
                    
            #print the map
            print("===============================")
            for line in labMap:
                print(line)
            print("Part one answear: ", result)

        if partExec==0 or partExec==2:
            #solution for second part of puzzle 
            print("PART TWO")
            result=0
            inputFile = open(fileName, 'r', encoding="utf-8")
            #put file to 2D table labMap
            labMap=inputFile.read().splitlines()
            #search guard position
            guardRe = re.compile(r"[<\^v>]")
            #search where guard is posGuard
            for i in range(len(labMap)):
                guardReMatch = guardRe.search(labMap[i])
                #print(row)
                if guardReMatch:
                    #print(labMap[i])
                    guardPos=(i,guardReMatch.span(0)[0])
                    guardDir=guardReMatch.group(0)
                    #print(guardPos)
            #calculate max dimensions of map
            maxRow=len(labMap)
            maxCol=len(labMap[0])
            #print(maxRow,maxCol)
            #move the guard around the map
            endOfMap=False
            changedDir=False
            putObstacle=False
            repChar=""
            while endOfMap==False:
                nextStep=nextPosition(guardDir,guardPos)
                if nextStep[0]>=maxRow or nextStep[1]>=maxCol or nextStep[0]<0 or nextStep[1]<0:
                    endOfMap=True
                    if putObstacle:
                        putObstacle=False
                        repChar="O"
                    labMap[guardPos[0]]=replaceStr(labMap[guardPos[0]],guardPos[1],repChar)
                else:
                    nextChar=labMap[nextStep[0]][nextStep[1]]
                    if repChar=="":
                        repChar=labMap[guardPos[0]][guardPos[1]]
                    if nextChar=="#":
                        guardDir=changeDirection(guardDir)
                        labMap[guardPos[0]]=replaceStr(labMap[guardPos[0]],guardPos[1],guardDir)
                        changedDir=True
                    #elif nextChar=="." or nextChar=="X":
                    else:
                        if changedDir==True:
                            repChar="+"
                        if putObstacle:
                            putObstacle=False
                            repChar="O"
                        if loopConditions(labMap, guardDir, guardPos):
                            putObstacle=True
                            result=result+1
                        labMap[guardPos[0]]=replaceStr(labMap[guardPos[0]],guardPos[1],repChar)
                        labMap[nextStep[0]]=replaceStr(labMap[nextStep[0]],nextStep[1],guardDir)
                        guardPos=nextStep
                        changedDir=False
                        repChar=getNextChar(guardDir, nextChar)
                print("=========================")
                for line in labMap:
                    print(line)
                #time.sleep(0.1)
                    
            #print the map
            print("===============================")
            for line in labMap:
                print(line)

            print("Part two answear: ", result)
    else:
        print("it is not file")

if __name__ == "__main__":
    main()
