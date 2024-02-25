import sys
from typing import Iterable, Optional


def input_lines() -> Iterable[str]:
    return map(str.strip, sys.stdin)


def if_arg_else(argv_n: int, default):
    return sys.argv[argv_n] if len(sys.argv) >= argv_n + 1 else default


def if_arg_else_throw(argv_n: int):
    return sys.argv[argv_n]


def if_arg(arg_n: int):
    return len(sys.argv) == arg_n + 1


def get_arg(arg_n: int):
    return sys.argv[arg_n]


def print_lines(lines: Iterable):
    for line in lines:
        print(line)


def input_lines_with_type(arg_n: Optional[int] = None) -> Iterable[str]:
    if arg_n is not None and if_arg(arg_n):
        return map(get_type_fn(get_arg(arg_n)), input_lines())

    return input_lines()


def get_type_fn(type_code: str):
    if type_code == 'i' or type_code == 'int':
        return int
    elif type_code == 'f' or type_code == 'float':
        return float
    else:
        raise Exception(f"invalid type code {type_code}")
