'''
@author: aonghus
'''

import re
import requests
import pprint

# Parses the instructions file

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
        #Count instructions, assign as N
        count_instr = len(instructions)
        light_board(N,instructions)
        print(N)
        print(instructions)
        return N, instructions

def light_board(N, instructions):
    print("Number of instructions are:", N)
    print("Instructions:")
    pprint.pprint(instructions)

    #light_board = [list(range(i * N, i * N + N)) for i in range(N)]

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

'''
    action = single_instr[0]
    start_r = int(single_instr[1])
    start_c = int(single_instr[2])
    end_r = int(single_instr[3])
    end_c = int(single_instr[4])
    print(action)
    
    for i in range(start_r, end_r+1):
        for j in range(start_c, end_c+1):
            light_board[i][j] = 1
            #print(parseFromFile("../data/test_data.txt"))
'''


