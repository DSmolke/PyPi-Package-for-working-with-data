import pytest

from smolke_data.smolke_data.common.validator.dictionary import is_dict_structure_correct, are_keys_in_dict


class TestIsDictStructureCorrect:
    def test_when_valid_dict(self):
        assert is_dict_structure_correct({'A': 1, "B": 1}, 'DATA', {'A', 'B'})

    def test_when_invalid_data(self):
        with pytest.raises(TypeError) as e:
            is_dict_structure_correct([1, 2, 3], 'DATA', {'A', 'B'})
        assert e.value.args[0] == f"Invalid DATA type"

    def test_when_empty_data(self):
        with pytest.raises(ValueError) as e:
            is_dict_structure_correct({}, 'DATA', {'A', 'B'})
        assert e.value.args[0] == f"DATA cannot be an empty dict"

    def test_when_key_not_matching(self):
        with pytest.raises(KeyError) as e:
            is_dict_structure_correct({'A': 1, "B": 1}, 'DATA', {'A', 'B', 'C'})
        assert e.value.args[0] == f"DATA is not valid due to different keys than desired"

class TestAreKeysInDict:
    def test_when_expressions_are_keys(self):
        assert are_keys_in_dict({'a', 'b'}, {'a': 1, 'b': 2})

    def test_when_expressions_are_not_keys(self):
        assert not are_keys_in_dict({'a', 'b'}, {'a': 1})
