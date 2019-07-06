# https://leetcode.com/problems/lru-cache/

class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class DoubleyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def __iter__(self):
        node_ptr = self.head
        for _ in range(self.count):
            yield node_ptr.value
            node_ptr = node_ptr.next

    def __len__(self):
        return self.count

    def append(self, node):
        if self.count == 0:
            self.head = node
            self.tail = self.head
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.count += 1

    def shift_node_to_tail(self, node):
        if node.next is None:
            return
        node.next.prev = node.prev
        
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next

        node.prev = self.tail
        node.next = None
        self.tail.next = node
        self.tail = node


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.node_map = {}
        self.cache = DoubleyLinkedList()

    def get(self, key: int) -> int:
        if key in self.node_map:
            self.cache.shift_node_to_tail(self.node_map[key])
            return self.node_map[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.node_map:
            self._update_existing_node(key, value)
        else:
            if len(self.cache) < self.capacity:
                self._add_new_node(key, value)
            else:
                self._replace_least_recently_used_node(key, value)

    def _add_new_node(self, key, value):
        self.node_map[key] = ListNode(key, value)
        self.cache.append(self.node_map[key])

    def _update_existing_node(self, key, value):
        self.node_map[key].value = value
        self.cache.shift_node_to_tail(self.node_map[key])

    def _replace_least_recently_used_node(self, key, value):
        least_recently_used_node = self.cache.head
        del self.node_map[least_recently_used_node.key]

        least_recently_used_node.key = key
        least_recently_used_node.value = value
        
        self.node_map[key] = least_recently_used_node
        self.cache.shift_node_to_tail(least_recently_used_node)