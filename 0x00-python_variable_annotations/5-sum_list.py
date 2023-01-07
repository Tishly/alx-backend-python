#!/usr/bin/env python3
from typing import List
"""
An annotated function
"""


def sum_list(input_list: List[float]) -> float:
    """
    A function that returns the sum of a list
    """
    sum1 = 0.00
    for num in input_list:
        sum1 = sum1 + num
    return sum1
