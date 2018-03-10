# -*- coding: utf-8 -*-
'''
@author: thanders
'''

import re
import requests
import pprint

# Parses the instructions file

def processInput(input):
    if input.startswith('http'):
        # This is for files stored online:
        req = requests.get(input)
        if req.status_code != 200:
            print("Error - Could not download the file you input")
        else:
            # Reads the request
            text = req.text
            f = open("data/instr_download.txt", "w+")
            f.write(text)
            f.close()
            file = "data/instr_download.txt"
            parseFromFile(file)
    else:
        return parseFromFile(input)

def parseFromFile(input):

    pat = re.compile(".*(turn on|turn off|switch)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*")
    # read from disk
    N, instructions = None, []
    with open(input, 'r') as f:
        N = int(f.readline())
        for line in f.readlines():
            if re.search(pat,line):
                result = re.search(pat, line)
                instructions.append(result.group(1,2,3,4,5))
            else:
                print("wtf")
                continue
        light_board(N,instructions)
        print(N)
        print(instructions)
        return N, instructions

def light_board(N, instructions):
    print("Number of instructions are:", N)
    print("Instructions:")
    pprint.pprint(instructions)

    #Initialize lightboard:
    light_board = [[0]*N for _ in range(N)]
    print("Light board: ")
    pprint.pprint(light_board)

    number_off = sum(i.count(0) for i in light_board)
    number_on = sum(i.count(1) for i in light_board)
    print("Lights on:", number_on, "\n", "Lights off:", number_off)

    #Apply instructions
    for i in instructions:
        single_instr = i
        apply_instructions(single_instr)

def apply_instructions(single_instr):
    print("Single instruction:", single_instr)
