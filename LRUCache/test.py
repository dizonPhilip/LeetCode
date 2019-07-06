import unittest
from lru_cache import LRUCache, ListNode, DoubleyLinkedList

class LRUCacheTest(unittest.TestCase):
    def test_link_list_append_empty(self):
        dlist = DoubleyLinkedList()
        dlist.append(ListNode(1, 2))
        self.assertEqual([2], list(dlist))

    def test_link_list_append(self):
        dlist = DoubleyLinkedList()
        dlist.append(ListNode(1, 2))
        dlist.append(ListNode(3, 4))
        self.assertEqual([2,4], list(dlist))

    def test_link_list_shift_to_tail_from_head(self):
        dlist = DoubleyLinkedList()
        dlist.append(ListNode(1, 2))
        dlist.append(ListNode(3, 4))
        dlist.append(ListNode(5, 6))
        dlist.append(ListNode(7, 8))
        dlist.shift_node_to_tail(dlist.head)
        self.assertEqual([4,6,8,2], list(dlist))

    def test_link_list_shift_to_tail_from_mid(self):
        dlist = DoubleyLinkedList()
        dlist.append(ListNode(1, 2))
        dlist.append(ListNode(3, 4))
        dlist.append(ListNode(5, 6))
        dlist.append(ListNode(7, 8))
        dlist.shift_node_to_tail(dlist.head.next.next)
        self.assertEqual([2,4,8,6], list(dlist))

    def test_link_list_shift_to_tail_from_tail(self):
        dlist = DoubleyLinkedList()
        dlist.append(ListNode(1, 2))
        dlist.append(ListNode(3, 4))
        dlist.append(ListNode(5, 6))
        dlist.shift_node_to_tail(dlist.head.next.next)
        self.assertEqual([2,4,6], list(dlist))


    def test_get_key_does_not_exist(self):
        capacity = 1
        cache = LRUCache(capacity)
        value = cache.get(1)
        self.assertEqual(-1, value)

    def test_get_key_exists(self):
        capacity = 1
        cache = LRUCache(capacity)
        cache.put(1, 3)
        value = cache.get(1)
        self.assertEqual(3, value)

    def test_put_update(self):
        capacity = 1
        cache = LRUCache(capacity)
        cache.put(1, 3)
        cache.put(1, 5)
        value = cache.get(1)
        self.assertEqual(5, value)

    def test_put_hit_capacity_update(self):
        capacity = 2
        cache = LRUCache(capacity)
        cache.put(1, 3)
        cache.put(2, 5)
        cache.put(1, 2)
        value = cache.get(1)
        self.assertEqual(2, value)

    def test_get_expired(self):
        capacity = 2
        cache = LRUCache(capacity)
        cache.put(1, 3)
        cache.put(2, 5)
        cache.get(1)
        cache.put(3, 6)
        value = cache.get(2)
        self.assertEqual(-1, value)

    def test_expired_after_update(self):
        capacity = 2
        cache = LRUCache(capacity)
        cache.put(2, 1)
        cache.put(1, 1)
        cache.put(2, 3)
        cache.put(4, 1)
        value = cache.get(1)
        self.assertEqual(-1, value)
        value = cache.get(2)
        self.assertEqual(3, value)

if __name__ == "__main__":
    unittest.main()