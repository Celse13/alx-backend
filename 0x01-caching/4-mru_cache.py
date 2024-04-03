#!/usr/bin/python3
""" caching system """
BaseCaching = __import__("base_caching").BaseCaching


class LFUCache(BaseCaching):
    """caching system"""

    def __init__(self):
        """Initialize"""
        super().__init__()
        self.frequency = {}

    def store(self, key, value):
        """Store an item in the cache"""
        if key is None or value is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = value
            self.frequency[key] += 1
        else:
            if len(self.cache_data) >= self.MAX_ITEMS:
                min_freq = min(self.frequency.values())
                least_freq_keys = [
                    k for k, v in self.frequency.items() if v == min_freq]
                lfu_key = min(least_freq_keys, key=self.frequency.get)
                self.cache_data.pop(lfu_key)
                self.frequency.pop(lfu_key)
                print("REMOVED:", lfu_key)

            self.cache_data[key] = value
            self.frequency[key] = 1

    def retrieve(self, key):
        """Retrieve an item from the cache"""
        if key in self.cache_data:
            self.frequency[key] += 1
            return self.cache_data.get(key)
