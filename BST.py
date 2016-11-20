class node:

    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
        self.parent=None
        
class BST:

    def __init__(self):
        self.root=None

    def addnode(self,val):
        n=node(val)
        if self.root!=None:
            cur=self.root
            while True:
                if val<cur.data:
                    if cur.left==None:
                        cur.left=n
                        n.parent=cur
                        break
                    else:
                        cur=cur.left
                else:
                    if cur.right==None:
                        cur.right=n
                        n.parent=cur
                        break
                    else:
                        cur=cur.right
                    
        else:
            self.root=n

    def search(self,val):
        n=node(val)
        if self.root!=None:
            cur=self.root
            while True:
                if val<cur.data:
                    if cur.left==None:
                        return False
                    else:
                        cur=cur.left
                elif val>cur.data:
                    if cur.right==None:
                        return False
                    else:
                        cur=cur.right
                else:
                    return True
        else:
            self.root=n

    def preOrder(self):
        self.pret(self.root)

    def pret(self,root):
        if self.root!= None:
            print self.root.data
            self.pret(root.left)
            self.pret(root.right)
        
        


    def delnode(self,val):
        n=node(val)
        if self.root!=None:
            cur=self.root
            while True:
                if val<cur.data:
                    if cur.left==None:
                        return False
                    else:
                        cur=cur.left
                elif val>cur.data:
                    if cur.right==None:
                        return False
                    else:
                        cur=cur.right
                else:
                    x=cur.left
                    if x!=None:
                        while x.right==None:
                            x=x.right
                        cur.data=x.data
                        if x.left!=None:
                            x.parent.right=None
                        else:
                            x.parent.right=x.left
                    else:
                         cur.data=cur.right.data
                         cur.parent.right=cur.right
                         
                    
        else:
            self.root=n



b=BST()
b.addnode(7)
b.addnode(4)
b.addnode(8)
b.addnode(10)
b.addnode(1)
b.addnode(5)
b.preOrder()

