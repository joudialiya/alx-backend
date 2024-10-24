#!/usr/bin/env python3
"""Helper module 1"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Returns a tuple of the start and end
    index of items of the 1-indexed page"""
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
