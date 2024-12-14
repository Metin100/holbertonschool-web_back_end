#!/usr/bin/env python3
"""
file to read from csv
"""
import csv
import math
from typing import List
index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Getting page for index
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()

        if start_index >= len(dataset):
            return []
        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Function of dictionary
        """
        datas = self.dataset()
        data = self.get_page(page, page_size)

        if page + 1 < len(datas):
            next_page = page + 1
        else:
            next_page = 'None'

        if page - 1 > 0:
            prev_page = page - 1
        else:
            prev_page = 'None'

        return {
            'page_size': page_size,
            'page': page,
            'data': data,
            'next_page': page + 1 if page + 1 < len(datas) else 'None',
            'prev_page': page - 1 if page - 1 > 0 else 'None',
            'total_pages': len(datas)
        }
