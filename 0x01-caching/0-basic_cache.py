#!/usr/bin/env python3


"""
    Task 0: Basic Dictionary
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
        A class `BasicCache` inherits from `BaseCache`
        and is a caching systems
    """

    def put(self, key, item):
        """
            assign to the dictionary `self.cache_data` the
            `item` value for the key `key`
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        returns the value in `self.cache_data` linked to `key`
        """
        return self.cache_data.get(key, None)
