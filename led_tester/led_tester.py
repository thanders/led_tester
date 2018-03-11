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

        # Define the size of the as variables for each light board corner:
        corner_top_left_x = 0
        corner_top_left_y = self.lbSize-1
        corner_top_right_x = self.lbSize-1
        corner_top_right_y = self.lbSize-1
        corner_bottom_left_x = 0
        corner_bottom_left_y = 0
        corner_bottom_right_x = self.lbSize-1
        corner_bottom_right_y = 0

        action = instr[0]
        start_r = int(instr[1])
        start_c = int(instr[2])
        end_r = int(instr[3])
        end_c = int(instr[4])

        # Adjust the instruction bounds to be within the size of the array

        # start_r
        if start_r < end_r and corner_bottom_left_y <= start_r <= corner_top_left_y:
            pass #print("Yes start_r is in bounds")
        else:
            start_r = corner_bottom_left_y
            # print("start_r not in bounds")

        # start_r
        if start_c < end_c and corner_bottom_left_x <= start_c <= corner_bottom_right_x:
            pass # print("Yes start_c is in bounds")
        else :
            start_c = corner_bottom_left_x
            # print("start_c not in bounds")

        # end_r
        if end_r > start_r and corner_bottom_right_y <= end_r <= corner_top_right_y:
            pass # print("Yes start_c is in bounds")
        else :
            end_r = corner_top_right_y
            # print("start_c not in bounds")

        # end_c
        if end_c > start_c and corner_top_left_x <= end_c <= corner_top_right_x:
            pass # print("Yes end_c is in bounds")
        else :
            end_c = corner_top_right_x
            # print("end_c not in bounds")

        # Execute the instruction:
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
