# -*- coding: utf-8 -*-
import re
import pprint
import requests
import sys
sys.path.append('.')
from led_tester import utils

class Light_board:

    def __init__(self, n):
        self.input = input
        self.light_board = [[0]*n for _ in range(n)]


    def LB_statistics(self, n, instructions):
        print("Number of instructions are:", n)
        print("Instructions:")
        pprint.pprint(instructions)

        number_off = sum(i.count(0) for i in self.light_board)
        number_on = sum(i.count(1) for i in self.light_board)
        return print("Lights on:", number_on, "\n", "Lights off:", number_off)

    def apply_instruction(self,instr):

        print('START:')
        action = instr[0]
        start_r = int(instr[1])
        start_c = int(instr[2])
        end_r = int(instr[3])
        end_c = int(instr[4])

        print(action, start_r, start_c, end_r, end_c)

        if action == 'turn on':
            for i in range(start_r, end_r+1):
                for j in range(start_c, end_c+1):
                    self.light_board[i][j] = 1

        if action == 'turn off':
            for i in range(start_r, end_r+1):
                for j in range(start_c, end_c+1):
                    self.light_board[i][j] = 0

        if action == 'switch':
            for i in range(start_r, end_r+1):
                for j in range(start_c, end_c+1):
                    if self.light_board[i][j] is 0:
                        self.light_board[i][j] = 1
                    else:
                        self.light_board[i][j] = 0

        pprint.pprint(self.light_board)

        '''
            if action is "turn off":
                for i in range(start_r, end_r+1):
                    for j in range(start_c, end_c+1):
                        self.light_board[i][j] = 0
                        # print(parseFromFile("../data/test_data.txt"))

            if action is "switch":
                for i in range(start_r, end_r+1):
                    for j in range(start_c, end_c+1):
                        if self.light_board[i][j] == 0:
                            self.light_board[i][j] = 1
                        if self.light_board[i][j] == 1:
                            self.light_board[i][j] = 0
                        # print(parseFromFile("../data/test_data.txt"))

'''

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
            n, instructions = parseFromFile(file)
    else:
        n, instructions = parseFromFile(input)
    return n, instructions

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
        return n, instructions
        #self.initalize_LB(N, instructions)
