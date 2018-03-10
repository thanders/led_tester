import pprint
import re
import requests
import sys
sys.path.append('.')

class Light_board:

    def __init__(self, n):
        self.lbSize = n
        self.light_board = [[0]*n for _ in range(n)]

    def LB_statistics(self, n, instructions):
        number_off = sum(i.count(0) for i in self.light_board)
        number_on = sum(i.count(1) for i in self.light_board)
        print("Number of instructions: {:0,.0f}".format(len(instructions)))
        print("Size of light board: {:0,.0f}".format(n), "rows, {:0,.0f}".format(n), "columns", "and {:0,.0f}".format(n*n), "light bulbs")
        print("Lights on: {:0,.0f}".format(number_on))
        print("Lights off: {:0,.0f}".format(number_off))
        print("Sum of on and off: {:0,.0f}".format(number_on + number_off))
        return 0

    def apply_instruction(self,instr):

        # Check to make sure instructions are all within a box:
        self.lbSize
        border_min_lx = 0
        border_max_lx = self.lbSize
        border_min_ly = 0
        border_max_ly = self.lbSize
        border_min_rx = 0
        border_max_rx = self.lbSize
        border_min_ry = 0
        border_max_ry = self.lbSize

        action = instr[0]
        start_r = int(instr[1])
        start_c = int(instr[2])
        end_r = int(instr[3])
        end_c = int(instr[4])

        #Check to make sure start row instruction within grid
        if border_min_ly <= start_r <= border_max_ly:
            pass
        else:
            if start_r < end_r:
                start_r = border_min_ly
            else:
                end_r = border_max_ly
        #Check to make sure start column instruction within grid
        if border_min_lx <= start_c <= border_max_rx:
            pass
        else:
            if start_c < end_c:
                start_c = border_min_lx
            else:
                end_c = border_max_rx
        #Check to make sure end row instruction within grid
        if border_min_ly <= end_r <= border_max_ly:
            pass
        else:
            if end_r > start_r:
                end_r = border_max_ry
            else:
                end_r = border_min_ry
        #Check to make sure end col instruction within grid
        if border_min_lx <= end_c <= border_max_lx:
            pass
        else:
            if end_c > start_c:
                end_c = border_max_rx
            else:
                end_c = border_min_lx

        # Execute Instructions
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

# These are functions and are not required by the class above:
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
            return n, instructions
    else:
        n, instructions = parseFromFile(input)
        return n, instructions

def parseFromFile(input):
    pat = re.compile(".*(turn on|turn off|switch)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*")
    # read from disk
    n, instructions = None, []
    with open(input, 'r') as f:
        n = int(f.readline())
        for line in f.readlines():
            if re.search(pat, line):
                result = re.search(pat, line)
                instructions.append(result.group(1, 2, 3, 4, 5))
            else:
                #print("Could not recognize instruction on line:", line)
                continue
        return n, instructions
