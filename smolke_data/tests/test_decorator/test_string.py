import pytest

from smolke_data.smolke_data.common.decorator.string import to_upper, to_lower, to_char_list
from smolke_data.tests.fixture.common.decorator.string import writer1, writer2, writer3


class TestToUpper:
    class TestValidCases:
        def test_with_one_arg(self, writer1) -> None:
            func = to_upper(writer1)
            assert func("word") == "WORD"

        def test_with_multiple_args(self, writer2) -> None:
            func = to_upper(writer2)
            assert func("word1", "Word2") == "WORD1+WORD2"

        def test_with_no_args(self, writer3) -> None:
            func = to_upper(writer3)
            assert func() == "DEFAULT"

    class TestInvalidCases:
        # All invalid data is treated accordingly to default exceptions
        def test_with_invalid_args_types(self, writer1):
            with pytest.raises(AttributeError) as e:
                func = to_upper(writer1)
                func(1)
            assert e.type == AttributeError


class TestToLower:
    class TestValidCases:
        def test_with_one_arg(self, writer1) -> None:
            func = to_lower(writer1)
            assert func("WORD") == "word"

        def test_with_multiple_args(self, writer2) -> None:
            func = to_lower(writer2)
            assert func("WORD1", "Word2") == "word1+word2"

        def test_with_no_args(self, writer3) -> None:
            func = to_lower(writer3)
            assert func() == "default"

    class TestInvalidCases:
        # All invalid data is treated accordingly to default exceptions
        pass


class TestToCharList:
    class TestValidCases:
        def test_with_one_arg(self, writer1) -> None:
            func = to_char_list(writer1)
            assert func("word") == ["w", "o", "r", "d"]

        def test_with_multiple_args(self, writer2) -> None:
            func = to_char_list(writer2)
            assert func("word1", "Word2") == ["w", "o", "r", "d", "1", "+", "W", "o", "r", "d", "2"]

        def test_with_no_args(self, writer3) -> None:
            func = to_char_list(writer3)
            assert func() == ["d", "e", "F", "a", "u", "l", "t"]

    class TestInvalidCases:
        # All invalid data is treated accordingly to default exceptions
        pass
