#!/usr/bin/python3
""" Caching """
BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """ BaseCache class """

    def put(self, key, item):
        """ add an item in a cache"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key """
        return self.cache_data[key]
