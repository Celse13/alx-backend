#!/usr/bin/env python3
""" Implementation of simple pagination"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ Pagination by the index"""
    starting_index = (page - 1) * page_size
    ending_index = page * page_size
    return (starting_index, ending_index)
