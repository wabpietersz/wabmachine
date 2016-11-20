class Queue:
    def __init__(self):
        self.qlist=[]

    def isEmpty(self):
        return len(self.qlist)==0

    def length(self):
        return len(self.qlist)

    def enqueue(self,item):
        self.qlist.append(item)

    def dequeue(self):
        self.qlist.pop(0)

q=Queue()
print q.isEmpty()
q.enqueue(3)
q.enqueue(4)
q.enqueue(7)
q.enqueue(1)
q.enqueue(10)
q.enqueue(2)
q.enqueue(6)
print q.length()
q.dequeue()
q.dequeue()
print q.length()
print q.qlist
