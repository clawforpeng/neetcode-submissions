class Cache:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        dummy = Cache(-1, -1)
        self.start: Cache = dummy # dummy head
        self.end: Cache = dummy

    def get(self, key: int) -> int:
        if key in self.cache:
            cache = self.cache[key]
            if cache != self.end:
                cache.prev.next = cache.next
                cache.next.prev = cache.prev

                cache.prev = self.end
                self.end.next = cache
                cache.next = None

                self.end = cache

            return self.cache[key].value
        else:
            return -1
    
    def evict(self):
        cache = self.start.next
        self.cache.pop(cache.key)

        self.start.next = cache.next
        if cache.next:
            cache.next.prev = self.start
        else:
            self.end = self.start
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            cache = self.cache[key]
            cache.value = value

            if cache != self.end:
                cache.prev.next = cache.next
                cache.next.prev = cache.prev

                cache.prev = self.end
                cache.next = None
                self.end.next = cache
                self.end = cache

        else:
            if len(self.cache) == self.capacity:
                self.evict()

            newCache = Cache(key, value)
            newCache.prev = self.end
            self.end.next = newCache
            newCache.next = None

            self.cache[key] = newCache
            self.end = newCache


