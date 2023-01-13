import re

def matches_regex(expression: str, regex: str) -> bool:
    """
    :param expression: valid string
    :param regex: valid string pattern
    :return: if expression matches pattern
    """
    if not isinstance(expression, str):
        raise TypeError(f"Invalid expression type: {type(expression)}")
    if not isinstance(regex, str):
        raise TypeError(f"Invalid regex type: {type(regex)}")
    return re.match(regex, expression)

def is_default_isoformat(expression: str) -> bool:
    """
    checks if expression is valid isoformat string
    :param expression: any string
    :return: expression match isoformat regex
    """
    if not isinstance(expression, str):
        raise TypeError('Expression should be string')
    return True if re.match(r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}[+-]\d{2}:\d{2}$', expression) else False
