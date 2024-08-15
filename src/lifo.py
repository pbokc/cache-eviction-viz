from cache import Cache

class LIFO(Cache):
    """
    Simulates a cache with LIFO eviction. 
    
    Does not prevent duplicates.
    """
    def __init__(self, cache_size=10):
        if cache_size < 1: 
            raise ValueError("Given cache size smaller than 1")
        Cache.__init__(self, cache_size)
        
        self.last_idx = cache_size - 1 # starts with full cache of size cache_size

    def get(self, element: str) -> bool:
        """
        Doesn't return if an element is in the cache - just adds it
        to the cache and evicts LIFO when the cache is full

        Returns true if element was successfully added, false if not. 
        """
        if len(self.cache) == 0 or not element or element == "": 
            return False 

        if self.last_idx < (self.cache_size - 1):
            self.last_idx += 1        
        self.cache[self.last_idx] = element        

        return True
    
    def flush(self):
        """
        Clears the cache of all elements. Empty string is used as a 
        placeholder value and adding empty strings to the cache is 
        not allowed by get(). 
        """
        self.cache = ["" for _ in range(self.cache_size)]
