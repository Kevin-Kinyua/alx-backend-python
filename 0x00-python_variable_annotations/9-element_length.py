#!/usr/bin/env python3
"""Annotate the below function’s parameters and return
values with the appropriate types

def element_length(lst):
    return [(i, len(i)) for i in lst]

{'lst': typing.Iterable[typing.Sequence], 'return': \
    typing.List[typing.Tuple[typing.Sequence, int]]}
"""


import typing


def safe_first_element(lst: typing.Sequence[typing.Any]) -> \
        typing.Union[typing.Any, None]:
    """Duck-typed annotation"""
    if lst:
        return lst[0]
    else:
        return None
