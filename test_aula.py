import pytest
from aula5 import soma

def test_soma():
    assert soma(5,0)==5
    assert soma(5,30)==35
    assert soma(5,6)==11