#!/usr/bin/python3
""" Caching System """
from collections import Counter
BaseCaching = __import__("base_caching").BaseCaching


class LFUCache(BaseCaching):
    def __init__(self):
        super().__init__()
        self.frequency = Counter()
        self.timestamp = {}

    def put(self, key, item):
        if key is not None and item is not None:
            if len(
                    self.cache_data) >= self.MAX_ITEMS and key not in self.cache_data:
                least_freq = min(self.frequency.values())
                least_freq_keys = [
                    k for k, v in self.frequency.items() if v == least_freq]
                if len(least_freq_keys) > 1:
                    lru_key = min(least_freq_keys, key=self.timestamp.get)
                else:
                    lru_key = least_freq_keys[0]
                del self.cache_data[lru_key]
                del self.frequency[lru_key]
                del self.timestamp[lru_key]
                print(f"DISCARD: {lru_key}")
            self.cache_data[key] = item
            self.frequency[key] += 1
            self.timestamp[key] = len(self.timestamp)

    def get(self, key):
        if key is None or key not in self.cache_data:
            return None
        self.frequency[key] += 1
        self.timestamp[key] = len(self.timestamp)
        return self.cache_data[key]
