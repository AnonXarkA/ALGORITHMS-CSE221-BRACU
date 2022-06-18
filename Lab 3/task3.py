fdata=open('E:\Study Brac\Spring 22\CSE 221\LABs\Lab 3\input1.txt')
file=open('E:\Study Brac\Spring 22\CSE 221\LABs\Lab 3\output3.txt','w')
di = int(fdata.readline())
file.write('Places: ')

arr = []
for x in range(di):
    r = fdata.readline().split()
    arr.append(r)

class graphbuild:
    def __init__(self,new_node):
        self.new_node =new_node
        self.adj = {}
        for x in self.new_node:
            self.adj[x] = []
    def last(self,x,y):
        self.adj[str(x)].append(str(y))

    def DFS_VISIT(self,x,places,endpoints):
        places.add(x)
        if endpoints in places:
            return
        #print(x,end=' ')
        file.write(x + " ")
        for y in self.adj[x]:
                if y not in places:
                    self.DFS_VISIT(y,places,endpoints)
    def DFS(self,endpoints,start='1'):
        places=set()
        self.DFS_VISIT(start,places,endpoints)
        file.write(endpoints)
node=[]
for x in arr:
    node.append(str(x[0]))
new_graph= graphbuild(node)
for y in arr:
    for z in range(1,len(y)):
        new_graph.last(y[0],y[z])
new_graph.DFS('12')