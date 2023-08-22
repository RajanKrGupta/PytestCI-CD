import pytest

@pytest.mark.parametrize('test_input', [78, 80, 90, 85])
def test_param01(test_input):
    assert test_input >50


@pytest.mark.parametrize("inp, op", [(2, 4), (3, 27), (4, 256)])
def test_param02(inp, op):
    assert (inp ** inp) == op


data = [
(2, 4), (3, 9), (4, 16)
]

@pytest.mark.parametrize("inp, op", data)
def test_param03(inp, op):
    assert (inp * inp) == op
