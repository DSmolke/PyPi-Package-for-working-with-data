import pytest

@pytest.fixture
def writer1() -> str:
    """ returns '{arg}' """
    # I know, it's funny to me as well.
    def f(word: str) -> str:
        return word
    return f

@pytest.fixture
def writer2() -> str:
    """ returns "{arg1}+{arg2}" """
    def f(word1: str, word2: str) -> str:
        return f"{word1}+{word2}"
    return f

@pytest.fixture
def writer3() -> str:
    """ returns "deFault" """
    def f() -> str:
        return "deFault"
    return f
