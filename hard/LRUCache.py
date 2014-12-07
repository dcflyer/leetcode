# -*- coding: utf-8 -*-
"""
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and set.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
set(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

@author: Dennis
"""

import collections
class LRUCache:
    
    # @param capacity, an integer
    def __init__(self, capacity):
        LRUCache.dict = collections.OrderedDict()
        LRUCache.capacity = capacity
        LRUCache.num = 0

    # @return an integer
    def get(self, key):
        try:
            value = LRUCache.dict[key]
            del LRUCache.dict[key]
            LRUCache.dict[key] = value
            return value
        except:
            return -1

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        try:
            del LRUCache.dict[key]
            LRUCache.dict[key] = value
            return
        except:
            if LRUCache.num == LRUCache.capacity:
                LRUCache.dict.popitem(last = False)
                LRUCache.num -= 1
            LRUCache.dict[key] = value
            LRUCache.num += 1
        return
                
        