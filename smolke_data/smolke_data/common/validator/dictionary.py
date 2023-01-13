from typing import Any


def is_dict_structure_correct(data: dict, data_name: str, desired_keys: set[str]) -> bool:
    """
    Checks if common dict has same names of keys as desired_keys argument
    :param data: dict needs to be checked
    :param data_name: dict name
    :param desired_keys: keys that we expect to be in checked dict
    :return:
    """
    if not isinstance(data, dict):
        raise TypeError(f'Invalid {data_name} type')
    if data == {}:
        raise ValueError(f'{data_name} cannot be an empty dict')
    if desired_keys != set(data.keys()):
        raise KeyError(f'{data_name} is not valid due to different keys than desired')
    return True

def are_keys_in_dict(data_keys: set, data: dict[str, Any]) -> bool:
    """ Checks if provided set of expressions are dictionary keys"""
    return data_keys == set(data.keys())
