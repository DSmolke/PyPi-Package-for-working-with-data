from collections import Counter
from enum import Enum

import pytest
from smolke_data.smolke_data.common.utils.collection import first_elements_having_same_value, \
    get_n_top_elements_of_most_common_list, is_enum_name


class TestFirstElementsHavingSameValue:
    def test_with_one_highest(self):
        assert first_elements_having_same_value([3, 2, 1]) == [3]

    def test_with_two_highest(self):
        assert first_elements_having_same_value([2, 2, 1]) == [2, 2]

    def test_with_all_highest(self):
        assert first_elements_having_same_value([3, 3, 3]) == [3, 3, 3]

    def test_with_one_lowest(self):
        assert first_elements_having_same_value([1, 2, 3]) == [1]

    def test_with_two_lowest(self):
        assert first_elements_having_same_value([1, 1, 2]) == [1, 1]

    def test_when_elements_are_empty_list(self):
        assert first_elements_having_same_value([]) == []

    def test_when_elements_have_one_value(self):
        assert first_elements_having_same_value([1]) == [1]

    def test_when_invalid_type_element_occur(self):
        with pytest.raises(TypeError) as e:
            first_elements_having_same_value([1, 2, '3'])
        assert e.value.args[0] == "Elements list containing invalid type elements"

    @pytest.mark.parametrize(("elements",), [
        (5,),
        ((1, 2, 3),),
        ({1: 1, 2: 2, 3: 3},)
    ])
    def test_when_invalid_type_of_elements_occur(self, elements):
        with pytest.raises(TypeError) as e:
            first_elements_having_same_value(5)
        assert e.value.args[0] == "Argument named 'elements' has invalid type"

    def test_with_str_values(self):
        assert first_elements_having_same_value(['A', 'A', 'B', 'B']) == ['A', 'A']

class TestGetNTopElementsOfMostCommonList:
    def test_when_few_most_common(self):
        counter = Counter([1, 3, 2])
        # because each value occurs once, so there are 3 most common values
        assert get_n_top_elements_of_most_common_list(counter.most_common()) == 3

    def test_when_two_most_common(self):
        counter = Counter([1, 2])
        assert get_n_top_elements_of_most_common_list(counter.most_common()) == 2

    def test_when_one_most_common(self):
        counter = Counter([1, 2, 3, 1])
        assert get_n_top_elements_of_most_common_list(counter.most_common()) == 1

    def test_when_empty_counter_provided(self):
        counter = Counter()
        with pytest.raises(IndexError) as e:
            get_n_top_elements_of_most_common_list(counter.most_common())
        assert e.value.args[0] == 'List is empty therefor index will be invalid'

class TestIsEnumName:

    def test_with_correct_enum(self):
        assert is_enum_name(Enum('Colors', 'RED'), 'RED')

    def test_with_empty_enum(self):
        assert not is_enum_name(Enum('Colors', ''), 'RED')

    def test_with_argument_different_than(self, enumerator='Enum'):
        with pytest.raises(TypeError) as e:
            is_enum_name(enumerator, 'RED')
        assert e.value.args[0] == "Object is not an Enum"

    def test_with_valid_enum_but_invalid_name(self):
        with pytest.raises(TypeError) as e:
            is_enum_name(Enum('Colors', 'RED'), 255)
        assert e.value.args[0] == "Name is not a string"
