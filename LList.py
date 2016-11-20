class node:
    def __init__ (self,data):
        self.data=data
        self.next=None
        self.prev=None

class linkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    def addNode(self,val):
        newNode=node(val)
        if self.head==None:
            self.head=newNode
        else:
            cur=self.head
            while cur.next!=None:
                cur=cur.next
            cur.next=newNode
            newNode.prev=cur

    def delNode(self,val):
        if self.head==None:
            return 
        else:
            cur=self.head
            while cur!=None and cur.data!=val :
                cur=cur.next
            if cur!=None:
                if cur.next==None:
                    cur=None
                else:
                    cur.next.prev=cur.prev
                    cur.prev.next=cur.next
            else:
                return

    def printll(self):
        if self.head==None:
            return
        else:
            x=[]
            cur=self.head
            while cur!=None:
                x.append(cur.data)
                cur=cur.next
            print x              

    def search(self,val):
        if self.head!=None:
            cur=self.head
            while cur!=None and cur.data!=val:
                cur=cur.next
            if cur!=None:

                print "True"
            else:
                print "False"
                
        
        


ll=linkedList()
ll.addNode(20)
ll.addNode(12)
ll.addNode(34)
ll.addNode(23)
ll.addNode(9)
ll.addNode(43)
ll.addNode(37)
ll.delNode(37)
ll.delNode(63)
ll.delNode(43)
ll.printll()

ll.search(12)
ll.search(21)


            
