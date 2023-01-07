#!/usr/bin/env python3

"""
An annotated function
"""


def sum_list(input_list: list[float]) -> float:
    """
    A function that returns th sum of a list
    """
    sum1 = 0.00
    for num in input_list:
        sum1 = sum1 + num
    return sum1
