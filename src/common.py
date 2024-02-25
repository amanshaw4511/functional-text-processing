import sys
from typing import Iterable, Optional


def input_lines() -> Iterable[str]:
    return map(str.strip, sys.stdin)


def print_lines(lines: Iterable):
    for line in lines:
        print(line)


def input_lines_with_type(arg_n: Optional[int] = 2) -> Iterable[str]:
    if len(sys.argv) == arg_n + 1:
        return map(get_type_fn(sys.argv[arg_n]), input_lines())
    return input_lines()


def get_type_fn(type_code: str):
    if type_code == 'i' or type_code == 'int':
        return int
    elif type_code == 'f' or type_code == 'float':
        return float
    else:
        raise Exception(f"invalid type code {type_code}")
