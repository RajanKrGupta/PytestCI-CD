import sys
import pytest

@pytest.mark.xfail
def test_comp01():
    num = 9/4
    s1 = 'I like ' + 'Pytest automation'
    assert str(num) == '2.25'


@pytest.mark.xfail(sys.platform =='win32', reason ="works only in Linux")
def test_comp02():
    letters = 'abcdefghijklmnopqrstuvwxyz'
    assert letters[100]

@pytest.mark.xfail
def test_comp03():
    letters = 'abcdefghijklmnopqrstuvwxyz'
    assert len(letters) == 26

def test_comp04():
    letters = 'abcdefghijklmnopqrstuvwxyz'
    assert letters[:] == letters
    assert letters[:3] == 'abc'
