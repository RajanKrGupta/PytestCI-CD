
import pytest

class TestMyStuff():
    def test_type(self):
        assert type(1) == int

    def test_case01(self):
        with pytest.raises(Exception):
            assert(1/0)


    def test_case02(self):
        with pytest.raises(Exception) as excinfo:
            assert (1, 2, 3) == (1, 2, 4)
        print(str(excinfo))


