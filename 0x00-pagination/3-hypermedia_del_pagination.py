#!/usr/bin/env python3
""" Implementation of simple pagination """
import csv
import math
from typing import List, Dict


class Server:
    """ This class will aid in pagination of the server"""

    CSV_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """ Constructor for the class"""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """ Storing pagination data"""
        if self.__dataset is None:
            with open(self.CSV_FILE) as file:
                read_from_file = csv.reader(file)
                dataset = [row for row in read_from_file]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ Getting the page """
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0
        starting_page, ending_page = self.index_range(page, page_size)
        return self.dataset()[starting_page:ending_page]

    def index_range(self, page: int, page_size: int) -> Tuple[int, int]:
        """ Pagination by the index"""
        starting_index = (page - 1) * page_size
        ending_index = page * page_size
        return (starting_index, ending_index)

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """Dictionary of pagination data"""
        data = self.get_page(page, page_size)
        all_pages = math.ceil(len(self.dataset()) / page_size)
        return {
            "page_size": page_size,
            "page": page,
            "data": data,
            "next_page": page + 1 if page < all_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": all_pages,
        }
