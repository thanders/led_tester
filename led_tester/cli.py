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
    x = led_tester.Light_board(input)
    pprint.pprint(x.light_board) # Initialize the class
    print(x.input)
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
