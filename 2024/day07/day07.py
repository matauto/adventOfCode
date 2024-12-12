#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Author: Mateusz O.
#Date:09 December 2024
#Time:12:33
#based on Advent Of Code template from github.com/matauto/templates

import argparse
import sys
import os
import re
from pathlib import Path
from itertools import product

parser = argparse.ArgumentParser(
        prog = 'day07.py',
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

def main():
    fileName=Path(args.file)
    partExec=args.part
    if (fileName.exists() and fileName.is_file()):
        if partExec==0 or partExec==1:
            #solution for first part of puzzle
            print("PART ONE")
            result=0
            inputFile = open(fileName, 'r', encoding="utf-8")
            #test value regex
            tvRe = re.compile(r"^(\d+)\:")
            for line in inputFile:
                numList=list([])
                #get test value for line
                tvSearch=tvRe.search(line)
                if tvSearch:
                    testValue=int(tvSearch.group(1))
                    #print(testValue)
                    txtList=line[(tvSearch.span(0)[1]+1):].strip().split(" ")
                    numList=[int(x) for x in txtList]
                    #create permutation list for operands
                    operPerm = list(product({'*','+'}, repeat=(len(numList)-1)))
                    #try all combinations of operators to get test value
                    for operList in operPerm:
                        eqVal=numList[0]
                        index=1
                        for oper in operList:
                            if oper == "*":
                                eqVal=eqVal * numList[index]
                            elif oper == "+":
                                eqVal=eqVal + numList[index]
                            index += 1
                        if eqVal==testValue:
                            result=result+testValue
                            print(testValue,"=",numList,operList)
                            break

                    #print for debug
                    #print(testValue, numList, operPerm)

            print("Part one answear: ", result)

        if partExec==0 or partExec==2:
            #solution for second part of puzzle 
            print("PART TWO")

            print("Part two answear: ", result)
    else:
        print("it is not file")

if __name__ == "__main__":
    main()
