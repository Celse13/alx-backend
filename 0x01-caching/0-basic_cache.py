#!/usr/bin/python3
""" Caching """


class BaseCaching:
    """ BaseCaching class """

    def __init__(self):
        """ Constructor """
        self.cache_data = {}


class BasicCache (BaseCaching):
    """ BaseCache class """

    def put(self, key, item):
        """ add an item in a cache"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
