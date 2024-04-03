#!/usr/bin/python3
""" caching system """
BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """caching system"""

    def put(self, key, item):
        """caching system"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """caching system"""
        return self.cache_data.get(key)
