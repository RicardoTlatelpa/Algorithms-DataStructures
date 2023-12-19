'''
Implement an ISBN cache

Create a cache for looking up prices of books identified by 
their isbn. You implement lookup, insert, and remove methods.
Use the least recently used(LRU) policy for cache eviction. If
an ISBN is already present, insert should not change the price,
but it should update that entry to be the most recently used
entry. Lookup should also update that entry to be the most recently
used entry.
'''
import collections
class LRUCache:
    def __init__(self, capacity):
        self._isbn_price_table = collections.OrderedDict()
        self._capacity = capacity
    def lookup(self,isbn):
        if isbn not in self._isbn_price_table:
            return -1
        price = self._isbn_price_table.pop(isbn)
        self._isbn_price_table[isbn] = price
        return price
    def insert(self,isbn,price):
        if isbn in self._isbn_price_table:
            price = self._isbn_price_table.pop(isbn)
        elif self._capacity <= len(self._isbn_price_table):
            self._isbn_price_table.popitem(last=False)
        self._isbn_price_table[isbn] = price
    def erase(self,isbn):
        return self._isbn_price_table.pop(isbn,None) is not None
'''
The time complexity for each lookup is O(1) for the hash table
lookup and O(1) for updating the queue, i.e., O(1) overall
'''
