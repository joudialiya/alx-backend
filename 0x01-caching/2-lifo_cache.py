#!/usr/bin/python3
""" BaseCaching module
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """FIFO cache context class"""
    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return
        keys = list(self.cache_data.keys())
        # if the key already exists
        # we update it
        if key in keys:
            self.cache_data[key] = item
            return
        # else we add a new one, taking into account
        # the MAX_ITEMS
        if len(self.cache_data) < self.MAX_ITEMS:
            self.cache_data[key] = item
            return

        print("DISCARD: {}".format(keys[-1]))
        self.cache_data.pop(keys[-1])
        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
