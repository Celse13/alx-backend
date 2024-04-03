#!/usr/bin/python3
"""  caching system  """
BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """ caching system """

    def __init__(self):
        """ caching system """
        super().__init__()

    def put(self, key, item):
        """ caching system """
        if key is not None and item is not None:
            while len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                removed = list(self.cache_data.keys())[0]
                self.cache_data.pop(removed)
                print("DISCARD: {}".format(removed))
            self.cache_data[key] = item

    def get(self, key):
        """ caching system """
        return self.cache_data.get(key)
