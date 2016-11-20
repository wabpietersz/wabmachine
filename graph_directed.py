class node():

    def __init__(self,data):
        self.data=data
        self.adj=[]



class d_graph ():

    def __init__(self):
        self.lst=[]

    def addv(self,n1,n2):
        flag1=False
        flag2=False
        if self.lst != []:
            for i in self.lst:
                if i.data==n1:   ##n1 founded in the array
                    flag1=True
                    t1=i
                if i.data==n2:   ##n2 founded in the array
                    flag2=True
                    t2=i
                if flag1==True and flag2==True:  #both founded
                    break

            if flag1==False:
                n=node(n1)
                n.adj.append(n2)
                self.lst.append(n)
            else:
                t1.adj.append(n2)

            if flag2==False:
                n=node(n2)
                self.lst.append(n)


        else:
            n=node(n1)
            n.adj.append(n2)
            self.lst.append(n)
            n=node(n2)
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

        
            
        

my=d_graph()
my.addv(1,2)
my.addv(5,1)
my.addv(5,2)
my.addv(4,5)
my.addv(4,2)
my.addv(3,4)
my.addv(3,2)
##my.remove(1)
my.printg()

            
