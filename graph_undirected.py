class node():

    def __init__(self,data):
        self.data=data
        self.adj=[]



class un_graph ():

    def __init__(self):
        self.lst=[]

    def addv(self,n1,n2):
        flag1=False
        flag2=False
        if self.lst != []:
            for i in self.lst:
                if i.data==n1:
                    flag1=True
                    t1=i
                if i.data==n2:
                    flag2=True
                    t2=i
                if flag1==True and flag2==True:
                    break

            if flag1==False:
                n=node(n1)
                n.adj.append(n2)
                self.lst.append(n)
            else:
                t1.adj.append(n2)

            if flag2==False:
                n=node(n2)
                n.adj.append(n1)
                self.lst.append(n)
            else:
                t2.adj.append(n1)    

        else:
            n=node(n1)
            n.adj.append(n2)
            self.lst.append(n)
            n=node(n2)
            n.adj.append(n1)
            self.lst.append(n)

    def remove(self,n):
        if self.lst != []:
            for i in self.lst:
                if i.data==n:
                    self.lst.remove(i)
            
            for i in self.lst:           
                    for j in i.adj:
                        if j==n:
                            i.adj.remove(n)
                    
    def printg(self):
        for i in self.lst:
            print i.data,
            print i.adj
#finding the path method!!
    def fpath(self,n1,n2):
        if self.lst != []:
            for i in self.lst:
                if i.data==n1:
                    if n2 in i.adj: #only if the vertices are adjacent.
                        print n1,n2
        
            
        

my=un_graph()
my.addv(1,2)
my.addv(1,6)
my.addv(2,6)
my.addv(6,3)
my.addv(6,5)
my.addv(6,4)
##my.remove(1)
my.printg()
my.fpath(1,2)
            
