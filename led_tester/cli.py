# -*- coding: utf-8 -*-

"""Console script for led_tester."""
import sys
sys.path.append('.')
from led_tester import utils
from led_tester import led_tester
import pprint

import click
click.disable_unicode_literals_warning = True

@click.command()
@click.option("--input", default=None, help="input URI (file or URL)")

def main(input):
    """Console script for led_tester."""
    print("input", input)
    #N, instructions = utils.processInput(input)

    # Process input to get n
    n, instructions = led_tester.processInput(input)
    # Initiate Light_board class to define light_board with n
    x = led_tester.Light_board(n)
    # Pretty print instance x's empty light board
    pprint.pprint(x.light_board)
    for instr in instructions:
        x.apply_instruction(instr)

    # count lights on and off
    print(x.LB_statistics(n, instructions))
    pprint.pprint(x.light_board)
    return 0

if __name__ == "__main__":
    sys.exit(main()) # pragma: no cover



'''


    print(x.store)
    #ledTester = LEDTester(N)
'''

    #for instruction in instructions:
    #    ledTester.apply(instruction)

    #print('#occupied: ', ledTester.countOccupied())
