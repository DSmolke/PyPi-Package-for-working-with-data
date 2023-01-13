import enum
from decimal import Decimal
from enum import Enum
from typing import Any


def first_elements_having_same_value(elements: list[Any]) -> list[int | float | Decimal]:
    """
    Can be used to extract the highest or the lowest occurrences of same value objects
    :param elements: list of elements sorted in ascending or descending order
    :return: list containing first few elements having same value
    """
    if isinstance(elements, list) is False:
        raise TypeError("Argument named 'elements' has invalid type")

    if not elements:
        return []
    desired_type = type(elements[0])
    if len(elements) != len([element for element in elements if isinstance(element, desired_type)]):
        raise TypeError("Elements list containing invalid type elements")
    if (l := len(elements)) == 1:
        return elements

    idx = 1
    for i in range(1, l):
        if elements[i] == elements[i - 1]:
            idx += 1
        else:
            return elements[:idx]
    return elements

def get_n_top_elements_of_most_common_list(elements: list[tuple[Any, Any]]) -> int:
    """
    This function purpose is to help with getting multiple values from Counters.
    Best example is when we have set of [1, 2, 3, 3]. We have 2 highest value, so we want to get list containing them
    :param elements: list that is what Counter.most_common() method returns. Example -> [(2,3), (3,3), (1,1)]
    :return: index of last value which is in most common group
    """
    if len(elements) == 0:
        raise IndexError("List is empty therefor index will be invalid")
    n = 1
    for i in range(1, len(elements)):
        if elements[i][1] == elements[i - 1][1]:
            n += 1
        else:
            return n
    return n

# ENUM
def is_enum_name(enum_: Enum, name: str) -> bool:
    """
    :param enum_: enum object that will be checked
    :param name: name that we are anticipating is an enum element name
    :return: bool checking if name is part of enum
    """
    if not isinstance(enum_, enum.EnumType):
        raise TypeError("Object is not an Enum")
    if not isinstance(name, str):
        raise TypeError("Name is not a string")
    return name in [element.name for element in enum_]
