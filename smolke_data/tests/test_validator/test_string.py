import pytest
from decimal import Decimal

from smolke_data.smolke_data.common.validator.string import matches_regex, is_default_isoformat


class TestMatchingRegex:
    def test_for_expression_matching_regex(self):
        assert matches_regex('ABC', r'^ABC$')

    def test_for_expression_not_matching_regex(self):
        assert not matches_regex('123', r'^12$')

    @pytest.mark.parametrize(('expression',), [
        (1,),
        (1.1,),
        ((1,),),
        ([1],),
        (Decimal("1"),),
    ])
    def test_for_invalid_expression_type(self, expression):
        with pytest.raises(TypeError) as err:
            matches_regex(expression, r'^1$')
        assert err.value.args[0] == f"Invalid expression type: {type(expression)}"

    @pytest.mark.parametrize(('regex',), [
        (1,),
        (1.1,),
        ((1,),),
        ([1],),
        (Decimal("1"),),
    ])
    def test_for_invalid_regex_type(self, regex):
        with pytest.raises(TypeError) as err:
            matches_regex("ABC", regex)
        assert err.value.args[0] == f"Invalid regex type: {type(regex)}"


class TestIsoformatValidator:
    correct_value = "2022-12-20T00:00:00+00:00"
    incorrect_value = "20:11:2020"

    def test_correct_isoformat(self):
        assert is_default_isoformat(self.correct_value)

    def test_incorrect_isoformat(self):
        assert is_default_isoformat(self.incorrect_value) is False