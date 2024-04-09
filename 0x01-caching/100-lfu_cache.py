#!/usr/bin/env python3
""" LFU Caching module """
from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """ LFU Caching class"""
    def __init__(self):
        """init method"""
        super().__init__()
        self.cache_data = OrderedDict()
        self.counts = {}
        self.least_count = None

    def put(self, key, value):
        """adds key value pair to the cache"""
        if key is None or value is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = value
            self.counts[key] += 1
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                self.remove_least_used()
            self.cache_data[key] = value
            self.counts[key] = 1

        self.update_least_used()

    def get(self, key):
        """gets the value of key from cache"""
        if key is None or key not in self.cache_data:
            return None
        self.counts[key] += 1
        self.update_least_used()
        return self.cache_data[key]

    def remove_least_used(self):
        """evicts the least frequently used item from cache"""
        if not self.cache_data:
            return

        least_used_count = min(self.counts.values())
        least_used_keys = [k for k, v in self.counts.items()
                           if v == least_used_count]

        if len(least_used_keys) > 1:
            for k in self.cache_data:
                if k in least_used_keys:
                    least_used_key = k
                    break
        else:
            least_used_key = least_used_keys[0]

        print(f'DISCARD: {least_used_key}')
        del self.cache_data[least_used_key]
        del self.counts[least_used_key]

    def update_least_used(self):
        """updates the least frequently used item in cache"""
        least_used_count = min(self.counts.values())
        self.least_count = [k for k, v in self.counts.items()
                            if v == least_used_count]
