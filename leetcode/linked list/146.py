class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity

        self.left, self.right = Node(0, 0), Node(0, 0)
        self.values = {
        }

        self.left.next, self.right.prev = self.right, self.left

    # REMOVE AT LEFT - MEANING LEAST RECENTLY USED CACHE IS REMOVED
    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev

    # INSERT AT RIGHT - MEANING MOST RECENT CACHE IS UPDATED
    def insert(self, node):
        prev, next = self.right.prev, self.right
        prev.next = next.prev = node
        node.next, node.prev = next, prev

    def get(self, key: int) -> int:
        if key in self.values:
            self.remove(self.values[key])
            self.insert(self.values[key])
            
            return self.values[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.values:
            self.remove(self.values[key])

        self.values[key] = Node(key, value)
        self.insert(self.values[key]) # UPDATING MOST RECENTLY USED

        if len(self.values) > self.capacity:
            least_recently_used = self.left.next # USING POINTER TO POINT TO NEXT
            
            self.remove(least_recently_used)
            del self.values[least_recently_used[key]]




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)