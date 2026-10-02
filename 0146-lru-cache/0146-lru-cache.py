class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache(object):

    def __init__(self, capacity):
        self.cap = capacity
        self.cache = {}   # key -> node

        # left = LRU
        # right = MRU
        self.left = Node(0, 0)
        self.right = Node(0, 0)

        self.left.next = self.right
        self.right.prev = self.left

    # Remove a node from the linked list
    def remove(self, node):
        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev

    # Insert node just before right (MRU position)
    def insert(self, node):
        prev = self.right.prev
        nxt = self.right

        prev.next = node
        node.prev = prev

        node.next = nxt
        nxt.prev = node

    def get(self, key):

        if key in self.cache:

            node = self.cache[key]

            # It was just accessed, so make it MRU
            self.remove(node)
            self.insert(node)

            return node.val

        return -1

    def put(self, key, value):

        if key in self.cache:
            # Remove old node
            self.remove(self.cache[key])

        # Create new node
        node = Node(key, value)

        # Store it in hashmap
        self.cache[key] = node

        # Make it MRU
        self.insert(node)

        # Capacity exceeded
        if len(self.cache) > self.cap:

            # LRU node is immediately after left
            lru = self.left.next

            self.remove(lru)

            # Remove from hashmap
            del self.cache[lru.key]