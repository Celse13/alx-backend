#!/usr/bin/env python3
"""implementation of the simple pagination
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Pagination by the index
    """
    return ((page - 1) * page_size, page * page_size)
