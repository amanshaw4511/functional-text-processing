import sys
from typing import Iterable

def get_lines() -> Iterable[str] :
    return map(str.strip, sys.stdin)

def get_lines_int() -> Iterable[int] :
    return map(int, get_lines())

def get_lines_float() -> Iterable[float] :
    return map(float, get_lines())

def print_lines(lines: Iterable) :
    for line in lines:
        print(line)

def get_lines_of_type(type_code: str) :
    if type_code == 'i' :
        return get_lines_int()
    elif type_code == 'f':
        return get_lines_float()
    else :
        raise Exception(f"invalid type code {type_code}")
