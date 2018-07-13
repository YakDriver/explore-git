# test_gravitybee.py

import pytest

import hello

# should print hello
def test_output():
    assert hello.say_hello() == "Hello"