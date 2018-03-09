'''
@author: aonghus
'''

import re
import requests

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
        parseFromFile(input)

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
        count_instr = len(instructions)
        print("number of instructions:", count_instr)
        return N, instructions

#print(parseFromFile("../data/test_data.txt"))
