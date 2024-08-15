from abc import ABC, abstractmethod
import random

class Cache(ABC): 
    """
    Template class for a Cache
    """
    def __init__(self, cache_size=10):
        """
        Initialize cache with random integers
        """
        self.cache = [random.randint(0, 99) for i in range(cache_size)]
        self.cache_size = cache_size

    @abstractmethod
    def get(self, element: str) -> bool: 
        pass

    @abstractmethod
    def flush(self):
        pass
    