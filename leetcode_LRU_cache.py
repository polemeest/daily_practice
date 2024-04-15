class LRUCache:
    class Node():
        def __init__(self, key: int, value: int) -> None:
            self.key = key
            self.val = value
            self.prev = self.next = None

    def __init__(self, capacity: int):
        self.cache = dict()
        self.capacity = capacity
        self.start, self.end = self.Node(0, 0), self.Node(0, 0)
        self.start.next, self.end.prev = self.end, self.start

    def insert(self, node):
        prev = self.end.prev
        prev.next = self.end.prev = node
        node.prev, node.next = prev, self.end

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def get(self, key: int) -> int:
        value = self.cache.get(key, None)
        if value:
            self.remove(value)
            self.insert(value)
            return value.val
        return -1

    def put(self, key: int, value: int) -> None:
        if self.cache.get(key):
            self.remove(self.cache[key])
        self.cache[key] = self.Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.start.next
            self.remove(lru)
            del self.cache[lru.key]
