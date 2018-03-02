'''
@author: aonghus
'''

import re
def parseFile(input):
    if input.startswith('http'):
        # use requests
        pass
    else:
        pat = re.compile(".*(turn on|turn off|switch)\s*([+-]?\d+)\s *,\s * ([+-]?\d+)\s * through\s * ([+-]?\d+)\s *,\s * ([+-]?\d+). * ")
        # read from disk
        N, instructions = None, []
        with open(input, 'r') as f:
            N = int(f.readline())
            for line in f.readlines():
                instructions.append(line)
                instructions = pat.instructions
            return N, instructions
    return
