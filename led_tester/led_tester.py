# -*- coding: utf-8 -*-
import re
import pprint
import requests
import sys
sys.path.append('.')
from led_tester import utils

class Light_board:

    def __init__(self, N):
        self.input = input
        self.light_board = [[0]*N for _ in range(N)]

def processInput(input):
    if input.startswith('http'):
        # use requests
        req = requests.get(input)
        if req.status_code != 200:
            print("Error - Could not download the file you input")
        else:
            #This reads the request
            text = req.text
            f = open("data/instr_download.txt", "w+")
            f.write(text)
            f.close()
            file = "data/instr_download.txt"
            n = parseFromFile(file)
    else:
        n = parseFromFile(input)
    return n

def parseFromFile(input):

    pat = re.compile(
        ".*(turn on|turn off|switch)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*")
    # read from disk
    n, instructions = None, []
    with open(input, 'r') as f:
        n = int(f.readline())
        for line in f.readlines():
            if re.search(pat, line):
                result = re.search(pat, line)
                instructions.append(result.group(1, 2, 3, 4, 5))
            else:
                print("Could not recognize instruction on line:", line)
                continue
        # Count instructions, assign as N
        count_instr = len(instructions)

        print("COUNT INSTRUCTIONS", count_instr)
        return n
        #self.initalize_LB(N, instructions)

    def initalize_LB(self, N, instructions):
        print("Number of instructions are:", N)
        print("Instructions:")
        pprint.pprint(instructions)

        #Initialize lightboard:
        LB = [[0]*N for _ in range(N)]

        number_off = sum(i.count(0) for i in LB)
        number_on = sum(i.count(1) for i in LB)
        print("Lights on:", number_on, "\n", "Lights off:", number_off)
        pprint.pprint(LB)

    '''
    def apply_instruction

        action = single_instr[0]
        start_r = int(single_instr[1])
        start_c = int(single_instr[2])
        end_r = int(single_instr[3])
        end_c = int(single_instr[4])
        print(action)

        for i in range(start_r, end_r + 1):
            for j in range(start_c, end_c + 1):
                light_board[i][j] = 1
                # print(parseFromFile("../data/test_data.txt"))


    def main(self, input):
        utils.processInput(input)
'''


