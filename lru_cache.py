class LRUCache:
    class Node:
        def __init__(self, k=None, v=None):
            self.key=k
            self.value=v
            self.prev=None
            self.next=None
    
    class DLList:
        def __init__(self, capacity):
            self.size=0
            self.head=LRUCache.Node()
            self.tail=LRUCache.Node()
            self.head.prev=self.tail
            self.tail.next=self.head
            self.capacity=capacity
        
        def get(self, k, cache):
            n = cache.get(k, None)
            if n:
                if n.next!=self.head:
                    n.prev.next=n.next
                    n.next.prev=n.prev
                    n.prev=self.head.prev
                    n.next=self.head
                    n.prev.next=n
                    self.head.prev=n

                return n.value
            return -1
        
        def add(self, k, v, cache):
            n=cache.get(k, False)
            if n:
                n.value=v
                if n.next!=self.head:
                    n.prev.next=n.next
                    n.next.prev=n.prev
                    n.prev=self.head.prev
                    n.next=self.head
                    n.prev.next=n
                    self.head.prev=n

            else:
                node=LRUCache.Node(k,v)
                if self.size >= self.capacity:
                    n=self.tail.next
                    self.tail.next=self.tail.next.next
                    self.tail.next.prev=self.tail
                    self.size-=1
                    cache.pop(n.key, None)
                    del n
                
                cache[k]=node
                node.next=self.head
                node.prev=self.head.prev
                self.head.prev.next=node
                self.head.prev=node
                self.size+=1

    def __init__(self, capacity: int):
        self.cache=dict()
        self.dllist=self.DLList(capacity)

    def get(self, key: int) -> int:
        return self.dllist.get(key, self.cache)

    def put(self, key: int, value: int) -> None:
        self.dllist.add(key, value, self.cache)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)