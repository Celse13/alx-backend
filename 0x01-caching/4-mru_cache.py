#!/usr/bin/python3
""" Caching System """
BaseCaching = __import__("base_caching").BaseCaching


class MRUCache(BaseCaching):
    """Constructor"""

    def __init__(self):
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """Add an item in cache"""
        if key is not None and item is not None:
            if key in self.cache_data:
                self.keys.remove(key)
            elif len(self.keys) >= self.MAX_ITEMS:
                discarded = self.keys.pop(0)
                del self.cache_data[discarded]
                print("DISCARD: {}".format(discarded))
            self.cache_data[key] = item
            self.keys.append(key)

    def get(self, key):
        """Get an item by key from the cache"""
        if key is not None and key in self.cache_data:
            self.keys.remove(key)
            self.keys.append(key)
            return self.cache_data.get(key)
        return None
