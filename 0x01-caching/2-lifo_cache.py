#!/usr/bin/python3
""" caching system  """
BaseCaching = __import__("base_caching").BaseCaching


class LIFOCache(BaseCaching):
    """caching system """

    def __init__(self):
        """caching system """
        super().__init__()

    def put(self, key, item):
        """caching system """
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                temp = list(self.cache_data.keys())[-1]
                self.cache_data.pop(temp)
                print("DISCARD: {}".format(temp))
            self.cache_data[key] = item

    def get(self, key):
        """caching system """
        return self.cache_data.get(key)
