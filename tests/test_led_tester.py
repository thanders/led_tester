#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `led_tester` package."""

# tests/test_led_tester.py
import sys
sys.path.append('.')
import pytest
from click.testing import CliRunner
from led_tester import led_tester
from led_tester import cli
from led_tester import utils


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string


def test_command_line_interface():
    ifile = "./data/input_assign3.txt"
    N, instructions = utils.parseFile(ifile)
    assert N is not None

def test_read_file():
    instr_file = "./data/test_data.txt"
    N, instructions = utils.parseFile(instr_file)
    assert N == 10
    print(instructions)
    assert instructions == [('turn on', '0', '0', '9', '9'), ('turn off', '0', '0', '9', '9'), ('switch', '0', '0', '9', '9'),
     ('turn off', '0', '0', '9', '9'), ('turn on', '2', '2', '7', '7')]

