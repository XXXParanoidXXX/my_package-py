# tests/test_module.py
from my_package.module import hello_world

def test_hello_world():
    assert hello_world() == "Hello, World!"