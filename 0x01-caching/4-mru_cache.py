#!/usr/bin/python3
""" Caching System """
BaseCaching = __import__("base_caching").BaseCaching


class MRUCache(BaseCaching):
    def __init__(self):
        super().__init__()
        self.mru_key = []

    def put(self, key, item):
        """ Put an item in cache"""
        if key is not None and item is not None:
            if key in self.cache_data:
                del self.cache_data[key]
            elif len(self.cache_data) >= self.MAX_ITEMS:
                del self.cache_data[self.mru_key]
                print(f"DISCARD: {self.mru_key}")
            self.cache_data[key] = item
            self.mru_key = key

    def get(self, key):
        """ Get an item by key from cache"""
        if key is None or key not in self.cache_data:
            return None
        self.mru_key = key
        return self.cache_data[key]
