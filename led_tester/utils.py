'''
@author: aonghus
'''

import re
import pprint

# Parses the instructions file
def parseFile(input):
    if input.startswith('http'):
        # use requests
        pass
    else:
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
            return N, instructions,
    return

print(parseFile("../data/test_data.txt"))
