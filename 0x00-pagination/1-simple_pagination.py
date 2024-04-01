#!/usr/bin/env python3
""" Implementation of simple pagination"""


def index_range(page, page_size):
    """ Pagination by the index"""
    starting_index = (page - 1) * page_size
    ending_index = page * page_size
    return starting_index, ending_index
  
