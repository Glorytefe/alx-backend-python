#!/usr/bin/env python3

"""complex types - mixed list"""
from typing import List, Union


def sum_list(mxd_lst: List[Union[float, int]]) -> float:
    """returns sum of mxd_lst"""
    return sum(mxd_lst)
