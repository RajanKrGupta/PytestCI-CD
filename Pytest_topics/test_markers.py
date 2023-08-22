import pytest
#pytestmark = [pytest.mark.sanity, pytest.mark.strtest]

@pytest.mark.sanity
def test_str01():
    num = 9/4
    s1 = 'I like ' + 'Pytest automations'
    assert str(num) == '2.25'
    assert s1 == 'I like Pytest automations'

@pytest.mark.sanity
def test_str02():
    letters = 'abcdefghijklmnopqrstuvwxyz'
    assert letters[0] == 'a'
    assert letters[-1] == 'z' == letters[25]


def test_str03():
    letters = 'abcdefghijklmnopqrstuvwxyz'
    assert len(letters) == 26

@pytest.mark.sanity
@pytest.mark.str
def test_strslice():
    letters = 'abcdefghijklmnopqrstuvwxyz'
    assert letters[:] == letters
    assert letters[:3] == 'abc'
