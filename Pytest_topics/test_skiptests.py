import sys
import pytest

#pytestmark = pytest.mark.skipif(sys.platform == 'win32', reason="Global skipped")
cons =9/5
def cent_to_fah(cent=0):
    fah = (cent*cons)+32
    return fah


@pytest.mark.skip(reason = "skipped for testing")
def test01_cent_to_fah():
    assert type(cent_to_fah(100)) == float

@pytest.mark.skipif(pytest.__version__ >'5.0', reason= "Pytest version is lower, needs higher highere version to check" )
def test02_cent_to_fah():
    assert cent_to_fah() == 32


def test03_cent_to_fah():
    assert cent_to_fah(38) == 100.4
