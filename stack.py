class stack:

    def __init__(self):
        self.slist=[]

    def isEmpty(self):
        return len(self.slist)==0

    def push(self,item):
        self.slist.append(item)
        
    def pop(self):
        return self.slist.pop()

    def peek(self):
        return self.slist[len(self.slist)-1]

    def size(self):
        return len(self.slist)

    

s=stack()
print s.isEmpty()
print s.size()
s.push(3)
s.push(1)
s.push(6)
s.push(2)
print s.peek()
print s.size()
s.push(9)
s.push(10)
print s.peek()
s.pop()
print s.peek()
print s.size()
s.push(12)
print s.isEmpty()
print s.slist

        
