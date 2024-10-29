#!/usr/bin/python3
""" BaseCaching module
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """FIFO cache context class"""
    def __init__(self):
        """
        The construction
        """
        super().__init__()
        # we keep tack of the timing usage
        self.usage = {}
        self.curent_usage_rank = 0

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
            self.usage[key] = self.curent_usage_rank
            self.curent_usage_rank += 1
            return
        # else we add a new one, taking into account
        # the MAX_ITEMS
        if len(self.cache_data) < self.MAX_ITEMS:
            self.cache_data[key] = item
            self.usage[key] = self.curent_usage_rank
            self.curent_usage_rank += 1
            return
        key_to_remove, _ = min(
            self.usage.items(),
            key=lambda entry: entry[1])
        print("DISCARD: {}".format(key_to_remove))
        self.cache_data.pop(key_to_remove)
        self.usage.pop(key_to_remove)

        self.cache_data[key] = item
        self.usage[key] = self.curent_usage_rank
        self.curent_usage_rank += 1

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data.keys():
            return None
        self.usage[key] = self.curent_usage_rank
        self.curent_usage_rank += 1
        return self.cache_data[key]
