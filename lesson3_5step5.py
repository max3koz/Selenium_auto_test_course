import pytest

@pytest.mark.xfail (strict=True)
def test_succeed():
    print(" 111")
    assert True


@pytest.mark.xfail
def test_not_succeed():
    print(" 222")
    assert False


@pytest.mark.skip
def test_skipped():
    print(" 333")
    assert False