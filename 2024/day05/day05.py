#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Author: Mateusz O.
#Date:07 December 2024
#Time:01:50
#based on Advent Of Code template from github.com/matauto/templates

import argparse
import sys
import os
import re
from pathlib import Path

parser = argparse.ArgumentParser(
        prog = 'day05.py',
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
            #regex for rules
            ruleRe = re.compile(r"(\d+)\|(\d+)")
            pgOrdRules=[]
            teachingPhase=True
            for line in inputFile:
                #read and memorize rules in table of tuples
                if teachingPhase:
                    matchRule = ruleRe.match(line)
                    if matchRule:
                        #print(matchRule)
                        print("RULE:",matchRule.group(1)," before ", matchRule.group(2))
                        pgOrdRules.append((int(matchRule.group(1)), int(matchRule.group(2))))
                        #print(pgOrdRules)
                    else:
                        teachingPhase=False
                else:
                    #ingest the page listing to list
                    pageOrder=[int(x) for x in line.split(",")]
                    #check the order according to rules
                    print(line, " is in: ", end="")
                    goodOrder=True
                    for i in range(len(pageOrder)):
                        for rule1, rule2 in pgOrdRules:
                            if pageOrder[i]==rule1:
                                for j in range(len(pageOrder)):
                                    if pageOrder[j]==rule2:
                                        if i>j:
                                            goodOrder=False
                                            print("BAD ORDER", pageOrder[i], "after", pageOrder[j])
                                            break
                    if goodOrder:
                        print("GOOD ORDER")
                        middleNum=pageOrder[int(len(pageOrder)/2)]
                        print("Middle number: ", middleNum)
                        result=result+middleNum

            print("Part one answear: ", result)

        if partExec==0 or partExec==2:
            #solution for second part of puzzle 
            print("PART TWO")
            result=0
            inputFile = open(fileName, 'r', encoding="utf-8")
            #regex for rules
            ruleRe = re.compile(r"(\d+)\|(\d+)")
            pgOrdRules=[]
            teachingPhase=True
            for line in inputFile:
                #read and memorize rules in table of tuples
                if teachingPhase:
                    matchRule = ruleRe.match(line)
                    if matchRule:
                        #print(matchRule)
                        #print("RULE:",matchRule.group(1)," before ", matchRule.group(2))
                        pgOrdRules.append((int(matchRule.group(1)), int(matchRule.group(2))))
                        #print(pgOrdRules)
                    else:
                        teachingPhase=False
                else:
                    #ingest the page listing to list
                    pageOrder=[int(x) for x in line.split(",")]
                    #check the order according to rules
                    print(line, " is in: ", end="")
                    goodOrder=True
                    for i in range(len(pageOrder)):
                        for rule1, rule2 in pgOrdRules:
                            if pageOrder[i]==rule1:
                                for j in range(len(pageOrder)):
                                    if pageOrder[j]==rule2:
                                        if i>j:
                                            goodOrder=False
                                            #print("BAD ORDER", pageOrder[i], "after", pageOrder[j])
                                            break
                    if goodOrder==False:
                        print("BAD ORDER")
                        newOrder=list(pageOrder)
                        while goodOrder==False:
                            goodOrder=True
                            for i in range(len(pageOrder)):
                                for rule1, rule2 in pgOrdRules:
                                    if pageOrder[i]==rule1:
                                        for j in range(len(pageOrder)):
                                            if pageOrder[j]==rule2:
                                                if i>j:
                                                    goodOrder=False
                                                    temp=pageOrder[i]
                                                    pageOrder[i]=pageOrder[j]
                                                    pageOrder[j]=temp
                        print("New Ordder: ", pageOrder)
                        middleNum=pageOrder[int(len(pageOrder)/2)]
                        print("Middle number: ", middleNum)
                        result=result+middleNum
                    else:
                        print("GOOD ORDER")

            print("Part two answear: ", result)
    else:
        print("it is not file")

if __name__ == "__main__":
    main()
