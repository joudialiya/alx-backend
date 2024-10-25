#!/usr/bin/env python3
"""Helper module 1"""
import csv
import math
from typing import List, Tuple, Dict


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Returns a tuple of the start and
    end index of items of the 1-indexed page"""
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Paginate the dataset"""
        assert type(page) is int
        assert type(page_size) is int
        assert page > 0
        assert page_size > 0
        (start, end) = index_range(page, page_size)
        return self.dataset()[start: end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Returne page with metadata"""
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)
        res = {}
        res['page_size'] = len(data)
        res['page'] = page
        res['data'] = data
        res['next_page'] = page + 1 if page + 1 <= total_pages else None
        res['prev_page'] = page - 1 if (page - 1 != 0) else None
        res['total_pages'] = total_pages
        return res
