class Node:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
        

class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next,self.tail.prev = self.tail,self.head
        self.head.prev, self.tail.next = None,None
        self.cap = capacity
        self.locs = {}
    def remove(self,node):
        p,n = node.prev,node.next
        p.next = n
        n.prev = p

    def insert(self,node):
        aft = self.head.next
        self.head.next = node
        aft.prev = node
        node.next = aft
        node.prev = self.head



    def get(self, key: int) -> int:
        if key in self.locs:
            self.remove(self.locs[key])
            self.insert(self.locs[key])
            return self.locs[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if len(self.locs) >= self.cap and key not in self.locs:
            rem = self.tail.prev
            self.remove(rem)
            del self.locs[rem.key]
        ins = Node(key,value)
        if key in self.locs:
            self.remove(self.locs[key])
        self.locs[key] = ins
        self.insert(ins)
